# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-01 11:55 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Direcția: fără LLM nicăieri; auto-joc cu verificator + specialiști + memorie;
  pe termen lung: Kronos dedicat pe cod și autodezvoltare.
- **Modelul în uz: #477** (română 1,2097), KGR1 Q8_0 110.859.040 octeți, SHA-256 `bcbe8187…3963`; #459 rezervă. `integrare/kronos/MODEL.md` arată #477.
- CCM pentru #477: procesor 1 fir 2,14 s/răspuns; **placa fp32 acceptată, 1,226 s (1,75× mai rapid)**, |Δ logit| 0,000155; placa 1,5 GB (S56).
- **Kronos-Cod (C-45 gata):** tokenizerul de cod (32.768 simboluri) BUN — 3,46 octeți/simbol (+22 % față de w2), refacere 100 % identică;
  setul de antrenare tokenizat: 1,08 mld simboluri; validare 5.686 fișiere ținute deoparte; examenul ascuns neatins.
- **S57 gata:** modulul de date pentru cod, examenul pe validare (biți/octet; pe datele reale = S55 exact), configurarea `cod_c1` (nepornită).
- **S59 gata:** modelul care citește direct simbolurile de cod + examenul pe ore (biți/octet, 1.000 fișiere fixe).
- **S60 gata:** proba „de la zero” + comanda care scrie răspunsurile pentru pass@k (setul ascuns închis). 1165 teste trec.
- **S58 pașii 1–2 gata:** pre-înregistrarea (înainte de probă) și proba de 10 minute: placa 6.078 MB, 63 °C, 32.364 simb/s.
  Observat: pierderea de pornire 474 (inițializarea implicită a încorporărilor).
- **S61 gata: AJUTĂ** — cu încorporările pornite mici (abaterea 0,02), pierderea de pornire 10,7 (în loc de 474) și după 10 minute 3,77 (în loc de 6,82); aceeași memorie (6.078 MB) și viteză. 1168 teste trec.

## Urmează
- **S58** (aprobat de Adrian, C-47; configurarea aleasă de Adrian, C-50): **cele 10 ore de antrenare: 1 nov de la 19:00, cu `cod_c1_init002`** (varianta S61), după fereastra OS/GPU dacă Adrian e la workstation. Pre-înregistrarea se actualizează înainte de pornire. Praguri neschimbate (biți/octet ≤ 1,10 și pass@10 ≥ 10/200).

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
- Pe 1 nov: dacă Adrian vine la workstation pentru fereastra OS/GPU, să spună când — antrenarea S58 pornește după fereastră.
- Opțional: excluderea mai îngustă propusă la S53; cauza repornirii din 29 oct (comanda din raportul S52).
- La ferestrele OS/GPU viitoare: antrenarea de pe placă să fie oprită întâi.
