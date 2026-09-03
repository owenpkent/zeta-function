import numpy as np, mpmath as mp, importlib.util
spec=importlib.util.spec_from_file_location("f","/tmp/claude-1000/-home-owen-dev-zeta-function/e54d8a47-d42d-42f1-813a-bf70a9ea50b5/scratchpad/fast.py")
# avoid running the census: re-implement hurwitz here with tunable NCUT
from scipy.special import bernoulli
NB=12; B2k=bernoulli(2*NB)[::2][1:]
def hurwitz(s,a,NCUT):
    s=np.asarray(s,dtype=np.complex128); tot=np.zeros_like(s)
    for k in range(NCUT): tot += (k+a)**(-s)
    N=NCUT+a
    tot += N**(1-s)/(s-1) - 0.5*N**(-s)
    for j in range(1,NB):
        poch=np.ones_like(s)
        for i in range(2*j-1): poch=poch*(s+i)
        fact=1.0
        for i in range(1,2*j+1): fact*=i
        tot += B2k[j-1]/fact*poch*N**(-s-2*j+1)
    return tot
mp.mp.dps=30
for (sg,t) in [(0.8,12.0),(0.93,15.5),(0.7,84.8),(0.6,199.0)]:
    s=complex(sg,t)
    for a in [1.0, 2/15, 7/15]:
        ref=complex(mp.zeta(mp.mpc(sg,t), mp.mpf(a)))
        for NC in (60,300,600):
            v=hurwitz(np.array([s]),a,NC)[0]
            print(f"s={sg}+{t}i a={a:.4f} NCUT={NC:4d}  err={abs(v-ref):.3e}")
    print()
