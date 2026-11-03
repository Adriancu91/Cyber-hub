"""Model: 36 / 35 / 34 fire lucrătoare; 1–2 fire lăsate libere pentru treburile calculatorului (ceas, rețea, ecran, USB).
Bloc mare + ajutor la cel lent (bucăți fine, 32 pe fir), cu și fără „copia de rezervă". Aceeași calibrare ca simulare_bucatele.py."""
import heapq, numpy as np
rng=np.random.default_rng(3)
IP={"H1":(0.10,0.004,60e-6),"H2":(0.28,0.012,150e-6)}
MUNCA=3.0e-3/63*36          # fir-secunde pe calcul
def calcul(n, sig, p, L, buc):
    b=MUNCA/buc; liber=[0.0]*n; pb=1-(1-p)**(n/buc)
    d=0.01e-6+b*rng.lognormal(0,sig,buc)+(rng.random(buc)<pb)*L
    for x in d: heapq.heapreplace(liber, liber[0]+x)
    return max(liber)+0.5e-6
def viteza(n, ip, liber, copie, simb=15):
    sig,p,L=IP[ip]; p=p*(0.15 if liber else 1.0); buc=n*32
    if copie: L=min(L,3*MUNCA/buc)
    return simb/sum(calcul(n,sig,p,L,buc) for _ in range(simb*63))
print(f"{'lucrători':24s} {'fără copie H1':>13s} {'H2':>5s}  {'cu copie H1':>11s} {'H2':>5s}")
for n,lib in ((36,0),(35,1),(34,2)):
    r=[round(viteza(n,ip,lib,c)) for c in (False,True) for ip in ("H1","H2")]
    print(f"{str(n)+' lucr.'+(f', {lib} liber' if lib else ' (azi)'):24s} {r[0]:13d} {r[1]:5d}  {r[2]:11d} {r[3]:5d}")
