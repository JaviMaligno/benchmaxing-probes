## Planteamiento

La ecuación $\log(kx) = 2\log(x+3)$ exige:
- $x + 3 > 0$, es decir $x > -3$,
- $kx > 0$,
- y, al igualar, $kx = (x+3)^2$, o sea $x^2 + (6-k)x + 9 = 0$.

## Caso $k = 0$

$kx = 0$ nunca es positivo: **sin soluciones**.

## Caso $k > 0$

Necesitamos $x > 0$ (para que $kx > 0$). El discriminante es $(6-k)^2 - 36 = k(k-12)$.

- Si $0 < k < 12$: discriminante negativo, sin soluciones reales.
- Si $k = 12$: raíz doble $x = \frac{k-6}{2} = 3 > 0$. **Exactamente una solución**. ✓
- Si $k > 12$: dos raíces reales con producto $9 > 0$ y suma $k - 6 > 6 > 0$, así que ambas son positivas y válidas: **dos soluciones**, no sirve.

Solo funciona $k = 12$.

## Caso $k < 0$

Ahora $kx > 0$ exige $x < 0$, combinado con $x > -3$: necesitamos $x \in (-3, 0)$.

El discriminante $k(k-12) > 0$ siempre que $k < 0$, así que hay dos raíces reales. Su producto es $9 > 0$ y su suma es $k - 6 < 0$: ambas raíces son negativas.

Evaluando $f(x) = x^2 + (6-k)x + 9$ en $x = -3$:
$$f(-3) = 9 - 3(6-k) + 9 = 3k < 0.$$

Como $f(-3) < 0$ y la parábola abre hacia arriba, hay exactamente una raíz mayor que $-3$ (y la otra menor que $-3$, que queda descartada). Esa raíz está en $(-3, 0)$, así que **cada entero negativo $k$ da exactamente una solución**. ✓

## Conteo en $[-250, 400]$

- Enteros negativos: $k \in \{-250, \dots, -1\}$, que son $250$ valores.
- Enteros positivos: solo $k = 12$, un valor.

Total: $250 + 1 = 251$.

$$\boxed{251}$$