# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-12 20:00 (ora României) · **de:** sesiunea Cyber-GPU 94 (cloud, fără placă) — **jurnalele 011 și 012 analizate (`cyber-gpu/docs/os-295_ANALIZA_011_012.md`): la repetarea variantei 1, I7 a picat deși scrierile au fost identice cu 010 — Booter a terminat cu 0, RISC-V-ul GSP a rămas `0x10`; cauza nu se poate stabili din jurnal (singurul lucru diferit: stick-ul la ~1 s/rând, C-113). Booter Unload (C-103) a răspuns 0x88 — cod nepublicat; singura diferență față de RM: fără FWSEC-SB înainte. De la `3404313`, după un I7 / Unload eșuat jurnalul scrie starea plăcii (9 citiri numite) și așteptarea „RISC-V activ” are limita 5 s (nova). 458 PASS, CI verde. Nimic testat pe placă.** 🎉 **I8 și golden (I8e) au trecut pe placă la 17:48 (os-295, jurnalul 010); I9 s-a oprit la `PROMOTE_CTX` virtual fără motiv în jurnal — de la `45dfc77` motivul merge pe stick.**
## Acum
- **Sesiunea 94 (19:25–20:00) — jurnalele 011 și 012 citite; un pas mic pe driver (`85e0a34`, `3404313`), doar citiri, doar adăugări.** Nicio comandă nouă pentru cyber-gpu în hub (C-113/C-114 sunt ale OS-ului).
  - **Jurnalul 011 (`gpu lant`, varianta 1, ~18:00, stick la ~1 s/rând): I7 ESEC.** `diff` fără marcaje de timp față de 010 = **12 rânduri**: 4 adrese RAM (alocare diferită a OS-ului, valide)
    + rezultatul → **scrierile în placă au fost identice, în aceeași ordine**; nu e regresie de cod. Booter a terminat cu `MAILBOX0 = 0` (`FALCON_OS` e scris după, deci SEC2 s-a oprit curat),
    apoi așteptarea „RISC-V activ” a expirat: `GSP RISCV_CPUCTL = 0x10` = exact valoarea pe care 010 o arată **înainte** ca Booter să pornească nucleul la I8 → nu se poate spune dacă nucleul
    n-a pornit deloc sau a pornit și s-a oprit; `SCRATCH_14` (bitul 26) și `GSP MAILBOX0` ar fi spus, dar la I7 nu le citeam. Singurul lucru diferit: **timpul** (I6 → Booter 65 s în loc de 15 s;
    încărcarea Booter-ului 56 s în loc de 9 s — lentoarea a început la rândul ~1440, în mijlocul ei). Corelație, nu cauză dovedită.
  - **Jurnalul 012 (`gpu recupereaza`, C-103, ~18:13, cel mai probabil aceeași pornire):** reset GSP + SEC2, Booter Unload → **`MAILBOX0 = 0x88`**, WPR2 rămâne ridicat. Codul **nu e publicat**
    (RM și nouveau doar îl tipăresc). Starea era una pe care niciun driver public n-o rulează așa: GSP-RM nu pornise niciodată, iar RM la `kgspTeardown` rulează **FWSEC-SB înainte** de Booter
    Unload (noi nu — decizia C-103). Propunere: FWSEC-SB înainte (același program semnat FWSEC, comanda SB) — **cere DA-ul lui Adrian**; până atunci `gpu recupereaza` nu se mai rulează.
  - **Pasul făcut:** `falcon::journal_i7_failure` — după un I7 eșuat (Booter cu cod, sau Booter cu 0 + RISC-V neactiv) și după un Booter Unload cu cod, jurnalul scrie `nota: … starea placii
    (doar citiri):` + **9 rânduri `valoare`** (`SCRATCH_14`, `SEC2 CPUCTL/MAILBOX0/1`, `GSP RISCV_CPUCTL/MAILBOX0/1`, `GSP RISCV_BCR_CTRL`, `GSP FALCON_OS`) — registre deja citite/scrise, niciunul nou.
    `RISCV_ACTIVE_US` 2 s → **5 s** (nova; cea mai lungă din sursele publice). T125 a–d, **458 PASS**, CI verde (rulările 43273728070, 43274217367, 43274259743). **OS-ul doar leagă `3404313`+**
    (nota `cyber-gpu/integration/cyber-universe/os-295_jurnalele-011-012.md`). Sursele RM n-au putut fi recitite din cloud azi (acces refuzat) — afirmațiile despre ordinea RM sunt din citirile anterioare.
  - Copia C-34 refăcută la `3d61b04` (clona fusese superficială — bundle-ul din sesiunea 93 era incomplet; acum 219 commit-uri, clonare de probă OK).
- **Sesiunea 93 (18:00–18:40) — jurnalul `gpu-jurnal-010.txt` (os-295, `gpu lant --varianta 1`, 17:48) citit; un pas pe driver.** Studiul: `cyber-gpu/docs/os-295_ANALIZA_I9.md`.
  - **I8 TRECE:** `GSP_INIT_DONE rpc_result = 0x00000000` după 11,17 s → `pas i8-gsp-init: ok`. Doar **2 NOCAT** (os-283: 844): 1 ASSERT (adresă nouă, `0x0132d3b2`) + 1 ENGINE
    `NV_ERR_INVALID_DMA_SPECIFIER` „Display Subsystem / Display Engine”; 2 `UCODE_LIBOS_PRINT` (ENG_PMU). **Analiza din sesiunea 88 (ordinea RPC-urilor) s-a confirmat pe placă;
    variantele 2–10 nu mai sunt necesare** (`compara_variante`: „au trecut de I8: varianta 1 (rpc-inainte)”).
  - **I8e golden TRECE:** 11 mesaje RM (7 alocări + 4 comenzi) acceptate de GSP-RM; tabelele de pagini scrise în VRAM prin fereastra 0x1700 — primele apeluri RM reușite pe placă.
  - **I9 ESEC, motiv necunoscut:** din numărarea soneriilor, GSP-RM a acceptat 10 mesaje ale clientului de lucru (client, dispozitiv, subdispozitiv, VA space, `SET_PAGE_DIRECTORY`,
    TSG, context share, canal, compute, `PROMOTE_CTX` fizic) și **al 11-lea — `PROMOTE_CTX` jumătatea virtuală (MAIN/PM/PATCH) — a eșuat**: refuz cu cod `NV_STATUS` sau limita de 5 s,
    nu se poate spune — `run_chain_ready` scria doar `pas i9-canal-lucru: ESEC`, textul erorii mergea doar pe ecran, și ecranul înghețase. Marcajele de timp de pe stick sunt ora scrierii
    (~13 ms/rând), nu a evenimentului. Forma mesajelor noastre e identică cu `promote_ctx` din tinygrad `ip.py` (citit azi ca specificație); dacă e refuz, diferă *ce* promovăm.
  - **Ecranul înghețat** la rândul 2274 (`SCRATCH_14 = 0x17100000`) = exact pornirea RISC-V-ului GSP; jurnalul a mers încă ~9 s de evenimente și s-a închis curat (Bus Master oprit, tur după).
    Ipoteză: GSP-RM a preluat afișajul (NOCAT „Display Engine”). **Nu avem o setare publică, cu sursă, care să-l oprească — nu inventăm**; propunere pentru OS: după I8 ecranul se
    consideră pierdut, raportul e jurnalul + `trimite`.
  - **Pasul făcut (`45dfc77`, doar adăugări):** `Journal::push_text`; `chain::run_chain_ready` scrie după `pas X: ESEC` rândul **`text motivul esecului = "…"`** (și pentru pașii opriți
    de poartă) — **OS-ul n-are nimic de schimbat, doar legarea**; `gsp::golden::QueueTransportBellKeep` + `journal_skipped` (mesajele GSP-RM sărite în timpul unui apel RM, NOCAT decodat —
    opțional pentru OS, o schimbare în `OsRm::call`); `compara_variante` arată motivul („fara motiv in jurnal” la jurnalele vechi). T124 a–e, **455 PASS**, CI verde (rulările 181, 182).
    Nota pentru OS: `cyber-gpu/integration/cyber-universe/os-295_i9-motiv-in-jurnal.md`.
  - **Văzut în hub la 18:30, neanalizat încă (sesiunea următoare):** repetarea variantei 1 (18:00, `gpu-jurnal-011.txt`) a picat la **I7 timeout** cu jurnalul la ~1 s/rând (C-113: stickul);
    `gpu recupereaza` (C-103, 18:13, `gpu-jurnal-012.txt`): **Booter Unload → SEC2 MAILBOX0 = 0x88**, WPR2 rămâne ridicat → recuperarea fără cablu nu merge încă. Ambele cer analiză
    (0x88 după regula trei surse: RM descarcă GSP-RM întâi cu RPC-ul de unload; dacă I7 e sensibil la pauzele lungi dintre scrieri).
- **Sesiunea 92 (13:25–13:40) — oprire scurtă, fără pas nou pe driver (a treia la rând: 90, 91, 92).** Nimic nou pentru cyber-gpu în hub (C-110 în vigoare; Kronos are placa, S103/S104 gata),
  niciun jurnal nou de pe placă (ultimul: `gpu-jurnal-009.txt`, os-283). OS-ul a publicat `os-293`/`os-294`/`os-295` (mouse USB, `log mmio` — pasul 1 din P6-12, testul `remote` în CI) —
  **nimic schimbat în partea GPU**, `kernel/Cargo.toml` leagă tot `49e6685` (toate cele 5 crate-uri). Verificat: CI verde pe `bc864e3` (rularea 179); codul neschimbat de la `b1d91a0` (451 PASS).
  **Regula 8, citită cinstit:** trei rulări fără pas, dar nu din împotmolire — singurul pas următor are nevoie de placă. Nu e „OPRIT: necesită analiza lui Adrian” (nu e nimic de analizat),
  ci **AȘTEAPTĂ PLACA**: rulările programate rămân opriri scurte până apare în hub un jurnal nou sau o comandă nouă pentru cyber-gpu. Doar documentul de stare (`c651bf5`); copia C-34 la `c651bf5`.
- **Sesiunea 91 (07:25–07:40) — oprire scurtă, fără pas nou pe driver.** C-110 (06:49): Adrian nu mai ajunge azi la test → **testul cu variante (C-108) se amână** la următoarea
  lui venire, anunțată prin centrul de comandă; placa e a lui Kronos toată ziua și la noapte. Nimic nou pentru cyber-gpu în hub, niciun jurnal nou de pe placă (ultimul: `gpu-jurnal-009.txt`, os-283).
  Verificat: CI verde pe `fbc70e7` (rularea 178); codul driverului neschimbat de la `b1d91a0` (451 PASS); Release-urile OS neschimbate. Doar documentul de stare (`bc864e3`); copia C-34 la `bc864e3`.
  **Lista „pentru joi” de mai jos rămâne valabilă pentru ziua în care vine Adrian** — nimic de schimbat pe stick (`os-289` sau `os-290`).
- **Sesiunea 90 (01:25–01:45) — oprire scurtă, fără pas nou pe driver (fără jurnal nou de pe placă nu se inventează lucru).** Verificat: `tools/check.sh` pe `b1d91a0` → 451 PASS, CI verde (rularea 177);
  OS-ul leagă `49e6685` (toate cele 5 crate-uri, `kernel/Cargo.toml`), care conține variantele (`20830f5`) → **Release `os-289` și `os-290` au cele 10 variante** (`gpu variante`, `gpu lant --varianta N`);
  `compara_variante` rulată dintr-un checkout proaspăt pe 009/008/007 → aceleași cifre ca în sesiunea 89, cod de ieșire 0. Doar documentul de stare (`fbc70e7`); copia C-34 la `fbc70e7`.
  **Pentru joi:** lista de mai jos rămâne valabilă; stick-ul de test = `os-289` sau `os-290` (același cod GPU).
- **Sesiunea 89 (19:25–19:55) — nicio comandă nouă pentru cyber-gpu; pregătirea pentru joi.**
  - **OS-ul a legat variantele:** `cyber-universe` `028369a` (P6-78: cyber-gpu `49e6685`, `gpu variante`, `gpu lant --varianta N`, varianta pe ecran înainte de DA și în jurnal;
    13/13 scenarii). Am citit codul OS față de nota noastră: `gpu_i7::prepare` pune RPC-urile în coadă după `CpuQueues::init`, `booter` sună soneria înainte de Booter,
    `gpu_i8::init` întreabă `init_rpcs_ready_for_i8`, rândurile variantei sunt **primele** din `gpu-jurnal-NNN.txt` — totul ca în notă, nimic de trimis OS-ului.
    CI-ul OS (289) pornit 19:26, încă în lucru la 19:45 (pasul apt pe mașinile GitHub e lent azi); Release-ul `os-289` vine din el (sesiunea OS îl urmărește).
  - **Nou (doar adăugări, text, fără placă):** `nvidia_ga104::variant_log` + unealta de pe gazdă **`compara_variante`** — joi vin 5–10 jurnale de ~2500 de rânduri; unealta le pune
    într-un singur tabel față de referința os-283 (`gpu-jurnal-009.txt`): varianta (numărul + numele din jurnal), commit-ul, rezultatul I8 (`I8 TRECUT` **doar** cu
    `pas i8-gsp-init: ok`; altfel `rpc_result` + numele), NOCAT primite / adrese de assert, setările, și **rândurile care diferă de referință** fără zgomot (prefixul `[ timp]`,
    antetul, marcajele de timp NOCAT, `asteptat …`, rândurile variantei). Concluzia numește varianta care a trecut sau „nicio varianta nu a trecut de I8”.
    `cargo run --release -p nvidia-ga104 --example compara_variante -- 0x9c66000 gpu-jurnal-009.txt <jurnalele de joi>...`
  - **Pe jurnalele reale** (os-279/280/283): cifrele sesiunilor 85–88 regăsite; în plus, os-280 față de os-283 diferă în **2 rânduri** pe care diff-ul de mână din sesiunea 88 le
    omisese: `SEC2 CPUCTL` 0x10 vs 0x20 și `GSP MAILBOX0` 0xcb vs 0 (citiri ale stării plăcii la același moment; nu schimbă concluzia — același 0x59, aceleași 844/16).
  - T123 a–e (inclusiv jurnalul ferestrei complete SIMULATE cu varianta 1, cu prefixul OS-ului, citit înapoi). **451 teste PASS**, clippy, format, build no_std; CI verde pe
    `b1d91a0` (rularea 43071432423, 50 s). Copia din hub (C-34) la `b1d91a0`.
- **Sesiunea 88 (17:30–18:20) — după os-283 + C-108.**
  - **Jurnalul `gpu-jurnal-009.txt` (os-283, `bDmemStack = 1`) e identic cu `gpu-jurnal-008.txt` (os-280)** — rând cu rând, în afara marcajelor de timp: aceleași 844 de asserturi,
    aceleași adrese, `GSP_INIT_DONE 0x59`. Deci `bDmemStack` nu era cauza (OBSERVAT).
  - **Ce diferă față de toți cei patru driveri e ORDINEA, nu conținutul:** RM 570.144, tinygrad, nouveau și nova-core pun `SetSystemInfo` + `SetRegistry` (și soneria) în coada de
    comenzi **înainte** ca Booter să pornească GSP-RM. Noi le puneam la I8, după I7 — în jurnal, soneria vine la ≈ 0,3–0,4 s după pornirea GSP-RM. NVIDIA scrie chiar de ce contează
    (570.144, MIT): GSP-RM le rulează „*in early boot before OBJGPU is created*” și „*GSP-RM may skip these RPCs if not sent in time*”. **DEDUS:** GSP-RM citește coada o dată, la
    pornire; fără `SetSystemInfo` își face OBJGPU fără BAR-uri și ID-uri PCI → asserturile în lanț, apoi `NV_ERR_OPERATING_SYSTEM`. Se potrivește cu jurnalul identic de la os-278
    la os-283, orice am schimbat în conținut. Studiul: `cyber-gpu/docs/os-283_ANALIZA_ORDINE_RPC.md`.
  - **C-108 gata (partea GPU, SIMULARE):** modulul nou `nvidia_ga104::gsp::variants` — **10 variante numerotate**, fiecare cu nume, „ce schimbă” (ro) și sursa:
    **1 `rpc-inainte`** (doar ordinea: RPC-urile + soneria la I7, înainte de Booter — cea mai probabilă), 2 +setul nova-core (hostPageSize 0, bIsPrimary 0, RMDevidCheckIgnore),
    3 +setul tinygrad (bIsPassthru 1, bIsPrimary 0, hostPageSize 0), 4 +setul nouveau, 5 +CLOCK_BOOST (RM), 6 +doar bIsPassthru, 7 +doar RMDevidCheckIgnore, 8 +stiva LibOS
    (bDmemStack 0), 9–10 ordinea veche + seturile tinygrad/nova (dacă ordinea nu era cauza). Toate valorile din surse publice; niciun registru nou. Valorile trimise ajung în jurnal
    (`valoare varianta I8 (C-108): numarul = …`, `text varianta I8: numele = "…"`, câte un rând pe setare).
  - **SIMULARE (T122):** modelul GSP-RM consumă la „pornire” ce e în coadă și răspunde `0x59` dacă lipsesc cele două RPC-uri — ordinea os-283 dă exact `0x59`, varianta 1 dă `0`
    (modelul e scris după comentariile RM, nu după placă — dovada e joi). `verifica_jurnal_lant` acceptă noua ordine a I7 (soneria înainte de resetul GSP).
  - Nota pentru OS: `cyber-gpu/integration/cyber-universe/C-108_variante-i8.md` (funcțiile, schimbările în `gpu_i7`/`gpu_i8`, `gpu variante`, procedura).
  - 445 teste PASS, clippy, format, build no_std; CI verde pe `20830f5` (rularea 174, 57 s); `6611c27` (doc) în curs. Copia din hub (C-34) la `6611c27`.
- **Sesiunea 87 (14:25–15:20):** comparația câmp cu câmp cu patru drivere (C-107) → `bDmemStack = 1` (`b3ac503`); conținutul jurnalelor PMU în jurnal (`d3c5351`). Infirmat de os-283 ca
  fiind cauza; rămâne valoarea corectă (toți o au 1).
- **Sesiunile 84–86:** jurnalul I8 numește sursa erorii (`d31ad8d`), decodează NOCAT (`5cfe523`), rezumatul NOCAT în `verifica_jurnal_lant` (`a669387`); C-103 partea GPU în SIMULARE
  (`364ece2`: Booter Unload → WPR2 = 0 → I6 din nou fără pornire rece; `gpu_pci::caps`).
- **Pe placă până acum:** I0–I4 doar citire TREC; I6 TRECE (os-242…os-283); I7 TRECE (os-246…os-283); I8: toate cele 420 de comenzi ale secvențiatorului trec, GSP-RM pornește și
  răspunde `GSP_INIT_DONE 0x59` (os-278, os-279, os-280, os-283 — identic); I9–I14 neîncercate.

## Lista pentru testul următor pe placă (după os-295)
0. **Întâi stick-ul (C-113, OS-ul).** La ~13 ms/rând lanțul I6 → I8 durează ~35 s; la ~1 s/rând ~25 de minute, și I7 a picat exact în rularea lentă. Testul se repetă **după** ce stick-ul scrie normal.
1. Release OS care leagă `cyber-gpu` **`3404313` sau mai nou** (conține `e49ca76` = varianta 1 implicită, `45dfc77` = motivul pe stick, `85e0a34` = starea plăcii după un I7 eșuat).
2. Pornire rece → `gpu lant` (fără `--varianta`) → `DA` → după repornire `trimite`. Ecranul va îngheța la pornirea GSP-RM (așteptat); jurnalul merge pe stick.
3. **Ce căutăm în jurnal:** dacă I7 pică: rândurile `valoare …` de după `nota: I7: …` (SCRATCH_14 bitul 26 = Booter a predat etapa 3?; `GSP MAILBOX0` = 0 → încărcătorul a rulat); dacă I9 pică:
   `text motivul esecului = "…"` (cod `NV_STATUS` numit; „timeout dupa 5000000 us” → GSP-RM blocat pe promovarea virtuală). `compara_variante 0x9c66000 gpu-jurnal-010.txt <jurnalul nou>`.
4. **`gpu recupereaza` NU se mai rulează** până nu decide Adrian despre FWSEC-SB înainte de Booter Unload — ar da același 0x88 (acum cu starea plăcii în plus). Pornirea rece rămâne calea.
5. Varianta 11 `rpc-inainte+neprimar` (doar `bIsPrimary = 0`): de încercat **după** `gpu lant` simplu, doar dacă Adrian vrea ecranul înapoi; efect DEDUS.
6. Dacă I9 trece: I10 (add64) e primul calcul pe placă — jurnalul lui se citește cu `verifica_jurnal_lant`.

## Urmează
1. **OS-ul:** C-113 (stick-ul) înaintea oricărui test; apoi legarea `3404313`+ → Release (opțional `QueueTransportBellKeep` + `journal_skipped` în `OsRm::call`, nota os-295 §2).
2. **Adrian, la următoarea venire:** un singur test, `gpu lant` + `trimite` (lista de mai sus). Decizia despre FWSEC-SB înainte de Booter Unload (C-103), când vrea.
3. **Noi, după jurnal:** I7 picat → rândurile stării spun unde (nu ghicim înainte); I9 picat cu cod RM → regulile `PROMOTE_CTX` (mărimi/aliniere, VA space prin context share, `engineType`);
   timeout → tabelele de pagini / `SET_PAGE_DIRECTORY`. Fără jurnal nou, nimic altceva pe driver.
4. După I9: I10 (add64), I11–I14 — scrise, testate doar în simulare.

## Ce oferă proiectul celorlalți
- **Sesiunea 94 (doar adăugări + o valoare):** `nvidia_ga104::gsp::falcon::{journal_i7_failure, I7_FAIL_RISCV_OFF, I7_FAIL_BOOTER_CODE, UNLOAD_FAIL_STATE, I7_FAIL_EXTRA_READS}`;
  `falcon::RISCV_ACTIVE_US` = 5 000 000 (era 2 000 000). `booter_load_dma_libos` / `booter_unload_dma` scriu singure starea plăcii la eșec — OS-ul compilează neschimbat, doar leagă.
- **Sesiunea 93, 18:45 (schimbare de comportament, semnătura neschimbată):** `variants::settings(None)` dă varianta 1 (nu `OS_283`); `Some(0)` refuzat; `journal(None)` scrie numărul 1 + rândul nou `text varianta I8: aleasa`; `variants::{DEFAULT, default_variant}`; `VARIANTS` are 11 intrări (varianta 11 nouă, numerele vechi stabile). Textele OS „ca os-283” de corectat (nota §5).
- **Sesiunea 93 (doar adăugări):** `gpu_core::diag::Journal::push_text`; `nvidia_ga104::chain::{STEP_FAIL_REASON, STEP_FAIL_REASON_MORE}` (motivul după `pas X: ESEC`, automat în
  `run_chain_ready`); `gsp::golden::{QueueTransportBellKeep, SKIPPED_KEEP_MAX, journal_skipped, SKIPPED_TOTAL, SKIPPED_AT}`; `variant_log::VariantRun::{fail_reasons, fail_reason}`.
  `QueueTransportBell` și tot restul neschimbate — OS-ul compilează neschimbat.
- **Sesiunea 89 (doar adăugări, text):** `nvidia_ga104::variant_log::{read, compare, strip_prefix, is_noise, VariantRun, Outcome, Difference, Table, TableRow}` + exemplul `compara_variante`. Codul driverului neschimbat.
- **Sesiunea 88 (C-108, doar adăugări):** `nvidia_ga104::gsp::variants::{Settings, Variant, VARIANTS, OS_283, list, get, settings}`; `Settings::{encode_sysinfo, encode_registry,
  encode_wpr_meta, encode_gsp_args, queue_init_rpcs, init_rpcs_ready_for_i8, journal}`; `sysinfo::{Options, encode_with, off::B_IS_PASSTHRU}`, `registry::{boot_entries_with,
  devid_check_ignore}`, `wpr_meta::{encode_with_flags, FLAG_CLOCK_BOOST}`, `libos::encode_gsp_args_with`, `msgq::CpuQueues::rpcs_sent`; `sim_peer::SimGsp::{start_early_boot,
  init_done_result, early_boot}`. **Funcțiile vechi (`sysinfo::encode`, `registry::boot_entries`, `wpr_meta::encode`, `libos::encode_gsp_args`) dau exact ce dădeau** — OS-ul
  compilează neschimbat; variantele intră doar prin schimbările din nota C-108.
- **Sesiunea 87:** `libos::encode_gsp_args` cu `bDmemStack = 1`; `nocat::LibosPrint::buf` (conținutul jurnalelor PMU).
- **Sesiunile 84–86:** `Event::Value`, `Event::Text`, `nvidia_rm570::names`, `gsp::nocat`, `gsp::nocat_log`, `falcon::{booter_unload, booter_unload_dma}`, `gpu_pci::caps::reset_capabilities`.
- **Mai vechi (toate doar adăugări):** C-99 `falcon::start_cpu` + `Clock::abort_requested`; C-96 `falcon::switch_to_falcon`; sesiunea 68 `chain_log`; sesiunile 57–65 I11–I14, `kronos_gen`,
  `recovery`; sesiunea 51 `falcon::booter_load_dma_libos`. Lista completă: `cyber-gpu/docs/IMPLEMENTATION_STATUS.md` și `cyber-gpu/integration/cyber-universe/`.
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). `kronos` / K6-CPU: operatorii pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: **C-113** (stick-ul care nu scrie / scrie la ~1 s/rând) înaintea testului; legarea `cyber-gpu` `3404313`+ → Release; opțional §2 din
  `integration/cyber-universe/os-295_i9-motiv-in-jurnal.md`.
- De la Adrian: un test, `gpu lant` cu Release-ul nou și stick-ul reparat, `trimite` după repornire. Și o decizie (fără grabă): FWSEC-SB înainte de Booter Unload pentru `gpu recupereaza` (C-103) — DA/NU.
- De la `cyber-universe` (P6-66, mai târziu): `Generation::run` + `VramBudget::check` în `kronos --gpu`, `recover` la erori; 32 KiB pushbuffer pentru 24 de straturi.

## Blocaje / nevoie de Adrian
- **Nu e blocat:** următorul pas pe driver depinde de jurnalul următor de pe placă (I7 cu starea plăcii, sau motivul lui I9). Fără jurnal nou nu inventăm lucru.
- **I7 a picat o dată din două azi** (jurnalul 011) fără cauză stabilită; singura variabilă: stick-ul lent (C-113, OS). Dacă se repetă cu stick-ul reparat, rândurile noi ale stării spun unde.
- **`gpu recupereaza` (C-103) nu merge pe placă** (Booter Unload 0x88, cod nepublicat); varianta cu sursă (FWSEC-SB înainte, ca RM) e un program semnat în plus → doar cu DA-ul lui Adrian.
- Ecranul care îngheață după pornirea GSP-RM: nu avem o setare publică, cu sursă, care să țină GSP-RM departe de afișaj; varianta 11 (`bIsPrimary = 0`) e o probă cu efect DEDUS.
- Numele funcțiilor din care vin asserturile nu se pot afla fără simbolurile GSP-RM — nu deschidem firmware-ul (regula proiectului).
- CI GitHub VERDE pe `3404313` (push-ul cu `85e0a34` + `3404313`; rularea 43273728070), `ea50749` (43274217367) și `3d61b04` (43274259743).
