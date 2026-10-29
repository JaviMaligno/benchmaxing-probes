**Respuesta: 153.**

Razonamiento:

Los segmentos de igual longitud en un 28-ágono regular son cuerdas con el mismo "paso" $k$ (que unen vértices $i$ e $i+k \pmod{28}$), con $k \in \{1, \dots, 14\}$. Para cada $k$ fijo, cuento los emparejamientos perfectos del grafo cuyas aristas son esas cuerdas.

**Caso $k = 14$ (diámetros):** cada vértice se une con su opuesto; hay exactamente **1** forma.

**Caso $1 \le k \le 13$:** el grafo es unión disjunta de $d = \gcd(28, k)$ ciclos, cada uno de longitud $28/d$. Un ciclo tiene emparejamiento perfecto solo si su longitud es par, y en ese caso tiene exactamente 2. Por tanto hay $2^d$ emparejamientos si $28/d$ es par, y $0$ si es impar:

- $k = 1, 3, 5, 9, 11, 13$: $d = 1$, ciclo de longitud 28 (par) → $2$ cada uno, total $12$.
- $k = 2, 6, 10$: $d = 2$, ciclos de longitud 14 (par) → $2^2 = 4$ cada uno, total $12$.
- $k = 4, 8, 12$: $d = 4$, ciclos de longitud 7 (impar) → $0$.
- $k = 7$: $d = 7$, ciclos de longitud 4 (par) → $2^7 = 128$.

**Suma total:** $12 + 12 + 0 + 128 + 1 = 153$.

$$\boxed{153}$$