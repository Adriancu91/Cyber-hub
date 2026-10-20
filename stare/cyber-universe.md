# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-20 22:40 (ora României) · **de:** sesiunea programată a OS-ului (20:40), cu acces la hub

## Acum
- Fazele 1, 2 și 4 închise; Faza 3 gata în emulator (lipsește doar testul pe un calculator real).
- Interfață grafică: desktop „Cyber Universe” care pornește singur, ferestre, aplicații (Terminal, Fișiere, Editor,
  Monitor, Setări, Module), tastatură românească, module instalabile din interfață.
- Rețea (Faza 5, azi): adresă automată (DHCP), nume → adresă (DNS), conexiuni TCP sigure (pachetele pierdute se
  retrimit), comenzile `ping`, `host`, `http` în shell; programele pot folosi rețeaua (`fetch`, `udp`) și există
  aplicația grafică **Rețea** (adresă, rută, DNS, ping).
- 39 de scenarii de test automate trec; CI verde.

## Urmează
- P5-06: HTTPS (pagini web securizate) — după „da”-ul lui Adrian la întrebarea de mai jos.
- P3-09 / P3-10: testul pe un calculator real, când Adrian trimite pozele.
- P5-07 / P5-08: suita office și Kronos ca module în OS — după ce suita își atinge ținta.

## Ce oferă proiectul celorlalți
- Infrastructura de test pe scenarii (`tests/scenarios.txt` + `tools/test.sh`, cu servere de test pornite automat).
- Formatul comun de modul (`standarde/modul-v0.md`) e folosit în `modules/` și `apps/`.

## De ce are nevoie de la ceilalți
- Nimic acum. (Testul pe stick se face pe alt calculator, nu pe ThinkPad-ul suitei.)

## Blocaje / nevoie de Adrian
- **Întrebare (B-002 / P5-06):** criptografia pentru HTTPS o scriem noi, după standardele publice, verificată cu
  exemplele oficiale (fără audit făcut de specialiști în securitate)? Recomandarea: **da**, e în spiritul deciziei
  din 19:40 („de la zero, fără alte licențe”). Răspuns „da” sau „nu” ajunge.
- **B-001 / P3-09:** testul pe un calculator real — imaginea de pe stick (pașii în `docs/USB.md` din repo-ul OS),
  pornire de pe stick, poze cu ecranul. P3-10 așteaptă după el.
- **B-003 / P5-07:** suita office ca modul — mai târziu, după ce suita e gata; nu e nevoie de nimic acum.
