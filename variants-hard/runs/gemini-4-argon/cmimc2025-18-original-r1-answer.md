Para encontrar el valor mínimo posible de $R$, analicemos las direcciones de los lados de los paralelogramos en cualquier disección de un polígono regular de $8960$ lados.

1. **Direcciones de los lados del polígono:**
   Un polígono regular de $2n = 8960$ lados tiene $n = 4480$ pares de lados opuestos paralelos. Llamemos $d_1, d_2, \dots, d_{4480}$ a las direcciones de estos $4480$ pares de lados, ordenadas según su ángulo:
   $$\theta_i = \frac{(i-1)\pi}{4480}, \quad \text{para } i = 1, 2, \dots, 4480.$$

2. **Bandas (o caminos) de paralelogramos:**
   Para cada dirección $d_i$, consideremos el conjunto de todos los paralelogramos de la disección que tienen un par de lados paralelos a $d_i$. Dado que cada lado interno en la dirección $d_i$ es compartido por paralelogramos adyacentes que también tienen lados en la dirección $d_i$, estos paralelogramos forman al menos una banda (o camino continuo) que conecta los dos lados opuestos del $8960$-ágono que tienen la dirección $d_i$.

3. **Intersección de bandas:**
   Para cualesquiera dos direcciones distintas $d_i$ y $d_j$, los dos lados opuestos del polígono con dirección $d_i$ se alternan en el borde del polígono con los dos lados opuestos de dirección $d_j$. Por continuidad (teorema de la curva de Jordan), la banda que conecta los lados de dirección $d_i$ y la banda que conecta los lados de dirección $d_j$ deben cruzarse en el interior del polígono.
   Como los paralelogramos no se superponen, su intersección debe contener al menos un paralelogramo de la disección que pertenezca a ambas bandas; es decir, un paralelogramo cuyos lados son paralelos a $d_i$ y $d_j$.

4. **Pares de direcciones perpendiculares:**
   Como $4480$ es par, las $4480$ direcciones se pueden agrupar en $k = \frac{4480}{2} = 2240$ pares de direcciones mutuamente perpendiculares: $(d_i, d_{i+2240})$ para $i = 1, 2, \dots, 2240$, ya que:
   $$\theta_{i+2240} - \theta_i = \frac{2240\pi}{4480} = \frac{\pi}{2}.$$
   Para cada uno de estos $2240$ pares, el paralelogramo en la intersección de las bandas correspondientes a $d_i$ y $d_{i+2240}$ tiene lados perpendiculares, por lo que es un **rectángulo**. Como los $2240$ pares de direcciones son disjuntos entre sí, estos $2240$ rectángulos son todos distintos. Por lo tanto, $R \ge 2240$.

5. **Construcción del mínimo:**
   En el teselado estándar de un $2n$-ágono regular (un zonógono) mediante $\binom{n}{2}$ rombos, existe exactamente un rombo por cada par de direcciones $\{d_i, d_j\}$. En dicho teselado, únicamente los $2240$ pares de direcciones perpendiculares forman rectángulos (cuadrados), alcanzándose la cota $R = 2240$.

\boxed{2240}