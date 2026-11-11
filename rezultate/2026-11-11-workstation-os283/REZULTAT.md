# Test workstation 11 nov 2026 (~17:25) — os-283 (cyber-gpu 2bbd0b3: bDmemStack = 1, C-102/C-107)

**Rezultat:** I6, I7 TREC; I8 ESUAT 0x59 (1777 scrieri) — **identic cu os-280**. Jurnal: `rezultate/os-automat/2026-11-11/gpu-jurnal-009.txt` (2438 rânduri, trimis singur de OS).
- Aceleași 844 NOCAT ASSERT, **aceleași adrese** (diff gol față de gpu-jurnal-008), aceleași 2 UCODE_LIBOS_PRINT (ENG_PMU), GSP_INIT_DONE = 0x59 NV_ERR_OPERATING_SYSTEM.
- Concluzie: **bDmemStack nu era cauza** (sau nu singura). Cauza e în altă parte din ce primește GSP-RM la prima pornire.
- Următorul pas (C-107 continuat): comparația „trei surse” pe TOATE câmpurile (GspSystemInfo întreg, registry — numărul și valorile cheilor, PCI/BAR, WPR meta, mesajele RPC trimise înainte de pornire: SET_SYSTEM_INFO, SET_REGISTRY etc.), plus conținutul hex al celor 2 UCODE_LIBOS_PRINT.
