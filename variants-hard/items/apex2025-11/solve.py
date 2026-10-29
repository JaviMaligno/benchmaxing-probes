import sys
from itertools import combinations
def canon(st):
    m={};out=[]
    for e in st:
        if isinstance(e,tuple):
            if e[1] not in m: m[e[1]]=len(m)
            out.append((1,m[e[1]]))
        else: out.append(e)
    return tuple(out)
def f(n,k):
    # vertices 0..n-1, edges (a,b) with 0<b-a<=k ; max weight Hamiltonian cycle
    states={tuple([0]*k):0}; best=None
    for v in range(n):
        new={}
        for st,val in states.items():
            e0=st[0]; rest=list(st[1:])+[0]
            d0=0 if e0==0 else (2 if e0==2 else 1)
            need=2-d0
            cand=[j for j in range(k) if v+1+j<n and rest[j]!=2]
            for S in combinations(cand,need):
                r=list(rest); w=val; closed=False; ok=True
                # endpoints: v's fragment label
                lab = e0[1] if d0==1 else ('new',v)
                if d0==0 and need==0: continue
                # v acts as an open end with label lab (if d0==0, v is fresh: first edge creates fragment)
                vend_count = 1 if d0==1 else 0
                cur=lab
                for j in S:
                    w+=j+1
                    t=r[j]
                    if d0==0 and vend_count==0:
                        # first edge from fresh v: v-w joins
                        vend_count=1
                        if t==0: r[j]=(1,cur)  # fragment cur has ends v and w
                        else:
                            # w end of fragment t[1]; merge: v becomes end of that fragment
                            r[j]=2; cur=t[1]
                        continue
                    # v is an end of fragment cur; connect to w
                    if t==0:
                        r[j]=(1,cur)
                    elif t[1]==cur:
                        r[j]=2; closed=True
                    else:
                        other=t[1]; r[j]=2
                        r=[(1,cur) if (isinstance(x,tuple) and x[1]==other) else x for x in r]
                if closed:
                    if all(x==2 or (v+1+i>=n and x==0) for i,x in enumerate(r)) and all(x==2 for i,x in enumerate(r) if v+1+i<n):
                        if best is None or w>best: best=w
                    continue
                # if v was fresh (d0==0) with need 2 and both formed: fine. if fresh and first edge made w end of cur, second edge handled above.
                ns=canon(r)
                if ns not in new or new[ns]<w: new[ns]=w
        states=new
    return best
from functools import lru_cache
from fractions import Fraction
def brute(n,k):
    full=(1<<n)-1
    @lru_cache(None)
    def go(mask,pos):
        if mask==full: return pos if pos<=k else None
        best=None
        for d in range(-k,k+1):
            q=pos+d
            if d and 0<=q<n and not mask>>q&1:
                r=go(mask|1<<q,q)
                if r is not None and (best is None or r+abs(d)>best): best=r+abs(d)
        return best
    return go(1,0)
def limit(k,N,bfmax):
    vals={n:f(n,k) for n in range(k+2,N+1)}
    for n in range(k+2,bfmax+1):
        assert vals[n]==brute(n,k),(k,n)
    tail=list(range(N//2,N+1))
    for p in range(1,N//4):
        diffs={vals[n]-vals[n-p] for n in tail}
        if len(diffs)==1:
            return Fraction(diffs.pop(),p),p
    return None
lo,po=limit(3,80,16); print("original (jump<=3): limit =",lo,"period",po); assert lo==Fraction(14,5)
lv,pv=limit(5,90,14); print("variant  (jump<=5): limit =",lv,"period",pv, float(lv))
