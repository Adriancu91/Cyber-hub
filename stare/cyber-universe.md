# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-06 11:45 (ora României) · **de:** sesiunea OS programată (11:40) · Release de testat: **`os-251`** (CI verde; pe placă identic cu `os-250`)

## Acum
- **`os-251` (P6-59, propunerea cyber-gpu sesiunea 54):** cyber-gpu fixat pe `657e209`; în `gpu lant --sim` Booter-ul modelului lărgește singur WPR2 din
  `GspFwWprMeta`-ul pregătit de OS (recitit din RAM), ca placa (`0x1f4100000`) — OS-ul nu mai pune valoarea de mână. Pe placă: nimic schimbat față de `os-250`.
- **`os-250` (P6-58, propunerea cyber-gpu sesiunea 53):** înainte de golden, OS-ul recitește WPR2 (2 citiri, nicio scriere) și ia zona VRAM din
  `FbLayout::free_after_i7` (cyber-gpu fixat pe `60740a3`). Dacă Booter a pus WPR2 altundeva decât a cerut `GspFwWprMeta`, golden se oprește **înainte de
  prima scriere în VRAM**. Pe valorile plăcii din 5 nov zona e aceeași (`0x10000000-0x1f4000000`). Nicio scriere nouă față de `os-249`.
- **`os-249` (P6-56 pas 3, C-72):** `gpu lant` are și I10, ultimul pas: programul `add64` (64 de adunări) rulat pe placă prin canalul de lucru deschis la I9,
  rezultatul citit înapoi din memoria plăcii și comparat **bit cu bit** cu procesorul; apoi costul unei lansări (16 lansări, ceasul plăcii).
  Scrieri NOI față de `os-248` (niciodată încercate pe placă): invalidarea TLB (3 registre) și **soneria canalului `0xBB0090`**, o dată pe pas, printr-un gard
  care permite doar acel registru și doar jetonul primit de la GSP-RM. Dacă placa nu răspunde în 2 s → oprire curată, Bus Master la loc.
- În SIMULARE tot lanțul trece (13 pași). Pe placă: neîncercat de la I8 încolo cu reparația C-75.
- C-72 (I7–I10) e acum **gata** în OS. `os-248` rămâne valabil, dar `os-249` îl cuprinde.

## Urmează
- Fereastra de azi (6 nov, C-79) pe workstation cu `os-250` sau `os-251` (identice pe placă; pașii mai jos); când apar jurnalele în `rezultate/`, `verifica_jurnal_lant` și analiza I6–I10 în sesiunea OS următoare.
- La 11:40 jurnalele ferestrei de azi nu sunt încă în `rezultate/`. Dacă nici sesiunea următoare nu le găsește (și nu e comandă nouă), sesiunile OS se opresc cu „OPRIT” până se uită Adrian (3 sesiuni la rând fără sarcină).
- Coada OS nu mai are sarcini libere fără hardware.

## Ce oferă proiectul celorlalți
- `gpu lant` I6 → I10 pe stick-ul de test; jurnalul fiecărui pas pe stick (`/usb/raport/gpu-jurnal-NNN.txt`) pentru `verifica_jurnal_lant`.
- Al doilea stick la `/usb2` (doar citire) pentru firmware.
- Actualizarea cu revenire, `compara`, `log --sumar`, `timp`, `hw lista`, `web`, remote criptat; bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

## De ce are nevoie de la ceilalți
- **`cyber-gpu`:** mulțumim — `wpr_meta_mem` e folosit din `os-251` (simularea trece fără valoare pusă de mână; `add64.sm86.sass` identic și în `657e209`).
  După fereastră: `verifica_jurnal_lant` pe jurnalele din `rezultate/`.

## Blocaje / nevoie de Adrian
- **La fereastra următoare pe workstation, `os-251` pe stick-ul de test** (`cyber-universe-gpu-scrie-usb.img` din Release-ul `os-251`, scris cu Rufus; `os-250` merge la fel):
  1. **Bagă ambele stick-uri**: stick-ul de test și stick-ul normal cu `firmware\nvidia\ga102\gsp\` (cele 4 fișiere).
  2. Pornire rece (cablul scos 30 s), pornire de pe stick-ul de test. Poză la rândul `fs: /usb2: ...`.
  3. `gpu firmware` → poză („fisiere oficiale 4/4”). `gpu pregatire-i6` → poză.
  4. `gpu lant` + `DA` **o singură dată** → poze la toate rândurile. Așteptat: I6 și I7 TREC (cutia GSP `0x110040` păstrează adresa LibOS);
     apoi I8, golden, I9, I10. La I10 rândul important: „pas I10 add64: ok (64 rezultate identice bit cu bit…)” sau ESEC cu motivul.
  5. `raport`, jurnalele `/usb/raport/gpu-jurnal-*.txt` în `rezultate/<data>-workstation-os251/`. Oprire completă (cablul scos 30 s).
- **Jurnalele de la fereastra de azi (6 nov):** pune `/usb/raport/gpu-jurnal-*.txt` și pozele în `rezultate/2026-11-06-workstation-os250/` (sau `-os251`); fără ele OS-ul nu are ce lucra și se oprește singur după sesiunea următoare.
- Token GitHub „fine-grained” doar pentru `Adriancu91/Cyber-hub` (Contents: Read and write) ca `github.token` pe stick — când vrei.
