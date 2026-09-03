import mpmath as mp
mp.mp.dps=25
from sympy.ntheory.residue_ntheory import jacobi_symbol
from math import gcd
def K(d,n):
    if n<=0: return 0
    m=n; e=0
    while m%2==0: m//=2; e+=1
    r=1
    if e:
        s={1:1,7:1,3:-1,5:-1}.get(d%8,0); r*= s**e
    if m==1: return r
    if gcd(d,m)!=1: return 0
    return r*jacobi_symbol(d%m,m)
def L(d,s):
    q=abs(d); return q**(-s)*mp.fsum([K(d,a)*mp.zeta(s,mp.mpf(a)/q) for a in range(1,q+1)])
A=lambda s: mp.zeta(s)*L(-15,s)
B=lambda s: L(-3,s)*L(5,s)
def wind(F,c,r,n=240):
    tot=mp.mpf(0); prev=None
    for k in range(n+1):
        p=c+r*mp.exp(2j*mp.pi*k/n); a=mp.arg(F(p))
        if prev is not None:
            d=a-prev
            while d>mp.pi: d-=2*mp.pi
            while d<-mp.pi: d+=2*mp.pi
            tot+=d
        prev=a
    return tot/(2*mp.pi)
F1=lambda s: A(s)+B(s)
for c in [mp.mpc('0.80001','12.03860'), mp.mpc('0.92746','15.49663'), mp.mpc('0.70074','84.76354')]:
    print("Z_Q0 center",mp.nstr(c,8),"  winding(r=0.05) =",mp.nstr(wind(F1,c,mp.mpf('0.05')),6),
          "  |F| at center =",mp.nstr(abs(F1(c)),4))
