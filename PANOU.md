# Panou de comandă

**Actualizat:** 2026-10-23 10:30 · **de:** centrul de comandă
_(Detalii: `stare/`. Comenzi: `COMENZI.md`. Rezumatul zilei: `rezumate/2026-10-23.md`.)_

## Așteaptă de la tine, Adrian
**Adrian e plecat câteva zile (din 23 oct).** Kronos în pauză; OS-ul (C-13, C-14) și Cyber-GPU (sesiune programată nouă) lucrează automat în cloud; niciun test pe hardware până se întoarce. Punctele de mai jos așteaptă întoarcerea.
00000. **Fereastra 1 pe workstation (09:30–09:55):** OS-ul PORNEȘTE pe workstation (i9, 128 GB), dar nu vede placa video (PCI pe mai multe rădăcini) → **C-13**; `rezultate/2026-10-23-workstation-os/`. Pune Secure Boot înapoi pe Enabled. Inventarul: inventarul K0 din Windows e FĂCUT (`rezultate/2026-10-23-k0-workstation/`): Dell, i9-10980XE 18C/36T, RTX 3070 Ti `10de:2482` pe bus B3, ReBAR oprit. Urmează BIOS + OS de pe stick (os-161), apoi `gpu identifica` după C-12.
1. **Kronos — alege 1, 2 sau 3 pentru S20** (1 = închidem E1, trecem la specialiști + ruter, recomandat; 2 = antrenare pe cele 918 întrebări; 3 = altă metodă). Placa stă liberă din 00:33 până alegi (`cyberspace/plan/pentru_adrian.md`).
2. **Fereastra pe workstation pentru Cyber-GPU (~30 min, Kronos oprit)** — acum e momentul bun, placa e liberă. Aștepți întâi Release-ul nou din C-12 (în lucru), apoi: inventarul din Windows, setările BIOS, `gpu identifica` de pe stick (`stare/cyber-gpu.md`, lista în `stare/cyber-universe.md` după C-12).
3. **OS — testul 8 pe laptop** (Release os-155 sau cel nou din C-12): la cald cu F12 și la rece, fără comenzi `rtl`, poze la `net` (`stare/cyber-universe.md`).
4. **Cyber-GPU — două decizii:** folosim firmware-ul semnat NVIDIA (licența lui cere sistem OSI, OS-ul e MIT)? și ce compilator pentru programele GPU: Mesa NAK (MIT) sau `ptxas` NVIDIA (restrictiv) (`stare/cyber-gpu.md`).
5. **Cyber-GPU — CI:** mută `ci/github-actions-ci.yml` în `.github/workflows/` din repo-ul `cyber-gpu` (tokenul lor nu are voie) (`stare/cyber-gpu.md`).
6. **Propunerea „Kronos bare-metal v0.2”** — da / nu / mai târziu (`idei/2026-10-23_kronos-bare-metal_v0.2.md`).
7. **Suita — de încercat (nu blochează):** Notițe noi (Desenare, Carduri, clic dreapta, Ctrl+1/2/0), Video, Imagini, Docs/Slides tabele, Sheets și PDF ca la birou (`stare/suita-office.md`).
8. **Suita — de verificat și o întrebare (nu blochează):** Rezolvitor, parole, .docx protejat, cod QR, PDF/A, al doilea monitor; vrei server de timp la semnarea PDF? Opțional: codul suitei pe GitHub (`stare/suita-office.md`).

## Proiectele acum
| Proiect | Unde e | Lucrează acum? | Ultima veste (ora) |
|---|---|---|---|
| **Kronos** | **PAUZĂ** (Adrian plecat; S20 așteaptă). E1 NECLAR (13/50, dar multe răspunsuri copiate); S21: fără regresie. 895 teste | Nu — placa liberă, așteaptă alegerea ta (S20) | 08:15 (`cyberspace/plan/pentru_adrian.md`) |
| **Cyber Universe OS** | C-10 gata (os-155); stătea oprit din 05:50 (aștepta testul 8), repornit de C-12 | Da — sesiunea de 08:40 face C-12 (comanda `gpu`, P6-11) | 08:44 (`cyber-universe` git, `docs/TASKS.md`) |
| **Cyber-GPU** | 7 piese de cod, 58 teste, doar în simulare; datele workstation-ului culese | Da — sesiune programată în cloud, de 4 ori pe zi (01:25/07:25/13:25/19:25), fără placa reală | 03:05 (`stare/cyber-gpu.md`) |
| **Suita office** | Toate 7 aplicații așezate ca programele cunoscute (punctul 5 gata). Word 80,3%, Excel 79,8% | Da, continuu pe ThinkPad (urmează 5b: nume fișier importat) | 08:45 (`stare/suita-office.md`) |

## Comenzi
- **C-14** · cyber-universe · cât e Adrian plecat: driver rețea I219 + pregătirea Kronos în OS (SSE/AVX, SMP, memorie mare) — `nou`, după C-13 (10:20)
- **C-13** · cyber-universe · PCI pe toate rădăcinile (GPU invizibil pe workstation), hub-uri USB, alegerea stick-ului — `nou` (09:55)
- **C-12** · cyber-universe · patch-ul `gpu identifica` + Release pentru workstation — `preluat` (08:42, P6-11)
- **C-11** · cyber-universe · experimente mici GPU + studiu driver propriu — `nou`, după C-7
- **C-7** · cyber-universe · bucla de test de la distanță — `nou`, după ce trece testul 8 la rece
- **C-3** · cyber-universe · Faza 6 (Claude în OS) — `preluat`: rămâne testul pe laptop
- Terminată de la rularea de aseară: **C-10** (buffer-ele primei inițializări + OCP la rece, os-155) — `gata` la 00:00.

## Propuneri de colaborare
- **Kronos bare-metal v0.2** (`idei/2026-10-23_kronos-bare-metal_v0.2.md`) — recomandare: **mai târziu**; întâi testul 8 și fereastra pe workstation, după care partea cea mai ieftină (Kronos pe procesor în OS, K6-CPU) poate fi aprobată prima.
