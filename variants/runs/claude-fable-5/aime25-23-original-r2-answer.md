## Solución

**Configuración del algoritmo voraz.** Para $N$ cents, el algoritmo voraz toma $a = \lfloor N/25 \rfloor$ monedas de 25, luego el máximo de monedas de 10 y el resto en monedas de 1. Si escribimos $N = 25a + r$ con $0 \le r < 25$, el número de monedas del voraz es
$$a + \left\lfloor \frac{r}{10} \right\rfloor + (r \bmod 10).$$

**Cuándo puede fallar.** Una colección mejor solo puede diferir usando *menos* monedas de 25 (usar menos monedas de 10 a cambio de monedas de 1 nunca ayuda). El caso relevante es usar $a-1$ monedas de 25 y cubrir $25 + r$ con monedas de 10 y 1, lo que da
$$(a-1) + \left\lfloor \frac{25+r}{10} \right\rfloor + \big((25+r) \bmod 10\big)$$
monedas. (Quitar dos o más monedas de 25 solo empeora las cosas, pues $50$ cents requieren ya 5 monedas de 10.)

**Comparación residuo por residuo.** Sea $g(r) = \lfloor r/10 \rfloor + (r \bmod 10)$ y $h(r) = -1 + \lfloor (25+r)/10 \rfloor + ((25+r) \bmod 10)$:

- $r = 0,\dots,4$: $g \le 4$, mientras $h \ge 6$. El voraz gana.
- $r = 5,\dots,9$: $g = 5,\dots,9$ pero $h = 2,\dots,6$. **El voraz falla** (p. ej., $30 = 3$ monedas de 10 contra $25+5$).
- $r = 10,\dots,14$: $g = 1,\dots,5$, $h = 7,\dots,8$. El voraz gana.
- $r = 15,\dots,19$: $g = 6,\dots,10$ pero $h = 3,\dots,7$. **El voraz falla** (p. ej., $40 = 4$ monedas de 10).
- $r = 20,\dots,24$: $g = 2,\dots,6$, $h = 8,\dots,9$. El voraz gana.

Así, el voraz falla exactamente cuando $N \ge 25$ y $N \bmod 25 \in \{5,6,7,8,9,15,16,17,18,19\}$.

**Conteo de fallos en $1 \le N \le 1000$.** Los fallos son $N = 25a + r$ con $a \ge 1$ y $r$ en ese conjunto de 10 residuos. Para $a = 1, 2, \dots, 39$ hay 10 valores cada uno (el mayor es $25 \cdot 39 + 19 = 994 \le 1000$); para $a = 40$, el menor sería $1005 > 1000$. Total de fallos: $39 \times 10 = 390$.

**Respuesta.** Valores donde el voraz tiene éxito: $1000 - 390 = 610$.

$$\boxed{610}$$