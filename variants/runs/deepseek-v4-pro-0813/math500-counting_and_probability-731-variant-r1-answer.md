Voy a razonar el problema paso a paso.

## 1. Plantear la región de interés

En un triángulo equilátero $PQR$ con centro (circuncentro/baricentro/incentro) $O$, piden la probabilidad de que un punto **interior** elegido uniformemente esté más cerca de $O$ que de cualquiera de los tres vértices.

Para cada vértice, digamos $P$, la condición "más cerca de $O$ que de $P$" es:

\[
|X - O| < |X - P|.
\]

Esto equivale a que $X$ esté en el semiplano del lado de $O$ respecto de la **mediatriz** del segmento $OP$.

Como el triángulo es equilátero, las tres mediatrices de $OP$, $OQ$ y $OR$ son rectas con simetría triple. La intersección de los tres semiplanos favorables forma una **región hexagonal o triangular** alrededor de $O$. Debemos hallar su área relativa al área del triángulo.

## 2. Normalizar el triángulo

Pongamos el triángulo equilátero con lado $L$ y área

\[
A_{\triangle} = \frac{\sqrt3}{4}L^2.
\]

La distancia del centro $O$ a cada vértice (circunradio) es

\[
R = \frac{L}{\sqrt3}.
\]

## 3. Encontrar los vértices de la región favorable

Consideremos el vértice $P$ y la mediatriz de $OP$. La mediatriz corta a las líneas desde $O$ hacia los otros vértices (o hacia los puntos medios, según convenga) en puntos que serán vértices del polígono favorable.

Gracias a la simetría, basta calcular la mitad del ángulo o usar coordenadas.

Pongamos coordenadas con $O$ en el origen. Tomemos

\[
P = (R, 0),\qquad Q = R\left(-\frac12,\frac{\sqrt3}{2}\right),\qquad R = R\left(-\frac12,-\frac{\sqrt3}{2}\right).
\]

La mediatriz de $OP$: el punto medio de $OP$ es $(R/2,0)$ y la recta perpendicular a $OP$ (que es el eje $x$) es la recta vertical

\[
x = \frac{R}{2}.
\]

Así, la condición de estar más cerca de $O$ que de $P$ es simplemente

\[
x < \frac{R}{2}.
\]

Por simetría, para $Q$ y $R$ obtenemos condiciones análogas que son las rotaciones de $x < R/2$ por $120^\circ$ y $240^\circ$.

La región favorable es la intersección de los tres semiplanos:

1. $x \le R/2$,
2. $-\frac12 x + \frac{\sqrt3}{2}y \le R/2$,
3. $-\frac12 x - \frac{\sqrt3}{2}y \le R/2$.

## 4. Identificar la región favorable

Estas tres desigualdades definen un **triángulo equilátero** centrado en $O$, cuyos lados son rectas a distancia $R/2$ del origen. En efecto, cada mediatriz está a distancia $R/2$ de $O$.

Un triángulo equilátero cuyo inradio (distancia del centro a cada lado) es $r_{\text{in}} = R/2$ tiene lado

\[
s = 2\sqrt3\, r_{\text{in}} = 2\sqrt3 \cdot \frac{R}{2} = \sqrt3\, R.
\]

Pero $R = L/\sqrt3$, luego

\[
s = \sqrt3 \cdot \frac{L}{\sqrt3} = L.
\]

¡La región favorable es un triángulo equilátero de lado $L$, el mismo lado que el triángulo original!

## 5. Calcular la probabilidad

El área del triángulo favorable es

\[
A_{\text{fav}} = \frac{\sqrt3}{4}s^2 = \frac{\sqrt3}{4}L^2.
\]

Pero esa es exactamente el área del triángulo original:

\[
A_{\triangle} = \frac{\sqrt3}{4}L^2.
\]

Esto daría probabilidad $1$, lo cual es claramente absurdo: hay puntos cerca de los vértices. Hay un error.

## 6. Corregir el error

Revisemos: la mediatriz de $OP$ está a distancia $R/2$ del origen, correcto. La intersección de los tres semiplanos a distancia $R/2$ del origen es un triángulo equilátero con inradio $R/2$.

El lado de ese triángulo interior es

\[
s = 2\sqrt3 \cdot \frac{R}{2} = \sqrt3 R = \sqrt3 \cdot \frac{L}{\sqrt3} = L.
\]

Eso parece correcto...

Pero cuidado: el triángulo original no tiene inradio $R/2$. El inradio del triángulo original es

\[
r = \frac{L\sqrt3}{6} = \frac{R}{2}.
\]

Espera, calculemos:

\[
R = \frac{L}{\sqrt3},\qquad \frac{R}{2} = \frac{L}{2\sqrt3} = \frac{L\sqrt3}{6} = r.
\]

Entonces la mediatriz de $OP$ pasa exactamente a distancia igual al **inradio** del triángulo original. Es decir, la mediatriz de $OP$ es paralela al lado $QR$ y está a la misma distancia de $O$ que el lado $QR$.

Por tanto, el triángulo favorable formado por las tres mediatrices tiene el mismo inradio que el triángulo original, luego es **congruente** al triángulo original. Eso significa que las tres mediatrices son precisamente los lados del triángulo original... pero no: la mediatriz de $OP$ es paralela a $QR$, pero no coincide con $QR$; está más cerca de $O$ o más lejos.

Veamos: el lado $QR$ está a distancia $r = R/2$ de $O$. La mediatriz de $OP$ también está a distancia $R/2$ de $O$. Como el segmento $OP$ es perpendicular al lado $QR$ (pues $O$ está en la mediana desde $P$), la mediatriz de $OP$ es paralela a $QR$ y pasa también a distancia $R/2$ de $O$. Pero $QR$ está en el lado opuesto de $O$ respecto de $P$, mientras que la mediatriz de $OP$ está entre $O$ y $P$, a distancia $R/2$ de $O$.

Entonces hay **dos** rectas paralelas a $QR$ a distancia $R/2$ de $O$: una es $QR$ (lejos de $P$) y otra es la mediatriz de $OP$ (cerca de $P$). No son la misma recta.

Por tanto, el triángulo formado por las tres mediatrices es un triángulo equilátero con inradio $R/2$, pero **orientado opuestamente** al triángulo original: sus vértices apuntan hacia los lados del triángulo original, no hacia sus vértices.

## 7. Relación de áreas

Ambos triángulos tienen lado $L$, así que mi cálculo de área sigue dando igual. Eso es sospechoso, pues la intersección de tres semiplanos no puede contener a todo el triángulo si los semiplanos no contienen a los vértices.

Revisemos la orientación de la desigualdad. Queremos $x < R/2$. El vértice $P=(R,0)$ no cumple $x<R/2$, correcto. El vértice $Q = (-R/2, \sqrt3 R/2)$ cumple $x = -R/2 < R/2$, y lo mismo $R$. Entonces la región favorable **sí contiene** a $Q$ y a $R$, pero no a $P$.

Análogamente, la desigualdad para $Q$ excluye a $Q$ pero incluye a $P$ y $R$, y la de $R$ excluye a $R$ pero incluye a $P$ y $Q$.

La intersección de las tres:

- La condición para $P$ elimina una franja cerca de $P$.
- La condición para $Q$ elimina una franja cerca de $Q$.
- La condición para $R$ elimina una franja cerca de $R$.

La región resultante es un **hexágono regular** (o un triángulo con las esquinas recortadas), no el triángulo completo.

Debo recalcular la intersección correctamente.

## 8. Cálculo correcto con coordenadas

Con $R$ como unidad por comodidad ($R=1$), el triángulo original tiene vértices en el círculo unitario:

\[
P=(1,0),\quad Q=\left(-\frac12,\frac{\sqrt3}{2}\right),\quad R=\left(-\frac12,-\frac{\sqrt3}{2}\right).
\]

Desigualdades favorables:

1. $x \le 1/2$,
2. $-\frac12 x + \frac{\sqrt3}{2}y \le 1/2$,
3. $-\frac12 x - \frac{\sqrt3}{2}y \le 1/2$.

La intersección de estos tres semiplanos cerrados contiene al origen. Hallemos sus vértices como intersecciones de pares de rectas límite.

Las rectas límite son:

\[
\ell_1: x = 1/2,
\]
\[
\ell_2: -\frac12 x + \frac{\sqrt3}{2}y = 1/2,
\]
\[
\ell_3: -\frac12 x - \frac{\sqrt3}{2}y = 1/2.
\]

Multiplicando $\ell_2$ y $\ell_3$ por 2:

\[
\ell_2: -x + \sqrt3\,y = 1,
\]
\[
\ell_3: -x - \sqrt3\,y = 1.
\]

Intersección $\ell_1 \cap \ell_2$: $x=1/2$, sustituyendo en $\ell_2$:

\[
-\frac12 + \sqrt3\,y = 1 \implies \sqrt3\,y = \frac32 \implies y = \frac{3}{2\sqrt3} = \frac{\sqrt3}{2}.
\]

Este punto es $(1/2, \sqrt3/2)$.

Intersección $\ell_1 \cap \ell_3$: $x=1/2$, sustituyendo en $\ell_3$:

\[
-\frac12 - \sqrt3\,y = 1 \implies -\sqrt3\,y = \frac32 \implies y = -\frac{\sqrt3}{2}.
\]

Punto: $(1/2, -\sqrt3/2)$.

Intersección $\ell_2 \cap \ell_3$: sumando ambas,

\[
-2x = 2 \implies x = -1.
\]

Sustituyendo $x=-1$ en $\ell_2$: $1 + \sqrt3 y = 1 \implies y=0$. Punto: $(-1, 0)$.

Estos tres puntos forman un triángulo con vértices

\[
(1/2, \sqrt3/2),\quad (1/2, -\sqrt3/2),\quad (-1,0).
\]

Veamos si este triángulo contiene al origen. El origen $(0,0)$ cumple las tres desigualdades estrictas, así que sí está en el interior.

Este triángulo es isósceles con base vertical de longitud $\sqrt3$ (de $y=-\sqrt3/2$ a $y=\sqrt3/2$) y altura horizontal desde $x=-1$ hasta $x=1/2$, es decir, altura $3/2$.

Área:

\[
A_{\text{fav}} = \frac12 \cdot \text{base} \cdot \text{altura} = \frac12 \cdot \sqrt3 \cdot \frac32 = \frac{3\sqrt3}{4}.
\]

Con $R=1$.

## 9. Área del triángulo original

Con $R=1$, el lado del triángulo original es

\[
L = \sqrt3\, R = \sqrt3.
\]

Área:

\[
A_{\triangle} = \frac{\sqrt3}{4}L^2 = \frac{\sqrt3}{4}\cdot 3 = \frac{3\sqrt3}{4}.
\]

¡Son iguales otra vez! Algo sigue mal.

## 10. Revisar qué región es la correcta

El problema es que la intersección de los tres semiplanos no es el triángulo con esos tres vértices, porque ese triángulo no está contenido en el triángulo original. Los puntos $(1/2, \pm\sqrt3/2)$ están fuera del triángulo original.

Recordemos que estamos eligiendo puntos **del interior del triángulo $PQR$**. Entonces la región favorable es la intersección del triángulo original con los tres semiplanos.

El triángulo original con $R=1$:

- Vértice $P=(1,0)$.
- Lado $QR$: $x = -1/2$.
- Lado $PQ$ y $PR$: rectas que pasan por $P$ y los otros vértices.

La intersección de los semiplanos favorables con el triángulo original es un **hexágono**.

Hallemos sus vértices.

Rectas del triángulo original:

- Lado $QR$: $x = -1/2$.
- Lado $PQ$: recta por $P=(1,0)$ y $Q=(-1/2,\sqrt3/2)$. Pendiente:

\[
m = \frac{\sqrt3/2 - 0}{-1/2 - 1} = \frac{\sqrt3/2}{-3/2} = -\frac{\sqrt3}{3}.
\]

Ecuación: $y = -\frac{\sqrt3}{3}(x-1)$.

- Lado $PR$: por simetría, $y = \frac{\sqrt3}{3}(x-1)$.

Ahora, la región favorable es la intersección de:

\[
x \le 1/2,\quad -x+\sqrt3 y \le 1,\quad -x-\sqrt3 y \le 1,
\]

y el triángulo:

\[
x \ge -1/2,\quad y \ge \frac{\sqrt3}{3}(x-1),\quad y \le -\frac{\sqrt3}{3}(x-1).
\]

Notemos que la recta $\ell_2: -x+\sqrt3 y = 1$ corta al lado $PQ$ y al lado $QR$.

Intersección de $\ell_2$ con $PQ$ ($y = -\frac{\sqrt3}{3}(x-1)$):

\[
-x + \sqrt3 \left(-\frac{\sqrt3}{3}(x-1)\right) = 1,
\]
\[
-x - (x-1) = 1,
\]
\[
-x - x + 1 = 1 \implies -2x = 0 \implies x = 0.
\]

Entonces $y = -\frac{\sqrt3}{3}(0-1) = \frac{\sqrt3}{3}$.

Punto: $\left(0, \frac{\sqrt3}{3}\right)$.

Intersección de $\ell_3$ con $PR$ ($y = \frac{\sqrt3}{3}(x-1)$):

\[
-x - \sqrt3 \cdot \frac{\sqrt3}{3}(x-1) = 1,
\]
\[
-x - (x-1) = 1 \implies -2x + 1 = 1 \implies x=0.
\]

Entonces $y = \frac{\sqrt3}{3}(0-1) = -\frac{\sqrt3}{3}$.

Punto: $\left(0, -\frac{\sqrt3}{3}\right)$.

Intersección de $\ell_1$ ($x=1/2$) con $PQ$:

\[
y = -\frac{\sqrt3}{3}\left(\frac12 - 1\right) = -\frac{\sqrt3}{3}\left(-\frac12\right) = \frac{\sqrt3}{6}.
\]

Punto: $\left(\frac12, \frac{\sqrt3}{6}\right)$.

Intersección de $\ell_1$ con $PR$:

\[
y = \frac{\sqrt3}{3}\left(\frac12 - 1\right) = \frac{\sqrt3}{3}\left(-\frac12\right) = -\frac{\sqrt3}{6}.
\]

Punto: $\left(\frac12, -\frac{\sqrt3}{6}\right)$.

Intersección de $\ell_2$ con $\ell_3$ ya la calculamos: $(-1,0)$, pero ese punto está fuera del triángulo (el triángulo tiene $x\ge -1/2$). En su lugar, la región favorable está limitada por el lado $QR$ ($x=-1/2$) entre las intersecciones de $\ell_2$ y $\ell_3$ con ese lado.

Intersección de $\ell_2$ con $QR$ ($x=-1/2$):

\[
-(-1/2) + \sqrt3 y = 1 \implies \frac12 + \sqrt3 y = 1 \implies \sqrt3 y = \frac12 \implies y = \frac{1}{2\sqrt3} = \frac{\sqrt3}{6}.
\]

Punto: $\left(-\frac12, \frac{\sqrt3}{6}\right)$.

Intersección de $\ell_3$ con $QR$ ($x=-1/2$):

\[
-(-1/2) - \sqrt3 y = 1 \implies \frac12 - \sqrt3 y = 1 \implies -\sqrt3 y = \frac12 \implies y = -\frac{1}{2\sqrt3} = -\frac{\sqrt3}{6}.
\]

Punto: $\left(-\frac12, -\frac{\sqrt3}{6}\right)$.

## 11. Vértices del hexágono favorable

Recorriendo en sentido antihorario:

1. $\left(0, \frac{\sqrt3}{3}\right)$ — intersección $\ell_2 \cap PQ$.
2. $\left(\frac12, \frac{\sqrt3}{6}\right)$ — intersección $\ell_1 \cap PQ$.
3. $\left(\frac12, -\frac{\sqrt3}{6}\right)$ — intersección $\ell_1 \cap PR$.
4. $\left(0, -\frac{\sqrt3}{3}\right)$ — intersección $\ell_3 \cap PR$.
5. $\left(-\frac12, -\frac{\sqrt3}{6}\right)$ — intersección $\ell_3 \cap QR$.
6. $\left(-\frac12, \frac{\sqrt3}{6}\right)$ — intersección $\ell_2 \cap QR$.

Este es un hexágono. Notemos que no es regular, pero tiene simetría respecto del eje $x$ y posee simetría triple.

## 12. Calcular el área del hexágono

Podemos calcular el área del hexágono como el área del triángulo original menos las tres esquinas recortadas.

Las esquinas recortadas son tres triángulos congruentes cerca de los vértices.

**Esquina cerca de $P$:** limitada por $PQ$, $PR$ y $\ell_1: x=1/2$. Los puntos de corte son $(1/2, \sqrt3/6)$ y $(1/2, -\sqrt3/6)$, y el vértice $P=(1,0)$. Este triángulo tiene base vertical (sobre $x=1/2$) de longitud

\[
\frac{\sqrt3}{6} - \left(-\frac{\sqrt3}{6}\right) = \frac{\sqrt3}{3},
\]

y altura horizontal desde $x=1/2$ hasta $x=1$, es decir $1/2$.

Área de esta esquina:

\[
A_P = \frac12 \cdot \frac{\sqrt3}{3} \cdot \frac12 = \frac{\sqrt3}{12}.
\]

**Esquina cerca de $Q$:** por simetría, también $\sqrt3/12$.

**Esquina cerca de $R$:** también $\sqrt3/12$.

Suma de esquinas:

\[
A_{\text{esquinas}} = 3 \cdot \frac{\sqrt3}{12} = \frac{\sqrt3}{4}.
\]

## 13. Área del triángulo original

Con $R=1$:

\[
A_{\triangle} = \frac{3\sqrt3}{4}.
\]

## 14. Área favorable

\[
A_{\text{fav}} = A_{\triangle} - A_{\text{esquinas}} = \frac{3\sqrt3}{4} - \frac{\sqrt3}{4} = \frac{2\sqrt3}{4} = \frac{\sqrt3}{2}.
\]

## 15. Probabilidad

\[
P = \frac{A_{\text{fav}}}{A_{\triangle}} = \frac{\sqrt3/2}{3\sqrt3/4} = \frac{\sqrt3}{2} \cdot \frac{4}{3\sqrt3} = \frac{2}{3}.
\]

## 16. Verificación alternativa

La distancia de $O$ a cada lado del hexágono es $R/2$, y la región favorable es un hexágono regular si lo vemos en el contexto correcto. Pero nuestro cálculo geométrico directo da $\frac23$, que es una respuesta razonable.

Para verificar: el apotema del hexágono favorable es $R/2$, y el hexágono está inscrito de cierta manera. Otra forma: la probabilidad de estar más cerca del centro que de un vértice dado es la proporción del área en el semiplano correspondiente, y por simetría la probabilidad final resulta $2/3$.

El área del hexágono también se puede obtener sumando áreas de triángulos. Confío en el resultado $\frac23$.

\[
\boxed{\frac{2}{3}}
\]