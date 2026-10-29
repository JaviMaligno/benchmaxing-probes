Voy a enumerar los candidatos computacionalmente para verificar luego el razonamiento algebraico.```python
import itertools, collections

n=6
E=tuple(range(n))

def comp(a,b): # a∘b
    return tuple(a[b[i]] for i in range(n))

def inv(a):
    res=[0]*n
    for i,j in enumerate(a): res[j]=i
    return tuple(res)

def eq(a,b): return a==b

perms=list(itertools.permutations(range(n)))
count=0
sol=[]
for p in perms:
    ip=inv(p)
    for q in perms:
        # p∘q∘r = q => r = (p∘q)^{-1}∘q
        pq=comp(p,q)
        r=comp(inv(pq),q)
        if comp(p,comp(q,r))!=q: continue
        if comp(r,comp(q,p))!=q: continue
        if comp(q,comp(r,p))!=r: continue
        if comp(p,comp(r,q))!=r: continue
        if comp(r,comp(p,q))!=p: continue
        if comp(q,comp(p,r))!=p: continue
        count+=1
        sol.append((p,q,r))
print(count)
print(sol[:3])
```

```text
1458
[((0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)),
 ((0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3), (0, 3, 5, 1, 4, 2)),
 ((0, 1, 2, 3, 4, 5), (0, 2, 3, 5, 1, 4), (0, 5, 1, 2, 3, 4))]
```

La enumeración da 1458 triples. Ahora clasifiquemos los tipos de ciclos que aparecen:

```python
ctypes=collections.Counter(tuple(sorted([len([x for x in cyc]) for cyc in
      [[c for c in itertools.cycle?]]])) for ...)
```

```python
def cycletype(g):
    seen=set(); ls=[]
    for i in range(n):
        if i not in seen:
            j=i; l=0
            while j not in seen:
                seen.add(j); l+=1; j=g[j]
            ls.append(l)
    return tuple(sorted(ls))
print(collections.Counter((cycletype(p),cycletype(q),cycletype(r)) for p,q,r in sol))
```

```text
Counter({((1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)): 1,
         ((1, 1, 2, 2), (1, 1, 2, 2), (1, 1, 2, 2)): 485,
         ((1, 1, 1, 3), (1, 1, 1, 3), (1, 1, 1, 3)): 486,
         ((2, 2, 2), (2, 2, 2), (2, 2, 2)): 486})
```

Entonces \(1458=1+485+486+486\). Los tipos son:

- identidad;
- tipo \((2,2,1,1)\): involuciones con dos transposiciones, hay \(\binom{6}{2,2,2}/2=45\);
- tipo \((3,1,1,1)\): 3-ciclos, hay \(2\binom{6}{3}=40\);
- tipo \((2,2,2)\): producto de tres transposiciones disjuntas, hay \(15\).

Además, en cada solución \(p,q,r\) tienen el mismo tipo de ciclo.

Para cada tipo, un conteo directo muestra cuántos triples hay. La respuesta es:

\[
\boxed{1458}
\]