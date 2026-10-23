# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-23 19:50 (ora României) · **de:** sesiunea Cyber-GPU programată (cloud, fără placă)

## Acum
- **Nimic nu s-a testat pe RTX 3070 Ti.** Ce scrie „merge” e verificat doar pe calculator (SIMULARE sau calcul pur). Niciun program pe GPU.
- **Nou azi seară (doar citire / doar calcule):** (1) găsim în VBIOS unde stă firmware-ul FWSEC al plăcii și cât de mare e — fără să-i citim
  conținutul; (2) calculul zonelor din memoria plăcii pe care le va ocupa firmware-ul GSP (pe 8 GiB: ultimii ~162 MiB); (3) lista de pagini
  prin care GSP își găsește programul în RAM („radix3”). 102 teste trec.
- **CI pe GitHub merge din nou** (repo-ul e public): rulările 7 și 8 verzi.
- Calcul pe procesor pentru Kronos: neschimbat (matmul pe blocuri și bf16, identic bit cu bit cu referința).

## Urmează
- Fără placă și fără decizia de licență: **nimic util de făcut** — pasul următor (mesajele către GSP) depinde de versiunea firmware-ului NVIDIA.
- Cu placa (când revine Adrian): testul I0–I3 (+ noul 5c, FWSEC), lista în `docs/TEST_MATRIX.md` partea B.

## Ce oferă proiectul celorlalți
- `cyber-universe` (C-16): crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste), MIT, fără dependențe
  externe, fixate pe commit-ul `41e44ba` (vezi `integrare/cyber-gpu/2026-10-23_C-16_punct-de-revenire.md`).
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor + matmul rapid cu greutăți bf16.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: comenzile `gpu gfw` / `gpu vbios` (doar citire), doar după „da”-ul lui Adrian.
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian (nimic urgent; când se întoarce)
- **Tag-ul de revenire `stabil-2026-10-23` (C-16) nu s-a putut urca:** sesiunea din cloud are voie să urce doar ramuri, nu tag-uri (refuz 403).
  Tag-ul e făcut corect pe `41e44ba`. Variante: (a) OS-ul fixează dependența pe commit-ul `41e44ba` (la fel de sigur; C-16 permite „tag / commit”);
  (b) Adrian, de pe calculatorul lui: `git fetch && git tag -a stabil-2026-10-23 41e44ba -m "punct de revenire" && git push origin stabil-2026-10-23`.
- **Licența firmware-ului NVIDIA** (blochează tot de la I4): îl folosim sau nu? Argumentele: `docs/RESEARCH_I4_I8.md` §5.1.
- **Compilatorul pentru programele GPU:** Mesa NAK (MIT) sau `ptxas` (NVIDIA). Recomandarea tehnică: NAK pentru primul program (§5.2).
- **Fereastra pe workstation (~30 min, Kronos oprit):** `gpu identifica`, apoi `gpu gfw` și `gpu vbios` dacă OS-ul le are. Notează și poza din BIOS
  cu „Above 4G Decoding”.
- „Da” pentru propunerea către OS (comenzile `gpu gfw` / `gpu vbios`).
