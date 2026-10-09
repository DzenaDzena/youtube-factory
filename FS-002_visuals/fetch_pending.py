#!/usr/bin/env python3
"""Download every MANIFEST.csv row whose file is missing, from direct_file_url.
Run from inside FS-002_visuals/:  python3 fetch_pending.py
Polite pacing for Wikimedia (one request per few seconds, honours Retry-After)."""
import csv, os, time, urllib.request, urllib.error
UA = "FS002-visual-research/1.0 (contact: channel owner)"
rows = list(csv.DictReader(open("MANIFEST.csv")))
todo = [r for r in rows if r["file"] and r["direct_file_url"] and not os.path.exists(r["file"])]
print(len(todo), "files to fetch")
for r in todo:
    for attempt in range(8):
        try:
            req = urllib.request.Request(r["direct_file_url"], headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=120) as resp:
                open(r["file"], "wb").write(resp.read())
            print("OK", r["file"]); break
        except urllib.error.HTTPError as e:
            wait = int(e.headers.get("Retry-After", 30)) if e.code == 429 else 10
            print(" ", e.code, "waiting", wait); time.sleep(min(wait, 120))
        except Exception as e:
            print(" ", e); time.sleep(10)
    time.sleep(4)
