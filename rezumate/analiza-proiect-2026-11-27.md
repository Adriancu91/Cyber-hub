# Analiza proiectului — frâne, erori, plan de reparație (ciorna 1)

**Cerută de Adrian:** 27 nov 2026, 17:57. **Regula:** analiza merge în paralel cu testele în curs; **nicio reparație și nicio schimbare de implementare** până se termină lucrul deja început (v7 în pas, token32_v2c). Apoi reevaluare cu toate datele și reparații în ordinea impactului, cu test înainte / după.
**Starea:** ciorna 1 (27 nov 18:15). Se actualizează la fiecare rezultat nou.

## 1. Unde suntem (măsurat)

| Ce | Azi | Referință |
|---|---|---|
| Antrenare #513, lot 6 | **15 339 simb/s** (pas 200,3 ms; cu paza termică 15 301) | Windows + PyTorch, aceeași placă: ~39 300 → **39 %** |
| Scris (generare) | 351 simb/s față de 129 în Windows (×2,72, 21 nov) | baza Windows nu e cea mai bună posibilă (F32, fără memoria de context) |
| Înmulțirea cea mai bună | v7@64k: 1,15–1,46 ms (≈ 17–18 TFLOP/s) | vârful plăcii la 1 965 MHz ≈ **48 TFLOP/s** (f16 cu sume f32, fără rărire; foaia NVIDIA GA104 scalată la 48 SM) |

Eficiența (cât din vârful plăcii folosim), socotită din ~0,65 GFLOP pe simbol la antrenare:
- noi: ~10 TFLOP/s efectivi ≈ **21 %** din vârf;
- Windows / PyTorch pe aceeași placă: ~25,5 TFLOP/s ≈ **53 %**.
Deci nu placa ne limitează, ci cât de bine o folosesc programele noastre.

## 2. Unde se duce timpul (pasul record, lot 6, 200 ms)

| Bucata | ms | % | Observație |
|---|---|---|---|
| Înmulțiri (147, mm_tc_v5) | 151,1 | 75 % | ~12 TFLOP/s în medie; v7 e gata (×1,35–1,7), încă nelegat în pas |
| Atenția înainte (attn_fwd_tile3, 12) | 15,9 | 8 % | **încă fără circuitele speciale** (tensor) |
| Atenția înapoi (dS + dQKV pe circuite) | 11,7 | 6 % | deja pe circuite |
| Mărunte (Adam, GELU, sume, LayerNorm, pierdere…) | ~21 | 10 % | ~300 de lansări mici, fiecare citește / scrie memoria separat |
| În afara plăcii | ~0 | 0 % | rezolvat (două locuri + lot prin RAM; tabloul ținut în jurnal) |

## 3. Frânele, în ordinea impactului

| # | Frâna | Dovada | Câștig estimat (DEDUS) |
|---|---|---|---|
| F1 | Înmulțirile folosesc ~25–37 % din vârf | v5 în pas 12 TFLOP/s; v7 18; un program bun pe Ampere ajunge la ~70–80 % | v7 în pas: 200 → ~150 ms (**~20 000 simb/s**); la ~30 TFLOP/s: înmulțirile ~60 ms |
| F2 | Înmulțirile încă nu folosesc tehnicile standard Ampere: citiri `ldmatrix` peste tot, memoria comună dublă (încărcarea blocului următor cât se calculează cel curent, `cp.async`) | planurile v5 / v6 le notează ca „tăiate acum, de reluat” | parte din F1; aici e drumul spre 30+ TFLOP/s |
| F3 | Atenția înainte fără circuitele speciale | 15,9 ms, singura bucată mare rămasă pe calcul obișnuit | ~10 ms mai puțin pe pas |
| F4 | ~300 de lansări mărunte, fiecare cu drumul ei prin memorie | 21 ms în total | lipirea lor (ex. GELU în înmulțire, Adam într-o singură trecere) ~8–12 ms |
| F5 | Un singur test pe placă odată, 30–40 min pe ciclu (repornire + lanțul întreg) | jurnalul de azi: 8 cicluri într-o zi | mai multe rânduri într-o pornire (sistemul acceptă până la 4) → de 2–3× mai multe măsurători pe zi |

Calea spre Windows (estimat, nemăsurat): F1 v7 → ~150 ms; F3 → ~140; F4 → ~130; F2 la ~30 TFLOP/s → **~85–90 ms ≈ 34 000–36 000 simb/s (~90 % din Windows)**. Peste Windows: programul care nu se oprește între lansări și lucrurile pe care Windows nu le permite (memorie, limite de timp).

## 4. Erori și cauze care ne-au încetinit (nu de viteză)

| # | Problema | Ce a costat | Starea |
|---|---|---|---|
| E1 | Antrenarea din OS merge pe **loturi sintetice** (nu există datele reale pe stick: `index.json` lipsește) | nu avem încă o antrenare reală în OS; lot 6 nu are verificare (oracol) | **deschis — cel mai mare gol funcțional** |
| E2 | Măsurători făcute după ce placa ieșea din viteza maximă (fereastra de 600 s) | concluzia greșită „dW = frâna” (corectată) | rezolvat: paza ferestrei + 1 800 s aprobat |
| E3 | Citirile tabloului scrise pe stick la fiecare pas (+71 ms) | un record ratat | rezolvat (os-487) |
| E4 | Rânduri de test refuzate (ordinea opțiunilor) — de 2 ori azi, greșeala centrului | ~1 h de placă | rezolvat ca regulă: fiecare rând verificat întâi în testele din `ciclu.rs` |
| E5 | CI picat din cauze externe (oglinda apt 404) | ~1 h de așteptare de 3 ori | deschis — soluție: oglindă / cache pentru pachete |
| E6 | Predicțiile dau ~jumătate din câștig (dS, înmulțiri în pas) și uneori greșesc direcția (v6 la dX) | timp pe căi slabe | parțial: multe greșeli veneau din E2; de remăsurat |
| E7 | Oprirea termică 0x20 din noapte, neexplicată | un test pierdut | nu s-a repetat (max 58 °C); de urmărit |
| E8 | Comparația la scris față de Windows nu e pe cea mai bună rețetă Windows | afirmația ×2,7 e atacabilă | de remăsurat cinstit (Windows cu memoria de context) |

## 5. Comparații cu alții (ce putem lua)

- **Aceeași placă, Windows / PyTorch:** ~53 % din vârf → arată ce e posibil pe 3070 Ti.
- **Programele de înmulțire de top pe Ampere (CUTLASS / cuBLAS):** ~70–80 % din vârf, prin `ldmatrix`, `cp.async` cu memoria comună în 2–3 trepte, blocuri mari 128×128 (sau 128×256) și „swizzle” contra conflictelor. Ideile sunt publice (documentația NVIDIA PTX, articole); noi le scriem singuri (clean-room).
- **llm.c / nanoGPT speedrun:** câștigurile mari au venit din atenția „flash” (o singură trecere pe circuitele speciale), din lipirea lansărilor mărunte și din precizie mixtă — exact F3 și F4.
- **tinygrad (fără CUDA, ca noi):** a ajuns la viteze bune tot prin lipirea automată a operațiilor mărunte → confirmă F4.

## 6. Planul de reparație (după ce se termină lucrul în curs)

1. **v7 în pas** (deja în lucru: PREDARE Cyber-GPU P2zzr) — lot 2 cu oracolul, apoi lot 6 cu paza termică. Prag de reușită: lot 6 ≥ 18 000 simb/s.
2. **Date reale pe stick + oracol la lot 6** (E1) — fără asta viteza nu antrenează nimic util. Mic ca muncă, mare ca valoare.
3. **Înmulțirea „v8” cu tehnicile Ampere** (F2): `ldmatrix` peste tot, memoria comună dublă / triplă cu `cp.async`, bloc 128×128. Țintă: ≥ 28 TFLOP/s pe qkv-513, aceiași biți.
4. **Atenția înainte pe circuitele speciale** (F3), stil „flash”: o trecere, fără matricea întreagă în memorie.
5. **Lipirea lansărilor mărunte** (F4): GELU + bias în înmulțire, Adam + norma într-o singură trecere, sumele pe coloane lipite.
6. **Mai multe rânduri într-o pornire** (F5) și **oglindă de pachete pentru CI** (E5) — mai multe măsurători pe zi.
7. **Comparația la scris, cinstită** (E8): Windows cu memoria de context și bf16, apoi noi cu aceeași rețetă.

Fiecare pas: măsurătoare înainte, schimbare, aceeași măsurătoare după, notă în hub; dacă o dată nouă schimbă diagnosticul, planul se rescrie.

## 7. Jurnalul analizei
- 27 nov 18:32 — os-495: scrisul dintr-o lansare (token32_v2c) 1 676 µs pe placă față de 1 067 la listă; 88 de operații măsurate cu ceasul (cost 0,6 %). Scrisul rămâne mai bun pe listă; F-scris = barierele dintre operații (de confirmat din zona ceasului).
- 27 nov 18:15 — ciorna 1 (date: profilul pasului record 08:24, os-485/486/489/490, stările din hub, foaia NVIDIA GA104).
