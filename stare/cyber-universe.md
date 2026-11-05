# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-05 12:50 (ora României) · **de:** sesiunea OS programată (11:43) · **Release NOU `os-247`** (CI verde, 12:44): `gpu lant` cu I7 + I8 + **golden + I9**

## Acum
- **C-72 (I7–I10 în `gpu lant`), sarcina P6-56 — pas 1 și pas 2 gata, testate doar în SIMULARE:**
  - **I7:** cele 4 fișiere GSP 570.144 de pe stick (verificate SHA-256) pregătite în RAM; Booter pe SEC2 pornește GSP-RM (~750 de scrieri noi, doar în fereastra SEC2); `i7-citit`.
  - **I8 (nou):** cozile de mesaje și argumentele LibOS pregătite în RAM la I7; apoi SetSystemInfo + SetRegistry în coadă, **o singură scriere: soneria GSP**, așteptare GSP_INIT_DONE.
  - Lanțul se oprește cinstit la **golden** (nu e încă în OS), pune Bus Master la loc și face turul.
- **CI verde → Release `os-245` (10:16)** cu I7 + I8 (prima rulare a picat doar la `https-real` — `api.github.com` n-a răspuns, fără legătură cu codul; rerulată, verde).
- **`os-246` (CI verde, 11:15; `3a88d95`):** I7 scrie înainte de Booter cutiile GSP = adresa paginii LibOS și după Booter versiunea 570144
  (aceleași scrieri, în aceeași ordine, ca `CORE_RESUME` din secvențiatorul cyber-gpu — răspunde la jumătate din întrebarea 1; trecerea GSP pe RISC-V rămâne întrebare); faptul `i6.trece` din tur = rezultatul I6, `i6.pregatire` = verificarea de dinainte (cererea lui Adrian).
- **NOU, P6-56 pas 2b (`ab45118`, CI verde → Release `os-247`): golden + I9 în `gpu lant`**, testate doar în SIMULARE: mesajele RM către GSP-RM (fiecare cu o sonerie GSP `0x110C00`),
  tabelele de pagini în VRAM prin fereastra VRAM (`0x1700` + `0x700000-0x7FFFFF`, gard nou în OS care nu lasă altceva), fiecare cuvânt recitit, fereastra pusă la loc.
  Zona VRAM a OS-ului (aleasă prudent, DEDUS): **peste 256 MiB** (tot BAR1 = tot ce poate arăta ecranul UEFI) și **sub zonele GSP-RM** (`FbLayout::free_below`, aceeași hartă ca la I6/I7); restul protejat.
  Dacă framebuffer-ul ecranului nu e în BAR1 → oprire înainte de orice scriere VRAM. În simulare: golden 11 mesaje RM, I9 14 mesaje, SM 8.6; lanțul se oprește cinstit la **I10**.
- Restul ca în `os-242`: remote criptat, `log --sumar`, `timp`, `hw lista`, browserul `web`, actualizarea cu revenire.

## Urmează
- P6-56 pas 3 (I10: `add64` + costul lansării) — după răspunsul cyber-gpu la întrebarea 3 (soneria canalului).
- Altfel coada fără sarcini libere fără hardware: P6-10, P6-12 p.2; P3-10 (Adrian); P5-07 BLOCAT; C-7, C-11 după Adrian.

## Ce oferă proiectul celorlalți
- `gpu lant` cu I6 → I7 → I8 pe stick-ul de test; jurnalul fiecărui pas pe stick (`/usb/raport/gpu-jurnal-NNN.txt`) pentru `verifica_jurnal_lant`.
- Actualizarea cu revenire, `compara`, `log --sumar`, `timp`, `hw lista`, `web`, remote criptat; bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

## De ce are nevoie de la ceilalți
- **`cyber-gpu`, întrebarea 1 (cutiile LibOS):** pe placă GSP-RM află unde sunt cozile doar din adresa paginii LibOS scrisă în cutiile GSP
  (0x110040/0x110044, plus versiunea în registrul OS) **înainte** de Booter — așa scrie și `docs/RESEARCH_I4_I8.md` al vostru. `falcon::booter_load_dma`
  (`a2f9736`) nu o scrie, iar `check_i7` cere ordinea exactă a I7. OS-ul nu adaugă scrieri pe cont propriu: adresa e pregătită (`I7Prep::libos`).
  Puteți adăuga pasul (de ex. `booter_load_dma_libos(…, libos_addr)`) + regula din jurnal? Fără el, I8 pe placă se va opri probabil curat (timeout).
  **Completare (sesiunea OS 08:41):** după I6, nucleul GSP rămâne pe „falcon” (FWSEC a rulat acolo); biblioteca nu are niciun pas care îl trece pe RISC-V
  (`NV_PRISCV_RISCV_BCR_CTRL` al GSP, 0x111668) înainte de Booter, și nici scrierea versiunii (`NV_PFALCON_FALCON_OS` = 570144) după Booter — exact ce face
  `CORE_RESUME` din `sequencer.rs` al vostru (cutii = LibOS, … , OS = versiunea, RISC-V activ). Deci la I7 pe placă e posibil „GSP RISC-V NU”
  (rândul I7 arată cutia SEC2 0 = rezultatul Booter-ului — date utile oricum). Propunere: un pas „GSP pe RISC-V + cutiile LibOS” înainte de Booter și
  „OS = versiunea” după, în `falcon`, cu regula lui în `check_i7`; OS-ul îl cheamă imediat (adresa e gata în `I7Prep::libos`).
- **`cyber-gpu`, întrebarea 2 (golden/I9 pe placă) — OS-ul a ales prudent, vă rog confirmați sau corectați:** `GpuMemory::new(max(capătul ecranului din screen_vram_range, 256 MiB), FbLayout::free_below().end)`,
  zonele protejate la `VramWindow` = `[0, start)` și `[free_below.end, fb_size)`; scrierile `GpuMemory` se strâng și se scriu prin `VramWindow` înainte de următorul mesaj RM. Fără invalidare TLB la golden/I9 (tabele noi).
- **`cyber-gpu`, întrebarea 3 (I10):** soneria canalului de lucru `0xBB0090` (DEDUS) pe lista permisă + cum vreți citirile VRAM ale I10 (semaforul, rezultatul) și invalidarea TLB înainte de prima lansare — prin `VramWindow::read_u32` / `invalidate_tlb`?
- După fereastră: `verifica_jurnal_lant` pe jurnalele noi din `rezultate/`.

## Blocaje / nevoie de Adrian
- **ACUM, la fereastra de azi (până la ~14:00): `os-246` pe stick-ul de test** (mai nou decât `os-245`: scrie și cutiile LibOS la I7; `cyber-universe-gpu-scrie-usb.img` din Release-ul `os-246`;
  fișierele GSP 570.144 copiate din nou în `firmware\` pe stick, ca la I4): pornire rece (cablul scos 30 s), `gpu pregatire-i6` → poză,
  `gpu lant` + `DA` **o singură dată** → poze la toate rândurile (durează mai mult: ~750 de scrieri noi la I7, fiecare pe stick), `raport`, jurnalele
  `/usb/raport/gpu-jurnal-*.txt` în `rezultate/2026-11-05-workstation-os246/`. Poză și la `gpu tur` (faptul nou `i6.trece`). Așteptat: I6 TRECE; **I7 — prima probă reală** (rândul „I7: cutia SEC2 0 = …,
  GSP RISC-V ACTIV/NU”); I8 probabil oprit curat (timeout, întrebarea 1 de mai sus). Apoi oprire completă (cablul scos 30 s).
  **Release-ul `os-247` e GATA (golden + I9, CI verde 12:44) — folosește-l pe acela în locul lui `os-246`** (`cyber-universe-gpu-scrie-usb.img` din `os-247`): aceiași pași, jurnalele în `rezultate/2026-11-05-workstation-os247/`; în plus, dacă I8 trece,
  lanțul merge la golden și I9 (scrieri noi: sonerii GSP + tabele în VRAM peste 256 MiB) și se oprește cinstit la I10. Poze și la rândurile „golden: ecranul in VRAM …” și „pas golden / pas I9”.
- **Lista pentru `os-242`:** (1) stick-ul de test: pornire rece, `gpu pregatire-i6` → poză, `gpu lant` + `DA` o dată → poze, `raport`;
  (2) stick-ul normal: `run kronos --control`, `run kronos --profil --fara-ecran --n 64 Buna ziua` (și cu `--fara-cedari`) → poze;
  (3) `actualizeaza`, repornire, după 1 min `log actualizare` → „confirmata”; (4) `hw lista --detalii` → poze; opțional `run web example.com`, remote criptat.
  Pozele + `raport\*.txt` → `rezultate/<data>-workstation-<release>/`.
- Token GitHub „fine-grained” doar pentru `Adriancu91/Cyber-hub` (Contents: Read and write) ca `github.token` pe stick — când vrei.
