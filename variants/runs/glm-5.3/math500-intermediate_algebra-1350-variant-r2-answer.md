## Razonamiento

Como todas las raíces son enteros distintos $r_1,\dots,r_n$, y $c_n=2$:

$$g(x)=2\prod_{i=1}^n (x-r_i)$$

**Condición sobre el término constante:**

$$c_0 = 2(-1)^n\prod r_i = 78 \;\Longrightarrow\; \prod r_i = 39\,(-1)^n$$

Por tanto $\prod |r_i| = 39 = 3\cdot 13$, así que cada raíz satisface $|r_i|\in\{1,3,13,39\}$. Además, como dos raíces con el mismo valor absoluto serían $r$ y $-r$, y $3\cdot 3 \nmid 39$, solo puede haber a lo sumo una raíz con valor absoluto $3$, una con $13$, una con $39$, y las dos raíces $1,-1$.

**Coeficiente que queremos minimizar:**

$$c_{n-1} = -c_n\sum r_i = -2\sum r_i \;\Longrightarrow\; |c_{n-1}| = 2\left|\sum r_i\right|$$

(válido también para $n=1$, donde $c_{n-1}=c_0$).

**Enumeración de configuraciones de valores absolutos** (con la condición de signo $\prod r_i = \pm 39$ según la paridad de $n$):

| Valores abs. | $n$ | Signos válidos | $\sum r_i$ posible | $|c_{n-1}|$ |
|---|---|---|---|---|
| $\{39\}$ | 1 | $(-39)$ | $-39$ | $78$ |
| $\{39,1\}$ | 2 | $(39,1),(-39,-1)$ | $\pm 40$ | $80$ |
| $\{39,1,1\}$ | 3 | $(39,1,-1)$ | $39$ | $78$ |
| $\{3,13\}$ | 2 | $(3,13),(-3,-13)$ | $\pm 16$ | $32$ |
| $\{3,13,1\}$ | 3 | impar de negativos | $15,-9,11,-17$ | $\min: 18$ |
| $\{3,13,1,1\}$ | 4 | $(\pm3,\pm13,1,-1)$ | $\pm 16$ | $32$ |

El mínimo de $\left|\sum r_i\right|$ es $9$, alcanzado con raíces $\{3,-13,1\}$ (producto $-39 = 39\cdot(-1)^3$ ✓).

**Verificación:**

$$g(x)=2(x-3)(x+13)(x-1)=2x^3+18x^2-98x+78$$

$c_3=2$ ✓, $c_0=78$ ✓, raíces $3,-13,1$ enteras y distintas ✓, y $c_2 = 18$.

$$\boxed{18}$$