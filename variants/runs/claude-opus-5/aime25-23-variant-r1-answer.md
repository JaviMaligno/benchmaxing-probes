
<invoke name="Bash">
<parameter name="command">cd /tmp && python3 -I -c "
INF=float('inf')
best=[0]+[INF]*1000
for n in range(1,1001):
    for c in (1,10,24):
        if n>=c and best[n-c]+1<best[n]: best[n]=best[n-c]+1
def greedy(n):
    k=0
    for c in (24,10,1):
        k+=n//c; n%=c
    return k
fails=[n for n in range(1,1001) if greedy(n)>best[n]]
print(1000-len(fails), len(fails))
print(fails[:40])
"</parameter>
</invoke>


Beräknat resultat: 610 390
[6, 7, 8, 9, 16, 17, 18, 19, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 78, 79, 80, 79, 80, 81, 82, 83, 84, 85, 86, 87]

El resultado anterior salió con la lista de fallos duplicando valores (imposible al generarse desde un `range`), así que lo verifico de nuevo de forma independiente.


<invoke name="Bash">
<parameter name="command">cd /tmp && python3 -I << 'EOF'
from functools import lru_cache
INF = 10**9
best = [0] + [INF]*1000
for n in range(1, 1001):
    best[n] = min(best[n-c] + 1 for c in (1,10,24) if n >= c)

def greedy(n):
    k = 0
    for c in (24,10,1):
        q, n = divmod(n, c)
        k += q
    return k

ok = [n for n in range(1,1001) if greedy(n) == best[n]]
fail = [n for n in range(1,1001) if greedy(n) > best[n]]
assert len(ok) + len(fail) == 1000
assert len(set(fail)) == len(fail)
print("exito:", len(ok))
print("fallo:", len(fail))
print("primeros fallos:", fail[:30])
# chequeo cruzado: fuerza bruta directa para n<=300
def brute(n):
    m = INF
    for a in range(n//24+1):
        r1 = n - 24*a
        for b in range(r1//10+1):
            m = min(m, a + b + (r1 - 10*b))
    return m
assert all(brute(n) == best[n] for n in range(1,301))
print("verificacion fuerza bruta OK")
EOF</parameter>
</invoke>


exito: 610 **ERROR**: 390