#!/usr/bin/env python3
"""cleveland.py SHOT RANK ID slug [note] - Cleveland Museum of Art Open Access (CC0) download + proof + manifest row"""
import sys, os, json, time, datetime, urllib.request, urllib.parse
sys.path.insert(0, os.path.dirname(__file__)); import fs
def get(u, b=False):
    u = urllib.parse.quote(u, safe=":/?=&%")
    for i in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": fs.UA}), timeout=120) as r:
                d = r.read(); return d if b else d.decode()
        except urllib.error.HTTPError as e:
            if e.code in (429, 503): time.sleep(10*(i+1)); continue
            raise
    raise RuntimeError(u)
shot, rank, aid, slug = sys.argv[1:5]; note = sys.argv[5] if len(sys.argv) > 5 else ""
d = json.loads(get(f"https://openaccess-api.clevelandart.org/api/artworks/{aid}"))["data"]
if d.get("share_license_status") != "CC0":
    print("REJECT not CC0:", aid, d.get("share_license_status")); sys.exit()
img = ((d.get("images") or {}).get("print") or {}).get("url")
if not img: print("REJECT no image", aid); sys.exit()
ext = os.path.splitext(img)[1].lower() or ".jpg"
fn = f"{shot}_{rank}__{slug}{ext}"
open(os.path.join(fs.ROOT, fn), "wb").write(get(img, True))
open(os.path.join(fs.ROOT, "proof", f"{shot}_{rank}__proof.html"), "w").write(
    f"<!-- Cleveland Museum of Art Open Access API record saved {datetime.date.today()} -->\n<pre>{json.dumps(d, indent=1, ensure_ascii=False)[:7000]}</pre>")
cr = (d.get("creators") or [{}])[0].get("description", "")
fs.manifest_row(dict(shot=shot, rank=rank, media="image", status="CC0_VERIFIED", file=fn, title=d.get("title", ""),
    creator=cr, date=d.get("creation_date", ""), collection="Cleveland Museum of Art (Open Access)", item_id=aid,
    source_page_url=d.get("url", ""), direct_file_url=img, licence="CC0 1.0 (share_license_status=CC0)", commercial_use="yes",
    derivatives_ok="yes", required_credit="Cleveland Museum of Art (optional)", accessed=str(datetime.date.today()),
    verify_note=note + " | proof = Cleveland Open Access API record"))
print("OK", fn, os.path.getsize(os.path.join(fs.ROOT, fn)))
