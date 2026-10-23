# Panou de comandă

**Actualizat:** 2026-10-23 14:55 · **de:** coordonator
_(Detalii: `stare/`. Comenzi: `COMENZI.md`. Rezumatul zilei: `rezumate/2026-10-23.md`.)_

## Așteaptă de la tine, Adrian
_Ești plecat câteva zile: totul de mai jos poate aștepta întoarcerea, în afară de punctul 1 (2 minute, de pe telefon)._
1. **NOU — Cyber-GPU: GitHub nu mai pornește verificările automate (CI)** din 13:46, probabil s-au terminat minutele gratuite pentru repo-uri private: verifică pe GitHub → Settings → Billing and plans → Actions (`stare/cyber-gpu.md`).
2. **Fereastra a doua pe workstation (~30 min, Kronos oprit)**, cu stick-ul din cel mai nou Release: `lspci` (trebuie să apară placa video), `gpu identifica`, rețeaua I219, `cpu porneste`, `reboot`; la final Secure Boot înapoi pe Enabled (`stare/cyber-universe.md`, partea GPU în `stare/cyber-gpu.md`).
3. **OS — testul 8 pe laptop:** la cald (F12) și la rece (pornire directă), cu poze la `net` (`stare/cyber-universe.md`).
4. **Cyber-GPU — firmware-ul semnat NVIDIA:** îl folosim sau nu? Blochează tot ce vine după pasul I4 (`stare/cyber-gpu.md`).
5. **Cyber-GPU — compilatorul pentru programele GPU:** Mesa NAK (recomandat) sau `ptxas` de la NVIDIA (`stare/cyber-gpu.md`).
6. **Propunerea `gpu gfw` + `gpu vbios`** pentru OS (doar citire, pentru fereastra de pe workstation) — da / nu (`integrare/cyber-gpu/2026-10-23_I2-I3_comenzi-gpu-gfw-vbios.md`).
7. **Propunerea „Kronos bare-metal v0.2”** — da / nu / mai târziu (`idei/2026-10-23_kronos-bare-metal_v0.2.md`).
8. **Suita — de privit:** capturile „PDF profil”, „Meniuri clasice”, „Aerisit”, „Simplu” din 23.10 și spune ce aranjare îți place (`stare/suita-office.md`).
9. **Suita — de încercat/verificat (nu blochează):** butonul EN, „Trimite o observație”, Rezolvitor, parole, QR, PDF/A, al doilea monitor; întrebare: server de timp la semnarea PDF? (`stare/suita-office.md`).

## Proiectele acum
| Proiect | Unde e | Lucrează acum? | Ultima veste (ora) |
|---|---|---|---|
| **Kronos** | E2: S22 gata (ruterul 90,0 %, la limită); **S23** = 3 specialiști pe placă | Da — S23 până pe la ~18:10, verdict la 20:15 | 11:15 (`cyberspace/plan/pentru_adrian.md`) |
| **Cyber Universe OS** | C-13 gata; C-14: rețea I219 (os-174), SSE/AVX (os-175), nucleele pornesc (os-177); 62 de teste | Da — sesiunea de 14:40 face K6-02b (fire pe toate nucleele) | 14:45 (`cyber-universe` git, `docs/TASKS.md`) |
| **Cyber-GPU** | Pașii I2–I3 scriși (doar simulare), 82 teste; calcul pe procesor bf16 ~12× mai rapid; CI oprit la GitHub | Nu acum — următoarea sesiune 19:25 | 13:55 (`stare/cyber-gpu.md`) |
| **Suita office** | Meniurile în engleză: Imagini, Video, Notițe gata; Word 80,3 %, Excel 79,8 % | Da, continuu pe ThinkPad (ferestrele din Docs/Sheets/Slides/PDF în engleză) | 14:12 (`stare/suita-office.md`) |

## Comenzi
- **C-14** · cyber-universe · rețea I219 + Kronos pe procesor (SSE/AVX, SMP, memorie mare) — `preluat` (P6-16, K6-01 gata; K6-02b în lucru)
- **C-11** · cyber-universe · experimente mici GPU + studiu — `nou`, după C-7 (așteaptă întoarcerea ta)
- **C-7** · cyber-universe · bucla de test de la distanță — `nou`, după testul 8 la rece
- **C-3** · cyber-universe · Faza 6 (Claude în OS) — `preluat`: rămâne testul pe laptop
- Terminate de la rularea de dimineață: **C-12** (comanda `gpu`, os-163) și **C-13** (PCI pe toate rădăcinile, hub-uri USB, stick-ul corect, `reboot` cu 4 metode, os-172) — `gata`.

## Propuneri de colaborare
- **Kronos bare-metal v0.2** (`idei/…_v0.2.md`) — recomandare: **da doar pentru partea Kronos pe procesor, după verdictul E2**; partea OS e deja în lucru prin C-14, iar partea GPU așteaptă fereastra pe workstation și decizia despre firmware.
- **`gpu gfw` + `gpu vbios`** (`integrare/cyber-gpu/…`) — recomandare: **da**, cost mic și doar citire; OS-ul o face după C-14, ca fereastra de pe workstation să verifice totul dintr-o pornire.
