from sympy.ntheory.residue_ntheory import jacobi_symbol
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
    from math import gcd
    if gcd(d,m)!=1: return 0
    return r*jacobi_symbol(d%m,m)
import itertools
N=200
def chi(d,n):
    return K(d,n)
# r_Q for Q0 = x^2+xy+4y^2 and Q1 = 2x^2+xy+2y^2, disc -15
def rQ(a,b,c,N):
    r=[0]*(N+1)
    for x in range(-60,61):
        for y in range(-60,61):
            v=a*x*x+b*x*y+c*y*y
            if 1<=v<=N: r[v]+=1
    return r
r0=rQ(1,1,4,N); r1=rQ(2,1,2,N)
aA=[0]*(N+1); aB=[0]*(N+1)
for n in range(1,N+1):
    aA[n]=sum(int(chi(-15,m)) for m in range(1,n+1) if n%m==0)
    aB[n]=sum(int(chi(-3,d))*int(chi(5,n//d)) for d in range(1,n+1) if n%d==0)
bad=[n for n in range(1,N+1) if r0[n]!=aA[n]+aB[n]]
bad1=[n for n in range(1,N+1) if r1[n]!=aA[n]-aB[n]]
print("r0 vs A+B mismatches:",bad[:10], "count",len(bad))
print("r1 vs A-B mismatches:",bad1[:10],"count",len(bad1))
print("r0(1,2,4)=",r0[1],r0[2],r0[4]," A+B:",aA[1]+aB[1],aA[2]+aB[2],aA[4]+aB[4])
