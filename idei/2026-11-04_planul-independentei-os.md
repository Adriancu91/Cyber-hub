# Planul „Cyber Universe independent de Windows” (înlocuiește varianta A din `2026-11-04_cyber-universe-dezvoltare-din-interior.md`)

- **Propus de:** centrul de comandă, după ideile lui Adrian (4 nov 22:50) · **Data:** 2026-11-04
- **Proiecte implicate:** `cyber-universe`, `cyber-gpu`, `kronos`
- **Stare:** aprobat (Adrian, „da la tot”, 2026-11-04 22:54) → C-68, C-69, C-70

## Ideea (pe înțelesul lui Adrian)
Workstation-ul rămâne în Windows: **Kronos se antrenează în continuare**. Cyber Universe rulează într-o **mașină virtuală (QEMU) pe Windows**, unde îl dezvoltăm de la distanță,
fără riscuri: dacă se blochează, repornim doar mașina. Testele cu placa video și vitezele reale le facem pe hardware real când Adrian e acolo. Când OS-ul devine independent
(remote propriu, actualizare de sine, revenire automată), trecem la teste și dezvoltare direct în OS pe workstation, de la distanță. **Renunțăm la cutiuța KVM.**

## Fazele (fiecare utilă și singură)
- **F1 — Mașina virtuală pe Windows** (~câteva zile): QEMU pe workstation, pornit/oprit de un script; Cyber Universe din ultimul Release; rețea; rapoarte în hub.
  Controlată de la distanță prin Remote Desktop + script. Nu atinge Kronos (procesoarele împărțite: ex. 8 nuclee mașinii, restul lui Kronos; placa rămâne a lui Kronos).
- **F2 — Remote direct din OS** (~1–2 săpt.): ecranul și tastatura lui Cyber Universe prin rețea (text), cu parolă/cheie doar pe stick; merge și în mașină și pe workstation.
- **F3 — Actualizare de sine + revenire automată** (~1–2 săpt.): ia Release-ul de pe GitHub, backup, repornire în versiunea nouă, revenire singur dacă pică.
- **F4 — Citirea completă a hardware-ului** (~1–2 săpt.): lista tuturor dispozitivelor (PCI, USB, ACPI) cu nume și stare, inclusiv **placa Wi-Fi — doar identificată și citită**.
  Un driver Wi-Fi care să se conecteze e o muncă foarte mare (firmware, criptare radio) → separat, mai târziu.
- **F5 — Kronos mediu bun pentru GPU** (în paralel, cu Adrian la workstation): I6 TRECE → I7–I10 → primul calcul pe placă → Kronos pe placă în OS.
- **F6 — Browser propriu, în trepte:** (a) **browser text**: citește pagini web și documentație (HTML simplu) — săptămâni; (b) formulare, imagini, CSS de bază — luni;
  (c) **aplicații web moderne** (JavaScript complet, ca Gmail sau claude.ai) — **ani**: e cea mai mare muncă din tot planul (SerenityOS a avut nevoie de ~4 ani cu zeci de oameni).
- **F7 — Claude în interior, fără API:** calea cinstită și permisă e **legătura prin GitHub** cu sesiunile Claude Code din abonament (decizia din 29 oct): Claude scrie codul,
  OS-ul îl ia, îl testează, trimite rezultatul. Folosirea claude.ai de către un program care „apasă singur” în pagină nu e permisă de regulile Anthropic (accesul automat se face
  prin API) → nu o planificăm; browserul propriu rămâne pentru oameni (Adrian) și pentru citit pagini.
- **F8 — Coding direct în OS:** editor de text + terminal + git simplu (săptămâni); **construirea codului în OS** (compilator Rust) e foarte departe → până atunci construiește
  GitHub (2–3 min). Mai târziu: Kronos-Cod ca ajutor în interior.
- **F9 — Unelte pentru dezvoltare și teste:** profil, jurnal, comparare rapoarte, teste automate în OS, toate pe lista albă.

## Ce rămâne neschimbat
- Scrierile pe placa video doar cu Adrian de față (până la o decizie nouă). Clean-room. `main` mereu construibil.
- Kronos se antrenează pe Windows (C-64: română, Kronos mai mare) — fără pauză.

## Ce trebuie de la Adrian
- „da” la plan (eventual pe faze); pentru F1: „da” la instalarea QEMU pe workstation (descărcare oficială); pentru F2/F3: tokenul GitHub pentru stick (drepturi minime).

## Decizia lui Adrian
- 2026-11-04 22:50: alege mașina virtuală pe Windows + Kronos continuă + fără KVM. 2026-11-04 22:54: **„da la tot”** — toate fazele, inclusiv descărcarea QEMU (oficială) pentru F1. Tokenul GitHub pentru stick: îl face Adrian când ajungem la F3.

## Discuție
