# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-20 08:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **S128 (C-150) gata, verificat: #651 e exportat în formatul plăcii.** `kronos_651_q8_0.kgr`, 206.898.464 octeți, SHA-256 `2edf75ac12eedb54bd2eace55d82bf5c14cc3240e11c0fca40263d3e65ea0bf2`, pe workstation în `C:\Kronos\cyberspace\lucru\export\`. Aceleași simboluri ca PyTorch pe cele 3 texte (dif. max 3,1e-5), marja minimă 0,051. Față de #513: doar mărimile (24 de straturi). Fișa: `integrare/kronos/MODEL_651.md`.
- **S129 în lucru:** pașii pe procesor (date noi: „din text” ×2 + mai multe înmulțiri). Placa nefolosită ziua (C-149).
- Chat-ul Kronos merge pe 8787 cu **#651**. Testele: 1.539 trec. Disc C: ~154–165 GB liberi.

## Urmează
- **S129 pe placă, noaptea 20 → 21 nov (19:00, pornire cel târziu 00:30; liberă la 07:00):** 4 h din #720, aceleași praguri (formulări ≥ 48 %). Verdictul la 02:15–08:15 pe 21 nov.
- Bucla 👍/👎 (S118) pornește pe placă la ≥ 30 de lecții noi (acum 2).

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL_651.md` (nou) — #651, 183 M parametri, fișierul `KRONOS\kronos_651_q8_0.kgr` (îl copiază centrul de comandă pe stick, verificând suma). `MODEL.md` rămâne cu **#513**, modelul implicit al ciclului.
- **Pentru `cyber-gpu`:** cifrele exacte ale lui #651 pentru limitele din simulare (C-147): 24 de straturi, 12 capete, n_emb 768, context 512, vocabular 16.384, 292 de tensori (98 Q8_0, 194 F32).
- Unelte pentru date mari cu RAM mic (`date_bucati`). La treapta 3 a uneltelor de independență: „pasul de aur” (după „da”-ul lui Adrian).

## De ce are nevoie de la ceilalți
- De la centrul de comandă: copierea lui `kronos_651_q8_0.kgr` pe stick (suma de mai sus).
- O rezervare în `RESURSE.md` dacă un test vrea placa noaptea (19:00–07:00); altfel noaptea e a lui Kronos. Ziua Kronos nu atinge placa.
- De la `suita-office`: nimic.

## Blocaje / nevoie de Adrian
- Nimic urgent.
- Opțional, la workstation (în Windows): `git -c core.editor=true rebase --continue` în `C:\Kronos\cyberspace` (închide o operație Git rămasă deschisă; nu oprește lucrul).
- Doar dacă vrea: „da CulturaX” după ce acceptă condițiile pe Hugging Face. Fără grabă: Release-ul `kronos-kgr1-513`.
