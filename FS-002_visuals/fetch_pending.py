#!/usr/bin/env python3
"""Download every picture listed in MANIFEST.csv that is missing from this folder.

Run from INSIDE the FS-002_visuals folder (the one that contains MANIFEST.csv):
    python3 fetch_pending.py            # all missing files
    python3 fetch_pending.py wikimedia  # only URLs containing 'wikimedia' (optional filter)

Uses the system `curl`, so it trusts the same certificates as your browser.
Video clips (media=video) are cut files, not downloads - they are skipped.
Re-running is safe: files that already exist are skipped.
"""
import csv, os, subprocess, sys, time, urllib.parse

UA = "FS002-visual-research/1.0 (Wikimedia/Met/LOC image fetch for a documentary channel)"

if not os.path.exists("MANIFEST.csv"):
    sys.exit("MANIFEST.csv not found here. Open Terminal INSIDE the FS-002_visuals folder and run again.")

flt = sys.argv[1] if len(sys.argv) > 1 else ""
rows = list(csv.DictReader(open("MANIFEST.csv", encoding="utf-8")))
todo = [r for r in rows
        if r["file"] and r["direct_file_url"] and r["media"] != "video"
        and not os.path.exists(r["file"]) and flt in r["direct_file_url"]]
print(len(todo), "files to fetch")


def retry_after(hdr_path):
    try:
        text = open(hdr_path, errors="replace").read().lower().split("http/")[-1]
        for line in text.splitlines():
            if line.startswith("retry-after:"):
                return int(line.split(":")[1].strip())
    except Exception:
        pass
    return 30


done = failed = 0
for r in todo:
    url = urllib.parse.quote(r["direct_file_url"], safe=":/?=&%")
    part = r["file"] + ".part"
    ok = False
    for attempt in range(10):
        res = subprocess.run(["curl", "-sS", "-L", "-A", UA, "-o", part,
                              "-D", "hdr.tmp", "-w", "%{http_code}", url],
                             capture_output=True, text=True)
        code = res.stdout.strip()
        if code == "200" and os.path.exists(part) and os.path.getsize(part) > 1000:
            os.replace(part, r["file"])
            ok = True
            break
        if os.path.exists(part):
            os.remove(part)
        if code == "429":
            w = min(retry_after("hdr.tmp"), 120)
            print(f"  {r['file'][:40]}: site asks to wait, sleeping {w}s")
            time.sleep(w)
        else:
            print(f"  {r['file'][:40]}: http {code or '?'} {res.stderr.strip()[:80]} (try {attempt + 1})")
            time.sleep(8)
    if ok:
        done += 1
        print("OK", r["file"])
    else:
        failed += 1
        print("FAILED", r["file"], r["direct_file_url"])
    time.sleep(3)

if os.path.exists("hdr.tmp"):
    os.remove("hdr.tmp")
print(f"\nFinished. downloaded: {done}, failed: {failed}. Run again to retry the failed ones.")
