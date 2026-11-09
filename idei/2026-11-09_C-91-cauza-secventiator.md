# C-91: cauza probabilă a opririi la I8 („secventiator: marime sau index in afara bufferului”)

- **Propus de:** `cyber-universe` · **Data:** 2026-11-09 (08:15 ora României)
- **Proiecte implicate:** `cyber-gpu` (reparația), `cyber-universe` (integrarea + Release)
- **Stare:** propus — diagnostic pentru C-91 punctul (1); reparația o face doar `cyber-gpu` (codul lui). Nimic schimbat în repo-ul cyber-gpu.

## Ideea (pe înțelesul lui Adrian)
Placa trimite la I8 o listă de comenzi („secvențiatorul”) într-o cutie mare din care e plină doar o parte.
Codul nostru crede că toată cutia e plină și, fiindcă mesajul aduce doar partea plină, zice „în afara bufferului” și se oprește.
Placa n-a greșit nimic; e o citire greșită a unui câmp, ușor de reparat.

## Detaliu tehnic (pentru sesiunea cyber-gpu)
- Locul: `crates/nvidia-ga104/src/gsp/rpc.rs`, `decode_sequencer` (cyber-gpu `8277933`, la fel în `34a9793` folosit de OS).
  Acum: `size = bufferSizeDWord`, `words = (payload.len()-40)/4`, eroare dacă `size > words || index > size`, iar comenzile = primele `size` cuvinte.
- În `rpc_run_cpu_sequencer_v17_00`, `bufferSizeDWord` = **capacitatea** bufferului din GSP, iar `cmdIndex` = **câte cuvinte sunt folosite**.
  Driverul public NVIDIA 570.144 (`src/nvidia/src/kernel/gpu/gsp/kernel_gsp.c`, `kgspExecuteSequencerBuffer_IMPL`, citit doar ca documentație) face:
  `buffer_end = cmdIndex`, verifică `bufferSizeDWord != 0` și `cmdIndex < bufferSizeDWord`, apoi rulează comenzile de la 0 până la `cmdIndex`.
  Nouveau (r535) la fel: bucla până la `seq->cmdIndex`. Mesajul RPC aduce doar cuvintele folosite, deci pe placa reală `bufferSizeDWord > words` → eroarea noastră.
- `gpu-sim` / `FakeGsp` (și testul `sequencer_header_decodes_without_executing`) pun `bufferSizeDWord` = numărul de cuvinte trimise, de aceea simularea n-a prins-o.
- Reparația propusă (comportament ca la NVIDIA): comenzile = cuvintele `0..cmdIndex`; eroare dacă `bufferSizeDWord == 0`, `cmdIndex >= bufferSizeDWord`
  sau `cmdIndex > words`. Test nou: antet cu `bufferSizeDWord` mare (ex. 0x1000) și doar `cmdIndex` cuvinte în mesaj → trece; `cmdIndex > words` → refuzat;
  și în `FakeGsp` un mesaj de secvențiator cu capacitatea mai mare decât partea folosită, ca pe placă.
- Aceeași clasă de greșeală (capacitate citită ca lungime) merită verificată și la celelalte mesaje I8–I14 cu „mărime + index”.
- Jurnalul complet (`gpu-jurnal-003.txt`) încă nu e în `rezultate/2026-11-09-workstation-os275/` la 08:15; dacă are valorile `bufferSizeDWord`/`cmdIndex`, confirmă diagnosticul.

## Ce face fiecare proiect
- `cyber-gpu`: reparația + testul (C-91 pct. 1), un commit nou.
- `cyber-universe` (sarcina **P6-68**): imediat ce apare commit-ul: `kernel/Cargo.toml` pe noul commit, build, `tools/test.sh` (gpu, gpu-sim, gpu-i6, gpu-tur, kronos-gpu…), CI verde → Release nou pentru Adrian.

## Cost și riscuri
- Schimbare mică (o funcție + teste). Risc: după secvențiator pot apărea alte diferențe placă/simulare la I8 (de aceea lanțul se oprește cinstit la primul pas greșit).

## Decizia lui Adrian
- C-91 (9 nov 08:06) cere deja reparația și Release-ul; nota asta doar arată unde e greșeala.

## Discuție
- 2026-11-09 `cyber-universe`: diagnostic din citirea codului cyber-gpu (doar citire) + documentația publică NVIDIA.
