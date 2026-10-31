# Sync between devices

Sync keeps your library the same on your phone, tablet and any other device running Saikou. Read a
chapter on one and the others know. This is one of Saikou's own features.

Sync goes through storage you already own: your Google Drive, or a WebDAV server. Saikou has no
server of its own.

## What sync carries

- Your library entries, with each entry's notes, manual order, reading mode and chapter list
  settings.
- Categories.
- Chapter progress (read, page reached), reading history, bookmarks and page notes.
- Tracking links.
- Each entry's scanlator filter and group ranking.

What stays on each device: settings, extensions and their repositories, source settings, tracker
sign-ins and downloaded chapters. Install the extensions you need on each device.
<!-- FIXABLE: F17 -->

## Setting it up

Open More > Settings > **Sync** and choose a **Sync service**.

### Google Drive

1. Choose **Google Drive** and tap **Sign in with Google**.
2. Google's sign-in page opens in your browser. Sign in and approve. A notification lets you jump
   back to Saikou.
3. Back in Saikou, the **Google account** row shows the account.

Saikou asks only for access to its own hidden app folder in your Drive. It cannot see or change your
other files, and the folder does not appear in your Drive's file list.

A Google sign-in does not expire. If you signed in during testing, before 24 October 2026, Saikou
still shows an end date for that sign-in: "Google's sign-in for this device expires on ...". A
day before that date Saikou posts a notification, **Google sign-in for sync ends soon**; tap
**Sign in again** to open the sync settings, then tap **Sign in with Google again** once and the
date goes away for good. Signing in again with the same account continues where the device left
off.

The Google Drive choice appears when this build of Saikou offers it.

### WebDAV

For your own server or a storage provider that offers WebDAV.

1. Choose **WebDAV**.
2. Enter the **Server address** (it must start with `https://`), your **User name** and
   **Password**.
3. Tap **Sign in**.

Saikou only accepts certificates your device trusts, and never sends your library over plain
`http://`. If the server redirects to another address, Saikou says so; enter the final address
instead.

## When sync runs

- On the schedule set in **Automatic sync**: **Off**, **1 h**, **6 h** (the default), **12 h** or
  **24 h**.
- When you open the app, if the last successful sync is more than a few minutes old.
- When you leave the app with changes not yet sent.
- Shortly after you close the reader.
- When you tap **Sync now**.

If background syncs do not run, tap **Allow background sync** (shown until Saikou may ignore battery
optimisation).

**Last sync** shows when the last run finished, or when and why it failed, with the last successful
sync below it.

When a background sync stops for a reason you can fix, Saikou posts a **Sync stopped**
notification saying why: the device lost its sign-in, Google no longer accepts it, the server
refused the saved password, or Google Drive is full. Tap it (or **Sign in again** / **Open sync
settings**) to go to the sync settings. Each reason is posted once, and the notification goes
away after the next successful sync. A sync that failed because the network or the server was
down posts nothing: the next sync tries again. A sync you start with **Sync now** shows its error
under **Last sync** instead.

A running sync and these notices have their own notification channels (**Sync progress** and
**Sync errors**), so you can silence one in Android's settings without the other.

## The first sync

The first time a device syncs with an account or server, it pulls everything already there, merges
it into its own library, then uploads its whole library once. After that, each sync sends and
receives only what changed.

When two devices change the same thing between syncs, both end up with the same result:

- Reading progress takes the side that got further. A chapter read on either device stays read.
- Settings you choose on an entry (its categories, reading mode, notes) take the most recent change.
- Details that come from the source are settled by the same rule on every device, so both end up
  with the same copy.

### The safety backup

Before a device's first sync, Saikou writes a backup of that device's library into its automatic
backup folder, so nothing can be lost by joining. The Sync section names the file. Saikou keeps it
until two later sign-ins have each written a newer one.

The notice in More > Settings > Sync ends with **Save a copy**, which opens Android's save dialog
and copies the file wherever you choose. The file is also listed under More > **Backup** >
**Automatic backups** as a **Sync safety backup**, to restore or copy. With a **Storage
location** set, the automatic backup folder is its `autobackup` folder, which you can open
yourself. See [Storage location](backups.md#storage-location).

## Sync reports

- **Last sync report** shows the library before and after the run (entries, categories, read
  chapters, bookmarks), how many routine merges there were, and any **conflicts**: changes made on
  this device that met a change from another device, each naming the entry and the fields where the
  other device's value won.
- **Earlier runs** keeps the reports of previous syncs.

## Checking that two devices agree

**Library fingerprint**: tap it to compute a short code from everything this device syncs. Two
devices that have both finished syncing show the same code. If they differ, tap **Sync now** on
both and compare again.

## Signing out

**Sign out** ("Stop syncing this device") forgets the account or server details on this device.
Your library on this device and Saikou's files in your Drive or on your server stay as they are.
For Google Drive, signing out also revokes Saikou's access to your account.

If you sign in again later, this device joins as a new device: it pulls everything from that
account or server, then uploads its whole library once. A different Google account, server or
user name works the same way.

## Messages you may see

- **Update Saikou on this device to keep syncing**: another device wrote a newer sync format.
- **Signed out of the sync server. Sign in again to keep syncing.** / **The server refused the saved
  password.**: enter the password again; the device keeps its place on the server.
- **Google no longer accepts this device's sign-in**: tap **Sign in with Google again**.
- **Google Drive is full**: free some space in the Google account, then sync again.
- **The sync server did not answer**: check that the server is running and reachable from this
  device.
- **The backup Saikou writes before the first sync could not be written**: nothing was synced. Check
  free space on the device, then sync again.
