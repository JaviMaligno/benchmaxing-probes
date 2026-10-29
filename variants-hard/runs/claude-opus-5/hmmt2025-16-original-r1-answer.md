## Planteamiento

En una cuadrícula de $5\times 5$ hay $6$ rectas verticales y $6$ horizontales. Un rectángulo queda determinado por dos rectas verticales y dos horizontales:

$$\binom{6}{2}^2 = 15 \cdot 15 = 225 \text{ rectángulos.}$$

**Condición de no solapamiento:** si $R_1=[a,b]\times[p,q]$ y $R_2=[c,d]\times[r,s]$, los rectángulos cerrados son disjuntos (ni interiores, ni aristas, ni vértices en común) si y solo si los intervalos en $x$ son disjuntos **o** los intervalos en $y$ son disjuntos.

## Conteo (pares ordenados)

**Intervalos disjuntos en una dimensión:** elegir $4$ rectas distintas de las $6$ determina de forma única $a<b<c<d$, es decir, un par de intervalos separados $[a,b]$, $[c,d]$. Hay $\binom{6}{4}=15$ pares no ordenados, o sea $30$ ordenados.

Sea $A$ = "disjuntos en $x$" y $B$ = "disjuntos en $y$":

- $|A| = 30 \cdot 225 = 6750$ (coordenadas $y$ libres)
- $|B| = 225 \cdot 30 = 6750$
- $|A\cap B| = 30 \cdot 30 = 900$

Por inclusión-exclusión:

$$|A\cup B| = 6750 + 6750 - 900 = 12600.$$

## Pares no ordenados

$$\frac{12600}{2} = 6300.$$

\boxed{6300}