## Planteamiento

Buscamos grafos con 8 vértices, 3-regulares (cada ciudad conecta con exactamente 3 otras), donde cada par de vértices distintos tiene exactamente 0 o 2 vecinos comunes.

## Identificación de los grafos posibles

**Caso 1: el grafo es disconexo.** Como es 3-regular, cada componente tiene al menos 4 vértices, así que hay dos componentes de 4 vértices cada una, y cada una debe ser $K_4$. Verificación: dos vértices adyacentes en el mismo $K_4$ tienen exactamente 2 vecinos comunes; dos vértices en componentes distintas tienen 0. ✓

**Caso 2: el grafo es conexo.** Supongamos que dos vértices adyacentes $u, v$ tienen 2 vecinos comunes; eso crea triángulos, y un análisis de los grados fuerza rápidamente una contradicción con la 3-regularidad y la condición "0 o 2" en los demás pares (los vértices restantes no pueden completar sus vecindades sin producir pares con exactamente 1 vecino común). Por tanto el grafo es libre de triángulos: todo par adyacente tiene 0 vecinos comunes, y los pares a distancia 2 tienen exactamente 2 vecinos comunes.

Tomemos un vértice $v$ con vecinos $a, b, c$. Cada par de $\{a,b,c\}$ tiene a $v$ como vecino común, luego necesita exactamente otro vecino común. Los vecinos restantes de $a, b, c$ caen en los 4 vértices lejanos. Siguiendo las restricciones, cada par de $\{a,b,c\}$ comparte exactamente un vecino lejano distinto, y la estructura que resulta es el **grafo del cubo $Q_3$** (equivalentemente, $K_{4,4}$ menos un emparejamiento perfecto). Verificación en $Q_3$: vértices adyacentes tienen 0 vecinos comunes, vértices a distancia 2 tienen exactamente 2, y vértices antipodales tienen 0. ✓

## Conteo de etiquetados

**Dos copias de $K_4$:** basta elegir qué 4 ciudades forman el primer $K_4$, dividiendo entre 2 por la simetría entre los dos grupos:
$$\frac{1}{2}\binom{8}{4} = 35.$$

**Grafo del cubo $Q_3$:** el número de copias etiquetadas es $\dfrac{8!}{|\mathrm{Aut}(Q_3)|}$. El grupo de automorfismos del cubo tiene orden $48$, así que:
$$\frac{40320}{48} = 840.$$

## Total

$$35 + 840 = 875.$$

$$\boxed{875}$$