## Planteamiento

El módulo de un número complejo $x + yi$ es

$$|x + yi| = \sqrt{x^2 + y^2}.$$

La desigualdad $|x + yi| \le 6$ equivale entonces a

$$x^2 + y^2 \le 36,$$

es decir, hay que contar los puntos de la red entera dentro (o sobre) el círculo de radio $6$ centrado en el origen.

## Conteo por filas

Fijamos $y$ y contamos los enteros $x$ que cumplen $x^2 \le 36 - y^2$:

| $y$ | $x^2 \le$ | $x$ permitidos | cantidad | filas | total |
|---|---|---|---|---|---|
| $0$ | $36$ | $-6,\dots,6$ | $13$ | $1$ | $13$ |
| $\pm 1$ | $35$ | $-5,\dots,5$ | $11$ | $2$ | $22$ |
| $\pm 2$ | $32$ | $-5,\dots,5$ | $11$ | $2$ | $22$ |
| $\pm 3$ | $27$ | $-5,\dots,5$ | $11$ | $2$ | $22$ |
| $\pm 4$ | $20$ | $-4,\dots,4$ | $9$ | $2$ | $18$ |
| $\pm 5$ | $11$ | $-3,\dots,3$ | $7$ | $2$ | $14$ |
| $\pm 6$ | $0$ | solo $x=0$ | $1$ | $2$ | $2$ |

(Obsérvese que $y = \pm 7$ ya es imposible, pues $49 > 36$.)

## Suma

$$13 + 22 + 22 + 22 + 18 + 14 + 2 = 113.$$

**Verificación** (método alternativo): el conteo coincide con $\sum_{k=0}^{36} r_2(k)$, donde $r_2(k)$ es el número de representaciones de $k$ como suma de dos cuadrados. Usando $r_2(k) = 4(d_1(k) - d_3(k))$ para $k \ge 1$ y sumando $k = 0, 1, \dots, 36$ se obtiene de nuevo $113$, el valor clásico del problema del círculo de Gauss para radio $6$.

$$\boxed{113}$$