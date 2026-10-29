## Planteamiento

Como el polinomio tiene todas sus raíces enteras y distintas, con $a_n = 2$:

$$f(x) = 2(x-r_1)(x-r_2)\cdots(x-r_n)$$

**Condición del término independiente:**
$$a_0 = 2(-1)^n r_1r_2\cdots r_n = 66 \quad\Longrightarrow\quad \prod r_i = (-1)^n\cdot 33$$

**Lo que hay que minimizar:**
$$a_{n-1} = -2\sum r_i \quad\Longrightarrow\quad |a_{n-1}| = 2\left|\sum r_i\right|$$

## Casos posibles

Como $33 = 3\cdot 11$ y las raíces son distintas, los valores absolutos de las raíces deben formar una factorización de $33$ en factores distintos: $\{33\}$, $\{1,33\}$, $\{3,11\}$ o $\{1,3,11\}$.

| Valores absolutos | $n$ | Signo requerido | Mejor suma | $|a_{n-1}|$ |
|---|---|---|---|---|
| $\{33\}$ | 1 | $-33$ | $-33$ | 66 |
| $\{1,33\}$ | 2 | $+33$ | $\pm34$ | 68 |
| $\{3,11\}$ | 2 | $+33$ | $\pm14$ | 28 |
| $\{1,3,11\}$ | 3 | $-33$ | $-7$ | **14** |

En el último caso se necesita un número impar de raíces negativas. Las opciones son $-1+3+11=13$, $1-3+11=9$, $1+3-11=-7$ y $-1-3-11=-15$. La mejor es $\{1,3,-11\}$.

**Verificación:** $f(x) = 2(x-1)(x-3)(x+11) = 2x^3 + 14x^2 - 82x + 66$, con $a_0 = 66$, $a_3 = 2$ y $|a_2| = 14$. ✓

Nótese que no se puede añadir el par $\{1,-1\}$ a una solución válida, pues eso cambia el signo del producto sin alterar la paridad de $n$.

\boxed{14}