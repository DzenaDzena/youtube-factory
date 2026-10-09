import csv, re, datetime
BRIEF="/root/.claude/uploads/c92badab-9905-5e78-96ab-c528a844811e/e6d02637-08A___BRIEF___VISUAL_SEARCH.md"
ROOT="/home/user/youtube-factory/FS-002_visuals"
COLS="shot,rank,media,status,file,title,creator,date,collection,item_id,source_page_url,direct_file_url,licence,commercial_use,derivatives_ok,required_credit,accessed,verify_note".split(",")
shots=[]
for line in open(BRIEF):
    m=re.match(r"\| (S\d{3}[A-Z]) \| ([\d:.–-]+) \| (.*?) \| (.*) \|$", line.strip())
    if m: shots.append(m[1])
rows=list(csv.DictReader(open(f"{ROOT}/MANIFEST.csv")))
covered={r['shot'] for r in rows}
today=str(datetime.date.today())
CROP={
 "S054A":"S053A main (Winterhalter 1859) - crop on earrings/necklace",
 "S075A":"S074A main / S075B main (Fildes 1905) - crop on jewels at the bodice",
 "S070A":"S066A main (Frederik VII, Schiott) - different crop",
 "S193A":"S002A main (Carolus-Duran, Greville) - same painting, different crop",
 "S127B":"composite of five first-wearer portraits already in the manifest: Victoria (S015A/S061A), Alexandra (S065A), Maria Pavlovna (S101A), Augusta (S122A), Mary (S003A)",
 "S255B":"same five-portrait composite as S127B, faded",
 "S247A":"S228A main (Nationaal Archief 1947, 902-4695) - full frame; JEWEL: check tiara visible",
 "S248B":"S228A / S229A (Nationaal Archief 1947) - crop on the tiara",
 "S256A":"S229A main (Nationaal Archief 1947, 902-4694 crop) - soft focus",
}
NF={
 "S020A":"No facsimile of Victoria's 10 Feb 1840 journal page found with clear rights. Lead: archive.org 'girlhoodofqueenv01victuoft' (1912, NOT_IN_COPYRIGHT) - printed text pages of the diaries; RCT facsimile not allowed.",
 "S021A":"No clear-rights 'Victoria writing' image found. Lead: Commons category 'Queen Victoria' paintings (e.g. Victoria at desk by Sir George Hayter / Tuxen) - search Commons 'Queen Victoria writing'.",
 "S021B":"Close-up of a journal page: use S028A/S112A style page scans from archive.org ('girlhoodofqueenv01victuoft' pages with diary text) - not yet cut.",
 "S022B":"Lead: archive.org 'A complete narrative of the celebration of the nuptials of Her Most Gracious Majesty Queen Victoria' (PD, 1840) - procession plates; also ILN 1840 on archive.org. Not downloaded.",
 "S044A":"No PD Garrard shop image found. Lead: Commons category 'Garrard & Co'; archive.org Victorian guidebooks to London (Regent St / Haymarket).",
 "S087A":"Same as S044A (Garrard shop 1880s) - NOT FOUND; GFX card suggested in the brief.",
 "S133A":"Same as S044A (Garrard) - NOT FOUND; GFX 'Lover's Knot' suggested.",
 "S052A":"No clear-rights photo of Victoria in widowhood wearing the necklace found. Lead: Commons 'Queen Victoria' 1880s-90s photographs (Bassano/Downey/Hughes & Mullins) - check each file page.",
 "S067A":"No ILN 1863 engraving of the Dagmar necklace found. Lead: archive.org Illustrated London News vol. 42 (1863) and Met plate S065B (parure of the Prince of Wales - NOT Dagmar).",
 "S077A":"By brief: GFX card only (book cover is copyrighted) - not a search shot.",
 "S084A":"No clear 1888 silver wedding image. Lead: Commons 'Queen Alexandra' 1888 prints (BM). S009A already uses BM 1902,1011.10420.",
 "S085A":"Lead: Judge magazine 2 Jul 1887 (Commons, PD) - Victorian caricature, not a court-dress photo. No photo with clear rights found.",
 "S088A":"LOC Prokudin-Gorskii search returned Armenian/Georgian/Bashkir women, none in a Russian kokoshnik. Lead: loc.gov/collections/prokudin-gorskii - browse 'peasant girls' items manually.",
 "S103A":"No wedding-1874 / St Petersburg 1870s image beyond S082B. Lead: Commons category 'Saint Petersburg in the 1870s'.",
 "S113A":"No Petrograd railway station photo found. Lead: LOC Bain collection 'Petrograd' 1917; Commons 'Nikolaevsky station 1917'.",
 "S121A":"JEWEL: no rights-clear photo of Elizabeth II in the Vladimir tiara with emeralds found. Lead: Nationaal Archief 1958 state-visit photos (S189A candidates 909-4441/4460) - check whether the tiara is the Vladimir; LAC 1959 portrait is the version with pearls.",
 "S143B":"JEWEL: no rights-clear photo of Catherine in the Lover's Knot found. Lead: Commons 'Catherine, Princess of Wales' diplomatic reception 2015+ (tiara worn 2015-2019); only CC licences count.",
 "S153B":"No Queen Mary 1910 photo found. Lead: Commons 'Duchess of York, 1898' (No restrictions) shows Mary of Teck, but 12 years early.",
 "S169A":"No rights-clear 1940s photo of Queen Elizabeth (consort). Lead: UK National Archives INF3-78 (S209B), Universal Newsreel 1939 tour (VIDEO_LEADS.md).",
 "S179A":"No rights-clear photo of Asscher cleaving the Cullinan 1908 found. Lead: Commons category 'Cullinan Diamond'; Asscher Museum / Rijksmuseum (check CC0) .",
 "S180A":"Same as S179A - Asscher workshop 1908 photo not found.",
 "S186A":"JEWEL: no PD photo of Queen Mary wearing the Cullinan III/IV brooch found. Lead: S182A candidates (LOC 2014716428, Autochrome 1914) - check visually after download.",
 "S187A":"JEWEL: no photo of Mary in the Delhi Durbar tiara with Cullinan found. Lead: S168A candidate; Commons category 'Delhi Durbar tiara'.",
 "S210A":"No rights-clear portrait of Queen Elizabeth (consort) 1940s beyond S209B. Lead: Commons 'Queen Elizabeth The Queen Mother' US Gov / Canadian archives 1939.",
 "S213A":"No rights-clear later photo of the Queen Mother found. Lead: Commons 'Queen Elizabeth The Queen Mother' 1980s-90s (US gov: DoD/NARA) - not located.",
 "S216A":"JEWEL: 2011 Turkey state banquet photo not found with clear rights (the only banquet photo found is 1954). Lead: Turkish Presidency press photos (check licence) / Royal Collection (not allowed).",
 "S235A":"Queen Mother in later years: only 1958 Queensland State Archives photos (S234A) found. Lead: Commons 'Queen Elizabeth The Queen Mother' 1990s-2002.",
 "S246A":"JEWEL: no PD photo of Queen Mary in the Fringe tiara confirmed. Lead: S153B/S222A candidate 'Queen Mary of Teck (8543179876)' CC BY 2.0 - check which tiara; Commons 'Queen Mary' portraits 1930s.",
 "S249B":"(see S249B main) - listed as covered if present.",
}
add=[]
for s in shots:
    if s in covered: continue
    if s in CROP:
        add.append(dict(shot=s,rank="main",media="image",status="VERIFY",file="",title="DERIVED CROP / COMPOSITE of files already in manifest",
            accessed=today,licence="inherits licence of the source file(s)",verify_note="DERIVED: "+CROP[s]+". Cut after the source file is downloaded; different crop for each shot per brief rule."))
    elif s in NF:
        add.append(dict(shot=s,rank="main",media="image",status="NOT FOUND",file="",accessed=today,verify_note=NF[s]))
    else:
        add.append(dict(shot=s,rank="main",media="image",status="NOT FOUND",file="",accessed=today,verify_note="No candidate found in this session; not searched with a dedicated query yet."))
with open(f"{ROOT}/MANIFEST.csv","a",newline="") as f:
    w=csv.DictWriter(f,fieldnames=COLS)
    for r in add: w.writerow({c:r.get(c,"") for c in COLS})
print(len(add),"rows appended; crops:",sum(1 for r in add if r['status']=='VERIFY'),"not found:",sum(1 for r in add if r['status']=='NOT FOUND'))
