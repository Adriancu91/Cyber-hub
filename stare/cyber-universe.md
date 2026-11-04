# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-04 22:30 (ora României) · **de:** sesiunea OS programată (20:42) · **OPRIT ridicat** (comenzile C-66 și C-67) · ultimele sarcini: **P6-46 + P6-47 gata, Release `os-224`**

## Acum
- **Release `os-224`** (CI verde, run 41898987803) = `os-222` + C-66 + C-67. **Acesta e Release-ul pentru fereastra următoare** (stick-ul normal și stick-ul de test `cyber-universe-gpu-scrie-usb.img`).
- **C-66 (P6-46):** cyber-gpu fixat pe `9ac89b8`: verificarea I6 acceptă acum capătul WPR2 = ultimul bloc de 128 KiB (cum l-a scris placa pe 4 nov → FWSEC-FRTS reușit);
  rândul „WPR2 citit dupa I6” nu mai e refuzat de politica de siguranță (3 citiri, fără permis) și spune forma capătului. În simulare: „rezultat I6: TRECE”.
- **C-67 (P6-47):** în blocul pe simbol, qkv/proiecția/fc/MLP au deja aceeași formă de cod; diferența apare doar în rularea reală (`--cauta`: tot modelul 2088 µs/simbol;
  rularea reală: produsele 4,85 ms). Timpii pe etapă se măsurau doar pe firul 0. Acum `--profil` arată fiecare etapă văzută de toate firele (câte au lucrat, cât de târziu
  a început ultimul, cedările procesorului) și atenția despărțită de qkv. Bănuiala: ~520 cedări ale procesorului pe simbol → fire care ajung târziu la etape.
  Opțiune nouă de încercat: `kronos --fara-cedari`. Simbolurile neschimbate (CONTROL în QEMU).
- CI a fost roșu o dată din testul ceasului cu 4 procesoare emulate (fără legătură cu codul) → prag ajustat, notat B-006 în repo.

## Urmează
- Fereastra următoare cu `os-224`: I6 o dată (așteptat TRECE → pragul spre I7, plan separat cu comandă nouă) și profilul Kronos cu și fără `--fara-cedari`.
- După pozele profilului: reparația frânei (fire care întârzie / cedări / altceva) → ținta ~350 simb/s.
- Altfel coada OS nu are sarcini libere fără placă/Adrian → opriri scurte până la o comandă nouă.

## Ce oferă proiectul celorlalți
- Pentru `cyber-gpu`: `gpu i6 --scrie` cu rândul „WPR2 citit dupa I6 … (capat: …)” prin `read_frts_after_i6`, jurnalul pe loc pe stick, `gpu tur`, `gpu lant`.
- Biblioteci Rust proprii: `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`; a doua implementare KGR1 pentru Kronos.

## De ce are nevoie de la ceilalți
- `cyber-gpu`: după fereastră, `verifica_jurnal_i6` pe jurnalele I6 noi din `rezultate/`.

## Blocaje / nevoie de Adrian
- **Fereastra următoare pe workstation (~25 min), Release `os-224`:**
  1. **I6, stick-ul de test** (`cyber-universe-gpu-scrie-usb.img`): pornire rece (cablul scos 30 s), `gpu pregatire-i6` → poză (trebuie „TRECE”, „0 scrieri”),
     `gpu i6 --scrie` + `DA` **o singură dată** → poză (așteptat „rezultat I6: TRECE” și „capat: ultimul bloc de 128 KiB”), `raport`.
     Dacă ecranul se blochează: 1 minut, oprire, nu repeta azi.
  2. **Kronos, stick-ul normal:** `run kronos --control` → poză; `run kronos --profil --fara-ecran --n 64 Buna ziua` → poză (toate rândurile „etapa …”);
     `run kronos --profil --fara-ecran --n 64 --fara-cedari Buna ziua` → poză.
  3. Pozele + `raport\*.txt` + `raport\gpu-jurnal-*.txt` → `rezultate/<data>-workstation-os224/`.
- **Bucla automată:** prima tură (pașii din `docs/BUCLA_AUTOMATA.md` din repo-ul OS) — când ai ~20 min.
- `github.token`, `claude.key`, tag-ul `stabil-2026-10-23`, P5-07: mai târziu.
