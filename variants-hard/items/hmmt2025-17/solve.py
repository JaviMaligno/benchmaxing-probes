# hmmt2025-17 variant: 3 copies of each of n letters; for distinct x1,x2 the number of x2's
# between 1st and 2nd x1 equals number between 2nd and 3rd x1.
# Brute-force small n (backtracking with prefix pruning), confirm closed form n! * 2^(n-1),
# then evaluate for original n=26 and variant n=24.
from math import factorial
import sympy as sp

def brute(n):
    cnt=[0]*n; seq=[]; total=0
    def ok_full(s):
        pos=[[] for _ in range(n)]
        for i,c in enumerate(s): pos[c].append(i)
        for a in range(n):
            p=pos[a]
            for b in range(n):
                if a==b: continue
                g1=sum(1 for i in range(p[0]+1,p[1]) if s[i]==b)
                g2=sum(1 for i in range(p[1]+1,p[2]) if s[i]==b)
                if g1!=g2: return False
        return True
    def prune(s):
        # once a letter's 3rd copy is placed, its two gaps are fixed: check them now
        c=s[-1]
        if s.count(c)!=3: return True
        p=[i for i,x in enumerate(s) if x==c]
        for b in range(n):
            if b==c: continue
            g1=sum(1 for i in range(p[0]+1,p[1]) if s[i]==b)
            g2=sum(1 for i in range(p[1]+1,p[2]) if s[i]==b)
            if g1!=g2: return False
        return True
    def rec():
        nonlocal total
        if len(seq)==3*n:
            if ok_full(seq): total+=1
            return
        for c in range(n):
            if cnt[c]<3:
                cnt[c]+=1; seq.append(c)
                if prune(seq): rec()
                seq.pop(); cnt[c]-=1
    rec(); return total

formula=lambda n: factorial(n)*2**(n-1)
for n in range(1,6):
    b=brute(n); print(f"n={n}: brute={b}, formula={formula(n)}", "OK" if b==formula(n) else "MISMATCH")
    assert b==formula(n)

orig=formula(26)
assert orig==sp.factorial(26)*2**25
print("original (n=26):", orig, "== 2^25*26! :", orig==sp.factorial(26)*2**25)
var=formula(24)
print("variant (n=24):", var, "== 2^23*24! :", var==sp.factorial(24)*2**23)
