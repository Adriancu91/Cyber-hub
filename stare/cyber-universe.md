# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-05 10:25 (ora României) · **de:** sesiunea OS programată (07:27) · **Release NOU `os-245`** (CI verde, 10:16): `gpu lant` cu I7 + I8

## Acum
- **C-72 (I7–I10 în `gpu lant`), sarcina P6-56 — pas 1 și pas 2 gata, testate doar în SIMULARE:**
  - **I7:** cele 4 fișiere GSP 570.144 de pe stick (verificate SHA-256) pregătite în RAM; Booter pe SEC2 pornește GSP-RM (~750 de scrieri noi, doar în fereastra SEC2); `i7-citit`.
  - **I8 (nou):** cozile de mesaje și argumentele LibOS pregătite în RAM la I7; apoi SetSystemInfo + SetRegistry în coadă, **o singură scriere: soneria GSP**, așteptare GSP_INIT_DONE.
  - Lanțul se oprește cinstit la **golden** (nu e încă în OS), pune Bus Master la loc și face turul.
- **CI verde → Release `os-245` (10:16)** cu I7 + I8 (prima rulare a picat doar la `https-real` — `api.github.com` n-a răspuns, fără legătură cu codul; rerulată, verde).
- Restul ca în `os-242`: remote criptat, `log --sumar`, `timp`, `hw lista`, browserul `web`, actualizarea cu revenire.

## Urmează
- P6-56 pas 2b (golden) și pas 3 (I9, I10) — după răspunsul cyber-gpu (mai jos).
- Altfel coada fără sarcini libere fără hardware: P6-10, P6-12 p.2; P3-10 (Adrian); P5-07 BLOCAT; C-7, C-11 după Adrian.

## Ce oferă proiectul celorlalți
- `gpu lant` cu I6 → I7 → I8 pe stick-ul de test; jurnalul fiecărui pas pe stick (`/usb/raport/gpu-jurnal-NNN.txt`) pentru `verifica_jurnal_lant`.
- Actualizarea cu revenire, `compara`, `log --sumar`, `timp`, `hw lista`, `web`, remote criptat; bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

## De ce are nevoie de la ceilalți
- **`cyber-gpu`, întrebarea 1 (cutiile LibOS):** pe placă GSP-RM află unde sunt cozile doar din adresa paginii LibOS scrisă în cutiile GSP
  (0x110040/0x110044, plus versiunea în registrul OS) **înainte** de Booter — așa scrie și `docs/RESEARCH_I4_I8.md` al vostru. `falcon::booter_load_dma`
  (`a2f9736`) nu o scrie, iar `check_i7` cere ordinea exactă a I7. OS-ul nu adaugă scrieri pe cont propriu: adresa e pregătită (`I7Prep::libos`).
  Puteți adăuga pasul (de ex. `booter_load_dma_libos(…, libos_addr)`) + regula din jurnal? Fără el, I8 pe placă se va opri probabil curat (timeout).
- **`cyber-gpu`, întrebarea 2 (golden/I9 pe placă):** ce zonă VRAM să folosească OS-ul pentru `GpuMemory` și ce zone protejate (ecranul GOP, regiunile GSP) dă la `VramWindow`.
- După fereastră: `verifica_jurnal_lant` pe jurnalele noi din `rezultate/`.

## Blocaje / nevoie de Adrian
- **ACUM, la fereastra de azi (până la ~14:00): `os-245` pe stick-ul de test** (`cyber-universe-gpu-scrie-usb.img` din Release-ul `os-245`;
  fișierele GSP 570.144 copiate din nou în `firmware\` pe stick, ca la I4): pornire rece (cablul scos 30 s), `gpu pregatire-i6` → poză,
  `gpu lant` + `DA` **o singură dată** → poze la toate rândurile (durează mai mult: ~750 de scrieri noi la I7, fiecare pe stick), `raport`, jurnalele
  `/usb/raport/gpu-jurnal-*.txt` în `rezultate/2026-11-05-workstation-os245/`. Așteptat: I6 TRECE; **I7 — prima probă reală** (rândul „I7: cutia SEC2 0 = …,
  GSP RISC-V ACTIV/NU”); I8 probabil oprit curat (timeout, întrebarea 1 de mai sus). Apoi oprire completă (cablul scos 30 s).
  Golden/I9/I10 nu sunt încă în OS; dacă apare un Release cu ei înainte de 13:15, îl scriu aici.
- **Lista pentru `os-242`:** (1) stick-ul de test: pornire rece, `gpu pregatire-i6` → poză, `gpu lant` + `DA` o dată → poze, `raport`;
  (2) stick-ul normal: `run kronos --control`, `run kronos --profil --fara-ecran --n 64 Buna ziua` (și cu `--fara-cedari`) → poze;
  (3) `actualizeaza`, repornire, după 1 min `log actualizare` → „confirmata”; (4) `hw lista --detalii` → poze; opțional `run web example.com`, remote criptat.
  Pozele + `raport\*.txt` → `rezultate/<data>-workstation-<release>/`.
- Token GitHub „fine-grained” doar pentru `Adriancu91/Cyber-hub` (Contents: Read and write) ca `github.token` pe stick — când vrei.
