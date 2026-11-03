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

## Bucățele (a doua idee a lui Adrian, 13:00) — `simulare_bucatele.py` → `rezultat_bucatele.txt`
Tot calculul e un bloc; fiecare fir ia o bucățică, iar când termină ia următoarea din ce a rămas (nimeni nu stă după cel lent).
| varianta | H1 | H2 |
|---|---|---|
| azi | 123 | 112 |
| bucățele 72 / 144 / 288 | 127 / 130 / 132 | 125 / 134 / 139 |
| bucățele 288 + fire treze | 234 | 153 |
| bucățele 288 + treji + echipe 9×4 | 260 | 158 |
| bucățele 288 + treji + echipe 6×6 | 261 | 157 |

Concluzie: bucățelele rezolvă partea „cel mai lent” (H2), echipele + firele treze partea „clopoțel” (H1). **Doar combinația trece de 150 în ambele ipoteze.**
(„Ajutor la cel lent” din primul tabel era o aproximare optimistă a bucățelelor; cifrele de aici sunt cele cinstite.)

## Un singur bloc, fără clopoțel (întrebarea lui Adrian, 13:05)
Fiecare fir ia bucăți dintr-un singur contor pe tot simbolul; nu există clopoțel, doar verificarea „sunt gata datele calculului de dinainte?” (~0,5 µs).
Bucăți 288 / 576 pe calcul: **H1 276 / 277, H2 158 / 160** — cea mai bună variantă din model (limita lui). Nu se poate fără deloc așteptare:
fiecare calcul are nevoie de TOT rezultatul celui de dinainte (ca acoperișul după pereți), deci la capătul fiecărui calcul tot se așteaptă bucata cea mai lentă.

## Ajutor la cel lent (ideea 3 a lui Adrian, 13:10) — `rezultat_ajutor.txt`
| varianta | H1 | H2 |
|---|---|---|
| un singur bloc, fără clopoțel | 276 | 159 |
| + ajutor: cine termină ia rânduri din bucata celui lent („furt”) | 292 | 166 |
| + „copie de rezervă”: dacă o bucată stă blocată (fir întrerupt), un ajutor o face din nou, câștigă cine termină primul | **298** | **274** |

Ajutorul simplu câștigă puțin: rândul pe care îl ține în mână un fir întrerupt nu se poate lua. Ce mai lipsea e „copia de rezervă”
(calculele sunt simple, se pot face de două ori fără risc; rezultatul e același). Cu ea, ambele ipoteze ajung la ~275–300 simb/s.
