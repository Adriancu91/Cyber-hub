# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-28 11:20 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- Cel mai bun model: **#459** (română 1,2162; mai mic = mai bine). **Rulează în Cyber Universe OS cu exact aceleași simboluri ca referința** (os-195, workstation).
- **S40 gata (28 oct, cu Adrian de față):** porturi **opționale** noi în nucleu, `cautare` și `inferenta` (configurările vechi neschimbate),
  plus modulele `CautareE3` și `InferentaKGR1`; 979 teste trec. Fișele comune: `module/manifeste/cautare_e3.toml`, `inferenta_kgr1.toml` (în cyberspace).
- **S42** (cititorul E3 refăcut din #459 cu rețeta A) a fost întreruptă după ora 1 de repornirea pentru fereastra OS/GPU; fără verdict.
  Se reia **de la zero** azi după 12:15 (altfel la 19:00), cu aceleași praguri scrise dinainte.

## Urmează
- Verdictul S42 (CONFIRMAT dacă răspunde corect la ≥ 5 întrebări mai mult din 100 decât cititorul de azi, #438, fără să piardă în altă parte).
- S41 (procesor): Kronos-Cod etapa 1a — lista surselor de cod cu licențe, examenul de cod scris înainte, cutia izolată (fără descărcări).

## Ce oferă proiectul celorlalți
- Pachetul KGR1 în `integrare/kronos/` (specificație, tokenizer, vectori, `MODEL.md`) — confirmat pe hardware real de `cyber-universe`.
- Motorul de referință `unelte/inferenta_bruta.py` și acum modulul `inferenta` cu același rezultat (egalitate exactă a logit-urilor):
  bun ca reper pentru profilul de viteză din C-29 (aceleași simboluri trebuie să rămână).
- Căutare în text pe procesor (FTS5 + BM25 + rădăcini + RRF), acum ca modul `cautare`; `verifica_text(text)`; verificatorul de răspunsuri.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: viteza după C-29 (simb/s pe 1 fir și pe toate nucleele, pe #459) — fără grabă, nu blochează nimic la Kronos.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- Opțional: Release-ul privat `kronos-kgr1-459` (o comandă `gh release create …` pe workstation, exactă în `plan/pentru_adrian.md`);
  OS-ul nu mai e blocat (modelul a fost copiat pe stick), dar Release-ul păstrează fișierul cu suma lui.
- La ferestrele OS/GPU viitoare: antrenarea de pe placă să fie oprită întâi (azi s-a pierdut ~1,5 ore de placă).
