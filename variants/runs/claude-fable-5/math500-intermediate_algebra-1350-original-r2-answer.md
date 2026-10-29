## Resolución

**Planteamiento.** Como las raíces $r_1, \dots, r_n$ son enteros distintos y $a_n = 2$, el polinomio se factoriza como
$$f(x) = 2(x - r_1)(x - r_2)\cdots(x - r_n).$$

**Condición sobre el producto de raíces.** El término constante es
$$a_0 = 2(-1)^n r_1 r_2 \cdots r_n = 66 \quad\Longrightarrow\quad |r_1 r_2 \cdots r_n| = 33.$$

Ninguna raíz puede ser $0$, y el producto de los valores absolutos de las raíces debe ser exactamente $33 = 3 \cdot 11$. Como las raíces son distintas, cada valor absoluto $>1$ aparece a lo más una vez (si estuvieran $3$ y $-3$, el producto tendría factor $9$, que no divide a $33$). Las posibles colecciones de valores absolutos son:

- $\{33\}$ (opcionalmente con $1$ y/o $-1$)
- $\{3, 11\}$ (opcionalmente con $1$ y/o $-1$)

**Condición sobre la suma.** El coeficiente buscado es
$$a_{n-1} = -2(r_1 + r_2 + \cdots + r_n) \quad\Longrightarrow\quad |a_{n-1}| = 2\left|\sum r_i\right|.$$

Hay que minimizar $\left|\sum r_i\right|$ eligiendo signos:

- $\{33\}$: suma mínima en valor absoluto $= 33$ (con $\pm 1$: $32$).
- $\{\pm 3, \pm 11\}$: $|\pm 3 \pm 11| \in \{8, 14\}$, mínimo $8$.
- $\{\pm 1, \pm 3, \pm 11\}$: $|\pm 1 \pm 3 \pm 11|$, mínimo $|1 + 3 - 11| = 7$.
- $\{1, -1, \pm 3, \pm 11\}$: los unos se cancelan, mínimo $8$.

El mínimo global es $7$, logrado por ejemplo con raíces $1, 3, -11$:
$$f(x) = 2(x-1)(x-3)(x+11) = 2x^3 + 14x^2 - 82x + 66,$$
donde efectivamente $a_0 = 66$, $a_n = 2$ y $|a_{n-1}| = 14$.

$$\boxed{14}$$