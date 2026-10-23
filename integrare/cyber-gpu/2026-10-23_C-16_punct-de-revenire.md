# C-16: punctul de revenire al Cyber-GPU (pentru sesiunea OS)

*Scris de sesiunea Cyber-GPU, 23 oct 2026, 19:50. Doar informație; nimic aplicat în `cyber-universe`.*

- C-16 cere dependența pe `cyber-gpu` fixată pe tag-ul `stabil-2026-10-23` / commit `41e44ba`.
- Tag-ul a fost creat (adnotat, pe `41e44ba`), dar **push-ul lui e refuzat** din sesiunea cloud (HTTP 403 — politica sesiunii permite doar ramuri).
  Pe GitHub tag-ul **nu există** până nu-l urcă Adrian.
- **Recomandare:** fixați pe commit, care e imuabil: `git = "https://github.com/Adriancu91/cyber-gpu", rev = "41e44ba492c606ba5abf15126210caf1313b9e6e"`.
  Commit-ul e pe ramura `g0-g2-fundatie` (`main` nu există), care doar crește (fără push --force), deci rămâne descărcabil.
- Ce conține `41e44ba` (verificat în sesiunea 3: 82 de teste, build `x86_64-unknown-none`): `gpu-core`, `gpu-pci`, `nvidia-ga104` (probe nivel 0 +
  I2/I3 doar citire, **nicio cale de scriere în BAR0**: `ReadOnlyBar0` n-are metodă de scriere; singura scriere în configurația PCI e dimensionarea
  BAR, doar la cerere explicită), `gpu-compute` (backend CPU), `gpu-sim` (doar teste). Toate MIT, fără dependențe externe.
- După `41e44ba` au intrat (sesiunea 3, pe aceeași ramură): `fwsec.rs`, `fb_layout.rs`, `radix3.rs` — doar citire/aritmetică; **nu sunt necesare** pentru C-16.
