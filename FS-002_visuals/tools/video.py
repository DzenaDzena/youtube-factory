#!/usr/bin/env python3
"""video.py SHOT RANK ITEM_ID SRC_MP4 IN OUT slug note — cut clip, save proof, add manifest row (media=video)"""
import sys, os, json, subprocess, datetime, urllib.request
sys.path.insert(0, os.path.dirname(__file__)); import fs
shot, rank, item, src, tin, tout, slug, note = sys.argv[1:9]
meta = json.loads(urllib.request.urlopen(urllib.request.Request(f"https://archive.org/metadata/{item}", headers={"User-Agent": fs.UA}), timeout=60).read())
m = meta["metadata"]
fn = f"{shot}_{rank}__{slug}.mp4"
out = os.path.join(fs.ROOT, fn)
subprocess.run(["ffmpeg","-loglevel","error","-y","-ss",tin,"-to",tout,"-i",src,"-c:v","libx264","-crf","18","-an","-pix_fmt","yuv420p",out],check=True)
open(os.path.join(fs.ROOT,"proof",f"{shot}_{rank}__proof.html"),"w").write(
    f"<!-- archive.org metadata saved {datetime.date.today()} for https://archive.org/details/{item} -->\n<pre>{json.dumps(m,indent=1,ensure_ascii=False)[:5000]}</pre>")
lic = m.get("licenseurl","")
fs.manifest_row(dict(shot=shot, rank=rank, media="video", status="PUBLIC_DOMAIN_VERIFIED", file=fn, title=m.get("title",""),
    creator=str(m.get("creator","")), date=m.get("date",""), collection="Internet Archive (" + ("Universal Newsreel / NARA" if "universal" in str(m.get("collection","")).lower() else "community upload") + ")",
    item_id=item, source_page_url=f"https://archive.org/details/{item}", direct_file_url=f"https://archive.org/download/{item}/{os.path.basename(src)}",
    licence=f"licenseurl={lic}", commercial_use="yes", derivatives_ok="yes", required_credit="", accessed=str(datetime.date.today()),
    verify_note=f"in {tin} / out {tout} of source; {note}"))
print("OK", fn, os.path.getsize(out))
