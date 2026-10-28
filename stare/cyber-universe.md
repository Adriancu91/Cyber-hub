# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-28 05:45 (ora României) · **de:** sesiunea OS programată · ultimul Release **`os-194`** (CI verde)

## Acum
- **C-25, partea 1 gata (P6-27): Kronos poate rula în OS.** Comanda nouă `kronos` citește un fișier de model `.kgr` (F32 sau Q8_0) de pe stick
  (`/usb/kronos/`), verifică suma SHA-256 și continuă un text dat ca numere de simboluri (`kronos --simboluri 1,2,3`), pe toate nucleele, cu
  instrucțiuni vectoriale AVX2 unde există; arată simbolurile pe secundă. Motorul e scris de noi din specificația KGR1 din hub (fără codul Kronos)
  și e verificat în CI pe un model minuscul cu greutăți la întâmplare: rezultatele egale cu un calcul de control (abatere ~1e-5).
- **Lipsește încă (P6-27b):** textul direct (`kronos "Bună ziua"`) — cere tokenizerul din fișier, iar specificația nu-l descrie încă — și testul pe
  vectorii oficiali Kronos (C-24 partea A).
- **C-27 gata (P6-28):** `kronos-calcul --cauta` caută singur cea mai bună variantă de calcul pentru calculatorul pe care rulează (vectori sau nu,
  câte fire, ordinea buclelor), aruncă orice variantă care dă rezultate greșite (testat cu una stricată intenționat) și scrie alegerea pe stick
  (`/usb/kronos/reglaj-<procesor>.txt`); `kronos` o folosește la pornire.
- CI run 194 verde → **Release `os-194`**. os-187 rămâne punctul de revenire.

## Urmează
- P6-27b imediat ce apar `integrare/kronos/vectori/` și descrierea tokenizerului **în hub** (la C-24 scrie că descrierea e deja la S39 în
  repo-ul Kronos; OS-ul o ia doar din hub, după ce o copiază supraveghetorul).
- C-7, C-11 când se întoarce Adrian.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/`.
- Pentru Kronos: un motor KGR1 independent (`user/src/kgr.rs`) — o a doua implementare a specificației, utilă ca verificare încrucișată.
- Pentru `cyber-gpu`: adresa framebuffer-ului în `hw` (C-26).

## De ce are nevoie de la ceilalți
- `kronos` (C-24 partea A): `integrare/kronos/vectori/` și, în `format_greutati.md`, **o descriere a tokenizerului** `tokenizer.bpe`: ce conțin
  `imbinari`, `speciale`, `reguli`, `versiune`; cum se împarte textul înainte de îmbinări (octeți? UTF-8? spații?); ordinea îmbinărilor; cum se
  decodează. Fără ea, OS-ul nu poate scrie tokenizerul fără să citească codul Kronos (C-25 cere cod propriu).
- `kronos` (C-24 partea B): `MODEL.md` cu suma SHA-256 și 3 texte cu primele 5 simboluri greedy (sumele se pot pune lângă model ca `<nume>.kgr.sha256`).
- `cyber-gpu`: o ramură `main` sau un tag ar fi mai clar de fixat decât `dac2e32`; nu blochează.

## Blocaje / nevoie de Adrian
- **Test cu `os-194` pe cele două laptopuri (~15 min, Secure Boot oprit):**
  - **AMD (Ryzen 5 4500U):** `run kronos-calcul` (așteptat „... (OK)”, fără #GP), `cpu porneste`, `run kronos-calcul`, `hw`, apoi
    `run kronos-calcul --cauta` (scrie `/usb/kronos/reglaj-….txt`; stick-ul trebuie să aibă `cyber.rw`), `raport`.
  - **Intel (ThinkPad L15 Gen 2):** `lsusb` (stick-ul, de ex. „c2/…”), `ls /usb`, `run kronos-calcul --cauta`, `raport`, `hw`.
  - Fișierele `raport/*.txt` și `kronos/reglaj-*.txt` de pe stick → în `rezultate/` din hub (cheile sunt ascunse).
- **Fereastra pe workstation** (când vrei, Kronos oprit): lista de dinainte cu `os-194` + `run kronos-calcul --cauta` (36 de fire: vedem dacă firele
  multe câștigă) + rândul „ecran:” din `hw` pentru Cyber-GPU.
- **Modelul Kronos real pe stick:** când e gata MODEL.md (C-24 B), copiezi fișierul `.kgr` în `kronos/` pe stick; apoi `run kronos --simboluri …`.
- Tag-ul `stabil-2026-10-23` (opțional); `github.token`, `claude.key`: mai târziu. B-003 / P5-07: mai târziu.
