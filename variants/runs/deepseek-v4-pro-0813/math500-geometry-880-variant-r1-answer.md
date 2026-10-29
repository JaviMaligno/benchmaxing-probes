Vamos a resolver el problema.

## 1. Ubicación de la araña y la polilla

La habitación mide:

- Largo (front↔back): $15$ pies
- Ancho (pared lateral a pared lateral): $12$ pies
- Alto (suelo↔techo): $9$ pies

**Araña:** está en una pared lateral ($12 \times 9$), a $1$ pie del techo y a $1$ pie de la pared trasera ($15 \times 9$).

**Polilla:** está en la pared lateral opuesta, a $1$ pie del suelo y a $1$ pie de la pared frontal.

Tomemos un sistema de coordenadas:

- $x$: dirección del largo ($0$ = pared trasera, $15$ = pared frontal)
- $y$: dirección del ancho ($0$ = pared lateral de la araña, $12$ = pared lateral de la polilla)
- $z$: dirección de la altura ($0$ = suelo, $9$ = techo)

Entonces:

- Araña: $x = 1$, $y = 0$, $z = 8$
- Polilla: $x = 14$, $y = 12$, $z = 1$

## 2. Posibles rutas

La araña puede caminar por paredes y techo. Las rutas candidatas se obtienen "desdoblando" la habitación.

### Ruta por el techo

Si la araña sube por su pared lateral hasta el techo, cruza el techo y baja por la pared lateral opuesta, el "desarrollo" tiene:

- Subida en la pared de la araña: $1$ pie
- Cruce del techo: $12$ pies (ancho)
- Bajada en la pared de la polilla: $8$ pies

La distancia lateral (en la dirección del largo) entre araña y polilla es $|14 - 1| = 13$ pies.

Distancia total en línea recta sobre el desarrollo:

$$ \sqrt{(1 + 12 + 8)^2 + 13^2} = \sqrt{21^2 + 13^2} = \sqrt{441 + 169} = \sqrt{610} $$

### Ruta por el suelo

Desarrollo similar, pero bajando hasta el suelo:

- Bajada en la pared de la araña: $8$ pies
- Cruce del suelo: $12$ pies
- Subida en la pared de la polilla: $1$ pie

Distancia:

$$ \sqrt{(8 + 12 + 1)^2 + 13^2} = \sqrt{21^2 + 13^2} = \sqrt{610} $$

Resulta igual que antes, pero aquí la araña solo puede usar **techo y paredes**, no el suelo. Así que esta ruta no es válida.

### Rutas por otras paredes

También se pueden considerar desarrollos que pasan por la pared frontal o trasera.

#### Por la pared trasera

Desarrollo usando la pared trasera:

- Desde la araña hasta la esquina trasera de su pared: $1$ pie (dirección del largo)
- A través de la pared trasera: $12$ pies (ancho)
- Desde la esquina trasera de la pared de la polilla hasta la polilla: $13$ pies (dirección del largo)

La diferencia de altura es $|8 - 1| = 7$ pies.

Distancia sobre el desarrollo:

$$ \sqrt{(1 + 12 + 13)^2 + 7^2} = \sqrt{26^2 + 7^2} = \sqrt{676 + 49} = \sqrt{725} $$

#### Por la pared frontal

- Desde la araña hasta la esquina frontal de su pared: $14$ pies
- A través de la pared frontal: $12$ pies
- Desde la esquina frontal de la pared de la polilla hasta la polilla: $1$ pie

Distancia:

$$ \sqrt{(14 + 12 + 1)^2 + 7^2} = \sqrt{27^2 + 7^2} = \sqrt{729 + 49} = \sqrt{778} $$

#### Pared trasera / frontal pasando por el techo

Combinaciones que incluyen el techo y una de las paredes extremas:

- Subir $1$ pie (al techo), cruzar parcialmente el techo hacia atrás/frente, bajar por la pared extrema, cruzar por la pared lateral opuesta y bajar.

Desarrollo por el techo + pared trasera:

La araña sube al techo ($1$ pie). Desde ahí se mueve hacia la pared trasera ($1$ pie en dirección $x$), baja por la pared trasera hasta la altura de la polilla ($7$ pies), cruza la pared trasera ($12$ pies), y desde la esquina trasera de la pared de la polilla avanza $13$ pies hasta la polilla.

Distancia:

$$ \sqrt{(1 + 1 + 7 + 12 + 13)^2 + 0^2} $$

Esto no es una línea recta en un solo plano; hay que analizar bien el desarrollo. El desarrollo correcto da:

$$ \sqrt{(1 + 7 + 12 + 13)^2 + 1^2} $$

Espera, organicemos mejor.

## 3. Desarrollo sistemático

La superficie transitable se compone de:

- Pared lateral araña: $12 \times 9$
- Pared lateral polilla: $12 \times 9$
- Pared frontal: $15 \times 9$
- Pared trasera: $15 \times 9$
- Techo: $15 \times 12$

Cualquier ruta se representa como un recorrido sobre un desarrollo plano de estas caras. Las distancias mínimas se obtienen uniendo los puntos con una recta en cada desarrollo posible.

### Desarrollo A: techo como puente directo

Ya calculado: $\sqrt{610}$.

### Desarrollo B: techo + pared trasera

Desdoblamos en el orden: pared araña → techo → pared trasera → pared polilla.

- En la pared de la araña, la posición del punto es $(1, 8)$ (en coordenadas largo × alto).
- En el techo, uniendo pared araña y pared trasera, la esquina trasera del techo está a distancia $1$ pie (largo) + las alturas correspondientes.

Calculemos geométricamente. Un desarrollo de 4 caras:

1. Pared araña (largo × alto): esquina trasera inferior en $(0,0)$, esquina frontal inferior en $(15,0)$.
2. Techo (unido al borde superior de la pared araña): el borde superior de la pared araña mapea a $z=9$.
3. Pared trasera (unida al borde trasero del techo).
4. Pared polilla.

La araña está en $(1,8)$ sobre la pared araña. La polilla está en la pared polilla en $(14,1)$.

El desarrollo tiene un eje común. La distancia entre las proyecciones:

- Distancia horizontal total desde la araña hasta la polilla en el desarrollo: 
  - De la araña al borde superior de su pared: $1$ pie (hacia arriba)
  - A través del techo hasta la pared trasera: $1$ pie (hacia atrás)
  - A través de la pared trasera hasta el borde de la pared polilla: $9 - 1 = 8$ pies hacia abajo (la polilla está a $1$ pie del suelo)
  - De la esquina trasera de la pared polilla hasta la polilla: $13$ pies (hacia adelante)

Suma de distancias verticales/horizontales en el desarrollo: $1 + 1 + 8 + 13 = 23$ pies.

La distancia perpendicular (a través del ancho): $12$ pies.

Distancia:

$$ \sqrt{23^2 + 12^2} = \sqrt{529 + 144} = \sqrt{673} $$

### Desarrollo C: techo + pared frontal

Similar, pero por la pared frontal:

- De la araña al borde superior: $1$
- A través del techo hasta la pared frontal: $14$
- A través de la pared frontal hacia abajo: $8$
- Desde la esquina frontal de la pared polilla hasta la polilla: $1$

Suma: $1 + 14 + 8 + 1 = 24$

Distancia:

$$ \sqrt{24^2 + 12^2} = \sqrt{576 + 144} = \sqrt{720} $$

### Desarrollo D: pared trasera (sin techo)

Ya calculado: $\sqrt{725}$.

### Desarrollo E: pared frontal (sin techo)

Ya calculado: $\sqrt{778}$.

### Desarrollo F: techo + pared trasera (variante con distinta unión)

Consideremos el desarrollo con la araña subiendo al techo y luego a la pared trasera, pero la polilla también subiendo. Existe otra forma de unir las caras.

Hay un desarrollo adicional: pared araña → pared trasera → techo → pared polilla.

- Araña en pared araña: a $1$ pie de la pared trasera y $1$ pie del techo.
- La polilla en pared polilla: a $1$ pie de la pared frontal y $1$ pie del suelo.

En este desarrollo, la araña se mueve lateralmente hacia la pared trasera ($1$ pie), luego sube por la pared trasera hasta el techo (diferencia de altura entre la araña y el techo ya es $1$ pie → queda en el techo), cruza el techo y baja.

Distancia horizontal acumulada en el desarrollo:

- Araña → esquina trasera de su pared: $1$
- Subida al techo: $1$
- Cruce del techo hasta pared polilla: $12$ (ancho)
- Bajada en pared polilla: $8$ (hasta la altura de la polilla a $1$ pie del suelo)
- Avance hacia la polilla: $13$

Suma: $1 + 1 + 12 + 8 + 13 = 35$

Distancia:

$$ \sqrt{35^2 + 0^2} $$

No, esto sería solo si todo estuviera alineado, lo cual no es el caso. La distancia perpendicular es $12$ pies (el ancho), porque cruzar de una pared lateral a otra es perpendicular.

Esto es incoherente. El método correcto es mantener dos ejes en el desarrollo.

## 4. Método general correcto

Para cada desarrollo, calculamos la distancia euclidiana entre las coordenadas de los dos puntos en el plano. Los desarrollos relevantes son los que unen las caras de forma que los puntos queden conectados.

Los desarrollos posibles (5 caras, usando solo paredes y techo) son:

1. **Araña pared → techo → polilla pared** (cruce directo por el techo)
2. **Araña pared → pared trasera → polilla pared** (cruce por pared trasera)
3. **Araña pared → pared frontal → polilla pared** (cruce por pared frontal)
4. **Araña pared → techo → pared trasera → polilla pared**
5. **Araña pared → pared trasera → techo → polilla pared**
6. **Araña pared → techo → pared frontal → polilla pared**
7. **Araña pared → pared frontal → techo → polilla pared**

Calculamos todos y elegimos el mínimo.

### Caso 1: techo directo
$$ \sqrt{(1 + 12 + 8)^2 + 13^2} = \sqrt{21^2 + 13^2} = \sqrt{610} $$

### Caso 2: pared trasera
$$ \sqrt{(1 + 12 + 13)^2 + 7^2} = \sqrt{26^2 + 7^2} = \sqrt{725} $$

### Caso 3: pared frontal
$$ \sqrt{(14 + 12 + 1)^2 + 7^2} = \sqrt{27^2 + 7^2} = \sqrt{778} $$

### Caso 4: techo + pared trasera (orden: techo → trasera)
Desarrollo: araña sube al techo, camina hacia atrás por el techo, baja por pared trasera, cruza a pared polilla, avanza hacia polilla.

Distancia en el eje horizontal del desarrollo: $1 + 1 + 8 + 13 = 23$

Distancia en el eje perpendicular (ancho): $12$

$$ \sqrt{23^2 + 12^2} = \sqrt{673} $$

### Caso 5: pared trasera + techo (orden: trasera → techo)
Desarrollo: araña camina hacia atrás, sube por pared trasera al techo, cruza techo, baja en pared polilla, avanza hacia polilla.

Distancia en el eje horizontal: $1 + 8 + 12 + 8 + 13$ — espera, revisemos.

La araña está a $1$ pie del techo ($z=8$). Para subir por la pared trasera, primero camina $1$ pie hacia atrás ($x$ de 1 a 0), luego sube $1$ pie en la pared trasera ($z$ de 8 a 9), llega al techo, cruza el techo $12$ pies (ancho), baja en pared polilla $8$ pies ($z$ de 9 a 1), y avanza $13$ pies ($x$ de 1 a 14, si la polilla está a $x=14$ desde la parte trasera).

Distancia en el eje del desarrollo (suma de todos los segmentos en línea recta): $1 + 1 + 12 + 8 + 13 = 35$

Distancia perpendicular: $0$ (todo en el mismo plano)

Pero esto no es correcto porque al desdoblar, no todos los segmentos van en la misma dirección. El desarrollo correcto asigna cada segmento a un eje.

Mejor: en el desarrollo, la araña tiene coordenadas $(1, 8)$ en la pared araña. La polilla tiene coordenadas que dependen de cómo se desdobla. Calculemos la posición relativa.

En el desarrollo "trasera → techo → polilla":

- Pared araña (coordenadas $x$: largo, $z$: alto)
- Pared trasera (unida al borde $x=0$ de la pared araña): su coordenada horizontal es $z$ (alto) y vertical es $x$ (largo, invertido)
- Techo (unido al borde superior $z=9$ de la pared trasera)
- Pared polilla (unida al borde lateral del techo)

Este cálculo es engorroso. Usemos la fórmula estándar para problemas de "ant on a box": para cada desarrollo, la distancia es

$$ \sqrt{(\text{suma de desplazamientos en un eje})^2 + (\text{suma en el otro eje})^2} $$

donde los desplazamientos se reflejan según el desarrollo.

Para los casos 4 y 5, la distancia correcta es:

**Caso 4** (techo → trasera):
$$ \sqrt{(1 + 12 + 8)^2 + (1 + 13)^2} = \sqrt{21^2 + 14^2} = \sqrt{441 + 196} = \sqrt{637} $$

**Caso 5** (trasera → techo):
$$ \sqrt{(1 + 8 + 12 + 8)^2 + (1 + 13)^2} $$

Hmm, no.

Reorganicemos con un método claro y confiable.

## 5. Método del desarrollo con coordenadas

Representemos cada cara en el desarrollo. La habitación tiene estas caras accesibles:

- **S1**: pared lateral araña ($y=0$), plano $x$–$z$
- **S2**: pared lateral polilla ($y=12$), plano $x$–$z$
- **F**: pared frontal ($x=15$), plano $y$–$z$
- **B**: pared trasera ($x=0$), plano $y$–$z$
- **T**: techo ($z=9$), plano $x$–$y$

Para cada desarrollo, escribimos las coordenadas $(u, v)$ de la araña y la polilla en un plano común.

### Desarrollo 1: S1 → T → S2

Desdoblamos S1, T, S2 en un plano:

- S1: coordenadas $(u, v) = (x, 8 - z)$ si unimos el borde superior. Mejor: tomemos S1 con $v$-eje hacia abajo desde el techo.

Convención: para S1, el borde del techo está en $v=0$, y la coordenada $v$ aumenta hacia el suelo.

- Araña en S1: $(x=1, v=1)$ (a 1 pie del techo)
- T unido al borde $v=0$ de S1: T tiene coordenadas $(u=x, w = \text{distancia a través del ancho})$. 
- S2 unido al borde $w=12$ de T: S2 tiene $v$ hacia abajo desde el techo.
- Polilla en S2: $x=14$, a $8$ pies del techo ($z=1$). En el desarrollo, su coordenada $v=8$, y su $u$ es $x + 12$ (desplazada por el ancho del techo).

Coordenadas:
- Araña: $(1, 1)$
- Polilla: $(14 + 12, 8) = (26, 8)$

Distancia:

$$ \sqrt{(26 - 1)^2 + (8 - 1)^2} = \sqrt{25^2 + 7^2} = \sqrt{625 + 49} = \sqrt{674} $$

¡Ajá! Aquí el desplazamiento del largo se suma de forma diferente. Esto da $\sqrt{674}$, distinto de lo que obtuvimos antes ($\sqrt{610}$).

Pero espera, ¿es este desarrollo correcto? Al desdoblar S1 → T → S2 con S2 unida al borde opuesto del techo, la coordenada $x$ de S2 se refleja. La polilla está en $x=14$ desde la pared trasera. Si el techo se une a S2 por su borde $y=12$, y desdoblamos el techo de forma que el eje $x$ sea el mismo para S1, T y S2 (sin reflexión), entonces:

- S1: araña en $(1, 1)$
- T: $u = x$ (sin reflexión), $w = 12$ en el otro eje
- S2: la polilla en $x=14$, pero al desdoblar S2 hacia fuera, el eje $x$ se refleja (porque S2 comparte el borde $y=12$ con T).

Este es el detalle clave de la reflexión. La coordenada de la polilla en S2 desdoblada es $(14, 8)$ en el sistema local de S2, pero al reflejarse respecto de la línea $u=12$ (porque el borde compartido es $y=12$), su coordenada $u$ se convierte en $2\cdot 12 - 14 = 10$.

Entonces:

- Araña: $(1, 1)$
- Polilla: $(10, 8)$

Distancia:

$$ \sqrt{(10 - 1)^2 + (8 - 1)^2} = \sqrt{9^2 + 7^2} = \sqrt{81 + 49} = \sqrt{130} $$

Esto es conspicuamente corto. $\sqrt{130} \approx 11.4$. ¿Es físicamente posible? La distancia en línea recta entre los puntos en 3D es:

$$ \sqrt{(14-1)^2 + (12-0)^2 + (1-8)^2} = \sqrt{169 + 144 + 49} = \sqrt{362} \approx 19.0 $$

La ruta sobre superficies no puede ser más corta que la distancia en línea recta ($\sqrt{362} \approx 19.0$). $\sqrt{130} \approx 11.4$ es imposible; por lo tanto, el desarrollo con esa reflexión no representa una ruta válida.

El error está en la forma de desdoblar. Veamos con cuidado.

Cuando desdoblamos S1 y S2 unidas al techo, ambas comparten el borde del techo. S1 se une al techo por su borde superior ($z=9$). S2 se une al techo por su borde superior ($z=9$). Al desdoblar S1 hacia un lado y S2 hacia el otro lado del techo, la geometría es correcta y no hay reflexión engañosa del eje $x$: ambas paredes laterales comparten la misma orientación del eje $x$ (desde trasera hacia frontal).

Entonces:

- S1: araña en $(x=1, d_1 = 1)$ donde $d_1$ es la distancia desde el techo.
- T: usamos eje $u = x$ (largo) y eje $v = y$ (ancho). S1 se une a lo largo del borde $y=0$.
- S2 se une al borde $y=12$ del techo. Al desdoblar S2, su coordenada vertical es la distancia desde el techo hacia el suelo, y su coordenada horizontal es $x$ (misma orientación).

Desarrollo en un plano:

- S1 ocupa $0 \le x \le 15$, $0 \le d_1 \le 9$ (distancia desde el techo)
- T ocupa $0 \le x \le 15$, pero en un eje perpendicular: pongamos $0 \le y' \le 12$ en el eje horizontal del plano.
- S2, unida al borde $y'=12$, ocupa $12 \le y' \le 21$ (si desdoblamos hacia fuera), con $x$ sin cambiar.

Coordenadas en el plano ($u$ horizontal, $v$ vertical):

- Araña en S1: $u = 1$, $v = 1$ (distancia desde el techo hacia abajo)
- Polilla en S2: $u = 14$, $v = 12 + 8 = 20$

Distancia:

$$ \sqrt{(14 - 1)^2 + (20 - 1)^2} = \sqrt{13^2 + 19^2} = \sqrt{169 + 361} = \sqrt{530} $$

Esto da $\sqrt{530} \approx 23.0$, que es mayor que la línea recta 3D ($\sqrt{362} \approx 19.0$). Es plausible.

Pero antes obtuvimos $\sqrt{610}$ con otra forma de contar. Veamos cuál es correcta.

La confusión surge de cómo se alinean los ejes en el desdoblamiento. Usemos una herramienta sistemática.

## 6. Fórmula general para el desarrollo S1 → T → S2

La cara T (techo) tiene dimensiones $15 \times 12$. La cara S1 se une al borde de $15$ pies (el largo). La cara S2 también se une al borde opuesto de $15$ pies.

En el desarrollo:

- S1 está pegada al techo por su borde superior.
- S2 está pegada al techo por su borde superior, en el lado opuesto.

La distancia entre los puntos es:

$$ d = \sqrt{(a + b)^2 + c^2} $$

donde:
- $a$ = distancia de la araña al borde del techo en S1 ($1$ pie)
- $b$ = distancia de la polilla al borde del techo en S2 ($8$ pies)
- $c$ = distancia entre las proyecciones de los puntos sobre el techo (a lo largo de la superficie del techo)

La proyección de la araña sobre el techo es $(x_a=1, y=0)$. La proyección de la polilla sobre el techo es $(x_m=14, y=12)$.

La distancia sobre el techo entre proyecciones es:

$$ c = \sqrt{(14-1)^2 + 12^2} = \sqrt{13^2 + 12^2} = \sqrt{169 + 144} = \sqrt{313} $$

Entonces la longitud de la ruta es:

$$ d = \sqrt{(a + b)^2 + c^2} = \sqrt{(1+8)^2 + 313} = \sqrt{81 + 313} = \sqrt{394} $$

Esto da $\sqrt{394} \approx 19.85$, que es cercano a la distancia en línea recta 3D ($\sqrt{362} \approx 19.0$). Plausible.

Pero antes obtuvimos $\sqrt{530}$ y $\sqrt{610}$. ¿Cuál es la correcta?

El problema de la ruta por el techo es equivalente a: la araña debe subir al techo en algún punto, viajar por el techo en línea recta, y bajar hasta la polilla. La distancia mínima es:

$$ \min_{P, Q \in \text{techo}} \left( d_A(P) + |PQ| + d_M(Q) \right) $$

donde $d_A$ es la distancia de la araña al techo (1 pie, vertical) y $d_M$ la de la polilla al techo (8 pies, vertical). Estas distancias son fijas: la araña debe llegar al borde superior de su pared (1 pie vertical), y la polilla debe llegar al borde superior de la suya (8 pies vertical).

La distancia horizontal en el techo entre proyecciones es $\sqrt{13^2 + 12^2} = \sqrt{313}$.

La distancia total es:

$$ \sqrt{(1+8)^2 + (\sqrt{313})^2} = \sqrt{81 + 313} = \sqrt{394} $$

Esto es correcto.

## 7. Otros desarrollos con la misma fórmula

### Desarrollo S1 → T → S2 (techo directo)
$$ d_1 = \sqrt{394} $$

### Desarrollo S1 → T → F → S2 (techo + pared frontal)

La araña sube al techo (1 pie), viaja por el techo hasta el borde frontal, baja por la pared frontal, cruza a S2, y llega a la polilla.

Distancia:

- Subida: $1$
- Techo hasta pared frontal: la proyección de la araña en el techo está en $(1, 0)$; el borde frontal está en $x=15$, $0 \le y \le 12$. La distancia más corta sobre el techo desde $(1,0)$ a la pared frontal es en línea recta: $15 - 1 = 14$ pies (si va directo al borde frontal en $y=0$), o más si cruza diagonalmente.
- Pero el punto exacto de la pared frontal por donde pasa afecta la ruta total. Usemos desarrollo.

Desarrollo S1 → T → F → S2:

- S1: araña en $(x=1, v=1)$
- T: unida al borde superior de S1. En el desarrollo, T se extiende en el eje horizontal por $\Delta x = 14$ (hasta la pared frontal en $x=15$) y en el eje vertical por... la pared frontal.
- F se une al borde $x=15$ del techo. F tiene dimensiones $12$ (ancho) × $9$ (alto).
- S2 se une al borde de F.

Coordenadas de la polilla en este desarrollo:

La polilla está en S2, en $x=14$ desde la trasera (es decir, a $1$ pie de la frontal), a $8$ pies del techo.

En el desarrollo, la polilla queda:

- Desde el borde de S2 compartido con F: la polilla está a $14$ pies hacia atrás (a lo largo del eje del largo) y $8$ pies hacia abajo desde el techo.

S2 se une a F (pared frontal) por su borde frontal ($x=15$). Al desdoblar S2 desde F, el eje del largo ($x$) se mapea al eje horizontal del plano, pero reflejado.

Calculemos la distancia usando la fórmula de "expandir el desarrollo":

Distancia horizontal total en el desarrollo (eje $u$):
$1 + 14 + 12 + 14 + 8$ — no, examinemos el orden de los segmentos.

La ruta en el desarrollo es una línea recta desde la araña hasta la polilla. Los desplazamientos en las dos direcciones del plano:

**Dirección 1 (a lo largo del desarrollo, eje $u$):** suma de segmentos que van en la misma dirección de desdoblamiento.

**Dirección 2 (eje $v$, perpendicular en el plano):** desplazamiento perpendicular restante.

Para S1 → T → F → S2:

Tomemos el plano de desarrollo:

- S1: eje $u$ = $x$, eje $v$ = distancia desde el techo hacia abajo.
- T: eje $u$ = $x$, pero desplazado por la altura de S1; eje $v$ = $y$ (ancho).
- F: eje $u$ = distancia desde el techo hacia abajo; eje $v$ = $y$, pero desplazado por $\Delta x$ del techo.
- S2: eje $u$ = $x$ (reflejado); eje $v$ = $y$, desplazado por la altura de F.

Esto es muy complejo. Usemos la fórmula estándar con sumas de distancias parciales.

En la ruta S1 → T → F → S2, los desplazamientos son:

1. De la araña al techo (vertical): $1$
2. Por el techo hacia la pared frontal: en dirección $x$, desde $x=1$ hasta $x=15$: $14$ pies (en línea recta, sin desviación en $y$)
3. Por la pared frontal hacia abajo: desde $z=9$ hasta la altura de la conexión con S2. La polilla está a $z=1$, es decir, $8$ pies por debajo del techo. Así que baja $8$ pies.
4. De la esquina frontal de S2 hasta la polilla: la polilla está a $1$ pie de la pared frontal, así que este segmento es $1$ pie (en dirección $x$, hacia atrás).

Pero además hay un desplazamiento en la dirección del ancho $y$: de $y=0$ (araña) a $y=12$ (polilla), se recorre por la pared frontal. En la pared frontal, la polilla está en $y=12$.

En el desarrollo, la suma de desplazamientos en un eje y en el otro:

**Eje A (dirección principal del desarrollo):** $1 + 14 + 8 + 1 = 24$
**Eje B (perpendicular):** $12$

Distancia: $\sqrt{24^2 + 12^2} = \sqrt{576 + 144} = \sqrt{720}$

Pero esto asume que el desplazamiento por la pared frontal ($12$ pies en $y$) va en el eje perpendicular en el desarrollo, lo cual es plausible.

Sin embargo, este resultado ($\sqrt{720} \approx 26.8$) es mayor que la línea recta 3D ($\approx 19.0$). También es mayor que el techo directo ($\sqrt{394} \approx 19.85$). Entonces no será el mínimo.

### Desarrollo S1 → T → B → S2 (techo + pared trasera)

Similar:

Eje A: $1 + 1 + 8 + 13 = 23$  (subida 1, techo hacia trasera 1, bajada 8, avance en S2 hacia polilla 13)
Eje B: $12$ (ancho, recorrido por la pared trasera)

Distancia: $\sqrt{23^2 + 12^2} = \sqrt{529 + 144} = \sqrt{673}$

También mayor que $\sqrt{394}$.

### Desarrollo S1 → B → S2 (pared trasera directa)

Eje A: $1 + 12 + 13 = 26$  (avance hacia trasera 1, ancho 12, avance en S2 13)
Eje B: $7$ (diferencia de altura)

Distancia: $\sqrt{26^2 + 7^2} = \sqrt{676 + 49} = \sqrt{725}$

### Desarrollo S1 → F → S2 (pared frontal directa)

Eje A: $14 + 12 + 1 = 27$
Eje B: $7$

Distancia: $\sqrt{27^2 + 7^2} = \sqrt{729 + 49} = \sqrt{778}$

### Desarrollo S1 → B → T → S2 (pared trasera + techo)

Eje A: $1 + 8 + 12 + 8 = 29$  (avance hacia trasera 1, subida por B 8, techo ancho 12, bajada en S2 8)
Eje B: $13$ (desplazamiento del largo entre araña y polilla, que en este desarrollo va en el eje perpendicular)

Distancia: $\sqrt{29^2 + 13^2} = \sqrt{841 + 169} = \sqrt{1010}$

Mayor aún.

### Desarrollo S1 → F → T → S2 (pared frontal + techo)

Eje A: $14 + 8 + 12 + 8 = 42$
Eje B: $1$

Distancia: $\sqrt{42^2 + 1^2} = \sqrt{1765}$

Mayor.

## 8. Comparación de resultados

| Desarrollo | Distancia |
|---|---|
| Techo directo | $\sqrt{394} \approx 19.85$ |
| Techo + trasera | $\sqrt{673} \approx 25.94$ |
| Techo + frontal | $\sqrt{720} \approx 26.83$ |
| Trasera | $\sqrt{725} \approx 26.93$ |
| Frontal | $\sqrt{778} \approx 27.89$ |
| Trasera + techo | $\sqrt{1010} \approx 31.78$ |
| Frontal + techo | $\sqrt{1765} \approx 42.01$ |

El mínimo parece ser $\sqrt{394}$ (techo directo).

## 9. Verificación geométrica del techo directo

Verifiquemos $\sqrt{394}$ con un argumento geométrico independiente.

La araña está en S1, a $1$ pie del techo. La polilla está en S2, a $8$ pies del techo.

La ruta más corta por el techo:

- Araña sube verticalmente hasta el techo: $1$ pie.
- Se mueve por el techo en línea recta desde $(1, 0)$ hasta $(14, 12)$: distancia $\sqrt{13^2 + 12^2} = \sqrt{313}$.
- Baja verticalmente hasta la polilla: $8$ pies.

Distancia total: $1 + \sqrt{313} + 8 = 9 + \sqrt{313} \approx 9 + 17.69 = 26.69$.

¡Espera! La ruta real sobre el desarrollo es una línea recta, no la suma de tres segmentos ortogonales. La línea recta en el desarrollo no corresponde a subir verticalmente, viajar horizontalmente en el techo, y bajar verticalmente; la línea recta combina estos movimientos en una sola diagonal.

La distancia en el desarrollo es:

$$ \sqrt{(1 + 8)^2 + (\sqrt{313})^2} = \sqrt{81 + 313} = \sqrt{394} \approx 19.85 $$

Esto es:
- $1+8 = 9$ pies en la dirección vertical (perpendicular al techo)
- $\sqrt{313}$ pies en la dirección paralela al techo

Estos son dos ejes perpendiculares, y la ruta en el desarrollo es la hipotenusa.

La suma $1 + \sqrt{313} + 8$ es lo que se obtendría si la araña subiera verticalmente, caminara horizontalmente en el techo, y bajara verticalmente. Pero la línea recta en el desarrollo es más corta porque sube y avanza simultáneamente (diagonal).

La ruta real (en 3D) sería: la araña se mueve diagonalmente en su pared lateral (subiendo los $1$ pie y avanzando horizontalmente al mismo tiempo), luego diagonalmente en el techo, y luego diagonalmente en la pared de la polilla. La longitud total es $\sqrt{394}$.

¿Es esta la ruta más corta posible?

La cota inferior es la distancia en línea recta 3D:

$$ \sqrt{13^2 + 12^2 + 7^2} = \sqrt{169 + 144 + 49} = \sqrt{362} \approx 19.03 $$

$\sqrt{394} \approx 19.85$ es mayor que $\sqrt{362} \approx 19.03$ (como debe ser).

Pero ¿hay una ruta por las paredes que se acerque más a $\sqrt{362}$?

## 10. Análisis más cuidadoso

El problema dice que la araña **solo puede caminar por techo y paredes** (no por el suelo). Las superficies accesibles son 5 caras: 4 paredes y el techo.

Al ser superficies desarrollables, la distancia más corta es una línea recta en algún desarrollo de las 5 caras.

Los desarrollos relevantes son aquellos donde la línea recta entre los puntos no cruza regiones inválidas. He enumerado 7 desarrollos, pero ¿he enumerado todos?

Con 5 caras, el número de desarrollos posibles es mayor, pero muchos son simétricos o irrelevantes. Los enumerados cubren los casos de pasar por 1 o 2 caras intermedias. Hay también desarrollos que pasan por 3 caras intermedias (por ejemplo, S1 → B → T → F → S2), que evidentemente serán más largos.

Sin embargo, el mínimo encontrado es $\sqrt{394}$, y quiero verificar si es realmente el mínimo.

### Ruta alternativa por la pared trasera con diagonal

Reconsideremos el desarrollo S1 → B → S2 con más cuidado. Quizá hay una forma de desdoblar que dé una distancia menor.

En S1, la araña está en $(x=1, z=8)$. En S2, la polilla está en $(x=14, z=1)$.

Desarrollo S1 → B → S2:

- S1 en plano con ejes $(x, z)$. Araña: $(1, 8)$.
- B se une al borde $x=0$ de S1. B tiene ejes $(y, z)$, pero al desdoblar, el eje $z$ es común (la altura), y el eje $x$ de S1 se mapea al eje $y$ de B.
- S2 se une al borde $y=12$ de B. S2 tiene ejes $(x, z)$.

En el desarrollo, la coordenada de la polilla:

La polilla está en S2 en $(x=14, z=1)$. Para pasar al desarrollo a través de B, la polilla se mapea a:

- Desde el borde $y=12$ de B, la polilla está a $x=14$ pies de la pared trasera, es decir, en el desarrollo, a $14$ pies a lo largo del eje horizontal después de B.
- Su altura es $z=1$.

Coordenadas en el desarrollo plano:

- Araña: $(u_A, v_A) = (1, 8)$
- Polilla: $(u_M, v_M) = (1 + 12 + 14, 1) = (27, 1)$

Aquí he unido S1 (ancho 15 en $u$), B (ancho 12 en $u$), S2 (ancho 15 en $u$). En el eje $v$, la altura.

Distancia:

$$ \sqrt{(27 - 1)^2 + (1 - 8)^2} = \sqrt{26^2 + (-7)^2} = \sqrt{676 + 49} = \sqrt{725} $$

Coincide con lo anterior.

### Desarrollo S1 → F → S2

- Araña: $(1, 8)$
- Polilla: la polilla está a $1$ pie de la pared frontal. En el desarrollo S1 → F → S2:
  - S1: $u$ de 0 a 15 (desde trasera a frontal), $v$ en altura.
  - F se une al borde $u=15$ (frontal). F agrega $12$ pies en $u$.
  - S2 se une al borde de F. La polilla está a $1$ pie de la frontal, es decir, en S2 cerca del borde frontal (a $1$ pie hacia atrás).

Coordenadas polilla: $u_M = 15 + 12 + 1 = 28$, $v_M = 1$.

Distancia:

$$ \sqrt{(28-1)^2 + (1-8)^2} = \sqrt{27^2 + 49} = \sqrt{778} $$

Coincide.

### Desarrollo S1 → T → S2 con reflexión correcta

Retomemos con cuidado.

Desarrollo S1 → T → S2:

- S1: ejes $(x, d)$ donde $d$ es la distancia desde el techo hacia abajo. Araña: $(1, 1)$.
- T se une al borde $d=0$ (borde superior de S1). T tiene ejes $(x, y)$. S1 y T comparten el eje $x$ (el largo). El eje $y$ (ancho) se mapea al eje perpendicular del plano.
- S2 se une al borde $y=12$ de T. S2 tiene ejes $(x, d_2)$ donde $d_2$ es la distancia desde el techo hacia abajo. Polilla: en S2, $x=14$, $d_2=8$.

Plano de desarrollo:

- Eje $u$ (horizontal): $x$ (largo)
- Eje $v$ (vertical): combinación de $d$ y $y$

Distribución:

- S1 ocupa $v$ de $-9$ a $0$ (por debajo del techo), con $d = -v \in [0,9]$. Araña en $(1, -1)$.
- T ocupa $v$ de $0$ a $12$ (a través del ancho), con $y = v$. 
- S2 ocupa $v$ de $12$ a $21$, con $d_2 = v - 12 \in [0,9]$. Polilla en $(14, 12+8) = (14, 20)$.

Distancia:

$$ \sqrt{(14-1)^2 + (20-(-1))^2} = \sqrt{13^2 + 21^2} = \sqrt{169 + 441} = \sqrt{610} $$

Esto da $\sqrt{610}$, que fue nuestro primer resultado. ¿Es esto correcto?

El problema con este desarrollo: al desdoblar S1, T y S2 de esta manera, ¿la línea recta entre $(1,-1)$ y $(14,20)$ pasa realmente por T y no se sale del desarrollo?

El segmento va de $(1,-1)$ a $(14,20)$. Para $v \in [0,12]$, el segmento está en T, y la coordenada $u$ varía de $1$ a $14$. La coordenada $u$ en T es $x$ (largo), que varía de $0$ a $15$. Como $u$ se mantiene entre $1$ y $14$, está dentro de T. Bien.

Para $v \in [-1, 0]$, el segmento está en S1. La coordenada $u$ en S1 es $x$, que varía de $1$ a un poco más, dentro de $[0,15]$. Bien.

Para $v \in [12, 20]$, el segmento está en S2. La coordenada $u$ en S2 es $x$, que varía de $14$ a un poco menos, dentro de $[0,15]$. Bien.

Entonces el desarrollo es válido y la distancia es $\sqrt{610}$.

Pero antes obtuvimos $\sqrt{394}$ con la fórmula $d = \sqrt{(a+b)^2 + c^2}$, lo cual es erróneo porque no consideró la reflexión del eje $x$ de S2 al desdoblar.

En realidad, mi fórmula $\sqrt{(a+b)^2 + c^2}$ asumía que los tres segmentos (subida, cruce en techo, bajada) van en dos ejes perpendiculares: el vertical ($a+b$) y el horizontal del techo ($c$). Pero en el desarrollo, la polilla tiene desplazamiento tanto en $x$ como en $y$ en el techo, y además el desdoblamiento añade desplazamiento adicional.

La fórmula correcta para el desarrollo S1 → T → S2 es:

$$ d = \sqrt{(\text{desplazamiento en } u)^2 + (\text{desplazamiento en } v)^2} $$

con:

- $\Delta u = 14 - 1 = 13$ (largo)
- $\Delta v = 20 - (-1) = 21$ (subida 1 + ancho 12 + bajada 8)

$$ d = \sqrt{13^2 + 21^2} = \sqrt{169 + 441} = \sqrt{610} $$

Coincide con nuestro primer cálculo.

¿Y la fórmula $\sqrt{(a+b)^2 + c^2} = \sqrt{394}$? Esa fórmula corresponde a un problema diferente: cuando la polilla está directamente encima del mismo punto del techo que la araña (sin desplazamiento en $x$).

En nuestro caso, la polilla tiene desplazamiento en $x$ (de 1 a 14) y en $y$ (de 0 a 12). La fórmula $\sqrt{(a+b)^2 + c^2}$ solo aplica si la proyección de la araña y la polilla sobre el techo están separadas en una sola dirección (no en dos). Al tener desplazamiento en ambas direcciones ($x$ e $y$), el desarrollo es más complejo, y la fórmula correcta es la del desarrollo completo.

Entonces, para el techo directo, la distancia es:

$$ \sqrt{610} $$

## 11. Recálculo de todos los desarrollos con la fórmula correcta

Hagamos un recuento sistemático.

### Desarrollo 1: S1 → T → S2

- Araña en $(1, -1)$
- Polilla en $(14, 20)$
- Distancia: $\sqrt{(14-1)^2 + (20+1)^2} = \sqrt{13^2 + 21^2} = \sqrt{610}$

### Desarrollo 2: S1 → B → S2

- Araña en $(1, 8)$
- Polilla en $(27, 1)$
- Distancia: $\sqrt{26^2 + 7^2} = \sqrt{725}$

### Desarrollo 3: S1 → F → S2

- Araña en $(1, 8)$
- Polilla en $(28, 1)$
- Distancia: $\sqrt{27^2 + 7^2} = \sqrt{778}$

### Desarrollo 4: S1 → T → B → S2

- S1: araña en $(1, -1)$
- T: eje $u$ = $x$, eje $v$ = $y$, con $v$ de $-1$ no... Organicemos.

En el desarrollo S1 → T → B → S2:

- S1: araña en $(u=1, v=-1)$ (como antes)
- T: unida al borde superior de S1, se extiende hacia $v$ positivo, con $u$ = $x$.
- B se une al borde trasero de T ($x=0$), se extiende en el eje $u$ hacia la izquierda.
- S2 se une a B.

Distribución en el plano:

- S1: $v \in [-9, 0]$, $u \in [0, 15]$. Araña en $(1, -1)$.
- T: $v \in [0, 12]$, $u \in [0, 15]$. (el borde trasero de T está en $u=0$)
- B: unida al borde $u=0$ de T (x=0, pared trasera). B se extiende en $u \in [-9, 0]$ (altura hacia abajo, porque B tiene ejes $y$ y $z$, y al unirla al borde $x=0$ del techo, el eje $z$ de B se mapea al eje $u$ negativo).
- S2: unida al borde de B en $y=12$. S2 se extiende en $u \in [-9, 0]$ (altura de S2)... 

Esto es complicado. Calculemos las coordenadas de la polilla paso a paso.

La pared trasera B tiene ejes $(y, z)$. El techo se une a B por su borde superior ($z=9$). Al desdoblar:

- T unido a B por el borde trasero ($x=0$), que en B corresponde a la línea superior ($z=9$).
- B se coloca en el plano con eje horizontal = $y$, eje vertical = distancia desde el techo hacia abajo.

La polilla está en S2. S2 se une a B por el borde $y=12$. La polilla en S2 está en $x=14$, $z=1$, es decir, a $8$ pies del techo.

En el desarrollo:

- Araña: $(1, -1)$ (en S1)
- La polilla: necesitamos su posición en el desarrollo S1 → T → B → S2.

Mejor usemos la técnica de "reflexión" o "suma de desplazamientos":

En el desarrollo, la distancia euclidiana entre los puntos es:

$$ d = \sqrt{(\Delta u)^2 + (\Delta v)^2} $$

Para cada desarrollo, calculamos $\Delta u$ y $\Delta v$ sumando los desplazamientos en las dos direcciones del plano.

**Desarrollo S1 → T → B → S2:**

Segmentos de la ruta (en el orden del desdoblamiento):

1. De la araña al techo: $1$ pie (en la dirección $v$ negativa)
2. Por el techo desde el punto de la araña ($x=1, y=0$) hacia el borde trasero ($x=0$): $1$ pie en dirección $u$ negativa
3. Por B (pared trasera) desde el techo ($z=9$) hacia abajo hasta la altura de la conexión con S2: la polilla está a $z=1$, así que baja $8$ pies. En el desdoblamiento, esta bajada va en la dirección $u$ negativa (continuando desde el borde de T).
4. Por S2 desde B ($y=12$) hasta la polilla: la polilla está a $x=14$ de la trasera, pero espera, S2 se une a B por su borde $y=12$, y la polilla está en S2 en la coordenada $x=14$ (desde la trasera).

En el desarrollo, el eje $u$ acumula:

- De araña a techo: $0$ en $u$ (es en $v$)
- Techo hacia trasera: $1$ en $u$
- Bajada por B: $8$ en $u$ (dirección negativa)
- S2 de B a polilla: la polilla está a $14$ pies de la trasera en S2, así que $14$ pies en $u$ (en la dirección positiva, de vuelta hacia el frente)

Suma en $u$: $1 + 8 + 14 = 23$ (tomando valores absolutos, porque en el desarrollo van en la misma dirección después de desdoblar)

En el eje $v$:
- De araña al techo: $1$
- Por T: la polilla tiene $y=12$, la araña $y=0$, así que el desplazamiento en $v$ por T y B es $12$.

Suma en $v$: $1 + 12 = 13$? No, el desplazamiento en $v$ es la componente perpendicular.

Reorganicemos.

En el desarrollo S1 → T → B → S2, pongamos:

- S1 en el plano: $u = x$, $v = -d$ (d: distancia desde el techo). Araña: $(1, -1)$.
- T: $u = x$, $v = y$. Borde trasero de T en $u=0$.
- B: unida al borde $u=0$ de T, se extiende hacia $u$ negativo. En B, el eje horizontal es $y$ (ancho) y el vertical es $z$ (altura). Al unir al techo por $z=9$, la altura de B se mapea a $u$ negativo: $u = -(9 - z)$. El eje $y$ de B se mapea a $v$.
- S2: unida a B por $y=12$, se extiende hacia $u$ positivo (porque S2 comparte el borde $y=12$ con B, y al desdoblar, S2 queda a la derecha de B). En S2, el eje horizontal es $x$ (largo) y el vertical es $z$.

La polilla en S2: $x=14$, $z=1$. En el desarrollo:

- Comenzando desde B, la polilla está en $y=12$ de B, es decir, en $v = 12$.
- En S2, la polilla está a $x=14$ de la trasera. En el desdoblamiento, S2 se extiende en la dirección $u$ positiva desde el borde $y=12$ de B. El eje $u$ de S2 es $x$. Entonces la polilla está en $u = 14$.
- Su altura es $z=1$, que en S2 se refleja en el eje $v$: la polilla está a $8$ pies del techo. En el desarrollo, la distancia desde el techo se mapea a... esto depende de cómo S2 se une a B.

S2 se une a B por su borde $y=12$. En B, ese borde es vertical (a lo largo de $z$). Al unir S2 a B por $y=12$, el eje $z$ de S2 se alinea con el eje $z$ de B. En B, $z=9$ corresponde al borde del techo (que está en $u=0$ en el desarrollo), y $z=0$ corresponde al borde del suelo (en $u=-9$).

Entonces, en S2, la polilla en $z=1$ está a $u = -(9 - 1) = -8$ desde el borde de B. Pero S2 se extiende en la dirección $u$ positiva desde B. Así que la coordenada $u$ de la polilla es $14 - 8 = 6$ (si S2 se coloca a la derecha de B y el eje $x$ se mapea positivamente).

Hmm, hay dos ejes en juego. Estoy confundiendo la orientación.

Dejemos de lado este desarrollo por un momento; ya vimos que su distancia ($\sqrt{673}$ o similar) es mayor que $\sqrt{610}$, así que no será el mínimo.

## 12. Enfoque alternativo: "unfold" mediante el método de la distancia geodésica

Para problemas de "spider and fly on a box", la distancia más corta sobre las caras se obtiene considerando todos los desdoblamientos donde las 3 caras que contienen a ambos puntos se aplanan. Hay una cantidad finita de desdoblamientos, y el mínimo se obtiene comparando.

Para este problema (habitación con araña en pared lateral y polilla en pared lateral opuesta), los desdoblamientos principales ya los hemos evaluado. El mínimo entre ellos es:

- $\sqrt{610} \approx 24.70$ (techo directo)
- $\sqrt{673} \approx 25.94$
- $\sqrt{720} \approx 26.83$
- $\sqrt{725} \approx 26.93$
- $\sqrt{778} \approx 27.89$

El mínimo es $\sqrt{610}$.

## 13. Verificación adicional: ¿existe una ruta más corta por B o F con diagonal más favorable?

Consideremos la ruta S1 → B → S2 de nuevo. La distancia era $\sqrt{725} \approx 26.93$. Esto es mayor que $\sqrt{610} \approx 24.70$. Bien.

¿Y una ruta que pase por B y T? Ya calculamos $\sqrt{673} \approx 25.94$. Mayor que $\sqrt{610}$.

¿Y una ruta que pase por F y T? $\sqrt{720} \approx 26.83$. Mayor.

¿Y rutas que pasen por B y F (las dos paredes extremas)? Serían aún más largas.

Entonces el mínimo parece ser $\sqrt{610}$.

## 14. Revisión final de la ruta por el techo

Verifiquemos que $\sqrt{610}$ es correcto mediante un cálculo independiente.

Araña: en S1, a 1 pie del techo y a 1 pie de la pared trasera.
Polilla: en S2, a 1 pie del suelo y a 1 pie de la pared frontal.

Desarrollo S1 → T → S2:

- S1 y T comparten el eje del largo ($x$).
- S2 y T comparten el eje del largo ($x$).
- El techo tiene ancho 12 pies.

En el plano de desarrollo:

- Eje horizontal $u$: corresponde al largo $x$.
- Eje vertical $v$: corresponde a la suma de distancias perpendiculares al largo: altura de S1 + ancho del techo + altura de S2.

La araña está en $u=1$, y su distancia al techo es $1$ pie, así que en el desarrollo está a $v = -1$ (por debajo del borde del techo, que es $v=0$).

La polilla está en $u=14$, y su distancia al techo es $8$ pies. En el desarrollo, S2 está por encima del techo en el eje $v$, así que la polilla está en $v = 12 + 8 = 20$.

Distancia:

$$ d = \sqrt{(14-1)^2 + (20 - (-1))^2} = \sqrt{13^2 + 21^2} = \sqrt{169 + 441} = \sqrt{610} $$

$\sqrt{610} \approx 24.70$. La distancia en línea recta 3D es $\sqrt{362} \approx 19.03$, lo cual es una cota inferior razonable. La ruta es válida.

## 15. ¿Hay un desdoblamiento con la araña y la polilla más cerca en el desarrollo?

Consideremos el desdoblamiento donde S1 se une a T por su borde lateral (no superior). Pero S1 solo comparte bordes con T por su borde superior; los bordes laterales de S1 los comparte con B y F.

Entonces los únicos desdoblamientos que incluyen T son S1 → T → S2 (y sus variantes pasando por B o F).

El desdoblamiento S1 → T → S2 da $\Delta u = 13$ y $\Delta v = 21$, resultando en $\sqrt{610}$.

Si desdoblamos de manera diferente, por ejemplo, S1 → T con S2 unida al techo por un borde diferente — no, S2 solo comparte con T por su borde superior.

Todos los desdoblamientos posibles:

1. S1 → T → S2: $\sqrt{610}$
2. S1 → B → S2: $\sqrt{725}$
3. S1 → F → S2: $\sqrt{778}$
4. S1 → T → B → S2: $\sqrt{673}$ (calculado antes)
5. S1 → B → T → S2: más largo
6. S1 → T → F → S2: $\sqrt{720}$
7. S1 → F → T → S2: más largo
8. S1 → B → T → F → S2: mucho más largo
9. S1 → F → T → B → S2: mucho más largo

El mínimo es $\sqrt{610}$.

## 16. Respuesta

La longitud del camino más corto es $\sqrt{610}$ pies.

Simplifiquemos $\sqrt{610}$:

$610 = 2 \cdot 305 = 2 \cdot 5 \cdot 61$

Ninguno de estos factores es un cuadrado perfecto, así que $\sqrt{610}$ ya está en forma radical simple.

**Respuesta final:** $\sqrt{610}$ pies.

\boxed{\sqrt{610}}