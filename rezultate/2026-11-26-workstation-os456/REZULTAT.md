# os-456 · profilul pasului mixt, lotul prin RAM, lotul 6, proba barierei — **lot 6: 10 480 simb/s (ținta etapei 1 atinsă)**

- **Când:** 26 nov 2026, semnal 07:08, 4 teste într-o pornire (07:18–07:31); rapoarte `rezultate/os-automat/2026-11-26/ciclu-auto-20261126-0718/0723/0728/0730.txt`.

| # | Testul | Pasul întreg | simb/s | Verdict |
|---|---|---|---|---|
| 1 | mixt rapid, lot 2 (fereastra VRAM) | 117,5 ms | 8 713 | **TRECE = oracolul MIXT** (pierderea 1,8e-5, norma 2,2e-4) |
| 2 | + `--lot-prin-ram`, lot 2 | 112,9 ms | 9 073 | TRECE (= oracolul mixt); în afara plăcii 11,3 → 7,2 ms |
| 3 | + `--doua-locuri --lot-513 6` | **293,1 ms** | **10 480** | „NU TRECE” = criteriul pe loturi sintetice (fără oracol la lot 6; ca os-437); 18 părți trimise cât placa lucra, 0 amânate, **în afara plăcii 0 µs** |
| 4 | `--bariera` | — | — | **oprită înainte de lansare:** „G prea mare pentru pagina probei” — OS-ul a citit **84 SM-uri (7 GPC × 6 TPC × 2)**, placa are **48**. Nicio lansare, placa neatinsă. |

## Profilul pasului #513 (lot 2, placa 106,2 ms, 484 lansări) — MĂSURAT
- Pe etape: înapoi 69,4 ms (65 %), înainte 30,7 (29 %), optimizatorul 5,6 (5 %), eroarea 0,5.
- Pe programe: **`mm_tc_v4` 73,6 ms (69 %, 147 lansări)** — Cyber-GPU prezisese ~73 ✔; **atenția 20,5 ms** (`attn_back_tile_3` 9,2 + `attn_fwd_tile3` 6,2 + `attn_back_tile0_3` 5,2) — prezis 20,6 ✔; `opt_step` 4,8; restul < 2 % fiecare.
- Deci: înmulțirile (~8,3 TFLOP/s în medie) + atenția = 89 % din pas. **Următoarele câștiguri: atenția pe circuitele speciale (Cyber-GPU: 5–10 ms în loc de 20,5) și înmulțirile mai aproape de 12–15 TFLOP/s.**

## Cereri
- **OS:** (a) proba barierei: numărul de SM-uri din GSP-RM e citit greșit (84 față de 48 pe RTX 3070 Ti) — de verificat câmpurile (GPC/TPC/SM) înainte de reluare; (b) verdict la lot > 2: oracolul mixt la lot 6 sau date reale pe stick (cererea de ieri).
- **Cyber-GPU:** atenția pe circuitele speciale în pasul mixt rapid (P2zm) — următorul test de viteză.
