¡Claro! Vamos a resolverlo paso a paso.

---

## Paso 1: Entender la situación

Tenemos un cubo de arista **6**. Dentro se colocan **8 bolas de radio** \( r = \tfrac{3}{2} \). Cada bola es externamente tangente exactamente a **tres** de las otras. Queremos el radio \( R \) de la mayor bola que quepa dentro de la caja y que sea externamente tangente a **todas** esas 8 bolas.

La clave es la configuración de las 8 bolas. Que cada una toque a exactamente tres sugiere disponerlas como los **centros de las caras de un cubo interno** o, de forma más natural, **una bola cerca de cada vértice de un cubo imaginario**.

---

## Paso 2: Posición de las 8 bolas

Una configuración que da tangencia a exactamente tres vecinos es la de **cuboctaedro** (los centros forman los vértices de un cuboctaedro). Pero como el cubo exterior tiene arista 6, lo más sencillo es pensar en un **cubo interior imaginario** cuyos vértices son los centros de las bolas.

Para que cada bola toque a exactamente tres, los centros deben estar en los vértices de un cubo pequeño.

Llamemos \( d \) a la distancia entre centros de dos bolas tangentes. Como son externamente tangentes y tienen radio \( r = 3/2 \):

\[
d = 2r = 3.
\]

---

## Paso 3: Tamaño del cubo de centros

Si los centros forman un cubo de arista \( a \), la distancia entre dos vértices conectados por una arista es \( a \). Para la tangencia externa entre bolas adyacentes:

\[
a = d = 3.
\]

Entonces los centros están en un cubo de arista \( a = 3 \).

---

## Paso 4: Colocación dentro del cubo grande

El cubo de centros (arista 3) debe caber dentro del cubo grande (arista 6) dejando espacio para las bolas de radio \( 3/2 \) que no salgan de las paredes.

Pongamos el cubo de centros **centrado**. Si su arista es 3, el hueco a cada lado (respecto al cubo de arista 6) es:

\[
\frac{6 - 3}{2} = 1.5 = \frac{3}{2}.
\]

¡Justo el radio de las bolas! Así cada bola toca también las caras del cubo grande. Como las 8 bolas están en los 8 vértices del cubo pequeño, cada una toca a 3 caras del cubo grande y a 3 bolas vecinas, coincidiendo con el dato del problema.

---

## Paso 5: Posición del centro y radio máximo

La mayor bola que toca a las 8 bolas estará centrada en el centro del cubo grande (también centro del cubo de centros). Llamemos \( O \) a dicho centro.

La distancia desde \( O \) hasta cada centro de las bolas es la **media diagonal espacial** del cubo de centros.

Para un cubo de arista \( a = 3 \):

\[
\text{diagonal} = a\sqrt{3} = 3\sqrt{3}.
\]

La distancia desde el centro a un vértice es la mitad:

\[
D = \frac{3\sqrt{3}}{2}.
\]

---

## Paso 6: Radio de la bola grande

La bola grande de radio \( R \) es tangente externamente a cada bola pequeña de radio \( r = 3/2 \). Entonces la distancia entre centros debe ser:

\[
D = R + r.
\]

Por lo tanto:

\[
R = D - r = \frac{3\sqrt{3}}{2} - \frac{3}{2} = \frac{3}{2}(\sqrt{3} - 1).
\]

---

## Paso 7: Verificar que cabe en el cubo

La bola grande queda centrada a distancia \( 3 \) de cada cara. Su radio:

\[
R = \frac{3}{2}(\sqrt{3} - 1) \approx \frac{3}{2}(0.732) = 1.098.
\]

Como \( R < 3 \), cabe perfectamente en el cubo.

---

## Resultado final

\[
\boxed{\frac{3\left(\sqrt{3}-1\right)}{2}}
\]