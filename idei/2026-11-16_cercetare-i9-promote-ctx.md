# Cercetare open source pentru I9 (`PROMOTE_CTX` virtual) — ce fac NVIDIA, nouveau și tinygrad

- **Propus de:** centrul de comandă (la cererea lui Adrian, 16 nov 12:20: „vezi ce mai găsești pe GitHub prin proiecte open source… care ne ajută la driverul nostru gpu”) · **Data:** 2026-11-16
- **Proiecte implicate:** `cyber-gpu` (și `cyber-universe` doar pentru testul pe placă)
- **Stare:** propus — **doar informație**, nimic de aprobat; Cyber-GPU o citește la sesiunea următoare

## Ideea (pe înțelesul lui Adrian)
Lanțul plăcii se oprește la I9, la al 11-lea mesaj: „spune-i plăcii unde sunt, în memoria ei, bufferele de lucru ale canalului” (`PROMOTE_CTX`, jumătatea virtuală).
Am citit cum fac exact acest pas trei drivere deschise: driverul oficial NVIDIA (open-gpu-kernel-modules **570.144**, aceeași versiune ca a noastră, MIT),
nouveau (Linux, MIT) și tinygrad (MIT, merge pe plăci Ampere fără driverul NVIDIA). Codul nostru face deja la fel ca tinygrad; am găsit **4 lucruri concrete
de verificat** și o diferență de versiune de firmware. Motivul exact îl va da oricum testul următor pe workstation (jurnalul scrie acum „motivul eșecului”).

## Ce am găsit (cu surse, citite ca specificație — nimic copiat)

1. **Driverul oficial NVIDIA, cazul nostru exact** (spațiu de adrese „deținut din afară”, `IS_EXTERNALLY_OWNED`, cum avem noi la I9c):
   - `src/nvidia/src/kernel/gpu/gr/kernel_graphics_context.c`, `kgrctxPreparePromoteCtxBuffer_IMPL`: „RM is not responsible for promoting the buffers when UVM is enabled”
     → `if (gvaspaceIsExternallyOwned(pGVAS)) return NV_OK;` — adică **driverul de kernel trimite doar jumătatea fizică**; jumătatea virtuală o trimite **UVM**, separat.
   - `src/nvidia/src/kernel/rmapi/nv_gpu_ops.c`, `nvGpuOpsBindChannelResources` (= jumătatea virtuală a lui UVM): `hChanClient` = clientul canalului,
     **`hObject` = handle-ul CANALULUI** (`RES_GET_HANDLE(pKernelChannel)`), trimis la subdispozitiv; fiecare intrare are DOAR `bufferId` + `gpuVirtAddr`
     (restul 0); **`entryCount` = numărul de buffere raportat de RM pentru acel canal** prin `NV2080_CTRL_CMD_GR_GET_CTX_BUFFER_INFO`.
   - `_nvGpuOpsRetainChannelResources`: UVM află lista bufferelor (tip, mărime, **aliniere**, **pageSize**, contiguu, aperture) cu
     `NV2080_CTRL_CMD_GR_GET_CTX_BUFFER_INFO(hUserClient, hChannel)` și le mapează exact așa înainte de promovarea virtuală.
   - `kernel_graphics_object.c`, `kgrobjPromoteContext_IMPL` (cazul obișnuit, fără UVM): **un singur** `PROMOTE_CTX` pe obiectul de calcul, cu PA și VA
     în aceeași intrare; `hObject` = părintele obiectului (canalul); `engineType` = `NV2080_ENGINE_TYPE_GR(n)`. Lista pentru calcul (fără 3D):
     MAIN, PM, PATCH, FECS_EVENT, PRIV_ACCESS_MAP, UNRESTRICTED_PRIV_ACCESS_MAP.
2. **nouveau** (`drivers/gpu/drm/nouveau/nvkm/subdev/gsp/rm/r535/gr.c`, MIT): tot un singur apel cu PA+VA; MAIN = `ALIGN(size, 0x1000) + 64 × 0x1000`
   (antetele de subcontext); pagina 2 MiB / 64 KiB / 4 KiB după mărime; ATTRIBUTE_CB aliniat la `order_base_2(size)`; bufferele mapate **`priv = 1`**
   (mapare privilegiată) cu alinierea din `get_ctxbufs_info`; promovarea per canal se face la crearea canalului.
3. **tinygrad** (`tinygrad/runtime/support/nv/ip.py`, `promote_ctx`, MIT, citit azi la commit `2466e27`): exact cele două jumătăți ca noi (fizic, apoi virtual,
   buffere 0/1/2), `hObject` = canalul, MAIN + 0x40000. Suportă Ampere (`GA1xx` → firmware `ga102`) — **dar cu GSP-RM `570.190`**, nu 570.144.

## Ce ar face Cyber-GPU (de verificat, fără placă, înainte de testul următor)
- **V1 — alinierea / pagina VA**: bufferele MAIN/PM/PATCH mapate cu alinierea și pagina raportate de RM (ca UVM/nouveau), nu doar 4 KiB; dacă RM verifică VA-ul
  (aliniere sau pagină mare), asta ar explica refuzul doar la jumătatea virtuală.
- **V2 — maparea privilegiată**: nouveau mapează bufferele de context cu `priv = 1`; verifică bitul PRIV în PTE-urile noastre pentru bufferele de context.
- **V3 — lista bufferelor**: varianta oficială pentru spațiu „deținut din afară” ia lista de la `NV2080_CTRL_CMD_GR_GET_CTX_BUFFER_INFO` (pe canal) — un mesaj în plus,
  doar citire, care ar arăta exact ce buffere și ce aliniere așteaptă GSP-RM pentru canalul nostru (poate fi pus în jurnal înainte de promovare).
- **V4 — versiunea firmware**: referința care merge pe Ampere (tinygrad) folosește 570.190; noi 570.144 (decizia din 26 oct). Doar de notat ca ipoteză;
  nu se schimbă nimic fără Adrian.
- Prioritar rămâne **testul pe workstation** (`gpu lant`, varianta 1, os-302+): `text motivul esecului` va spune care e.

## Cost și riscuri
- Doar citire și comparare în cod; V3 ar fi un mesaj RM de citire în plus. Nicio scriere nouă în placă fără fereastra cu Adrian.

## Decizia lui Adrian
- 2026-11-16 13:47: Adrian aprobă V2 + V3 în SIMULARE → comanda **C-125**. Testul pe placă rămâne în fereastra cu Adrian.

## Discuție
- 2026-11-16 centrul de comandă: surse — NVIDIA/open-gpu-kernel-modules tag 570.144 (MIT); nouveau r535 gr.c (MIT); tinygrad commit 2466e27 (MIT);
  nova-core (Rust, Linux) are deocamdată doar infrastructura RM control + ChannelIdPool (iul. 2026), fără canal de calcul — nu ajută încă la I9.
