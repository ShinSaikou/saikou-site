# Frequently asked questions

## General

### What is Saikou?

An open-source manga reader for Android. It reads `.tachibk` backups and extensions built for the
Tachiyomi extension API, and adds features of its own such as sync between devices.

### Where do I get it?

From its releases page on GitHub, <https://github.com/ShinSaikou/saikou/releases>. The source
code is there too. See [Getting started](getting-started.md#installing-saikou).

### I installed it. Why can I not find Saikou on my phone?

On your phone the app is called **Shin Saikou**. Search for that name.

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

### My other device says "Update Saikou on this device to keep syncing". Why?

Another device that syncs with it runs a newer Saikou, which writes a newer sync format. Update
Saikou on this device too. Since 0.1.5, sync also carries chapters marked unread and bookmarks you
remove, so every syncing device needs 0.1.5. See [Sync format](sync.md#sync-format).

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
every entry in the categories you update. The update interval button on an entry's page says when
it is next checked, or why it is not. See [Library updates](updates.md).

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

### Can one title use several sources?

Yes, with [Merged entries](merged-entries.md). Turn them on in More > Settings > Experimental. A
chapter one source lacks then comes from another, in one chapter list.

### How do I pause reading history?

Turn on **Incognito** in the More tab.

### How do I read only what I have downloaded?

Turn on **Downloaded only** in the More tab.

### Why can I not turn off the library's Downloaded filter?

**Downloaded only** is on in the More tab. Turn it off.

## Downloads

### Can I download several chapters at the same time?

By default, chapters download one after another, while several pages of each chapter download at
once (More > Settings > Downloads > **Pages downloaded at once**). Going one chapter at a time keeps
sites from blocking you.

To download chapters from different sources side by side, turn on More > Settings > Experimental >
**Download from several sources at once**. Each source still gets one chapter at a time. See
[Downloads](downloads.md#several-sources-at-once).

### Can downloads be saved as CBZ files?

Yes. Turn on More > Settings > Experimental > **Save chapters as CBZ files**. New downloads are then
one `.cbz` file per chapter; the ones you have stay folders. See
[Downloads](downloads.md#saving-chapters-as-cbz-files).

### Why did my downloads stop?

Usually the network or the site. The queue (More > **Download queue**) shows **Failed** with the
reason, and a notification lists failures. Also check **Only download over Wi-Fi**.

### Where are my downloads? Can I put them on an SD card?

In Saikou's own app storage on the device. You do not choose a folder, and they never appear in your
gallery. See [Downloads](downloads.md#where-downloads-are-kept).

## Reader

### Can I see two pages side by side?

Yes, in the left to right and right to left paged modes. Turn on More > Settings > Experimental >
**Two pages side by side**, then choose **In landscape** or **Always** in the reader's settings. See
[The reader](reader.md#two-pages-side-by-side).

### Can the reader scroll by itself?

Yes, in the long strip modes. Turn on More > Settings > Experimental > **Auto-scroll in long
strip**, then tap the play button in the reader's menu. See [The reader](reader.md#auto-scroll).

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

### Can extensions update themselves?

Yes, once a day on Wi-Fi or another unmetered network, with More > Settings > Experimental >
**Update extensions automatically**. An update signed with a different key still waits for you. See
[Extensions](extensions.md#updating-extensions-automatically).

### Can I search Saikou from another app?

Yes, once you turn on More > Settings > Experimental > **Open shared text and search requests**.
Share a title or a page of a source's site to Shin Saikou. See
[Browse and sources](browse.md#searching-from-other-apps).

### Why do sources fail behind my ad blocker or at work?

If they fail with "Trust anchor for certification path not found" while the same sites open in your
browser, the network inspects secure connections with a certificate installed on your device, and
Saikou does not trust that certificate for sources by default. See
[Troubleshooting](troubleshooting.md#sources-fail-behind-an-ad-blocker-a-dns-filter-or-a-work-network)
before turning on **Trust certificates you installed**.

### How do I uninstall an extension?

On Browse > Extensions, long press the extension, or open it and tap **Uninstall**. See
[Extensions and repositories](extensions.md#uninstalling).

## Settings

### How do I find a setting?

Tap the search button above the list in More > **Settings** and type. See
[Settings reference](settings.md#searching-settings).

### How do I report a bug?

Tap the logo at the top of the More tab to open **About**, then **Share bug report**, **Copy device
info** or **Report an issue**. See [Reporting a problem](troubleshooting.md#reporting-a-problem).

### Why are screenshots blocked?

**Secure screen** is on, or set to **Incognito** while incognito is on. Change it in More >
Settings > **Security and privacy**.

### What is DNS over HTTPS?

A way to look up site addresses over an encrypted connection instead of your network's DNS, which
can get around simple blocks. Set it in More > Settings > Advanced > **DNS over HTTPS (DoH)** and
restart the app.
