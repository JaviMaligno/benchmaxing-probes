## Planteamiento

La ecuación $\log(kx) = 2\log(x+3)$ requiere:
- $x + 3 > 0$, es decir $x > -3$
- $kx > 0$

Igualando: $kx = (x+3)^2$, o sea $x^2 + (6-k)x + 9 = 0$.

## Caso $k < 0$

Necesitamos $kx > 0$, lo que exige $x < 0$; junto con $x > -3$, buscamos raíces en $(-3, 0)$.

Sea $f(x) = (x+3)^2 - kx$. Entonces $f(-3) = 3k < 0$ y $f(0) = 9 > 0$. Como $f$ es cuadrática y cambia de signo en el intervalo, tiene exactamente una raíz en $(-3, 0)$. No puede haber otra solución con $x > 0$ porque ahí $kx < 0$. Por lo tanto, **todo $k < 0$ da exactamente una solución**.

En $[-250, 400]$ hay $250$ enteros negativos: $k = -250, \dots, -1$.

## Caso $k = 0$

$\log(0)$ no está definido: no hay solución.

## Caso $k > 0$

Necesitamos $x > 0$. En $x^2 + (6-k)x + 9 = 0$, el producto de raíces es $9 > 0$ y la suma es $k - 6$. Hay raíces reales cuando $(k-6)^2 \ge 36$, es decir $k \ge 12$ (para $k$ positivo).

- Si $k > 12$: dos raíces reales distintas, ambas positivas (suma y producto positivos), así que hay **dos** soluciones — no sirve.
- Si $k = 12$: raíz doble $x = 3 > 0$, exactamente **una** solución — sirve.
- Si $0 < k < 12$: sin raíces reales.

Solo $k = 12$ funciona entre los positivos.

## Total

$$250 + 1 = 251$$

$$\boxed{251}$$