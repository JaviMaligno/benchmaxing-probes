## Planteamiento

Como todas las raíces son enteros distintos y $c_n = 2$:

$$g(x) = 2(x-r_1)(x-r_2)\cdots(x-r_n)$$

**Condición del término constante:**
$$c_0 = g(0) = 2(-1)^n r_1r_2\cdots r_n = 78 \implies (-1)^n \prod r_i = 39$$

Como $39 = 3 \cdot 13$, cada raíz debe ser un divisor de 39, es decir, pertenecer a $\{\pm 1, \pm 3, \pm 13, \pm 39\}$ (ninguna puede ser 0).

**Condición del coeficiente buscado:**
$$c_{n-1} = -2\sum r_i \implies |c_{n-1}| = 2\left|\sum r_i\right|$$

Hay que minimizar $\left|\sum r_i\right|$, con la restricción de paridad: si $n$ es par, $\prod r_i = 39$; si $n$ es impar, $\prod r_i = -39$.

## Búsqueda por casos

| $n$ | Conjuntos válidos | Sumas |
|---|---|---|
| 1 | $\{-39\}$ | $-39$ |
| 2 | $\{3,13\},\{-3,-13\},\{1,39\},\{-1,-39\}$ | $\pm16,\ \pm40$ |
| 3 | $\{1,3,-13\},\{1,-3,13\},\{-1,3,13\},\{-1,-3,-13\},\{1,-1,39\}$ | $\mathbf{-9},\ 11,\ 15,\ -17,\ 39$ |
| 4 | $\{1,-1,3,-13\},\{1,-1,-3,13\}$ | $\mp 10$ |
| 5 | ninguno (requeriría repetir $\pm1$) | — |

El mínimo de $\left|\sum r_i\right|$ es $9$, alcanzado con las raíces $\{1, 3, -13\}$.

## Verificación

$$g(x) = 2(x-1)(x-3)(x+13) = 2x^3 + 18x^2 - 86x + 78$$

- $c_3 = 2$ ✓
- $c_0 = 78$ ✓
- Raíces enteras distintas: $1, 3, -13$ ✓
- $|c_{n-1}| = |18| = 2\cdot 9 = 18$

\boxed{18}