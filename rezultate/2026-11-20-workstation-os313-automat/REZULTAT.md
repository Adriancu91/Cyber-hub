# os-313 — testul automat P1 (jurnalul rapid + măsurătorile etapei 0), 20 nov 2026

- **Release:** `os-313` (`fc98337`, CI verde), `cyber-gpu 02bbc36`; pus pe stick de centrul de comandă la 07:35 (sume recitite identice).
- **Pornire:** paznicul la 08:01:52 (după ce a așteptat ora 08:00); testul 08:07:23 → gata în 202 s; Windows înapoi singur.
- **Fișiere:** `rezultate/os-automat/2026-11-20/ciclu-auto-20261120-0807.txt`, `gpu-jurnal-014.txt` (recuperare), `gpu-jurnal-015.txt` (lanțul, 4 184 rânduri).

## Rezultat
- **Corect:** 16 simboluri pe placă, **identice cu procesorul**; abaterea maximă a logit-urilor 1,75e-5; textul „, Imi doresc sa ma intorc la mine, Sa ma”. I14 trece din nou.
- **Viteza cu driverul: 21,54 simb/s** (os-308: 10,99) — de ~2 ori, din jurnalul ținut în memorie (646 rânduri de rutină → 24 de scrieri).
- Placa singură: 43,77 simb/s (22,97 ms/simbol), neschimbată, cum era de așteptat.
- Timpul pe simbol (median): placa 22 968 µs · driver 6 428 µs · jurnal 14 228 µs · ecran 0 = 43 698 µs.
- Procesorul (motorul rapid): 76,1 simb/s. Verificarea pe procesor după placă e încă cea lentă (0,25 simb/s; C-148 punctul 2 nu era în os-313).

## Etapa 0 — măsurătorile (primele, pe placa reală)
- **Starea de performanță la final (`ks`): P8** — cea mai joasă stare obișnuită (repaus). Nivelurile și temperatura: fără cale documentată (cum se știa).
- **Copierea VRAM → VRAM (`kc`):** 64 MiB × 3, 0 cuvinte greșite; 9 165 MB/s (18 330 MB/s trafic) = **3 % din 608 GB/s**.
- **Pornirea goală (`kl`):** 16 lansări, minim 3,84 µs, **median 3,90 µs**, maxim 153,5 µs.
- **Timpul pe fel de lansare (`kp`, µs pe simbol):** fc 4 119 · proj 3 582 · qkv 3 302 · atenție 2 382 · ln1 2 260 · ln2 2 214 · logit 1 601 · out 1 392; cele 8 mărunte (k, v, +b ×4, rez1, rez2, gelu) ~14–16 µs fiecare, ~1,4 ms pe simbol în total; embed 37, copiere 51, ln_final 189.

## Ce înseamnă
1. **Condiția pentru viteza maximă e îndeplinită** (completarea C-147, (a)): placa a rulat în **P8**, iar memoria a dat 3 % din cât poate. Chiar și normalizările (ln1/ln2, ~188 µs pentru 768 de numere) sunt de sute de ori mai lente decât ar trebui — semn de ceasuri joase, nu de program prost.
2. **Costul fix al unei porniri e mic** (3,9 µs; ~0,8 ms din 23 ms pe simbol). Lipirea calculelor (P3) aduce puțin (~1,4 ms, ~6 %). Ordinea se schimbă: **P5 (viteza maximă) înainte de P3**.
3. Rămân de luat din afara plăcii: jurnalul 14,2 ms și driverul 6,4 ms pe simbol.

## Următorul pas
- **P5:** `PERF_BOOST` (forma NVIDIA, 600 s, ștergere la final, o singură trimitere, `ks` înainte/după) + aceleași măsurători `kp`/`kc`, ca să vedem diferența. Aprobat de Adrian (DECIZII 19 nov 22:50 și 23:25) cu această condiție — acum îndeplinită.
- Kronos #651 (`kronos_651_q8_0.kgr`, 206 898 464 B, SHA-256 `2edf75ac…a0bf2`) e pe stick în `KRONOS\`, recitit cu suma identică; nu a rulat încă.
