# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-01 17:41 (ora României) · **de:** sesiunea OS programată (oprire scurtă, nicio comandă nouă) · ultima sarcină: **C-48 gata (P6-39)**; CI verde, Release `os-211`
(oprirea „OPRIT” ridicată de C-48)

## Acum
- **C-48 gata (P6-39) — proiecția Kronos și ecranul:**
  - Proiecția **era** pe toate 36 de fire, dar vine imediat după împărțirea qkv + atenție (o parte pe cap: 12 fire lucrează, 24 așteaptă)
    și pornea și pe firele care stătuseră degeaba. Acum, la generare, rulează pe firele care tocmai au lucrat (`fire_proiectie`,
    implicit câte capete: 12 la #477). Simbolurile identice (fiecare valoare de un singur fir, același cod).
  - `kronos-calcul --cauta` măsoară acum ca `kronos` (cu împărțirea pe capete) și caută și firele proiecției (verificate cu controlul),
    scriind `fire_proiectie` în reglaj. `kronos --fire-proiectie N` pentru probe.
  - Ecran: textul generat merge în bloc, cel mult o dată pe secundă; consola mută ecranul o singură dată pe bloc (era ~59 ms pe rând).
- Suita QEMU 80/80 + 1 sărit; CI verde la prima încercare → **Release `os-211`**. Ținta (≥ 150 / ≥ 120 simb/s) se vede doar pe workstation.

## Urmează
- Fereastra următoare pe workstation cu `os-211` (pașii mai jos) → cifrele noi în `rezultate/` → pașii următori.
- Coada fără alte sarcini libere (P6-10, P6-12 p.2 hardware; P5-07 blocat; C-7, C-11 după întoarcerea lui Adrian; C-41 amânat) →
  sesiunile următoare se opresc scurt până la o comandă nouă în `COMENZI.md` sau un rezultat nou în `rezultate/`.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (proprietare de la 28 oct; până la `0bf1303` MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/`.
- Pentru Kronos: a doua implementare independentă a KGR1 și a tokenizerului (`user/src/kgr.rs`, `user/src/bpe.rs`); `--control` TRECE pe #477 (1 nov).
- Pentru `cyber-gpu`: `gpu vbios --detalii`, `gpu fwsec`, `gpu firmware` (I4 TRECE pe placa reală, 1 nov) în `os-211`.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- **Stick-ul nou = Release `os-211`** (GitHub → cyber-universe → Releases, sau `actualizeaza` pe laptop cu cablu). Dacă scrii stick-ul de la zero,
  pune la loc folderul `kronos\` (#477 + `.sha256`, #459), `cyber.rw` și `firmware\`. Reglajul vechi `reglaj-*.txt` poate rămâne (se rescrie la pasul 1).
- **Workstation, Kronos (~6 min, cu `os-211`):** `cpu porneste`, apoi
  1. `run kronos-calcul --cauta` → rândurile „cauta: proiectia pe … fire” și „cea mai buna pe …” (scrie reglajul nou);
  2. `run kronos --control` → așteptat „CONTROL: TRECE (#477 …)”;
  3. `run kronos --profil --fara-ecran --n 64 Buna ziua` (ținta ≥ 150 simb/s) și `run kronos --profil --n 64 Buna ziua` (ținta ≥ 120);
  4. `raport`; pozele cu rândurile „profil:” + `raport/*.txt` + `kronos/reglaj-*.txt` → `rezultate/`.
- **Test pe cele două laptopuri (~15 min, Secure Boot oprit, `os-194` sau mai nou):** AMD (Ryzen 5 4500U): `run kronos-calcul`, `cpu porneste`,
  `run kronos-calcul --cauta`, `hw`, `raport`; Intel (ThinkPad L15 Gen 2): `lsusb`, `ls /usb`, `run kronos-calcul --cauta`, `raport`, `hw`.
- Tag-ul `stabil-2026-10-23` (opțional); `github.token`, `claude.key`: mai târziu. B-003 / P5-07: mai târziu.
