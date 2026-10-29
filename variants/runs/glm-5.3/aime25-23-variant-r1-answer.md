## Planteamiento

Escribo $N = 24a + r$ con $0 \le r \le 23$. El algoritmo codicioso toma $a$ monedas de 24, luego $\lfloor r/10 \rfloor$ monedas de 10, y luego el resto en monedas de 1. Defino $f(M) = \lfloor M/10 \rfloor + (M \bmod 10)$, el número mínimo de monedas para formar $M$ usando solo monedas de 1 y 10. Entonces el codicioso usa $g(N) = a + f(r)$ monedas.

**Criterio de fallo:** cualquier otra colección usa $z = a - k$ monedas de 24 (con $k \ge 0$), y luego necesita al menos $f(24k + r)$ monedas para el valor restante $24k + r$. El codicioso falla si y solo si existe $k \ge 1$ con $$(a - k) + f(24k + r) < a + f(r),$$ es decir, $f(24k + r) \le f(r) + k - 1$. Nota: esta condición no depende de $a$.

## Análisis por residuo $r = N \bmod 24$

**Caso $k = 1$:** el fallo equivale a $f(24 + r) \le f(r)$. Como $24 + r \equiv 4 + r \pmod{10}$:

| $r$ | $f(r)$ | $f(24+r)$ | ¿Falla? |
|---|---|---|---|
| 0–5 | $r$ | $r + 6$ | No |
| **6–9** | $r$ | $r - 3$ | **Sí** |
| 10–15 | $r - 9$ | $r - 2$ | No |
| **16–19** | $r - 9$ | $r - 12$ | **Sí** |
| 20–23 | $r - 18$ | $r - 10$ | No |

(Por ejemplo, $r = 16$: $N = 24a + 16$ usa $a + 7$ monedas, pero $24(a-1) + 4 \times 10$ usa solo $a + 3$.)

**Residuos buenos** $\{0,1,2,3,4,5,10,...,15,20,...,23\}$: aquí $f(r) \le 6$. Verifico que ningún $k \ge 2$ causa fallo:
- $k = 2$: $f(48 + r) \ge f(r) + 3$ (los peores casos son $r \equiv 2 \pmod{10}$: $f(50)=5, f(60)=6, f(70)=7$ contra $f(r)+1 \le 5$).
- $k = 3$: $f(72 + r) \ge 9 > f(r) + 2$.
- $k \ge 4$: $f(24k + r) \ge \lceil (24k+r)/10 \rceil \ge \lceil 96/10 \rceil = 10 > k + f(r) - 1$ (para $k=4$), y para $k \ge 5$ vale $f \ge 2.4k > k + 5$.

**Conclusión:** el codicioso falla exactamente cuando $N \equiv 6, 7, 8, 9, 16, 17, 18, 19 \pmod{24}$ **y** $N \ge 24$. Todos los $N \in [1, 23]$ funcionan (no caben monedas de 24).

## Conteo en $[1, 1000]$

Cuento los fallos ($N \ge 24$ con residuo malo). Como $1000 = 24 \cdot 41 + 16$:

- $r \in \{6,7,8,9,16\}$: $N = 24a + r$ con $1 \le a \le 41$ → 41 valores cada uno → $5 \times 41 = 205$.
- $r \in \{17,18,19\}$: $24 \cdot 41 + r > 1000$, así que $1 \le a \le 40$ → 40 valores cada uno → $3 \times 40 = 120$.

Total de fallos: $205 + 120 = 325$.

Éxitos: $1000 - 325 = 675$.

\boxed{675}