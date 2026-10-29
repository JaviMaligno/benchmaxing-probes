## Planteamiento

En un cubo $3\times3\times3$ las 27 posiciones se clasifican por el conjunto de caras grandes donde son visibles:

- **8 esquinas**: visibles en 3 caras (tres caras mutuamente adyacentes),
- **12 aristas**: visibles en 2 caras (dos caras adyacentes),
- **6 centros de cara**: visibles en 1 cara,
- **1 centro**: visible en 0 caras.

Si $S_1, S_2$ son los conjuntos de caras de los dos cubos rojos, necesitamos $|S_1\cup S_2| = 4$. Las combinaciones posibles de tamaños $(|S_1|,|S_2|)$ con solapamiento adecuado son:

**Caso 1: esquina + esquina con 2 caras comunes.** Dos esquinas comparten exactamente 2 caras cuando son adyacentes, es decir, están unidas por una arista del cubo: $\;12$ pares.

**Caso 2: esquina + arista con exactamente 1 cara común.** Para una esquina con caras $\{x^+,y^+,z^+\}$: elegimos la cara compartida (3 formas), digamos $x^+$; la otra cara de la arista debe estar en $\{x^-,y^-,z^-\}$ y ser adyacente a $x^+$, o sea $y^-$ o $z^-$ (2 formas). Son $3\cdot2=6$ aristas por esquina:
$$8\cdot 6 = 48.$$

**Caso 3: esquina + centro de cara disjuntos.** La esquina cubre 3 caras; el centro debe estar en una de las otras 3:
$$8\cdot 3 = 24.$$

**Caso 4: arista + arista con conjuntos disjuntos.** Fijada una arista con caras $\{x^+,y^+\}$, las aristas disjuntas usan dos caras adyacentes de $\{x^-,y^-,z^+,z^-\}$: $\binom{4}{2}-1=5$ (se descarta el par opuesto $z^+,z^-$). Luego
$$\frac{12\cdot 5}{2} = 30.$$

(Los pares con centro del cubo, o arista+centro de cara, dan a lo más 3 caras, así que no aportan.)

## Total

$$12 + 48 + 24 + 30 = 114$$

\boxed{114}