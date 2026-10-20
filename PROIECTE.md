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
- **Cum se lucrează:** sesiuni Claude Code în cascadă, continuu, pe laptopul lui Adrian (ThinkPad).

## Legături cunoscute între proiecte
| De la | Către | Legătura | Când |
|---|---|---|---|
| suita-office | kronos | Suita devine modul pe platforma Cyberspace (variantă Kronos) | după ce suita e terminată și testată de oameni |
| suita-office | cyber-universe | Suita devine set de aplicații de sistem în Cyber Universe | Faza 5 a OS-ului |
| kronos | cyber-universe | Kronos ca asistent/modul AI integrat în OS | Faza 5 a OS-ului |
| cyber-universe | kronos | OS ușor, optimizat pentru a rula Kronos pe hardware slab | pe termen lung |

## Principii comune ale lui Adrian (valabile pentru toate proiectele)
- Totul construit de la zero, cel puțin 90% propriu.
- Modular: nucleu central + module care se pot adăuga și scoate.
- Rapid și economic pe hardware slab.
- Fiecare pas reversibil.
