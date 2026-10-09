#!/usr/bin/env python3
"""Helpers for FS-002 visual search. Usage:
  fs.py search "<query>" [n]            search Commons File: namespace, print title + licence
  fs.py info "File:Name.jpg"            print licence metadata
  fs.py get SHOT RANK "File:Name.jpg" "slug" ["verify note"]   download + proof + manifest row
"""
import sys, os, re, csv, json, time, html, datetime, urllib.parse, urllib.request

ROOT = "/home/user/youtube-factory/FS-002_visuals"
UA = "FS002-visual-research/1.0 (alesiatrus15@gmail.com)"
API = "https://commons.wikimedia.org/w/api.php"
COLS = "shot,rank,media,status,file,title,creator,date,collection,item_id,source_page_url,direct_file_url,licence,commercial_use,derivatives_ok,required_credit,accessed,verify_note".split(",")


def throttle(gap=4.0):
    import fcntl
    p = "/tmp/fs_last_req"
    with open(p, "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        try:
            last = float(f.read() or 0)
        except ValueError:
            last = 0
        wait = last + gap - time.time()
        if wait > 0:
            time.sleep(wait)
        f.seek(0); f.truncate(); f.write(str(time.time()))


def http(url, binary=False, tries=12):
    for i in range(tries):
        throttle()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                d = r.read()
                return d if binary else d.decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                ra = e.headers.get("Retry-After")
                if ra and ra.isdigit() and int(ra) >= 300:
                    raise SystemExit(f'BLOCKED retry-after {ra}s on {url[:80]}')
                time.sleep(min(120, int(ra)) if ra and ra.isdigit() else min(90, 10 + 10 * i))
                continue
            raise
        except Exception:
            time.sleep(5)
    raise RuntimeError("failed " + url)


def api(**p):
    p["format"] = "json"
    return json.loads(http(API + "?" + urllib.parse.urlencode(p)))


def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def info(title):
    d = api(action="query", titles=title, prop="imageinfo", iiprop="url|size|mime|extmetadata")
    page = list(d["query"]["pages"].values())[0]
    if "imageinfo" not in page:
        return None
    ii = page["imageinfo"][0]
    m = ii["extmetadata"]
    g = lambda k: strip(m.get(k, {}).get("value", ""))
    return {
        "title": page["title"], "url": ii["url"].split("?")[0], "page": ii["descriptionurl"],
        "w": ii["width"], "h": ii["height"], "size": ii["size"],
        "lic": g("LicenseShortName"), "licurl": g("LicenseUrl"), "usage": g("UsageTerms"),
        "artist": g("Artist"), "credit": g("Credit"), "date": g("DateTimeOriginal") or g("DateTime"),
        "desc": g("ImageDescription"), "cats": g("Categories"), "restr": g("Restrictions"),
        "attr_req": g("AttributionRequired"), "copyrighted": g("Copyrighted"), "id": page["pageid"],
    }


def classify(i):
    l = (i["lic"] + " " + i["usage"]).lower()
    if re.search(r"\bnc\b|-nc|noncommercial|\bnd\b|-nd", l):
        return "REJECT", "NC/ND"
    if "cc0" in l or "cc-zero" in l or "public domain dedication" in l:
        return "CC0_VERIFIED", ""
    if re.search(r"public domain|\bpd\b|no known copyright|pdm", l) or i["copyrighted"].lower() == "false":
        return "PUBLIC_DOMAIN_VERIFIED", ""
    if "cc by" in l:
        return "CC_BY_VERIFIED", ""
    return "VERIFY", "licence not auto-classified: " + i["lic"]


def search(q, n=10):
    d = api(action="query", generator="search", gsrsearch=q, gsrnamespace=6, gsrlimit=n,
            prop="imageinfo", iiprop="url|size|extmetadata")
    for page in sorted(d.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 0)):
        ii = (page.get("imageinfo") or [{}])[0]
        m = ii.get("extmetadata", {})
        lic = strip(m.get("LicenseShortName", {}).get("value", ""))
        dt = strip(m.get("DateTimeOriginal", {}).get("value", "") or m.get("DateTime", {}).get("value", ""))[:10]
        print(f'{page["title"]} | {lic} | {ii.get("width")}x{ii.get("height")} | {dt}')


def manifest_row(row):
    p = os.path.join(ROOT, "MANIFEST.csv")
    new = not os.path.exists(p)
    with open(p, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        if new:
            w.writeheader()
        w.writerow({c: row.get(c, "") for c in COLS})


def get(shot, rank, title, slug, note=""):
    i = info(title)
    if not i:
        print("NO SUCH FILE", title); return
    status, why = classify(i)
    if status == "REJECT":
        print("REJECTED", title, i["lic"]); return
    ext = os.path.splitext(i["url"])[1].lower() or ".jpg"
    fn = f"{shot}_{rank}__{slug}{ext}"
    pending = ""
    try:
        data = http(i["url"], binary=True, tries=3)
        open(os.path.join(ROOT, fn), "wb").write(data)
    except BaseException as e:
        pending = "IMAGE NOT DOWNLOADED (upload.wikimedia.org rate-limits this environment) - run fetch_pending.py; "
        print("  download failed:", str(e)[:80])
    page = http(i["page"])
    pr = os.path.join(ROOT, "proof", f"{shot}_{rank}__proof.html")
    open(pr, "w").write(f"<!-- saved {datetime.date.today()} from {i['page']} -->\n" + page)
    attr = i["artist"] if i["lic"].upper().startswith("CC BY") else ""
    cred = f"{i['artist']} / {i['lic']}" if i["lic"].upper().startswith("CC BY") else ""
    row = dict(shot=shot, rank=rank, media="image", status=status, file=fn, title=i["title"],
               creator=i["artist"][:200], date=i["date"][:10], collection="Wikimedia Commons",
               item_id=i["id"], source_page_url=i["page"], direct_file_url=i["url"],
               licence=i["lic"], commercial_use="yes", derivatives_ok="yes",
               required_credit=cred, accessed=str(datetime.date.today()),
               verify_note=(pending + note + " " + why).strip() + f" [{i['w']}x{i['h']}]")
    manifest_row(row)
    print("OK", fn, status, i["lic"], f"{i['w']}x{i['h']}")


if __name__ == "__main__":
    c = sys.argv[1]
    if c == "search":
        search(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 10)
    elif c == "info":
        print(json.dumps(info(sys.argv[2]), indent=1, ensure_ascii=False))
    elif c == "get":
        get(*sys.argv[2:7])
