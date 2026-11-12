#!/usr/bin/env python3
"""Build Saikou's public docs: site/docs/*.md into site/public/docs/*.html.

Run from anywhere, whenever the Markdown changes:

    python3 site/tools/build_docs.py           # build, check, write
    python3 site/tools/build_docs.py --check   # build and check only, write nothing

docs/README.md becomes public/docs/index.html (served at /docs/); docs/foo.md becomes
public/docs/foo.html (served at /docs/foo by the Worker's default auto-trailing-slash handling,
which redirects /docs/foo.html and /docs/foo/ to it). The sidebar lists every page in the order
README.md links them, grouped by its "##" sections. public/sitemap.xml (the home page, the
privacy policy and every docs page) and public/robots.txt (which points to it) are written too.

Nothing is written unless every check passes:
  - every internal link and #anchor resolves (checked on the rendered HTML);
  - every page in docs/ is linked from README.md;
  - no HTML comment, em dash or unsupported construct (tables) reaches the output;
  - the forbidden-words check from site/README.md finds nothing (count only, never the words).

Python 3 standard library only. It converts the Markdown subset these pages use: ATX headings,
paragraphs, **bold**, *italic*, `code`, fenced code blocks, ordered and unordered lists with
nesting, [links](x.md#anchor), <autolinks> and blockquotes that start a block.
"""

import argparse
import html
import os
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
DOCS_SRC = SITE / "docs"
PUBLIC = SITE / "public"
DOCS_OUT = PUBLIC / "docs"
# The list lives outside every repository; SAIKOU_FORBIDDEN_WORDS_FILE names it, else the owner's
# checkout keeps it beside this one.
FORBIDDEN_WORDS = Path(os.environ.get("SAIKOU_FORBIDDEN_WORDS_FILE") or SITE.parent / "tools" / "forbidden-words.txt")

HOST = "https://shinsaikou.com"
# The community server, linked beside GitHub in the header and footer (as on public/index.html).
DISCORD = "https://discord.gg/VupfVKYquZ"
# The hand-written pages outside docs/, listed in the sitemap ahead of the docs.
SITE_PAGES = ["/", "/privacy-policy"]
INDEX_PAGE = "README"
EM_DASH = chr(0x2014)
DESCRIPTION_LIMIT = 160
TOC_MINIMUM = 3


class BuildError(Exception):
    pass


def page_url(name):
    return "/docs/" if name == INDEX_PAGE else f"/docs/{name}"


def out_name(name):
    return "index.html" if name == INDEX_PAGE else f"{name}.html"


# ---------------------------------------------------------------------------
# Markdown to HTML

def strip_comments(text):
    """Removes every HTML comment. A line holding only a comment goes entirely, so that a
    comment at the end of a list item or paragraph does not split it."""
    text = re.sub(r"<!--.*?-->", "\x01", text, flags=re.S)
    lines = [line for line in text.split("\n") if line.strip() != "\x01"]
    return "\n".join(lines).replace("\x01", "")


def slugify(text):
    """GitHub's heading anchors: lowercase, drop punctuation, spaces become hyphens."""
    slug = re.sub(r"[^\w\- ]", "", text.strip().lower())
    return slug.replace(" ", "-")


def plain_text(fragment):
    """The visible text of an HTML fragment."""
    return html.unescape(re.sub(r"<[^>]+>", "", fragment))


class Inline:
    """Inline Markdown. Code spans, autolinks and links become placeholders first, so that
    escaping and emphasis never touch their contents."""

    def __init__(self, rewrite_link):
        self.rewrite_link = rewrite_link
        self.store = []

    def _hold(self, fragment):
        self.store.append(fragment)
        return f"\x00{len(self.store) - 1}\x00"

    def render(self, text):
        text = re.sub(
            r"`([^`]+)`",
            lambda m: self._hold(f"<code>{html.escape(m.group(1), quote=False)}</code>"),
            text,
        )
        text = re.sub(
            r"<(https?://[^>\s]+)>",
            lambda m: self._hold(
                f'<a href="{html.escape(m.group(1))}">{html.escape(m.group(1), quote=False)}</a>'
            ),
            text,
        )
        text = re.sub(
            r"\[([^\]]+)\]\(([^)\s]+)\)",
            lambda m: self._hold(
                f'<a href="{html.escape(self.rewrite_link(m.group(2)))}">'
                f"{self._emphasis(m.group(1))}</a>"
            ),
            text,
        )
        return self._restore(self._emphasis(text))

    def _emphasis(self, text):
        text = html.escape(text, quote=False)
        text = re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", r"<strong>\1</strong>", text, flags=re.S)
        text = re.sub(r"(?<![*\w])\*(?=\S)(.+?)(?<=\S)\*(?![*\w])", r"<em>\1</em>", text, flags=re.S)
        text = re.sub(r"(?<![_\w])_(?=\S)(.+?)(?<=\S)_(?![_\w])", r"<em>\1</em>", text, flags=re.S)
        return text

    def _restore(self, text):
        while "\x00" in text:
            text = re.sub(r"\x00(\d+)\x00", lambda m: self.store[int(m.group(1))], text)
        return text


HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE = re.compile(r"^(\s*)(```+|~~~+)\s*([\w+-]*)\s*$")
LIST_ITEM = re.compile(r"^( *)([-*+]|\d{1,9}[.)])( +)(.*)$")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")


def indent_of(line):
    return len(line) - len(line.lstrip(" "))


def starts_paragraph_break(line):
    """Lines that end a paragraph without a blank line before them. Following CommonMark, a
    bullet list may interrupt a paragraph, and an ordered list only when it starts at 1. A
    line starting with ">" does NOT interrupt here (a blockquote must follow a blank line), so
    a wrapped menu path such as "Library\\n  > Categories" stays text."""
    if HEADING.match(line) or FENCE.match(line):
        return True
    item = LIST_ITEM.match(line)
    if item and item.group(4).strip():
        marker = item.group(2)
        return not marker[0].isdigit() or int(marker[:-1]) == 1
    return False


class Page:
    """One Markdown page parsed into HTML, with what the template needs from it."""

    def __init__(self, name, text):
        self.name = name
        self.title = None
        self.first_paragraph = None
        self.headings = []  # (level, slug, plain text) for h2 and below
        self._slugs = {}
        self._inline = Inline(self._rewrite_link)
        lines = strip_comments(text.replace("\r\n", "\n")).split("\n")
        self.body = self._blocks(lines, tight=False)
        if self.title is None:
            raise BuildError(f"{name}.md: no '# ' heading to use as the page title")

    def _error(self, message):
        return BuildError(f"{self.name}.md: {message}")

    def _rewrite_link(self, url):
        if re.match(r"(https?:|mailto:)", url) or url.startswith("#"):
            return url
        match = re.fullmatch(r"([\w-]+)\.md(#[\w-]*)?", url)
        if match:
            return page_url(match.group(1)) + (match.group(2) or "")
        raise self._error(f'unsupported link target "{url}" (use page.md or page.md#anchor)')

    def _heading(self, level, raw):
        inner = self._inline.render(raw)
        text = plain_text(inner)
        base = slugify(text)
        count = self._slugs.get(base, 0)
        self._slugs[base] = count + 1
        slug = f"{base}-{count}" if count else base
        if level == 1 and self.title is None:
            self.title = text
            return f'<h1 id="{slug}">{inner}</h1>'
        self.headings.append((level, slug, text))
        return (
            f'<h{level} id="{slug}">{inner}'
            f'<a class="anchor" href="#{slug}" aria-label="Link to this section">#</a></h{level}>'
        )

    def _blocks(self, lines, tight):
        out = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                i += 1
                continue

            fence = FENCE.match(line)
            if fence:
                indent, marker, lang = len(fence.group(1)), fence.group(2), fence.group(3)
                i += 1
                code = []
                while i < len(lines) and not re.fullmatch(
                    rf"\s*{re.escape(marker[0])}{{{len(marker)},}}\s*", lines[i]
                ):
                    code.append(lines[i][min(indent, indent_of(lines[i])):])
                    i += 1
                if i == len(lines):
                    raise self._error(f"unclosed code block ({marker})")
                i += 1
                cls = f' class="language-{lang}"' if lang else ""
                out.append(f"<pre><code{cls}>{html.escape(chr(10).join(code), quote=False)}</code></pre>")
                continue

            heading = HEADING.match(line)
            if heading:
                out.append(self._heading(len(heading.group(1)), heading.group(2)))
                i += 1
                continue

            if LIST_ITEM.match(line):
                fragment, i = self._list(lines, i)
                out.append(fragment)
                continue

            if line.lstrip().startswith(">"):
                quoted = []
                while i < len(lines) and lines[i].lstrip().startswith(">"):
                    quoted.append(re.sub(r"^\s*> ?", "", lines[i]))
                    i += 1
                out.append(f"<blockquote>\n{self._blocks(quoted, tight=False)}\n</blockquote>")
                continue

            paragraph = [line.strip()]
            i += 1
            while i < len(lines) and lines[i].strip() and not starts_paragraph_break(lines[i]):
                paragraph.append(lines[i].strip())
                i += 1
            if any(TABLE_ROW.match(p) for p in paragraph):
                raise self._error("tables are not supported by build_docs.py: " + paragraph[0])
            text = self._inline.render("\n".join(paragraph))
            if self.first_paragraph is None:
                self.first_paragraph = text
            out.append(text if tight else f"<p>{text}</p>")
        return "\n".join(out)

    def _list(self, lines, i):
        first = LIST_ITEM.match(lines[i])
        ordered = first.group(2)[0].isdigit()
        kind = first.group(2)[-1]  # "-", "*", "+" for bullets; "." or ")" for ordered
        start = int(first.group(2)[:-1]) if ordered else 1

        def sibling(line, content_indent):
            item = LIST_ITEM.match(line)
            return (
                item is not None
                and indent_of(line) < content_indent
                and item.group(2)[0].isdigit() == ordered
                and item.group(2)[-1] == kind
            )

        items = []
        loose = False
        content_indent = len(first.group(1)) + 1
        while i < len(lines) and sibling(lines[i], content_indent if items else 10**6):
            item = LIST_ITEM.match(lines[i])
            content_indent = len(item.group(1)) + len(item.group(2)) + len(item.group(3))
            body = [item.group(4)]
            i += 1
            while i < len(lines):
                line = lines[i]
                if not line.strip():
                    j = i
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and indent_of(lines[j]) >= content_indent:
                        body.extend([""] * (j - i))
                        loose = True
                        i = j
                        continue
                    break
                if indent_of(line) >= content_indent:
                    body.append(line[content_indent:])
                elif LIST_ITEM.match(line) or starts_paragraph_break(line):
                    break
                else:
                    body.append(line.strip())  # lazy continuation of the item's text
                i += 1
            items.append(body)
            if i < len(lines) and not lines[i].strip():
                j = i
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and sibling(lines[j], content_indent):
                    loose = True
                    i = j
                    continue
                break

        tag = "ol" if ordered else "ul"
        attrs = f' start="{start}"' if ordered and start != 1 else ""
        rendered = "\n".join(f"<li>{self._blocks(body, tight=not loose)}</li>" for body in items)
        return f"<{tag}{attrs}>\n{rendered}\n</{tag}>", i


# ---------------------------------------------------------------------------
# The site around each page

OVERVIEW_LABEL = "Overview"
VERSION_CHIP = "v0.1.5"  # as in public/index.html's hero; change both together
FONTS = (
    "https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900"
    "&family=Instrument+Sans:wght@400;500;600&display=swap"
)


def read_index(text):
    """The sidebar: README.md's "##" sections and the page each of their list items links."""
    groups = []
    for line in strip_comments(text).split("\n"):
        heading = re.match(r"^##\s+(.*?)\s*$", line)
        if heading:
            groups.append((heading.group(1), []))
            continue
        item = re.match(r"^\s*[-*+]\s+\[([^\]]+)\]\(([\w-]+)\.md\)", line)
        if item and groups:
            groups[-1][1].append((item.group(2), item.group(1)))
    return groups


def description(page):
    text = " ".join(plain_text(page.first_paragraph or page.title).split())
    if len(text) > DESCRIPTION_LIMIT:
        text = text[: DESCRIPTION_LIMIT - 1].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return text


def sidebar_html(groups, current):
    def link(name, label):
        here = ' aria-current="page"' if name == current else ""
        return f'<li><a href="{page_url(name)}"{here}>{html.escape(label, quote=False)}</a></li>'

    parts = [f'<div class="nav-group"><ul>{link(INDEX_PAGE, OVERVIEW_LABEL)}</ul></div>']
    for title, pages in groups:
        items = "".join(link(name, label) for name, label in pages)
        parts.append(
            f'<div class="nav-group"><p class="label">{html.escape(title, quote=False)}</p>'
            f"<ul>{items}</ul></div>"
        )
    return '<nav aria-label="Documentation pages">' + "".join(parts) + "</nav>"


def toc_html(page):
    entries = [(level, slug, text) for level, slug, text in page.headings if level <= 3]
    if len(entries) < TOC_MINIMUM:
        return ""
    out = ["<ul>"]
    open_sub = False
    for index, (level, slug, text) in enumerate(entries):
        link = f'<a href="#{slug}">{html.escape(text, quote=False)}</a>'
        if level == 3 and index > 0:
            if not open_sub:
                out[-1] = out[-1].removesuffix("</li>") + "<ul>"
                open_sub = True
            out.append(f"<li>{link}</li>")
            continue
        if open_sub:
            out.append("</ul></li>")
            open_sub = False
        out.append(f"<li>{link}</li>")
    if open_sub:
        out.append("</ul></li>")
    out.append("</ul>")
    return "".join(out)


def pager_html(order, labels, name):
    position = order.index(name)
    links = []
    if position > 0:
        previous = order[position - 1]
        links.append(
            f'<a class="prev" href="{page_url(previous)}"><span>Previous page</span>'
            f"{html.escape(labels[previous], quote=False)}</a>"
        )
    if position + 1 < len(order):
        following = order[position + 1]
        links.append(
            f'<a class="next" href="{page_url(following)}"><span>Next page</span>'
            f"{html.escape(labels[following], quote=False)}</a>"
        )
    return '<nav class="pager" aria-label="Previous and next page">' + "".join(links) + "</nav>"


def render_page(page, groups, order, labels):
    name = page.name
    title = page.title if name == INDEX_PAGE else f"{page.title} · Saikou docs"
    sidebar = sidebar_html(groups, name)
    toc = toc_html(page)
    docs_current = "page" if name == INDEX_PAGE else "true"
    layout_class = "docs-layout page" + ("" if toc else " no-toc")
    mobile_toc = (
        f'<details class="docs-toc-mobile"><summary>On this page</summary><div>{toc}</div></details>'
        if toc
        else ""
    )
    desktop_toc = (
        f'<aside class="docs-toc" aria-label="On this page"><p class="label">On this page</p>{toc}</aside>'
        if toc
        else ""
    )
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <title>{html.escape(title, quote=False)}</title>
    <meta name="description" content="{html.escape(description(page))}" />
    <link rel="canonical" href="{HOST}{page_url(name)}" />
    <link rel="icon" type="image/png" href="/icon-192.png" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link rel="stylesheet" href="{html.escape(FONTS)}" />
    <link rel="stylesheet" href="/docs/docs.css" />
  </head>
  <body>
    <a class="skip-link" href="#doc-content">Skip to content</a>
    <header class="site-header">
      <div class="page">
        <a class="brand" href="/">
          <img src="/icon-192.png" alt="" width="32" height="32" />
          <span class="wordmark">Saikou</span>
          <span class="brand-sub">Docs</span>
        </a>
        <nav aria-label="Site">
          <span class="chip">{html.escape(VERSION_CHIP, quote=False)}</span>
          <a href="/#features">Features</a>
          <a href="/#download">Download</a>
          <a href="/docs/" aria-current="{docs_current}">Docs</a>
          <a href="/privacy-policy">Privacy policy</a>
          <a href="https://github.com/ShinSaikou/saikou">GitHub</a>
          <a href="{DISCORD}">Discord</a>
        </nav>
      </div>
    </header>

    <div class="{layout_class}">
      <aside class="docs-sidebar" aria-label="Documentation">{sidebar}</aside>
      <main class="docs-main" id="doc-content">
        <div class="docs-mobile">
          <details class="docs-menu"><summary>Menu</summary><div>{sidebar}</div></details>
          {mobile_toc}
        </div>
        <article class="doc">
{page.body}
        </article>
        {pager_html(order, labels, name)}
      </main>
      {desktop_toc}
    </div>

    <footer class="site-footer">
      <div class="page">
        <div>
          <p class="wordmark">Saikou</p>
          <p class="footer-note">An open-source manga reader for Android.</p>
        </div>
        <div class="footer-links">
          <a href="/docs/">Docs</a>
          <a href="/privacy-policy">Privacy policy</a>
          <a href="https://github.com/ShinSaikou/saikou">GitHub</a>
          <a href="{DISCORD}">Discord</a>
          <a href="mailto:shinsaikou@proton.me">shinsaikou@proton.me</a>
          <span>© 2026 Saikou</span>
        </div>
      </div>
    </footer>
  </body>
</html>
"""


# ---------------------------------------------------------------------------
# Checks on the rendered output

class Anchors(HTMLParser):
    """Every id, and every href or src, in one HTML document."""

    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.targets = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key) is not None:
                self.targets.append(attrs[key])


def resolve(path, rendered):
    """The file the Worker serves for `path` under its default html_handling
    (auto-trailing-slash), as text if it is HTML. Raises BuildError for a missing file or a
    path the Worker would answer with a redirect."""

    def exists(rel):
        if rel.startswith("docs/") and rel.endswith(".html"):
            return rel[len("docs/"):] in rendered
        return (PUBLIC / rel).is_file()

    def read(rel):
        if rel.startswith("docs/") and rel.endswith(".html"):
            return rendered[rel[len("docs/"):]]
        return (PUBLIC / rel).read_text(encoding="utf-8") if rel.endswith(".html") else None

    if path.endswith(".html") or path.endswith("/index"):
        raise BuildError(f"{path} is redirected by the Worker; link the clean URL instead")
    rel = path.lstrip("/")
    if path.endswith("/"):
        rel += "index.html"
        if exists(rel):
            return read(rel)
        if exists(rel.removesuffix("/index.html") + ".html"):
            raise BuildError(f"{path} redirects; drop the trailing slash")
        raise BuildError(f"{path} does not exist")
    if exists(rel) and "." in rel.rsplit("/", 1)[-1]:
        return read(rel)
    if exists(rel + ".html"):
        return read(rel + ".html")
    if exists(rel + "/index.html"):
        raise BuildError(f"{path} redirects; add a trailing slash")
    raise BuildError(f"{path} does not exist")


def check_links(rendered):
    errors = []
    ids_of = {}

    def ids(text):
        key = text
        if key not in ids_of:
            ids_of[key] = set(Anchors(text).ids)
        return ids_of[key]

    for file_name, text in rendered.items():
        parsed = Anchors(text)
        duplicates = sorted({x for x in parsed.ids if parsed.ids.count(x) > 1})
        if duplicates:
            errors.append(f"docs/{file_name}: duplicate id(s) {', '.join(duplicates)}")
        for target in parsed.targets:
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:|//", target):
                continue  # another host, mailto
            path, _, fragment = target.partition("#")
            try:
                if not path:
                    target_text = text
                elif not path.startswith("/"):
                    raise BuildError(f"relative link {target}")
                else:
                    target_text = resolve(path, rendered)
                if fragment and (target_text is None or fragment not in ids(target_text)):
                    raise BuildError(f"no #{fragment} on {path or 'this page'}")
            except BuildError as error:
                errors.append(f"docs/{file_name}: broken link {target}: {error}")
    return errors


def forbidden_matches(rendered):
    """The count check from site/README.md, over public/*.html and the rendered docs. Returns
    (matching line count, files with a match), or None when the word list is missing. The
    matching text is never printed."""
    if not FORBIDDEN_WORDS.is_file():
        return None
    patterns = "\n".join(
        line
        for line in FORBIDDEN_WORDS.read_text(encoding="utf-8").splitlines()
        if not re.match(r"^\s*(#|$)", line)
    )
    with tempfile.TemporaryDirectory() as tmp:
        shown = {}
        files = []
        for path in sorted(PUBLIC.glob("*.html")):
            files.append(str(path))
            shown[str(path)] = f"public/{path.name}"
        for file_name, text in rendered.items():
            path = Path(tmp) / file_name
            path.write_text(text, encoding="utf-8")
            files.append(str(path))
            shown[str(path)] = f"public/docs/{file_name}"
        result = subprocess.run(
            ["grep", "-n", "-i", "-E", "-f", "-", *files],
            input=patterns,
            capture_output=True,
            text=True,
        )
    if result.returncode > 1:
        raise BuildError(f"the forbidden-words grep failed (exit {result.returncode})")
    lines = result.stdout.splitlines()
    matched = sorted({shown.get(line.split(":", 1)[0], "?") for line in lines})
    return len(lines), matched


# ---------------------------------------------------------------------------

def build():
    errors = []
    pages = {}
    for source in sorted(DOCS_SRC.glob("*.md")):
        try:
            pages[source.stem] = Page(source.stem, source.read_text(encoding="utf-8"))
        except BuildError as error:
            errors.append(str(error))
    if errors:
        raise BuildError("\n".join(errors))
    if INDEX_PAGE not in pages:
        raise BuildError(f"docs/{INDEX_PAGE}.md is missing")

    groups = read_index((DOCS_SRC / f"{INDEX_PAGE}.md").read_text(encoding="utf-8"))
    listed = [name for _, group in groups for name, _ in group]
    labels = {INDEX_PAGE: OVERVIEW_LABEL}
    labels.update((name, label) for _, group in groups for name, label in group)
    for name in sorted({n for n in listed if listed.count(n) > 1}):
        errors.append(f"{INDEX_PAGE}.md lists {name}.md more than once")
    for name in listed:
        if name not in pages:
            errors.append(f"{INDEX_PAGE}.md lists {name}.md, which does not exist")
    for name in pages:
        if name != INDEX_PAGE and name not in listed:
            errors.append(f"{name}.md is not linked from a list in {INDEX_PAGE}.md, so no sidebar shows it")
    if errors:
        raise BuildError("\n".join(errors))

    order = [INDEX_PAGE] + listed
    rendered = {out_name(name): render_page(pages[name], groups, order, labels) for name in order}
    for file_name, text in rendered.items():
        if EM_DASH in text:
            errors.append(f"docs/{file_name}: contains an em dash (U+2014)")
        if "<!--" in text:
            errors.append(f"docs/{file_name}: an HTML comment survived")
    errors.extend(check_links(rendered))
    if errors:
        raise BuildError("\n".join(errors))
    return rendered


def sitemap_xml(rendered):
    """Every public page, by its served URL: SITE_PAGES, then the docs in sidebar order."""
    docs = ["/docs/" if file_name == "index.html" else f"/docs/{file_name[:-len('.html')]}" for file_name in rendered]
    urls = "".join(f"  <url><loc>{HOST}{path}</loc></url>\n" for path in SITE_PAGES + docs)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}</urlset>\n"
    )


def robots_txt():
    return f"User-agent: *\nAllow: /\n\nSitemap: {HOST}/sitemap.xml\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="build and check, write nothing")
    args = parser.parse_args()

    try:
        rendered = build()
        forbidden = forbidden_matches(rendered)
    except BuildError as error:
        print(f"build_docs: FAILED\n{error}", file=sys.stderr)
        return 1
    if forbidden is None:
        print(f"build_docs: WARNING: {FORBIDDEN_WORDS} not found; forbidden-words check skipped", file=sys.stderr)
    elif forbidden[0]:
        print(
            f"build_docs: FAILED\nforbidden-words count: {forbidden[0]} matching line(s) in "
            + ", ".join(forbidden[1]),
            file=sys.stderr,
        )
        return 1

    if args.check:
        print(f"build_docs: {len(rendered)} pages pass every check; nothing written (--check)")
        return 0
    DOCS_OUT.mkdir(parents=True, exist_ok=True)
    for stale in sorted(DOCS_OUT.glob("*.html")):
        if stale.name not in rendered:
            stale.unlink()
            print(f"build_docs: removed stale public/docs/{stale.name}")
    for file_name, text in rendered.items():
        (DOCS_OUT / file_name).write_text(text, encoding="utf-8")
    (PUBLIC / "sitemap.xml").write_text(sitemap_xml(rendered), encoding="utf-8")
    (PUBLIC / "robots.txt").write_text(robots_txt(), encoding="utf-8")
    count = "skipped" if forbidden is None else forbidden[0]
    print(
        f"build_docs: wrote {len(rendered)} pages to public/docs/, and public/sitemap.xml and "
        f"public/robots.txt; links checked; forbidden-words count: {count}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
