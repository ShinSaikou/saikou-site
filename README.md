# Saikou public site

Two static pages that Google Auth Platform requires before an External OAuth app can be moved to
In production: a home page and a privacy policy, both on an authorized domain. Without them the app
stays in Testing, where Google expires refresh tokens after seven days (PLAN decision 9), and Drive
sync would ask the owner to sign in again every week.

- Home page: https://shinsaikou.com/ (`public/index.html`; redesigned 2026-10-01 and again 2026-10-30)
- Privacy policy: https://shinsaikou.com/privacy-policy (`public/privacy-policy.html`;
  `/privacy-policy.html` redirects there)
- Icon: `public/icon-192.png`, copied from `../brand/icon-192.png`

Made on 2026-09-26 for owner item 2 (`design/plans/phase3-start.md` section 6).

## The docs

User docs, written 2026-10-24. The Markdown in `docs/` is the source;
`tools/build_docs.py` (standard library only) turns it into `public/docs/*.html`, with `README.md`
as `public/docs/index.html`, served at `https://shinsaikou.com/docs/` (the app's Migrate
help action opens `/docs/migration`). Edit the Markdown, never the generated HTML, then from
this folder:

```bash
python3 tools/build_docs.py
```

The same run writes `public/sitemap.xml` (the home page, the privacy policy and every docs page)
and `public/robots.txt`, which points to it; a new hand-written page goes in `SITE_PAGES` in the
script. Google Search Console reads the sitemap at `https://shinsaikou.com/sitemap.xml`.

`--check` builds without writing. The build refuses to write on a broken link or anchor, a page
missing from the index, a table, an em dash, or an HTML comment that would ship. The
`<!-- FIXABLE: F<n> -->` markers in the Markdown are stripped from the HTML; each names an item in
`design/plans/docs/fixable-warnings.md` that the app should fix rather than warn about, and goes
when its fix lands. The version label ("v0.1.2") is in both `public/index.html` and
the script; change both together.

## How it is served

An assets-only Cloudflare Worker named `saikou-site` on one custom domain, `shinsaikou.com`, in the
Cloudflare account that holds that zone. Its `workers.dev` address and preview URLs are off, so the
site answers only on its own domain. `wrangler.jsonc` explains each choice.

## Changing it

From this folder:

```bash
tools/deploy.sh --dry-run
```

```bash
tools/deploy.sh
```

`tools/deploy.sh` runs `wrangler deploy` with the API token and account ID in
`~/.config/shinsaikou/cloudflare.env` (or the file `SAIKOU_CLOUDFLARE_ENV` names), never with the
global `wrangler login`, which may belong to a different account. Keep the Worker name
`saikou-site`: deploying under another name creates a second Worker and moves the domain onto it.

Before deploying, check that nothing in `public/` names a source, the catalog or an extension
(the list `SAIKOU_FORBIDDEN_WORDS_FILE` names, `../tools/forbidden-words.txt` in the owner's checkout, applies here as it does to the app's repository) and that no em dash crept in.
This prints only a count of matching lines, never the list itself:

```bash
grep -n -i -E -f <(grep -v -E '^\s*(#|$)' "${SAIKOU_FORBIDDEN_WORDS_FILE:-../tools/forbidden-words.txt}") public/*.html | wc -l
```

## What must stay in step with the app

The privacy policy states facts about the app. Update it, and its effective date, when any of these
change:

- **What sync carries.** Section 4 lists it, matching `sync_carries_note` in
  `saikou/i18n/src/main/res/values/strings_screens.xml`.
- **The Google scope.** Only `drive.appdata`. A second scope means editing section 4 and also
  Google Auth Platform > Data Access, and a sensitive scope brings Google's verification.
- **Where the refresh token lives** (the Android Keystore, via `KeystoreSecretStore`).
- **Network use.** Saikou has no analytics, crash reporting or server of its own. Adding any of them
  needs a new section.
- **Tracking.** Section 5 covers MyAnimeList (added 2026-10-01) and section 6 covers AniList
  (added 2026-11-01). Each states what a link, a finished chapter and a sheet edit send
  (`MyAnimeListApi.updateItem` and `AnilistApi.addLibManga`/`updateLibManga` in `saikou/tracking`),
  that the token lives in the ordinary preference file under a private key
  (`TrackPreferences.trackToken`, not `KeystoreSecretStore`) and so enters a backup only with
  private settings, and that sync never carries it (`sync_carries_note`). Section 6 also states
  that AniList's token lasts a year and can't be renewed (`Anilist.TOKEN_LIFETIME`,
  `AnilistInterceptor`). A third tracker, a move of a token into the Keystore, or a change to what
  is sent means editing these sections and sections 2, 3 and 8.

## Google's side

Google Cloud project `saikou-513412`, owned by the Shin Saikou Google account, with the Google Drive
API enabled and one OAuth client, "Saikou Drive sync" (Desktop app). Google Auth Platform > Branding
lists:

- Application home page: `https://shinsaikou.com`
- Application privacy policy link: `https://shinsaikou.com/privacy-policy`
- Authorized domain: `shinsaikou.com`, verified in Search Console with a DNS TXT record in Cloudflare
- No logo

Data Access holds the one scope, `drive.appdata`, which Google files as non-sensitive. Publishing
status: **In production** since 2026-11-01, with no verification asked, so refresh tokens don't
expire after seven days. Google's sign-in page names the app ("to continue to Saikou") without brand
verification. Adding a logo makes verification mandatory. Moving either URL means editing Branding
too.
