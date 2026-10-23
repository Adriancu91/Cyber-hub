# K0 — inventarul workstation-ului (din Windows, doar citire) — 23 octombrie 2026, 09:33

**Făcut de:** Adrian, cu `tools/k0-inventar-workstation.ps1` din `cyber-gpu` (rulat de pe stick, `-OutDir .\rezultate`). Fișierul brut: `k0-DESKTOP-BR58S2C-2026-10-23_0933.txt`.

| Ce | Valoare |
|---|---|
| Calculator | Dell, placă de bază **0X75JG** (ESTIMARE: Precision 5820 Tower), BIOS Dell **2.44.0** (10 iun 2025) |
| Procesor | **Intel Core i9-10980XE @ 3,00 GHz — 18 nuclee / 36 fire** (Cascade Lake-X, AVX-512) |
| RAM | 127,7 GiB |
| OS | Windows 11 Pro 10.0.26200 |
| Placa video | **NVIDIA GeForce RTX 3070 Ti**, PCI `10de:2482`, subsistem `1043:8813` (ASUS), rev A1, PCI bus **B3** (179), device 0, function 0; VBIOS **94.04.65.00.3e**; driver 616.56; 8192 MiB |
| Ferestre de memorie (BAR) | `E0000000–EFFFFFFF` **256 MiB** (BAR1, VRAM vizibilă), `F0000000–F1FFFFFF` 32 MiB (BAR3), `F9000000–F9FFFFFF` 16 MiB (BAR0, registre); I/O `F000–F07F` |
| Resizable BAR | **oprit** (BAR1 = 256 MiB; cu ReBAR ar fi 8 GiB) — de confirmat în BIOS |
| Above 4G Decoding | toate BAR-urile sub 4 GB → probabil oprit — de confirmat în BIOS |
| IOMMU / VT-d | Windows nu listează „protecție DMA/IOMMU disponibilă” (proprietățile VBS 1,2,5,7,8, fără 3) → **probabil oprit în BIOS** — de confirmat |
| VBS | rulează (stare 2) |
| Secure Boot | necunoscut din script (fără drepturi de administrator) — de citit în BIOS |

**Ce urmează:** pozele din BIOS (IOMMU/VT-d, Above 4G, ReBAR, Secure Boot), apoi pornirea OS-ului de pe stick (os-161): `hw`, `lspci`, `net`, `ls /disk`.
