## Solución

**Paso 1: Solo importa el orden cíclico.**

Como los seis puntos se eligen de manera independiente y uniforme sobre la circunferencia, por simetría rotacional todo lo que determina si las cuerdas se cortan es el **orden cíclico** de las etiquetas $P, Q, R, S, T, U$ alrededor del círculo. Fijamos $P$ en la posición 1; las 5 posiciones restantes se reparten entre las demás etiquetas de forma equiprobable, dando $5! = 120$ órdenes cíclicos posibles.

**Paso 2: Condición para que dos cuerdas se corten.**

Dos cuerdas $AB$ y $CD$ se cortan en el interior del círculo si y solo si sus extremos se **alternan** alrededor de la circunferencia; equivalentemente, $C$ y $D$ deben quedar en arcos opuestos determinados por $A$ y $B$.

**Paso 3: Posición de $Q$.**

Si $Q$ ocupa la posición $k$ (con $P$ en la posición 1), la cuerda $PQ$ divide las otras cuatro posiciones en dos arcos de tamaños $k-2$ y $6-k$. Para que tanto $RS$ como $TU$ corten a $PQ$, cada arco debe contener un extremo de cada pareja, así que cada arco necesita al menos 2 puntos:

$$k - 2 \ge 2 \quad\text{y}\quad 6 - k \ge 2 \implies k = 4.$$

Es decir, $Q$ debe estar «diametralmente opuesto» a $P$, con los arcos $\{2,3\}$ y $\{5,6\}$ de dos posiciones cada uno. Esto ocurre con probabilidad $\tfrac{1}{5}$.

**Paso 4: Contar los órdenes favorables en los arcos.**

Con $P$ en 1 y $Q$ en 4, asignamos $R,S,T,U$ a las posiciones $2,3,5,6$ ($4! = 24$ maneras). Se necesita además que $RS$ corte a $TU$, es decir, que $R,S,T,U$ se alternen. En el ciclo de posiciones $2 \to 3 \to 5 \to 6$, los pares opuestos son $\{2,5\}$ y $\{3,6\}$; la alternancia exige que $R$ y $S$ ocupen posiciones opuestas:

- posiciones de $\{R,S\}$: $(2,5)$ o $(3,6)$, en cualquiera de los dos órdenes $\Rightarrow 4$ maneras,
- $T$ y $U$ llenan las dos posiciones restantes $\Rightarrow 2$ maneras.

Total favorable: $4 \times 2 = 8$ órdenes de $24$, es decir, probabilidad $\tfrac{1}{3}$.

**Paso 5: Probabilidad total.**

$$\Pr = \frac{1}{5} \cdot \frac{1}{3} = \frac{8}{120} = \frac{1}{15}.$$

$$\boxed{\dfrac{1}{15}}$$