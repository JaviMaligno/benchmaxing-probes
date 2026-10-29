Voy a resolver el problema paso a paso.

## 1. Planteamiento

Tenemos 6 puntos fijos en el plano:
- $P_1 = (0,0)$
- $P_2 = (10,0)$
- $P_3 = (10,10)$
- $P_4 = (0,10)$
- $P_5 = (3,4)$
- $P_6 = (6,2)$

Un hexágono $RANDOM$ se forma asignando los rótulos $R,A,N,D,O,M$ a estos puntos en algún orden. La secuencia $R \to A \to N \to D \to O \to M \to R$ debe ser un hexágono **no autointersecante** (un polígono simple). Queremos el área máxima y mínima posibles.

## 2. Área de un polígono por el método «shoelace»

El área (con signo) de un polígono ordenado $(x_1,y_1),\dots,(x_n,y_n)$ es

$$
A = \frac{1}{2}\left|\sum_{i=1}^{n}(x_i y_{i+1} - x_{i+1}y_i)\right|
$$

con $(x_{n+1},y_{n+1})=(x_1,y_1)$. El valor absoluto da el área geométrica. Si el polígono se auto-interseca, esta fórmula da un área algebraica que no corresponde a la región «visible», por eso hemos de restringirnos a ordenamientos que den un polígono simple.

## 3. Observación clave sobre la envolvente convexa

Los puntos $(0,0)$, $(10,0)$, $(10,10)$, $(0,10)$ forman un cuadrado de área $100$. Los otros dos puntos, $(3,4)$ y $(6,2)$, están **en el interior** de ese cuadrado.

Esto sugiere una idea clásica: para que el hexágono sea simple y tenga área máxima, conviene ser el hexágono que recorre la envolvente convexa exterior (los 4 vértices del cuadrado) e incorpora los puntos interiores; para área mínima, conviene un hexágono en cierto modo «replegado» o que deje fuera una gran parte del cuadrado.

## 4. Envolvente convexa de los 6 puntos

Calculemos la envolvente convexa. Los dos puntos interiores:

- $(3,4)$: ¿está dentro del cuadrado? Sí, ambos interiores.
- $(6,2)$: también interior.

Los 4 vértices del cuadrado forman la envolvente convexa, pues los otros dos puntos caen dentro. La intersección de los semiplanos correspondientes a los lados del cuadrado contiene a ambos puntos interiores.

Así, la envolvente convexa es el cuadrado $[0,10]\times[0,10]$.

## 5. Área máxima

Dado un conjunto de puntos en el plano, entre todos los polígonos simples cuyos vértices son exactamente esos puntos, el de **área máxima** es justamente la envolvente convexa (recorrida como polígono). Los puntos interiores se insertan en el orden en que aparecen proyectados dentro del contorno, sin cambiar la frontera exterior.

La envolvente convexa es el cuadrado de área $100$. Pero ojo: el hexágono debe contener los 6 puntos como vértices, algunos interiores. El área de la región encerrada por el polígono simple que pasa por todos los puntos en el orden convexo:

Orden convexo (sentido antihorario) sería:

$$(0,0) \to (10,0) \to (10,10) \to (0,10) \to (0,0)$$

solo 4 vértices. Para incluir los interiores debemos intercalarlos a lo largo de la frontera. Por ejemplo:

- Vamos de $(0,0)$ a $(10,0)$, pasando por $(6,2)$.
- Luego a $(10,10)$.
- Luego a $(0,10)$.
- Luego a $(0,0)$, pasando por $(3,4)$, o similar.

¿Cuál es el área máxima? Veamos: los puntos interiores $(3,4)$ y $(6,2)$ están sobre el segmento interior. Si los insertamos en un orden que mantenga la frontera exactamente igual al cuadrado, el área sigue siendo básicamente la del cuadrado menos unos pequeños triángulos, dependiendo de la ruta.

Pero hay un resultado más fuerte: para un conjunto de puntos, el polígono simple de área máxima es el polígono convexo que los recorre a todos como vértices — solo que aquí los interiores no pueden ser «vértices» de la envolvente sin dejar de ser interiores. El área máxima del polígono simple será el área de la envolvente convexa **menos** las áreas de los triángulos que quedan «recortados» al pasar de un vértice exterior a otro pasando por interiores que están hacia adentro.

Veamos cuál ordenamiento maximiza el área. Necesariamente la frontera debe recorrerse en orden angular creciente para no auto-intersecarse. Los ángulos (argumentos) de los puntos respecto a un centro interior, p. ej. $(5,5)$:

- $(0,0)$: $225^\circ$
- $(10,0)$: $315^\circ$ (o $-45^\circ$)
- $(10,10)$: $45^\circ$
- $(0,10)$: $135^\circ$
- $(3,4)$: vector $(-2,-1)$, ángulo $\approx 206.6^\circ$
- $(6,2)$: vector $(1,-3)$, ángulo $\approx -71.6^\circ$ (o $288.4^\circ$)

Ordenando por ángulo creciente desde, digamos, $135^\circ$:

Veamos con más cuidado. Usemos el punto $(3,4)$ y $(6,2)$ para intercalar bien en el contorno del cuadrado.

Propongo colocar los puntos de forma que el recorrido siga el borde del cuadrado en el sentido más externo posible. Las posiciones naturales:

Desde $(0,10)$ bajando por el lado izquierdo hacia $(0,0)$, el punto $(3,4)$ está a la derecha de ese segmento (hacia el interior), así que insertarlo crea un pequeño «diente» hacia adentro, recortando el área.

Para minimizar las pérdidas, insertamos cada punto interior en el lado del cuadrado más cercano, donde el diente es pequeño.

Distancias:
- $(3,4)$: a $x=0$ (izquierda) distancia 3; a $y=0$ (abajo) distancia 4; a $y=10$ (arriba) distancia 6; a $x=10$ (derecha) distancia 7. Más cercano al lado izquierdo.
- $(6,2)$: a $y=0$ distancia 2; a $x=10$ distancia 4; a $x=0$ distancia 6; a $y=10$ distancia 8. Más cercano al lado inferior.

## 6. Un recorrido candidato de área máxima

Ordenemos (sentido antihorario) para maximizar:

$$(0,0) \to (6,2) \to (10,0) \to (10,10) \to (0,10) \to (3,4) \to (0,0)$$

Veamos el recorrido, paso a paso:

Este recorrido recorre el borde inferior del cuadrado desde $(0,0)$ hasta $(10,0)$, pero con un diente hacia arriba en $(6,2)$.

Área por shoelace:

Puntos ordenados:
1. $(0,0)$
2. $(6,2)$
3. $(10,0)$
4. $(10,10)$
5. $(0,10)$
6. $(3,4)$
7. cierre: $(0,0)$

Suma $S=\sum (x_i y_{i+1} - x_{i+1} y_i)$:

- $\mathbf{v_1 \to v_2}$: $0\cdot 2 - 6\cdot 0 = 0$
- $\mathbf{v_2 \to v_3}$: $6\cdot 0 - 10\cdot 2 = -20$
- $\mathbf{v_3 \to v_4}$: $10\cdot 10 - 10\cdot 0 = 100$
- $\mathbf{v_4 \to v_5}$: $10\cdot 10 - 0\cdot 10 = 100$
- $\mathbf{v_5 \to v_6}$: $0\cdot 4 - 3\cdot 10 = -30$
- $\mathbf{v_6 \to v_7}$: $3\cdot 0 - 0\cdot 4 = 0$

Suma $S = 0 -20 +100+100-30+0 = 150$

Área $A = \frac{|150|}{2} = 75$.

Hmm, área 75. Veamos otro orden.

¿Qué tal si ponemos $(6,2)$ en el lado derecho y $(3,4)$ en el izquierdo?

Recorrido:

$$(0,0) \to (10,0) \to (10,10) \to (0,10) \to (3,4) \to (0,0)$$

pero falta $(6,2)$. Probemos:

$$(0,0) \to (10,0) \to (10,10) \to (0,10) \to (3,4) \to (0,0)$$

con $(6,2)$ insertado en el borde inferior:

$$(0,0) \to (6,2) \to (10,0) \to (10,10) \to (0,10) \to (3,4) \to (0,0)$$

Eso ya lo calculamos: 75.

Otra opción: insertar $(6,2)$ en el lado derecho, cerca de $(10,0)$:

$$(0,0) \to (10,0) \to (6,2) \to (10,10) \to (0,10) \to (3,4) \to (0,0)$$

Calculamos shoelace:

Puntos:
1. $(0,0)$
2. $(10,0)$
3. $(6,2)$
4. $(10,10)$
5. $(0,10)$
6. $(3,4)$
7. $(0,0)$

Suma:
- $v_1 \to v_2$: $0\cdot 0 - 10\cdot 0 = 0$
- $v_2 \to v_3$: $10\cdot 2 - 6\cdot 0 = 20$
- $v_3 \to v_4$: $6\cdot 10 - 10\cdot 2 = 40$
- $v_4 \to v_5$: $10\cdot 10 - 0\cdot 10 = 100$
- $v_5 \to v_6$: $0\cdot 4 - 3\cdot 10 = -30$
- $v_6 \to v_7$: $3\cdot 0 - 0\cdot 4 = 0$

Suma = $0+20+40+100-30+0 = 130$

Área = $130/2 = 65$. Menor que 75.

Así que lo mejor entre estos es 75. ¿Podemos superar 75? 

El área máxima teórica si no hubiera dientes sería 100. Cada punto interior, al insertarse en un borde, recorta un triángulo.

Si insertamos $(6,2)$ en el borde inferior, el diente va del punto $(0,0)$ a $(6,2)$ a $(10,0)$. El área «perdida» respecto del triángulo recto $(0,0)-(10,0)-(?)... Mejor lo vemos directamente: el triángulo con base el segmento $(0,0)$–$(10,0)$ y vértice $(6,2)$ tiene área $= \frac12 \cdot 10 \cdot 2 = 10$. El polígono, al ir de $(0,0)$ a $(6,2)$ a $(10,0)$, en lugar de ir directo de $(0,0)$ a $(10,0)$, lo que hace es «subir» y crear un pico interior. La región entre el segmento recto y el pico se pierde del área del cuadrado?

Calculemos: si el contorno fuera solo el cuadrado $(0,0)\to(10,0)\to(10,10)\to(0,10)\to(0,0)$, área 100. Al insertar $(6,2)$ entre $(0,0)$ y $(10,0)$, el polígono pasa por el pico $(6,2)$. El área del cuadrado con el borde inferior ahora como poligonal $(0,0)\to(6,2)\to(10,0)$ pierde el área del triángulo con vértices $(0,0)$, $(6,2)$, $(10,0)$? 

Los vectores desde $(6,2)$: hacia $(0,0)$, diferencia $(-6,-2)$; hacia $(10,0)$, diferencia $(4,-2)$. El triángulo $(0,0),(6,2),(10,0)$ tiene área:

$$\frac12 |(-6)(-2) - (4)(-2)| = \frac12|12 +8| = \frac12\cdot 20 = 10.$$

Correcto, 10.

Al insertar $(3,4)$ entre $(0,10)$ y $(0,0)$ (borde izquierdo), el pico está en $(3,4)$. El triángulo con vértices $(0,10),(3,4),(0,0)$ tiene área:

Base vertical sobre $x=0$ de longitud 10, y altura horizontal del pico es 3. Área $= \frac12 \cdot 10 \cdot 3 = 15$.

Entonces el área del polígono será $100 - 10 - 15 = 75$. Coincide.

¿Se puede hacer mejor con otra colocación? Si insertamos $(6,2)$ en el lado derecho entre $(10,0)$ y $(10,10)$, el pico en $(6,2)$ está a distancia horizontal 4 del lado derecho. Triángulo con vértices $(10,0)$, $(6,2)$, $(10,10)$: base vertical 10, altura 4, área $=20$. Si además $(3,4)$ va en el lado izquierdo (área 15), total perdido $35$, área $65$. Peor.

Si insertamos $(6,2)$ en el borde inferior (pérdida 10) y $(3,4)$ en el lado izquierdo (pérdida 15), área 75. Esa parece la mejor combinación, porque cada punto debe ir en el borde más cercano para minimizar el área perdida.

¿Y si un punto interior se inserta entre dos bordes no contiguos, o en una esquina? Las esquinas están ocupadas por los vértices del cuadrado, pero podríamos elegir un recorrido no convexo en otros sentidos. Sin embargo, para maximizar el área con puntos interiores, lo lógico es asemejarse lo más posible a la envolvente convexa y soportar la mínima pérdida. La pérdida mínima por inserción en un borde del cuadrado es:

- Para $(6,2)$: borde inferior, pérdida 10. (borde derecho: 20; borde superior: ? calcular: a $y=10$ distancia 8, triángulo con base el borde superior longitud 10 y altura 8 → 40; borde izquierdo: 30). Mínima: 10.
- Para $(3,4)$: borde izquierdo, pérdida 15. (borde inferior: 20; borde derecho: 35; borde superior: 30). Mínima: 15.

Por tanto la pérdida total mínima es $10+15=25$, área máxima $100 - 25 = 75$.

Así que $a_{\max}=75$.

## 7. Área mínima

Ahora buscamos el polígono simple de área mínima. Con puntos que en su mayoría están en la envolvente convexa, el área mínima se consigue cuando los puntos interiores están en un orden que «rebana» la mayor parte del cuadrado, dejando un polígono delgado en el borde o alrededor del centro.

Intuición: el área mínima es la de un polígono que recorre todos los puntos con un área pequeña, quizá encerrando los puntos internos casi sin área.

Para incluirlos todos y que sea simple, uno puede recorrer en un orden tal que el polígono «vaya y vuelva» por los puntos interiores. Veamos candidates.

Posibilidad: el polígono del tipo «dos cadenas», una cadena superior y una inferior, ambas pasando por los puntos interiores. El área será la suma de las áreas de los triángulos formados entre cadenas.

El área mínima con todos estos puntos se alcanza quizá con los interiores en posición tal que las dos cadenas casi coincidan.

Probemos el recorrido:

$$(0,0) \to (3,4) \to (6,2) \to (10,0) \to (10,10) \to (0,10) \to (0,0)$$

Este es como el cuadrado pero con un «pico» en la parte inferior formado por $(0,0)\to(3,4)\to(6,2)\to(10,0)$. Calculemos shoelace.

Puntos:
1. $(0,0)$
2. $(3,4)$
3. $(6,2)$
4. $(10,0)$
5. $(10,10)$
6. $(0,10)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: $0\cdot4 - 3\cdot0 = 0$
- $v_2\to v_3$: $3\cdot2 - 6\cdot4 = 6 - 24 = -18$
- $v_3\to v_4$: $6\cdot0 - 10\cdot2 = -20$
- $v_4\to v_5$: $10\cdot10 - 10\cdot0 = 100$
- $v_5\to v_6$: $10\cdot10 - 0\cdot10 = 100$
- $v_6\to v_7$: $0\cdot0 - 0\cdot10 = 0$

Suma = $0 -18 -20 +100+100+0 = 162$

Área = $162/2 = 81$. Eso es mayor que 75, no nos sirve para mínimo.

Probemos ordenar de modo que el polígono se auto-repliegue brutalmente, es decir, dos puntos interiores consecutivos, y luego dedos por los bordes. Por ejemplo:

$$(0,0) \to (10,0) \to (6,2) \to (10,10) \to (0,10) \to (3,4) \to (0,0)$$

Eso da área 65 (calculado arriba, recorrido con $(6,2)$ en el lado derecho). Aún no es mínimo.

Probemos con interiores contiguos entre sí:

$$(0,0) \to (6,2) \to (3,4) \to (0,10) \to (10,10) \to (10,0) \to (0,0)$$

Puntos:
1. $(0,0)$
2. $(6,2)$
3. $(3,4)$
4. $(0,10)$
5. $(10,10)$
6. $(10,0)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: $0\cdot2 - 6\cdot0 = 0$
- $v_2\to v_3$: $6\cdot4 - 3\cdot2 = 24 - 6 = 18$
- $v_3\to v_4$: $3\cdot10 - 0\cdot4 = 30$
- $v_4\to v_5$: $0\cdot10 - 10\cdot10 = -100$
- $v_5\to v_6$: $10\cdot0 - 10\cdot10 = -100$
- $v_6\to v_7$: $10\cdot0 - 0\cdot0 = 0$

Suma = $0+18+30-100-100+0 = -152$

Área = $|-152|/2 = 76$. Tampoco.

Necesitamos una estrategia mejor. Para el área mínima con polígono simple, un resultado clásico es que se obtiene como el área de la envolvente convexa menos la máxima suma de áreas de los triángulos formados por puntos interiores que quedan «fuera».

Pensemos geométricamente. El polígono simple de área mínima que pasa por 4 vértices del cuadrado y 2 interiores sería aquel cuya frontera serpentea para encerrar la mínima región posible. Visualicemos: para que sea simple y contenga los 6 puntos como vértices, debe recorrer una frontera cerrada. El área mínima ocurre cuando el recorrido pasa por puntos interiores de forma consecutiva en el medio, creando una especie de «reloj de arena» o «corbata», en cuyo caso el área encerrada se resta en parte.

Un ejemplo de recorrido de este estilo:

$$(0,0) \to (3,4) \to (0,10) \to (10,10) \to (6,2) \to (10,0) \to (0,0)$$

Visualicemos: salimos del origen hacia $(3,4)$, subimos a $(0,10)$, recorremos el borde superior a $(10,10)$, bajamos hacia $(6,2)$, luego a $(10,0)$ y cerramos al origen. Esto forma un hexágono cóncavo con dos «picos» interiores.

Calculamos shoelace:

Puntos:
1. $(0,0)$
2. $(3,4)$
3. $(0,10)$
4. $(10,10)$
5. $(6,2)$
6. $(10,0)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: $0\cdot4 - 3\cdot0 = 0$
- $v_2\to v_3$: $3\cdot10 - 0\cdot4 = 30$
- $v_3\to v_4$: $0\cdot10 - 10\cdot10 = -100$
- $v_4\to v_5$: $10\cdot2 - 6\cdot10 = 20 - 60 = -40$
- $v_5\to v_6$: $6\cdot0 - 10\cdot2 = -20$
- $v_6\to v_7$: $10\cdot0 - 0\cdot0 = 0$

Suma = $0+30-100-40-20+0 = -130$

Área = $|-130|/2 = 65$. 

Bien, 65 otra vez. Probemos con los interiores intercambiados:

$$(0,0) \to (6,2) \to (0,10) \to (10,10) \to (3,4) \to (10,0) \to (0,0)$$

Puntos:
1. $(0,0)$
2. $(6,2)$
3. $(0,10)$
4. $(10,10)$
5. $(3,4)$
6. $(10,0)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: $0\cdot2 - 6\cdot0 = 0$
- $v_2\to v_3$: $6\cdot10 - 0\cdot2 = 60$
- $v_3\to v_4$: $0\cdot10 - 10\cdot10 = -100$
- $v_4\to v_5$: $10\cdot4 - 3\cdot10 = 40 - 30 = 10$
- $v_5\to v_6$: $3\cdot0 - 10\cdot4 = -40$
- $v_6\to v_7$: $10\cdot0 - 0\cdot0 = 0$

Suma = $0+60-100+10-40+0 = -70$

Área = $|-70|/2 = 35$. 

¡Esto ya es mucho menor! Área 35.

¿Podemos hacerlo aún menor? Probemos con los interiores más cerca de los bordes opuestos.

Otro recorrido:

$$(0,0) \to (6,2) \to (10,10) \to (0,10) \to (3,4) \to (10,0) \to (0,0)$$

Puntos:
1. $(0,0)$
2. $(6,2)$
3. $(10,10)$
4. $(0,10)$
5. $(3,4)$
6. $(10,0)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: $0\cdot2 - 6\cdot0 = 0$
- $v_2\to v_3$: $6\cdot10 - 10\cdot2 = 60 - 20 = 40$
- $v_3\to v_4$: $10\cdot10 - 0\cdot10 = 100$
- $v_4\to v_5$: $0\cdot4 - 3\cdot10 = -30$
- $v_5\to v_6$: $3\cdot0 - 10\cdot4 = -40$
- $v_6\to v_7$: $10\cdot0 - 0\cdot0 = 0$

Suma = $0+40+100-30-40+0 = 70$

Área = $70/2 = 35$. Mismo valor.

Intentemos con $(6,2)$ y $(3,4)$ en posiciones que formen un área aún más pequeña. ¿Y si van consecutivos entre los bordes?

$$(0,0) \to (6,2) \to (3,4) \to (10,10) \to (0,10) \to (10,0) \to (0,0)$$

Suma:
Puntos:
1. $(0,0)$
2. $(6,2)$
3. $(3,4)$
4. $(10,10)$
5. $(0,10)$
6. $(10,0)$
7. $(0,0)$

- $v_1\to v_2$: $0\cdot2 - 6\cdot0 = 0$
- $v_2\to v_3$: $6\cdot4 - 3\cdot2 = 24 - 6 = 18$
- $v_3\to v_4$: $3\cdot10 - 10\cdot4 = 30 - 40 = -10$
- $v_4\to v_5$: $10\cdot10 - 0\cdot10 = 100$
- $v_5\to v_6$: $0\cdot0 - 10\cdot10 = -100$
- $v_6\to v_7$: $10\cdot0 - 0\cdot0 = 0$

Suma = $0+18-10+100-100+0 = 8$

Área = $8/2 = 4$. 

¡Mucho menor! Veamos si es un polígono simple.

Recorrido:
1. $(0,0)$ → $(6,2)$
2. $(6,2)$ → $(3,4)$
3. $(3,4)$ → $(10,10)$
4. $(10,10)$ → $(0,10)$
5. $(0,10)$ → $(10,0)$
6. $(10,0)$ → $(0,0)$

¿Hay auto-intersección? El segmento $(0,10)\to(10,0)$ es la diagonal principal del cuadrado. Los segmentos anteriores: $(0,0)\to(6,2)\to(3,4)\to(10,10)$. 

¿El segmento $(3,4)\to(10,10)$ interseca al $(0,10)\to(10,0)$? La recta de $(3,4)$ a $(10,10)$: pendiente $\frac{6}{7}\approx0.857$. En $x$ entre 3 y 10, $y$ entre 4 y 10. La diagonal $(0,10)\to(10,0)$ es $y = 10-x$.

Intersección: $y = 4 + \frac{6}{7}(x-3) = 10 - x$.

$4 + \frac{6}{7}x - \frac{18}{7} = 10 - x$

$\frac{6}{7}x + x = 10 - 4 + \frac{18}{7}$

$\frac{13}{7}x = 6 + \frac{18}{7} = \frac{42+18}{7} = \frac{60}{7}$

$x = \frac{60}{13} \approx 4.615$, $y = 10 - 4.615 = 5.385$. 

Este punto está en el rango de ambos segmentos (x entre 3 y 10 para el primero; x entre 0 y 10 para la diagonal). Por tanto **hay auto-intersección**. Este ordenamiento no forma un polígono simple.

Debemos revisar cuál de los candidatos de área 35 es simple.

Candidato A:
$$(0,0) \to (6,2) \to (0,10) \to (10,10) \to (3,4) \to (10,0) \to (0,0)$$

Segmentos:
- $e_1$: $(0,0)\to(6,2)$
- $e_2$: $(6,2)\to(0,10)$
- $e_3$: $(0,10)\to(10,10)$ (borde superior)
- $e_4$: $(10,10)\to(3,4)$
- $e_5$: $(3,4)\to(10,0)$
- $e_6$: $(10,0)\to(0,0)$ (borde inferior)

¿Hay intersecciones no adyacentes?

- $e_2$ con los demás: $e_2$ es $(6,2)\to(0,10)$. Recta: pendiente $m = \frac{8}{-6} = -\frac43$, ecuación $y = 10 - \frac43 x$ (entre $x\in[0,6]$).

  - Con $e_4$: $(10,10)\to(3,4)$. Pendiente $m = \frac{4-10}{3-10} = \frac{-6}{-7}=\frac67$. Ecuación $y = 10 + \frac67(x-10) = \frac67 x + \frac{10}{7}$? Veamos: $y = 10 + \frac67(x-10) = 10 + \frac67 x - \frac{60}{7} = \frac67 x + \frac{70-60}{7} = \frac67 x + \frac{10}{7}$. Para $x\in[3,10]$.

  Intersección de $e_2$ y $e_4$: 
  
  $10 - \frac43 x = \frac67 x + \frac{10}{7}$.
  
  Multiplico por 21: $210 - 28x = 18x + 30$
  
  $180 = 46x$, $x = \frac{90}{23}\approx3.91$, dentro de $[3,6]$ (ambos). $y\approx10 - 5.22 = 4.78$. Intersección. **Hay auto-intersección.**

Así que candidato A no es simple.

Candidato B:
$$(0,0) \to (6,2) \to (10,10) \to (0,10) \to (3,4) \to (10,0) \to (0,0)$$

Segmentos:
- $e_1$: $(0,0)\to(6,2)$
- $e_2$: $(6,2)\to(10,10)$
- $e_3$: $(10,10)\to(0,10)$ (borde superior)
- $e_4$: $(0,10)\to(3,4)$
- $e_5$: $(3,4)\to(10,0)$
- $e_6$: $(10,0)\to(0,0)$ (borde inferior)

Revisemos intersecciones no adyacentes:

- $e_2$: $(6,2)\to(10,10)$. Pendiente $m=\frac{8}{4}=2$. Ecuación $y = 2 + 2(x-6)=2x-10$, $x\in[6,10]$.

  - Con $e_4$: $(0,10)\to(3,4)$. Pendiente $m=\frac{4-10}{3-0}=-2$. Ecuación $y=10-2x$, $x\in[0,3]$. Los dominios en $x$ no se solapan ($[6,10]$ vs $[0,3]$), así que no se cortan.

  - Con $e_5$: $(3,4)\to(10,0)$. Pendiente $m=\frac{0-4}{10-3}=-\frac47 \approx -0.571$. Ecuación $y = 4 - \frac47(x-3) = -\frac47 x + \frac{28}{7}+\frac{12}{7}?$ Veamos: $y = 4 - \frac47(x-3)$. En $x=3$: $y=4$. En $x=10$: $y=0$. Intersección con $e_2$: $2x - 10 = -\frac47(x-3)+4$.

  Lado derecho: $y = 4 - \frac47(x-3) = 4 - \frac47 x + \frac{12}{7} = \frac{28+12}{7} - \frac47 x = \frac{40}{7} - \frac47 x$.

  Igualamos: $2x - 10 = \frac{40}{7} - \frac47 x$.

  Multiplico por 7: $14x - 70 = 40 - 4x$.

  $18x = 110$, $x = \frac{55}{9}\approx6.11$, dentro de $[6,10]$ y también dentro de $[3,10]$. $y\approx 2\cdot6.11 -10 = 2.22$. Intersección. **Hay auto-intersección.**

Así que candidato B tampoco es simple.

El de área 65:
$$(0,0) \to (3,4) \to (0,10) \to (10,10) \to (6,2) \to (10,0) \to (0,0)$$

Segmentos:
- $e_1$: $(0,0)\to(3,4)$
- $e_2$: $(3,4)\to(0,10)$
- $e_3$: $(0,10)\to(10,10)$
- $e_4$: $(10,10)\to(6,2)$
- $e_5$: $(6,2)\to(10,0)$
- $e_6$: $(10,0)\to(0,0)$

Revisemos:
- $e_2$: $(3,4)\to(0,10)$. Pendiente $m=\frac{6}{-3}=-2$. $y = 10 - 2x$, $x\in[0,3]$.
- $e_4$: $(10,10)\to(6,2)$. Pendiente $m=\frac{2-10}{6-10}=\frac{-8}{-4}=2$. $y=2x-10$, $x\in[6,10]$. Dominios disjuntos con $e_2$, no se cortan.
- $e_2$ con $e_5$: $e_5$: $(6,2)\to(10,0)$. $m=-0.5$. $y = 2 -0.5(x-6) = 2 -0.5x +3 = 5 -0.5x$. $x\in[6,10]$. Dominios disjuntos con $e_2$, no se cortan.
- $e_1$: $(0,0)\to(3,4)$, $m=\frac43$, $y=\frac43x$, $x\in[0,3]$.
  - con $e_4$: dominios disjuntos.
  - con $e_5$: dominios disjuntos ($x\in[0,3]$ vs $[6,10]$).
  - con $e_3$: $e_3$ es $y=10$, $x\in[0,10]$. $e_1$: $y=\frac43 x$ con $x\in[0,3]$, $y_{\max}=4<10$. No se cortan.
- $e_4$ con $e_6$: $e_6$ es $y=0$, $x\in[0,10]$. $e_4$: $y=2x-10$, $x\in[6,10]$, $y\in[2,10]$, no toca $y=0$. No.
- $e_5$ con $e_3$: $e_5$: $y=5-0.5x$, en $x\in[6,10]$, $y\in[2,0]$. $e_3$: $y=10$. No se cortan.
- $e_2$ con $e_6$: $e_2$: $y=10-2x$, $x\in[0,3]$, $y\in[10,4]$. $e_6$: $y=0$. No.

Parece que **no hay intersecciones no adyacentes**, salvo los extremos compartidos adyacentes. Es un polígono simple. Área 65.

¿Hay algún polígono simple con área entre 35 y 65? 

Exploremos más sistemáticamente. Busquemos el mínimo.

Intuyo que el mínimo puede estar cerca de 20 o incluso menos. Probemos configuraciones donde los dos puntos interiores están consecutivos en el centro.

Prueba: 

$$(0,0) \to (6,2) \to (3,4) \to (0,10) \to (10,0) \to (10,10) \to (0,0)$$

Veamos si es simple. Segmentos:
- $e_1$: $(0,0)\to(6,2)$
- $e_2$: $(6,2)\to(3,4)$
- $e_3$: $(3,4)\to(0,10)$
- $e_4$: $(0,10)\to(10,0)$ (diagonal)
- $e_5$: $(10,0)\to(10,10)$ (lado derecho)
- $e_6$: $(10,10)\to(0,0)$ (diagonal)

Intersecciones: $e_4$ con $e_3$: $e_3$ es $(3,4)\to(0,10)$, $m=-2$, $y=10-2x$, $x\in[0,3]$. $e_4$ es $(0,10)\to(10,0)$, $y=10-x$, $x\in[0,10]$. Se cortan en $(0,10)$ que es un extremo compartido adyacente ($e_3$ termina en $(0,10)$, $e_4$ empieza ahí). Bien.

$e_4$ con $e_2$: $e_2$ es $(6,2)\to(3,4)$, $m = \frac{4-2}{3-6}=\frac{2}{-3}=-\frac23$, $y = 2 -\frac23(x-6)=2 - \frac23 x +4 = 6 - \frac23x$, $x\in[3,6]$. Intersección con $y=10-x$: $6 - \frac23x = 10 - x$, $\frac13 x = 4$, $x=12$ fuera de $[3,6]$. No.

$e_4$ con $e_1$: $e_1$: $y = \frac{1}{3}x$ (de $(0,0)$ a $(6,2)$), $x\in[0,6]$. Con $y=10-x$: $\frac13 x = 10-x$, $\frac43 x = 10$, $x=7.5$ fuera de $[0,6]$. No.

$e_6$ (diagonal $(10,10)\to(0,0)$, $y=x$) con:
- $e_5$: $(10,0)\to(10,10)$ lado derecho $x=10$. Intersección en $(10,10)$, extremo compartido adyacente.
- $e_4$: diagonales se cruzan en $(5,5)$, pero $e_4$ y $e_6$ son no adyacentes (están separados por $e_5$). $(5,5)$ está en el segmento $e_4$ ($x\in[0,10]$) y en $e_6$ ($x\in[0,10]$). **Intersección.** Auto-intersección. No sirve.

Probemos variantes. Está claro que debemos evitar que las diagonales se crucen.

El reto: queremos un área pequeña, lo cual instintivamente significa que el polígono debe casi «colapsar», pero debe seguir siendo simple.

Un enfoque: para encontrar el mínimo real, utilicemos el hecho de que el área mínima de un polígono simple que pasa por puntos dados se obtiene con un recorrido en que los puntos interiores quedan en cadenas casi coincidentes. 

Busquemos un candidato sin intersecciones con área baja.

Probemos:

$$(0,0) \to (10,0) \to (3,4) \to (6,2) \to (10,10) \to (0,10) \to (0,0)$$

Segmentos:
- $e_1$: $(0,0)\to(10,0)$ (borde inferior)
- $e_2$: $(10,0)\to(3,4)$
- $e_3$: $(3,4)\to(6,2)$
- $e_4$: $(6,2)\to(10,10)$
- $e_5$: $(10,10)\to(0,10)$ (borde superior)
- $e_6$: $(0,10)\to(0,0)$ (borde izquierdo)

Revisemos intersecciones:
- $e_2$: $(10,0)\to(3,4)$. $m=\frac{4-0}{3-10}=\frac4{-7}=-\frac47$. $y = 0 -\frac47(x-10) = -\frac47 x + \frac{40}{7}$. $x\in[3,10]$.
- $e_4$: $(6,2)\to(10,10)$. $m = \frac{8}{4}=2$. $y = 2 + 2(x-6)=2x-10$. $x\in[6,10]$.
- Intersección $e_2$ y $e_4$: $-\frac47x + \frac{40}{7} = 2x -10$. Multiplico por 7: $-4x+40 = 14x -70$, $18x = 110$, $x=\frac{55}{9}\approx6.11$, que está en $[6,10]$ (ambos rangos). $y\approx -\frac47\cdot6.11+5.71\approx 2.22$. **Intersección.** No sirve.

Probemos una en que los interiores estén al principio / final del recorrido:

$$(0,0) \to (3,4) \to (6,2) \to (10,0) \to (10,10) \to (0,10) \to (0,0)$$

(este es el primer recorrido que calculamos, área 81).

Segmentos:
- $e_1$: $(0,0)\to(3,4)$
- $e_2$: $(3,4)\to(6,2)$
- $e_3$: $(6,2)\to(10,0)$
- $e_4$: $(10,0)\to(10,10)$ (lado derecho)
- $e_5$: $(10,10)\to(0,10)$ (borde superior)
- $e_6$: $(0,10)\to(0,0)$ (borde izquierdo)

Intersecciones: los tres primeros segmentos forman una poligonal. ¿Se auto-interseca con bordes? Los bordes $e_4,e_5,e_6$ son los lados derecho, superior e izquierdo del cuadrado. Los puntos interiores en la poligonal son $(3,4)$ y $(6,2)$, dentro del cuadrado. La poligonal va de $(0,0)$ a $(10,0)$ pasando por interiores; ¿cruza bordes? No, está dentro del cuadrado y puede cruzarse a sí misma? $e_1$ va de $(0,0)$ a $(3,4)$, $e_2$ de $(3,4)$ a $(6,2)$, $e_3$ de $(6,2)$ a $(10,0)$. Veamos si $e_1$ cruza $e_3$: $e_1$: $y=\frac43 x$, $x\in[0,3]$. $e_3$: de $(6,2)$ a $(10,0)$, $m=\frac{0-2}{10-6}=-\frac12$, $y=2-\frac12(x-6)=2-\frac12x+3=5-\frac12x$, $x\in[6,10]$. Dominios disjuntos en $x$, no se cruzan. Simple. Área 81.

Ese es simple con área 81. No es el mínimo.

¿Dónde está el mínimo? Pensemos más.

El área mínima de un polígono simple sobre un conjunto de puntos fijos es un problema conocido; a menudo se obtiene conectando los puntos de manera que el polígono sea «lo más delgado posible». Dado que 4 puntos forman un cuadrado grande y 2 están en el interior, el mínimo probablemente involucra una especie de polígono que casi es un segmento ida y vuelta.

Podemos usar la idea de que para minimizar el área, conviene que los dos puntos interiores estén **consecutivos** y que el recorrido atraviese el interior casi duplicando un camino.

Probemos:

$$(0,0) \to (0,10) \to (3,4) \to (6,2) \to (10,10) \to (10,0) \to (0,0)$$

Segmentos:
- $e_1$: $(0,0)\to(0,10)$ (lado izquierdo)
- $e_2$: $(0,10)\to(3,4)$
- $e_3$: $(3,4)\to(6,2)$
- $e_4$: $(6,2)\to(10,10)$
- $e_5$: $(10,10)\to(10,0)$ (lado derecho)
- $e_6$: $(10,0)\to(0,0)$ (borde inferior)

Revisemos intersecciones:
- $e_2$: $(0,10)\to(3,4)$, $m=-2$, $y=10-2x$, $x\in[0,3]$.
- $e_4$: $(6,2)\to(10,10)$, $m=2$, $y=2x-10$, $x\in[6,10]$. Dominios disjuntos. No se cruzan.
- $e_3$: $(3,4)\to(6,2)$, $m=-\frac23$, $y=4-\frac23(x-3)=4-\frac23x+2=6-\frac23x$, $x\in[3,6]$.
  - con $e_5$: lado derecho $x=10$, no en $[3,6]$. No.
  - con $e_1$: lado izquierdo $x=0$, no. No.
  - con $e_6$: $y=0$, $x\in[0,10]$. $e_3$: $y=6-\frac23x$; $6-\frac23x=0$ da $x=9$, fuera de $[3,6]$. No.
- $e_2$ con $e_4$: dominios disjuntos, ya visto.
- $e_2$ con $e_5$: $e_5$ es $x=10$, $e_2$ tiene $x\in[0,3]$. No.
- $e_2$ con $e_6$: $e_6$ es $y=0$, $e_2$: $y=10-2x$, $x\in[0,3]$, $y\in[10,4]$, no toca $y=0$. No.
- $e_4$ con $e_6$: $e_4$: $y=2x-10$, $x\in[6,10]$, $y\in[2,10]$, no toca $y=0$. No.
- $e_1$ con $e_3$: $e_1$: $x=0$, $e_3$: $x\in[3,6]$. No.
- $e_1$ con $e_4$: $e_1$: $x=0$, $e_4$: $x\in[6,10]$. No.

Parece simple. Calculemos área.

Puntos:
1. $(0,0)$
2. $(0,10)$
3. $(3,4)$
4. $(6,2)$
5. $(10,10)$
6. $(10,0)$
7. $(0,0)$

Suma shoelace:
- $v_1\to v_2$: $0\cdot10 - 0\cdot0 = 0$
- $v_2\to v_3$: $0\cdot4 - 3\cdot10 = -30$
- $v_3\to v_4$: $3\cdot2 - 6\cdot4 = 6 - 24 = -18$
- $v_4\to v_5$: $6\cdot10 - 10\cdot2 = 60 - 20 = 40$
- $v_5\to v_6$: $10\cdot0 - 10\cdot10 = -100$
- $v_6\to v_7$: $10\cdot0 - 0\cdot0 = 0$

Suma = $0 -30 -18 +40 -100 +0 = -108$

Área = $|-108|/2 = 54$. Peor que 65 (aunque 65 era un candidato no óptimo, el mínimo que buscamos).

Necesito ser más metódico. En vez de probar al azar, pensemos en cuál es la estructura óptima.

### Enfoque sistemático

Tenemos 6 puntos: 4 esquinas del cuadrado y 2 interiores. Para que el hexágono $RANDOM$ sea simple, el recorrido debe ser un orden cíclico que no se cruce.

Un criterio útil: en un polígono simple, los vértices deben seguir un orden alrededor de la envolvente; los puntos interiores se insertan en «muescas» del contorno pero sin cruzar otras aristas.

Como el conjunto es pequeño, podemos en principio enumerar todos los ciclos hamiltonianos simples (hay $(6-1)!/2=60$ ciclos sin considerar orientación y punto de inicio, pero solo algunos son simples). De ellos, el de mayor y menor área.

Pero podemos reducir el espacio. Los 4 vértices del cuadrado están en la envolvente convexa; para que el ciclo sea simple, dichos 4 vértices deben aparecer en el orden cíclico convexo (o el reverso). Es decir, alrededor del ciclo, las esquinas deben ir en el orden $(0,0)\to(10,0)\to(10,10)\to(0,10)$ o su reverso. Si no, el polígono se auto-interseca.

Por tanto fijemos el orden de las esquinas en sentido antihorario:

$$A = (0,0),\; B=(10,0),\; C=(10,10),\; D=(0,10)$$

y el ciclo debe ser $A \to B \to C \to D \to A$, insertando $(3,4)$ y $(6,2)$ en alguna de las cuatro «ranuras» (entre $A$-$B$, $B$-$C$, $C$-$D$, $D$-$A$).

Las inserciones posibles:

1. Ambos interiores en la misma ranura, en dos órdenes posibles.
2. Cada uno en ranuras distintas.

Para que el ciclo resultante sea simple, hay restricciones.

El área máxima será claramente el ciclo convexo con inserciones que minimizan el recorte, que ya encontramos (75). 

El área mínima será el de mayor recorte. Exploremos.

Las esquinas $A,B,C,D$ y los interiores $I_1=(3,4)$ y $I_2=(6,2)$.

Veamos qué pasa si inserto ambos interiores en la ranura $A$–$B$ (el borde inferior). Sub-casos:

(1a) $A \to I_2(6,2) \to I_1(3,4) \to B$:

Secuencia completa:
$$(0,0) \to (6,2) \to (3,4) \to (10,0) \to (10,10) \to (0,10) \to (0,0)$$

Calculemos shoelace. Ya vimos uno similar. Puntos:
1. $(0,0)$
2. $(6,2)$
3. $(3,4)$
4. $(10,0)$
5. $(10,10)$
6. $(0,10)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: $0$
- $v_2\to v_3$: $6\cdot4 - 3\cdot2 = 24-6=18$
- $v_3\to v_4$: $3\cdot0 - 10\cdot4 = -40$
- $v_4\to v_5$: $10\cdot10 - 10\cdot0 = 100$
- $v_5\to v_6$: $10\cdot10 - 0\cdot10 = 100$
- $v_6\to v_7$: $0$

Suma = $0+18-40+100+100+0=178$

Área = $178/2=89$. Simple (interiores consecutivos en la ranura inferior, los bordes no se cruzan).

(1b) $A \to I_1(3,4) \to I_2(6,2) \to B$:

Secuencia:
$$(0,0) \to (3,4) \to (6,2) \to (10,0) \to (10,10) \to (0,10) \to (0,0)$$

Área = 81 (ya calculado).

Así que en la ranura inferior, el área es 81 u 89. No es mínimo.

(2) Insertar uno en la ranura inferior y otro en la ranura derecha.

Ranura inferior: $A \to ? \to B$; ranura derecha: $B \to ? \to C$.

Opciones:
- $A \to I_1 \to B \to I_2 \to C$:
  $$(0,0)\to(3,4)\to(10,0)\to(6,2)\to(10,10)\to(0,10)\to(0,0)$$

Calculemos shoelace.

Puntos:
1. $(0,0)$
2. $(3,4)$
3. $(10,0)$
4. $(6,2)$
5. $(10,10)$
6. $(0,10)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: $0\cdot4 - 3\cdot0 = 0$
- $v_2\to v_3$: $3\cdot0 - 10\cdot4 = -40$
- $v_3\to v_4$: $10\cdot2 - 6\cdot0 = 20$
- $v_4\to v_5$: $6\cdot10 - 10\cdot2 = 60-20=40$
- $v_5\to v_6$: $10\cdot10 - 0\cdot10 = 100$
- $v_6\to v_7$: $0\cdot0 - 0\cdot10 = 0$

Suma = $0-40+20+40+100+0 = 120$

Área = $120/2 = 60$. 

Revisemos simplicidad. Segmentos:
- $e_1$: $(0,0)\to(3,4)$
- $e_2$: $(3,4)\to(10,0)$
- $e_3$: $(10,0)\to(6,2)$
- $e_4$: $(6,2)\to(10,10)$
- $e_5$: $(10,10)\to(0,10)$
- $e_6$: $(0,10)\to(0,0)$

Intersecciones:
- $e_2$: $(3,4)\to(10,0)$, $m = \frac{0-4}{10-3}=-\frac47$, $y=-\frac47x+\frac{40}{7}$, $x\in[3,10]$.
- $e_4$: $(6,2)\to(10,10)$, $m=2$, $y=2x-10$, $x\in[6,10]$.
Intersección $e_2$ y $e_4$: $-\frac47x+\frac{40}{7}=2x-10$. Multiplico por 7: $-4x+40=14x-70$, $18x=110$, $x=\frac{55}{9}\approx6.11\in[6,10]$, en ambos rangos. **Intersección → no simple.**

- $A \to I_2(6,2) \to B \to I_1(3,4) \to C$:
  $$(0,0)\to(6,2)\to(10,0)\to(3,4)\to(10,10)\to(0,10)\to(0,0)$$

Segmentos:
- $e_1$: $(0,0)\to(6,2)$
- $e_2$: $(6,2)\to(10,0)$
- $e_3$: $(10,0)\to(3,4)$
- $e_4$: $(3,4)\to(10,10)$
- $e_5$: $(10,10)\to(0,10)$
- $e_6$: $(0,10)\to(0,0)$

Intersecciones:
- $e_3$: $(10,0)\to(3,4)$, $m=-\frac47$, $y=-\frac47x+\frac{40}{7}$.
- $e_4$: $(3,4)\to(10,10)$, $m=\frac67$, $y=\frac67x+\frac{10}{7}$.

Estos dos comparten el punto $(3,4)$ (adyacentes), no es intersección adicional.

- $e_2$: $(6,2)\to(10,0)$, $m=-\frac12$, $y=5-\frac12x$.
- $e_4$: $(3,4)\to(10,10)$, $m=\frac67$, $y=\frac67x+\frac{10}{7}$.
Intersección $e_2$ y $e_4$: $5-\frac12x = \frac67x+\frac{10}{7}$.

Multiplico por 14: $70-7x = 12x+20$, $50=19x$, $x=\frac{50}{19}\approx2.63$. Rango de $e_2$: $x\in[6,10]$. $x=2.63$ fuera. No se cruzan en los segmentos.

- $e_1$: $(0,0)\to(6,2)$, $m=\frac13$, $y=\frac13x$, $x\in[0,6]$.
  - con $e_3$: $e_3$ rango $x\in[3,10]$. Intersección de rectas: $\frac13x = -\frac47x+\frac{40}{7}$. Multiplico por 21: $7x = -12x+120$, $19x=120$, $x=6.315$, pero $e_1$ rango $x\in[0,6]$, $x=6.315$ fuera. No se cruzan.
  - con $e_4$: $e_4$ rango $x\in[3,10]$. $\frac13x = \frac67x+\frac{10}{7}$. Multiplico por 21: $7x = 18x+30$, $x=-\frac{30}{11}<0$, fuera. No.

Parece simple. Calculemos shoelace.

Puntos:
1. $(0,0)$
2. $(6,2)$
3. $(10,0)$
4. $(3,4)$
5. $(10,10)$
6. $(0,10)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: $0$
- $v_2\to v_3$: $6\cdot0 - 10\cdot2 = -20$
- $v_3\to v_4$: $10\cdot4 - 3\cdot0 = 40$
- $v_4\to v_5$: $3\cdot10 - 10\cdot4 = 30-40=-10$
- $v_5\to v_6$: $10\cdot10 - 0\cdot10 = 100$
- $v_6\to v_7$: $0$

Suma = $0-20+40-10+100+0 = 110$

Área = $110/2 = 55$.

Bien, 55. Simple. Candidato a mínimo.

¿Podemos bajar de 55?

Sigamos explorando inserciones.

(3) Insertar en la ranura inferior y en la ranura superior.

Ranura superior $C \to D$. Opciones:

- $A \to I_1 \to B \to C \to I_2 \to D$:
  $$(0,0)\to(3,4)\to(10,0)\to(10,10)\to(6,2)\to(0,10)\to(0,0)$$

Veamos si es simple. Segmentos:
- $e_1$: $(0,0)\to(3,4)$
- $e_2$: $(3,4)\to(10,0)$
- $e_3$: $(10,0)\to(10,10)$ (lado derecho)
- $e_4$: $(10,10)\to(6,2)$
- $e_5$: $(6,2)\to(0,10)$
- $e_6$: $(0,10)\to(0,0)$ (lado izquierdo)

Intersecciones:
- $e_4$: $(10,10)\to(6,2)$, $m=2$, $y=2x-10$, $x\in[6,10]$.
- $e_5$: $(6,2)\to(0,10)$, $m=\frac{8}{-6}=-\frac43$, $y=10-\frac43x$, $x\in[0,6]$.
Son adyacentes en $(6,2)$, comparten extremo. Bien.

- $e_2$: $(3,4)\to(10,0)$, $m=-\frac47$, $y=-\frac47x+\frac{40}{7}$, $x\in[3,10]$.
  - con $e_4$: ya vimos que $e_2$ y $e_4$ se cruzan (ver caso anterior). Intersección en $x=\frac{55}{9}\approx6.11\in[6,10]$, y en $e_2$ rango $[3,10]$. **Intersección → no simple.**

- $A \to I_2(6,2) \to B \to C \to I_1(3,4) \to D$:
  $$(0,0)\to(6,2)\to(10,0)\to(10,10)\to(3,4)\to(0,10)\to(0,0)$$

Segmentos:
- $e_1$: $(0,0)\to(6,2)$
- $e_2$: $(6,2)\to(10,0)$
- $e_3$: $(10,0)\to(10,10)$
- $e_4$: $(10,10)\to(3,4)$
- $e_5$: $(3,4)\to(0,10)$
- $e_6$: $(0,10)\to(0,0)$

Intersecciones:
- $e_4$: $(10,10)\to(3,4)$, $m=\frac67$, $y=\frac67x+\frac{10}{7}$, $x\in[3,10]$.
- $e_5$: $(3,4)\to(0,10)$, $m=-2$, $y=10-2x$, $x\in[0,3]$. Adyacentes en $(3,4)$.

- $e_2$: $(6,2)\to(10,0)$, $m=-\frac12$, $y=5-\frac12x$, $x\in[6,10]$.
  - con $e_4$: $5-\frac12x = \frac67x+\frac{10}{7}$. Multiplico por 14: $70-7x = 12x+20$, $50=19x$, $x=\frac{50}{19}\approx2.63$, fuera de $[6,10]$. No.
  - con $e_5$: dominios disjuntos ($e_2$: $x\in[6,10]$, $e_5$: $x\in[0,3]$). No.

- $e_1$: $(0,0)\to(6,2)$, $m=\frac13$, $y=\frac13x$, $x\in[0,6]$.
  - con $e_4$: $\frac13x = \frac67x+\frac{10}{7}$. Multiplico por 21: $7x=18x+30$, $x=-\frac{30}{11}$, fuera. No.
  - con $e_5$: $e_5$ rango $[0,3]$, $e_1$ rango $[0,6]$. Intersección $\frac13x = 10-2x$, $\frac73x=10$, $x=\frac{30}{7}\approx4.29$. Rango de $e_5$: $[0,3]$. $x=4.29$ fuera de $e_5$. No.

Simple. Área:

Puntos:
1. $(0,0)$
2. $(6,2)$
3. $(10,0)$
4. $(10,10)$
5. $(3,4)$
6. $(0,10)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: 0
- $v_2\to v_3$: $6\cdot0 - 10\cdot2 = -20$
- $v_3\to v_4$: $10\cdot10 - 10\cdot0 = 100$
- $v_4\to v_5$: $10\cdot4 - 3\cdot10 = 40-30=10$
- $v_5\to v_6$: $3\cdot10 - 0\cdot4 = 30$
- $v_6\to v_7$: 0

Suma = $0-20+100+10+30+0=120$

Área = $120/2=60$.

60, no es mejor que 55.

(4) Insertar en la ranura inferior y en la ranura izquierda.

Ranura izquierda $D \to A$. Opciones:

- $A \to I_1 \to B \to C \to D \to I_2 \to A$:
  $$(0,0)\to(3,4)\to(10,0)\to(10,10)\to(0,10)\to(6,2)\to(0,0)$$

Segmentos:
- $e_1$: $(0,0)\to(3,4)$
- $e_2$: $(3,4)\to(10,0)$
- $e_3$: $(10,0)\to(10,10)$
- $e_4$: $(10,10)\to(0,10)$
- $e_5$: $(0,10)\to(6,2)$
- $e_6$: $(6,2)\to(0,0)$

Intersecciones:
- $e_5$: $(0,10)\to(6,2)$, $m=-\frac43$, $y=10-\frac43x$, $x\in[0,6]$.
- $e_6$: $(6,2)\to(0,0)$, $m=\frac13$, $y=\frac13x$, $x\in[0,6]$. Adyacentes en $(6,2)$.

- $e_2$: $(3,4)\to(10,0)$, $m=-\frac47$, $y=-\frac47x+\frac{40}{7}$, $x\in[3,10]$.
  - con $e_5$: dominios $[3,10]$ vs $[0,6]$, solapan en $[3,6]$. Intersección: $-\frac47x+\frac{40}{7} = 10-\frac43x$.
  Multiplico por 21: $-12x+120 = 210-28x$, $16x=90$, $x=\frac{45}{8}=5.625\in[3,6]$. $y \approx -\frac47\cdot5.625+\frac{40}{7} = -3.214+5.714 = 2.5$. **Intersección → no simple.**

- $A \to I_2(6,2) \to B \to C \to D \to I_1(3,4) \to A$:
  $$(0,0)\to(6,2)\to(10,0)\to(10,10)\to(0,10)\to(3,4)\to(0,0)$$

Segmentos:
- $e_1$: $(0,0)\to(6,2)$
- $e_2$: $(6,2)\to(10,0)$
- $e_3$: $(10,0)\to(10,10)$
- $e_4$: $(10,10)\to(0,10)$
- $e_5$: $(0,10)\to(3,4)$
- $e_6$: $(3,4)\to(0,0)$

Intersecciones:
- $e_5$: $(0,10)\to(3,4)$, $m=-2$, $y=10-2x$, $x\in[0,3]$.
- $e_6$: $(3,4)\to(0,0)$, $m=\frac43$, $y=\frac43x$, $x\in[0,3]$. Adyacentes en $(3,4)$.

- $e_2$: $(6,2)\to(10,0)$, $m=-\frac12$, $y=5-\frac12x$, $x\in[6,10]$.
  - con $e_5$: dominios disjuntos. No.
  - con $e_6$: dominios disjuntos. No.

- $e_1$: $(0,0)\to(6,2)$, $m=\frac13$, $y=\frac13x$, $x\in[0,6]$.
  - con $e_5$: dominios solapan en $[0,3]$. Intersección: $\frac13x = 10-2x$, $\frac73x=10$, $x=\frac{30}{7}\approx4.29$, fuera de $[0,3]$. No.
  - con $e_6$: ambas pasan por $(0,0)$, adyacentes (e_6 termina en $(0,0)$, e_1 empieza en $(0,0)$). Además, ¿se cruzan en otro punto? Son rectas distintas que pasan por $(0,0)$, solo se cruzan ahí. Bien.

Simple. Área:

Puntos:
1. $(0,0)$
2. $(6,2)$
3. $(10,0)$
4. $(10,10)$
5. $(0,10)$
6. $(3,4)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: 0
- $v_2\to v_3$: $-20$
- $v_3\to v_4$: $100$
- $v_4\to v_5$: $100$
- $v_5\to v_6$: $0\cdot4 - 3\cdot10 = -30$
- $v_6\to v_7$: $3\cdot0 - 0\cdot4 = 0$

Suma = $0-20+100+100-30+0=150$

Área = $150/2=75$. 

Ese es el mismo 75, el máximo.

(5) Insertar solo en la ranura derecha y en la superior, etc.

Nos queda explorar inserciones en ranuras no contiguas (derecha y superior; derecha e izquierda; superior e izquierda). Pero por simetría rotacional del cuadrado (aunque los puntos interiores no son simétricos), debemos considerar las distintas.

Sin embargo, para minimizar el área, la mejor estrategia parece ser **insertar los dos puntos interiores en ranuras adyacentes** de modo que las poligonales se acerquen y el área encerrada se reduzca.

El mínimo encontrado hasta ahora es **55** en el caso:

$$(0,0)\to(6,2)\to(10,0)\to(3,4)\to(10,10)\to(0,10)\to(0,0)$$

con área 55.

¿Podemos encontrar una configuración con área menor que 55 revisando las ranuras derecha e izquierda (opuestas)?

(6) Insertar en ranura derecha ($B$–$C$) y ranura izquierda ($D$–$A$).

Opciones:

- $A \to B \to I_1 \to C \to D \to I_2 \to A$:
  $$(0,0)\to(10,0)\to(3,4)\to(10,10)\to(0,10)\to(6,2)\to(0,0)$$

Segmentos:
- $e_1$: $(0,0)\to(10,0)$
- $e_2$: $(10,0)\to(3,4)$
- $e_3$: $(3,4)\to(10,10)$
- $e_4$: $(10,10)\to(0,10)$
- $e_5$: $(0,10)\to(6,2)$
- $e_6$: $(6,2)\to(0,0)$

Intersecciones:
- $e_2$: $(10,0)\to(3,4)$, $m=-\frac47$, $y=-\frac47x+\frac{40}{7}$, $x\in[3,10]$.
- $e_3$: $(3,4)\to(10,10)$, $m=\frac67$, $y=\frac67x+\frac{10}{7}$, $x\in[3,10]$. Adyacentes en $(3,4)$.

- $e_5$: $(0,10)\to(6,2)$, $m=-\frac43$, $y=10-\frac43x$, $x\in[0,6]$.
- $e_6$: $(6,2)\to(0,0)$, $m=\frac13$, $y=\frac13x$, $x\in[0,6]$. Adyacentes en $(6,2)$.

- $e_5$ con $e_3$: dominios solapan en $[3,6]$. Intersección: $10-\frac43x = \frac67x+\frac{10}{7}$. Multiplico por 21: $210-28x = 18x+30$, $180=46x$, $x=\frac{90}{23}\approx3.913\in[3,6]$, $y\approx4.78$. **Intersección → no simple.**

- $A\to B \to I_2 \to C \to D \to I_1 \to A$:
  $$(0,0)\to(10,0)\to(6,2)\to(10,10)\to(0,10)\to(3,4)\to(0,0)$$

Segmentos:
- $e_1$: $(0,0)\to(10,0)$
- $e_2$: $(10,0)\to(6,2)$
- $e_3$: $(6,2)\to(10,10)$
- $e_4$: $(10,10)\to(0,10)$
- $e_5$: $(0,10)\to(3,4)$
- $e_6$: $(3,4)\to(0,0)$

Intersecciones:
- $e_2$: $(10,0)\to(6,2)$, $m=-\frac12$, $y=5-\frac12x$, $x\in[6,10]$.
- $e_3$: $(6,2)\to(10,10)$, $m=2$, $y=2x-10$, $x\in[6,10]$. Adyacentes en $(6,2)$.

- $e_5$: $(0,10)\to(3,4)$, $m=-2$, $y=10-2x$, $x\in[0,3]$.
- $e_6$: $(3,4)\to(0,0)$, $m=\frac43$, $y=\frac43x$, $x\in[0,3]$. Adyacentes.

- $e_2$ con $e_5$: dominios disjuntos. No.
- $e_3$ con $e_5$: dominios disjuntos. No.
- $e_3$ con $e_6$: dominios $[6,10]$ vs $[0,3]$, disjuntos. No.
- $e_2$ con $e_6$: disjuntos. No.

Simple. Área:

Puntos:
1. $(0,0)$
2. $(10,0)$
3. $(6,2)$
4. $(10,10)$
5. $(0,10)$
6. $(3,4)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: $0\cdot0-10\cdot0=0$
- $v_2\to v_3$: $10\cdot2 - 6\cdot0 = 20$
- $v_3\to v_4$: $6\cdot10 - 10\cdot2 = 60-20=40$
- $v_4\to v_5$: $10\cdot10 - 0\cdot10 = 100$
- $v_5\to v_6$: $0\cdot4 - 3\cdot10 = -30$
- $v_6\to v_7$: $3\cdot0 - 0\cdot4 = 0$

Suma = $0+20+40+100-30+0=130$

Área = $130/2=65$.

65, no es mínimo.

(7) Insertar en ranura superior y ranura izquierda.

- $A \to B \to C \to I_1 \to D \to I_2 \to A$:
  $$(0,0)\to(10,0)\to(10,10)\to(3,4)\to(0,10)\to(6,2)\to(0,0)$$

Segmentos:
- $e_3$: $(10,10)\to(3,4)$, $m=\frac67$, $y=\frac67x+\frac{10}{7}$, $x\in[3,10]$.
- $e_4$: $(3,4)\to(0,10)$, $m=-2$, $y=10-2x$, $x\in[0,3]$.
- $e_5$: $(0,10)\to(6,2)$, $m=-\frac43$, $y=10-\frac43x$, $x\in[0,6]$.
- $e_6$: $(6,2)\to(0,0)$, $m=\frac13$, $y=\frac13x$, $x\in[0,6]$.

Intersecciones:
- $e_4$ con $e_6$: $e_4$: $y=10-2x$, $x\in[0,3]$; $e_6$: $y=\frac13x$, $x\in[0,6]$. Intersección: $10-2x=\frac13x$, $10=\frac73x$, $x=\frac{30}{7}\approx4.29$, fuera del rango $[0,3]$ de $e_4$. No.

- $e_5$ con $e_3$: dominios solapan en $[3,6]$. Intersección: $10-\frac43x = \frac67x+\frac{10}{7}$. Ya calculé: $x=\frac{90}{23}\approx3.913\in[3,6]$, intersección. **No simple.**

- $A \to B \to C \to I_2 \to D \to I_1 \to A$:
  $$(0,0)\to(10,0)\to(10,10)\to(6,2)\to(0,10)\to(3,4)\to(0,0)$$

Segmentos:
- $e_3$: $(10,10)\to(6,2)$, $m=2$, $y=2x-10$, $x\in[6,10]$.
- $e_4$: $(6,2)\to(0,10)$, $m=-\frac43$, $y=10-\frac43x$, $x\in[0,6]$.
- $e_5$: $(0,10)\to(3,4)$, $m=-2$, $y=10-2x$, $x\in[0,3]$.
- $e_6$: $(3,4)\to(0,0)$, $m=\frac43$, $y=\frac43x$, $x\in[0,3]$.

Intersecciones:
- $e_4$ con $e_6$: dominios solapan en $[0,3]$. Intersección: $10-\frac43x = \frac43x$, $10=\frac83x$, $x=\frac{30}{8}=3.75$, fuera de $[0,3]$. No.

- $e_3$ con $e_5$: dominios disjuntos. No.
- $e_3$ con $e_6$: dominios disjuntos. No.

- $e_4$ con $e_5$: adyacentes en $(0,10)$? No, $e_4$ termina en $(0,10)$, $e_5$ empieza en $(0,10)$. Adyacentes. Bien.

Simple. Área:

Puntos:
1. $(0,0)$
2. $(10,0)$
3. $(10,10)$
4. $(6,2)$
5. $(0,10)$
6. $(3,4)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: 0
- $v_2\to v_3$: $10\cdot10-10\cdot0=100$
- $v_3\to v_4$: $10\cdot2 - 6\cdot10 = 20-60=-40$
- $v_4\to v_5$: $6\cdot10 - 0\cdot2 = 60$
- $v_5\to v_6$: $0\cdot4 - 3\cdot10 = -30$
- $v_6\to v_7$: $3\cdot0 - 0\cdot4=0$

Suma = $0+100-40+60-30+0 = 90$

Área = $90/2=45$.

¡45! Menor que 55. Simple según el análisis. Buen candidato.

Revisemos de nuevo la simplicidad de este candidato con más cuidado. Los segmentos:

- $e_1$: $(0,0)\to(10,0)$
- $e_2$: $(10,0)\to(10,10)$
- $e_3$: $(10,10)\to(6,2)$
- $e_4$: $(6,2)\to(0,10)$
- $e_5$: $(0,10)\to(3,4)$
- $e_6$: $(3,4)\to(0,0)$

Pares no adyacentes a verificar:
- $e_1$ vs $e_3$: $e_1$: $y=0$, $x\in[0,10]$. $e_3$: $y=2x-10$, $x\in[6,10]$, $y\in[2,10]$. No toca $y=0$ salvo en $x=5$ que no está en $[6,10]$. No.
- $e_1$ vs $e_4$: $e_4$: $y=10-\frac43x$, $x\in[0,6]$, $y\in[10,2]$. No toca $y=0$ (en $x=7.5$, fuera del rango). No.
- $e_1$ vs $e_5$: $e_5$: $y=10-2x$, $x\in[0,3]$, $y\in[10,4]$. No toca $y=0$. No.
- $e_2$ vs $e_4$: $e_2$: $x=10$, $y\in[0,10]$. $e_4$: $x\in[0,6]$. No se tocan (salvo si $(10, y)$ estuviera en $e_4$, pero $e_4$ no llega a $x=10$). No.
- $e_2$ vs $e_5$: $e_2$: $x=10$; $e_5$: $x\in[0,3]$. No.
- $e_2$ vs $e_6$: $e_2$: $x=10$; $e_6$: $x\in[0,3]$. No.
- $e_3$ vs $e_5$: dominios $[6,10]$ vs $[0,3]$, disjuntos. No.
- $e_3$ vs $e_6$: dominios disjuntos. No.
- $e_4$ vs $e_6$: ya revisado, no se cruzan (la intersección de rectas está en $x=3.75$, fuera de $[0,3]$).

Confirmamos que es un polígono simple. Área 45.

¿Podemos mejorar aún más? Probemos las variantes que faltan.

Hemos explorado:
- (1) Ambos interiores en la misma ranura: áreas 81, 89 (ranura inferior). En otras ranuras por simetría, las áreas serán análogas o mayores. No es mínimo.
- (2) Ranura inferior + derecha: 55 (simple), otro no simple.
- (3) Ranura inferior + superior: 60 (simple), otro no simple.
- (4) Ranura inferior + izquierda: 75 (simple), otro no simple.
- (5) Ranura derecha + izquierda: 65 (simple), otro no simple.
- (6) Ranura superior + izquierda: 45 (simple) ← mejor hasta ahora, otro no simple.

Queda ranura derecha + superior:

(7) Ranura derecha ($B$–$C$) y superior ($C$–$D$).

- $A \to B \to I_1 \to C \to I_2 \to D \to A$:
  $$(0,0)\to(10,0)\to(3,4)\to(10,10)\to(6,2)\to(0,10)\to(0,0)$$

Segmentos:
- $e_2$: $(10,0)\to(3,4)$, $m=-\frac47$, $y=-\frac47x+\frac{40}{7}$.
- $e_3$: $(3,4)\to(10,10)$, $m=\frac67$, $y=\frac67x+\frac{10}{7}$. Adyacentes en $(3,4)$.
- $e_4$: $(10,10)\to(6,2)$, $m=2$, $y=2x-10$, $x\in[6,10]$.
- $e_5$: $(6,2)\to(0,10)$, $m=-\frac43$, $y=10-\frac43x$, $x\in[0,6]$. Adyacentes en $(6,2)$.

Intersecciones:
- $e_2$ con $e_4$: ya calculado, se cruzan en $x=\frac{55}{9}\approx6.11\in[6,10]\cap[3,10]$. **No simple.**

- $A \to B \to I_2 \to C \to I_1 \to D \to A$:
  $$(0,0)\to(10,0)\to(6,2)\to(10,10)\to(6,2)?$$

Espera, repitamos: $I_2=(6,2)$ va en la ranura derecha, $I_1=(3,4)$ en la superior.

Secuencia:
$$(0,0)\to(10,0)\to(6,2)\to(10,10)\to(3,4)\to(0,10)\to(0,0)$$

Segmentos:
- $e_2$: $(10,0)\to(6,2)$, $m=-\frac12$, $y=5-\frac12x$, $x\in[6,10]$.
- $e_3$: $(6,2)\to(10,10)$, $m=2$, $y=2x-10$, $x\in[6,10]$.
- $e_4$: $(10,10)\to(3,4)$, $m=\frac67$, $y=\frac67x+\frac{10}{7}$, $x\in[3,10]$.
- $e_5$: $(3,4)\to(0,10)$, $m=-2$, $y=10-2x$, $x\in[0,3]$.

Intersecciones:
- $e_2$ con $e_4$: $5-\frac12x = \frac67x+\frac{10}{7}$. Multiplico por 14: $70-7x=12x+20$, $50=19x$, $x=\frac{50}{19}\approx2.63$, fuera de $[6,10]\cap[3,10]=[6,10]$. No.

- $e_2$ con $e_5$: dominios $[6,10]$ vs $[0,3]$, disjuntos. No.
- $e_3$ con $e_5$: dominios $[6,10]$ vs $[0,3]$, disjuntos. No.
- $e_3$ con $e_4$: adyacentes en $(10,10)$? No: $e_3$ termina en $(10,10)$, $e_4$ empieza en $(10,10)$. Adyacentes. Bien.

- $e_1$ interacciones ya cubiertas anteriormente (bordes no se cruzan con internos en rangos disjuntos).

Simple. Área:

Puntos:
1. $(0,0)$
2. $(10,0)$
3. $(6,2)$
4. $(10,10)$
5. $(3,4)$
6. $(0,10)$
7. $(0,0)$

Suma:
- $v_1\to v_2$: 0
- $v_2\to v_3$: $10\cdot2 - 6\cdot0 = 20$
- $v_3\to v_4$: $6\cdot10 - 10\cdot2 = 60-20=40$
- $v_4\to v_5$: $10\cdot4 - 3\cdot10 = 40-30=10$
- $v_5\to v_6$: $3\cdot10 - 0\cdot4 = 30$
- $v_6\to v_7$: $3\cdot0 - 0\cdot4=0$? Cuidado, $v_6=(0,10)$, $v_7=(0,0)$: $0\cdot0 - 0\cdot10 = 0$.

Suma = $0+20+40+10+30+0 = 100$

Área = $100/2 = 50$.

50, no es mejor que 45.

¿Hay alguna combinación que dé menos que 45? Revisemos los casos de interiores en ranuras no contiguas con órdenes que quizá no hemos probado. En principio, con las esquinas en orden convexo y los interiores asignados a ranuras, hay que elegir:

- qué ranura recibe cada interior,
- el orden de los interiores si comparten ranura.

Hemos cubierto en esencia todas las particiones de los 2 interiores en 4 ranuras. Para cada partición, alguno de los órdenes resultó simple en un caso (el otro se auto-intersecó). Los valores de área simple mínima entre los casos:

- Ambos en una ranura: 81, 89.
- Inferior + derecha: 55.
- Inferior + superior: 60.
- Inferior + izquierda: 75.
- Derecha + izquierda: 65.
- Superior + izquierda: 45. ← mínimo
- Derecha + superior: 50.

Espera, también hay que considerar el caso en que los interiores están en ranuras adyacentes en el otro sentido, pero ya están cubiertos por simetría. Hemos listado todas las 6 parejas de ranuras (hay $\binom42=6$) y el caso de ambos en la misma ranura. El mínimo entre los simples es 45.

Pero antes de concluir, ¿seguro que en el caso (6) superior + izquierda no hay otra disposición con área menor? En ese caso solo fue simple la variante $(0,0)\to(10,0)\to(10,10)\to(6,2)\to(0,10)\to(3,4)\to(0,0)$ con área 45. La otra variante fue no simple. Así que para esa partición, 45 es el valor.

Revisemos una vez más la simplicidad y el área del candidato de 45, porque es el mínimo propuesto. El recorrido con rótulos sería:

$$R=(0,0), A=(10,0), N=(10,10), D=(6,2), O=(0,10), M=(3,4)$$

dando el ciclo cerrado $(0,0)\to(10,0)\to(10,10)\to(6,2)\to(0,10)\to(3,4)\to(0,0)$.

Dibujo mental: comienza en la esquina inferior izquierda del cuadrado, recorre el borde inferior hacia la derecha, sube por el borde derecho hasta la esquina superior derecha, luego baja hacia $(6,2)$ (interior), sube a $(0,10)$ (esquina superior izquierda), baja hacia $(3,4)$ (interior), y vuelve al origen. Este es un polígono cóncavo (la muesca principal es el triángulo grande que queda fuera cerca del centro bajo y otro recorte).

Verificación de no auto-intersección, la hicimos y no encontramos cruces.

Cálculo del área 45 también parece correcto.

## 8. Verificación independiente del área 45 por descomposición

Podemos comprobar el área del polígono restando del cuadrado ($100$) las áreas de las regiones que quedan fuera.

Recorrido en sentido antihorario: $(0,0)\to(10,0)\to(10,10)\to(6,2)\to(0,10)\to(3,4)\to(0,0)$.

Identifiquemos qué partes del cuadrado quedan fuera. Recortes:

1. Al ir de $(10,10)$ a $(6,2)$ y de $(6,2)$ a $(0,10)$, se forma una muesca cuya frontera exterior sería el camino convexo $(10,10)\to(0,10)$ (borde superior). El área fuera es el área delimitada por esos segmentos.

Calculemos el área de la región del cuadrado que queda **dentro** del polígono sumando por integración o por shoelace (ya lo hicimos: 45). Verifiquemos con descomposición:

El área fuera del polígono pero dentro del cuadrado se compone de:

- La región por encima del segmento $e_3:(10,10)\to(6,2)$ y $e_4:(6,2)\to(0,10)$ y por debajo del borde superior $y=10$.

Consideremos la poligonal $P = (10,10) \to (6,2) \to (0,10)$ frente al borde superior del cuadrado $(10,10)\to(0,10)$. El área encerrada entre el borde superior y la poligonal $P$ es el área exterior de la muesca superior.

Calculemos área entre $y=10$ y la poligonal $P$ que baja hasta $(6,2)$ y vuelve a subir a $(0,10)$.

Segmento $(10,10)\to(6,2)$: $y = 2x - 10$ para $x\in[6,10]$.
Segmento $(6,2)\to(0,10)$: $y = 10 - \frac43 x$ para $x\in[0,6]$.

Área entre $y=10$ y estos segmentos:

- De $x=0$ a $x=6$: altura $10 - (10-\frac43x) = \frac43x$. Integral: $\int_0^6 \frac43 x\,dx = \frac43 \cdot \frac{6^2}{2} = \frac43 \cdot 18 = 24$.

- De $x=6$ a $x=10$: altura $10 - (2x-10) = 20 - 2x$. Integral: $\int_6^{10} (20-2x)\,dx = [20x - x^2]_6^{10} = (200-100) - (120-36) = 100 - 84 = 16$.

Área total de la muesca superior fuera = $24+16=40$.

- Ahora la muesca del lado izquierdo: la poligonal $(0,10)\to(3,4)\to(0,0)$ frente al borde izquierdo del cuadrado $x=0$.

El área entre el borde $x=0$ (con $y$ de 0 a 10) y la poligonal $(0,10)\to(3,4)\to(0,0)$.

Segmento $(0,10)\to(3,4)$: $y=10-2x$, $x\in[0,3]$.
Segmento $(3,4)\to(0,0)$: $y=\frac43x$, $x\in[0,3]$.

Visto desde el eje $y$: para cada $x\in[0,3]$, la anchura de la región exterior es $x$ (desde $x=0$ hasta la poligonal). Más concretamente, la región exterior entre el borde izquierdo y la poligonal va de $x=0$ a la línea de la poligonal.

Para $x$ entre 0 y 3, la poligonal tiene dos valores de $y$ para un mismo $x$ en dos partes. Mejor pensemos en la región cerrada por el borde $x=0$ y la poligonal. Es un triángulo con vértices $(0,0)$, $(0,10)$, y $(3,4)$.

Área del triángulo $(0,0),(0,10),(3,4)$: base vertical 10, altura horizontal 3, área = $\frac12\cdot 10 \cdot 3 = 15$.

Pero cuidado: la poligonal consta de dos segmentos $(0,10)\to(3,4)$ y $(3,4)\to(0,0)$. El triángulo $(0,0),(0,10),(3,4)$ es exactamente la región que queda entre el borde $x=0$ y la poligonal. Sí.

Entonces la muesca izquierda exterior tiene área 15.

Total área exterior dentro del cuadrado: $40+15 = 55$.

Área del polígono = $100 - 55 = 45$. Coincide.

Veamos si no solapamos regiones: la muesca superior está en la parte superior, la muesca izquierda en la izquierda. ¿Se solapan? Veamos el segmento $(0,10)\to(3,4)$ forma parte de ambas? En realidad la poligonal $(10,10)\to(6,2)\to(0,10)\to(3,4)\to(0,0)$ forma un solo recorte conectado que va desde la esquina superior derecha, baja al interior, sube a la esquina superior izquierda, baja al interior $(3,4)$, y al origen. Las regiones exteriores calculadas (40 y 15) corresponden a dos «dientes» del recorte. ¿Se solapan? El primer diente está por encima de la línea $(6,2)\to(0,10)$ y el borde superior; el segundo diente está a la izquierda del borde izquierdo y la poligonal $(0,10)\to(3,4)\to(0,0)$. Comparten el punto $(0,10)$ pero no se solapan porque uno está arriba (y entre $x=0$ y $6$ va hacia abajo hasta $y=2$) y el otro está a la izquierda (bajando por $x$ cercano a 0). No se solapan ya que el primer diente ocupa $y$ hasta cerca de 2 en $x=6$ y en $x=0$ está en $y=10$; el segundo diente ocupa desde $y=10$ hasta $y=0$ en $x$ cerca de 0. En la parte donde $x\in[0,3]$ y además está en el primer diente, ¿hay solape? El primer diente en $x=0$ tiene punto $(0,10)$, y para $x\in(0,6]$ el límite inferior del diente es la recta $y=10-\frac43x$. El segundo diente ocupa $x\in[0,3]$, entre $y=10-2x$ (abajo) y $y=\frac43x$? No, espera. La región del segundo diente es el triángulo $(0,0),(0,10),(3,4)$. El primer diente es la región entre $y=10$ y $y=10-\frac43x$ para $x\in[0,6]$. El segundo diente es el triángulo a la izquierda de la línea $(0,10)\to(3,4)$ y la línea $(3,4)\to(0,0)$.

¿Se solapan el primer diente y el segundo diente? El primer diente se extiende para $x\in[0,6]$ entre $y=10-\frac43x$ y $y=10$. En particular en $x=3$: primer diente entre $y=10-\frac43(3)=6$ y $y=10$. El segundo diente en $x=3$: la región del triángulo en $x=3$ se reduce al punto $(3,4)$ (el triángulo se estrecha). Para $x$ pequeño, digamos $x=1$: segundo diente: el triángulo $(0,0),(0,10),(3,4)$ en $x=1$ tiene $y$ entre (arriba) $y=10-2(1)=8$ y (abajo) $y=\frac43(1)=1.333$. Primer diente en $x=1$: entre $y=10-\frac43(1)=8.667$ y $y=10$. Se solapan en $y\in[8.667,8]$? No, no hay solape: primer diente desde 8.667 hasta 10; segundo diente desde 1.333 hasta 8. Son disjuntos. En $x=0$: primer diente solo $(0,10)$; segundo diente en $x=0$ es el segmento vertical $(0,0)-(0,10)$. Comparten solo $(0,10)$, un punto. Por lo tanto, no se solapan. La suma $40+15=55$ es correcta.

Área dentro del polígono = $100-55=45$. Verificado.

Pero espera, hay una región que quizá queda **dentro** del polígono y no la hemos restado. Déjame ver la cadena de segmentos nuevamente: 

$(0,0) \to (10,0) \to (10,10) \to (6,2) \to (0,10) \to (3,4) \to (0,0)$.

La frontera: borde inferior completo, borde derecho completo, luego diagonal-ish hacia el interior $(6,2)$, luego hacia $(0,10)$, luego hacia el interior $(3,4)$, luego al origen.

El interior del polígono está a la izquierda de cada arista (recorrido antihorario). Entonces:

- Al recorrer borde inferior a la derecha, interior arriba. Correcto.
- Borde derecho hacia arriba, interior a la izquierda (dentro del cuadrado). Correcto.
- $(10,10)\to(6,2)$: interior a la izquierda de este segmento. La izquierda de este segmento apunta hacia la esquina inferior derecha / centro del cuadrado.
- $(6,2)\to(0,10)$: interior a la izquierda. Izquierda de este segmento (que va hacia arriba-izquierda) apunta hacia abajo-izquierda.
- $(0,10)\to(3,4)$: interior a la izquierda.
- $(3,4)\to(0,0)$: interior a la izquierda.

Visualicemos: el polígono encierra la mitad inferior derecha del cuadrado, y deja fuera una gran región superior y una región izquierda. El área dentro tiene forma de «L» o un pentágono raro. El cómputo 45 parece consistente.

## 9. ¿Es 45 realmente el mínimo?

Revisemos si existe una configuración simple con área aún menor que 45.

Consideremos el caso de ranura derecha + superior que dio 50 (casi). La de superior + izquierda dio 45. ¿Por qué no hay algo por debajo de 40? 

Podemos buscar un polígono simple que encierre aún menos área, quizá con los interiores en ranuras opuestas y de manera que el recorte sea máximo. Hemos enumerado todas las posiciones en las ranuras respetando el orden convexo de las esquinas. Asumiendo que para un polígono simple las esquinas deben ir en orden convexo, la enumeración es exhaustiva. Por tanto el mínimo es 45.

Sin embargo, verifiquemos esta premisa: ¿Las esquinas de la envolvente convexa de un polígono simple deben recorrer en orden convexo en el ciclo? Sí, si tienes los vértices extremos de la envolvente convexa y el polígono es simple, la frontera del polígono debe contener los bordes de la envolvente en orden cíclico (puede ser un subconjunto de aristas del polígono, intercalando puntos interiores). De lo contrario, un tramo de la frontera cruzaría otro. Para un conjunto de puntos donde los 4 vértices del cuadrado son la envolvente convexa, es correcto.

Por tanto 45 es el área mínima de un hexágono simple sobre esos 6 puntos.

Y el máximo 75 lo confirmamos antes.

## 10. Diferencia

$$a_{\max} - a_{\min} = 75 - 45 = 30.$$

## 11. Respuesta

$$
\boxed{30}
$$