import mpmath as mp
mp.mp.dps=40
from sympy.ntheory.residue_ntheory import jacobi_symbol
from math import gcd
def K(d,n):
    if n<=0: return 0
    m=n; e=0
    while m%2==0: m//=2; e+=1
    r=1
    if e:
        dm8=d%8
        s=1 if dm8 in (1,7) else (-1 if dm8 in (3,5) else 0)
        r*= s**e
    if m==1: return r
    if gcd(d,m)!=1: return 0
    return r*jacobi_symbol(d%m,m)
def L(d,s):
    q=abs(d)
    return q**(-s)*mp.fsum([K(d,a)*mp.zeta(s,mp.mpf(a)/q) for a in range(1,q+1)])
def A(s): return mp.zeta(s)*L(-15,s)
def B(s): return L(-3,s)*L(5,s)
def f(lam,s): return A(s)+lam*B(s)
# sanity: Dirichlet coefficients
print("L(-3,2)=",mp.nstr(L(-3,mp.mpf(2)),12),"  ref sum 1-1/4+1/16-... :",mp.nstr(mp.nsum(lambda n: K(-3,int(n))/mp.mpf(n)**2,[1,mp.inf]),12))
pts=[mp.mpf('0.8000109882')+1j*mp.mpf('12.03859863'),
     mp.mpf('0.9274608808')+1j*mp.mpf('15.49663407'),
     mp.mpf('0.700741448')+1j*mp.mpf('84.76353854')]
for s in pts:
    print("s=",mp.nstr(s,10)," A+B =",mp.nstr(f(1,s),8)," |A|=",mp.nstr(abs(A(s)),6)," |B|=",mp.nstr(abs(B(s)),6))
