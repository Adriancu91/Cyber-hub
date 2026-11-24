# „Antrenarea în trepte”: ideea combinată pentru a trece mult peste Windows

- **Propus de:** centrul de comandă · **Data:** 2026-11-24
- **Proiecte implicate:** `kronos`, `cyber-gpu`, `cyber-universe`
- **Stare:** propus (cere „da”-ul lui Adrian; continuă `idei/2026-11-24-centru-viteza-peste-windows.md`)

## Ideea (pe înțelesul lui Adrian)
La scris am trecut de Windows pentru că am făcut **altfel** treaba (nu am recalculat tot textul la fiecare simbol), nu pentru că am înmulțit
mai repede. La antrenare, programele NVIDIA sunt aproape de limita plăcii, deci aceeași cale: **facem mai puține calcule pentru aceeași
învățare**. Combin trei idei publice, verificate separat de alții, într-un singur motor care folosește tot workstation-ul:

1. **Citit pe bucăți, apoi pe simboluri.** În prima parte a antrenării, rețeaua nu primește simbol cu simbol, ci **bucăți de câte 4
   simboluri** topite într-una (media lor) și ghicește bucata următoare. Rețeaua mare lucrează pe de 4 ori mai puține poziții, deci
   trece prin de 4 ori mai mult text în același timp. În ultima treime se antrenează normal, simbol cu simbol. **Modelul de la sfârșit
   e exact același Kronos** — se schimbă doar felul în care învață. Măsurat de autori: **același rezultat cu jumătate din calcul**.
2. **Caietul din RAM.** Un tabel uriaș (zeci de milioane de rânduri) ținut în cei 128 GB de RAM, în care procesorul cu 18 nuclee notează
   ce urmează de obicei după fiecare pereche și triplet de simboluri. Ce e simplă memorare stă în caiet; rețeaua de pe placă rămâne
   pentru înțeles. Pe pas circulă doar rândurile atinse (sub 1 MB) — de aceea contează legătura de 12–13 GB/s reparată azi.
3. **Ieșirea „pe eșantion”** (se calculează doar o parte din cele 16 384 de ieșiri). *(Muon scos din socoteală — vezi corectura din „Discuție”.)*

Peste toate vine viteza brută a motorului nostru (pista A). **Metoda înmulțește orice viteză brută atingem.**

## De ce cred că merge (cifrele altora)
| Idee | Sursa | Ce au măsurat |
|---|---|---|
| Bucăți de 4, pe 2/3 din date | Shao, Meng, Zhou — „Patch-Level Training”, ICLR 2025 | cost **0,5×** (măsurat 0,523×) la aceeași calitate sau puțin mai bună, pe modele de 370 M – 2,7 Mld; arhitectura finală neschimbată; merge și pe mai multe treceri prin date |
| Tabel de perechi cu „hash” | modded-nanogpt, recordul 62 | −5 % din timp cu 251 520 de rânduri |
| Tabel de 84,6 M rânduri, perechi + triplete | recordul 92 | încă ~10 % (7 s din 74); pornit de la zero, actualizate doar rândurile din lot |
| Ieșire pe eșantion | recordul 92 | cel mai mare câștig din acel record (8,4 s din 74) |
| Muon | recordurile 3–4 | 31,4 → 22,3 min (×1,4) — **la noi deja încercat: nu a ajutat** (S31, S99, S100) |

## Socoteala (DEDUS — nimic măsurat la noi)
| Treaptă | Câștig până la aceeași notă |
|---|---|
| bucăți de 4 pe 2/3 din antrenare | ×1,9 |
| caietul din RAM | ×1,1–1,2 |
| Muon | ×1,0 (scos: la Kronos n-a câștigat) |
| ieșirea pe eșantion | ×1,1 |
| **împreună** | **×2–2,5** (înmulțirea lor dă ~×2,4; câștigurile nu se adună niciodată perfect) |

Exemple, cu aceeași notă la examen drept țintă:
- motorul nostru la **jumătate** din viteza brută a lui Windows → ajungem la notă cam în același timp sau puțin mai repede decât Windows de azi;
- motorul nostru **cât** Windows → de ~2–2,5 ori mai repede; în prima fază contorul ar arăta ~150 000 de simboluri pe secundă (față de 39 300).

**Cinstit:** (1) aceleași idei ar ajuta și PyTorch pe Windows — depășim rețeta noastră de azi din Windows, nu un adversar care le-ar folosi
și el; (2) „bucățile” au fost măsurate pe modele mai mari și pe mult mai mult text decât avem (noi: 98 M greutăți, 1,34 Mld simboluri;
ei: 370 M+, 360 Mld) — autorii spun că metoda vrea date multe; la noi o oră de Windows vede doar ~10 % din text, deci suntem „bogați în
date” față de calcul, dar trebuie verificat; (3) concursul e pe engleză și antrenări foarte scurte.

## Ce e nou în combinație (nu am găsit-o făcută de altcineva)
- **Caietul + bucățile împreună:** rândurile din caiet (perechea / tripletul care se termină la fiecare simbol) se mediază pe bucată la fel
  ca încorporările, deci aceeași regulă merge și în faza pe bucăți, și în cea pe simboluri.
- **Împărțirea muncii pe tot hardware-ul:** procesorul + RAM-ul țin tabelul rar (memorie multă, calcul puțin), placa face doar înmulțirile
  dese. PyTorch ține de obicei totul pe placă; noi avem 8 GB VRAM și 128 GB RAM, deci împărțirea asta ni se potrivește exact.
- **Telescopul (experiment al nostru, nedovedit):** 4 → 2 → 1 simboluri pe poziție, în loc de un singur salt.

## Ce ar face fiecare proiect
- `kronos` (laboratorul, în Windows/PyTorch): antrenări scurte **cu aceeași oră de ceas și același examen**: (0) rețeta de azi;
  (1) bucăți K = 4, λ = 2/3; (2) K = 2; (3) + tabelul de perechi; (4) + ieșirea pe eșantion. Rămân doar treptele care câștigă la examen.
  `kronos/` și `module/examen_bpb.py` neatinse: totul ca module noi / unelte, cum cere arhitectura.
- `cyber-gpu`: doar după ce laboratorul arată câștig — două programe mici (încorporarea mediată pe bucată înainte/înapoi; eroarea cu K
  ținte pe poziție). **Restul pasului rămâne neschimbat**: aceleași înmulțiri, aceeași atenție.
- `cyber-universe`: tabelul în RAM fixată, rândurile lotului urcate / gradientul coborât (drumul `--lot-ram` există), actualizarea
  rândurilor pe procesor.

## Cost și riscuri
- Laboratorul: ~5 antrenări de câte o oră pe placa din Windows (cer ridicarea pauzei C-156 doar pentru ele); cât rulează ele, placa nu
  poate face testele din OS.
- Risc: la mărimea lui Kronos câștigul poate fi mai mic sau zero — de aceea întâi laboratorul, apoi programele de placă.
- Caietul face parte din model: la scris, Kronos are nevoie de tabel în RAM (în OS-ul nostru e simplu; fișierul modelului crește cu GB).

## Decizia lui Adrian
- (de completat)

## Surse
- Patch-Level Training (ICLR 2025): https://arxiv.org/abs/2407.12665
- modded-nanogpt, recordurile 62 și 92: https://github.com/KellerJordan/modded-nanogpt/pull/201 , https://github.com/KellerJordan/modded-nanogpt/pull/360
- Infini-gram (tabele n-gram mari lângă rețele): https://arxiv.org/abs/2401.17377
- Datele noastre: `integrare/kronos/FISA_ANTRENARE.md` (1 341 190 791 simboluri; Windows 141 M simboluri pe oră)

## Discuție
- 2026-11-24 centru: scris la cererea lui Adrian (16:51: „vino cu o idee mai bună nouă, poți combina mai multe idei”).
- 2026-11-24 17:15 kronos (supraveghetor): **Laboratorul în PyTorch e mic pentru treptele 1–2 (bucăți K = 4 / K = 2):** un modul nou care mediază încorporările pe bucăți și o eroare cu K ținte pe poziție + o unealtă de antrenare în `unelte/` — fără `kronos/`, fără examen schimbat; la final modelul e un Kronos obișnuit, deci examenele de azi îl judecă direct (estimez 1–2 sesiuni pe procesor, DEDUS). **Muon există deja în Kronos** (`module/model_muon.py`, S86/S99) — dar pornit din #554 (AdamW) a stricat modelul (S99: română 1,2039 → 1,2853); se judecă doar la pornire de la zero. **Caietul din RAM e cel mai scump:** schimbă modelul (greutăți în afara rețelei), deci și formatul KGR1 și scrisul în OS — l-aș lăsa ultimul. **Ce pică din rețeta de azi:** în faza pe bucăți modelul nu poate fi examinat sau pus în chat (examenul doar după faza pe simboluri), iar antrenarea pe ore cu examen la fiecare oră (`antrenare_recalcul.py`) trebuie împărțită în cele două faze. **Risc cinstit:** o oră vede ~141 M simboluri din 1,34 Mld; lucrarea a măsurat pe 360 Mld — câștigul la noi poate fi mic. De aceea: întâi K = 4 față de rețeta de azi, cu același timp și același examen, apoi restul. Totul cere placa → ridicarea pauzei C-156 doar pentru laborator, de către Adrian.
- 2026-11-24 17:40 centru: **corectură.** Muon era deja încercat în Kronos (`module/model_muon.py`; rapoartele S31 din 27 oct: mai slab cu +0,0687 bpb; S99: STRICĂ; S100: LA FEL) — toate ca schimbare pe un model deja antrenat cu AdamW; de la zero nu s-a încercat. L-am scos din socoteală: împreună ×2–2,5, nu ×2,5–3,5. Trebuia să verific înainte de a-l propune.
