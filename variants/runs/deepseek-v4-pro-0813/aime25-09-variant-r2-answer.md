Vamos a resolverlo paso a paso.

## 1. La rotación y la parábola original

La parábola original es $y = x^2 - 5$. Queremos rotar $60^\circ$ en sentido antihorario alrededor del origen. Si un punto $(x, y)$ rota $60^\circ$ antihorario, su imagen $(X, Y)$ viene dada por:

$$
\begin{pmatrix} X \\ Y \end{pmatrix}
=
\begin{pmatrix} \cos 60^\circ & -\sin 60^\circ \\ \sin 60^\circ & \cos 60^\circ \end{pmatrix}
\begin{pmatrix} x \\ y \end{pmatrix}
=
\begin{pmatrix} \frac12 x - \frac{\sqrt3}{2} y \\ \frac{\sqrt3}{2} x + \frac12 y \end{pmatrix}.
$$

Aquí, $(x,y)$ recorre la parábola original. La parábola rotada (imagen) es el conjunto de todos esos $(X,Y)$.

Los puntos de intersección de la parábola original y su imagen son puntos $(x,y)$ que pertenecen a la original y, además, están sobre la imagen. Decir que $(x,y)$ está sobre la imagen equivale a decir que su preimagen bajo la rotación, es decir, el punto obtenido rotando $(x,y)$ un ángulo de $-60^\circ$ (o $60^\circ$ horario), está sobre la parábola original.

## 2. Condición para los puntos de intersección

Un punto $(x,y)$ está sobre la parábola rotada si su rotación inversa está en $y = x^2 - 5$.

Rotamos $(x,y)$ un ángulo $-60^\circ$:

$$
\begin{pmatrix} u \\ v \end{pmatrix}
=
\begin{pmatrix} \cos(-60^\circ) & -\sin(-60^\circ) \\ \sin(-60^\circ) & \cos(-60^\circ) \end{pmatrix}
\begin{pmatrix} x \\ y \end{pmatrix}
=
\begin{pmatrix} \frac12 & \frac{\sqrt3}{2} \\ -\frac{\sqrt3}{2} & \frac12 \end{pmatrix}
\begin{pmatrix} x \\ y \end{pmatrix}.
$$

Por tanto:

$$
u = \frac{x + \sqrt3\,y}{2}, \qquad v = \frac{- \sqrt3\,x + y}{2}.
$$

La condición para que $(x,y)$ esté en la imagen es:

$$
v = u^2 - 5.
$$

Como además $(x,y)$ debe estar sobre la parábola original:

$$
y = x^2 - 5. \tag{1}
$$

Sustituimos $y = x^2 - 5$ en la condición de la imagen.

## 3. Sustitución

Con $y = x^2 - 5$, calculamos:

$$
u = \frac{x + \sqrt3(x^2 - 5)}{2}
= \frac{\sqrt3 x^2 + x - 5\sqrt3}{2}.
$$

$$
v = \frac{-\sqrt3 x + x^2 - 5}{2}.
$$

La condición $v = u^2 - 5$ se convierte en:

$$
\frac{-\sqrt3 x + x^2 - 5}{2}
=
\left( \frac{\sqrt3 x^2 + x - 5\sqrt3}{2} \right)^2 - 5.
$$

## 4. Multiplicando por 4

Multiplicamos por $4$:

$$
2(-\sqrt3 x + x^2 - 5) = (\sqrt3 x^2 + x - 5\sqrt3)^2 - 20.
$$

Esto es:

$$
-2\sqrt3 x + 2x^2 - 10 = (\sqrt3 x^2 + x - 5\sqrt3)^2 - 20.
$$

Sumamos $20$ a ambos lados:

$$
-2\sqrt3 x + 2x^2 + 10 = (\sqrt3 x^2 + x - 5\sqrt3)^2. \tag{2}
$$

## 5. Expandiendo el cuadrado

Sea $A = \sqrt3 x^2$, $B = x$, $C = -5\sqrt3$. Su suma es:

$$
\sqrt3 x^2 + x - 5\sqrt3.
$$

Elevamos al cuadrado:

$$
A^2 + B^2 + C^2 + 2AB + 2AC + 2BC.
$$

Calculamos cada término:

- $A^2 = 3x^4$.
- $B^2 = x^2$.
- $C^2 = 25 \cdot 3 = 75$.
- $2AB = 2\sqrt3 x^3$.
- $2AC = 2 \cdot \sqrt3 x^2 \cdot (-5\sqrt3) = -30 x^2$.
- $2BC = 2 \cdot x \cdot (-5\sqrt3) = -10\sqrt3 x$.

Entonces:

$$
(\sqrt3 x^2 + x - 5\sqrt3)^2
= 3x^4 + 2\sqrt3 x^3 + x^2 - 30x^2 - 10\sqrt3 x + 75
= 3x^4 + 2\sqrt3 x^3 - 29x^2 - 10\sqrt3 x + 75.
$$

## 6. Igualando según (2)

Tenemos:

$$
-2\sqrt3 x + 2x^2 + 10
=
3x^4 + 2\sqrt3 x^3 - 29x^2 - 10\sqrt3 x + 75.
$$

Llevamos todo al lado derecho:

$$
0
=
3x^4 + 2\sqrt3 x^3 - 29x^2 - 10\sqrt3 x + 75
- (-2\sqrt3 x + 2x^2 + 10).
$$

Distribuimos el signo:

$$
3x^4 + 2\sqrt3 x^3 - 29x^2 - 10\sqrt3 x + 75 + 2\sqrt3 x - 2x^2 - 10.
$$

Simplificamos:

- Términos con $\sqrt3 x$: $-10\sqrt3 x + 2\sqrt3 x = -8\sqrt3 x$.

Entonces:

$$
0 = 3x^4 + 2\sqrt3 x^3 - 31x^2 - 8\sqrt3 x + 65. \tag{3}
$$

## 7. Separando parte racional e irracional

Separamos los términos con $\sqrt3$ y sin $\sqrt3$:

$$
(3x^4 - 31x^2 + 65) + (2\sqrt3 x^3 - 8\sqrt3 x) = 0.
$$

Es decir:

$$
(3x^4 - 31x^2 + 65) + \sqrt3(2x^3 - 8x) = 0.
$$

Para que esta igualdad sea cierta con $x$ real (y resultado racional en general), la estrategia usual es despejar. Como $x$ puede no ser racional, no necesariamente ambas partes son cero por separado, pero aquí conviene reagrupar:

$$
3x^4 - 31x^2 + 65 = -\sqrt3(2x^3 - 8x).
$$

Factorizamos el lado derecho:

$$
2x^3 - 8x = 2x(x^2 - 4).
$$

Entonces:

$$
3x^4 - 31x^2 + 65 = -2\sqrt3 x(x^2 - 4). \tag{4}
$$

## 8. Elevando al cuadrado para eliminar el radical

Elevamos al cuadrado ambos lados de (4):

$$
(3x^4 - 31x^2 + 65)^2 = 12 x^2 (x^2 - 4)^2.
$$

Expandimos.

Primero el lado derecho:

$$
(x^2 - 4)^2 = x^4 - 8x^2 + 16.
$$

Luego:

$$
12x^2(x^4 - 8x^2 + 16) = 12x^6 - 96x^4 + 192x^2.
$$

Ahora el lado izquierdo. Sea $t = x^2$. Entonces:

$$
3x^4 - 31x^2 + 65 = 3t^2 - 31 t + 65.
$$

Queremos:

$$
(3t^2 - 31t + 65)^2.
$$

Expandimos:

$$
(3t^2)^2 + (-31t)^2 + 65^2 + 2(3t^2)(-31t) + 2(3t^2)(65) + 2(-31t)(65).
$$

Calculamos:

- $(3t^2)^2 = 9t^4$.
- $(-31t)^2 = 961t^2$.
- $65^2 = 4225$.
- $2 \cdot 3t^2 \cdot (-31t) = -186 t^3$.
- $2 \cdot 3t^2 \cdot 65 = 390 t^2$.
- $2 \cdot (-31t) \cdot 65 = -4030 t$.

Sumamos términos semejantes:

$$
9t^4 - 186t^3 + (961 + 390)t^2 - 4030t + 4225.
$$

$$
= 9t^4 - 186t^3 + 1351t^2 - 4030t + 4225.
$$

Volviendo a $x$:

$$
(3x^4 - 31x^2 + 65)^2
= 9x^8 - 186x^6 + 1351x^4 - 4030x^2 + 4225.
$$

Entonces la ecuación completa es:

$$
9x^8 - 186x^6 + 1351x^4 - 4030x^2 + 4225
=
12x^6 - 96x^4 + 192x^2.
$$

Llevamos todo al lado izquierdo:

$$
9x^8 - 186x^6 - 12x^6 + 1351x^4 + 96x^4 - 4030x^2 - 192x^2 + 4225 = 0.
$$

$$

9x^8 - 198x^6 + 1447x^4 - 4222x^2 + 4225 = 0. \tag{5}
$$

## 9. Factorización

Sospechamos que la parábola original y su imagen se intersectan en pocos puntos. Probamos valores sencillos de $x$ inspirados en la simetría.

Una observación útil: el vértice de la parábola original es $(0,-5)$. Al rotar $60^\circ$, su imagen es:

$$
X = \frac12 \cdot 0 - \frac{\sqrt3}{2}(-5) = \frac{5\sqrt3}{2}, \qquad
Y = \frac{\sqrt3}{2}\cdot 0 + \frac12(-5) = -\frac52.
$$

Ese punto no está en la parábola original. Pero puede haber intersecciones simétricas.

Probemos si $x$ está relacionado con $\sqrt3$. 

Una alternativa más limpia es no elevar al cuadrado, sino resolver el sistema linealmente para $\sqrt3$.

## 10. Método más limpio: despejar $\sqrt3$

De (3):

$$
3x^4 - 31x^2 + 65 + \sqrt3(2x^3 - 8x) = 0.
$$

Si $2x^3 - 8x \ne 0$, despejamos:

$$
\sqrt3 = -\frac{3x^4 - 31x^2 + 65}{2x^3 - 8x}
= -\frac{3x^4 - 31x^2 + 65}{2x(x^2-4)}. \tag{6}
$$

Como $x$ debe dar un valor real razonable, busquemos soluciones mediante factorización de (5).

## 11. Buscando raíces de (5)

Sabemos por el contexto geométrico que hay exactamente un punto de intersección en el cuarto cuadrante. En el cuarto cuadrante, $x>0$ e $y<0$.

Probamos factorizar el polinomio (5). Una raíz candidata sale al considerar simetrías. La rotación de $60^\circ$ sugiere ángulos como $30^\circ$, $150^\circ$, etc., así que podrían aparecer valores con $\sqrt3$ y fracciones.

Probemos $x = \frac{\sqrt3}{2}$ o $x = \frac{3}{2}$.

Evaluamos el polinomio en algunos valores. Pero hacerlo a mano es tedioso. En su lugar, usemos una identidad.

De la condición geométrica, si un punto $(x,y)$ está en la intersección, también lo está su rotación. Como las parábolas son simétricas respecto... en realidad el problema garantiza exactamente un punto en el cuarto cuadrante, lo que sugiere que las raíces aparecen en valores concretos.

Probemos si $x = \frac{1}{\sqrt3}$ (es decir, $x^2 = 1/3$) es solución. Sustituimos en (5):

- $x^2 = \frac13$, $x^4 = \frac19$, $x^6 = \frac1{27}$, $x^8 = \frac1{81}$.

Entonces:

$$
9\cdot \frac1{81} - 198\cdot \frac1{27} + 1447\cdot \frac19 - 4222\cdot \frac13 + 4225.
$$

Calculamos:

$$
\frac{9}{81} = \frac19, \qquad
-198/27 = -\frac{22}{3}, \qquad
1447/9, \qquad
-4222/3, \qquad
+4225.
$$

Llevando a denominador 9:

$$
\frac{1 - 66 + 1447 - 12666 + 38025}{9}
= \frac{26741}{9},
$$

que no es cero. Descartado.

Probemos $x = \frac{\sqrt3}{3}$. Es lo mismo que $x^2 = 1/3$; descartado.

Probemos $x = \frac{\sqrt3}{2}$, o sea $x^2 = 3/4$.

- $x^4 = 9/16$, $x^6 = 27/64$, $x^8 = 81/256$.

Evaluamos:

$$
9\cdot \frac{81}{256} - 198\cdot \frac{27}{64} + 1447\cdot \frac{9}{16} - 4222\cdot \frac{3}{4} + 4225.
$$

Primer término: $729/256$.

Segundo: $-5346/64 = -21384/256$.

Tercero: $13023/16 = 208368/256$.

Cuarto: $-12666/4 = -3166.5$; en denominador 256: $-12666\cdot 64 /256 = -810624/256$.

Quinto: $4225 \cdot 256 / 256 = 1081600/256$.

Sumamos numeradores:

$$
729 - 21384 + 208368 - 810624 + 1081600
= 468689.
$$

No es cero.

Probemos $x = \sqrt3$. Entonces $x^2 = 3$, $x^4 = 9$, $x^6 = 27$, $x^8 = 81$.

$$
9\cdot 81 - 198\cdot 27 + 1447\cdot 9 - 4222\cdot 3 + 4225.
$$

$$
729 - 5346 + 13023 - 12666 + 4225.
$$

Sumamos:

$729 - 5346 = -4617$. 

$-4617 + 13023 = 8406$.

$8406 - 12666 = -4260$.

$-4260 + 4225 = -35$.

No es cero.

Probemos valores más simples: $x = 2$, $x^2=4$, $x^4=16$, $x^6=64$, $x^8=256$.

$$
9\cdot 256 - 198\cdot 64 + 1447\cdot 16 - 4222\cdot 4 + 4225.
$$

$$
2304 - 12672 + 23152 - 16888 + 4225.
$$

$2304 - 12672 = -10368$. 

$-10368 + 23152 = 12784$. 

$12784 - 16888 = -4104$. 

$-4104 + 4225 = 121$.

No es cero.

Probemos $x = 1$:

$$
9 - 198 + 1447 - 4222 + 4225
= 1261.
$$

No.

Probemos $x = \sqrt{\frac{5}{3}}$, pues quizá relacionado con $y$-coordenada. Si $x^2 = 5/3$:

- $x^4 = 25/9$, $x^6 = 125/27$, $x^8 = 625/81$.

Evaluamos:

$$
9\cdot \frac{625}{81} - 198\cdot \frac{125}{27} + 1447\cdot \frac{25}{9} - 4222\cdot \frac{5}{3} + 4225.
$$

Simplificamos término a término:

1) $9\cdot 625/81 = 625/9$.
2) $-198\cdot 125/27 = -24750/27 = -8250/9$.
3) $1447\cdot 25/9 = 36175/9$.
4) $-4222\cdot 5/3 = -21110/3 = -63330/9$.
5) $4225 = 38025/9$.

Sumamos numeradores:

$$
625 - 8250 + 36175 - 63330 + 38025
= 3245.
$$

No.

Quizá debamos resolver de forma sistemática.

## 12. Usando la ecuación (3) directamente

Quizá haya una solución sencilla con $x$ tal que ambos términos en (3) se anulen por separado. Busquemos $x$ que satisfaga simultáneamente:

$$
3x^4 - 31x^2 + 65 = 0, \qquad 2x^3 - 8x = 0.
$$

La segunda da $2x(x^2-4)=0$, así que $x=0$ o $x=\pm 2$. Sustituimos en la primera:

- $x=0$: $65 \ne 0$.
- $x=2$: $3\cdot 16 - 31\cdot 4 + 65 = 48 - 124 + 65 = -11 \ne 0$.
- $x=-2$: mismo resultado.

Así que no.

## 13. Replanteando con la ecuación polinómica

Volvamos a (5) y busquemos factorizaciones. Quizá el polinomio tenga un factor cuadrático agradable.

Observemos que los puntos de intersección comunes deben cumplir que la parábola original y su rotación coinciden. Por la naturaleza del problema (exactamente un punto en el cuatro cuadrante), probablemente haya una solución con $x$ positivo y $y$ negativo.

Probemos si $x = \frac32$ es raíz.

$x^2 = 9/4$, $x^4 = 81/16$, $x^6 = 729/64$, $x^8 = 6561/256$.

$$

9\cdot \frac{6561}{256} - 198\cdot \frac{729}{64} + 1447\cdot \frac{81}{16} - 4222\cdot \frac{9}{4} + 4225.
$$

Calculamos en denominador 256:

1) $59049/256$.
2) $-198\cdot 729/64 = -144342/64 = -577368/256$.
3) $1447\cdot 81/16 = 117207/16 = 1875312/256$.
4) $-4222\cdot 9/4 = -37998/4 = -2431872/256$.
5) $4225 \cdot 256 = 1081600/256$.

Sumamos numeradores:

$$
59049 - 577368 + 1875312 - 2431872 + 1081600.
$$

$59049 - 577368 = -518319$. 

$-518319 + 1875312 = 1356993$. 

$1356993 - 2431872 = -1074879$. 

$-1074879 + 1081600 = 6721$.

No es cero.

Probemos $x = \frac{5}{2}$.

$x^2 = 25/4$, $x^4 = 625/16$, $x^6 = 15625/64$, $x^8 = 390625/256$.

Evaluamos en denominador 256:

1) $9\cdot 390625/256 = 3515625/256$.
2) $-198\cdot 15625/64 = -3093750/64 = -12375000/256$.
3) $1447\cdot 625/16 = 904375/16 = 14470000/256$.
4) $-4222\cdot 25/4 = -105550/4 = -6755200/256$.
5) $4225\cdot 256 = 1081600/256$.

Sumamos numeradores:

$$
3515625 - 12375000 + 14470000 - 6755200 + 1081600.
$$

$3515625 - 12375000 = -8859375$. 

$-8859375 + 14470000 = 5610625$. 

$5610625 - 6755200 = -1144575$. 

$-1144575 + 1081600 = -62975$.

No.

## 14. Enfoque con el resultado pedido

El problema dice que el punto de intersección en el cuarto cuadrante tiene $y$-coordenada

$$
y = \frac{a - \sqrt b}{c}.
$$

Probablemente $a$, $b$, $c$ sean números no muy grandes. En el cuarto cuadrante, $y<0$. La forma $\frac{a-\sqrt b}{c}$ es negativa si $\sqrt b > a$.

Para la parábola rotada, quizá convenga encontrar directamente la ecuación explícita en $(X,Y)$.

## 15. Ecuación implícita de la parábola rotada

Sabemos que $(X,Y)$ está en la imagen si su preimagen $(u,v)$ está en la original:

$$
u = \frac{X + \sqrt3 Y}{2}, \qquad v = \frac{-\sqrt3 X + Y}{2},
$$

donde $(u,v)$ se obtuvo rotando $(X,Y)$ por $-60^\circ$. La ecuación $v = u^2 - 5$ da:

$$
\frac{-\sqrt3 X + Y}{2}
=
\left(\frac{X+\sqrt3 Y}{2}\right)^2 - 5.
$$

Multiplicamos por 4:

$$
-2\sqrt3 X + 2Y = (X+\sqrt3 Y)^2 - 20.
$$

Esto es la ecuación de la parábola rotada en coordenadas $(X,Y)$.

Para encontrar intersecciones con $Y = X^2 - 5$, sustituimos $Y$ en la ecuación anterior. Como ya hicimos antes, usando $(x,y)$ (renombrando $X\to x$, $Y\to y$), obtenemos la misma condición.

## 16. Simplificación mediante combinación de ambas ecuaciones

Tenemos el sistema:

$$
y = x^2 - 5, \tag{A}
$$

$$

-2\sqrt3 x + 2y = (x+\sqrt3 y)^2 - 20. \tag{B}
$$

Sustituimos (A) en (B). Ya hicimos ese cálculo y llegamos a:

$$
3x^4 + 2\sqrt3 x^3 - 31x^2 - 8\sqrt3 x + 65 = 0. \tag{3'}
$$

## 17. Buscando soluciones simbólicas

Tratemos de factorizar (3') como producto de dos cuadráticas con coeficientes que involucren $\sqrt3$.

Postulemos:

$$
3x^4 + 2\sqrt3 x^3 - 31x^2 - 8\sqrt3 x + 65 = (Ax^2 + Bx + C)(Dx^2 + Ex + F).
$$

Como el coeficiente líder es $3$, tomemos $A=3$, $D=1$ (o variantes). Probemos:

$$
(3x^2 + px + q)(x^2 + rx + s).
$$

Expandimos:

$$
3x^4 + (3r+p)x^3 + (3s+pr+q)x^2 + (ps+qr)x + qs.
$$

Igualamos coeficientes:

1. $3r + p = 2\sqrt3$.
2. $3s + pr + q = -31$.
3. $ps + qr = -8\sqrt3$.
4. $qs = 65$.

Como $qs = 65$, con $q,s$ quizá enteros o involucrando $\sqrt3$. Los divisores de $65$: $\pm 1, \pm 5, \pm 13, \pm 65$.

Probemos $q=5$, $s=13$ (o viceversa).

Si $q=5$, $s=13$.

Ecuación 1: $p = 2\sqrt3 - 3r$.

Ecuación 3: $p \cdot 13 + 5r = -8\sqrt3$.

Sustituimos $p$:

$$
13(2\sqrt3 - 3r) + 5r = -8\sqrt3.
$$

$$

26\sqrt3 - 39r + 5r = -8\sqrt3.
$$

$$

26\sqrt3 - 34r = -8\sqrt3.
$$

$$

-34r = -34\sqrt3 \implies r = \sqrt3.
$$

Entonces $p = 2\sqrt3 - 3\sqrt3 = -\sqrt3$.

Verificamos la ecuación 2:

$$
3s + pr + q = 3\cdot 13 + (-\sqrt3)(\sqrt3) + 5
= 39 - 3 + 5 = 41 \ne -31.
$$

No funciona.

Probemos $q=13$, $s=5$.

$p = 2\sqrt3 - 3r$.

Ecuación 3: $p\cdot 5 + 13r = -8\sqrt3$.

$$

5(2\sqrt3 - 3r) + 13r = -8\sqrt3.
$$

$$

10\sqrt3 - 15r + 13r = -8\sqrt3.
$$

$$

10\sqrt3 - 2r = -8\sqrt3.
$$

$$

-2r = -18\sqrt3 \implies r = 9\sqrt3.
$$

Entonces $p = 2\sqrt3 - 27\sqrt3 = -25\sqrt3$.

Verificamos ecuación 2:

$$
3\cdot 5 + p r + 13 = 15 + (-25\sqrt3)(9\sqrt3) + 13
= 28 - 25\cdot 27 = 28 - 675 = -647 \ne -31.
$$

No.

Probemos valores negativos. $q=-5$, $s=-13$. Como $qs = 65$ ok.

$p = 2\sqrt3 - 3r$.

Ecuación 3: $p(-13) + (-5)r = -8\sqrt3$, o sea $-13p -5r = -8\sqrt3$.

Sustituimos $p$:

$$
-13(2\sqrt3 - 3r) - 5r = -8\sqrt3.
$$

$$

-26\sqrt3 + 39r - 5r = -8\sqrt3.
$$

$$

-26\sqrt3 + 34r = -8\sqrt3.
$$

$$

34r = 18\sqrt3 \implies r = \frac{9\sqrt3}{17}.
$$

Esto complica las cosas, probablemente no sea el camino.

Probemos $q=-13$, $s=-5$.

Ecuación 3: $-5p - 13r = -8\sqrt3$.

$$

-5(2\sqrt3 - 3r) - 13r = -8\sqrt3.
$$

$$

-10\sqrt3 + 15r - 13r = -8\sqrt3.
$$

$$

-10\sqrt3 + 2r = -8\sqrt3.
$$

$$

2r = 2\sqrt3 \implies r = \sqrt3.
$$

Entonces $p = 2\sqrt3 - 3\sqrt3 = -\sqrt3$.

Verificamos ecuación 2:

$$
3s + pr + q = 3(-5) + (-\sqrt3)(\sqrt3) + (-13)
= -15 - 3 - 13 = -31.
$$

¡Funciona! Entonces:

$$
3x^4 + 2\sqrt3 x^3 - 31x^2 - 8\sqrt3 x + 65
=
(3x^2 - \sqrt3 x - 13)(x^2 + \sqrt3 x - 5).
$$

## 18. Resolviendo las cuadráticas

Tenemos:

$$
(3x^2 - \sqrt3 x - 13)(x^2 + \sqrt3 x - 5) = 0.
$$

Así que:

$$
3x^2 - \sqrt3 x - 13 = 0 \quad \text{o} \quad x^2 + \sqrt3 x - 5 = 0.
$$

### Segunda cuadrática

$$
x^2 + \sqrt3 x - 5 = 0.
$$

Resolvemos:

$$
x = \frac{-\sqrt3 \pm \sqrt{3 + 20}}{2}
= \frac{-\sqrt3 \pm \sqrt{23}}{2}.
$$

Las raíces son:

$$
x_1 = \frac{-\sqrt3 + \sqrt{23}}{2}, \qquad x_2 = \frac{-\sqrt3 - \sqrt{23}}{2}.
$$

$x_1$ es positivo porque $\sqrt{23} > \sqrt3$, así que aproximadamente $\frac{4.7958 - 1.732}{2} \approx 1.5319 > 0$. $x_2$ es negativo.

### Primera cuadrática

$$
3x^2 - \sqrt3 x - 13 = 0.
$$

$$

x = \frac{\sqrt3 \pm \sqrt{3 + 156}}{6}
= \frac{\sqrt3 \pm \sqrt{159}}{6}.
$$

Raíces:

$$
x_3 = \frac{\sqrt3 + \sqrt{159}}{6} > 0, \qquad
x_4 = \frac{\sqrt3 - \sqrt{159}}{6} < 0.
$$

## 19. Identificando el punto del cuarto cuadrante

En el cuarto cuadrante, $x>0$ e $y<0$. Las raíces positivas son $x_1$ y $x_3$. Debemos ver cuál produce $y<0$.

Para $x_1 = \frac{-\sqrt3 + \sqrt{23}}{2} \approx 1.5319$, calculamos:

$$
y = x_1^2 - 5.
$$

$$

x_1^2 = \frac{(-\sqrt3+\sqrt{23})^2}{4}
= \frac{3 - 2\sqrt{69} + 23}{4}
= \frac{26 - 2\sqrt{69}}{4}
= \frac{13 - \sqrt{69}}{2}.
$$

Entonces:

$$
y = \frac{13 - \sqrt{69}}{2} - 5
= \frac{13 - \sqrt{69} - 10}{2}
= \frac{3 - \sqrt{69}}{2}.
$$

Como $\sqrt{69} \approx 8.3066$, $y \approx \frac{3 - 8.3066}{2} \approx -2.6533 < 0$. Así que $x_1$ está en el cuarto cuadrante.

Para $x_3 = \frac{\sqrt3 + \sqrt{159}}{6} \approx \frac{1.732 + 12.6095}{6} \approx 2.3903$.

$$

y = x_3^2 - 5.
$$

$$

x_3^2 = \frac{(\sqrt3 + \sqrt{159})^2}{36}
= \frac{3 + 2\sqrt{477} + 159}{36}
= \frac{162 + 2\sqrt{477}}{36}
= \frac{81 + \sqrt{477}}{18}.
$$

Entonces:

$$

y = \frac{81 + \sqrt{477}}{18} - 5
= \frac{81 + \sqrt{477} - 90}{18}
= \frac{-9 + \sqrt{477}}{18}.
$$

Como $\sqrt{477} \approx 21.8403$, $y \approx \frac{12.8403}{18} \approx 0.7133 > 0$. Así que $x_3$ está en el primer cuadrante.

Por tanto, el punto en el cuarto cuadrante corresponde a $x_1$, y su $y$ es:

$$
y = \frac{3 - \sqrt{69}}{2}.
$$

Comparando con la forma:

$$
y = \frac{a - \sqrt b}{c},
$$

tenemos:

$$
a = 3, \qquad b = 69, \qquad c = 2.
$$

$a=3$ y $c=2$ son relativamente primos.

## 20. Suma final

$$

a+b+c = 3 + 69 + 2 = 74.
$$

\boxed{74}