# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-23 03:05 (ora României) · **de:** sesiunea Cyber-GPU (Claude Code, laptopul lui Adrian)

## Acum
- **Cod pe GitHub, ramura `g0-g2-fundatie`** (`Adriancu91/cyber-gpu`, commit `94c629f`): 7 crate-uri Rust `no_std`, fără dependențe
  externe, MIT. **58 de teste trec pe laptop**; se compilează pentru ținta kernelului. Nimic pe `main`.
- **Gata, dar testat doar pe dispozitive SIMULATE:** identificarea plăcii la „nivel 0”. Citește doar configurația PCI și 2 registre
  publice (`NV_PMC_BOOT_0`, `BOOT_42`), cu **zero scrieri în placă** (verificat de teste).
- **Gata pe procesor:** operațiile lui Kronos în f32 (matmul, layernorm, GELU, softmax cauzal, embedding, atenție, cross-entropy).
  Sunt verificate față de o referință independentă și pot rula ca backend CPU. **Niciun program nu a rulat pe GPU.**
- Cercetare cu surse: pornirea plăcii cere firmware-ul semnat NVIDIA (GSP). Firmware propriu e imposibil, iar inițializarea se
  oprește onest la pasul I2 din 11.
- Laptopul sesiunii nu are placă NVIDIA, așa că nimic nu s-a testat pe RTX 3070 Ti.

## Urmează
- Fereastra pe workstation: inventarul din Windows, apoi `gpu identifica` de pe stick (doar citire).
- Pașii următori, tot doar citire: I2 (așteptarea firmware-ului plăcii) și I3 (citirea VBIOS).
- Activarea CI (fișierul e în `ci/`, vezi Blocaje).

## Ce oferă proiectul celorlalți
- `cyber-universe`: comanda `gpu` (nivel 0) ca patch gata în `integration/cyber-universe/`. Se aplică curat pe 2d038de, dar
  **nu e aplicat**; îl ia sesiunea OS dacă Adrian vrea. Tot acolo: 6 observații despre kernel (de ex. `map_mmio` poate lăsa
  registrele în cache).
- `kronos`: operatorii de referință + formatul de tensor (f32/bf16), utili pentru „Kronos pe procesor” (K6-CPU).

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: un Release cu patch-ul aplicat, ca `gpu identifica` să existe pe stick. Abia după decizia lui Adrian.
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
- **Fereastra pe workstation (~30 min, Kronos oprit):**
  1. În Windows rulezi `powershell -ExecutionPolicy Bypass -File tools\k0-inventar-workstation.ps1`. E doar citire și e permis oricând.
  2. Din BIOS notezi: IOMMU, Above 4G Decoding, Resizable BAR.
  3. De pe stick: `lspci`, `gpu identifica`, `log gpu 40`, `gpu plan` → poze. Lista completă: `docs/TEST_MATRIX.md`.
- **Licența firmware-ului NVIDIA:** e voie doar pentru sisteme cu licență OSI, iar OS-ul e MIT. Decizia ta: îl folosim sau nu.
- **Compilatorul pentru programele GPU:** Mesa NAK (MIT, pe calculator) sau `ptxas` de la NVIDIA (licență restrictivă). Decizia ta.
- **CI:** token-ul de push nu are dreptul `workflow`. Fișierul `ci/github-actions-ci.yml` trebuie mutat în `.github/workflows/`,
  de tine sau cu un token care are acest drept.
