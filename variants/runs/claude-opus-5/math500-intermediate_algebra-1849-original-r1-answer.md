## Planteamiento

La ecuación $\log(kx) = 2\log(x+2)$ exige $kx > 0$ y $x + 2 > 0$. Bajo esas condiciones equivale a

$$kx = (x+2)^2 \iff x^2 + (4-k)x + 4 = 0.$$

El producto de las raíces es $4 > 0$ y su suma es $k - 4$. El discriminante es $(4-k)^2 - 16 = k(k-8)$.

**Caso $k = 0$:** $\log(0)$ no está definido, no hay soluciones.

**Caso $k < 0$:** se necesita $x < 0$, junto con $x > -2$, es decir $-2 < x < 0$. El discriminante $k(k-8) > 0$, así que hay dos raíces reales distintas; como el producto es positivo y la suma $k-4 < 0$, ambas son negativas. Con $f(x) = x^2 + (4-k)x + 4$ se tiene $f(-2) = 2k < 0$ y $f(0) = 4 > 0$, luego exactamente una raíz cae en $(-2,0)$ y la otra es menor que $-2$. Por tanto **todo $k < 0$ sirve**: los valores $k = -1, \dots, -500$, es decir $500$ valores.

**Caso $k > 0$:** se necesita $x > 0$ (lo cual ya implica $x > -2$).
- Si $0 < k < 8$: discriminante negativo, no hay soluciones reales.
- Si $k = 8$: raíz doble $x = 2 > 0$, exactamente una solución. ✓
- Si $k > 8$: dos raíces reales distintas, ambas positivas (producto $4>0$, suma $k-4>0$), lo que da dos soluciones.

Solo $k = 8$ funciona: $1$ valor.

## Total

$$500 + 1 = 501$$

\boxed{501}