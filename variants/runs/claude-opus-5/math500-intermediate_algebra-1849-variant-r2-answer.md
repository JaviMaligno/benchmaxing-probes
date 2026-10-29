## Planteamiento

La ecuación $\log(kx) = 2\log(x+3)$ exige:
- $kx > 0$
- $x + 3 > 0$, es decir $x > -3$

Bajo esas condiciones equivale a $kx = (x+3)^2$, o sea
$$x^2 + (6-k)x + 9 = 0.$$

El discriminante es $(6-k)^2 - 36 = k^2 - 12k = k(k-12)$, y el producto de las raíces es $9 > 0$, con suma $k - 6$.

## Caso $k = 0$

No hay solución ($\log 0$ no está definido).

## Caso $k > 0$

Se requiere $x > 0$.

- Si $0 < k < 12$: discriminante negativo, sin raíces reales → 0 soluciones.
- Si $k = 12$: raíz doble $x = 3 > 0$ → **exactamente una solución**.
- Si $k > 12$: dos raíces reales distintas; como el producto es $9>0$ y la suma $k-6>0$, ambas son positivas → 2 soluciones.

Solo sirve $k = 12$.

## Caso $k < 0$

Se requiere $x < 0$, junto con $x > -3$: el intervalo es $-3 < x < 0$.

El discriminante $k(k-12) > 0$, así que hay dos raíces reales distintas, ambas negativas (producto $9>0$, suma $k-6<0$).

Con $f(x) = x^2 + (6-k)x + 9$:
$$f(-3) = 9 - 3(6-k) + 9 = 3k < 0, \qquad f(0) = 9 > 0.$$

Por el cambio de signo hay exactamente una raíz en $(-3,0)$; la otra queda a la izquierda de $-3$ (fuera del dominio). Luego **todo** $k < 0$ da exactamente una solución.

En $[-250, 400]$ eso son los valores $k = -250, \dots, -1$: **250** enteros.

## Total

$$250 + 1 = 251$$

\boxed{251}