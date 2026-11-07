# Backups and restore

A backup is a single file holding your library, your reading progress and, if you choose, your
settings. Keep a recent one somewhere other than your phone: it is what brings everything back
after a lost phone, a reinstall or a mistake.

Saikou's backups use the common `.tachibk` format: Saikou restores backups from other readers that use
it, and those readers can restore Saikou's.

The **Backup** screen has two tabs, **Create** and **Restore**.

## Creating a backup

1. Open More > **Backup** (also reachable from More > Settings > Data > **Create backup**).
2. On the **Create** tab, tick what to include. Everything except **Private settings** is ticked
   by default:
   - **Library entries**, **Categories**, **Chapters** (which you have read and bookmarked),
     **Tracking**, **Reading history**
   - **Entries read outside the library**: history of entries you read without adding them
   - **App settings**, **Extension stores** (your repository list), **Source settings**
   - **Private settings**: your tracker sign-ins. Leave it off and the file contains none, which
     looks the same as never having signed in.
3. Tap **Create backup** and choose where to save the file, for example a folder that your cloud
   storage app uploads, or your Downloads folder to copy to a computer.

A moving bar under the button shows for as long as the backup is waiting or working, and the tab
then says whether it finished or failed. A notification says **Backup created**, with **Share** to
send the file somewhere straight away.

### What a backup does not contain

- The extensions themselves (only the list of repositories, with **Extension stores**). A restore
  can install them again, see [Install extensions](#install-extensions).
- Downloaded chapters. See [Downloads](downloads.md#where-downloads-are-kept).
- Custom covers you set on entries.
- Your sync settings and sign-ins.
- [Merged entries](merged-entries.md): every entry and its chapters are kept, but not the merge. A
  restore brings them back as separate entries.

## Automatic backups

More > Settings > Data > **Automatic backup interval**: **Off**, **12 h** or **24 h**. It is set to
12 hours on a new install. **Last automatically backed up** shows when the last one ran. Saikou
keeps the newest four.

Automatic backups go to the `autobackup` folder of your **Storage location** (More > Settings >
Data > **Storage location**), a folder on your phone that you choose and that stays when Saikou
is uninstalled. Until you choose one, they are kept inside Saikou's app storage and are deleted
with the app; the **Restore** tab says so, with a **Choose folder** button.

The **Restore** tab of More > **Backup** lists the kept files under **Automatic backups**, newest
first, each with its date, its kind (**Automatic backup** or **Sync safety backup**) and its size.
Tap one to **Restore** it (the same restore as a picked file, with the options ticked at the top of
the tab) or to **Save a copy** somewhere else. This works with or without a storage location. On a
new phone or after a reinstall, choose the same folder as the storage location, or pick a file from
its `autobackup` folder with **Restore backup**.

If the folder cannot be reached any more (deleted, or access removed), backups are written inside
the app again and nothing is lost; the **Storage location** row says "<folder> cannot be reached.
Tap to choose it again".

### Storage location

More > Settings > Data > **Storage location** opens Android's folder picker. Saikou makes three
folders in the one you choose: `autobackup`, `local` and `downloads`. If Saikou already holds
automatic backups or Local series, it asks first ("4 backups and 12 Local series will be moved to
<folder>") with **Move** and **Cancel**. **Cancel** keeps the previous setting.

If you later choose a different folder, Saikou moves the backups, Local series and exported
downloads it put in the first folder into the new one, and tells you first how much that is, for
example "4 backups, 12 Local series and 3100 exported chapters will be moved from Saikou to SD card
(12.4 GB)". On the same storage this is immediate; across storages it copies in the background
with a notification. If the new folder's storage does not have room, the dialog says "<folder>
does not have 12.4 GB free" and **Move** is off; choose another folder or free some space first.
Files Saikou did not create, such as a backup you saved there yourself, stay in the first folder.

If a file cannot be moved, it stays where it was (in the app or in the first folder), the
notification says how many and where, and **Move to the storage location** appears under the row
to try again. Downloads themselves stay in the app; see [Downloads](downloads.md) for copying them
out.

## Restoring a backup

1. Before restoring on a new install, [add the extension repositories](extensions.md#adding-a-repository)
   you trust, if you can:
   [Install extensions](#install-extensions) only installs from repositories that were there before
   the restore. Entries restore either way; those whose extension is missing show **Source not
   installed** until you install it.
2. Open More > **Backup** and go to the **Restore** tab. Tick what to restore: **Library entries**,
   **Categories**, **App settings**, **Extension stores**, **Source settings** and **Install
   extensions**.
3. Tap **Restore backup** and pick the file (`.tachibk`, or `.proto.gz` as some exports are
   named). The restore starts right away, with the options ticked above the button. Extensions and
   tracker sign-ins the backup needs are listed in the [restore report](#the-restore-report)
   afterwards.

Opening a `.tachibk` file with Saikou from a file manager opens the **Restore** tab and asks first.
Saikou reads the file, then shows it with the sources and trackers it refers to that this device
lacks or is not signed in to, and **Restore** and **Cancel**. The restore starts only on
**Restore**.

The restore runs in the background with a **Restoring backup** notification, which has **Cancel**.
A moving bar under the button shows for as long as the restore is waiting or working, with its own
**Cancel**, and says how far it is (**Categories**, **Settings**, **Extension stores**, **Entries**,
**Installing extensions**). The tab then says whether it finished, failed or was cancelled. If
Android stops the app part way, the restore carries on from where it was.

Restoring into a library that already has entries merges the two. Read chapters, bookmarks and
reading progress never go backwards, so restoring an older backup cannot undo reading you did
since. Restoring the same file twice changes nothing the second time.

### Install extensions

**Install extensions** on the **Restore** tab is on by default. Once the library is back, the
restore reads your repositories (called extension stores on this screen) and installs each
extension the backup's sources come from that it finds there, one after another, showing which of
how many it is on.

It installs only from the repositories you had before the restore, so a backup someone else made
cannot install anything on its own. An extension that only a repository added by the backup offers
is not installed: the **Restore** tab and the restore report name that repository and its address,
and **Install all** installs those extensions once you have checked it.

### The restore report

When a restore ends, the notification says **Restore complete**, how many entries could not be
restored, how many extensions were installed or wait for **Install all**, or how many sources need
an extension. Tap it, or tap **Restore report** on the **Restore** tab, for:

- The counts: entries restored, merged with entries already in the library, and not restored.
- **Extensions**, when **Install extensions** was on: what was installed (**Installed**), what
  could not be (**Could not be installed**), the sources no repository lists, by name, so you know
  what to search for (**Not in any extension store**), and the extensions waiting under **From
  stores this backup added**, with each repository's name and address and **Install all**.
- **Missing sources**: the sources with no extension, each with **Install** when one of your
  repositories offers it, or **Open Extensions**. When several can be installed, **Install all**
  above the list installs whatever is still offered, for a restore made with **Install extensions**
  off too.
- **Trackers not logged into**, each with **Sign in**.
- **Copy downloads from a folder**, since a backup holds no downloads.
- **Errors**, with **Export error log**.

After a restore:

- If you also had downloads in another reader, or exported Saikou's own, copy them now with More > Settings >
  Downloads > **Copy downloads from a folder**. See
  [Downloads](downloads.md#copying-downloads-from-a-folder).

### Files Saikou cannot restore

- **"This is a JSON backup from an old release."** Very old apps wrote backups as JSON, which
  Saikou does not read. Restore the file in an app that reads it, create a new backup there, then
  restore that one in Saikou.
- **"This file could not be read as a backup."** The file is damaged or is not a backup. Try
  another copy.

## Backups and sync

[Sync](sync.md) keeps your library the same on several devices. It does not replace backups: a
mistake on one device syncs to the others. Before a device's first sync, Saikou writes a safety
backup automatically, see [Sync between devices](sync.md#the-safety-backup).

## Good habits

- Create a backup by hand before big changes: a migration of many entries, a restore, setting up
  sync, or moving to a new phone.
- Keep at least one backup off the phone.
- Saikou is young (version 0.1.3). Back up regularly so a problem in a new release costs you nothing.
