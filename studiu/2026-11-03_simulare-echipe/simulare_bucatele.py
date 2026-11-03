"""Simulare (model) pentru a doua idee a lui Adrian: tot calculul e un „bloc”; fiecare fir își ia o bucățică mică, iar când o termină își ia
alta din ce a rămas (cine e rapid face mai multe bucăți, nimeni nu stă după cel lent). Același model și aceeași calibrare ca simulare.py."""
import heapq, numpy as np
rng = np.random.default_rng(2)
N, CALCULE, SIMB = 36, 63, 300
W = 3.0e-3 / CALCULE
IP = {"H1": (0.10, 0.004, 60e-6, 1.50e-6, 0.30e-6), "H2": (0.28, 0.012, 150e-6, 0.30e-6, 0.10e-6)}

def un_calcul(ip, bucati, treji, luare=0.15e-6, echipe=0):
    sigma, p_int, L, trez_fir, adun_fir = IP[ip]
    munca = W * N                                   # toată munca unui calcul (fir-secunde)
    b = munca / bucati
    if bucati == N:                                  # azi: fiecare fir are fix bucata lui
        t = W * rng.lognormal(0, sigma, N) + (rng.random(N) < p_int) * L
        sfarsit = t.max()
    else:                                            # bucățele: următorul fir liber ia următoarea bucată
        liber = [0.0] * N; heapq.heapify(liber)
        p_buc = 1 - (1 - p_int) ** (1 / (bucati / N))   # aceeași șansă de întrerupere pe fir, împărțită pe bucăți
        for _ in range(bucati):
            t0 = heapq.heappop(liber)
            d = luare + b * rng.lognormal(0, sigma) + (rng.random() < p_buc) * L
            heapq.heappush(liber, t0 + d)
        sfarsit = max(liber)
    if echipe:                                       # clopoțel în 2 trepte (echipe de `echipe` fire)
        k = N // echipe
        return sfarsit + adun_fir * (echipe + k) + (0 if treji else trez_fir * ((echipe - 1) + (k - 1)))
    return sfarsit + adun_fir * N + (0 if treji else trez_fir * (N - 1))

def viteza(ip, bucati, treji=False, echipe=0):
    return SIMB / sum(un_calcul(ip, bucati, treji, echipe=echipe) for _ in range(SIMB * CALCULE))

print(f"{'varianta':42s} {'H1':>5s} {'H2':>5s}")
for nume, buc, tr in [("azi (o bucată fixă pe fir)", 36, False),
                      ("bucățele: 72 (2 pe fir)", 72, False),
                      ("bucățele: 144 (4 pe fir)", 144, False),
                      ("bucățele: 288 (8 pe fir)", 288, False),
                      ("bucățele 144 + fire treze", 144, True),
                      ("bucățele 288 + fire treze", 288, True)]:
    print(f"{nume:42s} {viteza('H1', buc, tr):5.0f} {viteza('H2', buc, tr):5.0f}")
for e in (4, 6):
    print(f"{f'bucățele 288 + treji + echipe {36//e}x{e}':42s} {viteza('H1', 288, True, e):5.0f} {viteza('H2', 288, True, e):5.0f}")
