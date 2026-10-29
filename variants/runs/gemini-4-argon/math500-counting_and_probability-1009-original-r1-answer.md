Para determinar cuántos surtidos diferentes de seis galletas se pueden seleccionar, podemos plantear el problema como una combinación con repetición (método de barras y estrellas).

1. **Definir las variables:**
   Sean $x_1$, $x_2$ y $x_3$ la cantidad de galletas de chispas de chocolate, de avena y de mantequilla de maní que selecciona Pat, respectivamente.

2. **Plantear la ecuación:**
   Como Pat selecciona un total de 6 galletas y hay al menos 6 de cada tipo disponibles, buscamos el número de soluciones enteras no negativas para la ecuación:
   $$x_1 + x_2 + x_3 = 6$$
   donde $x_1 \ge 0$, $x_2 \ge 0$ y $x_3 \ge 0$.

3. **Aplicar la fórmula de combinaciones con repetición:**
   El número de maneras de elegir $n = 6$ elementos de $k = 3$ tipos diferentes está dado por:
   $$\binom{n + k - 1}{k - 1} = \binom{6 + 3 - 1}{3 - 1} = \binom{8}{2}$$

4. **Calcular el resultado:**
   $$\binom{8}{2} = \frac{8 \times 7}{2 \times 1} = 28$$

\boxed{28}