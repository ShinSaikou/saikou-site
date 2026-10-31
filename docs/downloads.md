# Downloads

Downloaded chapters open without a network connection, load faster, and keep working even if the
extension they came from is uninstalled.

## Downloading chapters

- **From an entry's page**: the **Download** button in the top bar (**Next chapter**, **Next 5
  chapters**, **Next 10 chapters**, **Next 25 chapters**, **Unread**, **Bookmarked**), the download
  control at the end of a chapter row, or **Download** after selecting chapters.
- **From the library**: select entries and tap **Download** for the same choices across all of
  them.
- **From the Updates tab**: the download control on a chapter row.
- **Automatically**: see [Automatic downloads](#automatic-downloads) below.

Downloading an entry that is not in your library asks **Add to library?**.

## The download queue

More > **Download queue** lists the chapters waiting to download and any that failed.

- **Start** and **Pause** run or hold the queue.
- **Cancel download** removes one chapter; **Clear queue** removes them all.
- Each row shows **Queued**, **Starting**, **N of M pages**, or **Failed** with the reason.

Chapters download one at a time, in the order they were added. Within a chapter, several pages
download at once: More > Settings > Downloads > **Pages downloaded at once** (1 to 15, 5 by
default). Each page goes through the source's own rate limit, so a higher number speeds up only
sources that allow it.

Download progress and failures appear as notifications (**Download progress** and **Download
errors** channels).

## Download settings

In More > Settings > Downloads:

- **Only download over Wi-Fi** (on by default). Takes effect the next time downloads start.
- **Pages downloaded at once**, above.

### Delete chapters

- **After manually marked as read**: delete a chapter's download when you mark it read by hand.
- **After reading automatically delete**: **Disabled**, or delete the **Last read chapter**, the
  **Second to last read chapter**, and so on up to the fifth, counted back from the chapter you
  just finished.
- **Allow deleting bookmarked chapters**: off by default, so bookmarked chapters are kept.
- **Excluded categories**: entries in these categories keep every downloaded chapter.

### Automatic downloads

- **Download new chapters**: queue the new chapters a library update or a refresh finds for library
  entries.
  - **Skip downloading duplicate read chapters**: leave out a new chapter whose number you have
    already read (for example, the same chapter from a second group).
  - **Categories**: which categories get automatic downloads. An entry in an excluded category is
    never downloaded automatically, even if it is also in an included one.
- **Auto download while reading**: **Disabled**, or the **Next 2**, **3**, **5** or **10 unread
  chapters**. Once you are a quarter of the way into a chapter, Saikou queues that many of the
  following unread chapters.

**Auto download while reading** works for any entry in your library, whether you read it online
or from a download: a quarter of the way into a chapter, the next 2, 3, 5 or 10 unread chapters
(your choice) are queued, leaving out those already downloaded or in the queue. **Only download
over Wi-Fi** still applies. Entries that are not in your library are not downloaded ahead.

## Where downloads are kept

Saikou keeps downloads in its own app storage on the device. That has three effects:

- Downloaded pages never show up in your photo gallery, and no other app can read or change them.
- You do not choose a folder, and there is no storage permission to grant.
- Uninstalling Saikou, or clearing its storage in Android's settings, deletes the downloads. They
  are not part of a backup, and Android's phone-to-phone transfer does not carry them.

To keep your downloads through a reinstall or take them to a new phone, use More > Settings >
Downloads > **Export downloads**. It copies every downloaded chapter into the `downloads` folder
of your **Storage location** (it asks you to choose one first if none is set), in the layout other
Tachiyomi-compatible readers use, with a progress notification. Chapters already there are skipped, so running it
again copies only what is new, and an export that stopped carries on. Your downloads stay in
Saikou; this is a copy. The row then shows "Last export: N copied, N already there, N not copied".

On the new phone or after reinstalling, restore your backup, then use **Copy downloads from a
folder** (below) and pick the storage location folder or its `downloads` folder.

More > Settings > Data shows the space in use: **Storage usage** ("Downloads: ... Chapter cache:
..."), with the device's free space.

### Downloads not in library

Removing an entry from your library keeps its downloads, so nothing is lost by accident. More >
Settings > Data > **Downloads not in library** lists every entry that still has downloads but is no
longer in the library, with the number of chapters and their size. Select entries there to delete
their downloads. If you add the entry back instead, its downloads are used again.

### Unmatched downloads

Sometimes a source renames or renumbers chapters, so a downloaded chapter no longer matches any
chapter of its entry. Saikou tries to match it again each time it starts; downloads that still match
nothing are counted under More > Settings > Downloads > **Unmatched downloads**. **Delete** shows
which chapters they are and asks before removing them. They may not be downloadable again, so
check the list first.

### Downloads after a source or title change

Saikou finds a download even when the source has renamed itself or the entry's title has changed,
and whichever way **Disallow non-ASCII filenames** (More > Settings > Advanced) is set. You never
need to rename anything by hand.

## Copying downloads from a folder

Saikou can copy the chapters you downloaded in another reader that uses the same layout, or exported
from Saikou with **Export downloads**, so you do not download them again.

1. First restore your backup, the other reader's or Saikou's (see [Backups and restore](backups.md)). Only
   chapters of entries already in Saikou's library are copied.
2. Open More > Settings > Downloads > **Copy downloads from a folder**.
3. Pick the other reader's folder: either its main storage folder or the `downloads` folder inside it, or a
   folder that Saikou's **Export downloads** wrote.

Saikou only reads the folder; it never changes or deletes anything there. Progress appears as a
notification (**Copying downloads from a folder**). If the copy stops part way, the row says so;
pick the same folder again and it carries on with the rest, skipping what it already copied.

When it finishes, **Last copy from a folder** shows the result: how many chapters were copied, were
already here, were not matched, and could not be copied, each with the folder and the reason.

A chapter is **not matched** when Saikou cannot pair it with an entry and chapter in your library.
**Last copy from a folder** (More > Settings > Downloads) lists them by reason, each with what to
do: **Source not installed**, with **Install** when one of your repositories offers the extension,
or **Open Extensions**; **Not in your library**, with **Search**, which looks the title up across
your sources so you can add it; chapters with no match in an entry's chapter list, with **Open
entry**, where you can refresh the list. Unfinished downloads and second copies of a chapter are
listed too; they need nothing. Then tap **Copy again**: chapters already copied are skipped. If
Saikou can no longer read the folder, it asks you to pick it again.

## Downloaded only

**Downloaded only** in the More tab's **Quick controls** limits the app to what you have downloaded,
for reading offline. While it is on, the library's **Downloaded** filter is forced on.
