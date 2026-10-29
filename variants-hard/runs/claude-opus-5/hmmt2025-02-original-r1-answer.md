## Planteamiento

Sea $n = \underline{bcd}$. La condición es

$$\sqrt{1000a + n} = a\sqrt{n}$$

Elevando al cuadrado:

$$1000a + n = a^2 n \quad\Longrightarrow\quad 1000a = n(a^2-1) \quad\Longrightarrow\quad n = \frac{1000a}{a^2-1}$$

## Búsqueda sobre $a$

Como $a^2-1$ debe dividir a $1000a$, y $\gcd(a, a^2-1)=1$, se necesita $(a^2-1) \mid 1000$:

| $a$ | $a^2-1$ | $n = 1000a/(a^2-1)$ |
|---|---|---|
| 2 | 3 | $666.\overline{6}$ |
| 3 | 8 | **375** |
| 4 | 15 | $266.\overline{6}$ |
| 5 | 24 | $208.\overline{3}$ |
| 6 | 35 | $171.4\ldots$ |
| 7 | 48 | $145.8\overline{3}$ |
| 8 | 63 | $126.98\ldots$ |
| 9 | 80 | $112.5$ |

El único caso entero es $a=3$, $n=375$.

## Verificación

$$3\sqrt{375} = \sqrt{9 \cdot 375} = \sqrt{3375} \;\checkmark$$

\boxed{3375}