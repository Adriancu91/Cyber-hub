# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-11 18:20 (ora României) · **de:** sesiunea Cyber-GPU 88 (cloud, fără placă) — **os-283: `bDmemStack` nu era cauza; cauza probabilă a lui `0x59` e ORDINEA (RPC-urile de pornire ajungeau la GSP-RM după ce pornise); C-108: 10 variante numerotate gata pentru joi (`20830f5`/`6611c27`, 445 PASS, CI verde).**

## Acum
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

## Lista pentru joi 12 nov ~07:00 (C-108; Release-ul îl face sesiunea OS, P6-78)
1. Fiecare variantă = o pornire rece: oprire → cablu 30 s → F8 stick de test → `gpu lant --varianta N` → `DA` → `trimite` (sau jurnalul în `rezultate/`) → `N+1`. **Începe cu 1.**
2. **Reușita:** după `secv #419 CORE_RESUME`, rândul `valoare GSP_INIT_DONE: rpc_result … = 0x00000000` și lanțul intră în **I8e (golden)**. Se oprește la prima variantă care trece.
3. Dacă varianta 1 dă tot `0x59`: de văzut câte înregistrări NOCAT (844 iar?) și dacă rândul `varianta I8 … numarul = 0x00000001` e în jurnal (altfel Release-ul nu are variantele).
4. Opțional, după un lanț oprit: `gpu recupereaza` + `DA` (C-103, prima probă) — dacă WPR2 citește 0, următoarea variantă merge fără cablul scos.

## Urmează
1. **OS-ul (P6-78):** leagă `20830f5` (sau `6611c27`), `gpu variante`, `gpu lant --varianta N`, jurnalul și raportul cu numărul variantei → Release înainte de joi 06:00.
2. **Joi:** jurnalele variantelor în hub; noi rulăm `verifica_jurnal_lant <jurnal> 0x9c66000` pe fiecare. Dacă varianta 1 trece → I8e (golden) pe placă = primul apel RM; se citește jurnalul.
   Dacă nu trece niciuna din cele 10: următoarea comparație e starea plăcii/memoriei (adresele DMA reale, ce vede GSP-RM în RAM), nu conținutul mesajelor.
3. După `GSP_INIT_DONE = 0` pe placă: I8e, I9, I10 — scrise, testate doar în simulare.

## Ce oferă proiectul celorlalți
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
- De la `cyber-universe` (P6-78, **până joi 06:00**): legarea `cyber-gpu` ≥ `20830f5`, `gpu variante`, `gpu lant --varianta N`, numărul variantei în jurnal și raport — după nota
  `C-108_variante-i8.md` (schimbări mici în `gpu_i7.rs` / `gpu_i8.rs`: RPC-urile + soneria înainte de Booter când varianta o cere).
- De la Adrian (joi): variantele în ordine, de la 1, câte o pornire rece; pozele/jurnalele în hub.
- De la `cyber-universe` (P6-66, mai târziu): `Generation::run` + `VramBudget::check` în `kronos --gpu`, `recover` la erori; 32 KiB pushbuffer pentru 24 de straturi.

## Blocaje / nevoie de Adrian
- **Nu e blocat, dar depinde de placă:** că ordinea e cauza lui `0x59` e DEDUS din sursele RM (comentariile citate în studiu), nu probat; doar joi, cu varianta 1, se vede.
  Fiecare variantă e „prima încercare” pe placă; toate valorile vin din surse publice și niciuna nu scrie un registru pe care os-283 nu-l scria deja; „DA” la fiecare.
- Numele funcțiilor din care vin cele 844 de asserturi nu se pot afla fără simbolurile GSP-RM — nu deschidem firmware-ul (regula proiectului); decizia ar fi a lui Adrian.
- CI GitHub VERDE pe `20830f5` (rularea 174, 16:01 UTC, 57 s); `6611c27` (doar documente) în curs la ora scrierii.
