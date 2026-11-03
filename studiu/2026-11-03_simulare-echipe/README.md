# Simulare: ideea lui Adrian „9 echipe × 4 fire” (3 nov 2026)

MODEL pe calculator (cloud, 2 nuclee) — NU o măsurătoare pe workstation. Calibrat ca „azi” să dea ~122 simb/s, ca profilul real os-214.
Nu știm încă de unde vine exact cele 63 % de așteptare, deci două ipoteze: **H1** = mai ales clopoțelul (trezirea/adunarea firelor),
**H2** = mai ales firul cel mai lent. `python3 simulare.py` → `rezultat.txt`.

| varianta | H1 | H2 |
|---|---|---|
| azi | 123 | 112 |
| echipe 9×4 | 184 | 120 |
| + fire treze | 228 | 123 |
| + calcule unite | 236 | 134 |
| + raft fix pe echipă | 263 | 145 |
| + ajutor la cel lent | 306 | 300 |

Concluzie: echipele singure ajută mult doar dacă vina e la clopoțel (H1); dacă vina e la cel mai lent (H2), contează „ajutorul la cel lent”.
Împreună, ambele ipoteze dau ~300 simb/s. Pentru C-59: `--profil` să despartă „adunare/trezire” de „așteptat cel mai lent”; variantele se măsoară toate în `--cauta`.

## 9×4 față de 6×6 (cerut de Adrian, 12:57)
| | 9×4 H1 | 9×4 H2 | 6×6 H1 | 6×6 H2 |
|---|---|---|---|---|
| echipe | 184 | 120 | 189 | 120 |
| + fire treze | 228 | 123 | 230 | 124 |
| tot pachetul | 306 | 301 | 308 | 301 |

Diferența (sub 3 %) e mai mică decât incertitudinea modelului: simularea nu le poate despărți. Ce nu prinde modelul: 4 fire = 2 nuclee fizice,
6 fire = 3 nuclee; cum se potrivesc cu memoria rapidă a nucleelor se vede doar pe placă. **Decizie: în testul real `--cauta` le măsoară pe amândouă** (e doar un număr schimbat), iar 6×6 e prima, la egalitate.
