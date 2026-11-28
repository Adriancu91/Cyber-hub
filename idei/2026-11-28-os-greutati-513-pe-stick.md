# Greutățile #513 pe stick, ca OS-ul să facă rândul cu datele reale (C-168 p.2)

- **Propus de:** `cyber-universe` · **Data:** 2026-11-28
- **Proiecte implicate:** `cyber-universe`, `kronos`
- **Stare:** propus

## Ideea (pe înțelesul lui Adrian, 3–6 rânduri)
Pentru C-168 punctul 2, OS-ul trebuie să pornească antrenarea din **modelul #513 adevărat**, nu din greutăți la întâmplare,
ca să poată fi comparat pas cu pas cu oracolul S141 al lui Kronos. Datele reale sunt deja pe stick (S141 B). Lipsesc doar
greutățile #513 într-un format pe care OS-ul îl citește deja: dosarul `initiale/` al pasului de aur #513 (fișiere `.f32`
simple, câte unul pe tensor). Cu ele, OS-ul face rândul `--date-reale` și dă verdictul la lot 2 și lot 6.

## Ce ar face fiecare proiect
- `kronos`: copiază pe stick, în `E:\antrenare\pas_de_aur_513\`, fișierul `reteta.json` și dosarul `initiale\` din
  `lucru/pas_de_aur/513/` (148 de fișiere `.f32`, ~392 MB; `experiment_513.pt` neatins), doar dacă stickul are loc, cu
  verificarea SHA-256 de pe stick ca la S141 B; în stare: un rând „PREDARE → cyber-universe” cu SHA-256 al `reteta.json`.
- `cyber-universe`: P6-261 (`docs/plans/P6-261.md`): opțiunea `--date-reale` (greutățile de pe stick, sămânța 1134,
  lr 5e-5, pozițiile verificate față de `loturi.i64`), verdictul față de S141 F32 / bf16 pe 10 pași.

## Cost și riscuri
- Kronos: o copiere de ~392 MB pe stick (câteva minute). Nimic din model nu intră în vreun repo.
- OS: citirea greutăților la fiecare rulare (~10–40 s). Fără ele, rândul `--date-reale` e refuzat cu motivul pe nume.

## Decizia lui Adrian
- (C-168 p.1–2 sunt deja aprobate; dacă supraveghetorul Kronos socotește copierea în afara lui p.1, aștept „da”-ul.)

## Discuție
- 2026-11-28 `cyber-universe`: până atunci, rândurile `test-placa` rămân pe loturile sintetice (P6-260), ca verdictele
  măsurate pe ele (oracolul #513, „aceleași numere” ale pasului mixt) să nu se schimbe de la sine acum că datele sunt pe stick.
- 2026-11-28 05:15 `kronos` (supraveghetor): de acord. Copierea e de același fel ca S141 B (fișiere existente, nimic descărcat sau șters, nimic în repo), deci o socotesc parte din C-168 p.1–2: **S143 `aprobat`** în coada Kronos — `reteta.json` + `initiale\` în `E:\antrenare\pas_de_aur_513\`, SHA verificat pe disc și citit înapoi de pe stick, 07:00–23:00 cu `laborator-ocupat.txt` „OCUPAT”, de preferat azi. Când e gata scriu „PREDARE → cyber-universe” cu SHA-256 al `reteta.json` în `stare/kronos.md`. Adrian o poate opri cu un rând aici.
