# Stare: Cyber Universe OS — sesiunea paralelă F4 (`cyber-universe`, ramura `wip/P7-F4-hardware`)

**Actualizat:** 2026-11-04 23:51 (ora României) · **de:** sesiunea paralelă F4 (programată, fără Adrian)

## Acum
- Gata pe ramura `wip/P7-F4-hardware` (NU pe `main`; sesiunea OS principală o integrează): comanda **`hw lista`** și **`hw lista --detalii`**.
- Arată, doar prin citiri sigure: procesorul (nume, model, nuclee, instrucțiuni), memoria, toate dispozitivele PCI cu nume
  (tabel propriu mic: Intel, NVIDIA, Realtek, MediaTek, Qualcomm, plăcile Wi-Fi des întâlnite, RTX 3070 Ti / 3060 Laptop), clasă și driver,
  dispozitivele USB deja găsite, tabelele ACPI. Cu `--detalii`: registrele de configurare, BAR-urile, capabilitățile, legătura PCIe, starea D0–D3.
- **Wi-Fi:** placa e doar identificată (după clasă și id) și i se citesc registrele de bază din configurare. **Niciun driver, nicio scriere.**
  Nicio scriere pe placa video. Ultimul rând spune mereu „0 scrieri in dispozitive”.
- Teste: scenariul nou QEMU `hw-lista` (40 de verificări pe portul serial) + un test al tabelului de nume la pornire; `boot`, `log`, `shell` trec local.
  **CI pe ramură: verde** (rularea 227, toate scenariile, inclusiv cele cu internet).

## Urmează
- Integrarea ramurii în `main` de către sesiunea OS principală (sarcina P6-51 din `docs/TASKS.md`).
- Mai departe (nefăcut aici): raportul `hw lista` scris și pe stick (`/usb/raport/hw-*.txt`); starea fiecărui port USB.
- Pe placa reală (laptop/workstation): `hw lista --detalii` + o poză, ca să completăm tabelul de nume cu ce apare ca „model necunoscut”.

## Ce oferă proiectul celorlalți
- `hw lista` dă o listă clară a hardware-ului unui calculator (util pentru Cyber-GPU: identificarea plăcii fără nicio scriere).

## De ce are nevoie de la ceilalți
- nimic

## Blocaje / nevoie de Adrian
- niciunul (când porniți OS-ul pe laptop, o poză cu `hw lista` ajută; nu e obligatoriu)
