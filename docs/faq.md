# Frequently asked questions

## General

### What is Saikou?

An open-source manga reader for Android. It reads `.tachibk` backups and extensions built for the
Tachiyomi extension API, and adds features of its own such as sync between devices.

### Where do I get it?

From its releases page on GitHub, <https://github.com/ShinSaikou/saikou/releases>. The source
code is there too. See [Getting started](getting-started.md#installing-saikou).

### Is there an iOS version?

No. Saikou is an Android app (Android 8.0 and later).

### Does Saikou come with any content?

No. Read files from your device with the [Local source](local-source.md), or add extensions from
repositories you choose. See [Getting started](getting-started.md).

### Can I read light novels?

No. Saikou shows pages as images. It does not lay out text.

### I use another reader. Do I have to start over?

No. Restore its `.tachibk` backup in Saikou, then copy its downloads. See
[Getting started](getting-started.md#coming-from-another-reader).

### Can I sync between my devices?

Yes, through your Google Drive or a WebDAV server. See [Sync between devices](sync.md).

### Does Saikou collect data about me?

No. Saikou has no analytics, no crash reporting and no server of its own. See
[Security and privacy](security-and-privacy.md).

### How do I avoid losing my library?

Keep automatic backups on, and now and then create a backup by hand and keep it off the phone. See
[Backups and restore](backups.md).

## Library and updates

### Why does an automatic update skip some entries?

**Smart update** skips entries with unread chapters, entries you have not started, entries marked
**Completed**, and entries not expected to have a new chapter yet. This saves time and keeps the
sites from limiting you. A manual update (pull down on the Library) ignores those rules and checks
every entry in the categories you update. See
[Library updates](updates.md).

### Why am I warned about updating many entries from one source?

Sending one site a large number of requests can get you limited or blocked. Saikou already slows
down for a site that pushes back. To quiet the warning, exclude a category of rarely read entries
from updates. See [Library updates](updates.md#how-saikou-treats-the-sites).

### Why do updates not run in the background?

See [Troubleshooting](troubleshooting.md#updates-or-backups-do-not-run-in-the-background).

### How do I see how many chapters I have downloaded?

Turn on the **Downloaded badge** in the library sheet's **Display** tab (or More > Settings >
Library > **Show download badges**).

### How do I deal with duplicate chapters from several groups?

- On the entry's page, **Filter > Filter scanlator groups**: untick groups you do not want, and
  rank the rest with **Move up** / **Move down**.
- More > Settings > Reader > **Skip duplicate chapters**: the reader moves to one copy of each
  chapter, your preferred group's when you ranked them.
- More > Settings > Library > **Mark duplicate read chapter as read**.
- More > Settings > Downloads > **Skip downloading duplicate read chapters**.

### How do I pause reading history?

Turn on **Incognito** in the More tab.

### How do I read only what I have downloaded?

Turn on **Downloaded only** in the More tab.

### Why can I not turn off the library's Downloaded filter?

**Downloaded only** is on in the More tab. Turn it off.

## Downloads

### Can I download several chapters at the same time?

Chapters download one after another, while several pages of each chapter download at once (More >
Settings > Downloads > **Pages downloaded at once**). Going one chapter at a time keeps sites from
blocking you.

### Why did my downloads stop?

Usually the network or the site. The queue (More > **Download queue**) shows **Failed** with the
reason, and a notification lists failures. Also check **Only download over Wi-Fi**.

### Where are my downloads? Can I put them on an SD card?

In Saikou's own app storage on the device. You do not choose a folder, and they never appear in your
gallery. See [Downloads](downloads.md#where-downloads-are-kept).

## Reader

### Can I see two pages side by side?

Not yet. **Split wide pages** and **Rotate wide pages to fit** in the reader's settings help with
double-page spreads. See [The reader](reader.md).

### What do all the reader settings do?

See [The reader](reader.md).

## Browse and extensions

### Why do I not see a source I installed?

- Its language may be turned off: Browse > Sources > **Filter**, or More > Settings > Browse >
  **Enabled languages**.
- You may have disabled it (long press > **Disable**). Turn it back on in Browse > Sources >
  **Filter**.
- It may be marked as mature: More > Settings > Browse > **Show mature sources**.

### Do I need to allow installing unknown apps, or set an installer?

No. Saikou installs extensions inside the app, without Android's package installer.

### How do I uninstall an extension?

Browse > Extensions, open the extension and tap **Uninstall**. See
[Extensions and repositories](extensions.md#uninstalling).

## Settings

### Why are screenshots blocked?

**Secure screen** is on, or set to **Incognito** while incognito is on. Change it in More >
Settings > **Security and privacy**.

### What is DNS over HTTPS?

A way to look up site addresses over an encrypted connection instead of your network's DNS, which
can get around simple blocks. Set it in More > Settings > Advanced > **DNS over HTTPS (DoH)** and
restart the app.
