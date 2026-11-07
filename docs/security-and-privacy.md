# Security and privacy

## Security settings

In More > Settings > **Security and privacy**:

- **Require unlock**: ask for your fingerprint, face or screen lock when Saikou opens. Shown when the
  device has a lock set up.
- **Lock when idle**: when to ask again after you leave the app: **Always**, **After 1 minute**,
  **After 2**, **5** or **10 minutes**, or **Never**. Shown while **Require unlock** is on.
- **Hide notification content**: keep entry titles and chapter names out of Saikou's notifications
  (library updates, downloads, backups).
- **Secure screen**: hide the app's contents in the recent apps view and block screenshots.
  **Always**, **Incognito** (only while incognito is on; the default) or **Never**.

Changing the lock settings asks you to unlock first ("Authenticate to confirm change"), so someone
holding your unlocked phone cannot turn the lock off. Turning on **Show mature sources** in
More > Settings > Browse asks the same way.

## Incognito

**Incognito** in the More tab stops reading history from being written until the app next starts
fresh. Each extension also has its own **Incognito** switch on its page, which stays on. See
[History and statistics](history.md#incognito).

## What stays on your device

- Your library, history and settings live only in Saikou's app storage. Android's own cloud backup
  and phone-to-phone transfer are turned off for Saikou, so nothing is copied to Google by Android.
- Backups are files you create and place yourself. See [Backups and restore](backups.md).
- Crash logs are saved on the device (More > **Crash logs**) and only leave it when you export or
  share one. A bug report leaves it only when you share it, with sign-in tokens and cookies taken
  out. It can still name titles and sources from your library. See
  [Reporting a problem](troubleshooting.md#reporting-a-problem).
- Downloads stay in Saikou's app storage and are not visible to other apps.

## What Saikou sends over the network

Saikou has no analytics, no crash reporting and no server of its own. Network traffic comes from
things you set up:

- **Extensions** contact the sites they read from, when you browse, update, read or download.
- **Repositories** are fetched when you refresh them, or in the background with More > Settings >
  Advanced > **Check extension updates**.
- **Tracking** sends the chapters you read to MyAnimeList or AniList, once you sign in to it.
  See [Tracking](tracking.md).
- **Sync** exchanges your library with your Google Drive or your WebDAV server, once you set it up.
  See [Sync between devices](sync.md).

Saikou also asks GitHub for the latest release when you open the About screen, when you tap
**Check for updates**, and at most once a day when the app opens. Turning off More > Settings >
Advanced > **Check for updates automatically** stops only the daily check.

The public privacy policy is at <https://shinsaikou.com/privacy-policy>.

## Where sign-ins are kept

- Sync credentials (the Google sign-in, the WebDAV password) are stored encrypted with the Android
  Keystore. Sync, backups and restores never carry them.
- The MyAnimeList and AniList sign-ins are stored in the app's private settings. They enter a
  backup only when you tick **Private settings**, and sync never carries them.
- Cookies that sites set, or that you import under a source's **Source settings > Cookies**, stay
  in the app. Remove them per source under **Source settings > Cookies > Clear**, or per site from
  the WebView's menu (**Clear cookies for this site**). More > Settings > Advanced > **Clear WebView
  data** resets the in-app browser.

## Network privacy options

More > Settings > Advanced:

- **DNS over HTTPS (DoH)**: resolve site addresses through an encrypted DNS provider instead of
  your network's DNS. **Disabled** by default; choose a provider from the list. Takes effect after
  the app restarts; the message offers **Restart**.
- **Default user agent string**: the browser identity Saikou sends to sites. **Reset default user
  agent string** puts it back. Takes effect after the app restarts; the message offers **Restart**.
