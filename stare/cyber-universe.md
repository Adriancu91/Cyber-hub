# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-11 21:05 (ora României) · **de:** sesiunile OS programate (17:40, 20:40) — CI reparat, P6-77 (os-288), **C-108 gata (os-289)**, **C-109 gata (os-290)**.

## Acum
- **Release `os-289` (≈19:58, CI verde) — pe acesta îl folosește Adrian joi la 07:00 (C-108).** Are cele 10 variante de setări I8 de la
  Cyber-GPU (`49e6685`): `gpu variante` le arată, `gpu lant --varianta N` o alege (pe ecran înainte de DA, în jurnal și în raport;
  număr greșit = nimic scris; fără `--varianta` = exact ca os-283). Testat doar în SIMULARE (QEMU).
- `os-288` = os-283 + conținutul celor 2 mesaje PMU în jurnal (P6-77). `os-289` le are pe toate.
- **CI reparat:** serverele de pachete Ubuntu (`azure.archive.ubuntu.com`, `archive.ubuntu.com`) nu răspundeau; CI-ul ia acum pachetele
  de la oglinda kernel.org când primul încercat nu merge (4 rulări până la verde).
- **Release `os-290` (≈20:54) = os-289 + C-109 (P6-79):** pe ASUS TUF pornirea stătea după `acpi: MADT` — cel mai probabil ceasul PIT
  oprit de firmware (o buclă de așteptare fără limită). Acum așteptarea are limită, calibrarea trece pe temporizatorul ACPI PM sau pe CPUID,
  APIC-ul merge și în modul x2APIC, iar pe ecran apar rânduri noi. Testat în QEMU cu PIT-ul oprit; pe ASUS neîncercat.
- Dacă apare `os-291` (CI pornit 20:55): **același cod ca `os-290`**, doar reparația pentru rularea CI săptămânală — oricare din ele e bun.
- C-105 (`ciclu-test`) rămâne oprit până la cele două chei ale lui Adrian.

## Urmează
- Poza de pe ASUS cu `os-290`: dacă pornește → C-109 închis; dacă nu, ultimul rând `apic: …` arată pasul.
- Jurnalele de joi: prima variantă care trece de I8 → Cyber-GPU (unealta `compara_variante`) → pasul următor.

## Ce oferă proiectul celorlalți
- `gpu lant [--varianta N]` I6 → I14, `gpu variante`, `gpu recupereaza`, `kronos --gpu` pe stick-ul de test; jurnale + rapoarte trimise în hub (cu token).
- `hub ruleaza` / `hub asculta`, `test tot`, `kronos --conversatie`, git pe ramuri `os/…`, `web`, `files`; bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

## De ce are nevoie de la ceilalți
- **`cyber-gpu`:** după jurnalele de joi, pasul următor (varianta care a trecut sau, dacă niciuna, următoarea ipoteză).
- **`kronos`:** Release-ul `kronos-kgr1-513` (opțional).

## Blocaje / nevoie de Adrian

**Joi 12 nov, ~07:00, la workstation — testul cu variante (C-108), Release `os-289`:**
1. Din Release-ul **`os-289`** (github.com/Adriancu91/cyber-universe → Releases) iei `cyber-universe-gpu-scrie-usb.img` și îl scrii cu
   Rufus pe **stick-ul de test**. Stick-ul normal rămâne cum e.
2. Pentru fiecare variantă, începând cu **1**: **oprire completă → cablul scos 30 s** → pornire de pe stick-ul de test (F8) →
   `gpu lant --varianta 1` → verifici pe ecran rândul „varianta I8 1: rpc-inainte …” → `DA` + Enter.
3. Ce contează: rândul `valoare GSP_INIT_DONE: rpc_result … = 0x…` — **`0x00000000` = varianta a trecut** (lanțul merge mai departe la
   `i8e-golden`); tot `0x59` = nu. **Poză** la rândul acesta și la rezumatul de la final.
4. `trimite` (sau `raport`, apoi pozele + `raport\gpu-jurnal-*.txt` în `rezultate/2026-11-12-workstation-os289/`).
5. Repeți de la pasul 2 cu varianta următoare (2, 3, … 10). **Te oprești la prima variantă care trece.** Lista completă: `gpu variante`.

(Merge la fel și cu `os-290`, care are aceleași variante plus reparația pentru ASUS.)

**Pe ASUS TUF (C-109), când ai 5 minute:** scrii `cyber-universe-usb.img` din Release-ul **`os-290`** pe stick-ul normal (Rufus), pornești
ASUS-ul de pe el și faci **o poză** la rândurile `apic: mod …`, `apic: calibrez ceasul …`, `apic: ceasul de referinta: …` — sau la ultima
linie, dacă tot se oprește. Dacă ajunge la desktop: `hw` + `test tot`, poze în `rezultate/<data>-laptop-asus-tuf/`.

**Opțional (C-104, ~5 min):** tokenul pentru `hub asculta` — `docs/USB.md` punctul 15.

**Când vrei (C-105):** ciclul de test automat e gata, dar **oprit**; îl pornești doar tu, cu cele două chei (`docs/USB.md` punctul 16).
