# Evaluarea „dacă aș fi investitor” — istoric

Părerea centrului de comandă, la cererea lui Adrian, ca reper de progres (nu e o evaluare financiară profesională).
La fiecare nouă întrebare se adaugă un rând, cu ce s-a schimbat.

| Data | Stadiu | Cât aș pune (înger investitor) | Evaluare pre-money implicită | Ce a contat |
|---|---|---|---|---|
| 2026-10-28 | Prototip de cercetare, 4 săptămâni: Kronos 98M de la zero rulează corect în OS propriu (8 simb/s), driver GPU citește RTX 3070 Ti (fără calcul), fără clienți, fondator unic non-tehnic + agenți AI, OS și driver publice (MIT) | 25.000–50.000 €, în tranșe legate de repere | ~250.000–500.000 € | + lanț complet dovedit, viteză de execuție, piață mare; − fără produs/client, fără „șanț” (codul e public și reproductibil cu aceleași unelte), risc de om-cheie |
| 2026-11-01 | Kronos #477 verificat în OS la 123 simb/s (×25 într-o săptămână); driverul GPU trece toți pașii de citire (I0–I4) pe placa reală; codul OS + driver proprietar și privat; 1,1 mld simboluri de cod curat + vocabular propriu, prima antrenare Kronos-Cod pornește | 25.000–50.000 €, în tranșe | ~300.000–600.000 € | + „șanțul” s-a întărit (cod privat, proprietar), ritm dovedit pe hardware; − tot fără client/produs, tot un singur om |
| 2026-11-03 | os-214 pe workstation: CONTROL TRECE, Kronos 125 simb/s și cu ecran (de la 70 → ×1,8); primul program NVIDIA (FWSEC) încărcat și rulat pe placă de driverul nostru (prin DMA), verificarea noastră a capătului WPR2 încă greșită (C-58); profil care arată exact frâna (63 % așteptarea firelor) + plan simulat spre ~265–305 simb/s; Kronos-Cod: două nopți NECLAR, calea A+B+C+D aleasă | 25.000–50.000 €, în tranșe | ~320.000–650.000 € | + prima execuție reală pe placă, problemă de viteză înțeleasă și măsurabilă; − pragul 150 nu e trecut, I6 încă „NU TRECE”, Kronos-Cod fără progres pe rezolvare, tot fără client |
| 2026-11-04 | os-222: Kronos **206 simb/s** în OS (CONTROL TRECE; pragul 150 trecut, ×1,65 față de ieri); **I6 reușit pe placa reală** (FWSEC-FRTS a ridicat WPR2 exact pe zona FRTS: LO și HI citite, granulație 128 KiB) — verificarea noastră de reparat (C-66); Kronos-Cod: S70 și S71 NU AJUTĂ, școala de cod pornește (reper 14/200) | 25.000–50.000 €, în tranșe | ~380.000–750.000 € | + ambele repere tehnice anunțate atinse (150+ și prima scriere pe placă), ritm dovedit; − I6 încă neconfirmat formal, Kronos-Cod fără progres, tot fără client/produs, tot un singur om |

Ce ar urca cel mai mult cifra: un client-pilot plătitor; demonstrația la ≥ 150 simb/s + primul calcul pe GPU; un produs clar (ex. asistent privat pe documente, în română); un cofondator tehnic sau primul angajat; Kronos comparat cinstit cu OpenLLM-Ro pe teste românești.


Proiecție orientativă (1 nov): 150+ simb/s + primul calcul pe placă → ~400–800k €; Kronos pe GPU în OS → ~0,5–1 mil. €; Kronos-Cod funcțional + primul client-pilot → ~0,8–1,5 mil. €. Cel mai mare salt îl dă un client sau un produs clar, nu un test tehnic.
