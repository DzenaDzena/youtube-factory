#!/usr/bin/env python3
"""met.py SHOT RANK OBJECT_ID slug [note]  — Met Open Access download + proof + manifest row"""
import sys, os, json, time, datetime, urllib.request, urllib.parse, csv
sys.path.insert(0, os.path.dirname(__file__))
import fs
UA = fs.UA
def get(url, binary=False):
    url = urllib.parse.quote(url, safe=":/?=&%")
    for i in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120) as r:
                d = r.read(); return d if binary else d.decode()
        except urllib.error.HTTPError as e:
            if e.code in (429, 403, 503): time.sleep(10*(i+1)); continue
            raise
    raise RuntimeError(url)
shot, rank, oid, slug = sys.argv[1:5]; note = sys.argv[5] if len(sys.argv) > 5 else ""
raw = get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{oid}")
d = json.loads(raw)
if not d.get("isPublicDomain") or not d.get("primaryImage"):
    print("REJECT not open access", oid, d.get("title")); sys.exit()
img = d["primaryImage"]; ext = os.path.splitext(img)[1].lower() or ".jpg"
fn = f"{shot}_{rank}__{slug}{ext}"
open(os.path.join(fs.ROOT, fn), "wb").write(get(img, True))
page = d["objectURL"]
html = "(metmuseum.org page not reachable from this network; proof = Met Open Access API record above)"
open(os.path.join(fs.ROOT, "proof", f"{shot}_{rank}__proof.html"), "w").write(
    f"<!-- Met Open Access record saved {datetime.date.today()} -->\n<pre>{json.dumps(d, indent=1, ensure_ascii=False)}</pre>\n<!-- page {page} -->\n" + html)
fs.manifest_row(dict(shot=shot, rank=rank, media="image", status="CC0_VERIFIED", file=fn, title=d["title"],
    creator=d.get("artistDisplayName", ""), date=d.get("objectDate", ""), collection="The Metropolitan Museum of Art (Open Access)",
    item_id=oid, source_page_url=page, direct_file_url=img, licence="CC0 1.0 (Met Open Access, isPublicDomain=true)",
    commercial_use="yes", derivatives_ok="yes", required_credit="The Metropolitan Museum of Art (optional)",
    accessed=str(datetime.date.today()), verify_note=note))
print("OK", fn, os.path.getsize(os.path.join(fs.ROOT, fn)))
