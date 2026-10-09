#!/usr/bin/env python3
"""loc.py SHOT RANK PK slug [note]  — LOC Prints&Photographs (pictures/item) download + proof + manifest"""
import sys, os, json, time, datetime, urllib.request, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))
import fs
def get(url, binary=False):
    url = urllib.parse.quote(url, safe=":/?=&%")
    for i in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": fs.UA}), timeout=180) as r:
                d = r.read(); return d if binary else d.decode()
        except urllib.error.HTTPError as e:
            if e.code in (429, 503, 520, 522, 524): time.sleep(15*(i+1)); continue
            raise
    raise RuntimeError(url)
shot, rank, pk, slug = sys.argv[1:5]; note = sys.argv[5] if len(sys.argv) > 5 else ""
raw = get(f"https://www.loc.gov/pictures/item/{pk}/?fo=json"); d = json.loads(raw); it = d.get("item", d)
rights = it.get("rights_information", "")
if "no known restrictions" not in rights.lower() and "no restrictions" not in rights.lower():
    print("REJECT rights:", rights[:120]); sys.exit()
urls = [u for u in set(__import__("re").findall(r"https://(?:cdn|tile)\.loc\.gov/[^\"' ]+", raw))]
tif = [u for u in urls if u.endswith("u.tif")]; jpg = [u for u in urls if u.endswith("v.jpg")] or [u for u in urls if u.endswith("r.jpg")]
src = (([] if os.environ.get("LOC_JPG") else tif) or jpg)[0]; ext = os.path.splitext(src)[1]
fn = f"{shot}_{rank}__{slug}{ext}"
open(os.path.join(fs.ROOT, fn), "wb").write(get(src, True))
page = f"https://www.loc.gov/pictures/item/{pk}/"
try: html = get(page)
except Exception as e: html = f"(page fetch failed: {e})"
open(os.path.join(fs.ROOT, "proof", f"{shot}_{rank}__proof.html"), "w").write(f"<!-- LOC page saved {datetime.date.today()} {page} -->\n" + html + "\n<!--JSON-->\n<pre>" + json.dumps(it, indent=1)[:6000] + "</pre>")
fs.manifest_row(dict(shot=shot, rank=rank, media="image", status="PUBLIC_DOMAIN_VERIFIED", file=fn, title=it.get("title", ""),
    creator=", ".join((c.get("title") or c.get("name") or str(c)) if isinstance(c, dict) else str(c) for c in (it.get("creators") or [it.get("creator", "")])), date=it.get("created_published_date", ""),
    collection="Library of Congress, Prints & Photographs", item_id=it.get("reproduction_number", pk), source_page_url=page, direct_file_url=src,
    licence="No known restrictions on publication (LOC)", commercial_use="yes", derivatives_ok="yes", required_credit="Library of Congress, Prints & Photographs Division (courtesy)",
    accessed=str(datetime.date.today()), verify_note=(note + " | " + rights[:100]).strip(" |")))
print("OK", fn, os.path.getsize(os.path.join(fs.ROOT, fn)))
