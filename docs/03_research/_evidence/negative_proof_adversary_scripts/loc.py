import numpy as np, mpmath as mp
exec(open('fast2.py').read().split('gate=np.array')[0])
def wind(F,x0,x1,y0,y1,n=1400):
    b=np.concatenate([x0+(x1-x0)*np.arange(n)/n+1j*y0, x1+1j*(y0+(y1-y0)*np.arange(n)/n),
                      x1-(x1-x0)*np.arange(n)/n+1j*y1, x0+1j*(y1-(y1-y0)*np.arange(n)/n)])
    b=np.concatenate([b,b[:1]]); d=np.diff(np.angle(F(b)))
    return int(round(((d+np.pi)%(2*np.pi)-np.pi).sum()/(2*np.pi)))
def localize(F,x0,x1,y0,y1):
    for _ in range(46):
        if (x1-x0)>(y1-y0):
            xm=(x0+x1)/2
            if wind(F,x0,xm,y0,y1)==1: x1=xm
            else: x0=xm
        else:
            ym=(y0+y1)/2
            if wind(F,x0,x1,y0,ym)==1: y1=ym
            else: y0=ym
    return (x0+x1)/2,(y0+y1)/2
mp.mp.dps=30
from sympy.ntheory.residue_ntheory import jacobi_symbol
from math import gcd
def Km(d,n):
    if n<=0: return 0
    m,e=n,0
    while m%2==0: m//=2; e+=1
    r=1
    if e: r*={1:1,7:1,3:-1,5:-1}.get(d%8,0)**e
    if m==1: return r
    if gcd(d,m)!=1: return 0
    return r*jacobi_symbol(d%m,m)
def Lm(d,s):
    q=abs(d); return q**(-s)*mp.fsum([Km(d,a)*mp.zeta(s,mp.mpf(a)/q) for a in range(1,q+1)])
Am=lambda s: mp.zeta(s)*Lm(-15,s); Bm=lambda s: Lm(-3,s)*Lm(5,s)
bands={1:[(10,15),(15,20),(20,25),(30,35)], -1:[(20,25)]}
names={1:"Z_Q0 = A+B  principal   x^2+xy+4y^2", -1:"Z_Q1 = A-B  non-princ  2x^2+xy+2y^2"}
for lam in (1,-1):
    F=lambda s,lam=lam: A(s)+lam*B(s)
    Fm=lambda s,lam=lam: Am(s)+lam*Bm(s)
    print("\n"+names[lam],flush=True)
    for (y0,y1) in bands[lam]:
        sg,t=localize(F,0.502,4.0,float(y0),float(y1))
        v=Fm(mp.mpc(sg,t))
        print("   rho = %.10f + %.10f i     mpmath |Z_Q(rho)| = %s"%(sg,t,mp.nstr(abs(v),3)),flush=True)
