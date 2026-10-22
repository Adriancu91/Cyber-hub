# Harta proiectelor

## Kronos / Cyberspace (`kronos`)
- **Ce e:** AI propriu, construit de la zero. Platforma se numește Cyberspace, nucleul AI se numește Kronos. Are module conectabile.
- **Unde e codul:** repo privat `Adriancu91/cyberspace`.
- **Cum se lucrează:** Claude Code pe stația de lucru a lui Adrian execută sarcini din `plan/coada.md`; un supraveghetor în cloud verifică de 8 ori pe zi (2:15, 5:15 … 23:15) și pune sarcinile următoare.

## Cyber Universe OS (`cyber-universe`)
- **Ce e:** sistem de operare propriu, minim și modular, scris de la zero (nucleu Rust, x86_64, UEFI).
- **Unde e codul:** repo `Adriancu91/cyber-universe`.
- **Cum se lucrează:** sesiuni automate în cloud, de 8 ori pe zi (2:40, 5:40, 8:40 … 23:40), după `docs/TASKS.md`.

## Suita office (`suita-office`)
- **Ce e:** suită proprie de aplicații: foi de calcul cu formule, documente, PDF, prezentări, editare imagini, notițe, video.
- **Unde e codul:** deocamdată doar local, pe laptopul lui Adrian (nu e încă pe GitHub).
- **Cum se lucrează:** sesiuni Claude Code în cascadă, continuu, pe laptopul lui Adrian (ThinkPad), cu lista ei de sarcini.
  Adrian o dirijează direct, în chatul ei. **În hub doar raportează și propune colaborări; nu primește comenzi prin `COMENZI.md`.**

## Cyber-GPU (`cyber-gpu`) — din 23 octombrie 2026
- **Ce e:** driverul propriu de calcul pentru placa video (întâi NVIDIA RTX 3070 Ti / GA104), fără grafică, doar putere de calcul pentru
  Kronos în Cyber Universe OS. Rust `no_std`, clean-room (aceleași reguli ca OS-ul: `cyber-universe/docs/CLEAN_ROOM.md`, D-013).
- **Unde e codul:** repo `Adriancu91/cyber-gpu` (workspace separat; intră mai târziu ca crate în `cyber-universe`, ca `rtl8168/`).
- **Cum se lucrează:** sesiuni Claude Code pornite de Adrian (pe laptopul lui, „Auto mode”), după prompt-ul „MASTER PROMPT — CYBER-GPU v1.0”
  și documentele din `idei/2026-10-23_*`. **Nu modifică** `cyber-universe` sau alte repo-uri: schimbările necesare în OS se livrează ca
  patch-uri documentate, pe care le preia sesiunea OS. Testele pe RTX se fac **doar pe workstation, într-o fereastră aprobată de Adrian**
  (workstation-ul e al lui Kronos). Raportează în hub: `stare/cyber-gpu.md`, `jurnal/cyber-gpu.md`.

## Legături cunoscute între proiecte
| De la | Către | Legătura | Când |
|---|---|---|---|
| suita-office | kronos | Suita devine modul pe platforma Cyberspace (variantă Kronos) | după ce suita e terminată și testată de oameni |
| suita-office | cyber-universe | Suita devine set de aplicații de sistem în Cyber Universe | Faza 5 a OS-ului |
| kronos | cyber-universe | Kronos ca asistent/modul AI integrat în OS | Faza 5 a OS-ului |
| cyber-universe | kronos | OS ușor, optimizat pentru a rula Kronos pe hardware slab | pe termen lung |
| cyber-gpu | cyber-universe | driverul de calcul GPU devine crate în OS (backend `nvidia-ga104`), prin patch-uri de integrare | după primul calcul demonstrat pe RTX |
| cyber-gpu | kronos | runtime-ul tensorial pentru rularea/antrenarea lui Kronos fără CUDA | după K6-GPU și măsurătoarea K10 |

## Principii comune ale lui Adrian (valabile pentru toate proiectele)
- Totul construit de la zero, cel puțin 90% propriu.
- Modular: nucleu central + module care se pot adăuga și scoate.
- Rapid și economic pe hardware slab.
- Fiecare pas reversibil.
