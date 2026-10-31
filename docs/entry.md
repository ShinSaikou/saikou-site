# An entry's page

Tap any entry, in your library or while browsing a source, to open its page: its details, its
chapter list and everything you can do with it.

## The header

- The **cover**. Tap it to view it full size, with **Share** and **Save**. For library entries and
  Local source entries there is also **Edit cover**: **Choose an image** (pick any picture on the
  device as the cover) and **Delete custom cover** (go back to the source's cover). A custom cover
  stays on this device: backups and sync do not carry it. A saved cover goes to your gallery's
  **Pictures/Saikou** folder, never into an entry's sub-folder. On Android 8 and 9 it goes to
  Saikou's own pictures folder instead (`Android/data/com.shinsaikou/files/Pictures`), which the gallery
  does not show; use **Share** there.
- The title, the author (**By ...**), the source (**Source: ...**, or **Source not installed** when
  its extension is missing) and the status (**Ongoing**, **Completed**, **On hiatus** and so on).
- The description. Tap **More** to expand it and **Less** to fold it.
- **Add to library** or **Remove from library**.
- The **Tracking** button, which shows how many trackers the entry is linked to. See
  [Tracking](tracking.md).
- **Continue reading** opens the next unread chapter.

Pull the page down, or use the overflow menu's **Refresh**, to fetch the latest details and
chapters from the source.

## The top bar

- **Download** (the arrow icon) queues chapters: **Next chapter**, **Next 5 chapters**, **Next 10
  chapters**, **Next 25 chapters**, **Unread** or **Bookmarked**. See [Downloads](downloads.md).
- **Filter** opens the chapter settings (below).
- The overflow menu:
  - **Refresh**: the same as pulling down.
  - **Reading mode**: this entry's own reading mode and rotation, which override the defaults in
    More > Settings > Reader. See [The reader](reader.md).
  - **Edit details**: your own **Title** and **Description** for this entry. **Reset** brings back
    the source's text.
  - **Migrate**: move the entry to another source, keeping your progress. Shown for library
    entries. See [Migration](migration.md).
  - **Open in WebView**: open the entry's page on the source's site, inside Saikou. Shown when the
    source has a website.

Your edited title and description stay when the source changes its own. Saving the source's text
again removes the edit.

## The chapter list

Each row shows the chapter's name or number, its date, its scanlator group, and **Page: N** when
you stopped part of the way through. Read chapters are dimmed, bookmarked chapters are marked.

- **Tap** a chapter to read it.
- **The download control** at the end of a row queues the chapter. On a queued or downloading
  chapter it offers **Start downloading now** and cancel; on a downloaded chapter, delete.
- **Swipe** a row left or right for a quick action. Choose the actions in More > Settings >
  Library > **Chapter on swipe to left** and **Chapter on swipe to right**: **Disabled**, **Bookmark
  chapter**, **Mark as read** or **Download**. On a downloaded chapter, the download swipe deletes
  the download instead.
- **Long press** to start selecting. Long press a second chapter further down and every chapter
  between the two is selected too, so chapters 1 to 50 take two long presses. The bar then offers
  **Bookmark chapter** or **Unbookmark chapter**, **Mark as read**, **Mark as unread**, **Mark
  previous as read**, **Download** and **Delete downloads**, plus **Select all**, **Invert
  selection** and **Deselect all**.

When you mark chapters as read by hand and the entry is tracked, Saikou can ask **Update trackers to
chapter N?**, depending on More > Settings > Tracking > **Update progress when marked as read**.

## Chapter settings

The **Filter** icon opens **Chapter settings** with three tabs.

**Filter**

- **Downloaded**, **Unread** and **Bookmarked**, each off, include or exclude.
- **Filter scanlator groups**: tick the groups whose chapters you want to see. The same dialog
  ranks the groups: **Move up** and **Move down** set which group you prefer, and **Reset order**
  clears the ranking.

When a chapter exists from several groups, the ranking decides which copy **Continue reading**
opens and which copy the reader moves to next. With no ranking, no group is preferred.

**Sort**

**Source order**, **Chapter number**, **Upload date** or **Alphabetically**. Tap the active sort
again to reverse it.

**Display**

- **By chapter name** or **By chapter number**.
- **Group by volume**: headers such as **Volume 3** above each volume's chapters.

**Set as default** makes these settings the default for entries you add later. Tick **Also apply to
all entries in my library** to change every library entry now as well. **Reset** brings this entry
back to the default.

## Downloading from an entry outside your library

If you download chapters of an entry that is not in your library, Saikou asks **Add to library?**
so the download is not forgotten. You can say no; the files are then listed under
More > Settings > Data > **Downloads not in library**.
