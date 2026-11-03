"""Model (NU măsurătoare) pentru Kronos #477 pe RTX 3070 Ti: cât contează „clopoțelul” (lansarea fiecărui calcul) pe placă.
Date fixe: memoria plăcii 608 GB/s (specificația NVIDIA); la fiecare simbol se citesc ~105 MB de greutăți (Q8_0, ca în OS); 63 de calcule mari / simbol.
Calculul e limitat de citirea memoriei, deci timpul unui calcul = octeți / (608 GB/s × eficiență). Fiecare variantă are un interval jos–sus."""
BW = 608e9
OCTETI = 105e6
CALC = 63

def simb_pe_s(lansari, cost_lansare, eficienta):
    timp = OCTETI / (BW * eficienta) + lansari * cost_lansare
    return 1 / timp

variante = [
    # nume,                                          lansări/simbol, cost lansare (jos, sus) s, eficiență memorie (jos, sus)
    ("Windows + PyTorch, câte un program pe calcul",    150, (6e-6, 10e-6), (0.35, 0.50)),
    ("driverul nostru, câte un program pe calcul",       63, (3e-6,  5e-6), (0.40, 0.55)),
    ("driverul nostru, UN SINGUR program (contor)",      63, (1e-6,  2e-6), (0.45, 0.60)),
    ("un singur program + citește din timp calculul următor", 63, (1e-6, 2e-6), (0.60, 0.75)),
]
print(f"Limita teoretică (doar citirea memoriei, fără nicio pierdere): {BW/OCTETI:.0f} simb/s")
print(f"Pe procesor: azi 125 simb/s; ținta C-59 în model ~265–305\n")
for nume, n, (cj, cs), (ej, es) in variante:
    jos, sus = simb_pe_s(n, cs, ej), simb_pe_s(n, cj, es)
    pierdut = n * (cj + cs) / 2 / (OCTETI / (BW * (ej + es) / 2) + n * (cj + cs) / 2) * 100
    print(f"{nume:56s} {jos:5.0f} – {sus:5.0f} simb/s   (clopoțelul ia ~{pierdut:.0f} % din timp)")
