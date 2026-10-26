# Studiu open-source — 26 octombrie 2026

Cerut de Adrian (26 oct 17:20): „caută proiecte și coduri open source pe GitHub care putem să le folosim ca documentare pentru proiectele
noastre; fă-ți lecțiile, ia notițe, propune idei și arhitecturi noi și mai bune”.
Făcut de centrul de comandă, cu trei cercetători în paralel. ~45 de repo-uri clonate și citite (doar citit, nimic rulat, niciun repo modificat).
Fiecare afirmație din notițe e marcată: citit / din memorie / dedus. Licențele sunt luate din fișierele LICENSE.

| Fișier | Proiect | Cele mai utile surse găsite |
|---|---|---|
| `kronos.md` | Kronos | modded-nanogpt (speedrun), nanochat, llama2.c, Pyserini/bm25s, STaR, FineWeb-2 (română, ODC-By) |
| `os.md` | Cyber Universe OS | NIGHTRUN (UEFI + LLM local, MIT), Theseus, ArceOS, Hubris, Tock, Redox, smoltcp, talc, acpi |
| `gpu.md` | Cyber-GPU | **tinygrad (MIT): driver NVIDIA prin PCI care pornește GSP 570.144 pe GA102**, antetele NVIDIA 570.144 (MIT), Mesa NAK, siboehm SGEMM |

## Propunerile, pe scurt (detaliile în fiecare fișier)

**Cyber-GPU** — aprobate prin „da”-ul general al lui Adrian (DECIZII 26 oct 17:10) → `COMENZI.md` C-20:
- B. Structuri Rust generate din antetele NVIDIA 570.144 (MIT), cu teste de mărime.
- C. Secvența tinygrad ca specificație pentru I4–I10 (scriere proprie în Rust, sursa în PROVENANCE); pas nou „golden image” după pornirea GSP.
- D. Procesor de comenzi + GSP fals în `gpu-sim`, ca tot lanțul să ruleze în CI.
- E. NAK pe gazdă + treptele matmul; primul matmul în f32 (NAK folosește tensor cores doar cu f16 pe Ampere); atenție la FMA în comparația bit cu bit.
- A. „Proba de referință”: tinygrad pe un stick Linux, pe RTX 3070 Ti, cu jurnalul tuturor scrierilor — **se pregătește acum, se face doar cu Adrian de
  față** (scriere în placa reală, cod străin pe placă; ecranul workstation-ului se stinge, comenzile prin SSH de pe laptop).

**Kronos** — așteaptă „da”-ul lui Adrian (recomandarea centrului în paranteză):
1. Muon + răcire lungă, din #415 (~5–6 h placă) — **da, după S27**.
2. Memoria E3: rădăcini românești + reordonare cu #415 + RRF (minute pe placă) — **da, primul**.
3. Motor de inferență fără PyTorch, Q8 (~104 MB în loc de ~392 MB), țintă pentru OS (0 h placă) — **da**.
4. Linie nouă „w3” de la zero, arhitectură modernă + mai multă română (o noapte) — mai târziu, după 1 și 2.
5. Auto-joc doar pe „răspuns din text”, cu verificator — după verdictul S27.
- **Întrebare pentru Adrian:** TinyStories (folosit deja în date și în examen) a fost generat de GPT-3.5/4 (din memorie, neverificat). Nu e un LLM în buclă,
  dar vrei și datele curate de text generat de LLM străin?

**Cyber Universe OS** — așteaptă „da”-ul lui Adrian:
1. „Cutia neagră” pe stick: jurnalul + `hw` + registrele driverelor scrise într-un fișier pe stick (gata cu pozele) — **da, primul**.
2. Teste mai rapide: multe teste într-o pornire + teste pe gazdă cu fuzzing (CI ~18 min azi).
3. Găzduirea lui Kronos: model încărcat o dată, doar-citire, verificat SHA-256; pagini de 1 GiB; nuclee dedicate (după NIGHTRUN).
4. Permisiuni pe program: azi orice program poate citi `/usb/claude.key` și `github.token` — **da, înainte de Faza 6**.
5. Tipuri care previn greșelile din drivere (sincronizarea DMA, ordinea încuietorilor).
