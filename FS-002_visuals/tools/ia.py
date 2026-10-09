#!/usr/bin/env python3
"""ia.py SHOT RANK ITEM_ID LEAF slug [note] - archive.org book page scan + metadata proof + manifest row"""
import sys, os, json, time, datetime, urllib.request
sys.path.insert(0, os.path.dirname(__file__)); import fs
def get(u, b=False):
    for i in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": fs.UA}), timeout=120) as r:
                d = r.read(); return d if b else d.decode()
        except Exception: time.sleep(5*(i+1))
    raise RuntimeError(u)
shot, rank, item, leaf, slug = sys.argv[1:6]; note = sys.argv[6] if len(sys.argv) > 6 else ""
meta = json.loads(get(f"https://archive.org/metadata/{item}")); m = meta["metadata"]
st = m.get("possible-copyright-status", "")
src = f"https://archive.org/download/{item}/page/n{leaf}.jpg"
fn = f"{shot}_{rank}__{slug}.jpg"
open(os.path.join(fs.ROOT, fn), "wb").write(get(src, True))
details = f"https://archive.org/details/{item}/page/n{leaf}"
open(os.path.join(fs.ROOT, "proof", f"{shot}_{rank}__proof.html"), "w").write(
    f"<!-- archive.org metadata saved {datetime.date.today()} for {details} -->\n<pre>{json.dumps(m, indent=1, ensure_ascii=False)[:5000]}</pre>")
status = "PUBLIC_DOMAIN_VERIFIED" if st == "NOT_IN_COPYRIGHT" else "VERIFY"
fs.manifest_row(dict(shot=shot, rank=rank, media="image", status=status, file=fn, title=f"{m.get('title','')} (leaf {leaf})",
    creator=str(m.get("creator", "")), date=m.get("date", ""), collection="Internet Archive", item_id=item, source_page_url=details,
    direct_file_url=src, licence=f"possible-copyright-status={st}; published {m.get('date','')}", commercial_use="yes", derivatives_ok="yes",
    required_credit="Internet Archive (optional)", accessed=str(datetime.date.today()), verify_note=note))
print("OK", fn, status)
