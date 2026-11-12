# Test workstation 12 nov 2026 (~17:48) — os-295, C-108 varianta 1 „rpc-inainte”

## 🎉 I8 TRECE
Jurnal: `rezultate/os-automat/2026-11-12/gpu-jurnal-010.txt` (2425 rânduri, trimis cu `trimite` la pornirea următoare).
- Varianta 1 = `SetSystemInfo` + `SetRegistry` (+ sonerie) în coadă **la I7, înainte de Booter**; bIsPassthru 0, bIsPrimary 2, hostPageSize 0x1000, 2 chei de registru, WprMeta.flags 0, bDmemStack 1.
- **`GSP_INIT_DONE rpc_result = 0x00000000`** (după 11,17 s de așteptare) → `pas I8 GSP_INIT_DONE: ok`, **`pas i8-gsp-init: ok`**.
- Doar **2 NOCAT** (nu 844): unul ENGINE `NV_ERR_INVALID_DMA_SPECIFIER` (0x27), source „Display Subsystem”, faultingEngine „Display Engine”; + 2 UCODE_LIBOS_PRINT de la ENG_PMU (0x10 și 0x18 octeți, conținutul în jurnal).
- **`pas i8e-golden: ok`** (tabelele de pagini în VRAM prin fereastra 0x1700).
- **`pas i9-canal-lucru: ESEC`** (fără cod în jurnal; ultimele scrieri: fereastra 0x1700 ↔ 0x10e5, soneria 0x110c00 = 0). Apoi bus-master-oprit ok, tur-după ok.
- **Ecranul a înghețat la ~154 s** (Adrian a văzut ultimul rând „SCRATCH_14 = 0x17100000”), dar jurnalul pe stick a continuat până la 164 s și lanțul s-a terminat.
  Ipoteză: GSP-RM a preluat motorul de afișare (vezi NOCAT „Display Engine”) → framebuffer-ul UEFI nu mai e afișat. De verificat/evitat (ex. să nu lăsăm GSP-RM să ia afișajul, sau să cerem un raport pe ecran după).
