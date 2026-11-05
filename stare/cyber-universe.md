# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-05 07:45 (ora României) · **de:** sesiunea OS programată (07:27) · **Release `os-242`** (CI verde): `gpu lant` pe lanțul complet al ferestrei (C-71)

## Acum
- **Nou în `os-242` — `gpu lant` pe lanțul complet (P6-55, partea OS din C-71, pas 1):** OS-ul folosește lanțul de 13 pași al cyber-gpu
  (`a2f9736`, I6 → primul calcul). Are pașii până la I6 + „WPR2 citit după I6” (doar citire); I7–I10 nu sunt încă în OS, așa că lanțul se
  oprește cinstit la I7, pune Bus Master la loc și face turul. **Nicio scriere nouă în placă** față de `os-241`. Testat doar în SIMULARE.
- **Nou în `os-241` — remote criptat (P6-54, F2 pas 2):** consola prin rețea (`remote porneste`) e acum criptată și semnată cu cheia de pe stick
  (X25519 + ChaCha20-Poly1305, protocol propriu mic, decizia D-016). Cheia nu mai trece prin rețea; cine nu are cheia nu poate citi și nici schimba nimic.
  Clientul `tools/remote-client.py` merge tot fără nimic instalat pe Windows; **trebuie folosit clientul din `os-241`** (`py tools\remote-client.py --test` → „criptografia OK”).
- **Nou în `os-241` — unelte de profil/jurnal (P6-52 pas 3, F9):** `log --sumar` (câte rânduri pe nivel și ce module au avertismente/erori), `log --avertismente`,
  `timp <comanda>` (cât a durat, în ms, și memoria). Merg și prin remote / bucla automată, doar cu comenzi de pe lista albă. **P6-52 (F8/F9) încheiat.**
- **C-68 pentru OS e făcut în întregime:** F3 (actualizare cu revenire), F2 (remote, acum criptat), F4 (`hw lista`), F8/F9 (editor, terminal, `gh-ia`/`gh-trimite`,
  `compara`, profil/jurnal), F6a (browserul text `web`). F1 anulat de Adrian. Restul se verifică pe workstation la fereastră.

## Urmează
- I7–I10 în OS doar după „da”-ul lui Adrian (vezi mai jos). Altfel nicio sarcină liberă fără hardware: P6-10, P6-12 p.2 (workstation/laptop); P3-10 (Adrian); P5-07 BLOCAT; C-7, C-11 după întoarcerea lui Adrian.
- Sesiunile următoare: oprire scurtă dacă nu e comandă nouă.

## Ce oferă proiectul celorlalți
- Actualizarea cu revenire automată (orice stick Cyber Universe), `compara`, `log --sumar`, `timp` pentru rapoarte și profil, `hw lista`, browserul text `web`, remote criptat.
- Biblioteci Rust proprii: `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`; a doua implementare KGR1 pentru Kronos.

## De ce are nevoie de la ceilalți
- `cyber-gpu`: după fereastră, `verifica_jurnal_i6` / `verifica_jurnal_lant` pe jurnalele noi din `rezultate/`.
- `cyber-gpu`: pasul 1 din „Urmează” al vostru e făcut (`gpu lant` pe `WINDOW_CHAIN_FULL`, `os-242`); I7–I10 în OS așteaptă răspunsul lui Adrian.

## Blocaje / nevoie de Adrian
- **Răspuns la C-72 (fereastra de acum, ~08:30):** I7–I10 **NU vor fi gata până la 08:45** — e mult de scris în OS (GSP-RM de pe stick în memorie, tabelele radix3,
  cozile, `GspFwWprMeta`, apoi I8–I10), plus ~35 min de CI. **La fereastra de acum folosește `os-242`** (lista de mai jos). Am început I7–I10 (sarcina P6-56),
  pas cu pas, testat în simulare; Release-ul cu I7–I10 va fi pentru fereastra următoare.
- **Fereastra de azi ~08:30 pe workstation (~25 min), Release `os-242`** (I6 pe stick-ul de test din `os-242`):
  1. **I6, stick-ul de test** (`cyber-universe-gpu-scrie-usb.img`): pornire rece (cablul scos 30 s), `gpu pregatire-i6` → poză, `gpu i6 --scrie` + `DA` **o singură dată** → poză, `raport`. (Sau, în locul lui `gpu i6 --scrie`, `gpu lant` + `DA`: aceleași scrieri, plus „WPR2 citit”, oprire la I7.)
  2. **Kronos, stick-ul normal:** `run kronos --control`; `run kronos --profil --fara-ecran --n 64 Buna ziua`; același cu `--fara-cedari` → poze.
  3. **Nou — actualizarea cu revenire (F3), cu Release-ul nou:** pe stick-ul normal `actualizeaza`, repornire → pe ecran „prima pornire a versiunii …”; după 1 minut
     `log actualizare` → poză (trebuie „confirmata”).
  4. **Nou — hardware (F4):** `hw lista --detalii` → poze (completăm numele plăcilor necunoscute). Opțional browserul: `run web example.com`.
  5. Opțional, remote criptat: pe workstation `remote porneste` (cu `remote.cheie` pe stick), din alt calculator din casă `py tools\remote-client.py <adresa> -k remote.cheie -c "log --sumar"` → poză.
  6. Pozele + `raport\*.txt` → `rezultate/<data>-workstation-<release>/`.
- **Pentru rapoartele urcate singure în hub (F3):** un token GitHub „fine-grained” doar pentru `Adriancu91/Cyber-hub`, drept „Contents: Read and write”, pus ca
  `github.token` pe stick — când vrei.
- Bucla automată (prima tură, `docs/BUCLA_AUTOMATA.md`), `claude.key`, P5-07: mai târziu.
