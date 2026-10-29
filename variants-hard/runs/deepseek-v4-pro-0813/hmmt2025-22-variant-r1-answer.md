Voy a razonar el problema paso a paso.

Sea la caverna de altura $h$. Las estalactitas cuelgan del techo, así que sus puntas están a alturas:

- Estalactita de 18: punta a altura $h - 18$
- Estalactita de 34: punta a altura $h - 34$

Las estalagmitas suben del suelo, así que sus puntas están a alturas:

- Estalagmita de 25: punta a altura $25$
- Estalagmita de 47: punta a altura $47$

Los cuatro vértices del cuadrado son estos cuatro puntos. Como el suelo y el techo son paralelos, las posiciones de estas formaciones se proyectan verticalmente. Las cuatro puntas forman un cuadrado, lo que impone que la distancia entre los puntos que están arriba y los que están abajo, combinada con las distancias horizontales, forme lados iguales y diagonales correctas.

Sea $d$ la distancia horizontal entre las dos formaciones que cuelgan del techo (las estalactitas). Igualmente, por el paralelismo, supondremos que las proyecciones sobre el techo o el suelo de las cuatro formaciones son las cuatro esquinas de un cuadrado horizontal de lado $s$. Las alturas de las puntas serán:

- $A$: estalactita de 18 → altura $h-18$
- $B$: estalactita de 34 → altura $h-34$
- $C$: estalagmita de 25 → altura $25$
- $D$: estalagmita de 47 → altura $47$

Para que los cuatro puntos formen un cuadrado, podemos pensarlo como un cuadrado con dos vértices en un plano horizontal superior y dos en uno inferior, con lados inclinados que unen los niveles. La diferencia de alturas entre una estalactita y una estalagmita vecina es constante en lados opuestos.

Consideremos el cuadrado con vértices ordenados de forma que los lados alternan entre una punta alta (estalactita) y una punta baja (estalagmita). Dado un cuadrado, los cuatro lados son iguales. Las diferencias verticales entre pares de vértices deben compensarse con diferencias horizontales.

Si el cuadrado tiene lados inclinados, la condición clave es que la diferencia de alturas a lo largo de un lado sea la misma en magnitud que a lo largo del lado opuesto, pero como el cuadrado es cerrado, las alturas deben cumplir una relación de promedio.

Una forma directa: en un cuadrado, los vectores de los lados opuestos son iguales u opuestos. Si los cuatro puntos están a alturas $a_1, a_2, a_3, a_4$, y las proyecciones horizontales forman un cuadrado, la suma de alturas de vértices opuestos es constante en un paralelogramo. De hecho, para un cuadrado (paralelogramo), los puntos medios de las diagonales coinciden. Llamemos $P_1, P_2, P_3, P_4$ a los cuatro puntos en orden cíclico. La condición de paralelogramo es:

$$
P_1 + P_3 = P_2 + P_4
$$

En componentes verticales, esto da que las sumas de las alturas de los vértices opuestos son iguales. Los dos pares de vértices opuestos son:
- Estalactita 18 y estalagmita 25, vs. estalactita 34 y estalagmita 47:

$$
(h - 18) + 25 = (h - 34) + 47
$$

Esto da:

$$
h + 7 = h + 13
$$

Lo cual es falso. Probemos otro emparejamiento: estalactita 18 con estalagmita 47, y estalactita 34 con estalagmita 25:

$$
(h-18) + 47 = (h-34) + 25
$$

$$
h + 29 = h - 9
$$

También falso. Probemos el emparejamiento de las dos estalactitas opuestas entre sí (lo cual no puede ser en un cuadrado si están en lados opuestos, pero probemos la diagonal):

Para que dos vértices opuestos sean las dos estalactitas y los otros dos las estalagmitas:

$$
(h-18) + (h-34) = 25 + 47
$$

$$
2h - 52 = 72
$$

$$
2h = 124
$$

$$
h = 62
$$

Verifiquemos las alturas:

- $h - 18 = 44$
- $h - 34 = 28$
- $25$
- $47$

Las puntas en altura: 44, 28 (estalactitas) y 25, 47 (estalagmitas). La suma de alturas de los vértices opuestos (44 y 25) sería 69, y (28 y 47) sería 75; esto no es un paralelogramo. Así que este emparejamiento no es válido como cuadrado con esos pares opuestos.

En realidad, hay que ser más cuidadoso. La condición correcta para un paralelogramo es que las diagonales se bisequen. Si los vértices opuestos son $A$ y $C$, $B$ y $D$, entonces:

$$
A + C = B + D
$$

donde la suma incluye las tres coordenadas. Las alturas deben entonces satisfacer que el promedio de las alturas de un par de vértices opuestos sea igual al promedio del otro par. Las alturas son:

- $a = h-18$
- $b = h-34$
- $c = 25$
- $d = 47$

Debemos elegir cuáles son los pares opuestos. Enumeremos los posibles emparejamientos:

1. Pares opuestos: $(a,c)$ y $(b,d)$:

   $$
   (h-18) + 25 = (h-34) + 47
   \Rightarrow h+7 = h+13
   $$

   Imposible.

2. Pares opuestos: $(a,d)$ y $(b,c)$:

   $$
   (h-18) + 47 = (h-34) + 25
   \Rightarrow h+29 = h-9
   $$

   Imposible.

3. Pares opuestos: $(a,b)$ y $(c,d)$:

   $$
   (h-18) + (h-34) = 25 + 47
   \Rightarrow 2h - 52 = 72
   \Rightarrow 2h = 124
   \Rightarrow h = 62
   $$

   Este da una solución.

Ahora, ¿por qué el caso 3 es geométricamente factible? Si h = 62, las alturas son 44, 28, 25, 47. Notemos que:

- 44 y 47 difieren en 3
- 28 y 25 difieren en 3

De modo que las dos estalactitas (44 y 28) difieren en 16 entre sí, y las dos estalagmitas (25 y 47) difieren en 22. La diferencia de alturas entre la estalactita de 44 y la estalagmita cercana de 47 es 3, igual que entre 28 y 25. Entonces si en la proyección horizontal ponemos:

- Estalactita de 44 (arriba)
- Estalagmita de 47 (abajo)
- Estalactita de 28 (arriba)
- Estalagmita de 25 (abajo)

se puede formar un cuadrado cuyos lados tengan pendiente con la misma diferencia vertical de 3.

En efecto, consideremos un cuadrado horizontal de lado $s$ en la proyección. Los lados que conectan una estalactita y una estalagmita con diferencia vertical 3 tendrán longitud:

$$
L_{\text{lado}} = \sqrt{s^2 + 3^2}
$$

Los lados que conectan las dos estalactitas (diferencia vertical 16) no serían lados, sino diagonales, y los que conectan las dos estalagmitas (diferencia vertical 22) tampoco serían lados.

Espera: si los pares opuestos son las dos estalactitas y las dos estalagmitas, entonces en el cuadrado, los lados conectan una estalactita con una estalagmita. Los lados serían 4 segmentos que van de una estalactita a una estalagmita. Las diferencias verticales de los lados deben ser todas iguales en magnitud, pero como alternan subidas y bajadas, el cuadrado en 3D es como un cuadrado "inclinado" o un rombo en perspectiva. La condición de paralelogramo ya nos asegura que los puntos medios de las diagonales coinciden.

Para h = 62, las diagonales del cuadrado serían:
- Diagonal 1: entre las dos estalactitas → diferencia vertical 16
- Diagonal 2: entre las dos estalagmitas → diferencia vertical 22

Pero en un cuadrado, las diagonales deben ser iguales y perpendiculares (en la proyección horizontal). La condición de igual longitud de las diagonales en 3D:

$$
\sqrt{s^2 + 16^2} = \sqrt{s^2 + 22^2}
$$

Esto es imposible salvo que las distancias horizontales difieran. Pero en un cuadrado, las proyecciones de las diagonales son iguales (ambas son $s\sqrt2$). Por tanto, si las diagonales reales son entre las dos estalactitas y las dos estalagmitas, sus longitudes en 3D no serían iguales a menos que 16 = 22, lo cual es falso.

Por tanto, h = 62 no produce un cuadrado. Necesitamos replantear.

El error está en asumir que las proyecciones horizontales forman un cuadrado con la misma orientación de lados. En realidad, el cuadrado está en el espacio 3D y sus lados son las distancias reales entre puntas de formaciones. La proyección horizontal no tiene por qué ser un cuadrado.

Planteemos correctamente. Llamemos a los cuatro puntos:

- $A$: punta de la estalactita de 18, altura $h-18$
- $B$: punta de la estalactita de 34, altura $h-34$
- $C$: punta de la estalagmita de 25, altura 25
- $D$: punta de la estalagmita de 47, altura 47

La altura caverna $h$ es la distancia vertical entre suelo y techo. Notemos que:

- Distancia vertical entre $A$ y $B$: $|(h-18) - (h-34)| = 16$
- Distancia vertical entre $C$ y $D$: $|47 - 25| = 22$
- Distancia vertical entre $A$ y $C$: $|(h-18) - 25| = h - 43$
- Distancia vertical entre $A$ y $D$: $|(h-18) - 47| = h - 65$
- Distancia vertical entre $B$ y $C$: $|(h-34) - 25| = h - 59$
- Distancia vertical entre $B$ y $D$: $|(h-34) - 47| = h - 81$

Para que $A, B, C, D$ sean vértices de un cuadrado, ciertos pares serán lados y ciertos pares serán diagonales. En un cuadrado, hay 4 lados iguales y 2 diagonales iguales (de longitud $\sqrt2$ veces el lado). Las longitudes reales dependen de las posiciones horizontales, que son libres salvo por el hecho de que el suelo y el techo son paralelos y las formaciones son verticales.

Como las posiciones horizontales son variables, podemos elegir que los pares que son lados tengan la misma componente vertical o la misma proyección horizontal. Pero la relación clave es que, en un cuadrado, los lados son segmentos entre vértices adyacentes. Las diferencias verticales de los lados deben ser iguales en valor absoluto o las proyecciones horizontales deben compensar.

En realidad, hay un resultado más elegante. Las cuatro puntas forman un cuadrado que podemos rotar en el espacio. Sea $\ell$ el lado del cuadrado. Los cuatro vértices pueden ordenarse cíclicamente. Consideremos las diferencias de alturas entre vértices consecutivos. Denotemos por $\delta_1, \delta_2, \delta_3, \delta_4$ estas diferencias de altura a lo largo de los lados en orden cíclico. Como es una curva cerrada, $\delta_1 + \delta_2 + \delta_3 + \delta_4 = 0$.

En un cuadrado, los lados opuestos son paralelos; por tanto, las proyecciones verticales de lados opuestos son iguales en magnitud y opuestas en signo: $\delta_3 = -\delta_1$ y $\delta_4 = -\delta_2$. Esto implica que los pares de lados opuestos tienen la misma pendiente vertical (en valor absoluto).

Entonces, las diferencias de altura entre vértices adyacentes deben emparejarse. Las diferencias de altura entre vértices del cuadrado corresponden a diferencias entre las alturas $h-18, h-34, 25, 47$.

Los pares de valores que difieren en una cantidad fija son:
- $h-18$ y $h-34$ difieren en 16
- $25$ y $47$ difieren en 22
- $h-18$ y $25$ difieren en $h-43$
- $h-18$ y $47$ difieren en $h-65$
- $h-34$ y $25$ difieren en $h-59$
- $h-34$ y $47$ difieren en $h-81$

Para que los cuatro lados del cuadrado tengan diferencias verticales que se emparejen como $(\delta, -\delta, \delta, -\delta)$ o similar, necesitamos que dos pares de alturas (adyacentes) tengan la misma diferencia vertical en valor absoluto, y los otros dos pares también.

Si intentamos usar como lados los pares con diferencias verticales fijas 16 y 22, tendríamos por ejemplo lados con diferencias verticales 16 (entre las estalactitas) y 22 (entre las estalagmitas). Pero los lados de un cuadrado deben tener todos la misma longitud real. Si un lado tiene diferencia vertical 16 y el otro 22, las proyecciones horizontales serían diferentes para mantener igual la longitud real, lo cual es posible, pero entonces los ángulos no serían rectos en general. En un cuadrado, si un lado tiene pendiente vertical $v_1$ y el lado consecutivo pendiente vertical $v_2$, la perpendicularidad implica una relación entre las proyecciones.

Alternativamente, la condición de cuadrado puede verse así: en un cuadrado, los cuatro vectores lado consecutivos suman cero y son perpendiculares entre consecutivos. La componente vertical de los lados opuestos debe ser la misma en magnitud, y las componentes horizontales deben ser las mismas en magnitud.

Sea $\vec{u}$ el vector de un lado y $\vec{v}$ el vector del lado siguiente, con $\vec{u} \perp \vec{v}$ y $|\vec{u}| = |\vec{v}| = \ell$. Las componentes verticales de $\vec{u}$ y $\vec{v}$ sumadas con sus opuestos dan las alturas.

Otra forma más simple: usemos la propiedad de que en un cuadrado, las diagonales se bisecan y son perpendiculares, y sus longitudes son iguales. Como las dos diagonales conectan pares de vértices opuestos. Los pares opuestos son dos. Las alturas de los cuatro puntos se pueden organizar de modo que las diagonales tengan vectores:

$\vec{D_1} = P_A - P_C$, $\vec{D_2} = P_B - P_D$.

En componentes verticales, $\vec{D_1}$ y $\vec{D_2}$ tienen diferencias de altura iguales a las diferencias entre $h-18$ y $25$, y entre $h-34$ y $47$, dependiendo del emparejamiento.

La perpendicularidad e igualdad de longitudes de las diagonales en el espacio implica:

- Las proyecciones horizontales de $\vec{D_1}$ y $\vec{D_2}$ son perpendiculares y de igual longitud.
- La componente vertical de $\vec{D_1}$ elevada al cuadrado más su proyección horizontal al cuadrado debe ser igual a la de $\vec{D_2}$.

Pero la componente vertical de las diagonales puede no ser igual. Si las componentes verticales de las diagonales son diferentes, las proyecciones horizontales deberán compensar para que las longitudes reales de las diagonales sean iguales. Sin embargo, las proyecciones horizontales de las diagonales de un cuadrado también deben ser perpendiculares. Esto es posible solo con ciertas condiciones.

Aprovechemos la existencia de un cuadrado en 3D. Un cuadrado en el espacio, con dos diagonales iguales y perpendiculares, cuyos vectores son $\vec{D_1}$ y $\vec{D_2}$. La condición de igual longitud:

$$
|\vec{D_1}| = |\vec{D_2}|
$$

y perpendicularidad:

$$
\vec{D_1} \cdot \vec{D_2} = 0
$$

Además, los puntos medios de las diagonales coinciden. Esto da:

$$
P_A + P_C = P_B + P_D
$$

Como ya vimos, esta ecuación en componentes verticales restringe los emparejamientos. La única opción viable que da una solución finita fue el emparejamiento de las dos estalactitas como vértices opuestos y las dos estalagmitas como los otros dos vértices opuestos, dando h = 62. Pero concluimos que las diagonales tendrían diferencias verticales 16 y 22, que no pueden dar diagonales de igual longitud si las proyecciones horizontales son iguales.

Sin embargo, ¿acaso las proyecciones horizontales de las diagonales deben ser iguales? En un cuadrado, si los vértices opuestos son las estalactitas, estos dos puntos están a alturas 44 y 28 (para h = 62). Su vector diagonal tiene componente vertical -16. Los otros dos vértices (estalagmitas) están a 25 y 47, con componente vertical +22. Para que las diagonales sean perpendiculares e iguales, las proyecciones horizontales deben cumplir:

Sea $\vec{u}$ la proyección horizontal de la primera diagonal (entre estalactitas) y $\vec{v}$ la de la segunda (entre estalagmitas). Entonces:

$$
|\vec{u}|^2 + 16^2 = |\vec{v}|^2 + 22^2
$$

y

$$
\vec{u} \cdot \vec{v} + (-16)(22) = 0
$$

de la perpendicularidad.

Pero en un cuadrado, las proyecciones de las diagonales en el plano horizontal no son necesariamente perpendiculares; la perpendicularidad es en 3D. Así que $\vec{u}$ y $\vec{v}$ pueden no ser perpendiculares, y sus longitudes pueden diferir. Entonces sí es posible.

Necesitamos más condiciones. Los cuatro vértices del cuadrado son $A, B, C, D$. Si los pares opuestos son $(A,B)$ y $(C,D)$, entonces:

- $A$ y $B$ son las estalactitas (alturas $h-18$ y $h-34$)
- $C$ y $D$ son las estalagmitas (alturas 25 y 47)

Las posiciones horizontales de $A, B, C, D$ deben cumplir que formen un cuadrado. Esto significa que los lados son $AC$, $CB$, $BD$, $DA$ (o alguna permutación). La condición de cuadrado se traduce en que:

$$
A - B = C - D \quad \text{(o similar)}
$$

Espera, usemos la estructura del cuadrado. Si $A$ y $B$ son vértices opuestos, y $C$ y $D$ los otros dos opuestos, entonces los lados conectan $A$ con $C$ y $D$, y $B$ con $C$ y $D$. En un cuadrado, los vectores $A-C$ y $D-B$ etc. deben cumplir ciertas relaciones.

Una caracterización simple: si $A$ y $B$ son vértices opuestos de un cuadrado, y $C$ y $D$ los otros dos, entonces el centro del cuadrado es el punto medio de $AB$ y también el punto medio de $CD$. Además, los vectores desde el centro a los vértices son perpendiculares y de igual longitud. Es decir, si $O$ es el centro, entonces:

$$
\overrightarrow{OA} = \vec{p}, \quad \overrightarrow{OB} = -\vec{p}, \quad \overrightarrow{OC} = \vec{q}, \quad \overrightarrow{OD} = -\vec{q}
$$

con $\vec{p} \perp \vec{q}$ y $|\vec{p}| = |\vec{q}|$.

De esto, las componentes verticales de $\vec{p}$ y $\vec{q}$ son:

- $\vec{p}$ tiene componente vertical $(h-18 - \bar{z})$, donde $\bar{z}$ es la altura del centro.
- $-\vec{p}$ tiene componente vertical $(h-34 - \bar{z})$; por tanto, $(h-34 - \bar{z}) = -(h-18 - \bar{z})$, lo que implica:

$$
h - 34 - \bar{z} = -h + 18 + \bar{z}
$$

$$
2\bar{z} = 2h - 52
$$

$$
\bar{z} = h - 26
$$

Además, la componente vertical de $\vec{p}$ es:

$$
p_z = h - 18 - (h - 26) = 8
$$

De manera consistente, para $B$: $h - 34 - (h-26) = -8$. Correcto.

De forma análoga, para $\vec{q}$, con $C$ a altura 25 y $D$ a altura 47:

$$
q_z = 25 - \bar{z} = 25 - (h-26) = 51 - h
$$

y para $D$: $47 - (h-26) = 73 - h = -(51 - h)$, lo que implica:

$$
73 - h = h - 51
$$

$$
2h = 124
$$

$$
h = 62
$$

Esto confirma h = 62. La componente vertical de $\vec{q}$ es $q_z = 51 - 62 = -11$.

Entonces $\vec{p}$ y $\vec{q}$ son perpendiculares en 3D, con componentes verticales 8 y -11, e igual longitud. Sea $\vec{p} = (p_x, p_y, 8)$ y $\vec{q} = (q_x, q_y, -11)$.

Perpendicularidad:

$$
p_x q_x + p_y q_y + (8)(-11) = 0
$$

$$
p_x q_x + p_y q_y = 88
$$

Igual longitud:

$$
p_x^2 + p_y^2 + 64 = q_x^2 + q_y^2 + 121
$$

Esto es un sistema que tiene soluciones para $p_x, p_y, q_x, q_y$, así que geométricamente es factible. Por ejemplo, escojamos $\vec{p} = (a, 0, 8)$ y $\vec{q} = (0, b, -11)$ con $a^2 + 64 = b^2 + 121$ y perpendicularidad da $0 + 0 - 88 = 0$, que no se cumple. Entonces no podemos tenerlos en ejes ortogonales simples, pero sí existen soluciones: tomemos $\vec{p}$ y $\vec{q}$ con producto punto horizontal igual a 88 y longitudes que difieran en 57. Esto es factible; por ejemplo, elijamos $\vec{p} = (\sqrt{57}, 0, 8)$ y $\vec{q} = (88/\sqrt{57}, y, -11)$ con q_x ajustado, etc. Hay solución.

Por tanto, h = 62 es consistente con que las cuatro puntas sean los vértices de un cuadrado.

¿Podría haber otro valor de h? Los emparejamientos 1 y 2 produjeron ecuaciones inconsistentes, así que no. Por tanto, la única altura posible es:

$$
\boxed{62}
$$

Final answer: \boxed{62}