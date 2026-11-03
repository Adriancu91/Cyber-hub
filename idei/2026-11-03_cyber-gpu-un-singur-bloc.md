# Kronos pe placă: un singur program pornit o dată pe simbol (ideile lui Adrian din 3 nov)

- **Propus de:** centrul de comandă, din ideile lui Adrian · **Data:** 2026-11-03
- **Proiecte implicate:** `cyber-gpu`, `cyber-universe`
- **Stare:** aprobat (Adrian, „ok”, 2026-11-03 13:25) — ca direcție de plan, nu sarcină de acum

## Ideea (pe înțelesul lui Adrian)
Pe procesor, Kronos pierde 63 % din timp cu „clopoțelul” dintre cele 63 de calcule ale unui simbol și cu firul cel mai lent (C-59; simulările în
`studiu/2026-11-03_simulare-echipe/`). Pe placă „clopoțelul” e lansarea fiecărui calcul de către procesor (driver overhead). Ideea: când ajungem la calcul pe placă,
Kronos rulează ca **un singur program pornit o dată pe simbol** (sau pe mai multe), care face toate calculele fără să se întoarcă la procesor; echipele plăcii (48 SM)
își iau bucăți dintr-un contor comun și așteaptă doar datele calculului de dinainte (un caiet în memoria plăcii), cine termină ajută.

## Ce ar face fiecare proiect
- `cyber-gpu`: o păstrează în `docs/` ca țintă pentru treptele matmul / Kronos (după I6–I10 și primul calcul); proiectează coada de comenzi și formatul ca să permită
  un program lung, cu sincronizare prin contoare în VRAM, nu prin procesor. Măsoară întâi costul unei lansări, apoi compară „câte un program pe calcul” cu „un singur program”.
- `cyber-universe`: lecțiile de pe procesor (C-59: bloc fără clopoțel, ajutor la cel lent, un fir liber pentru întreruperi) se aplică și firului care comandă placa.

## Cost și riscuri
- Nimic de făcut acum (placa e la I6). Risc: un program lung blocat ține placa ocupată → ceas de siguranță și oprire curată, ca la `gpu i6`.
- Nicio scriere pe placă fără Adrian de față; clean-room neschimbat.

## Decizia lui Adrian
- 2026-11-03 13:25: „ok” (în chat, centrul de comandă).

## Discuție
- 2026-11-03 centrul de comandă: rezultatele C-59 pe procesor (`--cauta`, `--profil`) sunt măsurătoarea de pornire pentru acest plan.
