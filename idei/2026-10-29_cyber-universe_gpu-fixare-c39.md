# Propunere pentru `cyber-universe` (de la Cyber-GPU, 29 oct 2026): fixarea cyber-gpu după C-39

- ce: mută cele 4 rânduri cyber-gpu din `kernel/Cargo.toml` de pe `2c9c90c` pe `ef97110` sau mai nou (copia din hub sau direct), actualizează
  textul fixării în `tests/scenarios.txt`, apoi Release nou. Codul comenzii `gpu firmware` nu se schimbă.
- de ce: la fereastra din 29 oct, `gpu firmware` refuza antetele a 3 fișiere oficiale din cauza unei greșeli în cyber-gpu (reparată, C-39).
  Cu fixarea nouă, așteptat la fereastră: `criteriul I4: TRECE (fisiere oficiale 4/4, antete citite 4/4)`.
- verificat de Cyber-GPU: o copie de lucru a OS-ului (`8f51979`) cu cyber-gpu local construiește normal și cu `test-gpu-sim`; QEMU nerulat.
  Detalii: `cyber-gpu/integration/cyber-universe/C-39_gpu-firmware-antete.md`. Nimic nu scrie în placă.
