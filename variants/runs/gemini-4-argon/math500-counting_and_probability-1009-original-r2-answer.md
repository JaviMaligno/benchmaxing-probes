Para encontrar el número de selecciones diferentes de seis galletas, podemos plantear el problema como el número de combinaciones con repetición (método de barras y estrellas).

1. **Definir las variables:**
   Sean $x_1$, $x_2$ y $x_3$ la cantidad de galletas con chispas de chocolate, de avena y de mantequilla de maní que Pat selecciona, respectivamente.

2. **Plantear la ecuación:**
   Como Pat selecciona un total de 6 galletas y hay al menos 6 de cada tipo disponibles en la bandeja, buscamos el número de soluciones enteras no negativas para la ecuación:
   $$x_1 + x_2 + x_3 = 6$$
   donde $x_1, x_2, x_3 \ge 0$.

3. **Aplicar la fórmula de combinaciones con repetición:**
   El número de soluciones enteras no negativas para $x_1 + x_2 + \dots + x_n = k$ está dado por la fórmula:
   $$\binom{n + k - 1}{k}$$
   En este caso, tenemos $n = 3$ tipos de galletas y $k = 6$ galletas por elegir:
   $$\binom{3 + 6 - 1}{6} = \binom{8}{6}$$

4. **Calcular el resultado:**
   $$\binom{8}{6} = \binom{8}{2} = \frac{8 \times 7}{2 \times 1} = 28$$

\boxed{28}