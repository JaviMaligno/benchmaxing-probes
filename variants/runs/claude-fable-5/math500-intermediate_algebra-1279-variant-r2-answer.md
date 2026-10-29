## Resolución

**Paso 1: Reescribir cada término.** Observo que
$$\frac{k}{x^2-k} = \frac{x^2 - (x^2-k)}{x^2-k} = \frac{x^2}{x^2-k} - 1.$$

Sumando para $k=1,2,3,4$, la ecuación se convierte en
$$x^2\sum_{k=1}^{4}\frac{1}{x^2-k} - 4 = 2022x - 4 \quad\Longrightarrow\quad x^2\sum_{k=1}^{4}\frac{1}{x^2-k} = 2022x.$$

**Paso 2: Identificar la raíz $x=0$.** Sustituyendo $x=0$ en la ecuación original: el lado izquierdo da $-1-1-1-1=-4$ y el derecho da $-4$, así que $x=0$ es raíz (y no aporta nada a la suma).

**Paso 3: Formar el polinomio para $x\neq 0$.** Dividiendo entre $x$:
$$x\sum_{k=1}^{4}\frac{1}{x^2-k} = 2022.$$

Multiplicando por $P(x) = \prod_{k=1}^{4}(x^2-k)$:
$$x\sum_{k=1}^{4}\prod_{j\neq k}(x^2-j) = 2022\prod_{k=1}^{4}(x^2-k).$$

**Paso 4: Aplicar Vieta.** El lado derecho es un polinomio de grado 8 con término líder $2022x^8$, y como $\prod(x^2-k)$ solo contiene potencias pares de $x$, no aporta término en $x^7$. El lado izquierdo es $x$ por una suma de cuatro polinomios de grado 6 (cada uno con término líder $x^6$), es decir, su término líder es $4x^7$, y solo contiene potencias impares.

El polinomio resultante es
$$2022x^8 - 4x^7 + (\text{términos de grado menor}) = 0.$$

Por las fórmulas de Vieta, la suma de sus 8 raíces es
$$\frac{4}{2022} = \frac{2}{1011}.$$

Añadiendo la raíz $x=0$ (que no cambia la suma), la suma de todas las raíces complejas de la ecuación es:

$$\boxed{\dfrac{2}{1011}}$$