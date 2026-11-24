# Ordinea priorităților pentru antrenare (24 nov 2026, 21:40) — toate ideile de azi, într-o singură listă

- **Propus de:** centrul de comandă, la cererea lui Adrian (21:36: „analizează ce e mai relevant și pune-le în ordine după prioritate”)
- **Criteriu:** câștig așteptat ÷ efort, siguranța cifrei (MĂSURAT > DEDUS > ESTIMARE) și ce deblochează ce urmează.
- **Stare:** listă de lucru. Ce e marcat „aprobat” se face; ce e „de aprobat” așteaptă „da”-ul lui Adrian.

| Loc | Ce | De ce acum | Câștig (cifră) | Stare |
|---|---|---|---|---|
| **1** | **Înmulțirea mai rapidă:** cursa de noapte pe 4 variante + aflarea frânei comune (ceasul/puterea în timpul pasului, A4) | 93 % din pas e înmulțire (os-412); fiecare % de aici contează aproape întreg | ×1,5–3 pe pas (ESTIMARE) | aprobat (C-157, C-165) |
| **2** | **Tensor cores + „umbra pe 16 biți”** (`mm_tc`, activări f16) | aceeași piesă, nivelul următor; e drumul spre viteza Windows | ×2–4 peste pasul 1 (ESTIMARE) | aprobat (pista A) |
| **3** | **Laboratorul: rețeta de azi vs bucăți K = 4** | singura idee mare cu cifre publice bune (cost 0,5×) și ieftină de încercat | ×1,9 până la aceeași notă (DEDUS din lucrare) | aprobat (C-163), mâine de la 07:00 |
| **4** | **Laboratorul: harta greutății textului** | doar alegerea datelor, modelul neschimbat; se probează la fel de ieftin | ×1,5–2 (ESTIMARE) | aprobat (24 nov 21:39) |
| **5** | **Lotul mare** (12 × 512 sau mai mult, cu recalcularea activărilor, toată memoria plăcii) | placa e acum folosită ~6 %; pe plăci mari lotul a dat ×4,4 | ×1,5–3 (ESTIMARE) | aprobat (pista A); după 2 |
| **6** | **Optimizatorul în RAM + procesorul în paralel** | eliberează memorie pentru lotul mare | face loc, nu viteză directă | aprobat (condiția RAM ridicată) |
| **7** | **Kronos croit pe placă** (fișa v2: ReLU², RMS, fără bias, lățimi de 64) + ce a câștigat în laborator | proiectul modelului nou; se scrie pe hârtie acum, se antrenează după 1–6 | +10–20 % (ESTIMARE) | aprobat ca proiect (C-164) |
| **8** | **Proba pe 8 biți** (întâi: poate unealta noastră să scoată înmulțirea pe 8 biți?) | dublează viteza dacă merge; LLMQ ar arăta că se poate pe plăci de jocuri (sursă de verificat) | până la ×2 (ESTIMARE) | aprobat (24 nov 21:39) |
| **9** | **Straturi sărite pentru simbolurile ușoare** | intră în Kronos v2 dacă câștigă în laborator | −30–50 % calcul (lucrări publice) | de aprobat, după 3–4 |
| **10** | **Caietul din RAM** | cel mai scump (schimbă formatul modelului) | ×1,1–1,2 (ESTIMARE) | de aprobat, ultimul din trepte |
| — | Ieșirea pe eșantion / doar simbolurile posibile, un program pe tot stratul, Kronos care învață din folosire | câștig mic acum sau risc pentru ce învață modelul | — | mai târziu |

**Pe scurt:** 1–2 fac placa mai rapidă (aceleași calcule), 3–4 fac fiecare calcul să învețe mai mult, 5–7 pregătesc versiunea 1. Le măsurăm în ordinea asta; fiecare cifră reală intră în simulator.
