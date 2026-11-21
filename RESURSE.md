# Resursele: cine lucrează unde

Ca agenții să nu se calce pe picioare: fiecare calculator și fiecare fereastră orară are un singur stăpân.
Altcineva o folosește doar cu o rezervare de mai jos, aprobată de Adrian.

## Calculatoare
| Resursă | Stăpân | Cine lucrează acolo | Reguli |
|---|---|---|---|
| Workstation-ul Kronos (calculatorul de la firmă, placa video) — Kronos lucrează (E2) și cât e Adrian plecat; fereastră OS/GPU la întoarcere | `kronos` | executantul Kronos (Claude Code), la fiecare 30 de minute | **de la 19 nov 2026 22:33 vezi „Workstation: ferestre” mai jos** (testele driver/OS au întâietate; Kronos antrenează în ferestrele rămase); inventarul K0 din Windows (doar citire) e permis oricând |
| Laptopul lui Adrian (ThinkPad L15) — rezervat suitei până își atinge ținta (~1–2 săptămâni de la 20 oct) | `suita-office` | sesiunile Claude Code ale suitei, pornite de sarcina locală „Suite – lucru continuu” (verifică la 5 minute) | doar suita; repornirea laptopului (de ex. pentru stick-ul OS) doar cu rezervare |
| Cloud (sesiuni programate) | toate | supraveghetorul Kronos (la :15), Cyber Universe OS (la :40), coordonatorul hub-ului | fiecare lucrează doar în repo-ul lui + fișierele lui din hub |

## Workstation: placa video (decizia lui Adrian, 21 nov 2026 08:01 — înlocuiește ferestrele din 19 nov)
| Când | A cui e placa | Reguli |
|---|---|---|
| **La orice oră, zi și noapte** | **testele Cyber-GPU / Cyber Universe** (ciclul automat C-143, pornit doar de centrul de comandă prin paznicul de pe workstation) | Un singur test o dată; un test ține ~10–15 minute (Windows → stick → test → Windows). Cheile lui Adrian de pe stick și butonul `C:\Kronos\cyber-test\STOP` rămân stăpâne. |
| — | **Kronos: pe pauză** (C-156) | Nicio antrenare pe workstation până la o decizie nouă a lui Adrian. Chat-ul cu #651 rămâne pornit. Lucrul mic pe procesor (exporturi, „pasul de aur”) e voie oricând; un test îl poate întrerupe prin repornire, deci se face în bucăți care se pot relua. |

## Coada testelor pe placă (o ține centrul de comandă; un singur lucru nou pe test)
| Nr. | Versiunea | Ce e nou | Rândul din `auto\teste.txt` | Stare |
|---|---|---|---|---|
| 1 | `os-323` | tabloul de bord al plăcii (temperatură, ceasuri, stare) | `test-placa --tablou` | **făcut 21 nov 08:21 — merge** (35,8 °C, P8, 25 W; oprirea zonei refuzată) → `rezultate/2026-11-21-workstation-os323-tablou/` |
| 2 | `os-323` | proba de reset din interior (FLR) | `test-placa --flr-proba` | **făcut 21 nov 08:32 — merge** (placa răspunde după 0,13 s; al doilea lanț trece toți pașii) → `rezultate/2026-11-21-workstation-os323-flr/` |
| 3 | `os-324` | „dieta driverului” (C-154) | `test-placa` | **făcut 21 nov 11:01 — merge** (driverul 3 081 → 1 347 µs; 109 simb/s, mediana 245) → `rezultate/2026-11-21-workstation-os324-dieta/` |
| 4 | `os-328` | calculele lipite (P3) | `test-placa --lipit` | **făcut 21 nov 12:56 — merge** (simbolul median 3 284 µs = 304,5 simb/s; media 120 din cauza a 2 poziții lente) → `rezultate/2026-11-21-workstation-os328-p3/` |
| 4b | `os-329` | fără scriere pe stick în mijlocul generării (P6-112) + lista lipită implicită | `test-placa` | **făcut 21 nov 15:56 — merge: media 262 simb/s, de 2 ori Windows/PyTorch (129)** → `rezultate/2026-11-21-workstation-os329-pozitii/` |
| 4c | `os-331` | LayerNorm nou (P6-114) | `test-placa --ln-nou` | **făcut 21 nov 17:26 — merge: media 348 simb/s (a doua rulare), LayerNorm ~4 µs** → `rezultate/2026-11-21-workstation-os331-ln/` |
| 4d | `os-332` | poziția 0 — încălzirea (P6-116) | `test-placa --ln-nou` | **făcut 21 nov 19:16 — merge: nicio poziție lentă; media 351 simb/s (LayerNorm nou), de 2,7 ori Windows** → `rezultate/2026-11-21-workstation-os332-pozitia0/` |
| — | `os-328` | **proba agentului viu** (C-159 pasul 1; doar citiri + refuzuri; nu atinge placa) | `live 10`, apoi `live 2` | **făcut 21 nov 13:03 și 13:18 — trecută** (61 de comenzi, zero abateri) → `rezultate/2026-11-21-workstation-agentul-viu-proba/`; sesiunea C după reparația `live.cheie` secret |
| 5 | următorul | Kronos #651 pe placă (P6) | de stabilit de sesiunea OS | după 3–4 |
| 6 | de anunțat | **P8 — primul calcul cu circuitele speciale** (aprobat de Adrian, 21 nov 16:18) | de anunțat de sesiunea OS | așteaptă PREDARE Cyber-GPU (C-160 p.1) → Release OS (C-161 p.2) |
| 7 | de anunțat | **prima comandă pe placă din modul viu** (`test-placa` trimis prin canalul viu; cheia e pe stick din 16:12) | `live 10` + comanda trimisă de centrul de comandă | așteaptă Release-ul OS cu comanda de placă a modului viu (C-161 p.1); test separat, anunțat lui Adrian |
| 7b | de anunțat | **P7 — lanțul pe placă**, treptele 1, 2, 3 (aprobat de Adrian, 21 nov 16:27; fiecare treaptă = test separat) | de anunțat de sesiunea OS | după poziția lentă, P8 și predările în așteptare; așteaptă predările Cyber-GPU pe trepte |
| 8 | mai târziu | **motorul de antrenare:** un program „înapoi” singur, apoi „pasul de aur” al modelului mic | de anunțat de sesiunea OS | C-160 / C-161; antrenarea adevărată (ore) doar cu decizia nouă a lui Adrian |
Sesiunea OS anunță o versiune gata prin rândul `GATA DE TEST:` din `stare/cyber-universe.md`; centrul de comandă o trece aici.

## Program în cloud (ora României)
| Sesiune | Când |
|---|---|
| Kronos supraveghetor | 02:15, 05:15, 08:15, 11:15, 14:15, 17:15, 20:15, 23:15 |
| Cyber Universe OS (de la 21 nov 2026 14:23: de două ori pe oră, cu semnul „în lucru”) | în fiecare oră, la :10 și la :40 |
| Cyber-GPU (de la 21 nov 2026: din oră în oră, cu semnul „în lucru”; 19–21 nov: 8 pe zi) | în fiecare oră, la :10 |
| Coordonatorul hub-ului (rescrie PANOU.md) | 08:50, 14:50, 20:50 |
| Centrul de comandă (citește hub-ul, pune versiunile pe stick, pornește testele, răspunde la întrebări) | ziua din oră în oră, noaptea la două ore |

## Rezervări (doar cu „da”-ul lui Adrian)
| Când | Resursă | Pentru | Motiv | Aprobat |
|---|---|---|---|---|
| _(niciuna)_ | | | | |

## Cereri care așteaptă
- Niciuna. Testul OS-ului pe stick (B-001 / P3-09) se face pe **alt calculator**, nu pe ThinkPad (decizia lui Adrian, 20 oct 21:37);
  suita nu se oprește. Adrian îl face când are timp, posibil pe 21 oct.
