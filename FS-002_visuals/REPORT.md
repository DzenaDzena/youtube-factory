# FS-002 visuals — REPORT

_Generated 2026-10-09 from MANIFEST.csv_

## Summary

- Shots in brief: **175**
- Shots with a real candidate (file + licence): **142**
- Shots to be cut as crops/composites of those files: **9**
- Shots marked NOT FOUND (leads in manifest): **24**
- Shots with the full main + 2 alt: **19** (second pass for alternates was not done)
- Candidate rows: **235** — CC0_VERIFIED: 48, CC_BY_VERIFIED: 31, PUBLIC_DOMAIN_VERIFIED: 153, VERIFY: 3
- Video clips cut: **3** (target in brief ~40; see VIDEO_LEADS.md)
- Files on disk: **67**; **168** rows have licence + direct URL but the image is not downloaded yet

## 1. What you must do first: download the missing files

`upload.wikimedia.org` blocks image downloads from the cloud environment used for this work (HTTP 429, Retry-After 600). Licences, authors and proof pages for those files were checked on Commons and are saved. Download the images on a normal computer, from inside `FS-002_visuals/`:

```
python3 fetch_pending.py
```

Met, LOC and archive.org files are already downloaded. Note: metmuseum.org pages were unreachable, so Met proofs are the Open Access API record (`isPublicDomain: true`).

## 2. Rows that need a human decision (status VERIFY)

- **S058A/main** File:Elizabeth II waves from the palace balcony after t — Basis: Flickr Commons 'No known copyright restrictions' statement by National Media Museum (photographer Paul Thompson, 1953); NOT an explicit public-domain declaration - Max to accept or reject. JEWEL: check visually what she wears on the balcony. Not the Beaton portrait. | JEWEL VERIFY: licence status 'No restrictions' - check
- **S191A/alt1** File:Queen Elizabeth II with her British Prime Minister — IMAGE NOT DOWNLOADED (upload.wikimedia.org rate-limits this environment) - run fetch_pending.py; OGL v3 - licence not in allowed list: VERIFY licence not auto-classified: OGL 3 [1800x1323]
- **S068A/main** Queen Dagmar's Cross, facsimile in gold and colors of t — CHECKED VISUALLY: plate showing both sides of the Dagmar Cross (facsimile in gold and colours, 1863). Fits 'a cross buried with Dagmar'. Rights: book published London 1863 (PD by age) but archive.org has no copyright-status flag; Commons also tags it public domain.

Other files carry `VERIFY RIGHTS` / `JEWEL VERIFY` in `verify_note` even when status is a verified one; search the CSV for those words.

## 3. [JEWEL] shots not visually checked

I could only look at pictures that were downloaded. For Commons images (not yet downloaded) the jewel must be checked after `fetch_pending.py`.

- **S001A** — **[JEWEL]** Queen Elizabeth II in a tiara and jewels, any rights-clear photo 1950s–2010s (
- **S005A** — **[JEWEL]** Imperial State Crown / Crown regalia PD image (Tower of London regalia engravi
- **S017A** — **[JEWEL]** Albert's sapphire brooch — rights-clear photo of Elizabeth II wearing it (Comm
- **S031A** — **[JEWEL]** Elizabeth II wearing the sapphire brooch (same source as beat 17, different cr
- **S048A** — **[JEWEL]** Coronation Necklace pendant — Elizabeth II wearing it (Commons "Queen_Elizabet
- **S058A** — **[JEWEL]** Elizabeth II 1953 coronation-day image that is rights-clear (NOT Beaton portra
- **S089A** — **[JEWEL]** Kokoshnik tiara — Elizabeth II wearing it (Commons 1957 candidate, verify; US 
- **S105A** — **[JEWEL]** Vladimir tiara — LAC 1959 portrait of Elizabeth II (PD-Canada-Crown, verify)
- **S119A** — **[JEWEL]** LAC 1959 tour portrait (PD) full frame
- **S121B** — **[JEWEL]** with pearls (LAC 1959)
- **S142A** — **[JEWEL]** Diana wearing Lover's Knot — US gov PD photo (White House/DoD 1985 visit; veri
- **S164A** — **[JEWEL]** Delhi Durbar necklace image — Queen Mary 1911–12 photo crop (PD) ; GFX "8.8 ct
- **S191A** — **[JEWEL]** Elizabeth II 2012 Diamond Jubilee with brooch — rights-clear (Commons CC/gov, 
- **S222A** — **[JEWEL]** Queen Mary wearing the Fringe tiara (PD photo, verify)
- **S229A** — **[JEWEL]** 1947 wedding photo crop on tiara (Nationaal Archief CC0 / PD gov newsreel)
- **S250A** — **[JEWEL]** 1947 wedding photo slow push

## 4. Shots to cut as crops / composites (from files already in the manifest)

- **S054A** — S053A main (Winterhalter 1859) - crop on earrings/necklace. Cut after the source file is downloaded; different crop for each shot per brief rule.
- **S070A** — S066A main (Frederik VII, Schiott) - different crop. Cut after the source file is downloaded; different crop for each shot per brief rule.
- **S075A** — S074A main / S075B main (Fildes 1905) - crop on jewels at the bodice. Cut after the source file is downloaded; different crop for each shot per brief rule.
- **S127B** — composite of five first-wearer portraits already in the manifest: Victoria (S015A/S061A), Alexandra (S065A), Maria Pavlovna (S101A), Augusta (S122A), Mary (S003A). Cut after the source file is downloaded; different crop for each shot per brief rule.
- **S193A** — S002A main (Carolus-Duran, Greville) - same painting, different crop. Cut after the source file is downloaded; different crop for each shot per brief rule.
- **S247A** — S228A main (Nationaal Archief 1947, 902-4695) - full frame; JEWEL: check tiara visible. Cut after the source file is downloaded; different crop for each shot per brief rule.
- **S248B** — S228A / S229A (Nationaal Archief 1947) - crop on the tiara. Cut after the source file is downloaded; different crop for each shot per brief rule.
- **S255B** — same five-portrait composite as S127B, faded. Cut after the source file is downloaded; different crop for each shot per brief rule.
- **S256A** — S229A main (Nationaal Archief 1947, 902-4694 crop) - soft focus. Cut after the source file is downloaded; different crop for each shot per brief rule.

## 5. NOT FOUND (with leads)

- **S020A** 01:25.48–01:28.18 — need: Queen Victoria's journal page facsimile (PD; Commons/archive.org) — **why / lead:** No facsimile of Victoria's 10 Feb 1840 journal page found with clear rights. Lead: archive.org 'girlhoodofqueenv01victuoft' (1912, NOT_IN_COPYRIGHT) - printed text pages of the diaries; RCT facsimile not allowed.
- **S021A** 01:28.18–01:30.53 — need: Victoria writing / Victoria at desk engraving (PD) — **why / lead:** No clear-rights 'Victoria writing' image found. Lead: Commons category 'Queen Victoria' paintings (e.g. Victoria at desk by Sir George Hayter / Tuxen) - search Commons 'Queen Victoria writing'.
- **S021B** 01:30.53–01:32.88 — need: journal page close-up — **why / lead:** Close-up of a journal page: use S028A/S112A style page scans from archive.org ('girlhoodofqueenv01victuoft' pages with diary text) - not yet cut.
- **S022B** 01:35.94–01:39.00 — need: wedding procession engraving 1840 (PD, ILN/Met) — **why / lead:** Lead: archive.org 'A complete narrative of the celebration of the nuptials of Her Most Gracious Majesty Queen Victoria' (PD, 1840) - procession plates; also ILN 1840 on archive.org. Not downloaded.
- **S067A** 04:51.44–04:56.08 — need: Dagmar Necklace — ILN 1863 engraving or Danish archive drawing (PD); f — **why / lead:** No ILN 1863 engraving of the Dagmar necklace found. Lead: archive.org Illustrated London News vol. 42 (1863) and Met plate S065B (parure of the Prince of Wales - NOT Dagmar).
- **S077A** 05:40.34–05:45.42 — need: 1968 book cover? (copyrighted — DON'T) → GFX: card "Young, 1968 — book — **why / lead:** By brief: GFX card only (book cover is copyrighted) - not a search shot.
- **S084A** 06:17.50–06:22.14 — need: Alexandra & Edward silver wedding 1888 photo/engraving (PD) + GFX "25  — **why / lead:** No clear 1888 silver wedding image. Lead: Commons 'Queen Alexandra' 1888 prints (BM). S009A already uses BM 1902,1011.10420.
- **S085A** 06:22.14–06:25.42 — need: group of Victorian society ladies in court dress, photo 1880s (PD) — **why / lead:** Lead: Judge magazine 2 Jul 1887 (Commons, PD) - Victorian caricature, not a court-dress photo. No photo with clear rights found.
- **S088A** 06:38.20–06:42.06 — need: Russian woman in traditional kokoshnik headdress, Prokudin-Gorsky (LOC — **why / lead:** LOC Prokudin-Gorskii search returned Armenian/Georgian/Bashkir women, none in a Russian kokoshnik. Lead: loc.gov/collections/prokudin-gorskii - browse 'peasant girls' items manually.
- **S103A** 07:49.46–07:54.18 — need: St Petersburg 1870s view / wedding 1874 (PD) — **why / lead:** No wedding-1874 / St Petersburg 1870s image beyond S082B. Lead: Commons category 'Saint Petersburg in the 1870s'.
- **S113A** 08:32.32–08:34.85 — need: Petrograd 1917 railway station photo (PD) — **why / lead:** No Petrograd railway station photo found. Lead: LOC Bain collection 'Petrograd' 1917; Commons 'Nikolaevsky station 1917'.
- **S121A** 09:06.70–09:09.86 — need: **[JEWEL]** rights-clear photo of Elizabeth II in Vladimir with emeral — **why / lead:** JEWEL: no rights-clear photo of Elizabeth II in the Vladimir tiara with emeralds found. Lead: Nationaal Archief 1958 state-visit photos (S189A candidates 909-4441/4460) - check whether the tiara is the Vladimir; LAC 1959 portrait is the version with pearls.
- **S143B** 10:44.89–10:48.44 — need: **[JEWEL]** Catherine in the Lover's Knot — rights-clear (Commons CC / — **why / lead:** JEWEL: no rights-clear photo of Catherine in the Lover's Knot found. Lead: Commons 'Catherine, Princess of Wales' diplomatic reception 2015+ (tiara worn 2015-2019); only CC licences count.
- **S153B** 11:28.55–11:31.34 — need: Queen Mary 1910 photo (PD) — **why / lead:** No Queen Mary 1910 photo found. Lead: Commons 'Duchess of York, 1898' (No restrictions) shows Mary of Teck, but 12 years early.
- **S169A** 12:48.18–12:52.58 — need: Queen Elizabeth (consort) 1940s photo (PD gov/archive, verify) + GFX " — **why / lead:** No rights-clear 1940s photo of Queen Elizabeth (consort). Lead: UK National Archives INF3-78 (S209B), Universal Newsreel 1939 tour (VIDEO_LEADS.md).
- **S179A** 13:32.02–13:37.14 — need: Asscher cleaving the Cullinan 1908 photo (PD) — **why / lead:** No rights-clear photo of Asscher cleaving the Cullinan 1908 found. Lead: Commons category 'Cullinan Diamond'; Asscher Museum / Rijksmuseum (check CC0) .
- **S180A** 13:37.14–13:39.21 — need: Asscher workshop 1908 photo (PD) — **why / lead:** Same as S179A - Asscher workshop 1908 photo not found.
- **S186A** 14:03.96–14:06.46 — need: Queen Mary wearing the Cullinan III&IV brooch (PD photo, verify) — **why / lead:** JEWEL: no PD photo of Queen Mary wearing the Cullinan III/IV brooch found. Lead: S182A candidates (LOC 2014716428, Autochrome 1914) - check visually after download.
- **S187A** 14:06.46–14:12.72 — need: Queen Mary in Delhi Durbar tiara with Cullinan (PD) — **why / lead:** JEWEL: no photo of Mary in the Delhi Durbar tiara with Cullinan found. Lead: S168A candidate; Commons category 'Delhi Durbar tiara'.
- **S210A** 15:54.44–15:59.14 — need: Queen Elizabeth consort portrait (PD gov) — **why / lead:** No rights-clear portrait of Queen Elizabeth (consort) 1940s beyond S209B. Lead: Commons 'Queen Elizabeth The Queen Mother' US Gov / Canadian archives 1939.
- **S213A** 16:09.84–16:13.58 — need: Queen Mother later photo rights-clear (gov/CC, verify) — **why / lead:** No rights-clear later photo of the Queen Mother found. Lead: Commons 'Queen Elizabeth The Queen Mother' 1980s-90s (US gov: DoD/NARA) - not located.
- **S216A** 16:20.56–16:25.94 — need: **[JEWEL]** 2011 Turkey state banquet photo with Greville earrings + C — **why / lead:** JEWEL: 2011 Turkey state banquet photo not found with clear rights (the only banquet photo found is 1954). Lead: Turkish Presidency press photos (check licence) / Royal Collection (not allowed).
- **S235A** 17:51.34–17:53.67 — need: Queen Mother in later years rights-clear — **why / lead:** Queen Mother in later years: only 1958 Queensland State Archives photos (S234A) found. Lead: Commons 'Queen Elizabeth The Queen Mother' 1990s-2002.
- **S246A** 18:40.90–18:44.20 — need: **[JEWEL]** Queen Mary in Fringe tiara (PD) — reveal — **why / lead:** JEWEL: no PD photo of Queen Mary in the Fringe tiara confirmed. Lead: S153B/S222A candidate 'Queen Mary of Teck (8543179876)' CC BY 2.0 - check which tiara; Commons 'Queen Mary' portraits 1930s.

## 6. Decisions I made that you may want to know

- **S003A/alt1**: Checked visually: tiara has floral/fleur spikes - NOT a Kokoshnik, NOT Lover's Knot, NOT Fringe; do not use for S096A/S137A/S222A. Generic Queen Mary in tiara + Garter star. | No known restrictions on publication. For more information, see George Grantham Bain Collection - Ri
- **S046A/main**: Checked visually: gold Lesser George badge with Garter motto, 18th c. Generic Order of the Garter illustration, NOT one of Victoria's own badges. Acceptable for "Garter badges" beat only as generic. | proof = Met API record
- **S065B/main**: Checked visually: plate "Parure of Diamonds and Pearls - the gift of H.R.H. The Prince of Wales" (tiara, necklace, brooch, earrings). A wedding present, but NOT the Dagmar Necklace (that was from Frederik VII) - do not use on S067A/S068A. Does not show the wedding itself (S064A still open). | proof 
- **S149A/alt2**: in 00:05:20 / out 00:05:28 of source. CHECKED VISUALLY: Kinemacolor 1912 procession with elephants (not the royal couple, not an amphitheatre view). WARNING: burned-in 'Cineteca Bologna' logo top-left from 3:40 onward in this source - crop it out or choose another source. Film itself: Public Domain 
