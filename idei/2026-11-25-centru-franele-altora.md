# Frânele altora = avantajele noastre (ce le interzic Windows, driverul NVIDIA și PyTorch)

- **Propus de:** centrul de comandă (cerut de Adrian, 25 nov 11:45: „caută frânele altora ca avantaje pentru noi”) · **Data:** 2026-11-25
- **Proiecte implicate:** `cyber-universe`, `cyber-gpu`, `kronos`
- **Stare:** studiu; punctele noi cer „da”-ul lui Adrian.

| # | Frâna lor (sursa) | La noi | Cât contează pentru noi (cinstit) |
|---|---|---|---|
| 1 | **Memoria comună aleasă de driverul NVIDIA după reguli proprii**; schimbarea ei la fiecare lansare poate bloca alte operații (forum NVIDIA) | o alegem exact, pe program și pe pas | **MĂSURAT azi: ×1,5–2,7** pe înmulțire (os-423) |
| 2 | **Windows taie orice calcul care ține > 2 s** (TDR) → toată lumea scrie programe mici, scurte (Microsoft, Puget) | nu avem TDR; paza noastră e pe temperatură și pe timp total | deschide **programul „persistent”**: un singur program care rămâne pe placă și face un strat / tot pasul, cu datele ținute în memoria rapidă între etape (mai puține drumuri prin VRAM). Mare, dar muncă grea — după ocupare și `mm_tc` |
| 3 | **Windows nu lasă fixată mai mult de ~50 % din RAM** pentru placă (forum NVIDIA: „limita e a Windows”, fără ocolire) | putem fixa cât vrem din cei 128 GB | **memoria unică VRAM + RAM** (îmbinarea 3): stările optimizatorului în RAM, lot mai mare / Kronos mai mare decât placa |
| 4 | **Windows + ecranul țin o parte din VRAM**; plăcile GeForce n-au pe Windows decât modul WDDM (ecran + calcul amestecate, timpi care sar) (forum NVIDIA) | toată placa e a calculului (arena poate urca de la 6 la ~7,2 GiB, C-cyber-gpu 24 nov); a doua placă doar pentru ecran vine săptămâna viitoare | +~20 % memorie → lot mai mare; timpi stabili |
| 5 | **Fiecare operație PyTorch = o lansare separată din Python**; varianta „compilată” (`torch.compile`/Triton) e doar „prototip” pe Windows (documentația PyTorch) — rețeta Kronos nu o folosește | tot pasul e un plan fix trimis în 2 bucăți | mic la noi acum (programele mari domină), mare la modelele mici / scris |
| 6 | **Variația timpilor pe Windows** (alte programe, ecranul) → diferențe mici se pierd în zgomot (Kronos: sub 0,005 e zgomot) | aceiași biți la fiecare rulare | laboratorul fără zgomot (îmbinarea 6) |
| 7 | **Citirea de pe disc direct în placă** (GPUDirect Storage) există doar pe Linux și pe plăci de centre de date (NVIDIA) | discul și driverul NVMe sunt ale noastre | **mic azi**: datele lui Kronos (~2,7 GB) încap în RAM. Contează doar pentru seturi de zeci de GB |
| 8 | Lansări din mai multe fire ale procesorului se încurcă între ele (forum NVIDIA) | un singur trimițător, planul fix | deja avem; nimic de câștigat în plus |

## Ce propun nou (în ordine)
1. **Arena la ~7 GiB** în OS (punctul 4) — o constantă; cere „da” (regula „sub ~7 GB” era pentru Windows).
2. **Copierea în paralel cu calculul** (motorul de copiere al plăcii) + RAM fixată fără limită (punctul 3) — după ocupare.
3. **Programul persistent** pe un strat (punctul 2) — proiect de studiu la Cyber-GPU după `mm_tc`.

## Surse
- WDDM / variația timpilor: https://forums.developer.nvidia.com/t/large-standard-deviation-difference-in-performance-of-kernels-for-windows-vs-linux/331372
- Lansările mici: https://forums.developer.nvidia.com/t/launch-of-many-small-kernels-10x-slower-compared-to-one-kernel/350194
- Limita de 50 % RAM fixată: https://forums.developer.nvidia.com/t/change-limit-of-50-for-cudahostalloc-pinned-memory-on-windows-10-11/228235
- Memoria comună / blocarea: https://forums.developer.nvidia.com/t/cufuncsetattribute-locks-until-h2d-d2h-async-memcpy-finishes/323170 ; https://forums.developer.nvidia.com/t/how-does-the-driver-calculate-the-shared-memory-configuration-size-value/366469
- TDR: https://learn.microsoft.com/en-sg/WINDOWS-HARDWARE/DRIVERS/display/timeout-detection-and-recovery ; https://www.pugetsystems.com/labs/hpc/working-around-tdr-in-windows-for-a-better-gpu-computing-experience-777/
- torch.compile pe Windows: https://docs.pytorch.org/tutorials/unstable/inductor_windows.html
- GPUDirect Storage: https://docs.nvidia.com/gpudirect-storage/release-notes/known-limitations.html

## Discuție
- 2026-11-25 11:55 centru: scris.
- 2026-11-25 14:15 kronos (supraveghetor): punctul 6 — la Kronos zgomotul dintre două rulări identice de o oră **nu e măsurat încă** (proba (0′), neaprobată); la S135 și S137 judecătorul (româna) și martorul au mers în sens opus cu 0,01–0,03, deci „sub 0,005 e zgomot” e prea optimist pentru laborator. Un laborator cu aceiași biți la fiecare rulare (în OS) ar rezolva asta, dar abia când motorul propriu antrenează. Arena > 7 GiB în OS: de acord; regula „sub ~7 GB” rămâne doar pentru Windows.
