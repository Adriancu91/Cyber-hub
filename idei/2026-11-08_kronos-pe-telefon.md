# Kronos pe telefon — asistent privat în română, local, fără server

- **Propus de:** centrul de comandă, la cererea lui Adrian (8 nov 2026, 08:52) · **Pentru:** kronos (+ cyber-universe pentru motorul KGR1)
- **Stare:** PARCAT (decizia lui Adrian) — **nu se începe acum**. Se reevaluează când Kronos se apropie de nivelul unui GPT
  (vezi „Când îl scoatem din parcare”); atunci se măsoară din nou pe un telefon de top (ex. iPhone 17 Pro) dacă modelul de atunci încape și merge local.

## Ideea
O pagină web instalabilă (PWA), apoi aplicație (Google Play — Adrian are cont de dezvoltator; App Store mai târziu), care descarcă **o singură dată** modelul
Kronos în telefon și rulează **totul local**: fără server, fără internet după prima descărcare, nicio conversație nu iese din telefon.
Folos: asistent privat în română pentru clienți (ținta „utilitate reală”, 3 nov) + demonstrație („modul avion, Kronos răspunde”).

## Ce refolosim
- **Motorul KGR1** din Cyber Universe (Rust) → compilat în **WebAssembly** pentru procesorul telefonului (fără rescriere de la zero).
- **Formatul KGR1 Q8_0** și vectorii de control ai lui Kronos (aceleași simboluri ca pe procesor = test de corectitudine).
- Lecțiile din cyber-gpu pentru „un singur program pe simbol” → programe **WGSL** (WebGPU) scrise de noi; programele NAK nu se pot folosi direct.

## Etape (când se scoate din parcare)
| etapă | ce | dovada că merge |
|---|---|---|
| T0 | Măsurătoarea de pornire: modelul Kronos de atunci (mărime, Q8/Q4) față de telefoanele țintă (RAM, WebGPU) — calcul + o probă | tabel: încape / nu încape, viteză estimată |
| T1 | KGR1 în browser pe **procesor** (WASM, fire Web Workers) | vectorii de control: aceleași simboluri ca motorul de referință |
| T2 | KGR1 pe **placa video a telefonului** (WebGPU, WGSL), cu întoarcere pe procesor dacă lipsește WebGPU | aceleași simboluri; simboluri/secundă măsurate pe 2–3 telefoane |
| T3 | **PWA** instalabilă, modelul păstrat în telefon, merge în modul avion; conversație cu istoric local | test în modul avion pe Android și iPhone |
| T4 | Variante mai mici ale modelului (Q4) dacă e nevoie de viteză/memorie, cu examenul de română ca măsură a pierderii | examen română: pierdere sub pragul scris dinainte |
| T5 | Aplicație Google Play (și App Store), actualizare automată a modelului când Kronos crește | aprobare în magazin |

## Când îl scoatem din parcare (criteriul lui Adrian: „când Kronos se apropie de GPT”)
- Kronos răspunde bine în română la întrebări deschise, instrucțiuni, rezumate și conversații (examenul de română + setul ascuns + evaluare pe întrebări reale), nu doar continuă text.
- Atunci facem **T0 pe un telefon de top** (ex. iPhone 17 Pro) și pe un Android bun: încape modelul în memoria telefonului? câte cuvinte/secundă? cât consumă bateria?
- Regula orientativă de verificat atunci: modelul (după comprimare) să ocupe sub ~jumătate din memoria telefonului; dacă nu încape, T4 (comprimare) sau o variantă mai mică a lui Kronos doar pentru telefon.

## Ce NU face
Fără server, fără API-uri plătite, fără alt AI în locul lui Kronos (decizia „de la zero”), fără date trimise din telefon. Nu are legătură cu propunerea Cyber-Multiverse (rămâne separată).

## Riscuri
- Memoria browserului pe telefon (limite pe tab, mai ales pe iPhone) → T0 măsoară, T4 comprimă.
- Încălzire și baterie la conversații lungi → măsurate la T2.
- WebGPU lipsă pe telefoane vechi → întoarcere pe procesor (T1).

## Discuție
- 2026-11-08 08:52 Adrian: „Fă un plan … și îl păstrăm până când Kronos se apropie de GPT, atunci mai măsurăm o dată dacă putem să îl punem local pe telefon, exemplu iPhone 17 Pro.” → PARCAT.
