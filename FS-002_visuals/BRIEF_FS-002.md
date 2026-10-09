# ЗАДАНИЕ: поиск визуала для ролика FS-002 (FATESET)

Ты работаешь как исследователь изображений для документального YouTube-ролика (английский, коммерческий канал с монетизацией).
Ролик: **"10 Royal Jewels Elizabeth II Inherited — and the Women Who Wore Them First"**, 19:45.
Ниже 175 кадров с таймкодами и фразой диктора. Для каждого найди изображение, которое **можно законно использовать в коммерческом YouTube-видео**, и **точно соответствует тому, что говорит диктор**.

## 0. Перед стартом
- Твоя задача только **найти, проверить права и сложить** материалы с документами по лицензии. Видео не монтируй: ролик соберут позже из твоей папки.
- Ищи только в архивах из раздела 3. Если не ясно, разрешено ли коммерческое использование в монетизированном YouTube-ролике, файл **отклоняй**.
- Сессию запускай в окружении **FATEST** (в других окружениях архивы закрыты сетью).
- Сначала проверь доступ: `curl -sI https://upload.wikimedia.org`, `https://www.loc.gov`, `https://collectionapi.metmuseum.org`, `https://www.nationaalarchief.nl`, `https://web.archive.org`.

## 0a. Темп и количество (замер ролика конкурента, проверен вручную)
- Конкурент: 22:42. Ручной подсчёт трёх минут (2:00–3:00, 10:00–11:00, 18:00–19:00): 15 + 16 + 18 = 49 кадров за 180 с, **≈3.7 с на кадр**, то есть **~370 кадров** на весь ролик. Темп ровный, без провалов в середине. Фото и картины идут с медленным наездом, наезд считается одним кадром. **Видео ≈12%** (6 из 49).
- Наш ролик: 19:45, в плане **323 кадра = 3.7 с на кадр**, то есть ровно темп конкурента.
- На **каждый** кадр ищи **основной вариант + 2 запасных** (другой ракурс, другое фото того же события или человека, деталь). Запасные нужны на случай отказа по правам или если кадр не подойдёт на монтаже. Они проходят ту же проверку прав и смысла.
- **Видео:** где фраза про событие (коронации 1902/1911/1937/1953, Delhi Durbar 1911, свадьбы 1923/1947, процессии, визит 1958 в Амстердам, Russia 1917, шахта Premier/Cullinan, Лондон в войну), ищи также видеоклип 3–10 с. Цель: **~40 клипов** на ролик. Источники видео с чистыми правами: NARA (Universal Newsreel, US gov — PD), archive.org (PD-фильмы, Prelinger), Open Beelden / Beeld en Geluid (Polygoon, CC BY-SA), Nationaal Archief, LOC (Paper Print, PD), Europeana (фильтр по лицензии). **British Pathé, Reuters, AP, BFI** — только по лицензии, без неё не брать.
- Каждый вариант должен соответствовать **смыслу фразы диктора в его таймкоде**. Красивый, но не по смыслу кадр не годится.

## 1. Правила прав (обязательно)
Допустимые статусы — только эти:
`PUBLIC_DOMAIN_VERIFIED`, `CC0_VERIFIED`, `CC_BY_VERIFIED` (или CC BY-SA, условия записать), `LICENSED — PROOF SAVED`.
Запрещено брать в работу: `UNKNOWN`, «rights review required», «editorial use only», «permission needed», любое изображение из Google Images, Pinterest, YouTube, сайтов СМИ, Getty/Alamy/Shutterstock/AP/PA/Reuters без лицензии, **Royal Collection Trust (rct.uk) — их фото несвободны**. Портрет коронации 1953 (Cecil Beaton) — не брать.
- Лицензию проверяй **на странице конкретного файла**, не по коллекции целиком.
- CC BY-NC и CC BY-ND — **не подходят** (коммерция / нужны обрезка и движение).
- Фото PD-картин (старые картины) — ок как PD-Art, если на файле так указано.
- Нельзя: брать несвободный файл и «очищать» его кропом, ретушью, AI-перерисовкой.
- Если чистого изображения нет — так и пиши `NOT FOUND`, приложи лучшие leads (ссылки) с причиной. Не подставляй сомнительное.

## 2. Правило соответствия
- Тот же человек, тот же предмет, та же эпоха, что в фразе. Если фраза про Queen Mary в Lover's Knot tiara — нужна Mary именно в этой тиаре (сверить глазами по описанию тиары: ромбовидные банты-узлы с 19 подвесными жемчужинами).
- **[JEWEL]** = реальная драгоценность в кадре. Обязательно глазами сверить, что на фото именно этот предмет. Если не уверен — отметь `VERIFY` и объясни.
- **Не показывать Fringe Tiara и свадьбу 1947 года до главы 10** (S219+): это ответ на главный вопрос ролика.
- Один и тот же файл на разные кадры — нельзя (кроме кропа одной большой картины на разные детали: тогда разные кропы, это ок, но отметь).

## 3. Где искать (по приоритету)
1. **Wikimedia Commons** — смотри лицензию на странице файла. API `commons.wikimedia.org/w/api.php` часто отвечает 429: делай паузы 5–20 с, повторяй, или работай через HTML-страницы `commons.wikimedia.org/wiki/File:...` и прямые ссылки `upload.wikimedia.org`.
2. **Library of Congress** (loc.gov, Bain Collection, Prokudin-Gorsky) — «No known restrictions».
3. **Nationaal Archief (NL) / Anefo** — CC0: королевские визиты 1947, 1958 (визит Елизаветы II в Нидерланды и Амстердам 1958 — важно для S188–S189).
4. **Library and Archives Canada** — портрет Елизаветы II 1959 в Vladimir tiara (PD-Canada-Crown, проверить).
5. **US Government** (NARA, White House, DoD, State Dept) — работы федеральных служащих = PD. Государственные визиты: 1957, 1976, 1983, 1991, 2007; Диана 1985. Сверяй, какие драгоценности на фото.
6. **Met Museum** Open Access (CC0, API `collectionapi.metmuseum.org/public/collection/v1.1/search`), **Rijksmuseum**, **Smithsonian** (CC0), **Cleveland**, **Art Institute of Chicago**, **V&A**, **Europeana**, **DPLA**, **Flickr Commons** (no known restrictions).
7. **archive.org** — PD книги и журналы (Illustrated London News 1863/1888/1911, дневник Stopford 1919 «The Russian Diary of an Englishman», журналы Виктории 1912). rct.uk закрыт Cloudflare — только через `web.archive.org`.
8. Parliamentary Art Collection / Government Art Collection / National Trust Collections — PD-картины (Winterhalter 1859, Fildes 1905, Carolus-Duran 1891).

Известные зацепки из Blueprint (проверить лицензии!): Hayter «Marriage of Queen Victoria» (Met CC0); Winterhalter 1859 Victoria; Fildes Alexandra; Maria Pavlovna «in court dress» (PD); LAC 1959 (Vladimir); Nationaal Archief 1947 и 1958; Commons «Elizabeth_II_2012» (CC BY 2.0, брошь сверить), «Queen_Elizabeth_II_1963» (CC BY 2.0, ожерелье сверить), «Queen_Elizabeth_II_and_Prince_Philip,_1957» (тиару сверить), «Queen_Elizabeth_II.JPG» 5.06.2012 (CC BY-SA). NARA 1976/1983 с серьгами Гревилл — **не подходят** (серьги тогда были не у неё).

## 4. Формат результата
Создай папку `FS-002_visuals/`:
- файлы в максимальном доступном разрешении, имя = `<Shot>_<rank>__<short-slug>.<ext>`, например `S017A_main__elizabeth-sapphire-brooch-2012.jpg`, `S017A_alt1__...`;
- `MANIFEST.csv` со столбцами:
  `shot,rank,media,status,file,title,creator,date,collection,item_id,source_page_url,direct_file_url,licence,commercial_use,derivatives_ok,required_credit,accessed,verify_note`
  (`rank` = main / alt1 / alt2; `media` = image / video; для видео добавь in/out секунды фрагмента в `verify_note`; `status` = один из допустимых статусов, или `NOT FOUND`, или `VERIFY`);
- `proof/` — для каждого файла скриншот или сохранённый HTML страницы с лицензией (`<Shot>__proof.png` или `.html`);
- `REPORT.md` — сводка: сколько найдено / NOT FOUND / VERIFY, проблемные кадры, лучшие leads.
В конце упакуй всё в `FS-002_visuals.zip`, чтобы Max мог скачать и положить в Obsidian: `04 — Production/Ролики/FS-002 — elizabeth-ii-inherited-jewels/09 — VISUALS/`.

Работай по главам, сохраняй прогресс (MANIFEST дописывай после каждого кадра), не останавливайся на вопросы — сомнительное помечай `VERIFY`.

AI-кадры (тип AI) и графика (GFX) в этот список не входят — их делают отдельно.

## 5. Кадры (175)

| Shot | In–Out | Диктор говорит | Что найти |
|---|---|---|---|
| S001A | 00:00.00–00:02.37 | Some of the finest jewels Queen Elizabeth the Second ever wore did not come from | **[JEWEL]** Queen Elizabeth II in a tiara and jewels, any rights-clear photo 1950s–2010s (NOT Fringe Tiara, NOT 1953 coronation portrait) |
| S002A | 00:04.74–00:07.29 | kings. One pair of earrings had belonged to a brewer's daughter. | Margaret Greville portrait (Carolus-Duran 1891, National Trust, PD) |
| S002B | 00:07.29–00:09.84 | kings. One pair of earrings had belonged to a brewer's daughter. | William McEwan portrait or McEwan's brewery / 19th-c. Edinburgh brewery engraving |
| S003A | 00:09.84–00:13.84 | A tiara was sold to her grandmother by a Russian grand duchess's daughter, | Queen Mary portrait in a tiara (LOC Bain / PD, c.1910s–1920s) |
| S004A | 00:13.84–00:17.04 | four years after the revolution. | Russian Revolution 1917 street photo, Petrograd (PD) |
| S005A | 00:17.04–00:19.75 | Only two came with the Crown. The rest came the way jewels come in any family: | **[JEWEL]** Imperial State Crown / Crown regalia PD image (Tower of London regalia engraving or PD photo) |
| S007A | 00:25.54–00:29.24 | A brooch given the day before a wedding, 1840. | Hayter "Marriage of Queen Victoria" 1840 (Met CC0 engraving) + GFX date 1840 |
| S009A | 00:34.54–00:37.29 | 1947. A gift from three hundred and sixty-five women, | Alexandra, Princess of Wales, photo c.1888 (PD) |
| S015A | 01:04.28–01:06.95 | The first woman to wear it was Queen Victoria, and she wore it to her own wedding. | young Queen Victoria portrait c.1840 (PD, e.g. Winterhalter/Partridge) |
| S015B | 01:06.95–01:09.62 | The first woman to wear it was Queen Victoria, and she wore it to her own wedding. | Hayter wedding painting detail |
| S017A | 01:14.02–01:18.60 | Albert gave her this brooch: a sapphire set with diamonds. | **[JEWEL]** Albert's sapphire brooch — rights-clear photo of Elizabeth II wearing it (Commons "Elizabeth_II_2012" CC BY 2.0 candidate, verify brooch) ; fallback AI close-up of a large oval sapphire with diamond surround on velvet (non-distorting, generic) |
| S019A | 01:23.06–01:25.48 | and worn on the wedding day itself. | Hayter "Marriage of Queen Victoria" detail of the bride (Met CC0) |
| S020A | 01:25.48–01:28.18 | We don't have to guess whether she wore it. | Queen Victoria's journal page facsimile (PD; Commons/archive.org) |
| S021A | 01:28.18–01:30.53 | She wrote it down. In her journal for February tenth, describing what she wore | Victoria writing / Victoria at desk engraving (PD) |
| S021B | 01:30.53–01:32.88 | She wrote it down. In her journal for February tenth, describing what she wore | journal page close-up |
| S022B | 01:35.94–01:39.00 | to marry him, Victoria noted, "Albert's beautiful sapphire brooch." | wedding procession engraving 1840 (PD, ILN/Met) |
| S024A | 01:43.70–01:47.78 | it stayed close to her. In the Royal Collection's words, | Queen Victoria portrait 1840s with brooch at bodice (PD painting) |
| S025A | 01:47.78–01:51.10 | it remained a favorite piece of jewelry. | Victoria and Albert together, 1840s–50s photo/painting (PD) |
| S026A | 01:51.10–01:53.48 | Albert died in 1861. When Victoria settled what would happen to | Albert death 1861 — mourning engraving / Blue Room (PD) |
| S026B | 01:53.48–01:55.86 | Albert died in 1861. When Victoria settled what would happen to | Victoria in widow's weeds photo 1860s (PD) |
| S027A | 01:55.86–01:59.82 | her jewels, she did not leave this brooch to a person. | older Queen Victoria photo 1880s–90s (PD) |
| S028A | 01:59.82–02:02.65 | A note in the 1912 edition of her journals says she left it to the Crown. | title page of "Letters/Journals of Queen Victoria" 1912 edition (archive.org PD) |
| S029A | 02:05.48–02:08.94 | That meant it would belong to whoever was sovereign. | Imperial State Crown / regalia PD image |
| S030A | 02:08.94–02:12.78 | In February 1952, that became Elizabeth. | Elizabeth II accession 1952 — rights-clear photo or newspaper front page Feb 1952 (PD check) ; GFX "February 1952" |
| S031A | 02:12.78–02:15.66 | She inherited this brooch not from a grandmother, but with the Crown itself, | **[JEWEL]** Elizabeth II wearing the sapphire brooch (same source as beat 17, different crop) |
| S033A | 02:22.28–02:25.18 | Victoria's first jewel on this list came to her through love. | Victoria & Albert portrait (PD) warm grade |
| S036A | 02:33.24–02:38.16 | Its name suggests Victoria wore it when she was crowned in 1838. | Victoria's coronation 1838 painting (Hayter coronation, PD) + GFX 1838 |
| S038A | 02:41.40–02:45.10 | Some of Victoria's jewels had once belonged to Queen Charlotte. | Queen Charlotte portrait (Gainsborough/Ramsay, PD) |
| S039A | 02:45.10–02:47.47 | The King of Hanover claimed them as his. A commission investigated the claim, | Ernest Augustus, King of Hanover portrait (PD) |
| S041A | 02:54.54–02:58.06 | great dismay, it ruled against her. | Victoria portrait 1850s (PD), slow push |
| S044A | 03:10.32–03:15.16 | To replace Charlotte's necklace, Garrard made a new one in 1858, | Garrard / 19th-c. jeweller's shop engraving (PD) + GFX "Garrard 1858" |
| S046A | 03:19.88–03:24.36 | two of Victoria's Garter badges and a sword hilt. | Order of the Garter badge/star 19th c. (Met/V&A CC0 if available) ; sword hilt with diamonds PD museum image |
| S048A | 03:28.24–03:33.66 | From the center hangs the Lahore Diamond, twenty-two point four eight carats. | **[JEWEL]** Coronation Necklace pendant — Elizabeth II wearing it (Commons "Queen_Elizabeth_II_1963" CC BY 2.0 candidate, verify) + GFX "Lahore Diamond 22.48 ct" |
| S049A | 03:33.66–03:36.47 | The matching earrings were made from stones that once sat beside the Koh-i-Noor in its Indian setting. | Koh-i-Noor 19th-c. engraving (PD) |
| S049B | 03:36.47–03:39.28 | The matching earrings were made from stones that once sat beside the Koh-i-Noor in its Indian setting. | Ranjit Singh / Lahore court painting (PD, Met/V&A CC0) |
| S051A | 03:43.84–03:48.20 | Victoria was slightly under five feet tall. In her long widowhood, | Victoria photo full figure 1860s–80s (PD) showing small stature |
| S052A | 03:48.20–03:52.92 | this necklace was among the relatively few jewels she allowed herself to wear. | Victoria in widowhood with necklace, photo 1880s–90s (PD) |
| S053A | 03:52.92–03:57.76 | In 1859, Franz Xaver Winterhalter painted her in this necklace and | Winterhalter 1859 portrait of Victoria (Parliamentary Art Collection, PD) full |
| S054A | 03:57.76–04:01.80 | these earrings. The earrings end in two diamond drops, | same Winterhalter, close crop on earrings/necklace |
| S056A | 04:04.64–04:07.62 | Then it found the purpose its name promises. It was worn at the coronations of nineteen oh two, | coronation of Edward VII 1902 photo (PD) |
| S056B | 04:07.62–04:10.60 | Then it found the purpose its name promises. It was worn at the coronations of nineteen oh two, | Queen Alexandra coronation portrait 1902 (PD) |
| S057A | 04:10.60–04:13.32 | 1911 and 1937. In 1953, | coronation 1911 George V & Mary (PD) ; coronation 1937 photo (check rights) |
| S058A | 04:16.04–04:19.98 | Elizabeth wore it at her own. By published accounts, | **[JEWEL]** Elizabeth II 1953 coronation-day image that is rights-clear (NOT Beaton portrait): newsreel still/PD gov photo; fallback GFX + AI abbey interior |
| S061A | 04:27.86–04:30.28 | Victoria lost jewels to a ruling. The next woman on this list received hers as | Victoria portrait (PD) dim → transition |
| S061B | 04:30.28–04:32.70 | Victoria lost jewels to a ruling. The next woman on this list received hers as | Copenhagen 1860s view (PD) |
| S064A | 04:38.66–04:43.46 | In 1863, a Danish princess named Alexandra married | wedding of Albert Edward & Alexandra 1863, Frith painting / ILN engraving (PD) |
| S065A | 04:43.46–04:45.58 | the Prince of Wales. Among her wedding gifts was this necklace, | Alexandra in wedding dress 1863 photo (PD) |
| S065B | 04:45.58–04:47.70 | the Prince of Wales. Among her wedding gifts was this necklace, | ILN engraving of wedding presents 1863 if available |
| S066A | 04:47.70–04:51.44 | from King Frederik the Seventh of Denmark. | King Frederik VII of Denmark portrait (PD) |
| S067A | 04:51.44–04:56.08 | It was more than diamonds and pearls. At its center hung a replica of a | Dagmar Necklace — ILN 1863 engraving or Danish archive drawing (PD); fallback AI diamond-and-pearl necklace with central cross, non-distorting |
| S068A | 04:56.08–05:00.94 | famous twelfth-century enameled cross, a cross buried with Dagmar, | Dagmar Cross original (National Museum of Denmark, check CC licence) |
| S069A | 05:00.94–05:03.95 | Queen of Denmark, in twelve twelve. That is where the necklace gets its name. | Ringsted church / Queen Dagmar tomb (Commons CC) |
| S069B | 05:03.95–05:06.96 | Queen of Denmark, in twelve twelve. That is where the necklace gets its name. | Queen Dagmar medieval depiction (PD) |
| S070A | 05:06.96–05:10.40 | King Frederik suggested something stranger still. | Frederik VII portrait alt crop |
| S072A | 05:15.02–05:19.08 | and a scrap of silk from the grave of King Canute. | King Canute medieval manuscript illustration (PD, BL/Commons) |
| S073A | 05:19.08–05:21.89 | So the Danish king's wedding gift held a piece of Denmark's medieval past. | medieval Danish church interior (Commons CC) |
| S074A | 05:24.70–05:29.30 | Decades later, Luke Fildes painted Alexandra's coronation portrait. | Luke Fildes portrait of Queen Alexandra 1905 (Government Art Collection, PD) |
| S075A | 05:29.30–05:32.46 | Among the jewels massed on her dress, slightly adapted, is the Dagmar Necklace. | Fildes portrait close crop on jewels at bodice |
| S075B | 05:32.46–05:35.62 | Among the jewels massed on her dress, slightly adapted, is the Dagmar Necklace. | Fildes portrait full |
| S077A | 05:40.34–05:45.42 | spell out the route. A 1968 book on the Queen's jewelry says | 1968 book cover? (copyrighted — DON'T) → GFX: card "Young, 1968 — book on the Queen's jewelry" with neutral book icon |
| S078A | 05:45.42–05:50.22 | Elizabeth inherited it from her grandmother, Queen Mary, which would place it with her in | Queen Mary portrait (PD) + GFX "1953" |
| S081A | 06:00.14–06:05.30 | Alexandra's Danish necklace was a king's gift. Her next jewel on this list came twenty-five years | Alexandra portrait c.1880s (PD) |
| S082A | 06:05.30–06:08.83 | later, and it was Russian in style, the style of the country her sister had married into. | Empress Maria Feodorovna portrait (PD) |
| S082B | 06:08.83–06:12.36 | later, and it was Russian in style, the style of the country her sister had married into. | St Petersburg 1880s view (PD) |
| S084A | 06:17.50–06:22.14 | In 1888, Alexandra had been married for twenty-five years. | Alexandra & Edward silver wedding 1888 photo/engraving (PD) + GFX "25 years" |
| S085A | 06:22.14–06:25.42 | To mark it, a group the Royal Collection calls the Ladies of Society, | group of Victorian society ladies in court dress, photo 1880s (PD) |
| S087A | 06:33.00–06:38.20 | Garrard made it, at a cost of four thousand four hundred pounds: sixty-one bars | Garrard shop / 1880s jeweller (PD) + GFX "£4,400 · 61 bars" |
| S088A | 06:38.20–06:42.06 | of diamonds, standing upright like the traditional Russian headdress, | Russian woman in traditional kokoshnik headdress, Prokudin-Gorsky (LOC, PD) |
| S089A | 06:42.06–06:46.66 | the kokoshnik. It can also be worn as a necklace. | **[JEWEL]** Kokoshnik tiara — Elizabeth II wearing it (Commons 1957 candidate, verify; US gov White House photos PD if she wore it) ; fallback AI tall diamond-bar tiara silhouette, non-distorting |
| S090A | 06:46.66–06:49.71 | The Russian shape had a family meaning. Alexandra's sister was Empress Maria | Alexandra and Maria Feodorovna sisters photo (PD) |
| S090B | 06:49.71–06:52.76 | The Russian shape had a family meaning. Alexandra's sister was Empress Maria | Maria Feodorovna coronation portrait (PD) |
| S091A | 06:52.76–06:56.04 | Feodorovna, wife of Tsar Alexander the Third. | Tsar Alexander III portrait (PD) |
| S092A | 06:56.04–06:59.96 | Alexandra wore it often. One occasion stands out. | Alexandra in tiara photo 1890s (PD) |
| S093A | 06:59.96–07:04.76 | In 1893, she wore it to the marriage of the Duke of York to Princess Victoria | wedding of Duke of York and Princess May 1893 painting/photo (PD) |
| S094A | 07:04.76–07:08.02 | Mary of Teck. The bride that day would one day own this tiara. | Princess May of Teck 1893 photo (PD) |
| S095A | 07:11.28–07:15.60 | After Alexandra's death in 1925, it passed to that bride, | Queen Alexandra late photo / funeral 1925 (PD) |
| S096A | 07:15.60–07:20.00 | by then Queen Mary, who also wore it frequently. | Queen Mary wearing kokoshnik tiara, photo 1920s–30s (LOC Bain/PD, verify tiara) |
| S097A | 07:20.00–07:22.93 | And in 1953, Mary bequeathed it to her granddaughter, Elizabeth. | Queen Mary late portrait (PD) |
| S099A | 07:28.86–07:31.80 | The next one was Russian by birth, and it lived through a revolution. | Russia 1917 revolution crowd photo (PD) |
| S099B | 07:31.80–07:34.74 | The next one was Russian by birth, and it lived through a revolution. | Winter Palace 1917 (PD) |
| S101A | 07:38.74–07:43.80 | The first woman to wear it was a Russian grand duchess, Maria Pavlovna, | Grand Duchess Maria Pavlovna "in court dress" (PD) |
| S102A | 07:43.80–07:46.63 | wife of Grand Duke Vladimir. It was made for her around 1874, | Grand Duke Vladimir Alexandrovich portrait (PD) |
| S103A | 07:49.46–07:54.18 | probably at the time of her marriage, and almost certainly, the Royal Collection says, | St Petersburg 1870s view / wedding 1874 (PD) |
| S105A | 07:57.56–08:01.40 | Intersecting circles of diamonds, each hung with a pearl. | **[JEWEL]** Vladimir tiara — LAC 1959 portrait of Elizabeth II (PD-Canada-Crown, verify) |
| S108A | 08:07.04–08:09.43 | One night in September that year, at her house in Kislovodsk, a committee of | Kislovodsk pre-1917 photo / postcard (PD) |
| S111A | 08:20.84–08:24.27 | We know this because she wrote to a British friend, Albert Stopford, and he recorded what she wrote in his diary. | Albert Stopford portrait if PD; else archive.org page of "The Russian Diary of an Englishman" 1919 (PD) |
| S111B | 08:24.27–08:27.70 | We know this because she wrote to a British friend, Albert Stopford, and he recorded what she wrote in his diary. | diary page close-up |
| S112A | 08:27.70–08:32.32 | His published diary records her letter. It does not record what Sotheby's | archive.org diary page crop with letter passage |
| S113A | 08:32.32–08:34.85 | would later say he did: that he left Petrograd that month carrying her jewels, | Petrograd 1917 railway station photo (PD) |
| S115A | 08:40.68–08:44.02 | On that, the diary is silent. | diary closed / page blank margin crop; GFX "silent" |
| S117A | 08:48.24–08:52.14 | In 1921, her daughter, Princess Nicholas of Greece, | Princess Nicholas of Greece (Grand Duchess Elena Vladimirovna) portrait (PD) |
| S118A | 08:52.14–08:55.04 | sold it to Queen Mary. Elizabeth inherited it in 1953. | Queen Mary 1920s photo (PD) + GFX "1921" |
| S119A | 08:57.94–09:03.14 | In her official portrait for her 1959 tour, she is wearing it. | **[JEWEL]** LAC 1959 tour portrait (PD) full frame |
| S121A | 09:06.70–09:09.86 | with its original pearls, with nothing hanging at all, and with pendant emeralds. | **[JEWEL]** rights-clear photo of Elizabeth II in Vladimir with emeralds (US gov / Dutch NA candidates, verify) |
| S121B | 09:09.86–09:13.02 | with its original pearls, with nothing hanging at all, and with pendant emeralds. | **[JEWEL]** with pearls (LAC 1959) |
| S122A | 09:13.02–09:17.74 | By published accounts, those emeralds came from Queen Mary's Cambridge emeralds, | Duchess of Cambridge (Augusta) portrait (PD) + GFX "Cambridge emeralds" |
| S127B | 09:34.91–09:37.22 | A house searched in the middle of the night. None of the women who first wore these | five first-wearer portraits side by side |
| S128A | 09:37.22–09:40.04 | five chose Elizabeth as her heir. | young Elizabeth II portrait rights-clear (PD gov) |
| S132A | 09:55.32–09:59.84 | According to published histories of the collection, on the eve of the First World War, | 1914 London street / eve of WWI photo (PD) |
| S133A | 09:59.84–10:04.50 | Queen Mary had Garrard make a tiara modeled on the Cambridge Lover's Knot tiara that | Garrard / jeweller (PD) + GFX "Lover's Knot" |
| S134A | 10:04.50–10:09.16 | had belonged to her own grandmother, Princess Augusta, Duchess of Cambridge. | Princess Augusta, Duchess of Cambridge portrait (PD) |
| S137A | 10:15.72–10:20.62 | It was a copy of a family piece. The same histories say Elizabeth inherited | Queen Mary in the Lover's Knot tiara (LOC Bain/PD, verify tiara) |
| S139A | 10:23.48–10:28.20 | Then it left her hands. Royal jewelry historians record that in 1981 | 1981 — St Paul's Cathedral exterior (CC) + GFX "1981" |
| S140A | 10:28.20–10:32.04 | it went to the new Princess of Wales. | Diana, Princess of Wales rights-clear photo (US gov PD — e.g. White House 1985 photos; verify tiara) |
| S141A | 10:32.04–10:34.69 | Diana did not wear it to her wedding. She married in her own family's Spencer tiara. | Spencer family / Althorp (CC) ; NO wedding agency photos |
| S142A | 10:37.34–10:41.34 | But she wore this one often. According to press accounts, | **[JEWEL]** Diana wearing Lover's Knot — US gov PD photo (White House/DoD 1985 visit; verify) |
| S143A | 10:41.34–10:44.89 | after her divorce, it came back to the Queen. Since twenty fifteen, it has been worn by Catherine. | Buckingham Palace (CC) |
| S143B | 10:44.89–10:48.44 | after her divorce, it came back to the Queen. Since twenty fifteen, it has been worn by Catherine. | **[JEWEL]** Catherine in the Lover's Knot — rights-clear (Commons CC / gov PD, verify) |
| S145A | 10:53.40–10:58.10 | The next jewel also began with Mary's grandmother, and with a will the public | Duchess of Cambridge (Augusta) portrait again (different crop) |
| S148A | 11:05.06–11:09.74 | On December twelfth, 1911, George the Fifth and Queen Mary | George V and Queen Mary at Delhi Durbar 1911 (PD) |
| S149A | 11:09.74–11:11.66 | appeared at the Delhi Durbar. For the occasion, | Delhi Durbar 1911 crowd/amphitheatre (PD) |
| S150A | 11:13.58–11:19.06 | Garrard made Mary a suite of jewels. This necklace is part of it. | Queen Mary in Durbar jewels 1911–12 photo (PD) |
| S152A | 11:22.00–11:25.76 | The Royal Collection records that they had belonged to Mary's grandmother, | Duchess of Cambridge portrait (PD) |
| S153B | 11:28.55–11:31.34 | the Duchess of Cambridge, and that Mary acquired them in 1910. | Queen Mary 1910 photo (PD) |
| S155A | 11:37.62–11:40.16 | The duchess, the story goes, won them in a lottery in Frankfurt. | Frankfurt 19th-c. view (PD) |
| S156A | 11:42.70–11:45.40 | They passed to Mary's mother, and then to Mary's brother, Prince Francis of Teck. | Princess Mary Adelaide, Duchess of Teck portrait (PD) |
| S156B | 11:45.40–11:48.10 | They passed to Mary's mother, and then to Mary's brother, Prince Francis of Teck. | Prince Francis of Teck photo (PD) |
| S157A | 11:48.10–11:53.04 | Francis died in 1910, at forty. And something unusual happened | Prince Francis of Teck photo (PD) + GFX "1870–1910" |
| S158A | 11:53.04–11:57.88 | to his will. In twenty twenty-one, a High Court judge ruling on | Royal Courts of Justice exterior (CC) + GFX "2021" |
| S159A | 11:57.88–12:02.06 | Prince Philip's will explained the custom of sealing royal wills, | Prince Philip rights-clear photo (gov PD) |
| S164A | 12:24.60–12:28.40 | Hanging off-center from the necklace is an eight point eight carat marquise diamond, | **[JEWEL]** Delhi Durbar necklace image — Queen Mary 1911–12 photo crop (PD) ; GFX "8.8 ct marquise" |
| S166A | 12:33.52–12:36.94 | That small pendant came from one diamond, and the next jewel holds two of its largest pieces. | Cullinan diamond 1905 rough photo (PD) |
| S168A | 12:43.90–12:48.18 | The necklace had a companion: the Delhi Durbar tiara. | Queen Mary in Delhi Durbar tiara (PD) |
| S169A | 12:48.18–12:52.58 | In 1946, Queen Mary lent that tiara to her daughter-in-law, | Queen Elizabeth (consort) 1940s photo (PD gov/archive, verify) + GFX "1946" |
| S170A | 12:52.58–12:56.00 | Elizabeth's mother, for a royal tour of South Africa the following year. | 1947 royal tour of South Africa photo (PD — South African/UK gov/Nationaal Archief? verify) |
| S174A | 13:10.22–13:14.82 | In nineteen oh five, at the Premier Mine near Pretoria, a diamond was found that | Premier Mine 1905 photo (PD) + GFX 1905 |
| S175A | 13:14.82–13:19.00 | weighed three thousand one hundred and six carats uncut. | Cullinan rough diamond 1905 photo with scale (PD) + GFX "3,106 ct" |
| S177A | 13:23.64–13:28.50 | other diamond yet found. The story goes that clerks at the mine first threw | mine officials / Frederick Wells with the stone (PD) |
| S179A | 13:32.02–13:37.14 | The Asscher firm in Amsterdam cut it into nine major numbered stones, | Asscher cleaving the Cullinan 1908 photo (PD) |
| S180A | 13:37.14–13:39.21 | ninety-six smaller ones, and a few uncut fragments. | Asscher workshop 1908 photo (PD) |
| S181A | 13:41.28–13:44.03 | Two of them, a ninety-four point four carat pear and a sixty-three point six carat | Cullinan cut stones plate (PD, 1908/1910 publication) |
| S182A | 13:46.78–13:51.70 | cushion, went to Queen Mary. The pear-shaped Cullinan Three was | Queen Mary photo with Cullinan brooch (PD) |
| S185A | 14:00.32–14:03.96 | In 1911 they were set into her crown. | Queen Mary's crown 1911 coronation photo (PD) |
| S186A | 14:03.96–14:06.46 | Then they were mounted together as this brooch. | Queen Mary wearing the Cullinan III&IV brooch (PD photo, verify) |
| S187A | 14:06.46–14:12.72 | Later, the Delhi Durbar tiara from the last chapter was altered so that it could carry them too. | Queen Mary in Delhi Durbar tiara with Cullinan (PD) |
| S188B | 14:15.02–14:17.32 | Elizabeth inherited it in 1953. In 1958, | Amsterdam 1958 state visit photo (Nationaal Archief CC0) |
| S189A | 14:17.32–14:22.12 | by the Asscher firm's account, she visited their works in Amsterdam and called these stones | Nationaal Archief 1958 Queen at Asscher / Amsterdam (CC0, verify) |
| S190B | 14:24.67–14:27.22 | Granny's Chips. In twenty twelve, at the service at Saint Paul's | St Paul's Cathedral 2012 (CC) |
| S191A | 14:27.22–14:31.18 | Cathedral for her Diamond Jubilee, she wore the brooch. | **[JEWEL]** Elizabeth II 2012 Diamond Jubilee with brooch — rights-clear (Commons CC/gov, verify) |
| S193A | 14:34.94–14:39.12 | The next was first worn by a brewer's daughter. | Carolus-Duran portrait of Mrs Greville (National Trust, PD) |
| S195A | 14:43.56–14:47.42 | Margaret Greville was born into money, not into a title. | Mrs Greville photo (PD) |
| S196A | 14:47.42–14:49.17 | Her father was William McEwan, a millionaire brewer. | William McEwan portrait (PD) |
| S196B | 14:49.17–14:50.92 | Her father was William McEwan, a millionaire brewer. | McEwan's brewery Fountainbridge (PD) |
| S197A | 14:50.92–14:55.24 | She married Ronald Greville in 1891. | Ronald Greville photo (PD) + GFX 1891 |
| S198A | 14:55.24–14:59.40 | Soon after she bought a country house in Surrey, Polesden Lacey, | Polesden Lacey exterior (Commons CC) |
| S199A | 14:59.40–15:04.20 | her husband died, in nineteen oh eight. They had no children. | Polesden Lacey interior (CC) + GFX 1908 |
| S200A | 15:04.20–15:09.14 | In 1923, the future King George the Sixth and his bride spent | Duke & Duchess of York 1923 wedding photo (PD) |
| S201A | 15:09.14–15:11.77 | their honeymoon at Polesden Lacey. That bride, later Queen Elizabeth the Queen Mother, | Polesden Lacey gardens (CC) |
| S201B | 15:11.77–15:14.40 | their honeymoon at Polesden Lacey. That bride, later Queen Elizabeth the Queen Mother, | Elizabeth Bowes-Lyon 1923 (PD) |
| S203B | 15:22.24–15:25.06 | unkind, so sharp, such fun, so naughty. | Mrs Greville portrait crop |
| S204A | 15:25.06–15:29.18 | In 1938, Missus Greville bought these earrings from Cartier. | Cartier Paris/London 1930s shopfront (PD/CC) + GFX 1938 |
| S207A | 15:39.10–15:41.92 | She died in 1942, in the middle of the war, at the Dorchester hotel in London. | London Blitz 1942 photo (PD) |
| S207B | 15:41.92–15:44.74 | She died in 1942, in the middle of the war, at the Dorchester hotel in London. | Dorchester hotel exterior (CC) |
| S208A | 15:44.74–15:49.36 | She left Polesden Lacey to the nation, in memory of her father. | Polesden Lacey (CC) + National Trust sign |
| S209B | 15:51.90–15:54.44 | And she left more than sixty pieces of jewelry to Queen Elizabeth, the King's consort, | Queen Elizabeth (consort) 1940s (PD) |
| S210A | 15:54.44–15:59.14 | Elizabeth's mother. Among them was a tiara Boucheron had made for her | Queen Elizabeth consort portrait (PD gov) |
| S213A | 16:09.84–16:13.58 | Her mother kept these earrings for sixty years and, | Queen Mother later photo rights-clear (gov/CC, verify) |
| S216A | 16:20.56–16:25.94 | In twenty eleven, at a state banquet for the President of Turkey, the Queen wore them. | **[JEWEL]** 2011 Turkey state banquet photo with Greville earrings + Coronation Necklace (rights-clear only, find; Turkish Presidency press photos? verify) ; fallback GFX + PD Windsor |
| S220A | 16:42.10–16:44.83 | In 1893, Queen Victoria gave Princess Victoria Mary of Teck a | Princess May 1893 photo (PD) |
| S220B | 16:44.83–16:47.56 | In 1893, Queen Victoria gave Princess Victoria Mary of Teck a | Queen Victoria 1893 photo (PD) |
| S222A | 16:52.06–16:55.78 | Mary had it made into a tiara, a fringe of diamond rays, | **[JEWEL]** Queen Mary wearing the Fringe tiara (PD photo, verify) |
| S225A | 17:03.56–17:07.94 | It is often said to be made of George the Third's diamonds. | George III portrait (PD) + GFX "often said…" |
| S227A | 17:11.92–17:15.35 | In August 1936, Mary gave the tiara to her daughter-in-law, the future Queen Elizabeth. | Elizabeth (Duchess of York) 1936 photo (PD) |
| S228A | 17:18.78–17:24.34 | On November twentieth, 1947, Princess Elizabeth married Philip Mountbatten. | Nationaal Archief 1947 wedding photo (CC0, verify) + GFX "20 Nov 1947" |
| S229A | 17:24.34–17:29.14 | She wore her mother's tiara. The Royal Collection's entry is exact about | **[JEWEL]** 1947 wedding photo crop on tiara (Nationaal Archief CC0 / PD gov newsreel) |
| S231A | 17:34.08–17:39.50 | And according to one of her bridesmaids, Lady Pamela Mountbatten, later Lady Pamela Hicks, | bridesmaids 1947 group photo (PD/CC0, verify) |
| S234A | 17:46.96–17:51.34 | After the wedding, it stayed her mother's. Through the coronation, | Queen Mother 1950s photo (gov/PD, verify) |
| S235A | 17:51.34–17:53.67 | through decades of the reign, until the Queen Mother died in March two thousand two. | Queen Mother in later years rights-clear |
| S246A | 18:40.90–18:44.20 | Queen Mary's Fringe Tiara. | **[JEWEL]** Queen Mary in Fringe tiara (PD) — reveal |
| S247A | 18:44.20–18:47.82 | She wore it on her wedding day in 1947. | **[JEWEL]** 1947 wedding photo (Nationaal Archief CC0) full |
| S248B | 18:50.64–18:53.46 | It became hers in two thousand two, more than fifty-four years later. | **[JEWEL]** 1947 crop |
| S249B | 18:56.86–19:00.26 | As far as the record shows, she wore no other jewel on this list before it was hers. | Elizabeth II later photo rights-clear |
| S250A | 19:00.26–19:03.16 | The tiara in her wedding photographs was not hers. It was her mother's. | **[JEWEL]** 1947 wedding photo slow push |
| S255B | 19:25.86–19:29.48 | Seen this way, a queen's collection looks less like a treasure than a chain of hands. | five first-wearer portraits fade |
| S256A | 19:29.48–19:33.38 | On the day she married, she wore something borrowed. | **[JEWEL]** 1947 wedding image soft focus |
