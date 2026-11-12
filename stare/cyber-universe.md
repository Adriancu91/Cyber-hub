# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-12 17:50 (ora României) · **de:** sesiunea OS programată (17:40) — **Adrian vine acum la test (C-111). Release-ul `os-289` NU mai există pe GitHub (nici `os-292`) → testul se face cu `os-295`** (aceleași 10 variante GPU). Ultimul Release: **`os-295`**.

## Acum
- **⚠ Pentru testul de acum (C-111): ia Release-ul `os-295`**, nu `os-289` (a dispărut din lista de Release-uri; `os-295` = os-289 + reparația ASUS + mouse USB + `log mmio`, partea GPU identică). Procedura de jos e neschimbată, doar numărul Release-ului. Bonus: o poză la `log mmio` (pentru P6-12).
- **Testul cu variante (C-108) s-a amânat** (C-110). Procedura de mai jos rămâne valabilă cu **`os-289`** sau **`os-290`**; merge identic și
  cu `os-293`/`os-294` (au aceleași variante GPU, nimic schimbat în partea GPU).
- **Release `os-293` = os-290 + P6-80:** mouse-ul și tastatura USB merg acum și dacă le bagi DUPĂ pornire, iar receptoarele fără fir
  tastatură+mouse sunt văzute amândouă (era cauza probabilă pentru mouse-ul care nu mergea pe Lenovo). Testat în QEMU; pe Lenovo neîncercat.
- **Release `os-294` = os-293 + P6-81:** pasul 1 din P6-12 (observația Cyber-GPU despre registre cu cache). Nicio schimbare de
  comportament: OS-ul doar numără ce găsește, iar comanda `log mmio` arată rezumatul. În QEMU apare deja un caz real: zona ecranului
  (BAR0 al plăcii VGA de test) e mapată de Limine **cu cache** — exact situația din observație. Pe NVIDIA registrele sunt în alt BAR,
  deci pe workstation ar trebui să iasă „0 deja CU cache” pentru BAR0; o poză la `log mmio` lămurește.
- **Release `os-295` = os-294 + P6-82:** doar testul automat `remote` reparat (pica uneori în CI din cauza ordinii a două mesaje); nimic
  schimbat pentru tine — orice Release de la `os-289` încoace e bun pentru test.
- `os-290` (ASUS TUF, C-109) și C-105 (`ciclu-test`, oprit până la cele două chei) — neschimbate.

## Urmează
- P6-12 pasul 2 (fereastră proprie fără cache) doar după un `log mmio` de pe un calculator real.
- Când vine Adrian la workstation: testul cu variante (procedura de jos) → Cyber-GPU (`compara_variante`).

## Ce oferă proiectul celorlalți
- `gpu lant [--varianta N]` I6 → I14, `gpu variante`, `gpu recupereaza`, `kronos --gpu` pe stick-ul de test; jurnale + rapoarte trimise în hub (cu token).
- `hub ruleaza` / `hub asculta`, `test tot`, `kronos --conversatie`, git pe ramuri `os/…`, `web`, `files`; bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

## De ce are nevoie de la ceilalți
- **`cyber-gpu`:** după jurnalele de joi, pasul următor (varianta care a trecut sau, dacă niciuna, următoarea ipoteză).
- **`kronos`:** Release-ul `kronos-kgr1-513` (opțional).

## Blocaje / nevoie de Adrian

**Când ai Lenovo-ul la îndemână (nu grăbește nimic):** scrie pe stick-ul normal `cyber-universe-usb.img` din Release-ul **`os-293`**
(sau mai nou), pornește Lenovo-ul, apoi **bagă mouse-ul USB după ce apare desktopul** și vezi dacă merge; o poză la `lsusb` și una la
`log mmio`, în `rezultate/<data>-laptop-lenovo-i5/`. Dacă vrei să știi și cauza veche, varianta de mai jos (cu `os-290`):

**Mic, când ai Lenovo-ul la îndemână (nu grăbește nimic):** ca să știm sigur de ce nu mergea mouse-ul USB — pornește Lenovo-ul cu stick-ul normal
**cu mouse-ul deja băgat**, scrie `lsusb` și fă o poză. Dacă mouse-ul apare în listă și tot nu merge → altă cauză; dacă nu apare → era cauza
reparată în P6-80 (mouse băgat după pornire). Poza în `rezultate/2026-11-11-laptop-lenovo-i5/`.

**Testul cu variante (C-108/C-111, acum) — Release `os-295`** (`os-289` nu mai e pe GitHub):
1. Din Release-ul **`os-295`** (github.com/Adriancu91/cyber-universe → Releases) iei `cyber-universe-gpu-scrie-usb.img` și îl scrii cu
   Rufus pe **stick-ul de test**. Stick-ul normal rămâne cum e.
2. Pentru fiecare variantă, începând cu **1**: **oprire completă → cablul scos 30 s** → pornire de pe stick-ul de test (F8) →
   `gpu lant --varianta 1` → verifici pe ecran rândul „varianta I8 1: rpc-inainte …” → `DA` + Enter.
3. Ce contează: rândul `valoare GSP_INIT_DONE: rpc_result … = 0x…` — **`0x00000000` = varianta a trecut** (lanțul merge mai departe la
   `i8e-golden`); tot `0x59` = nu. **Poză** la rândul acesta și la rezumatul de la final.
4. `trimite` (sau `raport`, apoi pozele + `raport\gpu-jurnal-*.txt` în `rezultate/2026-11-12-workstation-os295/`).
5. Repeți de la pasul 2 cu varianta următoare (2, 3, … 10). **Te oprești la prima variantă care trece.** Lista completă: `gpu variante`.

(Merge la fel și cu `os-290`, `os-293` sau `os-294` — aceleași variante.)

**Pe ASUS TUF (C-109), când ai 5 minute:** scrii `cyber-universe-usb.img` din Release-ul **`os-290`** pe stick-ul normal (Rufus), pornești
ASUS-ul de pe el și faci **o poză** la rândurile `apic: mod …`, `apic: calibrez ceasul …`, `apic: ceasul de referinta: …` — sau la ultima
linie, dacă tot se oprește. Dacă ajunge la desktop: `hw` + `test tot`, poze în `rezultate/<data>-laptop-asus-tuf/`.

**Opțional (C-104, ~5 min):** tokenul pentru `hub asculta` — `docs/USB.md` punctul 15.

**Când vrei (C-105):** ciclul de test automat e gata, dar **oprit**; îl pornești doar tu, cu cele două chei (`docs/USB.md` punctul 16).
