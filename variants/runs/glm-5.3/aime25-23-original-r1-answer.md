Voy a resolver el problema analíticamente y luego verificar con un cálculo.

**Análisis:** Sea $N = 25q + r$ con $0 \le r < 25$, y escribamos $r = 10a + b$ con $0 \le b < 10$. El algoritmo voraz usa $g(N) = q + a + b$ monedas.

Cualquier otra colección usa $q' \le q$ monedas de 25 (no puede usar más). Si quitamos una moneda de 25, hay que representar $r + 25 = 10(a+2) + (b+5)$ con monedas de 10 y 1:
- Si $b < 5$: cuesta $a + 2 + b$ monedas, total $q + a + b + 1 > g(N)$ — el voraz gana.
- Si $b \ge 5$: cuesta $a + 3 + (b - 5) = a + b - 2$, total $g(N) - 3 < g(N)$ — el voraz **falla** (si $q \ge 1$).

Quitar dos monedas de 25 siempre es peor. Para $N < 25$ el voraz es óptimo (con solo monedas de 10 y 1). Por tanto el voraz falla exactamente cuando $N \ge 25$ y $(N \bmod 25) \bmod 10 \ge 5$.

**Conteo:** Los restos $r \in \{5,6,7,8,9,15,16,17,18,19\}$ son 10 clases. Para cada una, $N = 25q + r \le 1000$ permite $q = 1,\dots,39$ (pues $25\cdot 39 + 24 = 999 \le 1000$). Fallas: $10 \times 39 = 390$. Éxitos: $1000 - 390 = 610$.

Verifico con fuerza bruta:```python
def greedy(N):
    q, N = divmod(N, 25)
    a, b = divmod(N, 10)
    return q + a + b

def optimal(N):
    dp = [0] + [float('inf')] * N
    for i in range(1, N + 1):
        for c in (1, 10, 25):
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[N]

exitos = sum(greedy(N) == optimal(N) for N in range(1, 1001))
print(exitosos := exitos)
```
```
610
```

La fuerza bruta confirma el análisis: el algoritmo voraz falla exactamente cuando $(N \bmod 25) \bmod 10 \ge 5$ con $N \ge 25$, lo que da $390$ fallos y $610$ éxitos.

\boxed{610}