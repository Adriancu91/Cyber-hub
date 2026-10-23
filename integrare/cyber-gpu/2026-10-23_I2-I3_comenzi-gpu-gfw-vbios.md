# Propunere pentru OS: `gpu gfw` și `gpu vbios` (doar citire) — 23 oct 2026, sesiunea Cyber-GPU 2

**Stare: propus.** Nu e o comandă; o preia sesiunea OS doar dacă Adrian spune „da” (ar intra la C-11 / fereastra a doua pe workstation).

## De ce
În `cyber-gpu` sunt gata (testați **doar în SIMULARE**) pașii I2 (firmware-ul plăcii a terminat pornirea?) și I3 (se poate citi VBIOS-ul?).
Ambii sunt **doar citire**. Ca să fie verificați pe RTX 3070 Ti, OS-ul are nevoie de două comenzi. Comanda voastră `gpu` mapează deja
o pagină din BAR0 **fără drept de scriere** — același mecanism ajunge, cu câteva pagini în plus.

## `gpu gfw` (I2)
- Pagina BAR0 `0x118000` (mapată ca acum: necache-abilă, fără scriere).
- La fiecare ~1 ms, maximum 4 s: citește `0x118128`. Doar dacă **bitul 0 = 1**, citește `0x118234`; terminat când `(valoare & 0xff) == 0xff`.
  Nu citi `0x118234` înainte ca bitul 0 să fie 1 (registrul e încă protejat — nova-core).
- Opriri: `0xffffffff` → „placa nu raspunde”; `0xbadfxxxx` → „eroare de acces” (nu e dată). Pe ecran/jurnal: numărul de runde, timpul,
  ultimele două valori, `0 scrieri`.
- Sursă: nouveau `devinit/tu102.c` (`tu102_devinit_wait`, MIT); procedura nova-core `gfw.rs`.

## `gpu vbios` (I3)
- Fereastra PROM = BAR0 `0x300000 … 0x3FFFFF` (1 MiB = 256 de pagini; se pot mapa pe rând, câte una, fără scriere).
- Pași: primul cuvânt: `…AA55` → imaginile încep la 0; `0x4947564E` („NVGI”) → antet IFR (v1–2: începutul la `FIXED_DATA_SIZE+4`;
  v3: director „RFRD”, începutul la `dir+8`). Apoi lanțul: `0xAA55`, PCIR la `+u16(0x18)`, tipul la PCIR+0x14, mărimea ×512 la PCIR+0x10,
  „ultima” = bitul 7 la PCIR+0x15; dacă după PCIR (aliniat la 16) e „NPDE”: mărimea ×512 la +8 și „ultima” la +0x0A au prioritate.
  În imaginea PCI-AT: tabela BIT (`FF B8 'B' 'I' 'T'`), jetoanele de la +12 (mărime la +9, număr la +10).
- Pe ecran: lista imaginilor (offset, tip: 0x00 PCI-AT / 0x03 EFI / 0x70 NBSI / 0xE0 FWSEC, mărime), dacă BIT are jetonul 0x70, numărul de citiri.
- Limite: 2 s, maximum 300 000 de citiri, nicio citire în afara ferestrei. **Dacă primul cuvânt nu e o semnătură: oprire** (nouveau
  oprește „umbrirea ROM” cu o scriere în configurație — nu se face fără aprobarea lui Adrian).
- Sursă: documentația kernelului Linux „nova/core/vbios”, Specificația PCI Firmware 3.0, nouveau `bios/npde.c`, `bit.c` (MIT).

## PASS pe workstation (din `cyber-gpu/docs/TEST_MATRIX.md`)
- `gpu gfw`: bitul 0 = 1, `0xff`, în < 4 s; 0 scrieri.
- `gpu vbios`: semnătură la început; PCI-AT, EFI și cel puțin o FWSEC; BIT cu jetonul 0x70; ecranul rămâne viu; 0 scrieri.

## Observație separată (K6-CPU)
Biblioteca `gpu-compute` din `cyber-gpu` are acum matmul pe blocuri și matmul cu greutăți bf16, identice bit cu bit cu referința
(pe gazdă: ~12× mai rapid decât varianta simplă). Ținta `x86_64-unknown-none` compilează însă **fără SSE** (virgulă mobilă în software);
după K6-01 (SSE/AVX pornite), viteza reală pentru Kronos în OS depinde de compilarea codului de calcul cu SSE/AVX activ. De ținut minte la K6-CPU.
