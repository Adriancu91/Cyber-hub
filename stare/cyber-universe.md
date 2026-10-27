# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-28 01:22 (ora României) · **de:** sesiunea OS programată · ultimul Release **`os-192`** (CI verde)

## Acum
- **C-23 gata (P6-24, P6-25):**
  - **Căderea de pe laptopul AMD e reparată.** Cauza: o diferență Intel/AMD la instrucțiunea cu care nucleul se întoarce dintr-un apel de sistem
    (`sysret`). Pe AMD, programul rămânea cu un „segment de stivă” cu drepturi greșite (0x18 în loc de 0x1b); prima întrerupere de ceas în timpul
    unui calcul lung (`kronos-calcul`) oprea sistemul. Pe Intel procesorul corectează singur, de aceea acolo mergea. Test automat nou care pică
    pe valoarea veche + `kronos-calcul` în QEMU pe un procesor AMD Zen 2 emulat. Confirmarea reală: tu, pe laptopul AMD.
  - **Stick-ul pe laptopul Intel:** OS-ul pornește acum **toate** controlerele USB (pe Tiger Lake sunt două), nu doar primul. Test QEMU cu două controlere.
- **C-26 gata (P6-26):** `hw` (și deci `raport`) arată „ecran: framebuffer la adresa fizica 0x…, mărime, LxI, pitch, 32 bpp”. Doar citire.
- CI run 192 verde (la a doua încercare: două teste cu mouse, cunoscute ca instabile, picaseră o dată) → **Release `os-192`**. os-187 rămâne punctul de revenire.
- **C-25 preluat (P6-27)**, **C-27 preluat (P6-28)**: așteaptă C-24 de la Kronos (specificația KGR1 + vectorii de test în `integrare/kronos/`, încă nu există).

## Urmează
- P6-27 (motorul KGR1 + comanda `kronos`) imediat ce apar în hub `integrare/kronos/format_greutati.md` și vectorii de test; apoi P6-28 (C-27).
- C-7, C-11 când se întoarce Adrian.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/`.
- Pentru `cyber-gpu`: adresa framebuffer-ului în `hw` (C-26, propunerea lor B0); bibliotecile lor (fixate pe `dac2e32`) rulează în nucleu doar-citire.
- Pentru Kronos: `kronos-calcul` merge acum și pe AMD (în QEMU) și pe Intel real pe 8 nuclee (7×); motorul KGR1 vine după C-24.

## De ce are nevoie de la ceilalți
- `kronos`: C-24 partea A (specificația KGR1 + modelul minuscul + logit-urile de referință în `integrare/kronos/`) — de ea depinde C-25.
- `cyber-gpu`: o ramură `main` sau un tag ar fi mai clar de fixat decât `dac2e32`; nu blochează.

## Blocaje / nevoie de Adrian
- **Test cu `os-192` pe cele două laptopuri (~15 min, ca pe 27 oct, Secure Boot oprit):**
  - **AMD (Ryzen 5 4500U):** `run kronos-calcul` (așteptat: „toate rezultatele in toleranta declarata (OK)”, fără #GP), apoi `cpu porneste`,
    `run kronos-calcul` (6 fire), `hw` (rândul nou „ecran: framebuffer…”), `raport`.
  - **Intel (ThinkPad L15 Gen 2):** `lsusb` (stick-ul trebuie să apară, de ex. „c2/…”), `ls /usb`, `raport` (așteptat: „scris /usb/raport/…”), `hw`.
  - Fișierele `raport/*.txt` de pe stick → în `rezultate/` din hub (cheile sunt ascunse).
- **Fereastra pe workstation** (când vrei, Kronos oprit): ca în lista de dinainte, cu `os-192`; în plus rândul „ecran:” din `hw` pentru Cyber-GPU (B0).
- Tag-ul `stabil-2026-10-23` (2 minute, opțional): pașii din jurnalul de pe 26 oct; până atunci punctul de revenire e ramura + os-187.
- `github.token`, `claude.key`: mai târziu. B-003 / P5-07: mai târziu.
