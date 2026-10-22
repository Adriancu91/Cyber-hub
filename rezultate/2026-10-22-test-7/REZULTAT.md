# Testul 7 pe hardware real — Release os-150 — rece (R) și cald (C), rețea prin partajarea Windows (ICS)

**Data:** 2026-10-22, 22:25–22:41 · **Făcut de:** Adrian, pas cu pas, cu centrul de comandă · **Scris de:** centrul de comandă (din poze)
**Rețea:** cablu între laptopul de test și laptopul cu Windows, cu **„Internet Connection Sharing”** pornit pe Windows (Wi-Fi → Ethernet).
Windows dă adrese 192.168.137.x și face DNS/internet. Așa se testează de acum (routerul e greu accesibil). Stick: `cyber-universe-stick-v7.zip`.

## (R) La rece — oprit complet, pornit direct de pe stick
| Pas | Comanda | Rezultat | poza |
|---|---|---|---|
| R1 | `net` | 0 / 0, varianta implicită (cache), ISR 0020 | 01 |
| R2 | `rtl porneste rece` → `net` | secvența de 18 pași a rulat cu registre înainte/după; **tot 0 / 0** | 02 |

Din cei 18 pași, trei au ieșit **EXPIRAT / EȘUAT**: pasul 3 (așteptarea FIFO RX+TX goale, MCU biți 4,5: `[00d3] 22 -> 22`), pasul 9 (OCP E8DE bit 15
pus: `[e8de] 1 -> 1`, trebuia `8001`), pasul 12 (C+ Command bit 3: `2021 -> 2021`). Și pasul 7 (OCP E8DE bit 14 șters: `1 -> 1`) nu a schimbat nimic.
Deci **scrierile prin OCP/ERI în registrele interne ale cipului nu se aplică** (sau citirea lor e greșită): fără ele, trezirea la rece nu se poate
face. Restul: poarta RXDV închisă/deschisă corect (MISC 3f ↔ 8003f), PHY alimentat (PMCH f0), TCR/RCR scrise, revizia 8168GU/8111GU.

## (C) La cald — pornit din meniul F12
| Pas | Comanda | Rezultat | poza |
|---|---|---|---|
| C1 | `net` (prima inițializare, „implicită (cache)”) | 21 trimise / 40 primite, **„cadre cu tip 0000: 36 → 41”**, răspunsuri DHCP (udp 68) 2 → 4, **fără adresă** | 03 |
| C2 | `rtl porneste cache` → jurnal | toate cadrele bune (ARP interpretat, IPv4 346/114), **DHCP: adresa 192.168.137.88**, ruta/DNS 192.168.137.1 | 04 |
| C3 | `rtl porneste faracache` → jurnal | **toate cadrele bune și FĂRĂ golirea cache-ului** (buffer-e la 1595000…) | 05 |
| C4 | `fetch https://example.com/` | **TLS 1.3, certificat verificat, 577 octeți** — internet prin Windows | 06 |

## Concluzii
1. **Golirea cache-ului NU e cauza și nu e reparația.** C3 o infirmă: după repornire, cadrele sunt bune și fără ea. Ce repară e **repornirea
   plăcii**, adică a doua inițializare, care alocă buffer-ele în altă parte (150a000 / 1595000) decât prima (3db000, în memoria de jos).
   Ipoteza cea mai probabilă: la prima inițializare, zona buffer-elor se **suprapune cu altceva** (alocatorul timpuriu dă aceleași pagini și
   altcuiva, sau zona e ștearsă/refolosită după ce placa a scris) — un bug de alocare la pornire, nu de placă. De verificat în cod: cine mai
   folosește paginile 3db000–3fxxxx după pornire; soluție simplă: alocă buffer-ele RX/TX pe aceeași cale ca la repornire (după inițializarea
   completă a memoriei) și verifică printr-un test în QEMU că paginile nu sunt date de două ori.
2. **La rece:** secvența e scrisă și instrumentată bine; blocajul e accesul OCP/ERI (pașii 7, 9) și FIFO-urile care nu se golesc (pasul 3).
   De comparat exact cu FreeBSD `re(4)` / SerenityOS cum se face scrierea și citirea OCP (registrul, formatul comenzii, așteptarea bitului de gata).
3. **Rețeaua prin partajarea Windows merge** ca prin router: DHCP, DNS, HTTPS. E mediul de test de acum.
4. Noutățile din os-150 merg: `fetch` fără `run`, `host` cu „=”, contoarele.
