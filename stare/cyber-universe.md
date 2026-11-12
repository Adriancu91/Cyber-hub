# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-12 22:00 (ora României) · **de:** sesiunea OS programată (20:40) — **C-113 și C-114 gata → Release `os-297`** (CI verde). Ultimul Release: **`os-297`** (orice Release mai nou are aceleași schimbări).

## Acum
- **C-113 (stick Kingston 64 GB):** cauza găsită în cod — după antet, OS-ul îi cere stick-ului „sincronizarea” (SYNCHRONIZE CACHE),
  iar multe stick-uri nu au comanda asta și o refuză; până la os-295 refuzul oprea jurnalul. FAT-ul mare nu era problema (testat în QEMU
  pe 64 GB, clustere de 32 KiB). În **`os-297`**: refuzul e tolerat (scris o dată în `log usb`), orice alt refuz are motivul exact în log,
  un rând de jurnal rescrie 1–2 sectoare în loc de un cluster întreg de 32 KiB, iar **`usb timp`** (și ultimul rând din raportul
  `gpu lant`) arată cât au durat scrierile și sincronizările → vedem de unde vine ~1 s/rând.
- **C-114 (un singur stick):** în Release-ul `os-297` e arhiva **`stick-test-complet.zip`**: o dezarhivezi și copiezi tot în rădăcina
  stick-ului Kingston, apoi pui o dată `firmware\`, `kronos\`, `github.token` (pași și în `CITESTE.txt` din arhivă). Testat în QEMU:
  pornire de pe stick FAT32 de 64 GB + jurnal scris. Stick-ul normal CYBER-UNIV rămâne pentru folosirea obișnuită.
- **De ce a dispărut `os-289` (C-111):** CI-ul păstrează doar ultimele 5 Release-uri, în afară de cele trecute în
  `docs/RELEASES_PASTRATE.md`. `os-295` (testat azi) e acum trecut acolo → nu se mai șterge.
- Procedura testului cu variante (C-108) e aceeași, cu `os-297` în loc de `os-295` (partea GPU identică).

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

**La următorul test (înainte de orice altceva pe placă):** stick-ul Kingston de 64 GB cu `stick-test-complet.zip` din **`os-297`**
(sau, dacă preferi, cu imaginea de test ca până acum) → `gpu lant --varianta 1` + DA. Dacă jurnalul merge: poză la ultimul rând
`usb: scrieri …, sincronizari …`; dacă nu: poză la mesaj + `log usb`. Rezultatele în `rezultate/<data>-workstation-os297/`.

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
