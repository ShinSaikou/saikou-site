# The reader

Tap a chapter to open it in the reader. Tap the middle of the screen (or wherever your tap zones
put the menu) to show the reader's menu.

## The reader's menu

- **Top bar**: back, the entry and chapter, **Bookmark chapter** / **Unbookmark chapter**, and an
  overflow with **Open in WebView**, **Open in browser** and **Share**. When the page on screen has
  a note, the bar says **This page has a note**.
- **Bottom bar**: **Previous chapter** and **Next chapter**, the page slider, and buttons for
  **Reading mode**, **Rotation**, **Crop borders** and **Settings**. In the long strip modes, with
  [auto-scroll](#auto-scroll) turned on, a play button comes before **Settings**. While
  [two pages show side by side](#two-pages-side-by-side), a **Shift pages** button comes after
  **Crop borders**.

## Reading modes

- **Paged (right to left)**: the usual way to read manga. This is the default.
- **Paged (left to right)**: the usual way to read comics.
- **Paged (vertical)**: swipe up for the next page.
- **Long strip**: one continuous scroll, the usual way to read webtoons.
- **Long strip with gaps**: the same, with a small space between pages.

The default for every entry is More > Settings > Reader > **Default reading mode**. To use a
different mode for one entry, choose it from the reader's **Reading mode** button, from the
reader's **Settings** under **For this series**, or from the entry page's overflow menu >
**Reading mode**. Rotation works the same way: More > Settings > Reader > **Default rotation**
(**Free**, **Portrait**, **Landscape**, **Locked portrait**, **Locked landscape**, **Reverse
portrait**), or per entry.

To put every entry back on the defaults, use More > Settings > Advanced > **Reset per-series reader
settings**. With sync on, this resets them on every synced device.

## Auto-scroll

In the long strip modes the reader can scroll the pages down by itself, for reading without
swiping. Auto-scroll is experimental. Turn it on in More > Settings > Experimental > **Auto-scroll
in long strip**.

1. Open a chapter in **Long strip** or **Long strip with gaps**. To switch an entry to one of them,
   use the reader's **Reading mode** button (see [Reading modes](#reading-modes)).
2. Show the reader's menu and tap the play button (**Start auto-scroll**), just before **Settings**
   in the bottom bar. The menu closes and the pages start moving.

It carries on into the next chapter, the way the strip does when you scroll by hand, and the pages
ahead load as they would. The screen stays on while it runs, whatever **Keep screen on** is set to.
The paged modes have no play button.

Auto-scroll stops when:

- you touch the screen. The touch still does what it always does, so a tap where the menu opens
  also opens the menu;
- the menu, the settings sheet or a dialog opens;
- you leave the reader or switch to another app;
- you jump to another page;
- you switch to a paged mode;
- it reaches the end of the last chapter.

Tap the play button again to carry on.

**Scroll speed** sets how fast it goes, from 1 (slowest) to 10 (fastest), 4 by default. It is at the
end of the long strip options on the **Reading mode** tab of the reader's settings sheet, and at
the end of **Long strip** in More > Settings > Reader. Both show it only while the switch is on. A
level moves the pages at the same speed on every screen.

## Two pages side by side

In the paged modes **Paged (left to right)** and **Paged (right to left)**, the reader can show two
pages at once, as a printed book does. This is experimental. Turn it on in More > Settings >
Experimental > **Two pages side by side**.

Then choose when in **Two pages side by side**, on the **Reading mode** tab of the reader's settings
sheet or under **Paged** in More > Settings > Reader:

- **Never**: one page at a time, as before.
- **In landscape** (the default): two pages while the screen is in landscape, one in portrait.
- **Always**: two pages either way.

How pages pair up:

- In right to left the earlier page is on the right; in left to right it is on the left.
- The first page of a chapter stands alone, unless you shift the pages (below).
- A wide page, an animated page, a tall page cut into parts and a page that cannot be read always
  stand alone, and the pairing starts again after them. A wide page shows whole, not split or
  rotated, whatever **Split wide pages** and **Rotate wide pages to fit** are set to.
- Until a page has loaded, Saikou guesses its size, so a pair can change when a page turns out to be
  wide. The page on screen stays in view when that happens.

Taps, swipes and keys turn a whole spread. Zoom acts on the spread as one picture. The page number
shows both pages, for example 5-6 / 20.

When the pages pair the wrong way round, so the two halves of a drawing land on different spreads,
show the reader's menu and tap **Shift pages**. It moves the pairing by one page, for that entry, on
this device only; tap it again to move it back. It moves only the chapter's first run of pages, up
to the first page that always stands alone. Pages after that one keep their pairing. In a chapter
that opens on such a page, the run after it moves instead.

The switch and **Shift pages** stay on this device and are not in backups. The choice of
**Never**, **In landscape** or **Always** is an app setting, which a backup with **App settings**
keeps.

## The reader's settings sheet

The **Settings** button in the reader opens a sheet with three tabs. Changes apply at once.

### Reading mode

- **For this series**: **Reading mode** and **Rotation** for the entry you are reading.
- For paged modes: **Scale type** (**Fit screen**, **Stretch**, **Fit width**, **Fit height**,
  **Original size**, **Smart fit**), **Zoom start position** (**Automatic**, **Left**, **Right**,
  **Center**), **Crop borders**, **Automatically zoom into wide images**, **Pan wide images**,
  **Split wide pages** with **Invert split page placement**, **Rotate wide pages to fit** with
  **Flip orientation of rotated wide pages**, and **Two pages side by side** while
  [that switch](#two-pages-side-by-side) is on.
- For long strip modes: **Side padding**, **Crop borders**, **Split wide pages**, **Rotate wide
  pages to fit**, **Double tap to zoom**, **Disable zoom out**, and **Scroll speed** while
  [auto-scroll](#auto-scroll) is turned on.
- **Tap zones**: **Default**, **L shaped**, **Kindle-ish**, **Edge**, **Right and Left** or
  **Disabled**, and **Invert tap zones** (**None**, **Horizontal**, **Vertical**, **Both**).

### General

- **Background color**: **Black**, **Gray**, **White** or **Auto** (picked from the page).
- **Show page number**.
- **Use vertical chapter navigator in**, **Place vertical navigator on the left side** and
  **Vertical navigator height**.
- **Fullscreen**, **Show content in cutout area** and **Keep screen on**.
- **Show actions on long tap** (see Page actions below).
- **Always show chapter transition**: show the page between chapters even when the next chapter
  is already loaded.
- **Animate page transitions**.
- **Flash on page change**, for e-ink screens, with **Flash duration**, **Flash every** (pages) and
  **Flash with** (**Black**, **White**, **White and Black**).

### Custom filter

- **Custom brightness**: a brightness of its own for the reader, below the system minimum if you
  want.
- **Custom color filter**: **Red**, **Green**, **Blue** and **Alpha**, with a **Color filter blend
  mode** (**Default**, **Multiply**, **Screen**, and on Android 9 and later also **Overlay**,
  **Dodge / Lighten** and **Burn / Darken**).
- **Grayscale** and **Inverted**.

## Reader settings in Settings

More > Settings > Reader holds every reader option, the sheet's included, in groups (**Display**,
**E-Ink**, **Reading**, **Paged**, **Long strip**, **Navigation** and **Actions**), so you can set
the tap zones, scale type, crop borders and the rest without opening a chapter. See
[Settings](settings.md#reader). The rows the sheet does not have:

- **Default reading mode** and **Default rotation**.
- **Double tap animation speed**: **No animation**, **Normal** or **Fast**.
- **Show reading mode**: briefly show the current mode when the reader opens.
- **Show tap zones overlay**: briefly show the tap zones when the reader opens.
- **Skip chapters marked read**, **Skip filtered chapters** (on by default) and **Skip duplicate
  chapters**: which chapters the reader passes over when moving to the next one. When it skips,
  the transition page says how many chapters it skipped.
- **Sensitivity for hiding menu on scroll** (long strip): **Highest**, **High**, **Low** or
  **Lowest**.
- **Volume keys** and **Invert volume keys**: turn pages with the volume buttons.
- **Save pages into separate folders**: put saved pages in a folder per entry.

**Skip duplicate chapters** picks one copy when a chapter exists from several groups. If you
ranked the groups on the entry's page (**Filter scanlator groups**), the reader moves to your
preferred group's copy. See [An entry's page](entry.md#chapter-settings).

## Page actions

With **Show actions on long tap** on, long press a page for:

- **Set as cover**: use this page as the entry's cover, after **Use this image as cover art?**.
- **Share**: send the page to another app.
- **Save**: save the page as a picture.
- **Note**: write a note on this page (see below).

Saved pages go to your gallery's **Pictures/Saikou** folder, in a sub-folder named after the entry
when **Save pages into separate folders** is on. Your gallery and files apps show them and they
stay when the app is uninstalled. On Android 8 and 9 they go to Saikou's own pictures folder
instead (`Android/data/com.shinsaikou/files/Pictures`), which the gallery does not show; use **Share**
there.

## Bookmarks and page notes

**Bookmark chapter** in the top bar marks the whole chapter. Bookmarked chapters can be filtered on
the entry's page and in the Updates tab, and downloaded in one go with the **Bookmarked** download
choice.

A **page note** is a short note attached to one page of a chapter: long press the page, tap
**Note**, type, and save. Leave it empty to remove the note. While a page with a note is on screen,
the reader's top bar shows **This page has a note**. Sync carries bookmarks and page notes to your
other devices.

## When a page does not load

- A page that fails shows the reason and a retry button. Leaving the chapter and opening it again
  also retries it.
- "Unsupported image format" means the page is in a format Saikou cannot decode.
- A page that loads but stays blank can come from the device's limit on image size. Lower More >
  Settings > Advanced > **Custom hardware bitmap threshold** step by step until the page shows.

See also [Troubleshooting](troubleshooting.md).
