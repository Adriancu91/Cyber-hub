# Resursele: cine lucrează unde

Ca agenții să nu se calce pe picioare: fiecare calculator și fiecare fereastră orară are un singur stăpân.
Altcineva o folosește doar cu o rezervare de mai jos, aprobată de Adrian.

## Calculatoare
| Resursă | Stăpân | Cine lucrează acolo | Reguli |
|---|---|---|---|
| Workstation-ul Kronos (calculatorul de la firmă, placa video) — Kronos lucrează (E2) și cât e Adrian plecat; fereastră OS/GPU la întoarcere | `kronos` | executantul Kronos (Claude Code), la fiecare 30 de minute | **de la 19 nov 2026 22:33 vezi „Workstation: ferestre” mai jos** (testele driver/OS au întâietate; Kronos antrenează în ferestrele rămase); inventarul K0 din Windows (doar citire) e permis oricând |
| Laptopul lui Adrian (ThinkPad L15) — rezervat suitei până își atinge ținta (~1–2 săptămâni de la 20 oct) | `suita-office` | sesiunile Claude Code ale suitei, pornite de sarcina locală „Suite – lucru continuu” (verifică la 5 minute) | doar suita; repornirea laptopului (de ex. pentru stick-ul OS) doar cu rezervare |
| Cloud (sesiuni programate) | toate | supraveghetorul Kronos (la :15), Cyber Universe OS (la :40), coordonatorul hub-ului | fiecare lucrează doar în repo-ul lui + fișierele lui din hub |

## Workstation: ferestre (decizia lui Adrian, 19 nov 2026 22:33)
| Fereastră | A cui e placa | Reguli |
|---|---|---|
| Ziua, 08:00–18:00 | **testele Cyber-GPU / Cyber Universe** (ciclul automat C-143, pornit de centrul de comandă prin paznicul de pe workstation) | Kronos nu pune sarcini de placă în această fereastră. Un test ține ~10–15 minute (Windows → stick → test → Windows). |
| Noaptea, 19:00–07:00 | **Kronos** (antrenări, ca workstation-ul să nu stea degeaba) | placa liberă la 07:00. Dacă un test de driver/OS are nevoie de o noapte, centrul de comandă scrie o rezervare mai jos și Kronos sare peste noaptea aceea. |
| 07:00–08:00 și 18:00–19:00 | nimeni (tampon) | timp pentru oprirea curată a antrenării / întoarcerea în Windows. |

## Program în cloud (ora României)
| Sesiune | Când |
|---|---|
| Kronos supraveghetor | 02:15, 05:15, 08:15, 11:15, 14:15, 17:15, 20:15, 23:15 |
| Cyber Universe OS | 02:40, 05:40, 08:40, 11:40, 14:40, 17:40, 20:40, 23:40 |
| Coordonatorul hub-ului (rescrie PANOU.md) | 08:50, 14:50, 20:50 |

## Rezervări (doar cu „da”-ul lui Adrian)
| Când | Resursă | Pentru | Motiv | Aprobat |
|---|---|---|---|---|
| _(niciuna)_ | | | | |

## Cereri care așteaptă
- Niciuna. Testul OS-ului pe stick (B-001 / P3-09) se face pe **alt calculator**, nu pe ThinkPad (decizia lui Adrian, 20 oct 21:37);
  suita nu se oprește. Adrian îl face când are timp, posibil pe 21 oct.
