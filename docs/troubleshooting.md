# Troubleshooting

Most problems come from a site (slow, down, blocking, or changed), not from the app. Work through
the first section, then look up the message you see.

## First steps

1. **Update your extensions.** Browse > Extensions should show nothing under **Update available**.
   A broken source is often fixed by an extension update; there is no telling when one will come.
2. **Refresh the entry.** Pull down on its page.
3. **Try another entry from the same source**, to tell a problem with one series from a problem
   with the whole source.
4. **Open the site in WebView.** Entry page > overflow > **Open in WebView**, or while browsing a
   source, overflow > **Open in WebView**. If the site does not work there either, it is down or is
   blocking you. Wait for a browser check to pass if one appears.
5. **Change networks.** Switch between Wi-Fi and mobile data.
6. **Clear caches.** More > Settings > Data > **Clear chapter cache**, and More > Settings >
   Advanced > **Clear WebView data**.
7. **Restart Saikou.** Close it from the recent apps view, or force stop it in Android's app
   settings, and open it again.

If only you have the problem, the site may be limiting you: see [Sites that push back](#sites-that-push-back).
If everyone using that source has it, the site or the extension needs fixing, and waiting is the
only option.

## WebView

Saikou uses Android's WebView to open sites inside the app and to pass browser checks. The WebView
screen has **Back in page history**, **Forward in page history**, **Reload** / **Stop loading**,
and in its menu **Clear cookies for this site** and **Open in browser**.

- "**WebView is required for the app to function**": the device has no working WebView. Install or
  enable **Android System WebView** (on Android 8 and 9, Chrome provides it).
- "**Please update the WebView app for better compatibility**": update Android System WebView (or
  Chrome) from your app store.
- Android's Developer options let you see and change which WebView the device uses. Use the standard Android System WebView or Chrome; other WebView providers can make
  sites misbehave or crash the app.

## Browser checks

Some sites show a check page ("checking your browser") before letting anyone in. Saikou passes most
of these on its own: while it works on one, a banner says **Browser check for** the site with a
seconds counter, and how many requests are waiting on it.

When it fails:

- "**This site asked for a browser check that could not be completed**": open the site in WebView
  (entry page or source > overflow > **Open in WebView**) and complete the check there, then go back
  and retry. If you sign in to the site, do it there too.
- "**This request waited too long for another request's browser check on the same site, so it was
  stopped**": another request was solving the check and this one gave up waiting. Retry.
- If the check keeps looping, try a different **Default user agent string** in More > Settings >
  Advanced (any current browser's user agent), restart the app, and open WebView again.
- You can also copy a working `Cookie` header from a browser on another device into the source's
  **Source settings > Cookies > Import**. See [Browse and sources](browse.md#source-settings).
- If nothing works, the site has raised its protection. Wait, or [migrate](migration.md) to
  another source.

## Network errors

- "**No network connection**" / "**The request timed out**": check the connection, switch between
  Wi-Fi and mobile data, or try a VPN. A site can also be down or blocked by your network.
- Try More > Settings > Advanced > **DNS over HTTPS (DoH)**: choose a provider, or a different one if
  it is already on, or turn it off. Then tap **Restart** on the message.
- If you know your router well, its security settings may be blocking the site. If you do not,
  stick to the steps above.
- Certificate errors: check that the device's date and time are right, clear WebView data, and try
  another network.

Some settings, such as DNS over HTTPS, the user agent, **Verbose logging** and **Revoke trusted
unknown extensions**, say "Requires app restart to take effect" and offer **Restart**, which
restarts Saikou and brings you back to Settings > Advanced.

### HTTP errors

- **HTTP error 400 / 401**: the request was refused. Open the page in WebView to check it. For
  tracker errors, sign in again in More > Settings > Tracking.
- **HTTP error 403**: forbidden. Often a browser check (see above), or the site removed the series
  or is blocking you. Check in WebView.
- **HTTP error 404**: not found. The series or chapter is gone from the site. Check in WebView, and
  consider another source.
- **HTTP error 429**: too many requests. Pause downloads, take a break for a few hours, then try
  again.
- **HTTP error 500** and other 5xx errors: the site itself has a problem. Check it in WebView and
  wait.

### Sites that push back

Every site has its own limits and does not publish them. If one source keeps failing for you only:

- Download less from it at once, and lower More > Settings > Downloads > **Pages downloaded at
  once**.
- Keep fewer entries from it in your automatic updates (put rarely read ones in a category you
  exclude). See [Library updates](updates.md#how-saikou-treats-the-sites).

## Updates or backups do not run in the background

1. More > Settings > Advanced > **Allow background work**, and allow it.
2. If you use sync, also tap **Allow background sync** in More > Settings > Sync when it is shown.
3. Some phone makers stop background apps anyway. Look up your phone's brand on
   <https://dontkillmyapp.com> for the extra settings to change.

## Reading problems

- A page does not load: leave the chapter and open it again. See [The reader](reader.md#when-a-page-does-not-load).
- Reading feels slow or stutters: very large pages are usually the cause. Closing other apps helps.
- A badge or count in the library looks wrong: More > Settings > Advanced > **Rebuild library
  counts**.
- Covers are blank or broken: More > Settings > Advanced > **Refresh library covers**.

## Crash logs

If Saikou closes unexpectedly, the next launch shows "Saikou closed unexpectedly. A crash log was
saved on this device." with **Export** and **Dismiss**. All saved logs are in More > **Crash logs**,
where each can be shared or deleted, and **Clear all** removes them. Crash logs never leave the
device unless you share them.

If an extension makes Saikou close at every start, tap **Start without extensions** on the crash
screen. Until Saikou restarts, no extension runs, library updates and downloads wait, and a banner
says so, with **Restart**. The Extensions tab still lists every extension, so you can uninstall or
update the one at fault.

When reporting a problem, include:

- The version: More > Settings > Advanced > **Version** (tap to copy).
- The crash log, if there is one.
- What you did just before, and whether it happens every time.

For problems that do not crash, turn on More > Settings > Advanced > **Verbose logging**, restart,
reproduce the problem, then turn it off again.

## Reinstalling Saikou

If an update will not install over the version you have (Android reports that the signatures do
not match), the only way forward is to uninstall and install again. Uninstalling deletes everything
stored in Saikou's app storage: your library, settings, downloaded chapters, automatic backups and
the Local source's `local` folder (unless a Storage location is set, which keeps those two). Before
uninstalling:

1. Make sure a **Storage location** is set (More > Settings > Data). Your automatic backups and
   Local series are then already outside the app. Otherwise, create a backup by hand and save it
   outside the app (More > **Backup** > **Create backup**, or **Save a copy** of an automatic one).
2. Run More > Settings > Downloads > **Export downloads** to copy your downloads into the storage
   location.
3. After reinstalling, choose the same folder as the **Storage location**, restore a backup from
   More > **Backup** > **Automatic backups** (or **Restore backup**), then bring the downloads
   back with **Copy downloads from a folder**.
