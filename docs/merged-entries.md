# Merged entries

A merged entry is one title from several sources: one row in the Library and one chapter list. A
chapter the first source lacks comes from the next one, so a title keeps working when a source
falls behind, and if a source's extension is removed, the other sources take over.

Merged entries are experimental. Turn them on in More > Settings > Experimental > **Merged
entries**.

## Merging

Any of these merges entries. Each source stays in your library as a whole entry of its own: its
chapters, downloads and update checks do not change.

- **From an entry:** open its menu and tap **Merge with...**. Saikou searches every source for the
  title. Tap a result and confirm with **Merge**. An entry that is not in your library yet is added.
- **From the Library:** long press an entry, tap one or more others, then choose **Merge** in the
  bar's menu. Pick the main entry. The entries' chapters are preferred in the order you selected
  them.
- **While adding a title:** when Saikou asks whether a title is already in your library, pick the
  entry and tap **Merge**. The entry in your library stays the main one.

The **main entry** stands for the title: its cover, details, reading mode and tracking.

## Chapters

The chapter list shows each chapter number once, from the first source in the order that has it. A
source whose extension is not installed comes last. Each row names its source. A chapter with no
recognised number is always listed.

- **By source** is not offered as a sort, because each source numbers its own list. A merged entry
  sorts by chapter number.
- A small mark on a row means another source's copy of that chapter is downloaded. With **Downloaded
  only** on, the reader uses that copy.
- A chapter read on one source counts as read on all of them, and marking a chapter unread does the
  same. Bookmarks and the page you reached stay with each copy.
- The reader moves from one source to the next without a break.

## Merged sources

Tap the source line on the entry's page, such as **Source A + 1 more**, to open **Merged sources**.

- Drag a source by its handle to set the order. The first source that has a chapter wins it.
- A source's menu has **Use as main entry**, **Check for updates** and **Remove**. With **Check for
  updates** off, library updates skip that source.
- **Show every copy** lists each source's copy of every chapter, for when the one shown is broken.
- **Unmerge** puts the sources back as separate entries. Chapters read while merged stay read.

## Everywhere else

- **Library:** one row, in every category any of its sources is in. The unread badge counts each
  chapter number once. **Move to category** changes every source's categories.
- **Updates and Upcoming:** one row per chapter or title, under the main entry's title.
- **Statistics:** a merged entry counts as one title.
- **Downloads:** each chapter downloads to its own source's folder. Automatic downloads take the copy
  the list shows.
- **Remove from library:** removes every source of the entry, after asking.
- **Migrate:** migrating a merged entry replaces its main entry and keeps the rest merged.

## Sync and backups

Merges sync between your devices, and every device needs a version of Saikou that knows the new sync
format. An older device says **Update Saikou on this device to keep syncing**.

A backup keeps every entry, its chapters and its read marks, but not the merge. After restoring, the
sources are separate entries until you merge them again.

A backup from TachiyomiSY keeps its merged entries when restored here, in the same source order.
Saikou shows them with its own rule: one copy of each chapter number, by source order. A merge set
to show every chapter in TachiyomiSY comes in with **Show every copy** on. The restore report says
how many came in, names any source the backup did not hold, and, if the **Merged entries** switch is
off, says they show as one once you turn it on.

## Turning it off

With the switch off, every source shows as its own entry and the Merge actions are gone. Your merges
are kept: turning the switch back on brings them back, and they still sync. The setting stays on
this device and is not in backups.
