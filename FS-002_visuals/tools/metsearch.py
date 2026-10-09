import sys, json, urllib.request, urllib.parse, time
UA="FS002-visual-research/1.0 (alesiatrus15@gmail.com)"
def j(u):
    for i in range(4):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=40))
        except Exception as e: time.sleep(3)
for q in sys.argv[1:]:
    print("###",q)
    r=j("https://collectionapi.metmuseum.org/public/collection/v1.1/search?hasImages=true&isPublicDomain=true&limit=40&q="+urllib.parse.quote(q))
    ids=(r or {}).get("objectIDs") or []
    n=0
    for i in ids[:12]:
        d=j(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}")
        if d and d.get("isPublicDomain") and d.get("primaryImage"):
            print(i,"|",d["title"][:60],"|",d.get("artistDisplayName","")[:30],"|",d.get("objectDate"),"|",d.get("objectName"))
            n+=1
            if n>=5: break
