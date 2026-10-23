# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-24 01:35 (ora României) · **de:** sesiunea Cyber-GPU programată (cloud, fără placă)

## Acum
- **Nimic nu s-a testat pe RTX 3070 Ti.** Ce scrie „merge” e verificat doar pe calculator (SIMULARE sau calcul pur). Niciun program pe GPU.
- **OS-ul folosește deja bibliotecile noastre** (C-16, făcut de sesiunea OS, fixat pe commit-ul `41e44ba`, Release `os-189`).
- **Nou în noaptea asta:** calculul lui Kronos pe procesor se poate împărți acum pe mai multe nuclee și la atenție, softmax și pierdere
  (`gpu-compute::rows`), cu rezultat identic bit cu bit cu referința oricum s-ar împărți. Ghid pentru OS: `integration/cyber-universe/UTILIZARE.md`.
- 106 teste trec; CI verde (rularea 11).

## Urmează
- Fără placă și fără decizia de licență: **nimic util de făcut** — pasul următor (mesajele către GSP) depinde de firmware-ul NVIDIA.
- Cu placa (când revine Adrian): testul I0–I3 (+ 5c, FWSEC), lista în `docs/TEST_MATRIX.md` partea B.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste), MIT, fără dependențe externe.
  Fixarea pe `41e44ba` rămâne valabilă: **de atunci s-a doar adăugat**, nimic redenumit sau șters (verificat 24 oct).
  Opțional, la o mutare a fixării: I2/I3/FWSEC doar citire (SIMULARE) și `gpu-compute::rows` (mai multe nuclee). Detalii: `integration/cyber-universe/UTILIZARE.md`.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, matmul rapid cu greutăți bf16, împărțire pe nuclee fără stare globală.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: comenzile `gpu gfw` / `gpu vbios` (doar citire), doar după „da”-ul lui Adrian.
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian (nimic urgent; când se întoarce)
- **Tag-ul `stabil-2026-10-23`** e făcut corect pe `41e44ba`, dar din cloud nu se poate urca (403). Nu blochează: OS-ul e fixat pe commit.
  Când ai 2 minute: GitHub → cyber-gpu → Releases → „Draft a new release” → „Choose a tag” → `stabil-2026-10-23` → „Create new tag” →
  Target: commit-ul `41e44ba` (din „Recent commits”) → bifează „Set as a pre-release” → Publish.
- **Licența firmware-ului NVIDIA** (blochează tot de la I4): argumentele în `docs/RESEARCH_I4_I8.md` §5.1.
- **Compilatorul pentru programele GPU:** Mesa NAK sau `ptxas`. Recomandarea tehnică: NAK pentru primul program (§5.2).
- **Fereastra pe workstation (~30 min, Kronos oprit):** `gpu identifica` (OS-ul o are din `os-189`), apoi `gpu gfw` / `gpu vbios` dacă OS-ul le primește.
