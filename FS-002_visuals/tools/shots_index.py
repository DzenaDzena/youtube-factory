#!/usr/bin/env python3
"""Build SHOTS_INDEX.csv: one row per shot of the brief, joined with the files chosen in MANIFEST.csv."""
import csv, re, os
BRIEF = os.path.join(os.path.dirname(__file__), "..", "BRIEF_FS-002.md")
MAN = os.path.join(os.path.dirname(__file__), "..", "MANIFEST.csv")
OUT = os.path.join(os.path.dirname(__file__), "..", "SHOTS_INDEX.csv")
shots = []
for line in open(BRIEF, encoding="utf-8"):
    m = re.match(r"\| (S\d{3}[A-Z]) \| ([\d:.–-]+) \| (.*?) \| (.*) \|$", line.strip())
    if m: shots.append(dict(shot=m[1], in_out=m[2], narrator=m[3], need=m[4]))
rows = list(csv.DictReader(open(MAN, encoding="utf-8")))
by = {}
for r in rows: by.setdefault(r["shot"], []).append(r)
cols = ["shot", "in_out", "narrator", "need", "state", "main_file", "main_status", "main_note", "alt1_file", "alt2_file", "extra_files"]
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for s in shots:
        rs = by.get(s["shot"], [])
        real = {r["rank"]: r for r in rs if r["direct_file_url"]}
        extra = [r["file"] for r in rs if r["direct_file_url"] and r["rank"] not in ("main", "alt1", "alt2")]
        if "main" in real: state = "HAS_FILE"
        elif any(r["title"].startswith("DERIVED") for r in rs): state = "CROP_TO_MAKE"
        elif any(r["status"] == "NOT FOUND" for r in rs): state = "NOT_FOUND"
        elif real: state = "ALT_ONLY"
        else: state = "NOT_SEARCHED"
        m = real.get("main") or next((r for r in rs), {})
        w.writerow(dict(**s, state=state, main_file=real["main"]["file"] if "main" in real else "",
                        main_status=m.get("status", ""), main_note=m.get("verify_note", "")[:300],
                        alt1_file=real.get("alt1", {}).get("file", ""), alt2_file=real.get("alt2", {}).get("file", ""),
                        extra_files=" | ".join(extra)))
print(len(shots), "shots written to", os.path.normpath(OUT))
