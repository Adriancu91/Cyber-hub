# Simulare: Kronos #477 pe RTX 3070 Ti — clopoțelul pe placă (3 nov 2026, cerut de Adrian)

MODEL simplu (`simulare_gpu.py` → `rezultat.txt`), NU măsurătoare. Placa: 608 GB/s; la fiecare simbol se citesc ~105 MB de greutăți; 63 de calcule.
Limita teoretică: ~5.800 simb/s.

| varianta | simb/s (model) | cât ia clopoțelul |
|---|---|---|
| Windows + PyTorch, câte un program pe calcul | 500–800 | ~75 % |
| driverul nostru, câte un program pe calcul | 1.340–1.990 | ~41 % |
| **driverul nostru, un singur program pe simbol (contor în memoria plăcii)** | **1.960–2.850** | ~22 % |
| un singur program + citește din timp calculul următor | 2.420–3.410 | ~27 % |

**Realitatea măsurată (Kronos, S49/S50 CCM, Windows + PyTorch, placa fp32): 52 simb/s.** De 10× sub model, pentru că pe Windows se mai pierde timp
în Python la fiecare simbol (bucla, eșantionarea, copierile) — tot „clopoțel”, doar mai mare. Deci modelul e optimist în cifre absolute,
dar ordinea variantelor e aceeași: cu cât sunt mai puține opriri, cu atât mai repede. Cifrele reale vin abia la primul calcul pe placă (după I6–I10).
