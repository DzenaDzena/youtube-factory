import csv, re, os, collections, datetime
BRIEF="/root/.claude/uploads/c92badab-9905-5e78-96ab-c528a844811e/e6d02637-08A___BRIEF___VISUAL_SEARCH.md"
ROOT="/home/user/youtube-factory/FS-002_visuals"
shots=[]
for line in open(BRIEF):
    m=re.match(r"\| (S\d{3}[A-Z]) \| ([\d:.–-]+) \| (.*?) \| (.*) \|$", line.strip())
    if m: shots.append(dict(shot=m[1], tc=m[2], say=m[3], need=m[4]))
rows=list(csv.DictReader(open(f"{ROOT}/MANIFEST.csv")))
real=[r for r in rows if r['direct_file_url']]
derived=[r for r in rows if r['title'].startswith('DERIVED')]
nf=[r for r in rows if r['status']=='NOT FOUND']
by=collections.defaultdict(list)
for r in real: by[r['shot']].append(r)
have=lambda r: os.path.exists(f"{ROOT}/{r['file']}")
st=collections.Counter(r['status'] for r in real)
cov=[s for s in shots if s['shot'] in by]
dshots={r['shot'] for r in derived}; nshots={r['shot'] for r in nf}
pend=[r for r in real if not have(r)]
three=[s for s in cov if len(by[s['shot']])>=3]
vids=[r for r in real if r['media']=='video']
jewel_unchecked=[s for s in cov if '[JEWEL]' in s['need'] and not any('CHECKED VISUALLY' in r['verify_note'].upper() for r in by[s['shot']])]
w=[]; a=w.append
a(f"# FS-002 visuals — REPORT\n\n_Generated {datetime.date.today()} from MANIFEST.csv_\n")
a("## Summary\n")
a(f"- Shots in brief: **{len(shots)}**")
a(f"- Shots with a real candidate (file + licence): **{len(cov)}**")
a(f"- Shots to be cut as crops/composites of those files: **{len(dshots)}**")
a(f"- Shots marked NOT FOUND (leads in manifest): **{len(nshots)}**")
a(f"- Shots with the full main + 2 alt: **{len(three)}** (second pass for alternates was not done)")
a(f"- Candidate rows: **{len(real)}** — "+", ".join(f"{k}: {v}" for k,v in sorted(st.items())))
a(f"- Video clips cut: **{len(vids)}** (target in brief ~40; see VIDEO_LEADS.md)")
a(f"- Files on disk: **{len(real)-len(pend)}**; **{len(pend)}** rows have licence + direct URL but the image is not downloaded yet\n")
a("## 1. What you must do first: download the missing files\n")
a("`upload.wikimedia.org` blocks image downloads from the cloud environment used for this work (HTTP 429, Retry-After 600). "
  "Licences, authors and proof pages for those files were checked on Commons and are saved. Download the images on a normal computer, from inside `FS-002_visuals/`:\n\n```\npython3 fetch_pending.py\n```\n")
a("Met, LOC and archive.org files are already downloaded. Note: metmuseum.org pages were unreachable, so Met proofs are the Open Access API record (`isPublicDomain: true`).\n")
a("## 2. Rows that need a human decision (status VERIFY)\n")
for r in real:
    if r['status']=='VERIFY': a(f"- **{r['shot']}/{r['rank']}** {r['title'][:55]} — {r['verify_note'][:330]}")
a("\nOther files carry `VERIFY RIGHTS` / `JEWEL VERIFY` in `verify_note` even when status is a verified one; search the CSV for those words.\n")
a("## 3. [JEWEL] shots not visually checked\n")
a("I could only look at pictures that were downloaded. For Commons images (not yet downloaded) the jewel must be checked after `fetch_pending.py`.\n")
for s in jewel_unchecked: a(f"- **{s['shot']}** — {s['need'][:90]}")
a("\n## 4. Shots to cut as crops / composites (from files already in the manifest)\n")
for r in derived: a(f"- **{r['shot']}** — {r['verify_note'][9:260]}")
a("\n## 5. NOT FOUND (with leads)\n")
for r in nf:
    s=next((x for x in shots if x['shot']==r['shot']),{'tc':'','need':''})
    a(f"- **{r['shot']}** {s['tc']} — need: {s['need'][:70]} — **why / lead:** {r['verify_note'][:300]}")
a("\n## 6. Decisions I made that you may want to know\n")
for r in real:
    if 'CHECKED VISUALLY' in r['verify_note'].upper() and ('NOT' in r['verify_note'] or 'WARNING' in r['verify_note']):
        a(f"- **{r['shot']}/{r['rank']}**: {r['verify_note'][:300]}")
open(f"{ROOT}/REPORT.md","w").write("\n".join(w)+"\n")
print(len(shots),"shots;",len(cov),"real;",len(dshots),"derived;",len(nshots),"not found;",len(pend),"pending;",len(jewel_unchecked),"jewel unchecked;",len(vids),"videos")
