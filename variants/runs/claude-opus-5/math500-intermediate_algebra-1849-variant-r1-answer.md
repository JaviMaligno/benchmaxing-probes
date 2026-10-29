## Planteamiento

La ecuación $\log(kx) = 2\log(x+3)$ exige $kx > 0$ y $x+3 > 0$. Bajo esas condiciones:

$$kx = (x+3)^2 \quad\Longrightarrow\quad x^2 + (6-k)x + 9 = 0$$

Para las raíces: producto $= 9 > 0$, suma $= k-6$, discriminante $= (6-k)^2 - 36 = k^2 - 12k = k(k-12)$.

Nótese que $k=0$ queda excluido ($\log 0$ no existe).

## Caso $k < 0$

La condición $kx>0$ obliga a $x<0$. Como el producto de raíces es $9>0$ y la suma $k-6<0$, ambas raíces son negativas. El discriminante $k(k-12)>0$, así que son dos raíces distintas.

Como su producto es exactamente $9$ y ambas son negativas, no pueden estar las dos en $(-3,0)$ (daría producto $<9$) ni las dos fuera (daría producto $>9$). Por tanto **exactamente una** raíz cumple $-3 < x < 0$.

Así, todo $k$ con $-250 \le k \le -1$ funciona: **250 valores**.

## Caso $k > 0$

Aquí $kx>0$ obliga a $x>0$, y $x+3>0$ se cumple automáticamente. La suma y el producto de raíces son positivos, así que cualquier raíz real es válida.

- Si $0 < k < 12$: discriminante negativo, sin soluciones.
- Si $k = 12$: raíz doble $x = 3$, **exactamente una** solución.
- Si $k > 12$: dos raíces positivas distintas, dos soluciones.

Solo sirve $k=12$: **1 valor**.

## Total

$$250 + 1 = 251$$

\boxed{251}