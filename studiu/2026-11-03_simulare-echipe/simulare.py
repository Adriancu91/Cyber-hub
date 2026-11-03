"""Simulare (model, NU măsurătoare) pentru ideea lui Adrian: 36 fire = 9 echipe x 4.
Calibrat pe profilul real os-214 din 3 nov: 8,2 ms/simbol, 63 calcule, ~37 % calcul, ~63 % așteptare.
Două ipoteze despre de unde vine așteptarea (nu știm încă proporția; C-59 o va măsura):
  H1 = mai ales „clopoțelul” (trezirea și adunarea firelor), H2 = mai ales firul cel mai lent.
"""
import numpy as np
rng = np.random.default_rng(1)
N, CALCULE, SIMB = 36, 63, 400
W = 3.0e-3 / CALCULE            # timp de calcul pe un calcul (perete), s — 37 % din 8,2 ms

def ruleaza(ip, marime=4, echipe=False, treji=False, unite=False, raft=False, ajutor=False):
    # parametrii ipotezei (calibrați ca varianta de azi să dea ~8,2 ms/simbol)
    sigma, p_int, L, trezire_fir, adunare_fir = {
        "H1": (0.10, 0.004, 60e-6, 1.50e-6, 0.30e-6),
        "H2": (0.28, 0.012, 150e-6, 0.30e-6, 0.10e-6),
    }[ip]
    calc = CALCULE - (12 if unite else 0)          # Q/K/V + atenția unite per strat
    w = W * CALCULE / calc * (0.88 if raft else 1.0)  # felii fixe: date mai aproape (~-12 %)
    timp = 0.0
    for _ in range(SIMB * calc):
        t = w * rng.lognormal(0, sigma, N)
        t += (rng.random(N) < p_int) * L             # întreruperi ocazionale
        if ajutor:                                   # cine termină ajută la bucata celui lent
            t = np.minimum(t, np.mean(t) * 1.15)
        lent = t.max()
        if echipe:
            k = N // marime
            adun = adunare_fir * (marime + k); trez = 0 if treji else trezire_fir * ((marime - 1) + (k - 1))
        else:
            adun = adunare_fir * N;       trez = 0 if treji else trezire_fir * (N - 1)
        timp += lent + adun + trez
    return SIMB / timp

variante = [
    ("echipe", dict(echipe=True)),
    ("echipe + fire treze", dict(echipe=True, treji=True)),
    ("tot pachetul", dict(echipe=True, treji=True, unite=True, raft=True, ajutor=True)),
]
print(f"azi (36 deodată): H1 {ruleaza('H1'):.0f}, H2 {ruleaza('H2'):.0f} simb/s")
for marime in (4, 6):
    print(f"--- {36//marime} echipe x {marime} fire ---")
    for nume, k in variante:
        print(f"{nume:24s} H1 {ruleaza('H1', marime, **k):5.0f}   H2 {ruleaza('H2', marime, **k):5.0f}")
