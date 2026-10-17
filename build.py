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
        "slug": "tinyviolin", "name": "World's Tiniest Violin", "short": "Tiny Violin",
        "tagline": "A pocket-sized violin for life's smallest tragedies. Play it for someone who needs it.",
        "summary": "Everything you create in the app stays on your iPhone. JL3D does not collect, receive or sell any personal data. There are no ads, no analytics and no tracking.",
        "stored": [
            "The names or nicknames you add for people you play the violin for, plus their favourite size, sound and signature violin.",
            "Your play history (up to the most recent 100 plays) and simple statistics derived from it.",
            "Your Encores score, streaks and the collection items you have earned or chosen.",
            "App preferences such as haptics and shuffle.",
        ],
        "leaves": [
            ("Apple iCloud (optional)", "If iCloud is turned on for your Apple Account, the app keeps a tiny copy of your progress (Encores total, best streak and the IDs of earned items) in your private iCloud key-value storage so it survives a reinstall. No names, people or play history are synced. This data is stored by Apple under your account; JL3D cannot read it."),
            ("Apple App Store (purchases)", "Tips and optional cosmetic items are purchased through Apple's In-App Purchase. Apple processes the payment; JL3D receives no payment card, name or contact details. The app checks Apple-signed purchase records on your device to unlock what you bought."),
        ],
        "permissions": [],
        "purchases": "The app is free. Optional tips (consumable) and cosmetic items such as violin skins and stages (one-time, non-consumable) are sold through Apple. Tips are optional and unlock nothing. Items you earn by playing are always earnable for free.",
        "faq": [
            ("I can't hear anything.", "Turn the volume up with the side buttons. The violin plays through the media channel and is meant to be heard, so it also plays when the silent switch is on. Check that no Bluetooth device has taken the audio."),
            ("How do I restore a purchase on a new iPhone?", "In the app, tap Restore Purchase (on the store screen or in Settings) while signed in with the same Apple Account."),
            ("I reinstalled and my people and history are gone.", "People and play history are stored only on the device, so deleting the app deletes them. Earned items and your Encores total come back from iCloud if iCloud was on."),
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
        "tagline": "Keep every vehicle's service history, reminders and recalls in one place.",
        "summary": "Your vehicles and service records stay on your device. A few lookups you start are sent directly to public vehicle-data services, as described below. JL3D does not collect, receive or sell any personal data. There are no ads, no analytics and no tracking.",
        "stored": [
            "Vehicles (make, model, year, VIN and nickname), service records, costs, mileage and reminders, in a database on your device.",
            "Cached recall and complaint results, so they are available offline.",
            "App preferences.",
        ],
        "leaves": [
            ("NHTSA vPIC (U.S. Department of Transportation)", "When you decode a VIN, the VIN is sent to vpic.nhtsa.dot.gov to look up the vehicle's details."),
            ("NHTSA recalls and complaints API", "To check recalls and complaints, the vehicle's make, model and year are sent to api.nhtsa.gov. No VIN or personal details are sent for this."),
            ("Wikipedia", "To show a picture of your vehicle model, the make and model are used to look up a public image on en.wikipedia.org."),
            ("Carfax and AutoCheck (only if you tap)", "The vehicle-history links open those websites in your browser with the VIN. Nothing is sent unless you tap a link, and those sites' own privacy policies apply."),
        ],
        "permissions": [
            ("Notifications", "Used only for the service reminders you set. Reminders are scheduled on your device."),
        ],
        "purchases": None,
        "faq": [
            ("Recalls don't load.", "Recall lookups need an internet connection. Results already fetched are shown offline."),
            ("The app says the database couldn't open.", "Your data has not been deleted. Close and reopen the app. If the message stays, email us before deleting the app."),
            ("How do I back up my records?", "In Settings, tap Export Database to save a copy of all your records as a file, or rely on your normal iPhone backup."),
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
    body = f"""<h1>{esc(app['name'])} Privacy Policy</h1>
<p class="meta">Effective {EFFECTIVE} · {COMPANY}</p>
<div class="summary"><strong>In short:</strong> {esc(app['summary'])}</div>
<h2>What the app stores on your device</h2><ul>{stored}</ul>
<p>This data lives in the app's private storage on your device. iOS may include it in your own iCloud or computer backup; that is governed by Apple's privacy policy. Deleting the app deletes this data.</p>
<h2>What leaves your device</h2><dl>{leaves}</dl>
<p>JL3D runs no servers for this app and receives none of this data.</p>
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
<div class="contact"><strong>Contact us:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a>. Include your device model, iOS version and, if you can, the app version (iPhone Settings › Apps › the app name). We usually reply within two business days.</div>
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
    body = f"""<h1>JL3D Apps</h1><p class="lede">Small, focused iOS apps from {COMPANY}. None of them collects personal data.</p>
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
