import numpy as np, sys
from sympy.ntheory.residue_ntheory import jacobi_symbol
from math import gcd
from scipy.special import bernoulli
NB=10; B2k=bernoulli(2*NB)[::2][1:]; NCUT=400
_LOG={}
def hz(s,a):
    key=a
    if key not in _LOG: _LOG[key]=np.log(np.arange(NCUT)+a)
    lg=_LOG[key]
    tot=np.exp(np.multiply.outer(-s,lg)).sum(axis=-1)
    N=NCUT+a; lN=np.log(N)
    tot+=np.exp((1-s)*lN)/(s-1)+0.5*np.exp(-s*lN)
    for j in range(1,NB):
        p=np.ones_like(s)
        for i in range(2*j-1): p=p*(s+i)
        f=1.0
        for i in range(1,2*j+1): f*=i
        tot+=B2k[j-1]/f*p*np.exp((-s-2*j+1)*lN)
    return tot
def K(d,n):
    if n<=0: return 0
    m,e=n,0
    while m%2==0: m//=2; e+=1
    r=1
    if e: r*={1:1,7:1,3:-1,5:-1}.get(d%8,0)**e
    if m==1: return r
    if gcd(d,m)!=1: return 0
    return r*jacobi_symbol(d%m,m)
def Ld(d,s):
    q=abs(d); return np.exp(-s*np.log(q))*sum(K(d,a)*hz(s,a/q) for a in range(1,q+1) if K(d,a))
A=lambda s: hz(s,1.0)*Ld(-15,s)
B=lambda s: Ld(-3,s)*Ld(5,s)
gate=np.array([0.8000109882+12.03859863j,0.9274608808+15.49663407j,0.700741448+84.76353854j])
g=np.abs(A(gate)+B(gate))
print("GATE |A+B| at 2 certified zeros + 1 known non-zero:",g,flush=True)
if not (g[0]<1e-6 and g[1]<1e-6 and g[2]>1.0):
    print("GATE FAILED -> census discarded"); sys.exit(1)
print("GATE PASSED",flush=True)
def wind(F,x0,x1,y0,y1,n):
    b=np.concatenate([x0+(x1-x0)*np.arange(n)/n+1j*y0, x1+1j*(y0+(y1-y0)*np.arange(n)/n),
                      x1-(x1-x0)*np.arange(n)/n+1j*y1, x0+1j*(y1-(y1-y0)*np.arange(n)/n)])
    b=np.concatenate([b,b[:1]]); d=np.diff(np.angle(F(b)))
    return ((d+np.pi)%(2*np.pi)-np.pi).sum()/(2*np.pi)
for lam,name in [(1,"Z_Q0=A+B principal"),(-1,"Z_Q1=A-B non-principal")]:
    F=lambda s,lam=lam: A(s)+lam*B(s); tot=0; rows=[]
    for j in range(8):
        y0,y1=(0.05 if j==0 else j*5.0),(j+1)*5.0
        c=wind(F,0.5+0.002,4.0,y0,y1,9000); tot+=int(round(c)); rows.append((y0,y1,c))
    print(f"\n{name}: {tot} zeros with sigma>0.502, 0<t<40",flush=True)
    for y0,y1,c in rows:
        if abs(c)>0.1: print("   t in [%5.2f,%5.2f]: %d (raw %.5f)"%(y0,y1,int(round(c)),c))
