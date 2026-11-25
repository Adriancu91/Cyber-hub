# os-423 · `test-placa --mm-tc` · proba `mm_tc` (os-352) pe placa reală — TRECE la corectitudine, LENT la viteză

- **Când:** 25 nov 2026, semnal 10:45, pornit 10:46:53, raport `rezultate/os-automat/2026-11-25/ciclu-auto-20261125-1052.txt`.
- **Corectitudine:** `proba mm_tc: TRECE: 6 / 6 seturi in margine, 132780 / 132780 elemente exacte fata de model, abaterea maxima 69 promile`; gărzile neatinse; intrările qkv-513 recitite identic (fnv `0x7f6be273`).
- **Viteza:** qkv-513 (6144 × 2304 × 768) mediana **21,15 ms = 1,02 TFLOP/s** — prezis 8–17. Mai lent decât `mm_tv_128x128` pe F32 (~2,0 TFLOP/s).
- **Citire (DEDUS):** se potrivește cu bănuiala ocupării (`idei/2026-11-25-centru-inmultirea-la-altii.md`): `mm_tc` are blocuri de 128 de fire și 24 KiB partajați → cu treapta unui singur bloc, **4 grupuri de fire din 48 pe unitate**. Circuitele speciale stau aproape goale. Nu e o problemă de corectitudine: biții sunt exacți.
- **Următorul:** proba ocupării (os-423 `--cursa-mm --ocupare`), apoi `mm_tc` / `mm_tc128` cu treapta potrivită și mai puțină memorie partajată pe bloc (punctul 4 din studiu). Pasul mixt #513 (`--mixt-513`) abia după.
