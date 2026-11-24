# Idei din chatul simulatorului (Adrian, 24 nov seara) — triate de centrul de comandă

- **Propus de:** centrul de comandă (din discuția lui Adrian în chatul simulatorului) · **Data:** 2026-11-24
- **Proiecte implicate:** `kronos`, `cyber-gpu`, `cyber-universe`
- **Stare:** propus — nimic nu pornește fără „da”-ul lui Adrian. Cifrele de câștig sunt socotite în acel chat, **nemăsurate și neverificate de centru**.

## Ce e nou față de propunerile de azi (trepte, cele patru piese)
| # | Ideea | Unde se potrivește | Părerea centrului |
|---|---|---|---|
| 1 | **Harta greutății textului în RAM:** procesorul ține pentru tot textul (1,34 Mld simboluri) cât de „greu” e fiecare fragment, din pierderile pașilor trecuți, și alege ferestrele utile înainte de pas (idei publice: alegerea loturilor din mers, RHO-LOSS — cu avertismentul lor: nu doar „greu”, ci și nezgomotos și legat de țintă). Exemplu: TinyStories, pe care #513 le știe aproape pe de rost, ar fi trase mai rar | laboratorul C-163 (Windows), apoi OS | **Cea mai bună dintre ele.** Ieftină (doar alegerea datelor; modelul neschimbat), se probează în laborator cu același examen. Propun s-o pun a treia probă după rețeta de azi și bucăți K = 4. Câștig socotit acolo ×1,5–2 — de măsurat |
| 2 | **Straturi sărite pentru simbolurile ușoare** (idee publică: „mixture-of-depths”) — un simbol trece prin mai puține straturi; motorul nostru strânge restul într-o matrice compactă | C-164 (Kronos croit pe placă) | Bună pentru Kronos v2; schimbă arhitectura și generarea. Întâi laboratorul |
| 3 | **Ieșirea doar pe simbolurile care pot urma** (din caietul din RAM) | după caiet | Riscantă: schimbă ce învață modelul. Rămâne după ieșirea pe eșantion |
| 4 | **Dovadă pentru 8 biți la antrenare pe plăci de jocuri** (LLMQ, ~50 % din puterea plăcii, după chatul simulatorului) | pista B1 | Dacă sursa se confirmă, întărește proba pe 8 biți. De verificat sursa |
| 5 | **Un singur program pe tot stratul** („megakernel”) | după tensor cores | Azi înmulțirile sunt 93 % din pas (os-412), restul ~33 ms — câștigul ar fi mic acum |
| 6 | **Kronos învață în timp ce e folosit** (pași mici în pauzele dintre conversații) | după versiunea 1 | Utilitate, nu viteză; o idee pentru mai târziu |

**Avertisment adus de același chat:** un motor compact peste Vulkan (Meganeura) e în mediană de ~1,8 ori mai lent ca PyTorch în F32 — un motor general scris de mână pierde de obicei; câștigul nostru vine doar din specializare.

## Decizia lui Adrian
- (de completat) — întrebarea: ideea 1 intră ca a treia probă în laboratorul C-163?
