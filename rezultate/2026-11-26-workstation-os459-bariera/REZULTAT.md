# os-459 · proba barierei pe toată placa — TRECE (48 și 96 de grupuri), o barieră = 1,13 µs

- **Când:** 26 nov 2026, 11:01; raport `rezultate/os-automat/2026-11-26/ciclu-auto-20261126-1101.txt`.
- **48 SM-uri active** citite corect (24 TPC × 2; os-456 citise maximele de proiect 84).
- G = 48: R = 1 TRECE (contorul 48), R = 1 001 TRECE (48 048) → **o barieră = 1 126 ns**.
- G = 96 (2 blocuri pe unitate): R = 1 TRECE, R = 1 001 TRECE (96 096) → **1 143 ns**.
- Prezis ~1–3 µs (Cyber-GPU) ✔. Niciun cuvânt vechi, nicio blocare.
- **Ce înseamnă:** toată placa se poate sincroniza în ~1 µs, deci un **program persistent** (un singur program care face mai multe etape ale pasului, cu o barieră între ele) e posibil la noi. La 484 de lansări pe pas, chiar 1 µs pe barieră = < 0,5 ms. Următorul: studiul Cyber-GPU pe ce etape câștigă din lipire (datele ținute în memoria rapidă între etape).
