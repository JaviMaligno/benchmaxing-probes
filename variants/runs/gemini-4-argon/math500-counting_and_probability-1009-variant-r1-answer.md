Para determinar cuántas selecciones diferentes de siete muffins se pueden elegir entre tres tipos disponibles (arándano, plátano y salvado), podemos modelar este problema utilizando el método de combinaciones con repetición (también conocido como el método de barras y estrellas).

1. **Definición de variables:**
   Sea $x_1$ la cantidad de muffins de arándano, $x_2$ la cantidad de muffins de plátano y $x_3$ la cantidad de muffins de salvado. Como se eligen $7$ muffins en total y hay al menos $7$ de cada tipo, buscamos el número de soluciones enteras no negativas para la ecuación:
   $$x_1 + x_2 + x_3 = 7$$
   donde $x_1, x_2, x_3 \ge 0$.

2. **Aplicación de la fórmula:**
   El número de combinaciones con repetición al elegir $k$ elementos de $n$ tipos distintos está dado por la fórmula:
   $$\binom{n + k - 1}{k} = \binom{n + k - 1}{n - 1}$$
   Sustituyendo $n = 3$ (tipos de muffins) y $k = 7$ (muffins a elegir):
   $$\binom{3 + 7 - 1}{7} = \binom{9}{7}$$

3. **Cálculo final:**
   Por simetría de los coeficientes binomiales, $\binom{9}{7} = \binom{9}{2}$:
   $$\binom{9}{2} = \frac{9 \times 8}{2 \times 1} = 36$$

\boxed{36}