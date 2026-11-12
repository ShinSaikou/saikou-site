# Settings reference

More > **Settings** lists its sections; on a large screen the list stays beside the open section.
This page goes through each section row by row and links to the guide that explains it.

The More tab itself has the logo at the top, which opens [About](#the-about-screen), two **Quick
controls**, **Incognito** and **Downloaded only**, and the **Manage** rows: **Download queue**,
**Categories**, **Statistics**, **Data and storage** (opens Settings on the Data section),
**Extension repositories**, **Backup**, **Settings** and **Crash logs**. Each row has an icon.

## Searching settings

Tap the search button above the section list and type in **Search settings**. Every matching
setting is listed with the section it is in. Pick one to open that section scrolled to the setting,
which flashes for a moment so it is easy to spot.

## The About screen

Tap the logo at the top of the More tab to open **About**.

- The version, the build and the commit. Tap them to copy one line for a report.
- **Check for updates**.
- **Builds**: the latest release's APKs with their size. Each offers **Update** or **Download**, or
  says **Installed** for the one you have. **All releases** opens every version with its notes on
  GitHub.
- **Help**: **Share bug report**, **Copy device info**, **Report an issue**, **Discord** and
  **Website**. See [Reporting a problem](troubleshooting.md#reporting-a-problem).

From a later release, every release also carries a debug APK, listed here as **Debug
build**. It installs beside your app as Shin Saikou Debug, with a library of its own, so you can
try a fix or send a detailed bug report without touching your library. Its **Check for updates**
offers the next release's debug APK.

## Appearance

- **Theme**: **Saikou** (the default), **Dynamic** (colours from your wallpaper, Android 12 and
  later), and the named themes **Catppuccin**, **Green Apple**, **Lavender**, **Midnight Dusk**,
  **Monochrome**, **Nord**, **Strawberry Daiquiri**, **Tako**, **Teal & Turquoise**, **Tidal
  Wave**, **Tokyo Night**, **Yin & Yang** and **Yotsuba**.
- **Light and dark**: **Follow system**, **Light** or **Dark**.
- **Pure black in dark mode**: a black background, which saves power on OLED screens.
- **Two pane layout**: **Automatic**, **Always**, **Landscape** or **Never**. Shows lists and their
  details side by side.
- **Date format** and **Relative timestamps** ("Today" instead of a date).

## Library

See [Library and categories](library.md) and [Library updates](updates.md).

- **Show unread badges**, **Show download badges**.
- **Manual ordering**: keep entries you positioned by hand first.
- **Default category**: where new entries go, or **Always ask**.
- **Per-category settings for sort**.
- **Automatic library update**, **Automatic updates device restrictions**, **Categories**,
  **Refresh entry details**, **Smart update**.
- **Chapter on swipe to left**, **Chapter on swipe to right**.
- **Mark duplicate read chapter as read**.

## Reader

See [The reader](reader.md). Every reader option is here, the reader's own sheet included. A row
that depends on another is greyed out while that one is off, and a slider shows only while it
applies.

**Default reading mode**, **Double tap animation speed**, **Show reading mode**, **Show tap zones
overlay**, **Animate page transitions**, then:

- **Display**: **Default rotation**, **Background color**, **Fullscreen**, **Show content in cutout
  area** (on a screen with a cutout), **Keep screen on**, **Show page number**.
- **E-Ink**: **Flash on page change**, with **Flash duration**, **Flash every** and **Flash with**.
- **Reading**: **Skip chapters marked read**, **Skip filtered chapters**, **Skip duplicate
  chapters**, **Always show chapter transition**.
- **Paged**: **Tap zones**, **Invert tap zones**, **Scale type**, **Zoom start position**, **Crop
  borders**, **Automatically zoom into wide images**, **Pan wide images**, **Split wide pages**,
  **Invert split page placement**, **Rotate wide pages to fit**, **Flip orientation of rotated wide
  pages**, and **Two pages side by side** while [that switch](#experimental) is on.
- **Long strip**: **Tap zones**, **Invert tap zones**, **Side padding**, **Sensitivity for hiding
  menu on scroll**, **Crop borders**, **Split wide pages**, **Invert split page placement**,
  **Rotate wide pages to fit**, **Flip orientation of rotated wide pages**, **Double tap to zoom**,
  **Disable zoom out**, and **Scroll speed** while [Auto-scroll in long strip](#experimental) is
  on.
- **Navigation**: **Volume keys**, **Invert volume keys**, **Use vertical chapter navigator in**,
  **Place vertical navigator on the left side**, **Vertical navigator height**.
- **Actions**: **Show actions on long tap**, **Save pages into separate folders**.

## Downloads

See [Downloads](downloads.md).

**Only download over Wi-Fi**, **Sources downloaded at once** (only while [Download from several
sources at once](#experimental) is on), **Pages downloaded at once**, the **Delete chapters** group,
**Download new chapters** with its two sub-rows, **Auto download while reading**, **Unmatched
downloads**, **Export downloads**, **Copy downloads from a folder** and **Last copy from a folder**.

## Tracking

See [Tracking](tracking.md). Shown when this build offers a tracker.

**Trackers** (sign in and out), **Update progress after reading**, **Update progress when marked as
read**, **Compare with MyAnimeList**.

## Browse

See [Browse and sources](browse.md).

**Enabled languages**, **Show mature sources**, **Hide library entries**.

## Data

- **Storage location**: the folder for automatic backups, the Local source and exported downloads.
  See [Backups and restore](backups.md#storage-location).
- **Automatic backup interval**, **Create backup**, and **Last automatically backed up**. See
  [Backups and restore](backups.md).
- **Storage usage**: space used by downloads and by the chapter cache, and the device's free space.
- **Downloads not in library**: downloads of entries you removed from the library, to review and
  delete. See [Downloads](downloads.md#downloads-not-in-library).
- **Clear chapter cache on launch**: empty the cache of pages read online each time the app starts
  fresh.
- **Clear chapter cache**: empty it now. The row shows the space it uses.

## Sync

See [Sync between devices](sync.md).

## Security and privacy

See [Security and privacy](security-and-privacy.md).

**Require unlock**, **Lock when idle**, **Hide notification content**, **Secure screen**.

## Advanced

- **Version**: the app's version and build. Tap to copy it, for example into a bug report.
- **Check for updates**: ask GitHub now whether a newer version is out. **Check for updates
  automatically** does so at most once a day, when the app opens.
- **Check extension updates**: refresh your repositories in the background.
- **Extension library versions override**. See
  [Extensions](extensions.md#when-an-extension-does-not-load).
- **Allow background work**: ask Android not to stop library updates and backups.
- **Crash logs**: the same screen as More > **Crash logs**. See [Troubleshooting](troubleshooting.md#crash-logs).
- **Verbose logging**: write detailed logs to the system log, for diagnosing a problem. Slows the
  app; turn it off afterwards. Takes effect after a restart; the message offers **Restart**.
- **Clear database**: remove entries that are not in your library (ones you only browsed or read
  without adding) from the database, source by source. **Keep entries with read chapters** spares
  those you read. Read chapters and progress of the removed entries are lost.
- **Rebuild library counts**: count the unread, read and bookmarked chapters of every library entry
  again. Use it if a badge or a count looks wrong.
- **Clear WebView data**: reset the in-app browser.
- **DNS over HTTPS (DoH)**, **Default user agent string**, **Reset default user agent string**. See
  [Security and privacy](security-and-privacy.md#network-privacy-options).
- **Refresh library covers**: a full library update that also refreshes every entry's cover and
  details.
- **Reset per-series reader settings**: put every entry back on the default reading mode and
  rotation, on every synced device.
- **Update library manga titles to match source**: let updates replace library entries' titles with
  the source's current title. A renamed entry keeps its downloads and its place in the download
  queue.
- **Disallow non-ASCII filenames**: name new download folders with ASCII characters only, for
  storage that cannot handle other characters. Chapters already downloaded are still found either
  way.
- **Custom hardware bitmap threshold**: lower it if the reader shows blank pages. See
  [The reader](reader.md#when-a-page-does-not-load).
- **Revoke trusted unknown extensions**: withdraw every trust you gave by hand. Takes effect after a
  restart; the message offers **Restart**.

## Experimental

Behaviour that may not suit every source or device. Each switch is off until you turn it on, and
turning it off again puts things back as they were.

- **Load pages in parallel**: an online chapter fetches up to three pages at a time instead of one,
  so the pages ahead are ready sooner. A source that limits how often it may be asked can answer
  more slowly or refuse a page, which then shows its retry button. It applies to chapters opened
  after the change.
- **Custom update interval per entry**: lets an entry's **Update interval** dialog set how many days
  apart it is checked, instead of the estimate from its release dates. See
  [Library updates](updates.md#an-entrys-update-interval). The library's **Custom update interval**
  filter shows only while this is on. The setting stays on this device and is not in backups, and
  turning it off puts every entry back on its estimate.
- **Merged entries**: shows one title from several sources as one library entry with one chapter
  list. See [Merged entries](merged-entries.md). Turning this off shows the entries separately
  again and keeps your merges. The setting stays on this device and is not in backups.
- **Auto-scroll in long strip**: adds a play button to the reader's menu in the long strip modes.
  It scrolls the pages down by itself, on into the next chapter, until a touch stops it. **Scroll
  speed**, under Long strip in the reader's settings, sets how fast, and shows only while this is
  on. See [The reader](reader.md#auto-scroll). The setting stays on this device and is not in
  backups.
- **Two pages side by side**: lets the left to right and right to left paged modes show two pages
  at once, as a printed book does. **Two pages side by side**, in the reader's settings and under
  Paged in Settings > Reader, chooses **Never**, **In landscape** (the default) or **Always**, and
  shows only while this is on. The first page and wide pages stand alone, wide pages whole rather
  than split or rotated, and **Shift pages** in the reader's menu moves the pairing by one page for
  that entry. Until a page has loaded its size is a guess, so a pair can change as wide pages turn
  up. See [The reader](reader.md#two-pages-side-by-side). The setting stays on this device and is
  not in backups.
- **Open shared text and search requests**: adds Shin Saikou to Android's share menu, so sharing a
  title or a page of a source's site searches your sources for it, and lets other apps, such as an
  extension's link handler, open a search in Saikou. See
  [Browse and sources](browse.md#searching-from-other-apps). While it is off, no other app can send
  Saikou a search. The setting stays on this device and is not in backups.
- **Update extensions automatically**: once a day on Wi-Fi or another unmetered network, Saikou
  checks your extension repositories and installs the updates it finds, and a notification says what
  it did. An update signed with a different key still waits for you. A new version can change how a
  source behaves or break it. See [Extensions](extensions.md#updating-extensions-automatically). The
  setting stays on this device and is not in backups.
- **Download from several sources at once**: downloads one chapter from each of several sources at
  the same time. Chapters from one source still download one after another, in queue order. While
  it is on, More > Settings > Downloads shows **Sources downloaded at once**, which sets how many.
  Downloads use more data, memory and battery while it is on. See
  [Downloads](downloads.md#several-sources-at-once). The setting stays on this device and is not in
  backups.
- **Trust certificates you installed**: lets sources load through an ad blocker, a DNS filter or a
  network that inspects secure connections with a certificate you installed on the device. Whoever
  controls that certificate can read and change what Saikou loads from sources. Sync, tracking,
  extension stores and app updates keep trusting only the certificates Android ships with. Takes
  effect after a restart; the message offers **Restart**. See
  [Troubleshooting](troubleshooting.md#sources-fail-behind-an-ad-blocker-a-dns-filter-or-a-work-network).
  The setting stays on this device and is not in backups.
- **Save chapters as CBZ files**: saves each new download as one `.cbz` file instead of a folder of
  images. Chapters you already downloaded stay as they are, and turning it off saves new downloads
  as folders again without changing the files. See
  [Downloads](downloads.md#saving-chapters-as-cbz-files). This setting is in backups.
