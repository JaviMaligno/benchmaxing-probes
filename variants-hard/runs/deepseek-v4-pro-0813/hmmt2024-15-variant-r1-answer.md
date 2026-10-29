Voy a razonar el problema paso a paso.

## Entender el problema

- Hay $12$ pueblos.
- Cada pueblo está unido por **exactamente una carretera** a **exactamente $3$** otros pueblos.
- Para cualquier par de pueblos distintos, el número de pueblos unidos a **ambos** es **exactamente $0$ o exactamente $2$**.

Esto significa que el grafo es $3$-regular con $12$ vértices, y cada par de vértices tiene $0$ o $2$ vecinos comunes.

Recordemos la notación: un grafo $3$-regular con la propiedad de que cada pareja de vértices tiene $0$ o $2$ vecinos comunes se denomina **grafo fuertemente regular** con parámetros $(12, 3, \lambda, \mu)$, donde $\lambda$ es el número de vecinos comunes de parejas adyacentes y $\mu$ el de parejas no adyacentes. Aquí $\lambda, \mu \in \{0, 2\}$.

## Posibilidades para $\lambda$ y $\mu$

Sea $G$ un grafo fuertemente regular con $v = 12$, grado $k = 3$. Para un grafo fuertemente regular $(v, k, \lambda, \mu)$, se cumple la identidad:

$$
k(k - \lambda - 1) = (v - k - 1)\mu.
$$

Sustituyendo $v = 12$, $k = 3$:

$$
3(3 - \lambda - 1) = (12 - 3 - 1)\mu,
$$

es decir,

$$
3(2 - \lambda) = 8\mu.
$$

Como $\lambda, \mu \in \{0, 2\}$:

- Si $\mu = 0$, entonces $3(2-\lambda)=0$, luego $\lambda = 2$. Esto corresponde al grafo totalmente disconexo salvo componentes, pero con grado $3$ y $\mu=0$ implicaría que cada componente es un $K_4$? Veamos: $\mu = 0$ significa que no hay dos vértices no adyacentes con un vecino común, y $\lambda = 2$ significa que dos vértices adyacentes tienen exactamente $2$ vecinos comunes. Eso da $K_4$ como componente, lo cual no conecta las $12$ ciudades (serían 3 copias de $K_4$). Esto satisface la condición, porque cada ciudad tiene exactamente $3$ vecinos, pero para un par de ciudades de componentes distintas hay $0$ vecinos comunes, y para un par dentro de un $K_4$ hay $2$ vecinos comunes. ¡Sí cumple las condiciones! Entonces esto es válido.

- Si $\mu = 2$, entonces $3(2-\lambda)=16$, lo cual no tiene solución entera para $\lambda$. Por tanto, $\mu = 2$ es imposible.

Así que la única posibilidad es $\lambda = 2$, $\mu = 0$, es decir, el grafo es la unión disjunta de $12/4 = 3$ copias del grafo completo $K_4$.

## Contar maneras de construirlo

Queremos contar el número de formas de particionar las $12$ ciudades en $3$ grupos de $4$ ciudades, y dentro de cada grupo unir cada par de ciudades con una carretera. Como las carreteras son no dirigidas y cada grupo de $4$ tiene $\binom{4}{2}=6$ carreteras, la red queda determinada por la partición.

El número de formas de particionar $12$ elementos distinguibles en $3$ bloques no ordenados de tamaño $4$ es:

$$
\frac{\binom{12}{4}\binom{8}{4}\binom{4}{4}}{3!}.
$$

Calculamos:

$$
\binom{12}{4} = 495,\quad \binom{8}{4} = 70,\quad \binom{4}{4} = 1.
$$

Producto:

$$
495 \cdot 70 = 34\,650.
$$

Dividimos entre $3! = 6$:

$$
\frac{34\,650}{6} = 5\,775.
$$

## Verificación

Cada partición da exactamente un conjunto de carreteras. Las condiciones:

- Cada ciudad tiene grado $3$: en un $K_4$ cada vértice está unido a los otros $3$.
- Para cualquier par de ciudades:
  - Si están en el mismo bloque, tienen $2$ vecinos comunes (los otros dos del bloque).
  - Si están en bloques distintos, no comparten vecinos, pues cada bloque es cerrado.

Por tanto, todas y cada una de las $5\,775$ particiones cumplen las condiciones, y no hay otras configuraciones posibles.

La respuesta final es:

\[
\boxed{5775}
\]