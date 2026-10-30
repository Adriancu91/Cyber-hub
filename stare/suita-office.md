# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-30 09:45 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Plusurile alese de Adrian: P1 (diacritice), P2 (e-Factura) și P3 (extrase de cont) sunt gata; **P4 (semnături digitale) e gata în afară de LTV**, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”. Sesiunea 08:58–09:45, 4 pași, testele trec:
  - **Sheets:** stiluri de tabel proprii (Proiectare tabel → ＋ Stil de tabel nou… / Modifică / ✕ Șterge), ținute în registru și în .xlsx.
  - **Docs:** la deschiderea unui .docx, schimbările urmărite de culoare, font, mărime și evidențiere apar în panou și se pot respinge.
  - **PDF:** 🔎 Căutare în dosar cu ⚡ Index (catalog): căutările următoare iau textul din index, fără să redeschidă PDF-urile.
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: **Word 89,3%**, **Excel 89,1%**, **PowerPoint 90,1%**, Clipchamp 80,5%, Notițe 80,7%, Acrobat 82,3%, Photoshop 81,5%, formule 97,1%. Colecția de test: **476 / 560** fișiere reale fără pierderi, 0 erori.

## Urmează
- Alte funcții „parțial” / „nu” din inventar.

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text), motorul de diacritice și despărțirea în silabe românească, semnarea / verificarea XML (XML-DSig, scrise de la zero).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- Să încerce Sheets → un tabel → Proiectare tabel → ＋ Stil de tabel nou… cu culorile firmei → Export .xlsx deschis la serviciu (tabelul are culorile și stilul e în listă?); un .docx de la serviciu cu urmărirea pornită, în care a schimbat culoarea / fontul unui cuvânt → Docs → Import .docx (apare în panou, Respinge îl face la loc?); PDF → 🔎 Căutare în dosar → ⚡ Index pe un dosar mare: a doua căutare e mult mai rapidă?
- Să încerce Imagini → ✒ Traseu → un triunghi → Fereastră → ⌇ Trasee (apare „Traseul de lucru” cu forma lui?) → 💾 → ▉ Umple; ◫ Straturi → ＋ Compoziție nouă, mută sigla, încă o compoziție, clic pe prima (sigla revine?); ✎ Adnotează → T Text într-o casetă îngustă → a-b Silabe (cratimele sunt corecte?); Slides → Felie de cerc / Placă → Export .pptx deschis la serviciu.
- Să încerce Imagini → o fotografie → Salvează → JPG → ⊞ Compară 4 variante (se vede diferența?) și Metadate: Doar autorul și drepturile + profilul sRGB, apoi fișierul deschis la serviciu: culorile și autorul sunt bune? Și Fereastră → ⓘ Proprietăți → scrie 100 la ↔ pe un logo: se micșorează fără să se deformeze?
- Să încerce Sheets → un tabel lat → Vizualizare → ◫ Stânga-dreapta (scrie în stânga, derulează dreapta spre capăt), Slides → ◼ Formă ▾ → Explozie 1 / Val / Schemă: Document → Export .pptx deschis la serviciu (forma e aceeași?), Slides → Teme → Prună / Mentă, și Imagini → 🖌 Pensulă → Pensule gata → Confetti: arată bine?
- Să încerce Sheets → un tabel → Proiectare tabel → Stiluri tabel (derulează galeria) → „Verde umplut” / „Albastru cu grilă”, și un .xlsx de la serviciu cu un tabel cu linii: arată la fel? Și Video → ▭ Carton → Apariția textului → Săritură / Cuvânt cu cuvânt, Cum arată textul → Balon de vorbă, Felul trecerii → Stea / Dizolvare: arată bine?
- Să deschidă în Sheets un .xlsx de la serviciu cu poze puse în celule (de exemplu o listă de produse cu poze): pozele apar în celule? Apoi Inserare → ▣ În celulă cu o poză de-a lui → Salvează ca .xlsx → deschis la serviciu: poza e tot în celulă?
- Să deschidă în Sheets un .xlsx de la serviciu care ia cifre din alt fișier (de exemplu un raport legat de o listă de prețuri), cu ambele fișiere în același dosar: formulele rămân și cifrele sunt aceleași? Apoi Date → 🔗 Editare legături → ↻ Actualizează valorile după ce schimbă o cifră în fișierul-sursă.
- Să deschidă în Suite un .docx / .pptx de la serviciu cu formule: apar și se pot schimba (clic → ✎ Ecuație)? Și invers: o ecuație din Docs / Slides salvată .docx / .pptx și deschisă la serviciu: se poate schimba acolo?
- Să încerce un .xlsx de la serviciu cu o listă derulantă luată dintr-un nume sau din alt fișier: în Sheets apar variantele? Și un .odt / .odp cu o formulă: în Suite se poate schimba cu ✎ Ecuație? Și Imagini → Deschide → un .orf de la un aparat Olympus.
- Să încerce Imagini → Deschide → un fișier RAW de la aparatul lui (sau un .dng de pe telefon): apare poza, întoarsă corect? Și Notițe → ✎ Desen → scrie de mână un cuvânt → clic pe desen → ↧ Pune în notiță: cuvântul apare în text?
- Să încerce Slides → Inserare → ◇ Diagramă ▾ → Pâlnie / Cronologie → Export .pptx deschis la serviciu: arată la fel? Și Imagini → ✒ Traseu → 💾 Salvează traseul → salvat .psd și deschis la serviciu: traseul e în panoul de trasee?
- Să încerce Imagini → un logo pe un strat nou → V → trage-l spre mijlocul pozei: se oprește singur la mijloc, cu o linie roz (și cu Ctrl merge liber)? Și Slides → ◼ Formă → Explicație cu săgeți în patru direcții / Săgeată îndoită în sus → Export .pptx deschis la serviciu: forma e aceeași? Și Video → Felul trecerii → Cruce / Despicare orizontală: arată bine?
- Să încerce PDF → un afiș / pliant cu un Pantone → Producție pentru imprimare → 🖌 Cerneluri… → Toate în proces → Aplică, apoi 🎨 Separări…: culoarea arată la fel? Și Video → un text → Apariția textului → Intră din stânga / Zoom / Dezvăluire și stilurile Etichetă roșie / Chenar / Umbră spre jos: arată bine?
- Să încerce Docs / Slides / Sheets → Inserare → ☺ Pictograme → caută „telefon”, alege o culoare și 2–3 pictograme → Inserează: arată curat și au mărimea potrivită? Și Video → două poze → Felul trecerii → Ceas / Romb / Despicare → ▶: trecerile arată bine?
- Să încerce Slides → 🖵 Înregistrare ecran → trage un dreptunghi peste o fereastră → ● Înregistrează zona, apoi lucrează în fereastra aceea: clipul arată doar zona, fluent? Și Docs / Slides → o poză cu logo → Fundal… → Marchează zonele…: e ușor de folosit? Și Slides → Revizuire → ⚖ Compatibilitate pe o prezentare bogată: lista are sens?
- Să încerce Sheets → un tabel lung → Vizualizare → 📃 Aspect pagină (antet scris sus, Peisaj): paginile arată ca la tipărire? Și Stiluri celulă → ✎ Modifică un stil… pe „Bun” sau pe un stil de-al lui: se schimbă toate celulele cu stilul?
- Să încerce Slides → un tabel → clic într-o celulă și tras peste altele (sau Shift+clic) → Proiectare tabel → 🪣 / A / B: se schimbă toate celulele alese? Și un .odp cu un tabel colorat, cu celule îmbinate: arată la fel în Suite?
- Să încerce Slides → Inserare → ▦ Foaie de calcul… cu un .xlsx colorat de-al lui, apoi Export .pptx deschis la serviciu: tabelul are aceleași cifre și culori? Și un .pptx de la serviciu cu celule colorate de mână: culorile rămân la deschiderea în Suite?
- Să încerce PDF → Producție pentru imprimare → ✈ Preflight… pe un afiș sau un pliant pe care îl duce la tipografie (profilul Tipografie, apoi „Ecran și web”): ce apare cu ✗ și ⚠ are sens? Și Docs → Inserare → ▦ Foaie de calcul… cu un .xlsx colorat de-al lui: tabelul din document seamănă cu cel din Sheets?
- Să încerce PDF → ⧉ Combină… cu un .docx, un .xlsx colorat, o prezentare .pptx, un e-mail tras din programul de e-mail (.eml) și un PDF de-ale lui, și PDF → ⚙ Lot… cu câteva .docx: paginile arată bine (tabelul ca în Sheets, slide-urile ca în Slides, e-mailul cu antet și poze)? Și PDF → ☰ Meniu → ✉ Trimite prin e-mail…: se deschide programul de e-mail cu PDF-ul atașat?
- Să încerce Docs → Fișier → ✉ Trimite prin e-mail… și Notițe → Fișier → ✉ Trimite prin e-mail (pe o notiță cu o poză): se deschide programul lui de e-mail cu documentul atașat / notița și poza în mesaj? Și Docs → Corespondență → 📨 Începere îmbinare → ✉ Câte un e-mail (.eml) cu un tabel cu adrese: mesajele se deschid gata de trimis? Și un text cu un cuvânt mare și unul cu alt font, lipit în Notițe: în 📖 Lectură arată la fel?
- Să încerce Imagini → ⬚ Marcaj peste o semnătură scanată → 🖌 Definește pensulă → 🖌 Pensulă → „Pensulă proprie 1” → clic pe poză (apare semnătura?), și ✒ Traseu → ◇ Definește formă → ✎ Adnotează → Forme proprii: e ușor de folosit?
- Să copieze dintr-o pagină web sau dintr-un document un text cu aldin, culori și titluri și să-l lipească în Notițe: în 📖 Lectură arată la fel? Și Notițe → Titlu… → Citat / Sursă / Cod.
- Să încerce Imagini → Ajutor → ⌨ Scurtături de la tastatură… → pune F6 pe o comandă folosită des: e ușor? Și Video → Ctrl+clic pe două poze → 🔗 Grupează → trage-le: se mută împreună?
- Să încerce Imagini → ▤ Mai multe poze… cu un dosar amestecat (poze + scanări) → Culorile: Alb-negru, bifat doar „în tonuri de gri”: scanările ies alb-negru, pozele rămân color?
- Să încerce PDF → Semnează… → 🎬 Sunet / video… cu un film de pe telefon, salvat și deschis la serviciu în alt program de PDF: filmul se vede și pornește? Și 📐 → 🌐 Coordonate pe o hartă PDF reală (cadastru, topografică): coordonatele arată locul corect pe o hartă de pe internet?
- Să încerce Notițe → o listă de bifat → trage un element de căsuța lui pe alt rând: e ușor de prins căsuța? Și Imagini → ⓘ Informații → Autor și Cuvinte cheie pe o poză a lui → Ctrl+S, apoi în Windows clic dreapta pe fișier → Proprietăți → Detalii: apar autorul și etichetele?
- Să încerce Sheets → Ctrl+Q pe un tabel real, cu mouse-ul pe butoanele din filele Tabele, Minigrafice și Grafice (previzualizarea ajută?), și un Tabel de date (Ce-ar fi dacă) cu rata unui credit, salvat .xlsx și deschis la serviciu: rămâne tabel de date și se recalculează când schimbi suma?
- Să încerce Sheets → Tabel Pivot → Filtru deasupra rezumatului cu două-trei elemente bifate, și 🧮 Rezolvitor cu bifa de raport pe o problemă reală (foaia raportului: limitele și prețurile umbră au sens?), plus Slides → Fișier → Împachetează într-o arhivă .zip… deschisă pe alt calculator.
- Să încerce Sheets → Tabel Pivot pe un tabel real cu „+ Grupează categorii” (de exemplu orașele pe regiuni) și „+ Element calculat” (diferența dintre două categorii): e ușor de folosit și cifrele sunt cele așteptate?
- Să încerce Sheets → Tabel Pivot pe un tabel real cu Agent pe coloane și „Încă un câmp pe coloane” (de exemplu Produs), sau cu o coloană de date pe coloane grupată pe luni: cifrele și subtotalurile sunt cele așteptate?
- Să încerce Imagini → Ctrl+Shift+S → PNG cu bifa 2× și GIF cu Culori: 32: fișierele ies bine?
- Să deschidă în Imagini un .psd de-al lui cu text → ⓘ Proprietăți → Text → ✎ Rescrie textul, apoi Ctrl+S ca .psd și să-l deschidă la serviciu: noul text arată ca originalul și rămâne text pe care îl poate edita?
- Să încerce Slides → Fișier → Fă video din prezentare (MP4)… pe o prezentare cu tranziții: trecerile din film seamănă cu cele din prezentare? Și Imagini → ✒ Traseu → ◐ Mască din traseu: e ușor de folosit?
- Să încerce Slides → Inserare → 𝒜 Text artistic ▾ → „Arc auriu”, apoi Export .pptx deschis la serviciu: textul stă tot pe arc? Și Sheets → Ctrl+Q pe un tabel: previzualizarea la trecerea mouse-ului e utilă sau încurcă?
- Să tipărească din Docs (Ctrl+P) un document cu „Numerotează paginile” pe imprimanta lui: apar numerele jos, marginile sunt albe și textul e clar?
- Să încerce Docs → Corespondență → 📨 Începere îmbinare → 🖨 Tipărește exemplarele (de la … până la …) pe imprimanta lui, și Sheets → Date → Preluare date → Din PDF… cu un extras / o factură PDF reală.
- Să încerce Docs → Corespondență → 🏷 Etichete → „O etichetă pentru fiecare rând dintr-un tabel” și ✉ Plicuri → „Un plic pentru fiecare rând” cu un tabel de clienți de-al lui: ies bine adresele? Tipărite pe o foaie de etichete adevărată, cad pe etichete?
- Să încerce Sheets → Diagramă → tipul „Radar (pânză de păianjen)” și să salveze .xlsx deschis la serviciu: graficul rămâne radar?
- Să deschidă în Slides câteva .pptx reale de la serviciu cu diagrame SmartArt și scheme logice: apar toate, cu textul lor? Și Slides → tabel → Proiectare tabel → Culoarea stilului.
- Să încerce Slides → două dreptunghiuri unul sub altul → Săgeată → Traseu → ┐ Conector frânt, lipită de punctele albastre de jos / sus, apoi Export .pptx și deschiderea la serviciu: săgeata arată la fel și rămâne lipită când muți un dreptunghi?
- Să încerce Slides → Inserare → 📷 Cameo cu camera laptopului, și în prezentare (F5): se vede bine, fără să încetinească?
- Să încerce Video → ▭ Carton → stilul „Pastilă colorată” și trecerea „Jaluzele” între două poze: arată bine în filmul exportat?
- Să încerce PDF → Comprimă… → 🧹 Optimizează structura, ☰ Meniu → Elimină informațiile ascunse… și PDF → Semnează… → 🔍 Caută și redactează pe PDF-uri reale de-ale lui: după Salvează ca…, fișierul arată la fel și nu rămâne nimic din ce a fost redactat?
- Să încerce Docs → Revizuire → Compară cu un .docx… → 📝 Document marcat pe un contract real; și .docx cu secțiuni (Pagina următoare, Orientare / Margini doar pentru secțiune, antet propriu cu 🔗 Legat de anterior debifat) deschise la serviciu: arată la fel?
- Să încerce Sheets → Date → Preluare date → Din imagine… cu o poză a unui tabel adevărat și Sheets → Vizualizare → ⊟ Scindare pe un tabel lung: merg bine?
- Să încerce Imagini → Fișier → ✂ Felii… cu „Și o pagină web (.html)” și o legătură pe o felie: poza apare întreagă în browser și legătura merge?
- Să încerce Slides → Animații → Cale desenată de mână, ✍ Formă liberă, § Zoom de secțiune, 🎙 Înregistrează și 🖵 Înregistrare ecran (cu sunet și în MP4), apoi Export .pptx deschis la serviciu.
- Să încerce Docs → Revizuire → ✓ Gramatică pe un document adevărat: arată greșeli care nu sunt greșeli? Și Docs → Vizualizare → ⊟ Scindare, Slides → 📏 Riglă, Notițe → 📌 Lipește pe margine: sunt ușor de folosit?
- Să deschidă la serviciu fișierele salvate din Suite pe care aici nu le-am putut verifica: .ics din Notițe, .docx din PDF cu poze, .docx / .mht din Notițe, .pptx cu gradient, 3-D și conectori, .xlsx cu fonturile temei și comentarii cu răspunsuri, .odp din Slides, .fdf din PDF, .docx cu formular, filigran, siglă, cuprins și urmărirea formatării: arată la fel?
- **LTV:** ca o semnătură să poată fi verificată și peste ani, Suite ar trebui să întrebe pe internet serverele emitentului certificatului (OCSP / CRL), la semnare. E în regulă, doar la cererea ta, ca la marca temporală?
- Să încerce un .docx semnat din Suite la serviciu și semnarea cu tokenul lui real (PDF → 🔏 Semnează digital); dacă are un .p7m / .p7s sau un .docx semnat real, ni-l poate da pentru colecția de test.
- Să încerce o factură reală: Sheets → Șabloane → Factură (e-Factura) → Export e-Factura (XML), apoi încărcarea în SPV.
- Kitul 0.9.3 e gata (Office-Suite-Test-Instalare-0.9.3.exe, cu lista CE-E-NOU-0.9.3.txt, din commitul d009e246); noutățile de după el intră în 0.9.4. Pe acest laptop Smart App Control din Windows blochează kitul nesemnat (JURNAL.md, 28.10, ora 15:00).
- Dacă suita se va vinde: o verificare juridică a licenței.
