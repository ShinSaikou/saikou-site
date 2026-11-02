# The reader

Tap a chapter to open it in the reader. Tap the middle of the screen (or wherever your tap zones
put the menu) to show the reader's menu.

## The reader's menu

- **Top bar**: back, the entry and chapter, **Bookmark chapter** / **Unbookmark chapter**, and an
  overflow with **Open in WebView**, **Open in browser** and **Share**. When the page on screen has
  a note, the bar says **This page has a note**.
- **Bottom bar**: **Previous chapter** and **Next chapter**, the page slider, and buttons for
  **Reading mode**, **Rotation**, **Crop borders** and **Settings**.

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

## The reader's settings sheet

The **Settings** button in the reader opens a sheet with three tabs. Changes apply at once.

### Reading mode

- **For this series**: **Reading mode** and **Rotation** for the entry you are reading.
- For paged modes: **Scale type** (**Fit screen**, **Stretch**, **Fit width**, **Fit height**,
  **Original size**, **Smart fit**), **Zoom start position** (**Automatic**, **Left**, **Right**,
  **Center**), **Crop borders**, **Automatically zoom into wide images**, **Pan wide images**,
  **Split wide pages** with **Invert split page placement**, and **Rotate wide pages to fit** with
  **Flip orientation of rotated wide pages**.
- For long strip modes: **Side padding**, **Crop borders**, **Split wide pages**, **Rotate wide
  pages to fit**, **Double tap to zoom** and **Disable zoom out**.
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
