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

## Verificat local (doar în copia de lucru a sesiunii OS, nimic urcat în cyber-gpu)
Cu schimbarea de mai jos aplicată pe cyber-gpu `8277933`, `cargo test --workspace` trece tot (nvidia-ga104: 277 PASS). De observat: și ajutorul de test `payload()` din `sequencer.rs` punea capacitatea = numărul de comenzi și `cmdIndex = 0` — exact invers față de placă. `FakeGsp` din `gpu-sim` nu trimite deloc un mesaj de secvențiator, deci testele OS din QEMU nu ating codul ăsta. Sesiunea cyber-gpu decide dacă o ia așa sau o face altfel:

```diff
diff --git a/crates/nvidia-ga104/src/gsp/rpc.rs b/crates/nvidia-ga104/src/gsp/rpc.rs
index 2758b7b..b8d1474 100644
--- a/crates/nvidia-ga104/src/gsp/rpc.rs
+++ b/crates/nvidia-ga104/src/gsp/rpc.rs
@@ -259,7 +259,7 @@ pub fn decode_sequencer(payload: &[u8]) -> GpuResult<SequencerHeader> {
     let words = (payload.len() - 40) / 4;
     let size = get_u32(payload, 0);
     let index = get_u32(payload, 4);
-    if size as usize > words || index > size {
+    if size == 0 || index >= size || index as usize > words {
         return Err(GpuError::InvalidArgument(
             "secventiator: marime sau index in afara bufferului",
         ));
@@ -268,7 +268,7 @@ pub fn decode_sequencer(payload: &[u8]) -> GpuResult<SequencerHeader> {
     for (i, r) in reg_save.iter_mut().enumerate() {
         *r = get_u32(payload, 8 + 4 * i);
     }
-    let commands = (0..size as usize)
+    let commands = (0..index as usize)
         .map(|i| get_u32(payload, 40 + 4 * i))
         .collect();
     Ok(SequencerHeader {
@@ -333,8 +333,8 @@ mod tests {
     #[test]
     fn sequencer_header_decodes_without_executing() {
         let mut p = alloc::vec![0u8; 40 + 4 * 6];
-        put_u32(&mut p, 0, 4);
-        put_u32(&mut p, 4, 0);
+        put_u32(&mut p, 0, 0x1000); // capacity, larger than what is sent
+        put_u32(&mut p, 4, 4); // words in use
         put_u32(&mut p, 8, 0xdead);
         for i in 0..6 {
             put_u32(&mut p, 40 + 4 * i, 100 + i as u32);
@@ -342,7 +342,9 @@ mod tests {
         let s = decode_sequencer(&p).unwrap();
         assert_eq!(s.commands, [100, 101, 102, 103]);
         assert_eq!(s.reg_save[0], 0xdead);
-        put_u32(&mut p, 0, 7); // more words than present
+        put_u32(&mut p, 4, 7); // more words than present
+        assert!(decode_sequencer(&p).is_err());
+        put_u32(&mut p, 4, 0x1000); // index must stay below capacity
         assert!(decode_sequencer(&p).is_err());
     }
 
diff --git a/crates/nvidia-ga104/src/gsp/sequencer.rs b/crates/nvidia-ga104/src/gsp/sequencer.rs
index 6512093..e8de0da 100644
--- a/crates/nvidia-ga104/src/gsp/sequencer.rs
+++ b/crates/nvidia-ga104/src/gsp/sequencer.rs
@@ -360,7 +360,8 @@ mod tests {
 
     fn payload(cmds: &[u32]) -> Vec<u8> {
         let mut p = alloc::vec![0u8; 40];
-        p[0..4].copy_from_slice(&(cmds.len() as u32).to_le_bytes());
+        p[0..4].copy_from_slice(&0x1000u32.to_le_bytes());
+        p[4..8].copy_from_slice(&(cmds.len() as u32).to_le_bytes());
         for w in cmds {
             p.extend_from_slice(&w.to_le_bytes());
         }
```
