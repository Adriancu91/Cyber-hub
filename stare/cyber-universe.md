# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-22 17:30 (ora României) · **de:** sesiunea OS programată (16:28) — C-8 făcută (P6-10d), Release `os-138`

## Acum
- **C-8 (după testul 5) e gata, CI verde, Release `os-138`:**
  - **Revenire:** placa pornește iar EXACT ca în os-125 (testul 4, ultima versiune care trimitea și primea): nu mai scriem nimic în
    „Device Control” (os-136 ștergea Relaxed Ordering, 2010 → 2000) și nu mai golim cache-ul. Registrele PCI se scriu doar bit cu bit,
    fiecare scriere în jurnal.
  - **RCR 0002c70a vs 0000c70a:** am verificat — driverul scrie aceeași valoare în ambele versiuni și nu atinge bitul 17, deci placa era
    în altă stare la pornire. Bănuiala mea: testul 5 a pornit „la rece” direct de pe stick; la plăcile 8168G/H firmware-ul poate lăsa
    închisă „poarta RXDV” (registrul MISC, bitul 19), care oprește orice transfer — exact 0 trimise / 0 primite. Modelul cipului reproduce asta.
  - **Variante, încercate pe rând din aceeași pornire** (regula „o schimbare odată”): `rtl porneste rxdv` (deschide poarta RXDV, doar
    dacă e închisă), `rtl porneste bloc` (bufferele de primire într-un singur bloc sub 4 GB), `rtl porneste cache` (golirea de la os-136).
  - **Diagnostic:** `log rtl` arată registrele, MISC (poarta), Bus Master, adresele pe 64 de biți, RAM-ul; `log rx` arată fiecare din
    primele 8 pachete cu adresa completă și primii octeți.
  - **Studiu (clean-room):** driverul FreeBSD (licență BSD) deschide exact această poartă la plăcile 8168G; de acolo varianta `rxdv`.
- Test nou în emulator cu 6 GB și memoria forțată peste 4 GB: rețeaua merge. 50 de scenarii automate + 27 de teste ale driverului.

## Urmează
- Testul 6 pe laptop (lista mai jos) → varianta care merge devine implicită în versiunea următoare → apoi C-7 (bucla automată).

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3, rădăcini Mozilla), `json/` (și base64), `rtl8168/`.
- Clienți minimali: API-ul Claude, GitHub Releases + contents, cu imitații pentru teste în `tools/`.

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **Testul 6, dintr-o singură pornire, cablul de rețea băgat** (Release **`os-138`** sau mai nou):
  1. Copiezi pe stick fișierele din Release (ca la testul 5, inclusiv `cyber.rw`), pornești de pe stick, aștepți ~1 minut, **Esc** → `cyber>`.
  2. **Pasul A (exact ca os-125):** `net` → poză; `log rtl` → poză.
     Dacă „pachete trimise” > 0 și „primite” > 0: și `log rx` → poză, `ping 1.1.1.1` → poză, apoi treci la pasul C.
  3. **Pasul B (doar dacă la A e tot 0 / 0):** `rtl porneste rxdv` → aștepți ~30 s → `net` → poză; `log rtl` → poză.
  4. **Pasul C:** scrii varianta care a mers la B (sau nimic, dacă A a mers) plus ` bloc`, de ex. `rtl porneste rxdv bloc` sau
     `rtl porneste bloc` → ~30 s → `net` → poză; `log rx` → poză; `ping 1.1.1.1` → poză; `host github.com` → poză.
  5. Spune-mi și: la testul 4 (care mergea) ai pornit laptopul din Windows (Restart) sau de la oprit? La testul 5 a fost de la oprit?
- `github.token` / `claude.key`: încă nu — după ce merge rețeaua.
- B-003 / P5-07 (suita ca modul): mai târziu.
