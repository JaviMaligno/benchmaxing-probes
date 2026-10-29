## Planteamiento

Numeremos las casillas $(f,c)$ con $f=1$ abajo y $c=1$ a la izquierda. Kevin parte de $(1,1)$ y quiere llegar a $(3,3)$.

**Conteo total.** Quedan fijas $(1,1)$ y $(3,3)$, así que los 4 nenúfares que se quitan salen de los 7 restantes:
$$\binom{7}{4} = 35.$$

**Casos en que sí puede llegar.** Tras quitar 4 de los 9, sobreviven exactamente 5 nenúfares: $(1,1)$, $(3,3)$ y 3 más. Cualquier camino de $(1,1)$ a $(3,3)$ necesita al menos 4 pasos (hay que avanzar 2 en horizontal y 2 en vertical), es decir al menos 5 casillas distintas. Como solo hay 5 disponibles, el camino debe usarlas todas y ser monótono (solo derecha y arriba).

Los caminos monótonos son $\binom{4}{2}=6$, y cada uno determina un conjunto distinto de 3 casillas intermedias:

- $\{(1,2),(1,3),(2,3)\}$
- $\{(1,2),(2,2),(2,3)\}$
- $\{(1,2),(2,2),(3,2)\}$
- $\{(2,1),(2,2),(2,3)\}$
- $\{(2,1),(2,2),(3,2)\}$
- $\{(2,1),(3,1),(3,2)\}$

Los 6 conjuntos son diferentes, así que hay exactamente 6 configuraciones conexas.

**Resultado.** $35 - 6 = 29$.

\boxed{29}