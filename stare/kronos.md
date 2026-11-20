# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-20 02:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **S127 gata, verificat: rămâne #651.** Modelul nou #720 a luat 46,0 % la întrebările formulate altfel (pragul 48 %); e cel mai bun la chat (50) și calcule (80), dar „din text” a coborât exact la prag (218). Examenele s-au terminat la 01:15; placa e liberă și rămâne liberă până la 07:00.
- Chat-ul Kronos merge pe 8787 cu **#651**. Testele: 1.539 trec. Disc C: ~165 GB liberi. Placa noaptea max 6.690 MB / 64 °C.
- Regula C-149 se aplică: ziua (08:00–18:00) Kronos nu pune nimic pe placă.

## Urmează
- **S128 (C-150), 20 nov de la 07:00, doar procesor:** `kronos_651_q8_0.kgr` + `.sha256` în `C:\Kronos\cyberspace\lucru\export\`; apoi `integrare/kronos/MODEL_651.md` aici în hub (arhitectura, mărimea, SHA-256, 3 texte de control, marje, ce diferă față de #513), copiat de supraveghetor după ce e gata.
- **S129, noaptea 20 → 21 nov (19:00–07:00):** încă o rundă din #720, cu „din text” de 2 ori mai des și mai multe înmulțiri; aceleași praguri. Partea de procesor ziua, după S128.
- Bucla 👍/👎 (S118) pornește pe placă la ≥ 30 de lecții noi (acum 2).

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` rămâne cu **#513** (KGR1), modelul implicit al ciclului. **#651 vine în `MODEL_651.md` (C-150, azi)**; fișierul îl copiază centrul de comandă pe stick (`KRONOS\kronos_651_q8_0.kgr`), verificând suma.
- **Pentru `cyber-gpu`:** cifrele exacte ale lui #651 (straturi, capete, n_emb, context, vocabular, mărimea) pentru limitele din simulare (C-147) — în `MODEL_651.md` după S128.
- Unelte pentru date mari cu RAM mic (`date_bucati`).

## De ce are nevoie de la ceilalți
- De la `cyber-universe` / `cyber-gpu` / centrul de comandă: o rezervare în `RESURSE.md` dacă un test vrea placa noaptea (19:00–07:00); altfel noaptea e a lui Kronos. Ziua placa e a testelor, Kronos nu o atinge (S128 e doar pe procesor).
- De la `suita-office`: nimic.

## Blocaje / nevoie de Adrian
- Nimic urgent.
- Opțional, la workstation (în Windows): `git -c core.editor=true rebase --continue` în `C:\Kronos\cyberspace` (închide o operație Git rămasă deschisă; nu oprește lucrul).
- Doar dacă vrea: „da CulturaX” după ce acceptă condițiile pe Hugging Face. Fără grabă: Release-ul `kronos-kgr1-513`.
