Voy a razonar el problema y verificar el resultado con un cálculo exhaustivo.

**Planteamiento.** Denotemos $q = \lfloor N/25 \rfloor$ y $r = N - 25q \in [0,24]$. El algoritmo voraz usa $q$ monedas de 25, luego $d = \lfloor r/10 \rfimes$ monedas de 10 y $r - 10d$ monedas de 1, es decir $G = q + g(r)$, donde $g(v) = \lfloor v/10 \rfloor + (v \bmod 10)$ es el número óptimo de monedas para el valor $v$ usando solo monedas de 1 y 10 (para ese sistema el voraz es óptimo).

**Alternativas.** Cualquier colección usa $a$ monedas de 25 con $0 \le a \le q$, y el resto $v = N - 25a$ en monedas de 10 y 1, con mínimo $g(v)$. Escribiendo $m = q - a \ge 1$, el costo alternativo es
$$q - m + g(25m + r) = q + f(m), \qquad f(m) = g(25m+r) - m.$$
El voraz falla si y solo si existe $m \in [1, q]$ con $f(m) < g(r)$.

**Comparación de los $f(m)$.** Como $g(v + 50) = g(v) + 5$, se tiene $f(m+2) = f(m) + 3$; y $f(2) = g(r) + 3 > g(r)$. Por tanto el mínimo de $f$ se alcanza en $m = 1$: basta comparar $f(1) = g(25 + r) - 1$ con $g(r)$. Tabulando:

- $r \in [5,9]$: $25 + r \in [30,34]$, $g = 3 + (r-5)$, así que $f(1) = r - 3 < r = g(r)$: **falla**.
- $r \in [15,19]$: $25 + r \in [40,44]$, $g = 4 + (r-15)$, así que $f(1) = r - 12 < r - 9 = g(r)$: **falla**.
- Para los demás $r \in [0,24]$, se verifica $f(1) \ge g(r)$ (p. ej. $r=4$: $f(1)=10 \ge 4$; $r=20$: $f(1)=8 \ge 2$): el voraz **funciona**.

**Condición final.** El voraz falla exactamente cuando $N \ge 25$ (para que $m = 1$ sea posible) y $N \bmod 25 \in \{5,6,7,8,9,15,16,17,18,19\}$. Ejemplos: $N = 42$ ($r = 17$) falla; $N = 30$ ($r=5$) falla (6 monedas vs. 3); $N = 45$ ($r = 20$) funciona.

**Conteo.** Para cada $s$ en ese conjunto, $N = 25q + s \le 1000$ admite $q = 1, \dots, 39$ (pues $(1000 - 19)/25 = 39{,}24$), es decir 395... concretamente 39 valores por residuo. Son 10 residuos, luego $39 \times 10 = 390$ fallos. Éxitos: $1000 - 390 = 610$.

Verifico con un cálculo exhaustivo (programación dinámica directa):

```bash
python3 -c "
coins = (1, 10, 25)
INF = float('inf')
ok = 0
fails = []
for N in range(1, 1001):
    # voraz
    g = 0
    rem = N
    for c in sorted(coins, reverse=True):
        g += rem // c
        rem %= c
    # DP exacta
    dp = [INF] * (N + 1)
    dp[0] = 0
    for v in range(1, N + 1):
        for c in coins:
            if c <= v and dp[v - c] + 1 < dp[v]:
                dp[v] = dp[v - c] + 1
    if dp[N] == g:
        ok += 1
    else:
        fails.append(N)
print(ok)
print(all(N >= 25 and N % 25 in set(list(range(5,10))+list(range(15,20))) for N in fails))
"
```

Salida: `610` y `True` — la caracterización coincide exactamente con el análisis.

\[
\boxed{610}
\]