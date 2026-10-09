#!/usr/bin/env python3
"""Build TIMELINE.json for Remotion from BRIEF_FS-002.md (in/out timecodes) + MANIFEST.csv (chosen files).
Each entry: shot, startSec/endSec/durationSec, startFrame/durationFrames (30 fps), files{main,alt1,alt2}, state, credit, flags."""
import csv, json, re, os
D = os.path.join(os.path.dirname(__file__), "..")
FPS = 30
def sec(tc):  # 'MM:SS.ss'
    m, s = tc.split(":"); return int(m) * 60 + float(s)
rows = list(csv.DictReader(open(os.path.join(D, "MANIFEST.csv"), encoding="utf-8")))
by = {}
for r in rows: by.setdefault(r["shot"], []).append(r)
out = []
for line in open(os.path.join(D, "BRIEF_FS-002.md"), encoding="utf-8"):
    m = re.match(r"\| (S\d{3}[A-Z]) \| ([\d:.]+)–([\d:.]+) \| (.*?) \| (.*) \|$", line.strip())
    if not m: continue
    shot, a, b, say, need = m.groups()
    s0, s1 = sec(a), sec(b)
    rs = by.get(shot, [])
    real = {r["rank"]: r for r in rs if r["direct_file_url"]}
    files = {k: (real[k]["file"] if k in real else None) for k in ("main", "alt1", "alt2")}
    extra = [r["file"] for r in rs if r["direct_file_url"] and r["rank"] not in ("main", "alt1", "alt2")]
    if files["main"]: state = "HAS_FILE"
    elif any(r["title"].startswith("DERIVED") for r in rs): state = "CROP_TO_MAKE"
    elif any(r["status"] == "NOT FOUND" for r in rs): state = "NOT_FOUND"
    else: state = "ALT_ONLY" if real else "NOT_SEARCHED"
    credits = {k: real[k]["required_credit"] for k in real if real[k]["required_credit"]}
    notes = " | ".join(real[k]["verify_note"][:160] for k in ("main",) if k in real)
    out.append(dict(shot=shot, startSec=round(s0, 2), endSec=round(s1, 2), durationSec=round(s1 - s0, 2),
        startFrame=round(s0 * FPS), durationFrames=max(1, round((s1 - s0) * FPS)), narrator=say, need=need[:140],
        state=state, files=files, extraFiles=extra, credits=credits,
        isJewelShot="[JEWEL]" in need, needsCheck=bool(re.search(r"VERIFY", notes)), note=notes))
json.dump(dict(fps=FPS, assetsFolder="FS-002_visuals", shots=out), open(os.path.join(D, "TIMELINE.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "shots,", sum(1 for s in out if s["state"] == "HAS_FILE"), "with a file ->", os.path.normpath(os.path.join(D, "TIMELINE.json")))
