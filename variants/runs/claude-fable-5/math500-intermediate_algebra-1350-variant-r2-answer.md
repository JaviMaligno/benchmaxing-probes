## Planteamiento

Como todas las raíces son enteros distintos y el coeficiente principal es $c_n = 2$, el polinomio se factoriza como:
$$g(x) = 2(x - r_1)(x - r_2)\cdots(x - r_n)$$

**Condición del término constante.** Evaluando en $x=0$:
$$c_0 = g(0) = 2\prod_{i}(-r_i) = 78 \quad\Longrightarrow\quad \prod_i (-r_i) = 39$$

Definiendo $s_i = -r_i$, necesitamos enteros **distintos** $s_i$ con $\prod s_i = 39$.

**Qué queremos minimizar.** Por las fórmulas de Vieta, $c_{n-1} = -2\sum r_i = 2\sum s_i$, así que:
$$|c_{n-1}| = 2\left|\sum s_i\right|$$

## Búsqueda del mínimo

Como $39 = 3 \cdot 13$, los $s_i$ solo pueden tener valores absolutos en $\{1, 3, 13, 39\}$. No podemos repetir un mismo valor absoluto con ambos signos salvo el $1$ (porque $3\cdot 3 = 9 \nmid 39$ y $13 \cdot 13 = 169 > 39$). Los casos posibles:

- **Usando 39:** $\{39\}$, $\{-1,-39\}$, $\{1,-1,-39\}$, etc. → $|\text{suma}| \geq 38$.
- **Usando 3 y 13** (con posibles $\pm 1$), exigiendo producto $= +39$:
  - $\{3, 13\}$: suma $16$
  - $\{-3, -13\}$: suma $-16$
  - $\{1, 3, 13\}$: suma $17$
  - $\{1, -3, -13\}$: suma $-15$
  - $\{-1, 3, -13\}$: suma $-11$
  - $\{-1, -3, 13\}$: suma $\mathbf{9}$ ✓ (producto: $(-1)(-3)(13) = 39$ ✓)
  - $\{1, -1, -3, 13\}$: suma $10$
  - $\{1, -1, 3, -13\}$: suma $-10$

El mínimo es $\left|\sum s_i\right| = 9$.

## Verificación

Con $s = \{-1, -3, 13\}$ las raíces son $r = \{1, 3, -13\}$:
$$g(x) = 2(x-1)(x-3)(x+13) = 2x^3 + 18x^2 - 86x + 78$$

- $c_0 = 78$ ✓, $c_n = 2$ ✓, raíces enteras distintas ✓
- $|c_{n-1}| = |18| = 2 \cdot 9 = 18$

$$\boxed{18}$$