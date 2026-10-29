## Planteamiento

Como los coeficientes son enteros, $c_n = 2$ y todas las raíces son enteros distintos $r_1, \dots, r_n$, el polinomio se factoriza como:
$$g(x) = 2(x - r_1)(x - r_2)\cdots(x - r_n)$$

**Condición del término constante:** $c_0 = 2(-1)^n r_1 r_2 \cdots r_n = 78$, es decir:
$$(-1)^n \prod r_i = 39$$

**Objetivo:** $c_{n-1} = -2\sum r_i$, así que hay que minimizar $\left|\sum r_i\right|$ sujeto a que las raíces sean enteros distintos cuyo producto en valor absoluto sea $39 = 3 \cdot 13$.

## Búsqueda de raíces

Los únicos divisores disponibles son $\pm 1, \pm 3, \pm 13, \pm 39$, y ninguna raíz puede ser $0$. Reviso por número de raíces (respetando el signo $(-1)^n \prod r_i = 39$):

- **$n = 1$:** $r = -39$, suma $= -39$.
- **$n = 2$:** $\prod r_i = 39$: $\{3, 13\}$, $\{-3,-13\}$, $\{1,39\}$, $\{-1,-39\}$. Mejor suma: $|16|$.
- **$n = 3$:** $\prod r_i = -39$: $\{1, 3, -13\}$ da suma $-9$; $\{1,-3,13\}$ da $11$; $\{-1,3,13\}$ da $15$; $\{-1,-3,-13\}$ da $-17$. Mejor: $|{-9}| = 9$.
- **$n = 4$:** $\prod r_i = 39$: $\{1, -1, -3, 13\}$ da suma $10$; $\{1,-1,3,-13\}$ da $-10$. Mejor: $10$.
- **$n \geq 5$:** imposible, pues $39$ no admite 5 factores enteros distintos en valor absoluto.

El mínimo es $\left|\sum r_i\right| = 9$ con las raíces $\{1, 3, -13\}$.

## Verificación

$$g(x) = 2(x-1)(x-3)(x+13) = 2(x^3 + 9x^2 - 49x + 39) = 2x^3 + 18x^2 - 98x + 78$$

Efectivamente $c_n = 2$, $c_0 = 78$, raíces enteras distintas, y $|c_{n-1}| = 18$.

$$\boxed{18}$$