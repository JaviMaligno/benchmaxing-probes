## Planteamiento

Sea $N=\underline{bcde}$ (valor entre 0 y 9999, admitiendo ceros iniciales). Entonces $\underline{abcde}=10000a+N$, y la igualdad es:

$$\sqrt{10000a+N}=a\sqrt{N}$$

Elevando al cuadrado:

$$10000a+N=a^2N\quad\Longrightarrow\quad 10000a=N(a^2-1)\quad\Longrightarrow\quad N=\frac{10000a}{a^2-1}$$

## Búsqueda de soluciones

Con $a=1$ la ecuación daría $10000=0$, imposible. Para $a=2,\dots,9$ se requiere que $a^2-1$ divida a $10000a$; como $\gcd(a,a^2-1)=1$, hace falta $(a^2-1)\mid 10000=2^4\cdot 5^4$:

| $a$ | $a^2-1$ | $N=\frac{10000a}{a^2-1}$ |
|---|---|---|
| 2 | 3 | no entero |
| 3 | 8 | $3750$ ✓ |
| 4 | 15 | no entero |
| 5 | 24 | no entero |
| 6 | 35 | no entero |
| 7 | 48 | no entero |
| 8 | 63 | no entero |
| 9 | 80 | $1125$ ✓ |

Ambos valores cumplen $N\le 9999$, así que son válidos.

## Verificación

- $a=3$, $N=3750$: $\underline{abcde}=33750$ y $3\sqrt{3750}=\sqrt{9\cdot 3750}=\sqrt{33750}$ ✓
- $a=9$, $N=1125$: $\underline{abcde}=91125$ y $9\sqrt{1125}=\sqrt{81\cdot 1125}=\sqrt{91125}$ ✓

## Suma

$$33750+91125=124875$$

\boxed{124875}