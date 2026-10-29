Razonemos paso a paso.

**Paso 1: Traducir la condición.**
$|a+bi| = \sqrt{a^2+b^2}$, así que la condición $|a+bi|\le 5$ equivale a
$$a^2+b^2\le 25.$$
Es decir, contamos los puntos enteros $(a,b)$ dentro del disco cerrado de radio 5.

**Paso 2: Contar por columnas.**
Para cada valor entero de $a$ con $a^2\le 25$ (es decir, $-5\le a\le 5$), contamos los enteros $b$ con $b^2\le 25-a^2$:

| $a$ | $25-a^2$ | valores de $b$ | cantidad |
|---|---|---|---|
| $0$ | 25 | $-5\le b\le 5$ | 11 |
| $\pm1$ | 24 | $|b|\le 4$ | 9 cada uno |
| $\pm2$ | 21 | $|b|\le 4$ | 9 cada uno |
| $\pm3$ | 16 | $|b|\le 4$ | 9 cada uno |
| $\pm4$ | 9 | $|b|\le 3$ | 7 cada uno |
| $\pm5$ | 0 | $b=0$ | 1 cada uno |

**Paso 3: Sumar.**
$$11 + 2(9) + 2(9) + 2(9) + 2(7) + 2(1) = 11 + 18 + 18 + 18 + 14 + 2 = 81.$$

**Verificación (suma de representaciones como suma de cuadrados):** contando $r_2(n)=4(d_1(n)-d_3(n))$ para $n\le 25$ y sumando $1$ (el origen), se obtiene $1+4+4+4+8+4+4+8+8+4+8+4+8+12+\dots = 81$, lo cual confirma el resultado.

\boxed{81}