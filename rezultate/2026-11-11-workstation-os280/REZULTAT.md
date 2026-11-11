# Test workstation 11 nov 2026 (~14:20) — os-280 (C-102 continuare: decodarea NOCAT / UCODE_LIBOS_PRINT)

**Rezultat:** I6, I7 TREC; I8 ESUAT 0x59 (1777 scrieri), la fel. Jurnal: `rezultate/os-automat/2026-11-11/gpu-jurnal-008.txt` (2438 rânduri) —
**trimis SINGUR în hub de OS cu `trimite` + `github.token` (prima dată: 20 de rapoarte, cod 0)**.

## Ce spune jurnalul
- `GSP_INIT_DONE` rpc_result = 0x59 = **NV_ERR_OPERATING_SYSTEM**.
- **844 înregistrări NOCAT (0x34c), toate de tip 5 = ASSERT**, `linia = 0`, `subsystem = 0`, source „ASSERT”; adrese față de începutul GSP-RM în zona
  **0x019ef3c6 … 0x019f0060** (≈ 3 KiB de cod, adrese diferite, crescătoare), timestamp-uri crescătoare. Doar 16 feluri jurnalizate, 0x33c peste limită.
- **Toate ASSERT-urile vin ÎNAINTE de secvențiator** (rândurile 1498–1625; „cererea GSP-RM, comenzile urmează” la 1626) → apar în prima pornire a GSP-RM, nu la CORE_RESUME.
- 2 × UCODE_LIBOS_PRINT de la **ENG_PMU** (0xf3d72200), 0x10 și 0x18 octeți, nedecodați — chiar înainte de GSP_INIT_DONE.
- Interpretare (ipoteză): GSP-RM primește încă de la pornire ceva ce nu-i convine (GspSystemInfo / registry / PCI / BAR / WPR meta), aserțiile curg, iar la final
  inițializarea (posibil partea PMU) eșuează cu NV_ERR_OPERATING_SYSTEM. De comparat câmp cu câmp ce trimitem față de ce trimite driverul NVIDIA 570.144 MIT.
