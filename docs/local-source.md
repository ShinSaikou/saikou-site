# The Local source

The **Local source** reads comics and manga stored on your device: folders of images and comic
archives you already have. It is built in and needs no extension. You find it under **Browse >
Sources > Local source**, and its entries can be added to your library like any other, marked with
the **Local** badge.

## Where Saikou looks

With a **Storage location** set (More > Settings > Data > **Storage location**), Saikou reads the
`local` folder inside it, for example `Saikou/local`. Any file manager can open it, and it stays
when Saikou is uninstalled. Choosing the storage location moves the series already in Saikou's own
folder there; entries in your library keep working, covers included. If you later choose a
different folder, Saikou moves the backups, Local series and exported downloads it put in the first
folder into the new one, and tells you first how much that is. On the same storage this is
immediate; across storages it copies in the background with a notification. Entries in your
library keep working, covers included. See [Storage location](backups.md#storage-location).

Without one, Saikou reads `Android/data/com.shinsaikou/files/local`, which many file managers cannot
open on Android 11 and later and which is deleted with the app.

When the Local source has nothing to show, its listing says which folder it reads ("No Local
series in <folder>. Put series folders there, or choose another folder.") with a **Choose
folder** button.

Put one folder per series inside `local`.

### Without a storage location

Ways to get files into `Android/data/com.shinsaikou/files/local`:

- Connect the phone to a computer with a USB cable and copy the files into that folder from the
  computer; this often works where on-phone file managers cannot.
- Use a file manager that can still open `Android/data` on your device.

## Folder layout

Each series is a folder inside `local`, named after the series. Each chapter is either a folder of
images or one archive file inside the series folder.

```
local/
  Series title/
    cover.jpg
    ComicInfo.xml          (optional, see below)
    Chapter 1/
      001.jpg
      002.jpg
    Chapter 2.cbz
    Chapter 3.zip
```

- **Image folders**: a folder of pictures is one chapter.
- **Archives**: `.zip`, `.cbz`, `.rar`, `.cbr`, `.7z`, `.cb7`, `.tar` and `.cbt`. One archive is one
  chapter, named after the file. Folders inside an archive are ignored; every image in it becomes a
  page of that chapter.
- **EPUB**: an `.epub` file is read as one chapter of images. Saikou does not split an EPUB into
  several chapters.

Image folders and `.zip` / `.cbz` archives open the fastest.

When you add files to a series later, pull down on its page to read the folder again and see the
new chapters.

## Covers

Put an image named `cover` (for example `cover.jpg` or `cover.png`) in the series folder and Saikou
uses it as the cover. Without one, Saikou takes the first page of the first chapter.

You can also set a cover from inside the app: on the entry's page, tap the cover, then **Edit
cover > Choose an image**, or long press a page in the reader and tap **Set as cover**. For a Local
source entry, Saikou writes the chosen image into the series folder as its cover.

## Series details

Saikou reads a series' title, author, artist, description, genres and status from a `ComicInfo.xml`
file, the standard metadata file many comic tools write. It looks in this order:

1. A `ComicInfo.xml` in the series folder.
2. A JSON details file in the series folder (an older format, often named
   `details.json`). Saikou converts it to `ComicInfo.xml` the first time it reads it, then removes
   the JSON file.
3. The first `ComicInfo.xml` found inside one of the chapters. Saikou copies it into the series
   folder.

A JSON details file looks like this:

```json
{
  "title": "Example Title",
  "author": "Example Author",
  "artist": "Example Artist",
  "description": "Example description.",
  "genre": ["genre 1", "genre 2"],
  "status": 1
}
```

`status` is a number: 0 Unknown, 1 Ongoing, 2 Completed, 3 Licensed, 4 Publishing finished,
5 Cancelled, 6 On hiatus.

If a series folder has no details file at all, Saikou leaves a small `.noxml` marker file there so
it does not search the chapters again on every refresh. Adding a `ComicInfo.xml` later replaces
the marker.

## Sorting the Local source

Browsing the Local source lists every series at once. Its **Filter** offers **Order by** **Title**
or **Date**.

## Questions

**The series does not show up.** Check that each series is a folder directly inside `local`, and
that the chapters are folders of images or supported archives inside the series folder.

**A cover is missing or wrong.** Check that the series opens and its chapters read. Then add a
`cover` image to the series folder, or set one from the entry's page, and pull down on the page to
refresh.
