# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-16 17:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **Model în uz: #651** (24 de straturi, 183 M, de la zero, fără LLM străin), pe 8787 (local + Tailscale), procesor. După o repornire, interfața vine direct cu #651 (S115, C-124).
- **S114 (C-123) gata:** fila Chat întreabă în forma învățată și se oprește singură — saluturile și „cine ești” merg; faptele fără text încă nu.
- **S116 (C-126 A) gata, verificat:** 16.389 de perechi de chat fără text, făcute cu reguli din Wikipedia RO + șabloane (fără alt AI), și un examen de chat ținut deoparte (200 de întrebări): #651 = **25/200** acum.
- Teste: 1.477 trec, 0 pică. C: ~64 GB liberi.

## Urmează
- **S117 (C-126 A), la noapte 16 → 17 nov:** 4 h de învățat chat-ul din #651; intră în interfață doar dacă chat-ul ajunge ≥ 55/200, sociale ≥ 30/50, iar româna și „din text” nu scad.
- **S120 (C-128), procesor, în seara asta:** calcule simple făcute de program (+ examen de calcule ținut deoparte); „Nu scrie în text.” scos din răspunsurile fără text. Fără cod/Python (cerința lui Adrian: întâi vorbitul).
- **S121 (C-128), placă, 17 nov ziua:** 4 h din câștigătorul S117 cu calculele; intră în interfață doar dacă trece examenele.
- **S119 (C-127), procesor + rețea:** mai mult text românesc scris de oameni (restul FineWeb-2, oasst2 `ro`, HPLT doar cu licență deschisă); fără antrenare încă.
- **S118 (C-126 B), după S117:** 👍/👎 și corecturi în interfață + bucla care schimbă modelul doar dacă trece examenele. Conversațiile rămân doar pe workstation.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` rămâne cu **#513** (KGR1). #651 e mai bun, dar ~2× mai mare; un KGR1 nou doar după „da”-ul lui Adrian.
- Unelte pentru date mari cu RAM mic (`date_bucati`).

## De ce are nevoie de la ceilalți
- De la centrul de comandă: o notă în `COMENZI.md` când Adrian vrea placa workstation-ului pentru `gpu lant` (Cyber-GPU, I9) — Kronos nu pornește nimic pe placă până scrie „a terminat”. Placa e ocupată: noaptea 16 → 17 (S117) și 17 nov ziua (S121).
- De la `suita-office`: nimic.

## Blocaje / nevoie de Adrian
- Niciun blocaj. De la Adrian: nimic acum.
- Posibil după S119: dacă CulturaX cere acceptarea condițiilor pe Hugging Face, decizia e a lui Adrian.
- Fără grabă: `lucru\memorie_mare` (~10,5 GB), Release-ul `kronos-kgr1-513`.
