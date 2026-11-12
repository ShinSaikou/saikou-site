# Browse and sources

The **Browse** tab has three tabs: **Sources** (what you can browse), **Extensions** (what you can
install, see [Extensions and repositories](extensions.md)) and **Migrate** (see
[Migration](migration.md)).

A source is one site or one collection, provided by an extension. The **Local source**, for files
on your device, is built in. See [The Local source](local-source.md).

## The Sources tab

Sources are grouped under **Last used**, **Pinned** and the rest (**Other**), each with its
language. The Local source comes after every extension's sources.

- Tap a source to browse it.
- **Latest**, at the end of a row, opens the source's latest updates directly (shown when the
  source has a latest listing).
- The **pin** button keeps a source under **Pinned**, at the top.
- Long press a source for **Pin** or **Unpin** and **Disable**. A disabled source is hidden from
  this list and from global search.

### Choosing which sources show

The **Filter** icon in the top bar opens **Sources**: one switch per language, and under each
enabled language a checkbox per source. Turn off a language you do not read and its sources
disappear from the list and from global search.

More > Settings > Browse has related settings:

- **Enabled languages**: the same language choice.
- **Show mature sources**: show sources marked with a content warning. Changing it asks for your
  device's unlock (fingerprint, face or screen lock) when one is set.
- **Hide library entries**: leave out entries already in your library from browse lists.

If no source appears at all, the Sources tab says so: "Installed sources appear here. Configure an
extension repository to add them." See [Extensions and repositories](extensions.md).

## Browsing a source

- **Popular**, **Latest** and **Search** switch between the source's listings. Some sources have no
  latest listing ("This source has no latest listing").
- **Search this source** searches by title.
- **Filter** opens the source's own filters, when it has any. **Apply** runs them, **Reset** clears
  them; the list shows **Filters applied** while some are active. What the filters are depends on
  the source.
- **Display mode** switches between **Comfortable grid**, **Compact grid** and **List**.
- Entries already in your library are marked **In library**.
- The overflow menu has **Source settings** and **Open in WebView**.

Tap an entry to open its page, where **Add to library** adds it. See
[An entry's page](entry.md).

### Adding many entries at once

- **Long press** an entry to start selecting. Long press a second entry further down and every
  entry between the two is selected too. While a selection is open, a tap adds or removes one
  entry, and **Back** clears it.
- **Select all** selects the entries loaded so far (scroll further to load more first), and
  **Invert selection** swaps what is selected.
- **Add to library** adds the selected entries that are not in your library yet, all at once, and
  says how many it added. They go to your **Default category** (More > Settings > Library); when
  that is **Always ask** and you have categories, Saikou asks once for the whole selection.

Chapters an entry already had when you added it do not count as new in **Updates**. See
[Library updates](updates.md).

## Global search

**Search all sources** (the search icon on Browse) searches every enabled source at once. Results
come in source by source as each one answers, with the Local source last; **More from this source**
opens one source's full results. A source with nothing shows **No results**.

The button is on the **Sources** and **Migrate** tabs. On the **Extensions** tab the search button
searches the extensions instead.

Two other places start the same search with the words filled in: **Search all sources for "..."**
above the results of a [library search](library.md#the-library-tab), and a tap on the title or
author on [an entry's page](entry.md#the-header).

## Searching from other apps

Other apps can send Saikou something to search for: Android's share menu, a voice search, or an
extension's link handler. This is experimental. Turn it on in More > Settings > Experimental >
**Open shared text and search requests**.

While it is off, Shin Saikou is not in the share menu and no other app can send it a search. Web
pages cannot open a search in Saikou, whether it is on or off.

Each search another app sends goes to your sources, the same as a search you type. Only enabled
sources are asked: a source you disabled, or one whose language is turned off, is left out (see
[Choosing which sources show](#choosing-which-sources-show)).

### Sharing a page of a source's site

In a browser, share a page from a site one of your sources reads, and pick **Shin Saikou**. Saikou
opens that source's search for the page's address, which many sources answer with the page's entry.

When several sources of one extension read that site, for example one per language and one for
**Multiple languages**, Saikou picks one of them:

1. the one you pinned;
2. otherwise the one you used last;
3. otherwise the one for **Multiple languages**.

When sources of different extensions read the same site, Saikou cannot tell which one you meant. It
opens **Search all sources** instead, with the shared words, or with the address when the text is
only that.

### Sharing words

Select some words, such as a title on a web page, share them and pick **Shin Saikou**. Saikou opens
[Search all sources](#global-search) for them. Web addresses in the shared text are left out, and so
is a pair of quotes around the words, so a selection that a browser shares with a link to it
searches only the words. Text that is only the address of a site none of your sources reads
searches for that address. Line breaks become spaces, and only the first 500 characters are used.

### Searches from other apps

A voice search, or a link handler that names no extension, opens **Search all sources** with its
words. An extension's link handler that names its extension opens the search of that extension's
source, picked the same way as for a shared page. If that extension is not installed, or none of its
sources is enabled, the search goes to **Search all sources**.

## Source settings

Browse a source, then overflow > **Source settings**. It shows the settings the source itself
offers (if any: "This source has no settings of its own") and a **Cookies** section.

**Cookies** helps with sites that need you to sign in or to pass a check page:

- **Open the page** opens the site in Saikou's WebView, where you can sign in or clear the check.
  Cookies set there are used by the source afterwards.
- Or paste a **Cookie header** copied from a browser, with its **Address**, and tap **Import**.
- **Cookies currently set** lists what Saikou holds for the address; **Clear** removes them.

See [Troubleshooting](troubleshooting.md) for when a site keeps asking for a browser check.
