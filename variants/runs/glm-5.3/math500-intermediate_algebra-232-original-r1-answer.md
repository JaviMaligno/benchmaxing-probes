Vamos a contar los pares enteros $(a,b)$ tales que $|a+bi|\le 5$, es decir, $\sqrt{a^2+b^2}\le 5$, o equivalentemente:
$$a^2+b^2\le 25.$$

**Paso 1: Rango de $a$.** Como $a^2\le 25$, tenemos $a\in\{-5,-4,\dots,5\}$.

**Paso 2: Contar los valores de $b$ para cada $a$.** Para cada $a$, necesitamos $b^2\le 25-a^2$:

- $a=0$: $b^2\le 25$ → $b\in\{-5,\dots,5\}$ → **11 valores**
- $a=\pm 1$: $b^2\le 24$ → $|b|\le 4$ → **9 valores** cada uno
- $a=\pm 2$: $b^2\le 21$ → $|b|\le 4$ → **9 valores** cada uno
- $a=\pm 3$: $b^2\le 16$ → $|b|\le 4$ → **9 valores** cada uno
- $a=\pm 4$: $b^2\le 9$ → $|b|\le 3$ → **7 valores** cada uno
- $a=\pm 5$: $b^2\le 0$ → $b=0$ → **1 valor** cada uno

**Paso 3: Sumar.**
$$11 + 2(9+9+9+7+1) = 11 + 2(35) = 11+70 = 81.$$

Es decir, hay $81$ pares ordenados (los mismos que los puntos de la retícula dentro o sobre el círculo de radio $5$ centrado en el origen).

$$\boxed{81}$$