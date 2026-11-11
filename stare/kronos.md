# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-11 08:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **S100 (gata 11 nov 02:01, verificat): LA FEL.** Muon cu pași de 20 de ori mai mici (`rata_muon` 0,0001) pe modelul de 24, din #554, 2 ore:
  română curat **1,2055** (pornire 1,2039; ora 1: 1,2057), povești 0,4047, cod 0,7246, R1 99,20 / 100 — nu strică, nu mișcă. Placa max 6.277 MB / 63 °C.
- Raportul de dimineață (11 nov 06:47): S99 STRICĂ, S100 LA FEL, 1343 teste trec, placa liberă (476 MB / 28 °C).
- **Concluzie:** la S99 (STRICĂ) vina era a pașilor prea mari. Modelul **crescut** de 24 nu se mai mișcă la nicio rețetă de continuare
  (AdamW ×0,5…×4, Muon ×400, Muon ×20) → continuările lui sunt închise.
- **Modelul în uz: #513** (98M, KGR1 Q8_0, 110.859.008 octeți, SHA `66f734b3…5859`); #554 cel mai bun la română (1,2040); #477 și #459 rezerve.
  Model propriu, de la zero, fără LLM străin.

## Urmează
- **S98 (procesor, în lucru din 11 nov 08:00, ~2–3 h):** legarea datelor pe bucăți în antrenare printr-un modul nou, neactivat. Placa nefolosită.
- **S101 (placa, propus — necesită Adrian):** P1 din `idei/2026-11-10_kronos-mare-pe-ce-avem.md` — modelul de 24 de straturi **de la zero**
  (Muon, rețetă completă), ~7 nopți lungi. Fără „da”, placa nu primește altă sarcină de la Kronos.
- C-89 (tokenizer românesc): PARCAT până la >1 mld parametri.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu **#513** (suma, 3 texte de control). Rezervele #477 și #459 pornibile.
- Motorul de referință `unelte/inferenta_bruta.py`, modulul `inferenta`; nota automată în română + setul ascuns de 500 (`examen_romana`).
- Unelte: `date_bucati.py` (mmap + SHA pe bucată), `puncte_salvare.py` (listă + ștergere cu probă).
- Lecții: un model „crescut” se așază lângă modelul din care a crescut; Muon pe model gata antrenat merge doar cu pași mici și atunci nu ajută.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: testele OS pe workstation se anunță în `COMENZI.md` (până la un „da” la S101, placa e liberă noaptea).
- De la `suita-office`: nimic acum.

## Blocaje / nevoie de Adrian
- **„Da/nu” la P1 / S101** (modelul de 24 de la zero, ~7 nopți) — dacă vine până pe la 18:00, poate porni la noapte.
- Testul `os-278` e la Cyber Universe; placa e liberă (S98 folosește doar procesorul). Workstation-ul a repornit pe 10 nov ~23:15 (fără pagube) — de confirmat de Adrian dacă a fost el.
- **S88:** ștergerea celor 82 de modele intermediare (33,4 GB) + `lucru/memorie_mare` — Adrian rulează comanda sau dă o excepție. Discul C: 91 %.
- Release-ul `kronos-kgr1-513` (cu Adrian la workstation). `claude setup-token` pe workstation, dacă expiră.
