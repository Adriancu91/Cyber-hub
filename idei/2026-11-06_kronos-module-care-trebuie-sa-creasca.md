# Kronos: modulele care trebuie să crească odată cu modelul (ca să nu devină frâne)

- **Propus de:** centrul de comandă, la cererea lui Adrian (6 nov 2026, 17:51) · **Pentru:** kronos (+ cyber-universe la punctul 7)
- **Stare:** aprobat (Adrian, „Da”, 2026-11-06 17:56) → C-85

## Ce frânează deja sau va frâna (în ordinea importanței)
1. **Examenul oficial măsoară altceva decât ținta.** `examen_bpb` (protejat de paznic) se dă pe primele 100.000 de caractere din validarea TinyStories (engleză, povești
   pentru copii). Ținta e acum româna și răspunsurile în română (C-64). Deciziile reale se iau deja pe examene puse lângă (română curat, R1, R2, fapte) prin scripturi din `unelte/`.
   → **Propunere:** un al doilea examen oficial, `examen_romana`, ca modul cu MANIFEST, păzit și el de paznic (setul ascuns de 500 + română curat), fără să-l schimbăm pe cel vechi.
2. **Memoria plăcii la modelul mare.** S77c: 24 de straturi au rămas fără memorie la ora 3 (5,56 GiB din 5,66). Optimizatorul e `adamw` (2 stări pe parametru).
   → Muon (există deja `model_muon`, o singură stare) sau stări pe 8 biți; puncte de salvare pe bucăți; paza de memorie verificată la fiecare oră, nu doar în primele 15 minute.
3. **Puncte de salvare `.pt`: 114 GB pe disc.** Discul a coborât la 31 GB liberi. → Regula din Mini Brain: se păstrează automat doar câștigătorul + rezervele numite (#459, #477, #513);
   restul se șterg după verdict (cu jurnal: nume + SHA + scor), `*.pt` mereu în afara git.
4. **Contextul de 512 simboluri.** Pentru un asistent (rezumate, conversații lungi) e scurt. → Extindere treptată (1024 → 2048) când trecem la antrenarea pe placă din OS sau la un upgrade de placă.
5. **Datele se citesc întregi în RAM, ca text.** Merge azi; la „super-școala de română” (milioane de exemple) devine frână. → Date pre-tokenizate, pe bucăți, citite pe rând.
6. **Cercetătorul alege dintr-un spațiu mic** (`lot = [6]`) și încearcă direct pe modelul mare. → Încercări pe un model mic „trimis în avans” și doar câștigătorul pe cel mare.
7. **Motorul KGR1 din OS** (256 simb/s cu #477): un model de 2× mai mare scrie de ~2–3× mai încet pe procesor. → Calea pe placă (C-83, I12–I14) devine necesară, nu opțională.
8. **Porturile goale (memorie, profesor, traducere)** sunt corecte pentru antrenare, dar asistentul din OS (C-84) va avea nevoie de **memorie** (`memorie_ierarhica`) și de un
   modul de **fapte verificate** (lecția Mini Brain) la folosire, nu la antrenare.
9. **Module nefolosite** (`model_plasa*`, `model_ngram`, `model_continuu`, `model_racit`, `date_tinystories`, `cercetator_aleator`): nu frânează, dar încurcă și lungesc testele.
   → Mutare în `module/arhiva/` cu testele lor (nimic șters), dacă Adrian vrea. `profesor_qwen` rămâne oprit (decizia „fără alt AI”).

## Ordinea propusă
3 (disc) → 2 (memorie) → 1 (examen română, cu „da”) → 6 → 5 → 8 → 4 → 9. Punctul 7 îl face C-83.

## Discuție
- 2026-11-06 17:56 Adrian: „Da” la toată propunerea (inclusiv examenul de română și arhiva modulelor nefolosite) → C-85.
- 2026-11-06 20:15 kronos (supraveghetor): preluat — pasul 1 (lista punctelor de salvare, doar listă) = S84 în coadă, după S77e și S83; pașii 2–8 intră câte unul, după S84.
- 2026-11-06 23:15 kronos (supraveghetor): pasul 1 gata (S84, doar listă: 71,5 GB „se pot șterge”, decide Adrian); pasul 2 (memoria plăcii la modelul mare) = S86, ziua de 7 nov.
