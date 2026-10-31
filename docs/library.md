# Library and categories

The **Library** tab holds every entry you have added. Categories split it into tabs, and the
library's own sheet filters, sorts and lays it out.

## The Library tab

- **Search library** (the search icon) filters the current tab by title as you type.
- The **filter** icon opens the library sheet with three tabs: **Filter**, **Sort** and
  **Display**.
- The overflow menu (three dots) has **Update library**, **Update category** for the tab you are
  on, and **Stop update** while an update runs. See [Library updates](updates.md).
- Tap an entry to open its page. See [An entry's page](entry.md).

On a large screen the library can show the tapped entry's chapters in a second pane beside the
grid. More > Settings > Appearance > **Two pane layout** chooses when:
**Automatic**, **Always**, **Landscape** or **Never**.

## Filter

Each filter has three states: off, include (show only entries that match) and exclude (hide
entries that match). Tap a filter to move to the next state.

- **Downloaded**: entries with downloaded chapters. While **Downloaded only** is on in the More
  tab, this filter is forced on.
- **Unread**, **Started**, **Bookmarked**, **Completed**.
- **Custom update interval**: entries whose update interval you set by hand.
- **Tracked**: entries linked to a tracker. It appears once you are signed in to a tracker. See
  [Tracking](tracking.md).

When a filter hides everything, the tab says **No entries match the active filters**.

## Sort

**Alphabetically**, **Last read**, **Last entry update**, **Unread count**, **Total chapters**,
**Latest chapter**, **Date fetched**, **Date added**, **Tracker score** (shown once you are
signed in to a tracker) and **Random**. Tap the active sort again to switch between ascending and
descending.

By default one sort applies to every category. To give each category its own, turn on
More > Settings > Library > **Per-category settings for sort**.

### Your own order

To arrange entries by hand:

1. Turn on More > Settings > Library > **Manual ordering** ("Keep manually positioned entries
   first").
2. Open the Library with no search and no filter active, and with **Per-category settings for
   sort** off.
3. Drag an entry by its handle (**Drag to reorder**) to where you want it.

The handles are hidden while you search, filter or select, because the order you see then is not
the whole tab. Your manual order is carried by [sync](sync.md).

## Display

- Layout: **Compact grid**, **Comfortable grid**, **Cover only grid** or **List**.
- **Columns**: how many covers per row in a grid; **Auto** fits as many as the screen allows.
- Badges on each cover: **Unread badge**, **Downloaded badge**, **Local badge** and
  **Language badge**.
- **Category tabs**: show or hide the tab row.
- **Entry count**: show the number of entries next to each category name.
- **Continue reading button**: a button on each cover that opens the next unread chapter.

## Categories

Categories are tabs in your library, for example "Reading", "Plan to read" and "Finished". An
entry can be in several categories at once. Entries in no category appear under **Default**.

### Managing categories

Open More > **Categories**.

- **Add category**: type a name and tap **Add**. Two categories cannot share a name.
- Tap a category's menu for **Rename category**, **Delete category**, **Move up**, **Move down**,
  **Move under…** and **Move to top level**.
- Deleting a category never removes entries from the library. They stay in the library, without
  that category.

### Sub-categories

A category can sit under another one, one level deep. Use **Move under…** on the Categories screen
and pick the parent. In the library, a sub-category's tab follows its parent's tab, with the
parent's name shown above its own. **Move to top level** undoes it.

### Putting entries in categories

- **When adding.** If you have categories and no default, Saikou asks which ones (**Set
  categories**). To skip the question, choose a category in More > Settings > Library >
  **Default category**; **Always ask** brings the question back.
- **Later, for one or many.** Long press an entry in the library, select any others, then tap
  **Move to category** and tick the categories you want. Untick a category to take the entries out
  of it.

### Categories and updates

Categories also decide what library updates and automatic downloads include:

- More > Settings > Library > **Categories** picks which categories an update includes or
  excludes.
- More > Settings > Downloads > **Categories** (under **Download new chapters**) does the same for
  automatic downloads, and **Excluded categories** (under **Delete chapters**) keeps every chapter
  of the entries in those categories.

In each of these, an excluded category wins: an entry in both an included and an excluded category
is left out.

## Selecting many entries

Long press an entry to start a selection, then tap more entries to add them. The bar that appears
has:

- **Select all**, **Invert selection** and **Deselect all**.
- **Mark as read** and **Mark as unread** for every chapter of the selected entries.
- **Download**, with the same choices as an entry's download menu (next chapters, unread,
  bookmarked).
- **Move to category**.
- **Migrate**: move the selected entries to another source. See [Migration](migration.md).
- **Remove from library**, after a confirmation.

Removing an entry keeps its downloaded chapters on the device. They are listed under
More > Settings > Data > **Downloads not in library**, where you can delete them, and they are
used again if you add the entry back.
