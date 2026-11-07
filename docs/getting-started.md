# Getting started

What you need to get from a fresh install to reading your first chapter.

## Installing Saikou

[Download the latest APK](https://github.com/ShinSaikou/saikou/releases/latest/download/app-release.apk)
and open it. The first time, Android asks you to allow the app you opened it from (usually your
browser or file manager) to install apps. Release notes and earlier versions are on GitHub,
<https://github.com/ShinSaikou/saikou/releases>.

On your phone the app is called **Shin Saikou**, so look for that name on your home screen, in your
app list or in the phone's search. These pages call it Saikou.

Saikou needs Android 8.0 or later.

## The first launch

Two questions may appear:

- **Notifications** (Android 13 and later). Saikou posts library update progress, new chapters,
  downloads and backups as notifications. If you decline, the app still works; you just will not
  see those.
- **Keep background work running.** Library updates and backups run in the background, and
  Android can stop them to save power. **Allow** asks Android to let Saikou run unrestricted;
  **Skip** leaves it as it is. You can change this later in More > Settings > Advanced >
  **Allow background work**.

The app opens on the **Library** tab, which is empty at first. The bottom bar has five tabs:
**Library**, **Updates**, **History**, **Browse** and **More**. A long press on the app icon offers
shortcuts to Library, Updates, History and Browse.

## Coming from another reader

If you already use a reader that makes `.tachibk` backups, you do not have to start over:

1. In that reader, create a backup (usually More > Settings > Data and storage > Create backup).
2. In Saikou, open More > **Backup**, go to the **Restore** tab, tap **Restore backup** and pick
   that `.tachibk` file. The restore starts right away. Opening the file with Saikou from a file
   manager also works: it opens the **Restore** tab and asks first. See
   [Backups and restore](backups.md).
3. Get the extensions your library uses. The backup carries your repositories when **Extension
   stores** was included. Once you have checked them, **Install all** on the **Restore** tab
   installs their extensions. If you add a repository in Saikou before restoring, **Install
   extensions** installs from it during the restore. See
   [Install extensions](backups.md#install-extensions).
4. To bring your downloaded chapters over as well, open More > Settings > Downloads >
   **Copy downloads from a folder** and pick that reader's folder. Do this after the restore: only
   chapters of entries already in your library are copied. See
   [Downloads](downloads.md#copying-downloads-from-a-folder).

## Adding content

Saikou does not come with any content. There are two ways to add some.

### Files on your device

The **Local source** reads comic archives and image folders stored on the device. See
[The Local source](local-source.md).

### Extensions from a repository

Extensions are small add-ons that each connect Saikou to one site. They come from repositories,
which are lists of extensions published by third parties.

1. Open More > **Extension repositories** (or Browse > Extensions, then the button shown when no
   repository is configured).
2. Under **Add a repository**, paste the repository's address into **Repository address** and tap
   **Add**.
3. Go to **Browse > Extensions**, where its extensions are already listed, and tap the install
   button at the end of an extension's row.

Extensions and repositories are made by third parties. An extension runs its code inside Saikou
and can see what Saikou can see, so only add repositories and extensions you trust. Saikou helps
with this: an extension signed by a key Saikou does not know is held under **Needs trust** until
you look at its signer and tap **Trust**. See [Extensions and repositories](extensions.md).

Saikou installs extensions inside the app itself. Android's "Install unknown apps" permission is
not needed for them.

## Adding an entry to your library

1. Open **Browse**. The **Sources** tab lists the sources of your installed extensions.
2. Tap a source. Use **Popular** or **Latest**, or the search field, to find something.
3. Tap an entry to open its page, then tap **Add to library**.

If you have made categories and no default category is set, Saikou asks which categories to put the
entry in. If an entry with the same title is already in your library from another source, Saikou
says so and offers **Add anyway**, **View chapters** (open the one you have) or **Migrate** (move
your progress to this source). See [Migration](migration.md).

## Searching every source at once

On the **Sources** tab of **Browse**, tap the search icon in the top bar (**Search all sources**).
Type a title and Saikou
searches every enabled source and shows the results source by source. **More from this source**
opens the full results of one source.

If you cannot find a title:

- Check the spelling, and try the romanized Japanese title as well as the English one. Sources
  often list a series under one or the other.
- Try a shorter part of the title. Sources spell and word titles differently.

## Where to go next

- [Library and categories](library.md) to organize what you add.
- [Library updates](updates.md) to get new chapters automatically.
- [Backups and restore](backups.md) before you invest time in your library.
