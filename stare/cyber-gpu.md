# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-23 13:55 (ora României) · **de:** sesiunea Cyber-GPU programată (cloud, fără placă)

## Acum
- **Nimic nu s-a testat pe RTX 3070 Ti.** Tot ce scrie „merge” e verificat doar pe calculator, în SIMULARE. Niciun program nu a rulat pe GPU.
- **Datele reale ale workstation-ului** (inventarul K0) sunt în `docs/HARDWARE_WORKSTATION.md` și în simulare. Concluzie: pornirea plăcii
  **nu depinde** de ReBAR sau Above-4G; nu trebuie schimbat nimic în BIOS. VT-d oprit = mai simplu, dar fără plasă de siguranță.
- **Pașii I2 și I3 sunt scriși** (doar citire, cu limite de timp): „a terminat placa pornirea?” și „citim VBIOS-ul”. Pornirea se oprește
  acum cinstit la **I4** (licența firmware-ului NVIDIA), nu la I2.
- **Calcul pe procesor (pentru Kronos în OS):** înmulțirea de matrice pe blocuri și cu greutăți bf16, identică bit cu bit cu varianta de
  referință, de ~12 ori mai rapidă pe calculator. Conversia bf16 verificată pe toate cele 65 536 de valori.
- **CI activ pe GitHub** și verde. 82 de teste trec. Totul e pe ramura `g0-g2-fundatie` (`main` nu există).

## Urmează
- Fără placă: extragerea descrierii FWSEC din VBIOS (doar citire, pe imagine sintetică) și calculul regiunilor de memorie pentru GSP.
- Cu placa (când revine Adrian): testul I0–I3, după ce OS-ul are comenzile `gpu gfw` / `gpu vbios` (propunere în `integrare/cyber-gpu/`).
- Cercetarea I4–I8 e scrisă: `docs/RESEARCH_I4_I8.md`.

## Ce oferă proiectul celorlalți
- `cyber-universe`: procedura exactă pentru `gpu gfw` și `gpu vbios` (doar citire) — `integrare/cyber-gpu/2026-10-23_I2-I3_comenzi-gpu-gfw-vbios.md`.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor + matmul rapid cu greutăți bf16 (format f32/bf16).

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: comenzile `gpu gfw` și `gpu vbios`, doar după „da”-ul lui Adrian.
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian (nimic urgent; când se întoarce)
- **Licența firmware-ului NVIDIA** (blochează tot de la I4 încolo): îl folosim sau nu? Argumentele pro/contra: `docs/RESEARCH_I4_I8.md` §5.1.
- **Compilatorul pentru programele GPU:** Mesa NAK (MIT) sau `ptxas` (NVIDIA). Recomandarea tehnică: NAK pentru primul program (§5.2).
- **Fereastra pe workstation (~30 min, Kronos oprit):** `gpu identifica`, apoi `gpu gfw` și `gpu vbios` dacă OS-ul le are; lista: `docs/TEST_MATRIX.md` partea B.
  Notează și poza din BIOS cu „Above 4G Decoding”.
- „Da” pentru propunerea către OS (comenzile `gpu gfw` / `gpu vbios`).
