Para encontrar el valor de $n$, contemos la cantidad de cuadrados de cada uno de los tres tamaños posibles cuyos vértices son puntos de la cuadrícula de $3 \times n$ puntos:

1. **Cuadrados de lado $1$ (alineados con la cuadrícula):**
   En una cuadrícula de $3 \times n$ puntos, hay $3 - 1 = 2$ filas de cuadrados unitarios y $n - 1$ columnas de cuadrados unitarios. Por lo tanto, el número de cuadrados de lado $1$ es:
   $$2(n - 1)$$

2. **Cuadrados de lado $2$ (alineados con la cuadrícula):**
   Cada cuadrado de $2 \times 2$ abarca $3$ puntos de alto y $3$ puntos de ancho. En una cuadrícula de $3 \times n$ puntos, caben $3 - 2 = 1$ a lo alto y $n - 2$ a lo ancho. Por lo tanto, el número de cuadrados de lado $2$ es:
   $$n - 2$$

3. **Cuadrados de lado $\sqrt{2}$ (inclinados):**
   Dentro de cada región cuadrada de $2 \times 2$ (formada por $3 \times 3$ puntos), se puede formar exactamente un cuadrado inclinado de lado $\sqrt{2}$ conectando los puntos medios de los cuatro lados del cuadrado de $2 \times 2$. Como hay $n - 2$ cuadrados de $2 \times 2$, el número de cuadrados de lado $\sqrt{2}$ también es:
   $$n - 2$$

Sumando las cantidades de los tres tamaños de cuadrados e igualando al total de $70$:
$$2(n - 1) + (n - 2) + (n - 2) = 70$$
$$2n - 2 + 2n - 4 = 70$$
$$4n - 6 = 70$$
$$4n = 76$$
$$n = 19$$

\boxed{19}