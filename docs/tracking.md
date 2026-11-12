# Tracking

Tracking keeps your list on a tracking site up to date as you read. Saikou supports
**MyAnimeList**, **AniList**, **MangaBaka** and **Comick** (the tracking site at comick.dev). You can
sign in to any of them, and link each entry to each.

The Tracking section appears in More > Settings when this build of Saikou offers a tracker.

## Signing in

1. Open More > Settings > **Tracking**.
2. Under **Trackers**, tap **Sign in** next to the tracker.
3. Your browser opens that site's sign-in page. While you sign in there, Saikou shows "Waiting
   for the browser. Finish signing in there, then switch back to Saikou", and a notification lets
   you jump back.
4. Sign in on the site and approve **Saikou**. The browser then shows "Signed in. Switch back to
   Saikou to finish." Tap **Return to Saikou** on that page, or the **Signed in, tap to return**
   notification. The row now says **Signed in as** your name.

MangaBaka's sign-in page may first show a Cloudflare browser check. Finish it in the browser, then
sign in.

Comick's page that asks you to approve Saikou leaves the permission to change your library off.
Turn it on, and keep the permission to stay signed in on, before you approve. If either is off,
the sign-in stops and the Comick row says which one to turn on, for example "The sign-in left out
permission to change your library (library:write). Sign in again and turn it on".

If sign-in is not finished in the browser within five minutes, start again. If Saikou says
"Another app is using port N on this device", close that app (the sign-in needs the port for a
moment to hear back from the browser) and sign in again. **Sign out** stops Saikou
from sending progress to that tracker; your list on the site stays as it is. Signing out of
MangaBaka also ends Saikou's access on MangaBaka, when the device can reach it.

## Linking an entry

1. Open the entry's page and tap the **Tracking** button in the header.
2. Tap **Add tracking** for the tracker.
3. Search, then tap the right result.

If the search finds nothing, try another title (romanized, English, or shorter). You can also look
the series up on the site:

- On MyAnimeList, AniList and MangaBaka, paste the series' address (on MangaBaka, its address on
  mangabaka.org), or search for `id:` followed by the number in its address.
- On Comick, search for `id:` followed by the title's Comick ID.

On MyAnimeList you can also search your own list with `my:` followed by part of the title.

Once linked, the tracking sheet shows the entry's **Status**, **Chapters**, **Score**, **Start
date** and **Finish date** on the tracker. Tap any of them to change it. Comick keeps no dates, so
its sheet has no date rows.

- On AniList the score uses the scoring system your AniList list is set to (for example 100
  points, 10 points or 5 stars).
- On MangaBaka the score runs from 0 to 100 in the rating steps your MangaBaka account is set to
  (steps of 1, 5, 10, 20 or 25). Saikou reads the steps when you sign in, so sign in again after
  you change them on MangaBaka. The statuses include MangaBaka's **Considering**, **Paused** and
  **Rereading**.
- On Comick the score runs from 0 to 10, and the statuses are **Reading**, **Completed**, **On
  hold**, **Dropped** and **Plan to read**.

The sheet's menu has **Open in browser** and **Copy link** for the entry's address on the tracker,
and, for AniList and MangaBaka, **Track privately** or **Track publicly**, which sets whether the
entry is private on your list there.

To unlink, remove the tracking from the sheet. The dialog, for example **Remove AniList tracking?**,
removes the link in Saikou; tick **Also remove from AniList** (with your tracker's name) to delete
the entry from your list there as well.

## What Saikou sends

Tracking goes one way, from Saikou to your trackers, except when you run a comparison (below).

- **Update progress after reading** (More > Settings > Tracking): when you finish a chapter in the
  reader, its number is sent to the entry's trackers.
- **Update progress when marked as read**: **Always**, **Ask** or **Never** for chapters you mark as
  read by hand. With **Ask**, Saikou offers **Update trackers to chapter N?** after you mark them.
- Only progress forward is sent. Reading an earlier chapter again changes nothing on the tracker.
- The first chapter sent sets the status to **Reading**. Reaching the last chapter the tracker
  knows sets it to **Completed**, with today as the finish date. Saikou does not know Comick's
  chapter count, so on Comick you set **Completed** yourself.
- Without a connection, the update waits and is sent once you are online ("Updating trackers to
  chapter N").

In the library, the **Tracked** filter and the **Tracker score** sort use your trackers. See
[Library and categories](library.md).

## Compare with MyAnimeList

Reading on several apps or devices can leave MyAnimeList and Saikou disagreeing. More > Settings >
Tracking > **Compare with MyAnimeList** finds those entries and lets you choose, entry by entry,
which side to keep. Nothing changes until you confirm. Comparing is available for MyAnimeList only,
not for AniList, MangaBaka or Comick.

If sync is set up, Saikou first syncs with your other devices ("Syncing with your other device"),
so their reading counts. Then it reads your MyAnimeList list and checks each tracked library entry.
The result is grouped:

- **MyAnimeList is ahead**: you read further there. Choose **Mark as read in the app** (the
  chapters in between are marked read here and on your other devices after they sync; downloads
  are kept), or **Set MyAnimeList back to chapter N**, or **Don't change**.
- **The app is ahead**: choose **Update MyAnimeList to chapter N** or **Don't change**. When an
  update is already waiting to be sent, **Keep MyAnimeList at chapter N** cancels it instead.
- **Not on your MyAnimeList list**: the entry was removed there. **Add it back** (with its old
  status, score and dates), **Remove tracking** (in the app only, on both your devices), or leave it.
- **Can't compare**: for example the entry has no chapters yet, or its chapters have no numbers
  Saikou can read. You can still set MyAnimeList by hand from the entry's tracking button.

Some rows carry a warning, for example when MyAnimeList counts chapters differently ("Numbers may
not match"), shows a reread, or when Saikou has no reading history for a chapter marked read.
**Keep the higher number** answers every row without a warning at once; rows with a warning are
left for you. **Don't change any** sets every row back to leaving both sides as they are.

Saikou cannot move your reading position in the app backwards for you. When the app is ahead
because you marked chapters read by mistake, mark them unread on the entry's page.
<!-- FIXABLE: F14 -->

After you confirm (**Apply N changes?**), Saikou applies them one by one and reports **Done**,
**Changed since you compared** and **Failed** counts. **Compare again** runs a fresh comparison.

## Sign-in and privacy

- Each tracker sign-in is stored on this device only. Sync never carries it.
- A backup includes the sign-ins only when you tick **Private settings** while creating the
  backup. Without it, a restored device shows the trackers as signed out, and you sign in again.
- If a tracker stops accepting the sign-in ("The tracker no longer accepts this device's
  sign-in"), tap **Sign in again** in the Tracking settings.
- An AniList sign-in lasts a year and can't be renewed, so a year after you sign in, Saikou asks
  you to sign in to AniList again. Updates waiting to be sent go out once you do.
