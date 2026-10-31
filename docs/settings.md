# Settings reference

More > **Settings** lists its sections; on a large screen the list stays beside the open section.
This page goes through each section row by row and links to the guide that explains it.

The More tab itself has two **Quick controls**, **Incognito** and **Downloaded only**, and the
**Manage** rows: **Download queue**, **Categories**, **Statistics**, **Data and storage** (opens
Settings on the Data section), **Extension repositories**, **Backup**, **Settings** and **Crash
logs**.

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

See [The reader](reader.md).

**Default reading mode**, **Double tap animation speed**, **Show reading mode**, **Show tap zones
overlay**, **Default rotation**, **Fullscreen**, **Keep screen on**, **Show page number**, **Skip
chapters marked read**, **Skip filtered chapters**, **Skip duplicate chapters**, **Sensitivity for
hiding menu on scroll**, **Volume keys**, **Invert volume keys**, **Save pages into separate
folders**.

## Downloads

See [Downloads](downloads.md).

**Only download over Wi-Fi**, **Pages downloaded at once**, the **Delete chapters** group, **Download
new chapters** with its two sub-rows, **Auto download while reading**, **Unmatched downloads**,
**Export downloads**, **Copy downloads from a folder** and **Last copy from a folder**.

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
