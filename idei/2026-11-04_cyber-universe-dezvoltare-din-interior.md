# Dezvoltare din interior: workstation-ul stă în Cyber Universe, legat de GitHub (varianta A)

- **Propus de:** centrul de comandă, din ideea lui Adrian (4 nov 21:52–22:00) · **Data:** 2026-11-04
- **Proiecte implicate:** `cyber-universe`, `cyber-gpu`, `kronos`
- **Stare:** propus — Adrian citește și dă „da” (a ales deja varianta A: pauză la antrenări)

## Ideea (pe înțelesul lui Adrian)
Workstation-ul stă pornit non-stop în Cyber Universe, „ca și cum Windows n-ar exista”. Claude (sesiunile din cloud, din abonament, fără API) scrie codul pe GitHub;
GitHub construiește versiunea; Cyber Universe o ia singur, își face backup, repornește **tot în Cyber Universe**, rulează testele și urcă raportul pe GitHub; dacă ceva
pică, revine singur la versiunea bună. Testăm pe hardware real de 10–20 de ori pe zi, fără Adrian și fără Windows. Antrenările Kronos fac pauză (varianta A) și revin
direct în OS când OS + GPU sunt destul de avansate.

## Pași (fiecare util și singur; ne putem opri după oricare)
1. **Legătura cu GitHub (doar citire):** OS-ul citește periodic o „cutie de sarcini” din hub (o listă de comenzi din lista albă) și Release-urile OS. Fără server deschis spre internet.
2. **Actualizare de sine:** descarcă versiunea nouă (HTTPS, sumă SHA-256 verificată), o scrie pe stick lângă cea veche, repornește în ea (Limine: intrarea nouă + cea veche).
3. **Revenire automată:** ceas de siguranță; dacă versiunea nouă nu pornește sau pică testele de bază → următoarea pornire alege versiunea veche, singur; raport „revenit”.
4. **Rapoarte pe GitHub:** OS-ul urcă raportul fiecărui tur (scriere în hub prin API-ul GitHub, cu un token doar pe stick, cu drepturi doar pe un dosar al hub-ului).
5. **Programe noi fără restart:** unelte și teste noi încărcate din mers; restart doar când se schimbă nucleul.
6. Mai târziu (nu acum): fișiere cu scriere completă, apoi compilatorul în OS, apoi antrenarea în OS (pe GPU).

## Ce rămâne neschimbat
- **Scrierile pe placa video doar cu Adrian de față.** De la distanță pe placă: doar citiri (lista albă, ca `gpu tur`).
- Clean-room, testele în QEMU înainte de orice Release, `main` mereu construibil.

## Ce trebuie de la Adrian (când e momentul)
- „da” la propunere; stick-ul lăsat în workstation; BIOS: Cyber Universe primul la pornire (reversibil).
- Tokenul GitHub pentru stick (doar el îl face; drepturi minime; niciodată în repo/hub).
- Opțional, recomandat: o **priză inteligentă Wi-Fi** (~50–80 lei), ca să poată reporni workstation-ul de pe telefon dacă se blochează tot.

## Cost și riscuri
- ~1 săptămână pentru pașii 1–2, încă 1–2 pentru 3–5 (sesiunile OS + GPU, fără Adrian).
- Risc: OS blocat fără nimeni lângă el → ceasul de siguranță + priza inteligentă. Risc: token pe stick → drepturi minime, doar un dosar.
- Kronos: pauză la antrenări (#477 rămâne în uz și rulează în OS); C-64 (română, Kronos mai mare) așteaptă.

## Decizia lui Adrian
- 2026-11-04 22:00: alege varianta A (pauză la antrenări). „Da”-ul pentru pornire: (de completat)

## Discuție
