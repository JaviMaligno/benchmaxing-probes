## Solución

**Planteamiento del algoritmo voraz.** Para un valor $N$, el algoritmo voraz toma $q = \lfloor N/25 \rfloor$ monedas de 25, luego dimes y centavos para el resto $r = N \bmod 25$. Con solo monedas de 1 y 10 el voraz siempre es óptimo, así que la única forma de mejorar es **usar menos monedas de 25** y compensar con dimes y centavos.

**Función auxiliar.** Sea $a(m) = \lfloor m/10 \rfloor + (m \bmod 10)$ el número mínimo de monedas de 1 y 10 que suman $m$. El voraz usa $q + a(r)$ monedas. Quitar una moneda de 25 da $q - 1 + a(r+25)$ monedas, así que el voraz **falla** si y solo si
$$a(r+25) \le a(r),$$
(quitar más de una moneda de 25 nunca ayuda si quitar una no ayuda, por la estructura de $a$).

**Análisis por residuo** $r = N \bmod 25$:

| $r$ | $a(r)$ | $a(r+25)$ | ¿Falla? |
|---|---|---|---|
| $0$–$4$ | $r$ | $r+7$ | No |
| $5$–$9$ | $r$ | $r-2$ | **Sí** |
| $10$–$14$ | $r-9$ | $r-2$ | No |
| $15$–$19$ | $r-9$ | $r-11$ | **Sí** |
| $20$–$24$ | $r-18$ | $r-11$ | No |

Por ejemplo, $r=17$: el voraz usa $1$ dime $+ 7$ centavos ($8$ monedas), pero con $r+25 = 42$ se logra con $4$ dimes $+ 2$ centavos ($6$ monedas), ahorrando incluso contando la moneda de 25 eliminada.

**Conteo.** El voraz falla exactamente cuando $N \ge 25$ y $N \bmod 25 \in \{5,\dots,9\} \cup \{15,\dots,19\}$ (10 residuos). Para $N \le 24$ no hay monedas de 25 que quitar, así que el voraz siempre tiene éxito ahí.

En el rango $25 \le N \le 999$ hay $975 = 39 \times 25$ valores, es decir, 39 ciclos completos de residuos, cada uno con 10 fallas:
$$39 \times 10 = 390 \text{ fallas}.$$
$N = 1000$ tiene residuo $0$, por lo que tiene éxito.

**Resultado.** Los valores exitosos son
$$1000 - 390 = 610.$$

$$\boxed{610}$$