Para determinar cuántas combinaciones diferentes de siete muffins se pueden elegir, podemos plantear el problema utilizando el método de combinaciones con repetición (también conocido como el método de «estrellas y barras»).

1. **Definición de variables:**
   Sea $x_1$ la cantidad de muffins de arándano, $x_2$ la cantidad de muffins de plátano y $x_3$ la cantidad de muffins de salvado. Como se eligen $7$ muffins en total y hay al menos $7$ disponibles de cada tipo, buscamos el número de soluciones enteras no negativas para la ecuación:
   $$x_1 + x_2 + x_3 = 7$$
   donde $x_1, x_2, x_3 \ge 0$.

2. **Aplicación de la fórmula:**
   El número de maneras de elegir $k$ elementos de $n$ tipos diferentes (con repetición) está dado por la fórmula:
   $$\binom{n + k - 1}{k}$$
   En este caso, tenemos $n = 3$ tipos de muffins y queremos elegir $k = 7$ muffins.

3. **Cálculo:**
   Sustituyendo los valores en la fórmula, obtenemos:
   $$\binom{3 + 7 - 1}{7} = \binom{9}{7}$$
   Por simetría de los coeficientes binomiales, sabemos que $\binom{9}{7} = \binom{9}{2}$:
   $$\binom{9}{2} = \frac{9 \times 8}{2 \times 1} = 36$$

\boxed{36}