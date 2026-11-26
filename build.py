#!/usr/bin/env python3
"""Build the public JL3D privacy / support / terms site (GitHub Pages, jel777/jl3d-legal).

Every statement here must match what the shipping build actually does. When an app's data
flows change, update APPS below in the same change as the app, then rebuild:  python3 build.py
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
EFFECTIVE = "16 October 2026"
COMPANY = "JL3D Services, LLC"
PLACE = "Houston, Texas, USA"
EMAIL = "JL3D@proton.me"
APPLE_EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
MANAGE_SUBS = "https://support.apple.com/en-us/118428"
REFUNDS = "https://support.apple.com/en-us/118223"

# Each app: what it stores on the device, what leaves the device (and to whom, when), permissions,
# purchases, and support FAQ. Keep sentences plain and specific.
APPS = [
    {
        "slug": "fdjsongfinder",
        "name": "FDJ Song Finder",
        "short": "FDJ Song Finder",
        "tagline": "Search your church's Planning Center song library by lyric, title, author, key, or tempo—even offline.",
        "summary": (
            "Your church's song library is downloaded directly from Planning Center using your church access key "
            "and stays on your device. JL3D runs no servers for this app and does not collect, receive, or sell "
            "any personal data. There are no ads, no analytics, and no tracking."
        ),
        "stored": [
            (
                "A local copy of your church's Planning Center Services songs, arrangements, chord charts, lyrics, "
                "keys, tempos, and scheduling metadata in a private SQLite database on your device so search and "
                "chart reading work offline."
            ),
            (
                "Your saved lists (Favorites and Shortlist), recent searches (up to the 10 most recent per library "
                "on Android), and display preferences such as Light/Dark appearance and chart text size."
            ),
            (
                "Your read-only Planning Center church access key (Application ID and Secret): stored in the iOS "
                "Keychain on iPhone and iPad, and encrypted on Android with an AES-256-GCM key held in the Android "
                "Keystore inside app-private no-backup storage."
            ),
            (
                "On Android, your Planning Center organization name and ID plus a randomly salted SHA-256 hash of "
                "the access key's Planning Center person ID, stored locally in the app's private database to prevent "
                "mixing libraries from different organizations or accounts."
            ),
            (
                "On Android, the downloaded song library, saved lists, recent searches, preferences, and encrypted "
                "access key are excluded from Android cloud backup (Google Drive Auto Backup), ADB backup, and "
                "device-to-device transfer. On iOS, app storage may be included in your own iCloud or computer "
                "backup under Apple's privacy policy."
            ),
        ],
        "leaves": [
            (
                "Planning Center (Ministry Centered Technologies)",
                "The app talks directly and only to Planning Center's HTTPS API (api.planningcenteronline.com) "
                "using the read-only church access key you enter, to verify the key and download or refresh your "
                "church's Services songs, arrangements, chord charts, and keys. The app sends GET requests only "
                "and never edits, creates, or deletes anything in Planning Center. On Android, the app rejects "
                "non-HTTPS traffic, redirects, and user-installed certificates. Planning Center's own privacy "
                "policy applies to your church's account there. JL3D runs no servers for this app and receives "
                "none of this data.",
            ),
            (
                "Optional links you tap",
                "If you tap a Planning Center menu link (such as Open in Planning Center, Open Planning Center "
                "Songs, or Open Web Music Stand), your device's browser opens that Planning Center web page "
                "(services.planningcenteronline.com or musicstand.planningcenteronline.com). The browser handles "
                "that visit under its own and Planning Center's privacy policies.",
            ),
            (
                "Sharing and copying song titles",
                "On Android, tapping Share on a song sends only the plain song title to the app you choose in the "
                "Android share sheet; sharing a Saved list sends only the song titles, one per line. Copying a "
                "song title on iOS or Android puts only the plain song title on your clipboard. Lyrics, chord "
                "charts, Planning Center IDs, links, and access keys are never shared or copied by those actions.",
            ),
        ],
        "provider_policies": [
            ("Planning Center", "https://www.planningcenter.com/privacy"),
        ],
        "permissions": [
            (
                "Network access",
                "Used only to connect over HTTPS to Planning Center (api.planningcenteronline.com) to check your "
                "access key and download or refresh your church's song library. No other network permissions or "
                "tracking SDKs are included.",
            ),
            (
                "Background refresh (iOS)",
                "Used to keep your downloaded library up to date while the app is closed, including an occasional "
                "overnight verification check while your iPhone or iPad is charging. You can turn it off in iOS "
                "Settings > General > Background App Refresh.",
            ),
            (
                "Background refresh (Android)",
                "While signed in, the app schedules WorkManager periodic checks (a refresh every 6 hours when "
                "connected, plus an overnight verification sweep around 1:00 AM when on unmetered Wi-Fi and "
                "charging). The app does not use foreground services. You can stop background refreshes by "
                "restricting background battery or background data for FDJ Song Finder in Android Settings > Apps "
                "> FDJ Song Finder, or by signing out in the app.",
            ),
        ],
        "purchases": None,
        "faq": [
            (
                "How do I get a church access key?",
                "Ask your church's Planning Center Services administrator. Your administrator creates a dedicated "
                "viewer-only Planning Center person, generates a Personal Access Token (an Application ID and a "
                "Secret) for that person, and shares it privately with band members. The key is read-only and can "
                "be revoked by your administrator at any time.",
            ),
            (
                "What happens if our church access key is revoked?",
                "Automatic and manual updates pause and the app tells you Planning Center access was removed. "
                "Your already-downloaded songs stay readable offline on your device so you are never stuck during "
                "a service. Ask your church administrator for a new key, or sign out in Settings.",
            ),
            (
                "How do I remove the songs and access key from this device?",
                "Open Settings, tap Sign Out, and choose Sign Out and Remove Downloaded Songs (or Sign Out and "
                "Remove Songs on iOS). That deletes the downloaded library, saved lists, recent searches, and "
                "saved access key from your device without changing anything in Planning Center. If you only want "
                "to stop updates while keeping the downloaded songs offline, choose Sign Out and Keep Songs on "
                "This Device. Uninstalling the app also deletes all app data.",
            ),
            (
                "Search shows old lyrics or an older chart.",
                "Open the app while online and let it refresh, or go to Settings > Verify all charts now before "
                "rehearsal or a service.",
            ),
            (
                "Is FDJ Song Finder affiliated with Planning Center?",
                "No. FDJ Song Finder is an independent app made by JL3D Services, LLC. It is not affiliated with, "
                "endorsed by, or supported by Planning Center or Ministry Centered Technologies.",
            ),
            (
                "The app says the song library cannot be opened.",
                "Nothing has been deleted automatically. Close and reopen the app. If the message stays, you can "
                "tap Delete it and start over (Android) to clear the damaged file and re-sync, or email "
                "JL3D@proton.me before deleting the app.",
            ),
        ],
        "backup_note": "On Android, this data is excluded from cloud backup and device-to-device transfer. On iPhone and iPad, iOS may include it in your own iCloud or computer backup; that is governed by Apple's privacy policy. Deleting the app deletes this data.",
        "support_note": "Include your device model, iOS or Android version and, if you can, the app version (shown in the app's Settings, under About).",
        "leaves_note": "Planning Center's privacy policy: planningcenter.com/privacy.",
    },
    {
        "slug": "tinyviolin", "name": "World's Tiniest Violin", "short": "Tiny Violin",
        "effective": "26 November 2026",
        "tagline": "A pocket-sized violin for life's smallest tragedies. Play it for someone who needs it.",
        "summary": "People, play history and preferences are stored only on your iPhone or iPad. Apple handles the optional Pro purchase. JL3D runs no servers for this app and does not collect, receive or sell any personal data. There are no accounts, ads, analytics or tracking.",
        "label": "On the App Store privacy label, the app declares Data Not Collected.",
        "stored": [
            "The names or nicknames you add for people you play the violin for, plus their saved size and sound preferences.",
            "Your play history (up to the most recent 100 plays) and simple statistics derived from it.",
            "App preferences such as haptics, shuffle and your selected sound and size.",
        ],
        "leaves": [
            ("Apple App Store (purchases)", "Apple processes the optional Pro purchase through StoreKit 2. JL3D receives no payment card, name or contact details from Apple for the purchase. The app verifies Apple-signed transactions on your device to check Pro access."),
        ],
        "permissions": [],
        "purchases": "The app is free to download and play. Pro is an optional one-time purchase priced at US$0.99 in the U.S. App Store. Your local price is shown in the app. Pro unlocks two Drama phrases, Grand Lament and Sob Story. Existing eligible purchases from earlier versions continue to unlock Pro.",
        "faq": [
            ("I can't hear anything.", "Turn the volume up with the side buttons. The violin plays through the media channel and is meant to be heard, so it also plays when the silent switch is on. Check that no Bluetooth device has taken the audio."),
            ("How do I restore Pro on a new iPhone or iPad?", "Tap Restore Purchases on the Pro screen or in Settings while signed in with the same Apple Account."),
            ("I reinstalled and my people and history are gone.", "Deleting the app removes the people and play history stored on the device. Use Restore Purchases to recover an eligible Pro purchase."),
            ("The app says your library couldn't open.", "Your people and history have not been deleted. Close and reopen the app. If the message stays, email us before deleting the app, because deleting it removes the data stored on the device."),
            ("How do I get a refund?", f'Refunds for App Store purchases are handled by Apple. <a href="{REFUNDS}">Request a refund from Apple</a>.'),
        ],
    },
    {
        "slug": "printpilot", "name": "Print Pilot", "short": "Print Pilot",
        "tagline": "Lay out photos and documents and print them to any AirPrint printer, or export a clean PDF.",
        "summary": "The documents and photos you work with stay on your device. JL3D does not collect, receive or sell any personal data. There are no ads, no analytics and no tracking.",
        "stored": [
            "Documents, PDFs and photos you import, the layouts you build from them, and their thumbnails.",
            "Print settings, presets and your local print history.",
            "App preferences. If you updated from an older version, a copy of any data that could not be migrated is kept in the app's Documents folder under \"Previous Version Export\".",
        ],
        "leaves": [
            ("Your printer", "When you print, the page you chose is sent directly from your device to the AirPrint printer you select on your local network. It does not pass through JL3D."),
            ("Apple App Store (subscriptions)", "Print Pilot Pro is an auto-renewable subscription sold through Apple's In-App Purchase. Apple processes the payment; JL3D receives no payment card, name or contact details."),
        ],
        "permissions": [
            ("Photos", "Only the photos you pick are imported. The app does not browse your library."),
            ("Camera (Pro document scanner)", "Used only while you scan a document. Scanning happens on the device."),
            ("Local network", "Used to find and print to AirPrint printers on your Wi-Fi network."),
        ],
        "purchases": "Core printing and PDF export are free. Print Pilot Pro is available as a monthly or yearly auto-renewable subscription through Apple. Payment is charged to your Apple Account at confirmation of purchase. The subscription renews automatically unless it is turned off at least 24 hours before the end of the current period, and your account is charged for renewal within 24 hours before the end of the period. You can manage or cancel the subscription in your Apple Account settings.",
        "terms": True,
        "faq": [
            ("My printer doesn't appear.", "Make sure the printer supports AirPrint and is on the same Wi-Fi network as your device, and that Print Pilot has Local Network access (Settings › Print Pilot)."),
            ("A photo prints sideways.", "Open the layout preview and rotate the page before printing. If it still prints incorrectly, email us with the printer model and iOS version."),
            ("How do I cancel Pro?", f'Cancel any time in your Apple Account subscriptions. <a href="{MANAGE_SUBS}">How to cancel a subscription</a>. You keep Pro until the end of the period you paid for.'),
            ("How do I restore Pro on a new device?", "Open the Pro screen in the app and tap Restore Purchases while signed in with the same Apple Account."),
        ],
    },
    {
        "slug": "soccerlineup", "name": "Soccer Lineup", "short": "Soccer Lineup",
        "tagline": "Build formations, set your lineup on the pitch and share a clean image with your team.",
        "summary": "Your teams, players and lineups stay on your device. The app makes no network connections. JL3D does not collect, receive or sell any personal data. There are no ads, no analytics and no tracking.",
        "stored": [
            "Team names, player names and numbers you enter, formations, lineups and pitch drawings.",
            "Display preferences such as kit colours, contrast and name size, and the team you last had open.",
        ],
        "leaves": [
            ("Only when you share", "When you export a lineup image, it is handed to the iOS share sheet and goes only where you send it, such as Messages or Photos."),
        ],
        "permissions": [],
        "purchases": None,
        "kids": "Coaches often enter children's names. Those names are stored only on the coach's device and are never sent to JL3D or anyone else by the app.",
        "faq": [
            ("Where are my lineups saved?", "On your device. They are included in your normal iPhone or iPad backup (iCloud or computer backup)."),
            ("A message says my lineups were saved by a newer version.", "Update Soccer Lineup from the App Store. The app shows that data read-only so an older version can never overwrite it."),
            ("How do I share a lineup?", "Open Save / Export, tap Export PNG, then choose where to send the image."),
        ],
    },
    {
        "slug": "garagelog", "name": "Garage Log", "short": "Garage Log",
        "effective": "26 November 2026",
        "tagline": "Keep every vehicle's service history, reminders and recalls in one place.",
        "summary": "Your vehicles, service records, photos, reminders and backups stay on your device. To decode a VIN, load model lists and check recalls, the app sends only the vehicle details described below to the U.S. National Highway Traffic Safety Administration (NHTSA). JL3D runs no servers for this app and does not receive, sell or share your data. There are no accounts, ads, analytics or tracking.",
        "stored": [
            "Vehicles you add (year, make, model, trim, engine, body class, fuel type, VIN if you enter one, colour, licence plate, nickname, odometer readings and purchase details).",
            "Service records, parts, costs, shop names, notes and service reminders.",
            "Vehicle photos you choose with the system photo picker. The app sees only the photo you pick, saves a resized copy and removes embedded metadata such as location. Photos are never uploaded.",
            "Cached NHTSA results (model lists, recalls and complaints), so lookups are not repeated and saved safety results stay available offline.",
            "App preferences, such as distance units and whether reminders are on. Reminders and odometer check-ins are local notifications scheduled by iOS on the device.",
        ],
        "leaves": [
            ("NHTSA vPIC: VIN decoding (Add Vehicle)", "When you add a vehicle by VIN and tap to decode it, the 17-character VIN is sent to vpic.nhtsa.dot.gov. Not stored by the app."),
            ("NHTSA vPIC: Refresh from VIN (Edit Vehicle)", "Only when you tap Refresh from VIN, the vehicle's VIN is sent to vpic.nhtsa.dot.gov. Proposed changes are shown first and nothing is saved until you confirm."),
            ("NHTSA vPIC: model lists", "When you enter a vehicle by hand, the make and model year you pick are sent to vpic.nhtsa.dot.gov to list models. Lists are cached on the device for 30 days. Make and trim lists are built into the app."),
            ("NHTSA recalls and complaints (automatic)", "When you open a vehicle and no fresh results are saved, its make, model and model year (never the VIN) are sent to api.nhtsa.gov. Results are cached for 7 days; if a later refresh fails, the saved results stay visible with a Last updated date."),
            ("Files you choose to create", "Back Up Garage makes one .garagelogbackup file with all your vehicles, records, reminders and photos; Export Service History makes a CSV spreadsheet. You choose where they go (for example Files, iCloud Drive or AirDrop). They are never sent to JL3D and are not encrypted, so keep them somewhere private."),
        ],
        "leaves_note": "Each request uses HTTPS and, like any internet request, reveals your IP address to NHTSA, which handles it under its own privacy policy (nhtsa.gov/about-nhtsa/privacy-policy). Links to NHTSA recall campaign pages carry only the campaign number. Your service records, costs, notes, reminders, licence plate, odometer, photos and backups are never sent to anyone.",
        "label": "On the App Store privacy label, the NHTSA lookups are declared conservatively as Other Data, used only for App Functionality, not linked to you and not used for tracking.",
        "permissions": [
            ("Notifications", "Used only for the service reminders and odometer check-ins you set. They are scheduled on your device."),
            ("Photos", "No library permission is requested. You pick a single photo with the system photo picker."),
        ],
        "purchases": None,
        "faq": [
            ("How do I back up my garage or move to a new iPhone?", "In Settings, tap <strong>Back Up Garage</strong>, then <strong>Save to Files</strong> (for example to iCloud Drive) or <strong>Share or AirDrop</strong>. The file contains all vehicles, records, reminders and photos. It is not encrypted, so keep it private. On the new device, tap <strong>Restore from Backup</strong> in Settings, or tap the file in the Files app and choose Garage Log."),
            ("What happens when I restore a backup?", "Garage Log checks the file and shows what it contains compared with what is on the device. Nothing changes until you tap <strong>Replace My Garage</strong> and confirm. Restoring replaces everything on that device, so you can back up the current garage first from the same screen. If anything goes wrong, your current garage is put back automatically."),
            ("Can I open my records in a spreadsheet?", "Yes. In Settings, tap <strong>Export Service History</strong> to make a CSV file for Numbers, Excel or Google Sheets. It does not include photos and cannot be restored into the app; use Back Up Garage for that."),
            ("My reminders don't appear.", "Check that Service Reminders is on in the app's Settings and that notifications are allowed for Garage Log in the iOS Settings app; the app shows a banner when they are turned off. Mileage reminders use the odometer reading you enter, so update it from time to time; the app can remind you to do that."),
            ("Recalls don't load.", "New recall and complaint lookups need an internet connection. Results already fetched stay available offline with a Last updated date. Recalls are matched by year, make and model, not your VIN, so check your VIN on <a href=\"https://www.nhtsa.gov/recalls\">NHTSA.gov</a> or with a dealer to see whether your vehicle is affected."),
            ("Can I use kilometres?", "Yes. In Settings, choose Distance Units: Miles, Kilometers, or Automatic to follow your region."),
            ("The app says my garage couldn't be opened, or a restore didn't finish.", "Don't delete the app: that would delete your data and its safety copy. Use <strong>Save a Copy</strong> on that screen, free up some storage, tap <strong>Try Again</strong>, and email us if it still doesn't open."),
        ],
    },
]

CSS = """
:root{--bg:#f6f7f9;--surface:#fff;--ink:#16202a;--muted:#5a6672;--line:#dde2e8;--accent:#1f5f99;--accent-ink:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#0f141a;--surface:#161d25;--ink:#e7ecf1;--muted:#98a5b2;--line:#2a3440;--accent:#7fb4e6;--accent-ink:#0f141a;color-scheme:dark}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 -apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",system-ui,sans-serif}
.wrap{max-width:760px;margin:0 auto;padding:40px max(18px,env(safe-area-inset-left)) 64px max(18px,env(safe-area-inset-right))}
header.site{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:28px;font-size:14px;color:var(--muted)}
header.site a{color:var(--ink);font-weight:600;text-decoration:none;letter-spacing:.02em}
h1{font:700 clamp(28px,5vw,38px)/1.15 -apple-system,"SF Pro Display",system-ui,sans-serif;margin:0 0 8px;text-wrap:balance}
h2{font-size:20px;margin:34px 0 8px}
h3{font-size:16px;margin:18px 0 4px}
p,li{max-width:68ch}
a{color:var(--accent)}
.lede{font-size:18px;color:var(--muted);margin:0 0 20px}
.meta{font-size:14px;color:var(--muted)}
.summary{background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:10px;padding:14px 18px;margin:20px 0}
.cards{display:grid;gap:14px;margin-top:24px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:18px 20px}
.card h2{margin:0 0 4px;font-size:19px}
.card p{margin:0 0 10px;color:var(--muted)}
.links{display:flex;gap:16px;flex-wrap:wrap;font-weight:600;font-size:15px}
dl{margin:0} dt{font-weight:600;margin-top:12px} dd{margin:2px 0 0}
details{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:10px 16px;margin:8px 0}
summary{cursor:pointer;font-weight:600}
.contact{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin-top:28px}
footer{margin-top:44px;padding-top:16px;border-top:1px solid var(--line);font-size:13px;color:var(--muted)}
a:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
"""


def page(title, body, depth):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title><style>{CSS.strip()}</style></head>
<body><div class="wrap">
<header class="site"><a href="{up}index.html">JL3D Apps</a><span>{COMPANY}</span></header>
{body}
<footer>© 2026 {COMPANY} · {PLACE} · <a href="mailto:{EMAIL}">{EMAIL}</a></footer>
</div></body></html>
"""


def esc(s):
    return html.escape(s, quote=False)


def privacy(app):
    stored = "".join(f"<li>{esc(x)}</li>" for x in app["stored"])
    leaves = "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in app["leaves"])
    perms = ("<h2>Permissions</h2><dl>" + "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in app["permissions"]) + "</dl>"
             if app["permissions"] else "<h2>Permissions</h2><p>The app asks for no special permissions.</p>")
    purchases = f"<h2>Purchases</h2><p>{esc(app['purchases'])}</p>" if app.get("purchases") else ""
    kids = app.get("kids", "")
    note = f"<p>{esc(app['leaves_note'])}</p>" if app.get("leaves_note") else ""
    label = f"<h2>App Store privacy label</h2><p>{esc(app['label'])}</p>" if app.get("label") else ""
    body = f"""<h1>{esc(app['name'])} Privacy Policy</h1>
<p class="meta">Effective {app.get("effective", EFFECTIVE)} · {COMPANY}</p>
<div class="summary"><strong>In short:</strong> {esc(app['summary'])}</div>
<h2>What the app stores on your device</h2><ul>{stored}</ul>
<p>This data lives in the app's private storage on your device. {esc(app.get('backup_note', "iOS may include it in your own iCloud or computer backup; that is governed by Apple's privacy policy. Deleting the app deletes this data."))}</p>
<h2>What leaves your device</h2><dl>{leaves}</dl>
{note}<p>JL3D runs no servers for this app and receives none of this data.</p>{label}
{perms}
{purchases}
<h2>What we do not do</h2><ul><li>No accounts or sign-in with JL3D.</li><li>No advertising, analytics, crash-reporting or tracking SDKs, and no use of the advertising identifier.</li><li>No selling or sharing of personal data.</li></ul>
<h2>Children</h2><p>The app is suitable for all ages and does not knowingly collect personal information from anyone, including children under 13. {esc(kids)}</p>
<h2>Changes</h2><p>If the app's data practices change, this page is updated before the new version is released, and the effective date above changes.</p>
<div class="contact"><strong>Questions about privacy?</strong> Email <a href="mailto:{EMAIL}">{EMAIL}</a>. We reply within two business days.</div>"""
    return page(f"{app['short']} Privacy Policy · JL3D", body, 1)


def support(app):
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in app["faq"])
    terms = f' · <a href="../terms/{app["slug"]}.html">Terms of Use</a>' if app.get("terms") else ""
    body = f"""<h1>{esc(app['name'])} Support</h1>
<p class="lede">{esc(app['tagline'])}</p>
<div class="contact"><strong>Contact us:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a>. {esc(app.get('support_note', 'Include your device model, iOS version and, if you can, the app version (iPhone Settings › Apps › the app name).'))} We usually reply within two business days.</div>
<h2>Common questions</h2>{faq}
<p class="meta"><a href="../privacy/{app['slug']}.html">Privacy Policy</a>{terms}</p>"""
    return page(f"{app['short']} Support · JL3D", body, 1)


def terms(app):
    body = f"""<h1>{esc(app['name'])} Terms of Use</h1>
<p class="meta">Effective {EFFECTIVE} · {COMPANY}</p>
<p>Your use of {esc(app['name'])} is governed by Apple's <a href="{APPLE_EULA}">Licensed Application End User License Agreement (Standard EULA)</a>, together with the subscription terms below.</p>
<h2>Subscriptions</h2><p>{esc(app['purchases'])}</p>
<p>Prices are shown in the app before you subscribe and may vary by country. If a free trial is offered, any unused portion is forfeited when you purchase a subscription.</p>
<h2>Refunds</h2><p>Purchases are processed by Apple. <a href="{REFUNDS}">Request a refund from Apple</a>.</p>
<h2>Privacy</h2><p>See the <a href="../privacy/{app['slug']}.html">Privacy Policy</a>.</p>
<div class="contact">Questions: <a href="mailto:{EMAIL}">{EMAIL}</a></div>"""
    return page(f"{app['short']} Terms of Use · JL3D", body, 1)


def index():
    cards = ""
    for a in APPS:
        t = f'<a href="terms/{a["slug"]}.html">Terms</a>' if a.get("terms") else ""
        cards += f"""<section class="card"><h2>{esc(a['name'])}</h2><p>{esc(a['tagline'])}</p>
<div class="links"><a href="privacy/{a['slug']}.html">Privacy</a><a href="support/{a['slug']}.html">Support</a>{t}</div></section>"""
    body = f"""<h1>JL3D Apps</h1><p class="lede">Small, focused iOS and Android apps from {COMPANY}. None of them collects personal data.</p>
<div class="cards">{cards}</div>"""
    return page("JL3D Apps · Privacy & Support", body, 0)


def main():
    (ROOT / "index.html").write_text(index())
    for folder in ("privacy", "support", "terms"):
        (ROOT / folder).mkdir(exist_ok=True)
    for a in APPS:
        (ROOT / f"privacy/{a['slug']}.html").write_text(privacy(a))
        (ROOT / f"support/{a['slug']}.html").write_text(support(a))
        if a.get("terms"):
            (ROOT / f"terms/{a['slug']}.html").write_text(terms(a))
    (ROOT / ".nojekyll").write_text("")
    print("built", sum(1 for _ in ROOT.rglob("*.html")), "pages")


if __name__ == "__main__":
    main()
