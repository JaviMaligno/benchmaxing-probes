Para encontrar el número de formas de ensamblar los cubos unitarios bajo las condiciones dadas (considerando las rotaciones y reflexiones como distintas), basta con elegir $2$ de las $27$ posiciones fijas en el cubo de $3 \times 3 \times 3$ para colocar los $2$ cubos azules.

Primero, clasificamos las $27$ posiciones del cubo de $3 \times 3 \times 3$ según el número de caras exteriores en las que sería visible un cubo colocado en dicha posición:

1. **Centro interior ($I$):** $1$ posición (en el centro absoluto del cubo). Es visible en $0$ caras.
2. **Centros de cara ($F$):** $6$ posiciones (una en el centro de cada cara). Cada una es visible en $1$ cara.
3. **Centros de arista ($E$):** $12$ posiciones (una en el punto medio de cada arista). Cada una es visible en $2$ caras adyacentes.
4. **Esquinas ($C$):** $8$ posiciones (una en cada vértice). Cada una es visible en $3$ caras mutuamente adyacentes.

Para cualquier posición $P$, sea $V(P)$ el conjunto de caras del cubo grande en las que $P$ es visible. Buscamos el número de pares de posiciones $\{P_1, P_2\}$ tales que $|V(P_1) \cup V(P_2)| = 3$. 

Usando la fórmula $|V(P_1) \cup V(P_2)| = |V(P_1)| + |V(P_2)| - |V(P_1) \cap V(P_2)| = 3$, analizamos todos los casos posibles según los tipos de posiciones elegidas:

* **Caso 1: Una esquina ($C$) y el centro interior ($I$)**
  Aquí $|V(P_1)| = 3$ y $|V(P_2)| = 0$. Su unión siempre tiene $3$ caras.
  $$\text{Formas} = 8 \times 1 = 8$$

* **Caso 2: Una esquina ($C$) y un centro de cara ($F$)**
  Aquí $|V(P_1)| = 3$ y $|V(P_2)| = 1$. Para que la unión tenga exactamente $3$ caras, necesitamos que $|V(P_1) \cap V(P_2)| = 1$; es decir, la cara de $F$ debe ser una de las $3$ caras que comparten la esquina $C$.
  $$\text{Formas} = 8 \times 3 = 24$$

* **Caso 3: Una esquina ($C$) y un centro de arista ($E$)**
  Aquí $|V(P_1)| = 3$ y $|V(P_2)| = 2$. Necesitamos que $|V(P_1) \cap V(P_2)| = 2$, lo que significa que las $2$ caras de la arista $E$ deben estar entre las $3$ caras de la esquina $C$ (es decir, $E$ es una de las $3$ aristas incidentes en la esquina $C$).
  $$\text{Formas} = 8 \times \binom{3}{2} = 8 \times 3 = 24$$

* **Caso 4: Dos esquinas ($C$ y $C$)**
  Aquí $|V(P_1)| = 3$ y $|V(P_2)| = 3$. Para que la unión tuviera tamaño $3$, ambas esquinas tendrían que compartir las mismas $3$ caras, lo cual es imposible para dos esquinas distintas.
  $$\text{Formas} = 0$$

* **Caso 5: Dos centros de arista ($E$ y $E$)**
  Aquí $|V(P_1)| = 2$ y $|V(P_2)| = 2$. Necesitamos que $|V(P_1) \cap V(P_2)| = 1$, es decir, que las dos aristas compartan exactamente $1$ cara. Cada arista pertenece a $2$ caras, y en cada una de esas caras hay otras $3$ aristas (además, dos aristas distintas nunca comparten $2$ caras). Por lo tanto, cada una de las $12$ aristas comparte exactamente una cara con $2 \times 3 = 6$ otras aristas.
  $$\text{Formas} = \frac{12 \times 6}{2} = 36$$

* **Caso 6: Un centro de arista ($E$) y un centro de cara ($F$)**
  Aquí $|V(P_1)| = 2$ y $|V(P_2)| = 1$. Necesitamos que $|V(P_1) \cap V(P_2)| = 0$, lo que significa que el centro de cara $F$ no debe pertenecer a ninguna de las $2$ caras de la arista $E$. Para cada una de las $12$ aristas, quedan $6 - 2 = 4$ centros de cara válidos.
  $$\text{Formas} = 12 \times 4 = 48$$

* **Otros casos:** Cualquier otra combinación ($E$ con $I$, $F$ con $F$, $F$ con $I$) tiene $|V(P_1)| + |V(P_2)| \le 2$, por lo que es imposible alcanzar $3$ caras.

Sumando todos los casos posibles, obtenemos el total de formas:
$$8 + 24 + 24 + 0 + 36 + 48 = 140$$

\boxed{140}