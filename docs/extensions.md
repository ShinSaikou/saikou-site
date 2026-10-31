# Extensions and repositories

An **extension** adds one or more sources to Saikou. A **repository** is a list of extensions that
someone publishes at a web address. Saikou ships with no repository and no extension: you choose
which repositories to add.

Saikou reads extensions and repositories built for the Tachiyomi extension API (lib 1.4 and 1.6).

## Safety

Extensions are made by third parties, not by Saikou. An extension's code runs inside Saikou, with
the same access to the app and its data that Saikou has, so an extension from an untrustworthy
place could misbehave. Only add repositories you trust.

Saikou checks every extension's signature before it runs:

- An extension signed with the key of one of your repositories is trusted without a question.
- An extension signed with any other key is held under **Needs trust**. Tapping it asks **Trust
  this extension?** and shows the signer. Trust it only if you recognise the signer.
- An unsigned file, or an update signed with a different key than the copy you have, is refused.

More > Settings > Advanced > **Revoke trusted unknown extensions** withdraws every trust you gave
by hand. It takes effect the next time the app starts; the message offers **Restart**.

## Adding a repository

1. Open More > **Extension repositories**. (Browse > Extensions also offers the screen when no
   repository is configured, and the **Repositories (N)** button opens it later.)
2. Under **Add a repository**, paste the address its maintainers publish into **Repository
   address**.
3. Tap **Add**. Saikou reads the list and confirms with **Repository added.**

Some repository pages offer a link that opens Saikou directly. Such a link only fills in the
address: Saikou still waits for you to read it and tap **Add**.

The refresh button reloads every repository's list. To remove one, tap **Remove** next to it and
confirm.

## Installing and updating

**Browse > Extensions** lists, in this order: **Update available**, **Needs trust**, **Did not
load**, **Installed** and **Available**.

- **Install** downloads and installs an extension. The row shows **Pending**, **Downloading** and
  **Installing**; **Cancel install** stops it.
- **Update** installs a newer version; **Update all** updates every extension that has one.
- **Search extensions** filters the list, and the **Filter** icon chooses which languages appear.
- Each row shows the version (**v1.4.2**), the extension library version (**lib 1.4**), the
  languages, and **18+** for extensions marked as mature.

Saikou installs extensions inside the app. They do not appear in Android's app list and do not need
the "Install unknown apps" permission.

More > Settings > Advanced > **Check extension updates** refreshes your repositories in the
background so the **Update available** section stays current.

## An extension's page

Tap an installed extension to open its page:

- **Package**, **Version**, **Library** and **Signer**.
- **Sources**: each source it provides, with a switch. **Enable all** and **Disable all** switch
  them together.
- **Incognito**: do not record reading history for this extension's sources.
- **Update** (when one is available) and **Uninstall**.
- **Settings** and **Open in WebView** for each source, when the source has them.

## Uninstalling

Tap **Uninstall** on the extension's page or in its row menu (**More actions**), then confirm
("Remove ... and the sources it provides?"). Entries from its sources stay in your library, marked
**Source not installed**, with their read chapters and downloads. Install the extension again, or
[migrate](migration.md) those entries to another source.

## When an extension does not load

Extensions that cannot run are listed under **Did not load**, with the reason:

- **Built for an unsupported library version**: the extension targets an extension library
  version Saikou does not support. More > Settings > Advanced > **Extension library versions
  override** accepts other versions (comma separated, for example `1.4,1.6,1.7`). Extensions
  already on disk are read again the next time the app starts; saving a changed value offers
  **Restart**. Only use this if you know the
  extension works with Saikou.
- **Not signed**, **Not an extension**, **The entry point is missing**, **The code could not be
  loaded**, **The entry point failed to start**: the file is broken or not meant for this app.
  Update or reinstall it; if that does not help, the extension itself needs fixing.
- **Loaded before the app finished starting**: restart the app.
