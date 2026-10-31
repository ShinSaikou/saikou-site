# Library updates and the Updates tab

A library update asks each source for the latest chapter list of your library entries. New
chapters appear in the **Updates** tab and, if you want, download on their own.

## Updating by hand

Any of these starts an update of the whole library:

- Pull down on the **Library** tab.
- Library > overflow menu > **Update library**.
- Pull down on the **Updates** tab.

**Update category** in the Library's overflow menu updates only the category tab you are on. While
an update runs, the same menu offers **Stop update**. Starting a second update while one runs only
shows **A library update is already running**.

A manual update checks every entry in the categories you include for updates (see below). The
**Smart update** rules do not apply to it, so a manual update is the way to check entries that
smart update is holding back. The only entries a manual update leaves out are those whose source
says their chapter list never changes.

To refresh one entry, pull down on its page.

## Automatic updates

Set these in More > Settings > Library.

- **Automatic library update**: **Off**, **12 h**, **24 h** or **48 h**. Off by default.
- **Automatic updates device restrictions**: **Only on Wi-Fi** (on by default), **Only on
  unmetered network** and **When charging**. Available once automatic updates are on.
- **Categories**: which categories an update includes and excludes. An entry in an excluded
  category is never updated, even if it is also in an included one. With nothing included, every
  category is.
- **Refresh entry details**: also fetch the cover, description and status on automatic updates.
  Off by default; a manual update only fetches chapters.
- **Smart update**: rules that skip entries on automatic updates, to save time, data and requests
  to the sites. All four are on by default:
  - **Skip entries with unread chapter(s)**
  - **Skip unstarted entries**
  - **Skip entries with "Completed" status**
  - **Predict next release time**: skip an entry until the time Saikou expects its next chapter,
    worked out from the gaps between its past chapters.

An entry whose details were never fetched (for example one that just arrived through a migration
or a sync) is always updated, whatever the rules say, so it gets its details.

For automatic updates to run reliably, let Saikou run in the background: More > Settings > Advanced >
**Allow background work**. Some phone makers stop background apps even then; see
[Troubleshooting](troubleshooting.md#updates-or-backups-do-not-run-in-the-background).

### Other update settings

Also in More > Settings > Library:

- **Mark duplicate read chapter as read**: when a chapter has the same number as one you have
  read, mark it read too, **After reading a chapter** and/or **After fetching new chapter**.

In More > Settings > Advanced:

- **Update library manga titles to match source**: let an update replace the titles of library
  entries with the title the source uses now. Your own titles from **Edit details** are kept either
  way.
- **Refresh library covers**: runs a full library update that also refreshes every entry's cover
  and details.

## How Saikou treats the sites

Saikou updates several sources at the same time and adjusts how fast it asks each site. When a site
starts refusing requests or slowing down, Saikou halves its pace for that site, and waits as long
as the site asks when it says so. If a site pushes back three times during one update, Saikou stops
asking it until the next update. Other sources carry on.

The entries it did not check are listed in the update errors as **Not checked**, naming the site,
under a line that says how many were not checked and why, with an **Open library settings**
button. It opens More > Settings > Library, where the **Categories** row after **Automatic library
update** chooses which categories update, so fewer entries from one site are asked at once.

## Notifications

- **Updating library** shows progress while an update runs.
- **New chapters found** lists the entries with new chapters, with **Mark as read** and **View
  chapters** actions.
- **N update(s) failed** appears when some entries could not be updated. Tap it (**Show errors**)
  to open the Updates tab with the error list.

Each kind has its own notification channel (**Library progress**, **New chapters**, **Library
update errors**), so you can silence one in Android's settings without the others.

## The Updates tab

The **Updates** tab lists new chapters from your library, newest first, under day headers
(**Today**, **Yesterday**, **N days ago**). Several new chapters of one entry on one day are folded
into one row showing **N chapters**; tap it to show or hide them.

Chapters that were already out when you added an entry are not new. When an entry joins your
library before its chapters are loaded (added from a source's list, or restored from a backup
without chapters), its first update loads the whole list but counts only the chapters released
after you added it. The rest go straight to the entry's page, unread, with no notification and no
automatic download. A chapter the site gives no date counts as already out.

- Tap a chapter to read it, or use its download control to queue it.
- **Filter** chooses what the list shows: **Downloaded**, **Unread**, **Started**, **Bookmarked**,
  **Filter excluded scanlators** (hide chapters from groups you excluded on an entry's page), and
  **Categories**. Chapters of entries in an excluded category are never shown, even if the entry
  is also in an included category.
- Long press to select. As on an entry's page, a second long press further away selects every
  chapter in between. The bar offers **Mark as read**, **Mark as unread**, **Bookmark chapter**,
  **Unbookmark chapter**, **Select all**, **Invert selection** and **Deselect all**.

### Update errors

When the last update had failures, the Updates tab's top bar shows an error button with the count.
It opens **Update errors**: the failed entries grouped by source, each with the reason. Tap an
entry to open its page, where pulling down tries it again.

When the update stopped asking a site, a line above the list says how many entries were not
checked, with **Open library settings**. The Library tab's error button opens the same list.

Common reasons:

- **Not checked: ... refused or timed out three times during this update**: the site pushed back,
  see above. The next update tries again.
- **HTTP error 403**, **HTTP error 429**, **This site asked for a browser check that could not be
  completed**: see [Troubleshooting](troubleshooting.md).
- **That source is not installed**: install the entry's extension again, or
  [migrate](migration.md) the entry.
