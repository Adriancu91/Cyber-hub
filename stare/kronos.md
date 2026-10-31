# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-10-31 20:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- **Modelul în uz: #477** (română 1,2097), KGR1 Q8_0 110.859.040 octeți, SHA-256 `bcbe8187…3963`; #459 rezervă. `integrare/kronos/MODEL.md` arată #477.
- CCM pentru #477: procesor 1 fir 2,14 s/răspuns; **placa fp32 acceptată, 1,226 s (1,75× mai rapid)**, |Δ logit| 0,000155; placa 1,5 GB (S56).
- **Kronos-Cod (C-45 gata):** tokenizerul de cod (32.768 simboluri) BUN — 3,46 octeți/simbol (+22 % față de w2), refacere 100 % identică;
  setul de antrenare tokenizat: 1,08 mld simboluri; validare 5.686 fișiere ținute deoparte; examenul ascuns neatins.
- **S57 gata:** modulul de date pentru cod, examenul pe validare (biți/octet; pe datele reale = S55 exact), configurarea `cod_c1` (nepornită).
- 1145 teste trec. Placa liberă.

## Urmează
- **S59** (aprobat, doar procesor): un model nou care citește direct simbolurile de cod + un examen nou pe ore (biți/octet), fără să atingă #477, examenul oficial sau nucleul. Fără el, S58 s-ar opri la pornire.
- **S58** (propus — necesită Adrian; după S59): prima antrenare `cod_c1`, o noapte de 10 ore, ~110M parametri, de la zero; praguri scrise dinainte (biți/octet ≤ 1,10 și pass@10 ≥ 10/200).

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu #477 (suma, cele 3 texte de control, marjele). Reper de viteză pe Windows pentru #477: 1 fir ~2,14 s / răspuns de 64 simboluri, placa fp32 ~52 simb/s.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice).
- Un tokenizer pentru cod (Python/Rust/C), care păstrează indentarea ca simboluri întregi — util dacă OS-ul va rula vreodată Kronos-Cod.
- Căutare în text pe procesor, verificatorul de răspunsuri, cutia izolată pentru cod netestat, un set de cod curat cu proveniență pe fișier.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: după ce #477 e pe stick, simbolurile identice cu cele 3 texte din `MODEL.md` și viteza pe 1 fir (simb/s) — fără grabă.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- **Release-ul privat `kronos-kgr1-477`** (executantul n-are voie la `gh`; fără el OS-ul nu are fișierul pentru stick). Pe workstation, în PowerShell, din `C:\Kronos\cyberspace`:
  `gh release create kronos-kgr1-477 lucru/export/kronos_477_q8_0.kgr lucru/export/kronos_477_q8_0.kgr.sha256 --repo Adriancu91/cyberspace --title "Kronos #477 KGR1 Q8_0" --notes "SHA-256 bcbe8187087dbb3e531a8a7b10991cd24ea14a6e067d07c0fcbb8d3edd753963, 110859040 octeți"`
- **„da S58”** pentru prima antrenare Kronos-Cod pe placă (linie de model nouă).
- Opțional: excluderea mai îngustă propusă la S53; cauza repornirii din 29 oct (comanda din raportul S52).
- La ferestrele OS/GPU viitoare: antrenarea de pe placă să fie oprită întâi.
