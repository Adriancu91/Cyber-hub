# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-10 23:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **S99 (gata 10 nov 22:05, verificat): STRICĂ.** Rețeta Muon (`rata_muon` 0,002 = ×400) pe modelul de 24 de straturi, din #554: după o oră
  română curat **1,2853** (pornire 1,2039), povești 0,4447, cod 0,7930 — peste praguri; oprire timpurie corectă, orele 2–5 nefăcute. R1 a rămas 99,20.
  Muon a folosit în antrenare ~1,1 GB mai puțin decât AdamW, dar vârful plăcii (6.492 MB) vine din examenul orei. **1343 teste trec.**
- **S95 (gata 10 nov 02:13): LA FEL** — modelul de 24, 5 ore AdamW 5e-6: română 1,2040 (#554, cel mai bun scor) vs #513 1,2060; câștigul doar din răcire.
- **Modelul în uz: #513** (98M, KGR1 Q8_0, 110.859.008 octeți, SHA `66f734b3…5859`); #477 și #459 rezerve. Model propriu, de la zero, fără LLM străin.
- S96: date pe bucăți (SHA identic pe 1,34 mld simboluri, 125 MB RAM); S93: examenul de română decide pe linia de 24; S94: modelul mic NU alege rata celui mare.

## Urmează
- **S100 (placa, noaptea 10→11, aprobat):** probă scurtă Muon cu pași de 20 de ori mai mici (`rata_muon` 0,0001) din #554, max 2 ore, oprire timpurie
  după ora 1; pre-înregistrare întâi; placa liberă cel târziu **05:30**. Întrebarea: strica S99 din cauza pașilor sau a metodei?
- **S98 (procesor, 11 nov de la 08:00):** legarea datelor pe bucăți în antrenare printr-un modul nou, neactivat.
- Dacă S100 nu mișcă modelul: continuările modelului crescut de 24 se închid; pasul următor = propunerea `idei/2026-11-10_kronos-mare-pe-ce-avem.md` (decizia lui Adrian).
- C-89 (tokenizer românesc): PARCAT până la >1 mld parametri.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu **#513** (suma, 3 texte de control). Rezervele #477 și #459 pornibile.
- Motorul de referință `unelte/inferenta_bruta.py`, modulul `inferenta`; nota automată în română + setul ascuns de 500 (`examen_romana`).
- Unelte: `date_bucati.py` (mmap + SHA pe bucată), `puncte_salvare.py` (listă + ștergere cu probă).
- Lecții: la un model crescut, rata mică strică cel mai puțin (S94); Muon cu pașii din rețeta de la zero strică un model deja antrenat (S99);
  `gc.collect()` înainte de `empty_cache()` eliberează memoria adunată între ore.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: în nopțile de antrenare Kronos ține placa de la 19:00; testele OS se anunță în `COMENZI.md`.
- De la `suita-office`: nimic acum.

## Blocaje / nevoie de Adrian
- Testul `os-278` e la Cyber Universe; noaptea asta placa e a lui Kronos până la 05:30 (S100), apoi liberă.
- Propunerea „Kronos mare pe ce avem” (P1: modelul de 24 de la zero cu Muon) — așteaptă „da/nu” (fără grabă).
- **S88:** ștergerea celor 82 de modele intermediare (33,4 GB) + `lucru/memorie_mare` — Adrian rulează comanda sau dă o excepție.
- Release-ul `kronos-kgr1-513` (cu Adrian la workstation). `claude setup-token` pe workstation, dacă expiră.
- Opțional: arhiva de mutare (26,2 GB) + Coșul; browserele deschise pe workstation țin ~200 MB pe placă.
