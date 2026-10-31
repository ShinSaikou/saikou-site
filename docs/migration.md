# Migration

Migration moves an entry from one source to another while keeping your progress. Use it when a
source stops working, is slower than another, or another source has chapters it lacks.

Create a backup before migrating many entries at once (More > **Backup**), in case you want to go
back. See [Backups and restore](backups.md).

## Migrate or copy

At the end of every migration you choose:

- **Migrate**: the new entry takes the old one's place. The old entry leaves your library; the new
  one keeps its date added and its position in your manual order.
- **Copy**: the new entry is added to your library and the old one stays too.

## What moves to the new entry

Choose under **Select data to include** (one entry) or **Data to migrate** (several):

- **Chapters**: read and bookmarked marks, matched by chapter number. A chapter read on the old
  entry is read on the new one; nothing read is ever marked unread.
- **Categories**.
- **Custom cover**: the cover you set on this device.
- **Downloaded chapters**: the old entry's downloads follow it to the new entry's chapters with the
  same chapter number, so you can keep reading offline without downloading again. Shown when the
  entry has downloaded chapters. See [Downloads and migration](#downloads-and-migration).
- **Notes**: the entry's notes, when it has any.

Always carried: tracking links (and any tracker update still waiting to be sent), the entry's
reading mode and chapter list settings.

Not carried: page notes and the scanlator group ranking and filter, because they refer to the old
source's chapters and groups.

## Migrating one entry

1. Open the entry's page (it must be in your library) and tap overflow > **Migrate**.
2. Choose the sources to search, then **Continue**. Saikou opens a search across them.
3. Tap the entry you want to move to.
4. Tick what to include and tap **Migrate** or **Copy**.

You can also start from the duplicate question: when you add an entry and Saikou says it is
**Already in your library** from another source, tap **Migrate** to move your progress from the
old one to the one you are adding.

## Migrating many entries

Start in either place:

- In the library, select entries and tap **Migrate**.
- **Browse > Migrate**: pick the source to migrate from (sort the list **Alphabetically** or by
  **Total entries**), then select its entries.

Then:

1. **Choose the target sources.** Sources under **Selected** are searched in that order; drag them
   to reorder. **Select none**, **Select enabled sources** and **Select pinned sources** are
   shortcuts. Tap **Continue**.
2. **Set the options** in the sheet:
   - **Data to migrate**, as above.
   - **Delete downloads of current entry after migration**.
   - **Additional keywords (optional)**: words added to every search, to narrow the results.
   - **Hide entries without a match** and **Hide entries without newer chapters** ("Only show
     entry if the match has additional chapters").
   - **Advanced search mode** (search with the title broken into keywords) and **Match based on
     chapter number** (pick the match furthest ahead rather than the first by source order). These
     two send many more searches and are slow; sites may start refusing requests if you use them
     on a large batch.
3. Tap **Continue**. The **Migration** screen searches for a match for each entry and shows its
   progress in the title.

On the Migration screen each row shows the old entry and the match found, with the match's
**Latest** chapter, or **No alternatives found**. For each row you can **Search manually**, choose
**Don't migrate**, or **Migrate now** / **Copy now**. The top bar migrates or copies everything at
once, after **Migrate N entries?** or **Copy N entries?**.

A match with no chapters cannot be used ("No chapters found, this entry cannot be used for
migration"), and an entry that is itself part of the batch cannot be a target. Entries that fail
stay in the list so you can try them again or search by hand.

## Downloads and migration

With **Downloaded chapters** ticked (it is on unless you turn it off), each downloaded
chapter of the old entry goes to the new entry's chapter with the same number. When several
chapters share that number, the one from the same scanlator group is used, else the first in the
source's list. A chapter the new entry has already downloaded keeps its own download.

- **Migrate** moves the files, so the old entry's downloads become the new entry's.
- **Copy** copies them: the old entry, which stays in your library, keeps its own.

A downloaded chapter with no match in the new entry (no chapter with that number, or a chapter
without a number) cannot be moved. After a **Migrate**, Saikou says how many: "3 downloaded chapters
could not be moved to the new entry". Tap **Delete them** to remove those files, or **Keep them**.
When migrating many entries, the Migration screen shows the count for the whole batch with
**Delete them**. Kept chapters are listed under More > Settings > Data > **Downloads not in
library**, where you can delete them later.

With **Delete downloaded** (one entry) or **Delete downloads of current entry after migration**
(several) ticked, the chapters that could not be moved are deleted without asking. This works
whether or not the old entry's extension is still installed.

If you untick **Downloaded chapters**, Saikou does not move the old entry's downloads. After a
**Migrate** it tells you how many stay on the device ("3 downloaded chapters of the old entry
stay on this device") and offers **Delete them** or **Keep them**; when migrating many
entries, the Migration screen shows the count for the whole batch with **Delete them**. Kept
ones are listed under More > Settings > Data > **Downloads not in library**. A **Copy** says
nothing, since the old entry stays in your library with its downloads.
