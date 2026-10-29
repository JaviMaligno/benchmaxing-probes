Voy a razonar el problema paso a paso.

**Paso 1: Entender la estructura del problema**

Tenemos un 8960-gono regular. Queremos dividirlo en paralelogramos que no se superpongan. Algunos de estos paralelogramos son rectángulos, y queremos minimizar el número $R$ de rectángulos.

**Paso 2: Observación clave sobre los lados**

Un 8960-gono regular tiene 8960 lados. Los lados vienen en pares de lados paralelos: en un polígono regular con $n$ lados, cada lado tiene exactamente un lado paralelo (el lado opuesto cuando $n$ es par). Como $8960$ es par, hay $8960/2 = 4480$ pares de lados paralelos.

**Paso 3: Direcciones de los lados**

Los lados de un $n$-gono regular apuntan en $n$ direcciones distintas. Para $n = 8960$, hay 8960 direcciones de lados. Cada dirección tiene un lado paralelo en la dirección opuesta (a 180°), así que hay $4480$ direcciones no orientadas distintas.

**Paso 4: Propiedad de los paralelogramos en la subdivisión**

En cualquier subdivisión de un polígono en paralelogramos, cada paralelogramo tiene lados paralelos a dos de las direcciones de los lados del polígono original. Esto se debe a que los lados de los paralelogramos deben ser paralelos a los lados del polígono (o a combinaciones de ellos), y en una subdivisión por paralelogramos, las direcciones de los lados de los paralelogramos provienen de las direcciones de los lados del polígono.

**Paso 5: Condición para que un paralelogramo sea rectángulo**

Un paralelogramo es un rectángulo si y solo si sus dos direcciones de lados son perpendiculares entre sí.

**Paso 6: Direcciones perpendiculares en un polígono regular**

En un $n$-gono regular, dos direcciones de lados son perpendiculares si difieren en un ángulo de $90°$. El ángulo entre lados consecutivos es $360°/n = 360°/8960$. Para que dos lados sean perpendiculares, necesitamos que la diferencia de ángulos sea $90° = 360°/4$, lo que corresponde a $n/4 = 8960/4 = 2240$ lados de separación.

Como $8960$ es divisible por 4, sí existen pares de direcciones perpendiculares.

**Paso 7: El argumento de minimización**

La idea clave es que en una subdivisión en paralelogramos, cada paralelogramo "conecta" dos pares de lados paralelos del polígono. Un paralelogramo no rectangular usa dos direcciones no perpendiculares, mientras que un rectángulo usa dos direcciones perpendiculares.

Para minimizar el número de rectángulos, queremos emparejar las direcciones de manera que evitemos pares perpendiculares tanto como sea posible.

**Paso 8: Emparejamiento de direcciones**

Tenemos 4480 direcciones no orientadas. Queremos agruparlas en pares (cada paralelogramo usa dos direcciones). Un rectángulo aparece cuando un par consiste en dos direcciones perpendiculares.

Las direcciones perpendiculares forman pares: la dirección $\theta$ es perpendicular a $\theta + 90°$. En términos de las 4480 direcciones no orientadas, cada dirección tiene una dirección perpendicular única.

**Paso 9: Contar los pares perpendiculares inevitables**

Las 4480 direcciones no orientadas se pueden dividir en 2240 pares de direcciones perpendiculares (cada dirección $\theta$ con $\theta + 90°$).

Si queremos evitar rectángulos, necesitaríamos emparejar cada dirección con una dirección no perpendicular. Pero esto es un problema de emparejamiento: ¿podemos emparejar las 4480 direcciones en 2240 pares, ninguno de los cuales sea un par perpendicular?

**Paso 10: Análisis del emparejamiento**

Consideremos el grafo donde los vértices son las 4480 direcciones y las aristas conectan direcciones no perpendiculares. Queremos un emparejamiento perfecto en este grafo.

Cada dirección es perpendicular a exactamente una otra dirección. Así que cada vértice tiene grado $4480 - 1 - 1 = 4478$ (todas las direcciones excepto sí misma y su perpendicular).

Por el teorema de Dirac (o simplemente porque el grafo es muy denso), existe un emparejamiento perfecto que evita todos los pares perpendiculares. Esto significa que **podemos tener $R = 0$ rectángulos**.

**Paso 11: Verificación de la construcción**

¿Es realmente posible? Necesitamos construir una subdivisión real del 8960-gono en paralelogramos donde ningún paralelogramo sea un rectángulo.

La construcción estándar: tomamos el polígono regular y lo subdividimos usando paralelogramos cuyos lados son paralelos a pares de lados no perpendiculares del polígono. Como podemos emparejar las direcciones evitando perpendiculares, y la subdivisión en paralelogramos es posible (por ejemplo, mediante una triangulación refinada o una construcción explícita), obtenemos $R = 0$.

**Paso 12: Conclusión**

El mínimo posible de $R$ es 0.

Sin embargo, debo verificar esto más cuidadosamente. En problemas de este tipo (como el conocido problema de subdividir un polígono regular en paralelogramos), hay un resultado que dice que el número de rectángulos está relacionado con la estructura de las direcciones.

**Reconsideración:**

En realidad, hay una sutileza. En una subdivisión de un polígono en paralelogramos, los lados de los paralelogramos deben ser paralelos a los lados del polígono. Además, hay un resultado conocido: si un polígono se subdivide en paralelogramos, entonces el número de paralelogramos con un par dado de direcciones está determinado por la geometría.

Para un polígono regular con $n$ lados, la subdivisión en paralelogramos más natural usa todas las direcciones. El número mínimo de rectángulos resulta ser $n/4$ cuando $n$ es divisible por 4.

**Argumento más riguroso:**

En una subdivisión en paralelogramos de un polígono, consideremos las "franjas" (strips) de paralelogramos que comparten una dirección. Cada dirección de lado del polígono debe ser "cubierta" por franjas de paralelogramos.

Un resultado clave (debido a trabajos sobre teselaciones de polígonos por paralelogramos) establece que para un polígono regular de $n$ lados, el número mínimo de rectángulos en cualquier subdivisión por paralelogramos es exactamente $n/4$ cuando $4 \mid n$.

La razón es que las direcciones perpendiculares forman "cruces" que fuerzan la aparición de rectángulos. Específicamente, si consideramos las $n$ direcciones de los lados, y las agrupamos en clases de paralelismo (cada clase tiene 2 lados), obtenemos $n/2$ direcciones. Las direcciones perpendiculares vienen en pares, y hay $n/4$ pares de direcciones perpendiculares.

En cualquier subdivisión por paralelogramos, cada par de direcciones perpendiculares debe aparecer en al menos un paralelogramo (un rectángulo), porque las franjas correspondientes a direcciones perpendiculares deben intersecarse, y su intersección es un rectángulo.

Por lo tanto, $R \geq n/4 = 8960/4 = 2240$.

Y esta cota es alcanzable mediante una construcción adecuada.

**Conclusión final:**

El mínimo posible de $R$ es $2240$.

\boxed{2240}