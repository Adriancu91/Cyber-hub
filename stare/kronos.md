# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-13 17:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **C-119 în lucru (antrenamentul mare; Adrian plecat până luni seara 16 nov):** S109 (E1) gata → S110 (E2) → S111 (E3) → S112 (E4), fiecare cu pre-înregistrare și praguri scrise dinainte.
- **S109 (E1) GATA, verificat: AJUTĂ.** Modelul nou **#577** („#513+b”): 102/130 corecte pe tipurile antrenate (#513: 24), verificatorul 91 față de 23; fără regresii (română 1,2055, cod, R2, R1 98,97, S15, S4 în praguri). Mai slab pe tipuri nevăzute (5 față de 10 din 50).
- **C-120 preluat:** S110 rescrisă după revizia Fable: pornire corectă a încorporărilor (`ModelGPTCod`, 0,02; verificat în cod), lot 6 × 16, fără examenele de engleză orare, restul FineWeb-2 românesc (~2,45 GB, deja descărcat) ca hrană 55 % după verificarea scurgerilor → ~69 % română; 52 h; praguri noi la 12 h / 24 h.
- **Modelul în uz: #513** (98M, KGR1 Q8_0); **#577 = cel mai bun măsurat** (nu e încă în interfață). Model propriu, de la zero, fără LLM străin.

## Urmează
- **S110 (E2):** pregătirea datelor + scurgeri (procesor ~1–1,5 h) → proba de rată (~1,2 h) → 52 h pe placă (pornire ~20:00–21:00, gata ~luni dimineață); oprire la 12 h / 24 h doar dacă nu mai învață.
- **S111 (E3, ~8 h):** conversația pe baza nouă (AdamW 1e-5) + toate examenele → câștigătorul față de #577.
- **S112 (E4):** câștigătorul în interfața de convorbire (port 8787, local + Tailscale) + raport final pentru luni seara.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu **#513**. Dacă C-119 dă un model mai bun (#577 sau cel de 24), îl anunțăm aici; KGR1 nou doar după „da”-ul lui Adrian.
- Unelte pentru date mari cu RAM mic (`date_bucati`, dovedite pe placă).

## De ce are nevoie de la ceilalți
- De la centrul de comandă: notă în `COMENZI.md` dacă Adrian vine totuși la workstation până luni (Kronos salvează, se oprește, reia).
- De la `suita-office`: nimic.

## Blocaje / nevoie de Adrian
- Niciun blocaj. Nimic de la Adrian până luni seara.
- De știut: interfața 8787 rulează încă modele vechi (#312/#407); executantul n-are voie să oprească procesul → se schimbă la S112 (sau Adrian de mână, opțional; comanda în raportul S109).
- Riscul de urmărit: discul C: (~73 GB liberi; S110 salvează un model pe oră + ~4 GB date noi). Sub 15 GB → oprire și întrebare la Adrian (fără ștergeri singure).
- Fără grabă: `lucru\memorie_mare` (~10,5 GB), Release-ul `kronos-kgr1-513`.
