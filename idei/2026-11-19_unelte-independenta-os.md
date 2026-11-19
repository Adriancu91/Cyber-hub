# Unelte pentru „mai mult timp în OS”: ce avem, ce lipsește, în ce ordine

- **Propus de:** centrul de comandă (la cererea lui Adrian, 19 nov 2026 23:28: „caută de ce unelte mai avem nevoie pe OS-ul nostru și pentru viitor, și pentru mai multă independență de Windows”) · **Data:** 2026-11-19
- **Proiecte implicate:** `cyber-universe`, `cyber-gpu`, `kronos`
- **Stare:** propus
- **Leagă:** `idei/2026-11-04_planul-independentei-os.md` (aprobat pe 4 nov; mare parte făcut), `idei/2026-11-19_plan-performanta-placa.md` (firele V, T, M, S), decizia din 13 nov („toate piesele la treabă”)

## Ideea (pe înțelesul lui Adrian)
Dacă placa merge repede sub driverul nostru, are rost să stăm mult în Cyber Universe: teste unul după altul, apoi Kronos rulat și, la capăt, antrenat acolo.
Am făcut inventarul: OS-ul are deja aproape tot ce ține de „a fi condus de la distanță”. Lipsesc cinci unelte mici ca să putem **rămâne** în el fără Windows,
patru ca să **lucrăm util** acolo și una mare — **motorul de antrenare** — ca Windows să nu mai fie necesar deloc pentru Kronos.

## Ce avem deja (din `cyber-universe/docs/TASKS.md`, toate bifate)
- Agentul din OS care ascultă centrul comun și răspunde singur (`hub asculta`), ciclul automat (`ciclu-test`), actualizarea de sine din Release cu revenire la versiunea veche.
- Consola de la distanță, criptată; rapoartele și jurnalele urcate singure în hub.
- Toate nucleele procesorului, memorie mare, fire de lucru; rețea pe cablu (Intel, Realtek); ceasul prin rețea.
- Editor, terminal, git simplu, manager de fișiere, browser de text, inventar de hardware (`analiza`), unelte de profil și jurnal.
- Kronos în OS: convorbire, generare pe procesor (pe mai multe fire) și pe placă.
- Drivere de disc SATA (citire și scriere) și NVMe, FAT32, cu regula „scriu doar pe partițiile marcate `cyber.rw`”.

## De ce mai avem nevoie de Windows azi
1. **Antrenarea lui Kronos** (PyTorch) și executantul care o conduce.
2. **Comutarea pornirii** spre stick (o face scriptul din Windows) și întoarcerea.
3. **Punerea versiunii noi pe stick** (centrul de comandă, prin aplicația din Windows) — deși OS-ul știe deja să se actualizeze singur.
4. **Coborârea plăcii în starea de pornire** între două teste (azi o face oprirea Windows-ului; în OS, a doua rulare din aceeași pornire cere „pornire rece”).
5. **Temperatura** plăcii și a procesorului (se văd doar în Windows).
6. **Dacă OS-ul se blochează**, nimeni nu-l repornește.

## Treapta 1 — ca să putem RĂMÂNE în OS (unelte mici; zile)

| Unealta | Ce face | Ce există / ce am găsit | Ce cere |
|---|---|---|---|
| **1. Tabloul de bord al plăcii** | temperatura plăcii, ceasurile (MHz) ale nucleului și memoriei, starea de performanță, cât e de ocupată, motivul oricărei încetiniri (inclusiv „încetinire termică”) | **Găsit pe 19 nov:** fișierele publice NVIDIA pentru exact versiunea noastră (570.144) descriu o „zonă comună” în care programul intern al plăcii scrie singur aceste date: `class/cl00de.h` (structurile, inclusiv `RUSD_TEMPERATURE`, `clkPublicDomainInfos`, `clkThrottleReason`) și cele două comenzi de pornire din `ctrl2080internal.h` (`INTERNAL_INIT_USER_SHARED_DATA`, `INTERNAL_USER_SHARED_DATA_SET_DATA_POLL`). Driverul deschis nouveau a primit în iulie 2026 o serie de patch-uri care citește temperatura exact așa, „de la Turing la Blackwell”, cu firmware 570 sau mai nou. Sesiunea Cyber-GPU 119 căutase în alte fișiere și trăsese concluzia că temperatura nu are cale documentată | regula „trei surse” (Cyber-GPU); două comenzi noi către programul plăcii → **„da”-ul lui Adrian** înainte de placă |
| **2. Resetul plăcii din interior** | coboară placa în starea de pornire fără să ieșim din OS → teste unul după altul (10–20 pe zi în loc de 2) | pregătit: `gpu recupereaza` (Booter Unload) și studiul FLR (`cyber-gpu/docs/C-142_K513_VITEZA_FLR.md` §4); niciunul dovedit pe placă cu WPR2 ridicat | **DA-ul lui Adrian pentru proba FLR** (așteaptă din 18 nov) |
| **3. Comutatorul de pornire de pe stick** | stick-ul e primul în BIOS; încărcătorul nostru pornește fie Cyber Universe, fie Windows, după un rând scris de noi pe stick → nu mai e nevoie de Windows ca să ajungem în OS și nici ca să ne întoarcem | încărcătorul nostru (Limine) are documentate „pornirea altui sistem” (`efi` / `efi_chainload`) și `default_entry`; azi fișierul lui are o singură intrare | Adrian schimbă o dată ordinea de pornire în BIOS (reversibil; fără stick, calculatorul pornește Windows ca azi) |
| **4. Ceasul de pază al plăcii de bază** | dacă OS-ul îngheață, calculatorul se repornește singur după un termen | neexistent în OS; cipul plăcii de bază (Intel) are un astfel de ceas, documentat public | regula de surse a OS-ului; test întâi în QEMU, apoi pe workstation |
| **5. Temperatura procesorului + oprire de siguranță** | citirea temperaturii fiecărui nucleu și oprirea lucrului peste un prag | neexistent; registrele sunt documentate de Intel | doar citire |

## Treapta 2 — ca să LUCRĂM util în OS (zile–săptămâni)

| Unealta | Ce face |
|---|---|
| **6. Discul propriu** | o partiție marcată `cyber.rw` pentru modele, date și jurnale; golirea sigură a scrierilor (pregătită în C-148); seturi de date în bucăți de cel mult 4 GiB (limita FAT32) |
| **7. Examenul lui Kronos în OS** | examenul de azi rulat pe placă, în loturi, cu același rezultat ca în Windows → putem judeca un model fără Windows |
| **8. Managerul de lucrări lungi** | pornește la o oră, raportează în hub la N minute, se oprește la comandă sau la oră, reia singur după o pană de curent |
| **9. Starea pe telefon** | OS-ul urcă singur în hub un rezumat și o captură de ecran; centrul de comandă le trimite lui Adrian. (Ecranul direct, ca prin Remote Desktop, nu se poate: în OS nu există Tailscale.) |

## Treapta 3 — ca să ANTRENĂM în OS (unealta mare; săptămâni–luni)

**10. Motorul de antrenare propriu.** Azi Kronos învață cu PyTorch, care nu există în OS-ul nostru. Ne trebuie:
- programele „înapoi” pentru fiecare calcul (cele care spun fiecărei greutăți cu cât să se schimbe), funcția de eroare și optimizatorul, toate pe placă, prin driverul nostru;
- înmulțiri matrice × matrice rapide — aici firul T (circuitele speciale) devine obligatoriu, nu opțional;
- **„pasul de aur”**: Kronos exportă din PyTorch un pas de antrenare (intrările, eroarea, schimbările cerute, greutățile după 10 pași), iar motorul nostru trebuie să dea aceleași numere — cum sunt azi vectorii KGR1 pentru rulare;
- date de antrenare într-un format simplu, pe discul propriu (tokenizatorul există deja în OS);
- salvări sigure și reluare; modele care trec în ambele direcții între Windows și OS;
- toate nucleele procesorului pentru date și verificare (ține de decizia din 13 nov).

Că se poate fără PyTorch arată proiectul `llm.c`: antrenează GPT-2 de 124 de milioane în C simplu (referința pe procesor are ~1 000 de rânduri), a ieșit cu ~7 % mai rapid decât PyTorch și se verifică exact prin compararea cu PyTorch a erorii și a 10 pași de antrenare. Diferența: ei stau pe driverul și bibliotecile NVIDIA; noi le scriem pe ale noastre.

**Cinstit despre viteză:** antrenarea în OS nu va fi curând mai rapidă decât în Windows. PyTorch folosește de ani de zile circuitele speciale ale plăcii; noi abia le atingem. Câștigul la început e independența și controlul (toată memoria plăcii, niciun strat străin), nu viteza. Devine „mai favorabilă” abia după firele V și T.

## Mai târziu
- Wi-Fi, browser complet, compilarea codului în OS (rămân ca în planul din 4 nov: foarte departe).
- Compilatorul programelor pentru placă rămâne o unealtă pe calculatorul de construit (nu în OS, nu în Windows).

## Ce ar face fiecare proiect (dacă Adrian spune „da” la treapta 1)
- `cyber-gpu`: unealta 1 (zona comună: studiu cu trei surse, cod oprit implicit, SIMULARE; pe placă întâi doar pornirea zonei + citirea ei la sfârșitul testului); partea de driver din unealta 2.
- `cyber-universe`: uneltele 3, 4, 5; comanda FLR din unealta 2 (scrierea în configurația PCI) și legarea ei în ciclul automat; afișarea tabloului de bord (`gpu stare`).
- `kronos`: nimic la treapta 1. La treapta 3: „pasul de aur” (export din PyTorch, fără nimic în `kronos/`).

## Cost și riscuri
- Treapta 1: o săptămână la ritmul nou, în paralel cu planul de viteză (OS-ul are capacitate liberă). Unealta 2 e singura cu risc pe placă: dacă resetul nu coboară placa, rămânem ca azi (întoarcere prin Windows).
- Unealta 3 schimbă cine hotărăște pornirea: dacă stick-ul sau încărcătorul nostru nu pornește, BIOS-ul trece singur la Windows. De verificat pe workstation cu Adrian de față, o dată.
- Unealta 4 poate reporni calculatorul în mijlocul unei lucrări dacă termenul e prea scurt → pornită doar în modul ciclu, cu termen larg.
- Treapta 3 e un proiect cât tot driverul de până acum. Până e gata, antrenările rămân în Windows.

## Decizia lui Adrian
- (completează Adrian sau centrul de comandă cu data aprobării din chat)

## Discuție
- 2026-11-19 centrul de comandă: inventarul e din `cyber-universe` (`docs/TASKS.md`, `kernel/src`, `user/src/bin`) la commit-ul de după `os-308`; căile pentru uneltele 1 și 3 sunt citite din surse publice, ca specificație.

## Surse
- NVIDIA 570.144 (MIT), zona comună: `src/common/sdk/nvidia/inc/class/cl00de.h`, `src/common/sdk/nvidia/inc/ctrl/ctrl2080/ctrl2080internal.h`, `src/nvidia/inc/kernel/gpu/gpu_user_shared_data.h` — https://github.com/NVIDIA/open-gpu-kernel-modules/tree/570.144
- nouveau, seria „GSP telemetry via RM User Shared Data” (14 iul 2026): https://ratatoskr.run/dri-devel/2026/07/17259533/t
- Limine, configurare (`efi` chainload, `default_entry`): https://github.com/limine-bootloader/limine/blob/trunk/CONFIG.md
- llm.c (antrenarea GPT-2 în C simplu): https://github.com/karpathy/llm.c
