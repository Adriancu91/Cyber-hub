# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-07 11:55 (ora României) · **de:** sesiunea OS programată (11:40; nicio sarcină liberă, nimic schimbat) · Release de testat: **`os-268`** (CI verde) = `os-264` + managerul de fișiere pentru stick + CSS și imagini PNG în browser (pe placă nimic schimbat)

## Acum
- **C-84 (unelte spre independența de Windows) → P6-61 GATA** (toate testate în QEMU, nimic încă pe hardware):
  - **Nou azi — `files` pentru stick:** se deschide direct în stick; butoane „Nou” (dosar nou), „Nume” (redenumire), „Stick”; copiază și dosare întregi;
    un dosar plin se șterge doar la al doilea `s`; arată mărimile; după fiecare schimbare scrie imediat pe stick (îl poți scoate). Discurile calculatorului rămân neatinse.
  - **Nou azi — browserul `web`:** nu mai arată ce ascunde pagina (CSS de bază); `web --imagini` + `web --imagine N` arată o imagine **PNG** într-o fereastră
    (JPEG/GIF încă nu — spune cinstit). Decodorul PNG e scris de noi.
  - Deja: rapoartele pleacă singure în hub (cu `github.token` pe stick), `hub`, `kronos --intreaba`, git pe ramuri `os/…`, `test tot`, formulare în `web`, `ora`, setări pe stick.
- **C-83 → P6-62 GATA în SIMULARE:** `gpu lant` I6 → I14 și `kronos --gpu` (cere `DA`; la orice eroare continuă pe procesor). Pe placă: neîncercat de la I8.
- **C-82 → P6-60 GATA în OS:** `kronos` alege #513 de pe stick (apoi #477, #459). Lipsește doar fișierul real (Release-ul `kronos-kgr1-513`, luni cu Adrian).
- CI: reparată și instabilitatea veche a testului `revenire` (ordinea rândurilor de pe serial).

## Urmează
- **P6-63:** duminică seara (8 nov) lista exactă pentru fereastra de luni (aici, la „Blocaje / nevoie de Adrian”).
- Altfel nimic liber fără hardware; idei doar cu „da”: JPEG în browser, fereastră grafică de conversație pentru Kronos.

## Ce oferă proiectul celorlalți
- `gpu lant` I6 → I14 și `kronos --gpu` pe stick-ul de test (I11–I14 doar în SIMULARE), jurnal pe stick; rapoartele pot ajunge singure în `rezultate/os-automat/` (cu token).
- `hub`, `test tot`, `ora`, git pe ramuri `os/…`, `web` (formulare, CSS de bază, PNG), `files` pentru stick.
- Bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`; decodorul `png.rs` (DEFLATE + PNG, fără dependențe).

## De ce are nevoie de la ceilalți
- **`kronos`:** doar Release-ul `kronos-kgr1-513` (luni, cu Adrian — C-86 pct. 4). Nimic altceva.
- **`cyber-gpu`:** nimic nou de cerut acum (copia `d706cbb` e în OS).

## Blocaje / nevoie de Adrian
- **Release-ul modelului #513 (luni, pe workstation, în `C:\Kronos\cyberspace`):** comanda e în `integrare/kronos/MODEL.md` (`gh release create kronos-kgr1-513 …`).
  Apoi pe stick, în dosarul `kronos`: `kronos_513_q8_0.kgr` + `kronos_513_q8_0.kgr.sha256` (sau copiate din `lucru\export\`). Fără ele OS-ul folosește #477.
- **Tokenul GitHub pe stick:** GitHub → Settings → Developer settings → Fine-grained tokens → doar depozitul **`Cyber-hub`**, *Contents: Read and write*;
  salvat ca `github.token` (un rând) în rădăcina stick-ului. Cu el, jurnalele ferestrei ajung singure în hub.
- **Fereastra de luni pe workstation:** stick-ul de test cu `os-268` (`cyber-universe-gpu-scrie-usb.img`) + stick-ul cu firmware; lista exactă duminică seara.
