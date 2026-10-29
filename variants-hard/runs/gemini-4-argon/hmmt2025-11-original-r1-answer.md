Para determinar el número de formas de colocar los números $1, 2, 3, 4, 5, 6$ y $7$ alrededor de un círculo de modo que el producto de cada par de números adyacentes sea a lo sumo $20$, analizamos las adyacencias permitidas para los números más grandes:

1. **Vecinos del $7$:**
   Los únicos productos con $7$ que no superan $20$ son $7 \times 1 = 7$ y $7 \times 2 = 14$ (ya que $7 \times 3 = 21 > 20$). Por lo tanto, el $7$ debe ser adyacente obligatoriamente al $1$ y al $2$, formando el bloque fijo $1 - 7 - 2$.

2. **Camino restante entre $1$ y $2$:**
   Los cuatro números restantes $\{3, 4, 5, 6\}$ deben formar un camino entre el $1$ y el $2$. Analizamos qué conexiones son posibles entre $\{4, 5, 6\}$:
   - $6 \times 4 = 24 > 20$ y $6 \times 5 = 30 > 20$, por lo que el $6$ solo puede ser adyacente a elementos de $\{1, 2, 3\}$.
   - $4 \times 5 = 20 \le 20$, por lo que el $4$ y el $5$ sí pueden ser adyacentes entre sí, además de poder conectarse con $\{1, 2, 3\}$.

3. **Estructura del camino de $1$ a $2$:**
   El camino desde $1$ hasta $2$ tiene cuatro posiciones internas para $\{3, 4, 5, 6\}$. 
   - Si $4$ y $5$ no fueran adyacentes, entonces ningún par del conjunto $\{4, 5, 6\}$ podría ser adyacente entre sí. Sin embargo, es imposible colocar $3$ elementos en $4$ posiciones consecutivas sin que al menos dos de ellos queden juntos. Por lo tanto, $4$ y $5$ **deben ser adyacentes**, formando un bloque $\{4, 5\}$.
   - Como el $6$ y el bloque $\{4, 5\}$ no pueden ser adyacentes entre sí, el número $3$ debe situarse necesariamente en medio de ambos para separarlos.

   Así, la estructura del camino entre $1$ y $2$ debe ser de la forma:
   $$1 - 6 - 3 - \{4, 5\} - 2 \quad \text{o} \quad 1 - \{4, 5\} - 3 - 6 - 2$$
   Todos los productos en estas configuraciones cumplen la condición ($1 \times 6 = 6$, $6 \times 3 = 18$, $3 \times 4 = 12$, $3 \times 5 = 15$, $4 \times 5 = 20$, $4 \times 2 = 8$, $5 \times 2 = 10$).

4. **Conteo total de disposiciones:**
   - Hay $2$ formas de elegir de qué lado del $3$ va el $6$ (junto al $1$ o junto al $2$, lo que equivale a reflejar el ciclo).
   - Hay $2$ formas de ordenar internamente el bloque $\{4, 5\}$ ($4 - 5$ o $5 - 4$).
   - Esto produce $2 \times 2 = 4$ ciclos dirigidos (donde las reflexiones ya se cuentan por separado).
   - Como las rotaciones también cuentan como disposiciones diferentes, hay $7$ posiciones posibles para ubicar el número $7$ en el círculo.

Multiplicando las opciones, obtenemos:
$$4 \times 7 = 28$$

\boxed{28}