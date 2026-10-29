## Planteamiento

**Paso 1: Dominio y simplificación.**

La ecuación $\log(kx) = 2\log(x+3)$ requiere $kx > 0$ y $x + 3 > 0$ (es decir, $x > -3$).

Aplicando propiedades de logaritmos (legítimas bajo el dominio):
$$\log(kx) = \log\big((x+3)^2\big) \implies kx = (x+3)^2$$

**Paso 2: Ecuación cuadrática.**

Reordenando:
$$x^2 + (6-k)x + 9 = 0$$

Observación clave: si $x > -3$ y $x$ es raíz de esta cuadrática, entonces $kx = (x+3)^2 > 0$ se cumple automáticamente. (La raíz $x=-3$ solo aparece si $k=0$, caso donde $\log(0)$ es indefinido.) Así que basta contar raíces reales con $x > -3$.

**Paso 3: Análisis por casos según el discriminante.**

El discriminante es $(6-k)^2 - 36 = k(k-12)$, y las raíces tienen producto $9$ y suma $k-6$.

- **$k = 0$:** raíz doble $x = -3$, inválida ($\log 0$ indefinido). → 0 soluciones. ✗
- **$0 < k < 12$:** discriminante negativo, no hay raíces reales. → 0 soluciones. ✗
- **$k = 12$:** raíz doble $x = 3 > -3$, válida ($\log 36 = 2\log 6$). → exactamente 1 solución. ✓
- **$k > 12$:** dos raíces reales distintas, de producto $9>0$ y suma $k-6>0$, ambas positivas y $> -3$. → 2 soluciones. ✗
- **$k < 0$:** dos raíces reales negativas. Evaluando $f(-3) = 9 + (6-k)(-3) + 9 = 3k < 0$, como la parábola abre hacia arriba, $-3$ queda **entre** las dos raíces: la menor es $< -3$ (inválida) y la mayor es $> -3$ (válida, y $kx = (x+3)^2 > 0$ se cumple). → exactamente 1 solución. ✓

*Verificación con $k = -1$:* $x^2 + 7x + 9 = 0$ da $x \approx -1.697$ (válido: $\log(1.697) = \log((1.303)^2)$ ✓) y $x \approx -5.303$ (inválido, $x+3<0$). Exactamente una solución. ✓

**Paso 4: Conteo de enteros en $[-250, 400]$.**

- Enteros negativos: de $-250$ a $-1$ → $250$ valores.
- El valor $k = 12$ → $1$ valor.

Total: $250 + 1 = 251$.

$$\boxed{251}$$