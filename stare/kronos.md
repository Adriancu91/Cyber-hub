# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-13 02:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **S107 gata, verificat: LA FEL → #513 rămâne.** Unealta nouă de renotare numără corect refuzul cinstit la întrebările-capcană (#513 1 → 16, #554 0 → 16 din 20), dar modelele refuză și 46–49 din 50 de întrebări știute → examenul de conversație fără text nu le desparte. Pentru modelul în uz contează examenele „răspuns din text” (S106: 81 față de 80 din 140).
- Întrebarea #554 față de #513 e închisă. Slăbiciunea comună: tipurile de întrebări nevăzute la antrenare (11–13 din 50; la „actori”, „profesie”, „canal”, „câștigător” 0).
- Noaptea 12→13: nimic pe placă.
- **Modelul în uz: #513** (98M, KGR1 Q8_0, 110.859.008 octeți, SHA `66f734b3…5859`); #554 cel mai bun la română (1,2040); #477 și #459 rezerve.
  Model propriu, de la zero, fără LLM străin.

## Urmează
- **S108 (13 nov de la 08:00, doar procesor, doar citire, aprobat de supraveghetor):** câte exemple din fiecare tip de întrebare a văzut linia modelului în uz și câte s-ar putea face din datele deja descărcate pentru tipurile slabe — cifre pentru alegerea lui Adrian. Nimic antrenat.
- Direcția următoare (decizia lui Adrian): S101 (24 de straturi de la zero, ~7 nopți, „nu deocamdată” din C-101) sau mai multe tipuri de întrebări pe linia modelului în uz. C-89 (tokenizer românesc): PARCAT.
- 13 nov dimineață: verificarea prin citire a ștergerii C-112 (în raportul de dimineață).

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu **#513** (suma, 3 texte de control). Rezervele #477 și #459 pornibile.
- Motorul de referință `unelte/inferenta_bruta.py`, modulul `inferenta`; nota automată în română + setul ascuns de 500 (`examen_romana`).
- Unelte pentru date mari cu RAM mic: `bucati_din_text.py` (text → bucăți, cu reluare), `date_bucati.py` + modulul `date_bucati` (mmap + SHA pe bucată); legate în antrenare și dovedite pe placă (S103 + S104 DA) — antrenări pe date mult mai mari fără 42 GB RAM.
- Lecții: un model „crescut” se așază lângă modelul din care a crescut; Muon pe model gata antrenat merge doar cu pași mici și atunci nu ajută. Unealta `renoteaza_conversatie.py` (refuzul „Nu scrie în text.” numărat corect).

## De ce are nevoie de la ceilalți
- De la centrul de comandă: nota în `COMENZI.md` când Adrian vine iar la workstation pentru testele OS/GPU (os-295), ca Kronos să elibereze placa.
- De la `suita-office`: nimic acum.

## Blocaje / nevoie de Adrian
- Niciun blocaj.
- De la Adrian, fără grabă: alegerea direcției (S101 de la zero sau mai multe tipuri de întrebări pe #513).
- Fără grabă: `lucru\memorie_mare` (~10,5 GB), pe care Adrian îl șterge de mână.
- Release-ul `kronos-kgr1-513` (cu Adrian la workstation). `claude setup-token` pe workstation, dacă expiră.
