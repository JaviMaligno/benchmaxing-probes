Vamos a resolver el problema paso a paso.

## 1. Planteamiento

La parábola original es

\[
y = x^2 - 4.
\]

La rotamos \(60^\circ\) en sentido antihorario alrededor del origen. Buscamos el punto en el cuarto cuadrante donde la parábola original y su imagen se intersectan.

## 2. Imagen de la parábola bajo rotación

Una rotación antihoraria de ángulo \(\theta\) transforma un punto \((x, y)\) en

\[
(x', y') = (x\cos\theta - y\sin\theta,\; x\sin\theta + y\cos\theta).
\]

Para \(\theta = 60^\circ\), tenemos

\[
\cos 60^\circ = \frac{1}{2}, \qquad \sin 60^\circ = \frac{\sqrt{3}}{2}.
\]

Entonces la transformación inversa (para expresar las coordenadas originales en términos de las rotadas) es una rotación horaria de \(60^\circ\):

\[
x = \frac{1}{2}x' + \frac{\sqrt{3}}{2}y',
\]

\[
y = -\frac{\sqrt{3}}{2}x' + \frac{1}{2}y'.
\]

La ecuación de la imagen rotada se obtiene sustituyendo \(x, y\) en la ecuación original \(y = x^2 - 4\):

\[
-\frac{\sqrt{3}}{2}x' + \frac{1}{2}y' = \left(\frac{1}{2}x' + \frac{\sqrt{3}}{2}y'\right)^2 - 4.
\]

Quitando las primas, la imagen satisface

\[
-\frac{\sqrt{3}}{2}x + \frac{1}{2}y = \left(\frac{1}{2}x + \frac{\sqrt{3}}{2}y\right)^2 - 4.
\]

Multiplicando por 4:

\[
-2\sqrt{3}\,x + 2y = (x + \sqrt{3}\,y)^2 - 16.
\]

O bien:

\[
(x + \sqrt{3}\,y)^2 + 2\sqrt{3}\,x - 2y - 16 = 0. \tag{1}
\]

## 3. Intersección

Un punto de intersección debe cumplir tanto la ecuación original

\[
y = x^2 - 4
\]

como la ecuación (1). Sustituimos \(y = x^2 - 4\) en (1).

Primero:

\[
x + \sqrt{3}\,y = x + \sqrt{3}(x^2 - 4) = \sqrt{3}\,x^2 + x - 4\sqrt{3}.
\]

Elevamos al cuadrado:

\[
(x + \sqrt{3}\,y)^2 = (\sqrt{3}\,x^2 + x - 4\sqrt{3})^2.
\]

Desarrollamos:

\[
= 3x^4 + 2\sqrt{3}\,x^3 - 24x^2 + x^2 - 8\sqrt{3}\,x + 48
\]

\[
= 3x^4 + 2\sqrt{3}\,x^3 - 23x^2 - 8\sqrt{3}\,x + 48.
\]

Además,

\[
2\sqrt{3}\,x - 2y = 2\sqrt{3}\,x - 2(x^2 - 4) = 2\sqrt{3}\,x - 2x^2 + 8.
\]

Entonces la ecuación (1) se convierte en:

\[
\left(3x^4 + 2\sqrt{3}\,x^3 - 23x^2 - 8\sqrt{3}\,x + 48\right) + \left(2\sqrt{3}\,x - 2x^2 + 8\right) - 16 = 0.
\]

Simplificando:

\[
3x^4 + 2\sqrt{3}\,x^3 - 25x^2 - 6\sqrt{3}\,x + 40 = 0. \tag{2}
\]

## 4. Factorización

Buscamos factores. Observemos que los puntos de intersección deben cumplir también la relación geométrica. Probemos si hay una factorización por inspección.

La parábola original corta al eje \(y\) en \((0, -4)\). Bajo rotación de \(60^\circ\), ese punto se convierte en

\[
(0\cdot \tfrac12 - (-4)\cdot \tfrac{\sqrt3}{2},\; 0\cdot \tfrac{\sqrt3}{2} + (-4)\cdot \tfrac12)
= (2\sqrt{3}, -2).
\]

Este punto \((2\sqrt3, -2)\) está en el cuarto cuadrante. ¿Pertenece también a la parábola original?

Verificamos:

\[
y = x^2 - 4 \implies -2 = (2\sqrt3)^2 - 4 = 12 - 4 = 8,
\]

lo cual es falso. Así que no es un punto de intersección.

Probemos una factorización de (2). Escribimos la ecuación polinómica de cuarto grado en \(x\) con coeficientes que involucran \(\sqrt3\). La parte racional y la parte con \(\sqrt3\) deben anularse por separado.

Escribimos (2) como:

\[
(3x^4 - 25x^2 + 40) + \sqrt{3}\,(2x^3 - 6x) = 0.
\]

Para que esto sea cero como número real, no es necesario que ambas partes sean cero por separado. Sin embargo, para hallar soluciones sencillas, probemos si hay soluciones donde \(2x^3 - 6x = 0\).

\[
2x(x^2 - 3) = 0 \implies x = 0, \pm \sqrt3.
\]

- \(x = 0\): parte racional \(= 40 \neq 0\). Descartado.
- \(x = \sqrt3\): parte racional
  \[
  3(\sqrt3)^4 - 25(\sqrt3)^2 + 40 = 3\cdot 9 - 25\cdot 3 + 40 = 27 - 75 + 40 = -8 \neq 0.
  \]
  Descartado.
- \(x = -\sqrt3\): igual, da \(-8 \neq 0\). Descartado.

Así que no hay soluciones con la parte irracional nula.

## 5. Uso de la propiedad de la rotación

Una forma más cómoda: para que un punto \((x, y)\) esté en la intersección, tanto \((x, y)\) como su imagen rotada deben estar en el mismo lugar resuelto por el sistema.

El punto de intersección \((x, y)\) satisface:

- Pertenece a la parábola original: \(y = x^2 - 4\).
- Su rotación de \(60^\circ\) antihorario también pertenece a la parábola original.

Es decir, si definimos

\[
R_\theta(x, y) = (x\cos\theta - y\sin\theta,\; x\sin\theta + y\cos\theta),
\]

entonces el punto rotado \(R_{60^\circ}(x, y)\) debe cumplir:

\[
x\sin60^\circ + y\cos60^\circ = (x\cos60^\circ - y\sin60^\circ)^2 - 4.
\]

Con \(\theta = 60^\circ\):

\[
\frac{\sqrt3}{2}x + \frac{1}{2}y = \left(\frac{1}{2}x - \frac{\sqrt3}{2}y\right)^2 - 4.
\]

Multiplicando por 4:

\[
2\sqrt3\,x + 2y = (x - \sqrt3\,y)^2 - 16.
\]

Esta es equivalente a (1). Sustituyendo \(y = x^2 - 4\):

\[
2\sqrt3\,x + 2(x^2 - 4) = \left(x - \sqrt3(x^2 - 4)\right)^2 - 16.
\]

\[
2x^2 + 2\sqrt3\,x - 8 = \left(x - \sqrt3\,x^2 + 4\sqrt3\right)^2 - 16.
\]

\[
2x^2 + 2\sqrt3\,x + 8 = \left(-\sqrt3\,x^2 + x + 4\sqrt3\right)^2.
\]

La expresión del cuadrado:

\[
(-\sqrt3\,x^2 + x + 4\sqrt3)^2 = 3x^4 - 2\sqrt3\,x^3 - 24x^2 + 8\sqrt3\,x + 48 + x^2.
\]

Espera, desarrollemos con cuidado:

Sea \(A = -\sqrt3\,x^2\), \(B = x\), \(C = 4\sqrt3\).

\[
(A+B+C)^2 = A^2 + B^2 + C^2 + 2AB + 2AC + 2BC.
\]

\[
A^2 = 3x^4, \quad B^2 = x^2, \quad C^2 = 48.
\]

\[
2AB = 2(-\sqrt3 x^2)(x) = -2\sqrt3\,x^3.
\]

\[
2AC = 2(-\sqrt3 x^2)(4\sqrt3) = -24x^2.
\]

\[
2BC = 2(x)(4\sqrt3) = 8\sqrt3\,x.
\]

Entonces:

\[
= 3x^4 - 2\sqrt3\,x^3 + x^2 - 24x^2 + 8\sqrt3\,x + 48.
\]

\[
= 3x^4 - 2\sqrt3\,x^3 - 23x^2 + 8\sqrt3\,x + 48.
\]

Igualamos:

\[
2x^2 + 2\sqrt3\,x + 8 = 3x^4 - 2\sqrt3\,x^3 - 23x^2 + 8\sqrt3\,x + 48.
\]

Pasando todo a un lado:

\[
0 = 3x^4 - 2\sqrt3\,x^3 - 23x^2 + 8\sqrt3\,x + 48 - 2x^2 - 2\sqrt3\,x - 8.
\]

\[
0 = 3x^4 - 2\sqrt3\,x^3 - 25x^2 + 6\sqrt3\,x + 40.
\]

Esta es exactamente la ecuación (2).

## 6. Solución del cuarto grado

La ecuación es:

\[
3x^4 - 2\sqrt3\,x^3 - 25x^2 + 6\sqrt3\,x + 40 = 0.
\]

Separamos en parte racional y parte irracional:

\[
(3x^4 - 25x^2 + 40) + \sqrt3\,(-2x^3 + 6x) = 0.
\]

\[
(3x^4 - 25x^2 + 40) + \sqrt3\,x\,(-2x^2 + 6) = 0.
\]

Como \(\sqrt3\) es irracional, no hay una factorización inmediata por separación. Sin embargo, podemos despejar \(\sqrt3\):

\[
\sqrt3 = \frac{3x^4 - 25x^2 + 40}{2x^3 - 6x} \quad \text{(si el denominador no es cero)}.
\]

Esto no ayuda directamente. Probemos a buscar soluciones racionales o sencillas.

Probemos \(x = 2\):

\[
3\cdot 16 - 2\sqrt3\cdot 8 - 25\cdot 4 + 6\sqrt3\cdot 2 + 40
= 48 - 16\sqrt3 - 100 + 12\sqrt3 + 40.
\]

\[
= (48 - 100 + 40) + (-16 + 12)\sqrt3 = -12 - 4\sqrt3 \neq 0.
\]

Probemos \(x = \frac{4}{\sqrt3}\). Calculamos:

\[
x^2 = \frac{16}{3}, \quad x^3 = \frac{64}{3\sqrt3} = \frac{64\sqrt3}{9}, \quad x^4 = \frac{256}{9}.
\]

\[
3x^4 = \frac{256}{3}, \quad -25x^2 = -\frac{400}{3}, \quad 40 = 40.
\]

Parte racional:

\[
\frac{256}{3} - \frac{400}{3} + 40 = -\frac{144}{3} + 40 = -48 + 40 = -8.
\]

Parte irracional:

\[
-2\sqrt3 \cdot x^3 + 6\sqrt3 \cdot x = -2\sqrt3 \cdot \frac{64\sqrt3}{9} + 6\sqrt3 \cdot \frac{4}{\sqrt3}.
\]

\[
= -\frac{128 \cdot 3}{9} + 24 = -\frac{128}{3} + 24 = -\frac{128}{3} + \frac{72}{3} = -\frac{56}{3} \neq 0.
\]

Descartado.

## 7. Sustitución por la relación entre \(x\) e \(y\)

Otra vía: usar que la rotación de la parábola y la parábola original son simétricas respecto de la bisectriz del ángulo de rotación? No, la rotación de \(60^\circ\) no es una simetría.

Quizá convenga usar la forma trigonométrica. Sabemos que el punto de intersección \((x, y)\) cumple \(y = x^2 - 4\).

También, como el punto está en el cuarto cuadrante, \(x > 0\), \(y < 0\).

Probemos una factorización astuta de la ecuación (2). Observemos la estructura:

\[
3x^4 - 2\sqrt3\,x^3 - 25x^2 + 6\sqrt3\,x + 40.
\]

Intentemos factorizar como producto de dos cuadráticos con coeficientes de la forma \(a + b\sqrt3\). Supongamos:

\[
(ux^2 + vx + w)(u'x^2 + v'x + w') = 0.
\]

Podemos intentar con coeficientes que mezclen \(\sqrt3\). Otra idea: dividir la ecuación por \(x^2\) si \(x \neq 0\), pero eso no simplifica.

Probemos buscar raíces de la forma \(x = p + q\sqrt3\).

Sustituimos \(x = p + q\sqrt3\). Esto se vuelve engorroso.

## 8. Enfoque con el ángulo de la recta

Observemos que el punto de intersección \((x,y)\) y su rotado \(R_{60}(x,y)\) están ambos sobre la parábola original. Los puntos de la parábola tienen la forma \((t, t^2 - 4)\).

Entonces debe existir \(t\) tal que:

\[
(x, y) = (t, t^2 - 4),
\]

y su rotado \(60^\circ\) antihorario también es de la forma \((s, s^2 - 4)\) para algún \(s \neq t\).

Esto produce un sistema con dos parámetros \(t\) y \(s\).

La rotación de \(60^\circ\) de \((t, t^2 - 4)\) es

\[
\left(\frac12 t - \frac{\sqrt3}{2}(t^2 - 4),\; \frac{\sqrt3}{2}t + \frac12(t^2 - 4)\right).
\]

Este punto debe ser igual a \((s, s^2 - 4)\).

Entonces:

\[
s = \frac12 t - \frac{\sqrt3}{2}(t^2 - 4), \tag{3}
\]

\[
s^2 - 4 = \frac{\sqrt3}{2}t + \frac12(t^2 - 4). \tag{4}
\]

Sustituimos (3) en (4):

\[
\left(\frac12 t - \frac{\sqrt3}{2}(t^2 - 4)\right)^2 - 4 = \frac{\sqrt3}{2}t + \frac12(t^2 - 4).
\]

Multiplicamos por 4 para simplificar:

Sea \(u = t\), \(v = t^2 - 4\).

\[
\left(t - \sqrt3(t^2 - 4)\right)^2 - 16 = 2\sqrt3\,t + 2(t^2 - 4).
\]

\[
\left(t - \sqrt3\,t^2 + 4\sqrt3\right)^2 - 16 = 2t^2 + 2\sqrt3\,t - 8.
\]

Esto es lo mismo que antes, con \(x = t\).

## 9. Resolver la cuártica explícitamente

La ecuación:

\[
3x^4 - 2\sqrt3\,x^3 - 25x^2 + 6\sqrt3\,x + 40 = 0.
\]

Intentemos una factorización de la forma:

\[
(x^2 + px + q)(3x^2 + rx + s) = 0,
\]

donde \(p, q, r, s\) pueden contener \(\sqrt3\).

Igualando coeficientes:

- Coeficiente de \(x^3\): \(r + 3p = -2\sqrt3\).
- Coeficiente de \(x^2\): \(s + pr + 3q = -25\).
- Coeficiente de \(x\): \(ps + qr = 6\sqrt3\).
- Término constante: \(qs = 40\).

Probemos valores. Como \(qs = 40\), si \(q\) y \(s\) son números sencillos, posibilidades: \(q = 8, s = 5\); \(q = 5, s = 8\); \(q = 4, s = 10\), etc., o con signos.

Supongamos \(q = 8\), \(s = 5\). Entonces:

\[
s + pr + 3q = 5 + pr + 24 = 29 + pr = -25 \implies pr = -54.
\]

\[
ps + qr = 5p + 8r = 6\sqrt3.
\]

\[
r + 3p = -2\sqrt3.
\]

De \(r = -2\sqrt3 - 3p\), sustituimos en \(5p + 8r = 6\sqrt3\):

\[
5p + 8(-2\sqrt3 - 3p) = 6\sqrt3.
\]

\[
5p - 16\sqrt3 - 24p = 6\sqrt3.
\]

\[
-19p = 22\sqrt3 \implies p = -\frac{22\sqrt3}{19}.
\]

Entonces \(r = -2\sqrt3 - 3\left(-\frac{22\sqrt3}{19}\right) = -2\sqrt3 + \frac{66\sqrt3}{19} = \frac{-38 + 66}{19}\sqrt3 = \frac{28\sqrt3}{19}\).

Ahora verificamos \(pr\):

\[
pr = \left(-\frac{22\sqrt3}{19}\right)\left(\frac{28\sqrt3}{19}\right) = -\frac{616 \cdot 3}{361} = -\frac{1848}{361} \approx -5.12,
\]

pero necesitábamos \(pr = -54\). No coincide.

Probemos \(q = 5\), \(s = 8\):

\[
8 + pr + 15 = 23 + pr = -25 \implies pr = -48.
\]

\[
8p + 5r = 6\sqrt3, \quad r + 3p = -2\sqrt3.
\]

De \(r = -2\sqrt3 - 3p\), sustituimos:

\[
8p + 5(-2\sqrt3 - 3p) = 6\sqrt3.
\]

\[
8p - 10\sqrt3 - 15p = 6\sqrt3.
\]

\[
-7p = 16\sqrt3 \implies p = -\frac{16\sqrt3}{7}.
\]

\[
r = -2\sqrt3 - 3\left(-\frac{16\sqrt3}{7}\right) = -2\sqrt3 + \frac{48\sqrt3}{7} = \frac{-14 + 48}{7}\sqrt3 = \frac{34\sqrt3}{7}.
\]

Verificamos \(pr\):

\[
pr = \left(-\frac{16\sqrt3}{7}\right)\left(\frac{34\sqrt3}{7}\right) = -\frac{544 \cdot 3}{49} = -\frac{1632}{49} \approx -33.3,
\]

pero necesitábamos \(pr = -48\). No coincide.

Tal vez los coeficientes tengan una forma distinta.

Probemos con factores que tengan término irracional.

Supongamos \(q = 4\sqrt3\), \(s = \frac{10}{\sqrt3} = \frac{10\sqrt3}{3}\). Entonces \(qs = 4\sqrt3 \cdot \frac{10\sqrt3}{3} = \frac{120}{3} = 40\). Bien.

Entonces:

\[
s + pr + 3q = \frac{10\sqrt3}{3} + pr + 12\sqrt3 = \frac{46\sqrt3}{3} + pr = -25.
\]

Esto obliga a que \(pr\) tenga parte racional \(-25\) y parte irracional \(-\frac{46\sqrt3}{3}\).

\[
ps + qr = p \cdot \frac{10\sqrt3}{3} + 4\sqrt3 \cdot r = 6\sqrt3.
\]

\[
r + 3p = -2\sqrt3.
\]

Este sistema con incógnitas \(p, r\) que mezclan racional e irracional es resoluble. Dejemos \(p = p_0 + p_1\sqrt3\), \(r = r_0 + r_1\sqrt3\). Es bastante laborioso.

## 10. Enfoque alternativo: usar la rotación del sistema de coordenadas

En lugar de rotar la parábola, rotemos los ejes. El punto de intersección \((x, y)\) satisface la parábola original y también su versión rotada. Podemos usar la ecuación en coordenadas rotadas.

La ecuación de la parábola original en coordenadas \((x, y)\) es \(y = x^2 - 4\).

En coordenadas rotadas un ángulo \(60^\circ\) horario \((u, v)\), la parábola original se transforma en la imagen que buscamos. Un punto \((x, y)\) pertenece a la imagen rotada si y solo si su rotación inversa pertenece a la original.

Ya lo hicimos. Volvamos a la ecuación cuártica y tratemos de resolverla numéricamente para identificar la raíz, y luego construir la solución exacta.

## 11. Solución numérica

La ecuación:

\[
f(x) = 3x^4 - 2\sqrt3\,x^3 - 25x^2 + 6\sqrt3\,x + 40.
\]

Evaluemos en algunos puntos:

- \(x = 0\): \(f(0) = 40\).
- \(x = 1\): \(3 - 2\sqrt3 - 25 + 6\sqrt3 + 40 = (3 - 25 + 40) + (-2 + 6)\sqrt3 = 18 + 4\sqrt3 > 0\).
- \(x = 2\): calculamos antes \(= -12 - 4\sqrt3 < 0\).

Hay una raíz entre 1 y 2.

- \(x = 1.5\):

\[
x^2 = 2.25, \quad x^3 = 3.375, \quad x^4 = 5.0625.
\]

\[
3x^4 = 15.1875, \quad -2\sqrt3 x^3 \approx -2(1.732)(3.375) \approx -11.691, \quad -25x^2 = -56.25,
\]

\[
6\sqrt3 x \approx 6(1.732)(1.5) = 15.588, \quad +40.
\]

Suma:

\[
15.1875 - 11.691 - 56.25 + 15.588 + 40 \approx 2.8345 > 0.
\]

- \(x = 1.7\):

\[
x^2 = 2.89, \quad x^3 = 4.913, \quad x^4 = 8.3521.
\]

\[
3x^4 = 25.0563, \quad -2\sqrt3 x^3 \approx -2(1.732)(4.913) \approx -17.028, \quad -25x^2 = -72.25,
\]

\[
6\sqrt3 x \approx 6(1.732)(1.7) = 17.6664, \quad +40.
\]

Suma:

\[
25.0563 - 17.028 - 72.25 + 17.6664 + 40 \approx -6.5553 < 0.
\]

Entonces la raíz está entre 1.5 y 1.7.

Prueba \(x = 1.6\):

\[
x^2 = 2.56, \quad x^3 = 4.096, \quad x^4 = 6.5536.
\]

\[
3x^4 = 19.6608, \quad -2\sqrt3 x^3 \approx -2(1.732)(4.096) \approx -14.1885, \quad -25x^2 = -64,
\]

\[
6\sqrt3 x \approx 6(1.732)(1.6) = 16.6272, \quad +40.
\]

Suma:

\[
19.6608 - 14.1885 - 64 + 16.6272 + 40 \approx -1.9005 < 0.
\]

Prueba \(x = 1.55\):

\[
x^2 = 2.4025, \quad x^3 = 3.723875, \quad x^4 = 5.77300625.
\]

\[
3x^4 \approx 17.3190, \quad -2\sqrt3 x^3 \approx -2(1.732)(3.7239) \approx -12.9003, \quad -25x^2 = -60.0625,
\]

\[
6\sqrt3 x \approx 6(1.732)(1.55) = 16.1076, \quad +40.
\]

Suma:

\[
17.3190 - 12.9003 - 60.0625 + 16.1076 + 40 \approx 0.4638 > 0.
\]

Prueba \(x = 1.575\):

\[
x^2 = 2.480625, \quad x^3 \approx 3.9069843, \quad x^4 \approx 6.1535003.
\]

\[
3x^4 \approx 18.4605, \quad -2\sqrt3 x^3 \approx -2(1.732)(3.9070) \approx -13.5350, \quad -25x^2 \approx -62.0156,
\]

\[
6\sqrt3 x \approx 6(1.732)(1.575) \approx 16.3698, \quad +40.
\]

Suma:

\[
18.4605 - 13.5350 - 62.0156 + 16.3698 + 40 \approx -0.7203 < 0.
\]

Prueba \(x = 1.565\):

\[
x^2 = 2.449225, \quad x^3 \approx 3.831037125, \quad x^4 \approx 5.9960731.
\]

\[
3x^4 \approx 17.9882, \quad -2\sqrt3 x^3 \approx -2(1.732)(3.8310) \approx -13.2717, \quad -25x^2 \approx -61.2306,
\]

\[
6\sqrt3 x \approx 6(1.732)(1.565) \approx 16.2624, \quad +40.
\]

Suma:

\[
17.9882 - 13.2717 - 61.2306 + 16.2624 + 40 \approx -0.2517 < 0.
\]

Prueba \(x = 1.558\):

\[
x^2 \approx 2.427364, \quad x^3 \approx 3.781833, \quad x^4 \approx 5.892095.
\]

\[
3x^4 \approx 17.6763, \quad -2\sqrt3 x^3 \approx -2(1.732)(3.7818) \approx -13.1011, \quad -25x^2 \approx -60.6841,
\]

\[
6\sqrt3 x \approx 6(1.732)(1.558) \approx 16.1905, \quad +40.
\]

Suma:

\[
17.6763 - 13.1011 - 60.6841 + 16.1905 + 40 \approx 0.0816 > 0.
\]

Prueba \(x = 1.5605\):

\[
x^2 \approx 2.43516025, \quad x^3 \approx 3.80006757, \quad x^4 \approx 5.92980546.
\]

\[
3x^4 \approx 17.7894, \quad -2\sqrt3 x^3 \approx -2(1.732)(3.8001) \approx -13.1655, \quad -25x^2 \approx -60.8790,
\]

\[
6\sqrt3 x \approx 6(1.732)(1.5605) \approx 16.2159, \quad +40.
\]

Suma:

\[
17.7894 - 13.1655 - 60.8790 + 16.2159 + 40 \approx -0.0392 < 0.
\]

Prueba \(x = 1.5595\):

\[
x^2 \approx 2.43214025, \quad x^3 \approx 3.79294272, \quad x^4 \approx 5.91448583.
\]

\[
3x^4 \approx 17.7435, \quad -2\sqrt3 x^3 \approx -2(1.732)(3.7929) \approx -13.1401, \quad -25x^2 \approx -60.8035,
\]

\[
6\sqrt3 x \approx 6(1.732)(1.5595) \approx 16.2017, \quad +40.
\]

Suma:

\[
17.7435 - 13.1401 - 60.8035 + 16.2017 + 40 \approx 0.0016 > 0.
\]

Así que la raíz en el cuarto cuadrante está cerca de \(x \approx 1.5597\).

Entonces:

\[
y = x^2 - 4 \approx 2.4323 - 4 = -1.5677.
\]

## 12. Hallar la forma exacta

El problema dice que la coordenada \(y\) del punto es

\[
\frac{a - \sqrt{b}}{c}.
\]

Con \(x \approx 1.5597\), \(y \approx -1.5677\).

Busquemos una expresión sencilla de la forma \(\frac{a - \sqrt{b}}{c}\) que valga aproximadamente \(-1.5677\).

Probemos con denominadores sencillos. Sabemos que \(x\) no es necesario; necesitamos \(y\).

Si \(y = \frac{a - \sqrt{b}}{c}\), con \(a,b,c\) enteros positivos. Probemos algunas posibilidades.

Buscamos \(y \approx -1.5677\). Entonces \(\frac{a - \sqrt{b}}{c} \approx -1.5677\), es decir, \(\sqrt{b} \approx a + 1.5677 c\).

Probemos \(c = 2\). Entonces \(y = \frac{a - \sqrt{b}}{2}\). Para que \(y \approx -1.5677\), necesitamos \(a - \sqrt{b} \approx -3.1354\), luego \(\sqrt{b} \approx a + 3.1354\).

Probemos \(a = 7\): \(\sqrt{b} \approx 10.1354\), \(b \approx 102.73\). No es entero cuadrado perfecto. Esto sugiere que probablemente la expresión involucra \(\sqrt{3}\) u otra raíz no perfecta.

Espera: el problema dice \(b\) es un entero positivo, no necesariamente libre de cuadrados. La expresión \(\frac{a - \sqrt{b}}{c}\) puede no simplificarse a un número sencillo.

Para obtener más información, resolvamos la cuártica exactamente.

## 13. Resolver la cuártica exactamente

Ecuación:

\[
3x^4 - 2\sqrt3\,x^3 - 25x^2 + 6\sqrt3\,x + 40 = 0.
\]

Hagamos la sustitución \(z = \frac{x}{\sqrt3}\) o algo similar. Observemos que \(\sqrt3\) aparece tanto en \(x^3\) como en \(x\).

Escribimos la ecuación como:

\[
3x^4 - 25x^2 + 40 = \sqrt3\,(2x^3 - 6x).
\]

Elevamos al cuadrado ambos lados (esto introduce soluciones extrañas que luego filtraremos):

\[
(3x^4 - 25x^2 + 40)^2 = 3(2x^3 - 6x)^2.
\]

Desarrollemos el lado derecho:

\[
(2x^3 - 6x)^2 = 4x^6 - 24x^4 + 36x^2.
\]

Multiplicado por 3:

\[
12x^6 - 72x^4 + 108x^2.
\]

Lado izquierdo:

\[
(3x^4 - 25x^2 + 40)^2.
\]

Sea \(A = 3x^4\), \(B = -25x^2\), \(C = 40\).

\[
= A^2 + B^2 + C^2 + 2AB + 2AC + 2BC.
\]

\[
A^2 = 9x^8, \quad B^2 = 625x^4, \quad C^2 = 1600.
\]

\[
2AB = 2(3x^4)(-25x^2) = -150x^6.
\]

\[
2AC = 2(3x^4)(40) = 240x^4.
\]

\[
2BC = 2(-25x^2)(40) = -2000x^2.
\]

Entonces:

\[
= 9x^8 - 150x^6 + 625x^4 + 240x^4 - 2000x^2 + 1600.
\]

\[
= 9x^8 - 150x^6 + 865x^4 - 2000x^2 + 1600.
\]

Igualando:

\[
9x^8 - 150x^6 + 865x^4 - 2000x^2 + 1600 = 12x^6 - 72x^4 + 108x^2.
\]

\[
9x^8 - 162x^6 + 937x^4 - 2108x^2 + 1600 = 0.
\]

Hagamos \(u = x^2\):

\[
9u^4 - 162u^3 + 937u^2 - 2108u + 1600 = 0.
\]

Esta cuártica en \(u\) puede factorizarse. Probemos si tiene raíces racionales. Las posibles raíces racionales son factores de \(1600/9\).

Probemos \(u = 4\):

\[
9(256) - 162(64) + 937(16) - 2108(4) + 1600.
\]

\[
= 2304 - 10368 + 14992 - 8432 + 1600.
\]

\[
2304 - 10368 = -8064; \quad -8064 + 14992 = 6928; \quad 6928 - 8432 = -1504; \quad -1504 + 1600 = 96 \neq 0.
\]

Probemos \(u = \frac{16}{3}\) (porque antes \(x^2 \approx 2.4323\), que es cercano a \(\frac{16}{3} \cdot \frac{9}{16}\)? No, \(x^2 \approx 2.43\).

Probemos \(u = 2.4323\). Busquemos una fracción. \(2.4323 \approx \frac{73}{30}\)? No.

Probemos raíces racionales de la cuártica en \(u\). Posibles raíces: \(\pm1, \pm2, \pm4, \pm5, \pm8, \pm10, \pm16, \pm20, \pm25, \pm32, \pm40, \pm50, \pm64, \pm80, \pm100, \pm160, \pm200, \pm320, \pm400, \pm800, \pm1600\) y divididas por \(1, 3, 9\).

Probemos \(u = \frac{25}{9} \approx 2.777\):

\[
9\left(\frac{625}{81}\right)^2? 
\]

Esto se complica. Mejor usamos la relación \(y = x^2 - 4\). Si podemos encontrar \(u = x^2\), entonces \(y = u - 4\).

La cuártica en \(u\):

\[
9u^4 - 162u^3 + 937u^2 - 2108u + 1600 = 0.
\]

Intentemos factorizar. Probemos si \((u - 4)\) es factor; no lo es. Probemos \((u - 5)\):

Evaluamos en \(u = 5\):

\[
9(625) - 162(125) + 937(25) - 2108(5) + 1600.
\]

\[
= 5625 - 20250 + 23425 - 10540 + 1600.
\]

\[
5625 - 20250 = -14625; \quad -14625 + 23425 = 8800; \quad 8800 - 10540 = -1740; \quad -1740 + 1600 = -140 \neq 0.
\]

Probemos \(u = \frac{16}{4} = 4\) ya lo hicimos.

Probemos \(u = \frac{50}{9} \approx 5.556\):

\[
9\left(\frac{6250000}{6561}\right) = \frac{6250000}{729} \approx 8573.4,
\]

pero mejor busquemos una factorización inteligente.

Observemos que la cuártica en \(u\) podría factorizarse como:

\[
(3u^2 - 27u + 40)(3u^2 - 27u + 40)?
\]

No. Intentemos con coeficientes enteros:

\[
(au^2 + bu + c)(du^2 + eu + f) = 9u^4 - 162u^3 + 937u^2 - 2108u + 1600.
\]

Con \(ad = 9\), \(cf = 1600\). Probemos \(a = 3, d = 3\). Entonces \(c f = 1600\).

El coeficiente de \(u^3\): \(ae + bd = 3e + 3b = 3(e + b) = -162\), luego \(e + b = -54\).

El coeficiente de \(u^2\): \(af + be + cd = 3f + be + 3c = 937\).

El coeficiente de \(u\): \(bf + ce = -2108\).

Este sistema no es obvio.

Probemos \(a=9, d=1\). Entonces \(cf = 1600\), y:

- \(u^3\): \(e + 9b = -162\).
- \(u^2\): \(f + be + 9c = 937\).
- \(u\): \(bf + ce = -2108\).

Aún más difícil.

Probemos \(a=1, d=9\):

- \(u^3\): \(9e + b = -162\).
- \(u^2\): \(9f + be + c = 937\).
- \(u\): \(bf + ce = -2108\).

También difícil.

Quizá la factorización no sea con enteros.

## 14. Buscar una solución exacta más elegante

Regresemos a la geometría. La parábola original \(y = x^2 - 4\) tiene foco en \((0, -4 + \frac14) = (0, -\frac{15}{4})\) y directriz \(y = -4 - \frac14 = -\frac{17}{4}\). Rotar la parábola rota su foco y su directriz. La imagen tiene foco en la rotación de \((0, -\frac{15}{4})\):

\[
F' = \left(\frac{15\sqrt3}{8},\; -\frac{15}{8}\right).
\]

La intersección de dos parábolas quizá pueda hallarse con las distancias. Un punto \((x, y)\) está en la parábola original si su distancia al foco \((0, -\frac{15}{4})\) es igual a su distancia a la directriz \(y = -\frac{17}{4}\):

\[
x^2 + \left(y + \frac{15}{4}\right)^2 = \left(y + \frac{17}{4}\right)^2.
\]

Esto se simplifica a la ecuación usual \(y = x^2 - 4\). Análogamente, la parábola rotada tiene su propia ecuación de distancia.

Un punto en la intersección cumple ambas. Igualando las dos distancias a los focos implicaría que el punto está en la mediatriz de los dos focos, pero las directrices también intervienen; no es tan simple.

## 15. Volver al sistema en \(t\) y \(s\)

El sistema original:

\[
s = \frac12 t - \frac{\sqrt3}{2}(t^2 - 4), \tag{3}
\]

\[
s^2 - 4 = \frac{\sqrt3}{2}t + \frac12(t^2 - 4). \tag{4}
\]

Sustituimos \(s\) en (4). Esto ya lo hicimos y nos dio la cuártica.

Alternativamente, podemos despejar \(t\) en términos de \(s\) usando la rotación inversa. El punto \((s, s^2 - 4)\) rotado \(60^\circ\) horario da \((t, t^2 - 4)\). La rotación horaria de \((s, s^2-4)\) es:

\[
\left(\frac12 s + \frac{\sqrt3}{2}(s^2 - 4),\; -\frac{\sqrt3}{2}s + \frac12(s^2 - 4)\right) = (t, t^2 - 4).
\]

Entonces:

\[
t = \frac12 s + \frac{\sqrt3}{2}(s^2 - 4), \tag{5}
\]

\[
t^2 - 4 = -\frac{\sqrt3}{2}s + \frac12(s^2 - 4). \tag{6}
\]

Que es simétrico.

## 16. Relación entre \(t\) y \(s\)

¿Hay una relación más directa? La rotación \(60^\circ\) aplicada dos veces es una rotación de \(120^\circ\), y tres veces es \(180^\circ\) (simetría central). Si \((t, t^2-4)\) se rota a \((s, s^2-4)\), entonces al rotar tres veces volvemos al punto original pero con la parábola rotada \(120^\circ\) más.

Quizá sea más fácil derivar la ecuación de la imagen rotada en forma estándar y luego intersectar usando la forma polar o paramétrica.

## 17. Ecuación de la imagen rotada en forma estándar

Una parábola rotada puede escribirse como \((ax + by + c)^2 = d(px + qy + r)\) o similar. Ya tenemos la ecuación (1):

\[
(x + \sqrt3 y)^2 + 2\sqrt3 x - 2y - 16 = 0. \tag{1}
\]

La parábola original:

\[
y - x^2 + 4 = 0.
\]

Tenemos el sistema:

\[
\begin{cases}
y = x^2 - 4, \\
(x + \sqrt3 y)^2 + 2\sqrt3 x - 2y - 16 = 0.
\end{cases}
\]

Sustituimos \(y = x^2 - 4\) en la segunda y obtuvimos la cuártica (2).

## 18. Resolver la cuártica en \(x\) por factorización astuta

Ecuación (2):

\[
3x^4 - 2\sqrt3 x^3 - 25x^2 + 6\sqrt3 x + 40 = 0.
\]

Intentemos completar cuadrados. Observemos que el término \(3x^4\) sugiere \((\sqrt3 x^2)^2\).

Escribamos la ecuación como una cuadrática en la variable \(\sqrt3 x^2\)? No.

Intentemos factorizar (2) como:

\[
(\sqrt3 x^2 + ax + b)(\sqrt3 x^2 + cx + d) = 0.
\]

Entonces el coeficiente de \(x^4\): \(\sqrt3 \cdot \sqrt3 = 3\). Bien.

Coeficiente de \(x^3\): \(\sqrt3 c + a\sqrt3 = \sqrt3(a + c) = -2\sqrt3\), luego \(a + c = -2\).

Coeficiente de \(x^2\): \(\sqrt3 d + ac + b\sqrt3 = -25\).

Coeficiente de \(x\): \(ad + bc = 6\sqrt3\).

Término constante: \(bd = 40\).

Tenemos:

\[
a + c = -2, \quad bd = 40.
\]

Además \(ad + bc = 6\sqrt3\) y \(\sqrt3(b + d) + ac = -25\).

Intentemos \(b\) y \(d\) que hagan todo consistente.

De \(a + c = -2\), sea \(c = -2 - a\).

De \(bd = 40\), \(bd\) es un entero (40). Probemos \(b = 5, d = 8\):

\[
ad + bc = 8a + 5c = 8a + 5(-2 - a) = 8a - 10 - 5a = 3a - 10 = 6\sqrt3.
\]

Entonces \(3a = 10 + 6\sqrt3\), \(a = \frac{10 + 6\sqrt3}{3}\). Esto no es sencillo, y además:

\[
\sqrt3(b + d) + ac = \sqrt3(13) + a(-2 - a).
\]

Con \(a = \frac{10 + 6\sqrt3}{3}\), \(ac = -2a - a^2\). Necesitamos que esto sea \(-25\). Veamos:

\[
\sqrt3 \cdot 13 + (-2a - a^2) = -25.
\]

Es decir, \(a^2 + 2a - 13\sqrt3 - 25 = 0\).

Con \(a = \frac{10 + 6\sqrt3}{3}\), calculamos \(a^2 + 2a\):

\[
a^2 = \frac{(10 + 6\sqrt3)^2}{9} = \frac{100 + 120\sqrt3 + 108}{9} = \frac{208 + 120\sqrt3}{9}.
\]

\[
2a = \frac{20 + 12\sqrt3}{3} = \frac{60 + 36\sqrt3}{9}.
\]

\[
a^2 + 2a = \frac{208 + 120\sqrt3 + 60 + 36\sqrt3}{9} = \frac{268 + 156\sqrt3}{9}.
\]

Entonces \(a^2 + 2a - 13\sqrt3 - 25\):

\[
= \frac{268 + 156\sqrt3}{9} - 13\sqrt3 - 25.
\]

\[
= \frac{268 + 156\sqrt3 - 117\sqrt3 - 225}{9} = \frac{43 + 39\sqrt3}{9} \neq 0.
\]

No funciona.

Probemos \(b = 10, d = 4\):

\[
ad + bc = 4a + 10c = 4a + 10(-2 - a) = 4a - 20 - 10a = -6a - 20 = 6\sqrt3.
\]

Entonces \(-6a = 20 + 6\sqrt3\), \(a = -\frac{10 + 3\sqrt3}{3}\).

Luego:

\[
\sqrt3(b + d) + ac = 14\sqrt3 + a(-2 - a) = 14\sqrt3 - 2a - a^2.
\]

Necesitamos que sea \(-25\):

\[
14\sqrt3 - 2a - a^2 = -25 \implies a^2 + 2a - 14\sqrt3 - 25 = 0.
\]

Con \(a = -\frac{10 + 3\sqrt3}{3}\):

\[
a^2 = \frac{100 + 60\sqrt3 + 27}{9} = \frac{127 + 60\sqrt3}{9}.
\]

\[
2a = -\frac{20 + 6\sqrt3}{3} = -\frac{60 + 18\sqrt3}{9}.
\]

\[
a^2 + 2a = \frac{127 + 60\sqrt3 - 60 - 18\sqrt3}{9} = \frac{67 + 42\sqrt3}{9}.
\]

\[
a^2 + 2a - 14\sqrt3 - 25 = \frac{67 + 42\sqrt3}{9} - 14\sqrt3 - 25.
\]

\[
= \frac{67 + 42\sqrt3 - 126\sqrt3 - 225}{9} = \frac{-158 - 84\sqrt3}{9} \neq 0.
\]

Probemos \(b = 20, d = 2\):

\[
ad + bc = 2a + 20c = 2a + 20(-2 - a) = 2a - 40 - 20a = -18a - 40 = 6\sqrt3.
\]

\[
-18a = 40 + 6\sqrt3 \implies a = -\frac{20 + 3\sqrt3}{9}.
\]

\[
\sqrt3(b+d) + ac = 22\sqrt3 + a(-2 - a) = 22\sqrt3 - 2a - a^2 = -25.
\]

Es decir, \(a^2 + 2a - 22\sqrt3 - 25 = 0\).

Con \(a = -\frac{20+3\sqrt3}{9}\):

\[
a^2 = \frac{400 + 120\sqrt3 + 27}{81} = \frac{427 + 120\sqrt3}{81}.
\]

\[
2a = -\frac{40 + 6\sqrt3}{9} = -\frac{360 + 54\sqrt3}{81}.
\]

\[
a^2 + 2a = \frac{427 + 120\sqrt3 - 360 - 54\sqrt3}{81} = \frac{67 + 66\sqrt3}{81}.
\]

\[
a^2 + 2a - 22\sqrt3 - 25
= \frac{67 + 66\sqrt3}{81} - 22\sqrt3 - 25.
\]

\[
= \frac{67 + 66\sqrt3 - 1782\sqrt3 - 2025}{81}
= \frac{-1958 - 1716\sqrt3}{81} \neq 0.
\]

Probemos \(b = 40, d = 1\):

\[
ad + bc = a + 40c = a + 40(-2-a) = a - 80 - 40a = -39a - 80 = 6\sqrt3.
\]

\[
-39a = 80 + 6\sqrt3 \implies a = -\frac{80 + 6\sqrt3}{39}.
\]

\[
\sqrt3(41) + ac = 41\sqrt3 + a(-2-a) = -25.
\]

Es decir, \(a^2 + 2a - 41\sqrt3 - 25 = 0\).

Con \(a = -\frac{80+6\sqrt3}{39}\):

\[
a^2 = \frac{6400 + 960\sqrt3 + 108}{1521} = \frac{6508 + 960\sqrt3}{1521}.
\]

\[
2a = -\frac{160 + 12\sqrt3}{39} = -\frac{6240 + 468\sqrt3}{1521}.
\]

\[
a^2 + 2a = \frac{6508 + 960\sqrt3 - 6240 - 468\sqrt3}{1521} = \frac{268 + 492\sqrt3}{1521}.
\]

\[
a^2 + 2a - 41\sqrt3 - 25
= \frac{268 + 492\sqrt3}{1521} - 41\sqrt3 - 25.
\]

\[
= \frac{268 + 492\sqrt3 - 62361\sqrt3 - 38025}{1521}
= \frac{-37757 - 61869\sqrt3}{1521} \neq 0.
\]

Probemos \(b = 8, d = 5\):

\[
ad + bc = 5a + 8c = 5a + 8(-2-a) = 5a - 16 - 8a = -3a - 16 = 6\sqrt3.
\]

\[
-3a = 16 + 6\sqrt3 \implies a = -\frac{16 + 6\sqrt3}{3}.
\]

\[
\sqrt3(13) + ac = 13\sqrt3 + a(-2-a) = -25.
\]

Es decir, \(a^2 + 2a - 13\sqrt3 - 25 = 0\).

Con \(a = -\frac{16+6\sqrt3}{3}\):

\[
a^2 = \frac{256 + 192\sqrt3 + 108}{9} = \frac{364 + 192\sqrt3}{9}.
\]

\[
2a = -\frac{32 + 12\sqrt3}{3} = -\frac{96 + 36\sqrt3}{9}.
\]

\[
a^2 + 2a = \frac{364 + 192\sqrt3 - 96 - 36\sqrt3}{9} = \frac{268 + 156\sqrt3}{9}.
\]

\[
a^2 + 2a - 13\sqrt3 - 25 = \frac{268 + 156\sqrt3 - 117\sqrt3 - 225}{9} = \frac{43 + 39\sqrt3}{9} \neq 0.
\]

Igual que antes.

¿Hay alguna opción con \(b\), \(d\) irracionales? El producto \(bd = 40\) sugiere que quizá \(b\) y \(d\) sean de la forma \(k\sqrt3\) y \(\frac{40}{k\sqrt3}\).

No avanza con esta factorización. Tal vez la factorización correcta no requiera que los factores tengan la forma \(\sqrt3 x^2 + px + q\) con productos tan simples.

## 19. Otra estrategia: resolver para \(y\) directamente

En lugar de \(x\), resolvamos para \(y\). De \(y = x^2 - 4\), tenemos \(x^2 = y + 4\). Para el punto en el cuarto cuadrante, \(x > 0\), así que \(x = \sqrt{y + 4}\).

Sustituimos en la ecuación (1):

\[
(x + \sqrt3 y)^2 + 2\sqrt3 x - 2y - 16 = 0.
\]

\[
x + \sqrt3 y = \sqrt{y+4} + \sqrt3 y.
\]

Elevado al cuadrado:

\[
(\sqrt{y+4} + \sqrt3 y)^2 = (y+4) + 2\sqrt3 y \sqrt{y+4} + 3y^2.
\]

Entonces la ecuación queda:

\[
(y+4) + 2\sqrt3 y \sqrt{y+4} + 3y^2 + 2\sqrt3\sqrt{y+4} - 2y - 16 = 0.
\]

Simplificando:

\[
3y^2 - y - 12 + 2\sqrt3 \sqrt{y+4}\,(y + 1) = 0.
\]

Es decir:

\[
3y^2 - y - 12 = -2\sqrt3 \sqrt{y+4}\,(y+1).
\]

Elevamos al cuadrado:

\[
(3y^2 - y - 12)^2 = 12 (y+4)(y+1)^2.
\]

Esta es una cuártica en \(y\), quizá más simple.

Desarrollemos.

Lado izquierdo:

\[
(3y^2 - y - 12)^2.
\]

\[
= 9y^4 - 6y^3 - 72y^2 + y^2 + 24y + 144 \quad ?
\]

Desarrollemos con cuidado:

\[
(3y^2 - y - 12)^2 = (3y^2)^2 + (-y)^2 + (-12)^2 + 2(3y^2)(-y) + 2(3y^2)(-12) + 2(-y)(-12).
\]

\[
= 9y^4 + y^2 + 144 - 6y^3 - 72y^2 + 24y.
\]

\[
= 9y^4 - 6y^3 - 71y^2 + 24y + 144.
\]

Lado derecho:

\[
12(y+4)(y+1)^2 = 12(y+4)(y^2 + 2y + 1).
\]

\[
(y+4)(y^2 + 2y + 1) = y^3 + 2y^2 + y + 4y^2 + 8y + 4 = y^3 + 6y^2 + 9y + 4.
\]

Multiplicado por 12:

\[
12y^3 + 72y^2 + 108y + 48.
\]

Igualando:

\[
9y^4 - 6y^3 - 71y^2 + 24y + 144 = 12y^3 + 72y^2 + 108y + 48.
\]

\[
9y^4 - 18y^3 - 143y^2 - 84y + 96 = 0.
\]

Esta es la cuártica en \(y\):

\[
9y^4 - 18y^3 - 143y^2 - 84y + 96 = 0. \tag{7}
\]

## 20. Factorización de la cuártica en \(y\)

Intentemos factorizar (7) como producto de dos cuadráticos con coeficientes enteros:

\[
(ay^2 + by + c)(dy^2 + ey + f) = 0.
\]

Con \(ad = 9\), \(cf = 96\).

Probemos \(a=3, d=3\). Entonces \(cf = 96\).

Coeficiente de \(y^3\): \(ae + bd = 3e + 3b = 3(e+b) = -18\), luego \(e+b = -6\).

Coeficiente de \(y^2\): \(af + be + cd = 3f + be + 3c = -143\).

Coeficiente de \(y\): \(bf + ce = -84\).

Probemos combinaciones. \(c\) y \(f\) son factores de 96. Opciones: (1,96), (2,48), (3,32), (4,24), (6,16), (8,12), y con signos.

Probemos \(c = 12, f = 8\). Entonces:

\[
3f + be + 3c = 24 + be + 36 = 60 + be = -143 \implies be = -203.
\]

\[
bf + ce = 8b + 12e = -84.
\]

Además \(e+b = -6\), luego \(e = -6 - b\).

Sustituimos \(e\):

\[
8b + 12(-6 - b) = -84.
\]

\[
8b - 72 - 12b = -84 \implies -4b = -12 \implies b = 3.
\]

Entonces \(e = -6 - 3 = -9\).

Verificamos \(be = 3(-9) = -27 \neq -203\). No funciona.

Probemos \(c = 8, f = 12\):

\[
3f + be + 3c = 36 + be + 24 = 60 + be = -143 \implies be = -203.
\]

\[
bf + ce = 12b + 8e = -84.
\]

Con \(e = -6 - b\):

\[
12b + 8(-6-b) = 12b - 48 - 8b = 4b - 48 = -84 \implies 4b = -36 \implies b = -9.
\]

Entonces \(e = -6 - (-9) = 3\).

\(be = (-9)(3) = -27 \neq -203\). No.

Probemos \(c=16, f=6\):

\[
3f + be + 3c = 18 + be + 48 = 66 + be = -143 \implies be = -209.
\]

\[
bf + ce = 6b + 16e = -84.
\]

Con \(e = -6-b\):

\[
6b + 16(-6-b) = 6b - 96 - 16b = -10b - 96 = -84 \implies -10b = 12 \implies b = -1.2.
\]

No entero, descartado.

Probemos \(c=6, f=16\):

\[
3f + be + 3c = 48 + be + 18 = 66 + be = -143 \implies be = -209.
\]

\[
bf + ce = 16b + 6e = -84.
\]

Con \(e = -6-b\):

\[
16b + 6(-6-b) = 16b - 36 - 6b = 10b - 36 = -84 \implies 10b = -48 \implies b = -4.8.
\]

No entero.

Probemos \(c=24, f=4\):

\[
3f + be + 3c = 12 + be + 72 = 84 + be = -143 \implies be = -227.
\]

\[
bf + ce = 4b + 24e = -84.
\]

Con \(e=-6-b\):

\[
4b + 24(-6-b) = 4b - 144 - 24b = -20b - 144 = -84 \implies -20b = 60 \implies b = -3.
\]

Entonces \(e = -6 - (-3) = -3\).

\(be = (-3)(-3) = 9 \neq -227\). No.

Probemos \(c=4, f=24\):

\[
3f + be + 3c = 72 + be + 12 = 84 + be = -143 \implies be = -227.
\]

\[
bf + ce = 24b + 4e = -84.
\]

Con \(e=-6-b\):

\[
24b + 4(-6-b) = 24b - 24 - 4b = 20b - 24 = -84 \implies 20b = -60 \implies b=-3.
\]

Entonces \(e = -6 - (-3) = -3\).

\(be = 9 \neq -227\). No.

Probemos \(c=32, f=3\):

\[
3f + be + 3c = 9 + be + 96 = 105 + be = -143 \implies be = -248.
\]

\[
bf + ce = 3b + 32e = -84.
\]

Con \(e=-6-b\):

\[
3b + 32(-6-b) = 3b - 192 - 32b = -29b - 192 = -84 \implies -29b = 108 \implies b = -108/29.
\]

No entero.

Probemos \(c=3, f=32\):

\[
3f + be + 3c = 96 + be + 9 = 105 + be = -143 \implies be = -248.
\]

\[
bf + ce = 32b + 3e = -84.
\]

Con \(e=-6-b\):

\[
32b + 3(-6-b) = 32b - 18 - 3b = 29b - 18 = -84 \implies 29b = -66 \implies b = -66/29.
\]

No entero.

Probemos con \(a=9, d=1\):

\[
ad = 9. 
\]

Coeficiente de \(y^3\): \(e + 9b = -18\).

Coeficiente de \(y^2\): \(f + be + 9c = -143\).

Coeficiente de \(y\): \(bf + ce = -84\).

\(cf = 96\).

Probemos \(c=12, f=8\) (con \(a=9, d=1\)):

\[
e = -18 - 9b.
\]

\[
bf + ce = 8b + 12e = -84.
\]

\[
8b + 12(-18 - 9b) = 8b - 216 - 108b = -100b - 216 = -84.
\]

\[
-100b = 132 \implies b = -1.32.
\]

No entero.

Probemos \(c=8, f=12\):

\[
e = -18 - 9b.
\]

\[
12b + 8e = 12b + 8(-18-9b) = 12b -144 -72b = -60b -144 = -84.
\]

\[
-60b = 60 \implies b = -1.
\]

Entonces \(e = -18 - 9(-1) = -9\).

Verificamos \(y^2\): \(f + be + 9c = 12 + (-1)(-9) + 72 = 12 + 9 + 72 = 93 \neq -143\).

No.

Probemos \(c=16, f=6\):

\[
e = -18 - 9b.
\]

\[
6b + 16e = 6b + 16(-18-9b) = 6b -288 -144b = -138b -288 = -84.
\]

\[
-138b = 204 \implies b = -204/138 = -34/23.
\]

No entero.

Probemos \(c=6, f=16\):

\[
e = -18 - 9b.
\]

\[
16b + 6e = 16b + 6(-18-9b) = 16b -108 -54b = -38b -108 = -84.
\]

\[
-38b = 24 \implies b = -24/38 = -12/19.
\]

No entero.

Probemos \(c=24, f=4\):

\[
e = -18 - 9b.
\]

\[
4b + 24e = 4b + 24(-18-9b) = 4b -432 -216b = -212b -432 = -84.
\]

\[
-212b = 348 \implies b = -348/212 = -87/53.
\]

No entero.

Probemos \(c=4, f=24\):

\[
e = -18 - 9b.
\]

\[
24b + 4e = 24b + 4(-18-9b) = 24b -72 -36b = -12b -72 = -84.
\]

\[
-12b = -12 \implies b = 1.
\]

Entonces \(e = -18 - 9 = -27\).

Verificamos \(y^2\): \(f + be + 9c = 24 + 1(-27) + 36 = 24 - 27 + 36 = 33 \neq -143\).

No.

Probemos \(c=32, f=3\):

\[
e = -18-9b.
\]

\[
3b + 32e = 3b + 32(-18-9b) = 3b -576 -288b = -285b -576 = -84.
\]

\[
-285b = 492 \implies b = -492/285.
\]

No.

Probemos \(c=3, f=32\):

\[
e = -18-9b.
\]

\[
32b + 3e = 32b + 3(-18-9b) = 32b -54 -27b = 5b -54 = -84.
\]

\[
5b = -30 \implies b = -6.
\]

Entonces \(e = -18 - 9(-6) = -18 + 54 = 36\).

Verificamos \(y^2\): \(f + be + 9c = 32 + (-6)(36) + 27 = 32 - 216 + 27 = -157 \neq -143\).

No.

Probemos \(c=48, f=2\):

\[
e = -18-9b.
\]

\[
2b + 48e = 2b + 48(-18-9b) = 2b -864 -432b = -430b -864 = -84.
\]

\[
-430b = 780 \implies b = -780/430 = -78/43.
\]

No.

Probemos \(c=2, f=48\):

\[
e = -18-9b.
\]

\[
48b + 2e = 48b + 2(-18-9b) = 48b -36 -18b = 30b -36 = -84.
\]

\[
30b = -48 \implies b = -8/5.
\]

No entero.

Probemos \(c=96, f=1\):

\[
e = -18-9b.
\]

\[
b + 96e = b + 96(-18-9b) = b -1728 -864b = -863b -1728 = -84.
\]

\[
-863b = 1644 \implies b = -1644/863.
\]

No.

Probemos \(c=1, f=96\):

\[
e = -18-9b.
\]

\[
96b + e = 96b -18 -9b = 87b -18 = -84.
\]

\[
87b = -66 \implies b = -66/87 = -22/29.
\]

No.

Ninguna factorización con enteros. Intentemos con coeficientes que involucren \(\sqrt3\) o simplemente aceptar que las raíces son irracionales.

## 21. Factorizar la cuártica en \(y\) con raíz cuadrada

La cuártica (7):

\[
9y^4 - 18y^3 - 143y^2 - 84y + 96 = 0.
\]

Probemos factorizarla como \((3y^2 + py + q)(3y^2 + ry + s)\).

Con \(qs = 96\), y \(p+r = -6\) (porque \(3r + 3p = -18\)).

Probemos \(q = 16, s = 6\):

\[
p + r = -6.
\]

Coeficiente de \(y^2\): \(3s + pr + 3q = 18 + pr + 48 = 66 + pr = -143 \implies pr = -209.\)

Coeficiente de \(y\): \(ps + qr = 6p + 16r = -84.\)

Sistema:

\[
p + r = -6, \quad pr = -209, \quad 6p + 16r = -84.
\]

De \(p+r=-6\), \(r = -6-p\). Entonces \(pr = p(-6-p) = -6p - p^2 = -209\), luego \(p^2 + 6p - 209 = 0\).

Resolvemos:

\[
p = \frac{-6 \pm \sqrt{36 + 836}}{2} = \frac{-6 \pm \sqrt{872}}{2} = \frac{-6 \pm 2\sqrt{218}}{2} = -3 \pm \sqrt{218}.
\]

Entonces \(p = -3 + \sqrt{218}\) o \(p = -3 - \sqrt{218}\).

Verificamos \(6p + 16r = -84\):

\[
6p + 16(-6-p) = 6p -96 -16p = -10p -96.
\]

Debe ser \(-84\), luego \(-10p = 12\), \(p = -1.2\). Pero \(p = -3 \pm \sqrt{218} \approx -3 \pm 14.765\), es decir \(p \approx 11.765\) o \(p \approx -17.765\). Ninguno es \(-1.2\). No funciona.

Probemos \(q=6, s=16\):

\[
9y^4 -18y^3 + (3s + pr + 3q)y^2 + (ps + qr)y + 96.
\]

\[
3s + 3q = 48 + 18 = 66. 
\]

\[
66 + pr = -143 \implies pr = -209.
\]

Coeficiente de \(y\): \(ps + qr = 16p + 6r = -84\).

Con \(r=-6-p\):

\[
16p + 6(-6-p) = 16p -36 -6p = 10p -36 = -84 \implies 10p = -48 \implies p = -4.8.
\]

Pero \(p+r=-6\) y \(pr=-209\) da \(p = -3 \pm \sqrt{218}\), no coincide.

Probemos \(q=12, s=8\):

\[
3s + 3q = 24 + 36 = 60.
\]

\[
60 + pr = -143 \implies pr = -203.
\]

Coeficiente de \(y\): \(8p + 12r = -84\).

Con \(r=-6-p\):

\[
8p + 12(-6-p) = 8p -72 -12p = -4p -72 = -84 \implies -4p = -12 \implies p = 3.
\]

Entonces \(r = -9\).

Pero \(pr = 3(-9) = -27 \neq -203\). No.

Probemos \(q=8, s=12\):

\[
3s+3q = 36+24 = 60.
\]

\[
60+pr = -143 \implies pr=-203.
\]

Coeficiente de \(y\): \(12p + 8r = -84\).

Con \(r=-6-p\):

\[
12p + 8(-6-p) = 12p -48 -8p = 4p -48 = -84 \implies 4p = -36 \implies p = -9.
\]

Entonces \(r = 3\).

\(pr = -27 \neq -203\). No.

Probemos \(q=24, s=4\):

\[
3s+3q = 12+72 = 84.
\]

\[
84+pr=-143 \implies pr=-227.
\]

Coeficiente de \(y\): \(4p + 24r = -84\).

Con \(r=-6-p\):

\[
4p + 24(-6-p) = 4p -144 -24p = -20p -144 = -84 \implies -20p = 60 \implies p=-3.
\]

Entonces \(r=-3\).

\(pr = 9 \neq -227\). No.

Probemos \(q=4, s=24\):

\[
3s+3q = 72+12=84.
\]

\[
84+pr=-143 \implies pr=-227.
\]

Coeficiente de \(y\): \(24p+4r=-84\).

Con \(r=-6-p\):

\[
24p+4(-6-p) = 24p -24 -4p = 20p -24 = -84 \implies 20p = -60 \implies p=-3.
\]

Entonces \(r=-3\).

\(pr=9\neq-227\). No.

Probemos \(q=48, s=2\):

\[
3s+3q = 6+144=150.
\]

\[
150+pr=-143 \implies pr=-293.
\]

Coeficiente de \(y\): \(2p+48r=-84\).

Con \(r=-6-p\):

\[
2p+48(-6-p) = 2p -288 -48p = -46p -288 = -84 \implies -46p = 204 \implies p = -204/46 = -102/23.
\]

Pero \(p+r=-6\) y \(pr=-293\) no da \(p=-102/23\)? Verifiquemos: \(p\) debe cumplir \(p^2+6p-293=0\), \(p = -3 \pm \sqrt{302}\)? \(\sqrt{36 + 4\cdot293} =\sqrt{36+1172} = \sqrt{1208}\). No coincide.

Probemos \(q=2, s=48\):

\[
3s+3q=144+6=150.
\]

\[
150+pr=-143 \implies pr=-293.
\]

Coeficiente de \(y\): \(48p+2r=-84\).

Con \(r=-6-p\):

\[
48p+2(-6-p) = 48p -12 -2p = 46p -12 = -84 \implies 46p = -72 \implies p = -72/46=-36/23.
\]

No coincide.

Probemos \(q=32, s=3\):

\[
3s+3q=9+96=105.
\]

\[
105+pr=-143 \implies pr=-248.
\]

Coeficiente de \(y\): \(3p+32r=-84\).

Con \(r=-6-p\):

\[
3p+32(-6-p) = 3p -192 -32p = -29p -192 = -84 \implies -29p=108 \implies p=-108/29.
\]

No coincide con \(p^2+6p-248=0\).

Probemos \(q=3, s=32\):

\[
3s+3q=96+9=105.
\]

\[
105+pr=-143 \implies pr=-248.
\]

Coeficiente de \(y\): \(32p+3r=-84\).

Con \(r=-6-p\):

\[
32p+3(-6-p) = 32p -18 -3p = 29p -18 = -84 \implies 29p = -66 \implies p=-66/29.
\]

No.

Probemos \(q=96, s=1\):

\[
3s+3q=3+288=291.
\]

\[
291+pr=-143 \implies pr=-434.
\]

Coeficiente de \(y\): \(p+96r=-84\).

Con \(r=-6-p\):

\[
p+96(-6-p) = p -576 -96p = -95p -576 = -84 \implies -95p = 492 \implies p = -492/95.
\]

No.

Probemos \(q=1, s=96\):

\[
3s+3q=288+3=291.
\]

\[
291+pr=-143 \implies pr=-434.
\]

Coeficiente de \(y\): \(96p+r=-84\).

Con \(r=-6-p\):

\[
96p -6 -p = 95p -6 = -84 \implies 95p = -78 \implies p=-78/95.
\]

No.

Quizá \(q\) y \(s\) no son ambos enteros positivos, o la factorización en dos cuadráticos con coeficientes enteros no existe.

## 22. Raíces de la cuártica en \(y\)

La cuártica (7) se obtuvo elevando al cuadrado, por lo que puede incluir soluciones extrañas. Pero la solución para \(y\) en el cuarto cuadrante es una de sus raíces.

Podemos hallar las raíces de (7) numéricamente o factorizarla usando la forma \((ay^2+by+c)^2 - (ey+f)^2 = 0\) (diferencia de cuadrados) si es posible.

Intentemos expresar (7) como \((3y^2 - 3y - 8)^2 - (ky + m)^2 = 0\).

Desarrollemos \((3y^2 - 3y - 8)^2\):

\[
(3y^2)^2 + (-3y)^2 + (-8)^2 + 2(3y^2)(-3y) + 2(3y^2)(-8) + 2(-3y)(-8).
\]

\[
= 9y^4 + 9y^2 + 64 - 18y^3 - 48y^2 + 48y.
\]

\[
= 9y^4 - 18y^3 - 39y^2 + 48y + 64.
\]

Nuestra cuártica es \(9y^4 - 18y^3 - 143y^2 - 84y + 96\).

Restamos:

\[
(9y^4 - 18y^3 - 143y^2 - 84y + 96) - (9y^4 - 18y^3 - 39y^2 + 48y + 64)
= -104y^2 - 132y + 32.
\]

Queremos que la diferencia sea de la forma \(-(ky+m)^2\) o \(+(ky+m)^2\). Tenemos \(-104y^2 -132y +32\), que no es un cuadrado perfecto con signo uniforme.

Probemos otra forma: \((3y^2 - 3y - \alpha)^2\). Busquemos un \(\alpha\) que haga que la diferencia sea un cuadrado perfecto (por diferencia de cuadrados).

Sea \(C(y) = 9y^4 - 18y^3 - 143y^2 - 84y + 96\).

Probemos \((3y^2 - 3y - \lambda)^2\):

\[
= 9y^4 - 18y^3 + (9 - 6\lambda)y^2 + 6\lambda y + \lambda^2.
\]

Entonces la diferencia \(C(y) - (3y^2 - 3y - \lambda)^2\) es:

Coeficiente de \(y^2\): \(-143 - (9 - 6\lambda) = -152 + 6\lambda\).

Coeficiente de \(y\): \(-84 - 6\lambda\).

Coeficiente independiente: \(96 - \lambda^2\).

Queremos que esta diferencia sea de la forma \((ky+m)^2\) o \(-(ky+m)^2\). Para que sea un cuadrado, el coeficiente de \(y^2\) y el coeficiente independiente deben tener el mismo signo (si es \((ky+m)^2\)) o ambos negativos (si es \(-(ky+m)^2\)).

Además, si la diferencia es \((ky+m)^2\), entonces el discriminante de la cuadrática debe ser cero, es decir, \(m^2 = (coef. indep.)\) y \(k^2 = (coef. y^2)\), con \(2km = coef. y\).

Imponemos que la diferencia sea un cuadrado perfecto. Entonces:

\[
(coef.\ y)^2 = 4 (coef.\ y^2)(coef.\ indep).
\]

Es decir:

\[
(-84 - 6\lambda)^2 = 4(-152 + 6\lambda)(96 - \lambda^2).
\]

Desarrollemos.

Lado izquierdo:

\[
(-84 - 6\lambda)^2 = (84 + 6\lambda)^2 = 7056 + 1008\lambda + 36\lambda^2.
\]

Lado derecho:

\[
4(-152 + 6\lambda)(96 - \lambda^2) = (-608 + 24\lambda)(96 - \lambda^2).
\]

\[
= -608 \cdot 96 + 608\lambda^2 + 24\lambda\cdot 96 - 24\lambda^3.
\]

\[
= -58368 + 608\lambda^2 + 2304\lambda - 24\lambda^3.
\]

Igualando:

\[
7056 + 1008\lambda + 36\lambda^2 = -58368 + 2304\lambda + 608\lambda^2 - 24\lambda^3.
\]

\[
0 = -58368 - 7056 + 2304\lambda - 1008\lambda + 608\lambda^2 - 36\lambda^2 - 24\lambda^3 + ? 
\]

Espera, movamos todo a la derecha:

\[
0 = -58368 + 2304\lambda + 608\lambda^2 - 24\lambda^3 - 7056 - 1008\lambda - 36\lambda^2.
\]

\[
0 = -65424 + 1296\lambda + 572\lambda^2 - 24\lambda^3.
\]

Dividimos entre \(-4\):

\[
0 = 16356 - 324\lambda - 143\lambda^2 + 6\lambda^3.
\]

O bien:

\[
6\lambda^3 - 143\lambda^2 - 324\lambda + 16356 = 0. \tag{8}
\]

Buscamos raíces enteras de (8). Posibles raíces: factores de 16356 divididos por factores de 6.

Factores de 16356: \(16356 = 4 \cdot 4089 = 4 \cdot 3 \cdot 1363 = 4 \cdot 3 \cdot 29 \cdot 47\)? Verifiquemos: \(1363 = 29 \cdot 47\)? \(29 \cdot 47 = 1363\). Sí.

Entonces \(16356 = 4 \cdot 3 \cdot 29 \cdot 47\).

Probemos \(\lambda = 6\):

\[
6(216) - 143(36) - 324(6) + 16356 = 1296 - 5148 - 1944 + 16356.
\]

\[
1296 - 5148 = -3852; \quad -3852 - 1944 = -5796; \quad -5796 + 16356 = 10560 \neq 0.
\]

Probemos \(\lambda = 12\):

\[
6(1728) - 143(144) - 324(12) + 16356 = 10368 - 20592 - 3888 + 16356.
\]

\[
10368 - 20592 = -10224; \quad -10224 - 3888 = -14112; \quad -14112 + 16356 = 2244 \neq 0.
\]

Probemos \(\lambda = 24\):

\[
6(13824) - 143(576) - 324(24) + 16356.
\]

\[
= 82944 - 82368 - 7776 + 16356.
\]

\[
82944 - 82368 = 576; \quad 576 - 7776 = -7200; \quad -7200 + 16356 = 9156 \neq 0.
\]

Probemos \(\lambda = 18\):

\[
6(5832) - 143(324) - 324(18) + 16356.
\]

\[
= 34992 - 46332 - 5832 + 16356.
\]

\[
34992 - 46332 = -11340; \quad -11340 - 5832 = -17172; \quad -17172 + 16356 = -816 \neq 0.
\]

Probemos \(\lambda = 36\):

\[
6(46656) - 143(1296) - 324(36) + 16356.
\]

\[
= 279936 - 185328 - 11664 + 16356.
\]

\[
279936 - 185328 = 94608; \quad 94608 - 11664 = 82944; \quad +16356 = 99300 \neq 0.
\]

Probemos \(\lambda = 4\):

\[
6(64) - 143(16) - 324(4) + 16356 = 384 - 2288 - 1296 + 16356.
\]

\[
384 - 2288 = -1904; \quad -1904 - 1296 = -3200; \quad +16356 = 13156 \neq 0.
\]

Probemos \(\lambda = 3\):

\[
6(27) - 143(9) - 324(3) + 16356 = 162 - 1287 - 972 + 16356.
\]

\[
162 - 1287 = -1125; \quad -1125 - 972 = -2097; \quad +16356 = 14259 \neq 0.
\]

Probemos \(\lambda = 2\):

\[
6(8) - 143(4) - 324(2) + 16356 = 48 - 572 - 648 + 16356.
\]

\[
48 - 572 = -524; \quad -524 - 648 = -1172; \quad +16356 = 15184 \neq 0.
\]

Probemos \(\lambda = 1\):

\[
6 - 143 - 324 + 16356 = 15895 \neq 0.
\]

Probemos \(\lambda = 8\):

\[
6(512) - 143(64) - 324(8) + 16356 = 3072 - 9152 - 2592 + 16356.
\]

\[
3072 - 9152 = -6080; \quad -6080 - 2592 = -8672; \quad +16356 = 7684 \neq 0.
\]

Probemos \(\lambda = 9\):

\[
6(729) - 143(81) - 324(9) + 16356 = 4374 - 11583 - 2916 + 16356.
\]

\[
4374 - 11583 = -7209; \quad -7209 - 2916 = -10125; \quad +16356 = 6231 \neq 0.
\]

Probemos \(\lambda = 16\):

\[
6(4096) - 143(256) - 324(16) + 16356 = 24576 - 36608 - 5184 + 16356.
\]

\[
24576 - 36608 = -12032; \quad -12032 - 5184 = -17216; \quad +16356 = -860 \neq 0.
\]

Probemos \(\lambda = 27\):

\[
6(19683) - 143(729) - 324(27) + 16356.
\]

\[
= 118098 - 104247 - 8748 + 16356.
\]

\[
118098 - 104247 = 13851; \quad 13851 - 8748 = 5103; \quad +16356 = 21459 \neq 0.
\]

Probemos \(\lambda = -6\):

\[
6(-216) - 143(36) - 324(-6) + 16356 = -1296 - 5148 + 1944 + 16356.
\]

\[
-1296 - 5148 = -6444; \quad +1944 = -4500; \quad +16356 = 11856 \neq 0.
\]

Probemos \(\lambda = -4\):

\[
6(-64) - 143(16) - 324(-4) + 16356 = -384 - 2288 + 1296 + 16356.
\]

\[
-384 - 2288 = -2672; \quad +1296 = -1376; \quad +16356 = 14980.
\]

Probemos \(\lambda = -3\):

\[
6(-27) - 143(9) + 972 + 16356 = -162 - 1287 + 972 + 16356.
\]

\[
-162 -1287 = -1449; \quad +972 = -477; \quad +16356 = 15879.
\]

Probemos \(\lambda = -2\):

\[
-48 -572 +648 +16356 = 16384.
\]

¡Interesante! \(\lambda = -2\) da \(16384 = 128^2\), pero no, evaluamos la cúbica (8), no su cuadrado. Rehagamos:

\[
6(-8) - 143(4) - 324(-2) + 16356 = -48 - 572 + 648 + 16356.
\]

\[
-48 -572 = -620; \quad +648 = 28; \quad +16356 = 16384 \neq 0.
\]

No.

Probemos \(\lambda = -8\):

\[
6(-512) - 143(64) + 324(8) + 16356 = -3072 - 9152 + 2592 + 16356.
\]

\[
-3072 - 9152 = -12224; \quad +2592 = -9632; \quad +16356 = 6724 \neq 0.
\]

Probemos \(\lambda = -12\):

\[
6(-1728) - 143(144) + 324(12) + 16356.
\]

\[
= -10368 - 20592 + 3888 + 16356.
\]

\[
-10368 -20592 = -30960; \quad +3888 = -27072; \quad +16356 = -10716 \neq 0.
\]

Probemos \(\lambda = -9\):

\[
6(-729) - 143(81) + 324(9) + 16356 = -4374 - 11583 + 2916 + 16356.
\]

\[
-4374 -11583 = -15957; \quad +2916 = -13041; \quad +16356 = 3315 \neq 0.
\]

Probemos \(\lambda = -18\):

\[
6(-5832) - 143(324) + 324(18) + 16356.
\]

\[
= -34992 - 46332 + 5832 + 16356.
\]

\[
-34992 -46332 = -81324; \quad +5832 = -75492; \quad +16356 = -59136 \neq 0.
\]

Probemos \(\lambda = -24\):

\[
6(-13824) - 143(576) + 324(24) + 16356.
\]

\[
= -82944 - 82368 + 7776 + 16356.
\]

\[
-82944 -82368 = -165312; \quad +7776 = -157536; \quad +16356 = -141180 \neq 0.
\]

Probemos \(\lambda = -36\):

\[
6(-46656) - 143(1296) + 324(36) + 16356.
\]

\[
= -279936 - 185328 + 11664 + 16356.
\]

\[
-279936 -185328 = -465264; \quad +11664 = -453600; \quad +16356 = -437244 \neq 0.
\]

Probemos \(\lambda = -16\):

\[
6(-4096) - 143(256) + 324(16) + 16356.
\]

\[
= -24576 - 36608 + 5184 + 16356.
\]

\[
-24576 -36608 = -61184; \quad +5184 = -56000; \quad +16356 = -39644 \neq 0.
\]

Probemos \(\lambda = -27\):

\[
6(-19683) - 143(729) + 324(27) + 16356.
\]

\[
= -118098 - 104247 + 8748 + 16356.
\]

\[
-118098 -104247 = -222345; \quad +8748 = -213597; \quad +16356 = -197241 \neq 0.
\]

Probemos \(\lambda = -48\):

\[
6(-110592) - 143(2304) + 324(48) + 16356.
\]

\[
= -663552 - 329472 + 15552 + 16356.
\]

No es cero.

Probemos \(\lambda = 29\) (ya que 29 es factor de 16356):

\[
6(24389) - 143(841) - 324(29) + 16356.
\]

\[
= 146334 - 120263 - 9396 + 16356.
\]

\[
146334 - 120263 = 26071; \quad -9396 = 16675; \quad +16356 = 33031 \neq 0.
\]

Probemos \(\lambda = 47\):

\[
6(103823) - 143(2209) - 324(47) + 16356.
\]

\[
= 622938 - 315887 - 15228 + 16356.
\]

\[
622938 -315887 = 307051; \quad -15228 = 291823; \quad +16356 = 308179 \neq 0.
\]

Probemos \(\lambda = 58\) (\(2\cdot29\)):

\[
6(195112) - 143(3364) - 324(58) + 16356.
\]

\[
= 1170672 - 481052 - 18792 + 16356.
\]

\[
1170672 -481052 = 689620; \quad -18792 = 670828; \quad +16356 = 687184 \neq 0.
\]

Probemos \(\lambda = 94\) (\(2\cdot47\)):

\[
6(830584) - 143(8836) - 324(94) + 16356.
\]

\[
= 4983504 - 1263548 - 30456 + 16356.
\]

\[
4983504 -1263548 = 3719956; \quad -30456 = 3689500; \quad +16356 = 3705856 \neq 0.
\]

Probemos \(\lambda = 87\) (\(3\cdot29\)):

\[
6(658503) - 143(7569) - 324(87) + 16356.
\]

\[
= 3951018 - 1082367 - 28188 + 16356.
\]

\[
3951018 -1082367 = 2868651; \quad -28188 = 2840463; \quad +16356 = 2856819 \neq 0.
\]

Probemos \(\lambda = 141\) (\(3\cdot47\)):

\[
6(2803221) - 143(19881) - 324(141) + 16356.
\]

\[
= 16819326 - 2842983 - 45684 + 16356.
\]

No.

Probemos \(\lambda = 116\) (\(4\cdot29\)):

\[
6(1561152) - 143(13456) - 324(116) + 16356.
\]

No.

Probemos \(\lambda = 188\) (\(4\cdot47\)):

\[
6(6644672) - 143(35344) - 324(188) + 16356.
\]

No.

Probemos \(\lambda = 1363\):

\[
6\cdot 1363^3 - 143\cdot 1363^2 - 324\cdot 1363 + 16356.
\]

Obviamente no es cero por magnitud.

Probemos \(\lambda = 1363/6\) o fracciones. No.

Tal vez la raíz de (8) no es entera. Entonces la técnica de completar cuadrado con \(\lambda\) entero no aplica directamente; podríamos resolver (8) numéricamente y luego construir la factorización.

## 23. Resolver la cuártica en \(y\) directamente por fórmula o numéricamente

Mejor usemos un enfoque distinto: resolver el sistema original simbólicamente o aproximar mejor.

Ya sabíamos que la raíz en el cuarto cuadrante tiene \(x \approx 1.5597\), \(y = x^2 - 4 \approx -1.5677\).

La cuártica en \(y\) es:

\[
C(y) = 9y^4 - 18y^3 - 143y^2 - 84y + 96.
\]

Evaluemos \(C(-1.5677)\) para confirmar.

Hagámoslo de manera más sistemática. Encontremos la raíz de \(C(y)\) cerca de \(-1.5677\).

Sea \(y_0 \approx -1.5677\).

Usemos Newton o bisección.

Evaluemos \(C(-1.6)\):

\[
y = -1.6, \quad y^2 = 2.56, \quad y^3 = -4.096, \quad y^4 = 6.5536.
\]

\[
9y^4 = 58.9824, \quad -18y^3 = 73.728, \quad -143y^2 = -366.08, \quad -84y = 134.4, \quad +96.
\]

Suma:

\[
58.9824 + 73.728 - 366.08 + 134.4 + 96.
\]

\[
58.9824 + 73.728 = 132.7104; \quad -366.08 = -233.3696; \quad +134.4 = -98.9696; \quad +96 = -2.9696.
\]

Evaluemos \(C(-1.55)\):

\[
y^2 = 2.4025, \quad y^3 = -3.723875, \quad y^4 = 5.77150625? 
\]

Calculemos \(y^3 = (-1.55)^3 = -3.723875\), \(y^4 = (-1.55)^4 = 5.77200625\).

\[
9y^4 = 51.94805625, \quad -18y^3 = 67.02975, \quad -143y^2 = -343.5575, \quad -84y = 130.2, \quad +96.
\]

Suma:

\[
51.94805625 + 67.02975 = 118.97780625; \quad -343.5575 = -224.57969375; \quad +130.2 = -94.37969375; \quad +96 = 1.62030625.
\]

Entonces hay una raíz entre \(-1.6\) y \(-1.55\) para \(C(y)\).

Probemos \(y = -1.575\):

\[
y^2 = 2.480625, \quad y^3 = -3.906984375, \quad y^4 = 6.153500390625.
\]

\[
9y^4 = 55.381503515625, \quad -18y^3 = 70.32571875, \quad -143y^2 = -354.729375, \quad -84y = 132.3, \quad +96.
\]

Suma:

\[
55.3815035 + 70.32571875 = 125.707222265625; \quad -354.729375 = -229.022152734375; \quad +132.3 = -96.722152734375; \quad +96 = -0.722152734375.
\]

Probemos \(y = -1.57\):

\[
y^2 = 2.4649, \quad y^3 = -3.869893, \quad y^4 = 6.07573201.
\]

\[
9y^4 = 54.68158809, \quad -18y^3 = 69.658074, \quad -143y^2 = -352.4807, \quad -84y = 131.88, \quad +96.
\]

Suma:

\[
54.68158809 + 69.058074? 
\]

Espera, recalculemos \(-18 y^3 = -18(-3.869893) = 69.658074\). Bien.

\[
54.68158809 + 69.658074 = 124.33966209; \quad -352.4807 = -228.14103791; \quad +131.88 = -96.26103791; \quad +96 = -0.26103791.
\]

Probemos \(y = -1.565\):

\[
y^2 = 2.449225, \quad y^3 = -3.833037125? 
\]

Calculemos: \((-1.565)^2 = 2.449225\). \((-1.565)^3 = 2.449225 \cdot (-1.565) = -3.833037125\). \(y^4 = (-3.833037125)(-1.565) = 5.998703100625\).

\[
9y^4 = 53.988327905625, \quad -18y^3 = 68.99466825, \quad -143y^2 = -350.239175, \quad -84y = 131.46, \quad +96.
\]

Suma:

\[
53.988327905625 + 68.99466825 = 122.982996155625; \quad -350.239175 = -227.256178844375; \quad +131.46 = -95.796178844375; \quad +96 = 0.203821155625.
\]

Entonces la raíz está entre \(-1.57\) y \(-1.565\).

Probemos \(y = -1.5677\):

\[
y^2 = 2.45768329, \quad y^3 = -2.45768329 \cdot 1.5677.
\]

Calculemos \(2.45768329 \cdot 1.5677\):

\(2.45768329 \cdot 1.5 = 3.686524935\), \(2.45768329 \cdot 0.0677 = 2.45768329 \cdot 0.06 = 0.1474609974\), \(2.45768329 \cdot 0.0077 = 0.018924161333\). Suma de los dos últimos: \(0.1474609974 + 0.018924161333 = 0.166385158733\). 

Entonces \(y^3 = -(3.686524935 + 0.166385158733) = -3.852910093733\).

\(y^4 = (-3.852910093733)(-1.5677) = 3.852910093733 \cdot 1.5677\).

\(3.852910093733 \cdot 1.5 = 5.7793651405995\), \(3.852910093733 \cdot 0.0677 = 0.23114460562398 + 0.029667407717... \) calculemos \(3.852910093733 \cdot 0.0677\): \(3.852910093733 \cdot 0.06 = 0.23117460562398\), \(3.852910093733 \cdot 0.0077 = 0.029667407721744\). Suma \(= 0.260842013345724\).

Entonces \(y^4 = 5.7793651405995 + 0.260842013345724 = 6.040207153945224\).

\[
9y^4 = 54.361864385507016, \quad -18y^3 = 69.352381687194, \quad -143y^2 = -351.44871047? 
\]

Calculemos \(2.45768329 \cdot 143 = 2.45768329 \cdot 100 = 245.768329\), \(2.45768329 \cdot 40 = 98.3073316\), \(2.45768329 \cdot 3 = 7.37304987\). Suma \(= 245.768329 + 98.3073316 + 7.37304987 = 351.44871047\). Entonces \(-143y^2 = -351.44871047\).

\(-84y = 84 \cdot 1.5677 = 84 \cdot 1.5 = 126\), \(84 \cdot 0.0677 = 5.6868\). Suma \(= 131.6868\).

Suma total \(C(-1.5677)\):

\[
54.361864385507016 + 69.352381687194 = 123.714246072701016.
\]

\[
123.714246072701016 - 351.44871047 = -227.734464397298984.
\]

\[
-227.734464397298984 + 131.6868 = -96.047664397298984.
\]

\[
-96.047664397298984 + 96 = -0.047664397298984.
\]

Aún ligeramente negativo.

Probemos \(y = -1.5675\):

Hagámoslo con menos precisión; la raíz está cerca de \(-1.5676\).

## 24. Buscar la forma cerrada de \(y\)

Necesitamos la forma exacta \(y = \frac{a - \sqrt{b}}{c}\). La raíz que nos interesa está cerca de \(-1.5676\).

Podemos resolver la cuártica en \(y\) con un CAS mental, pero mejor busquemos una solución exacta asumiendo que el resultado final es relativamente simple.

El problema es de olimpiada matemática, por lo que los números \(a, b, c\) deben ser "razonables". Busquemos una fracción \(\frac{a - \sqrt{b}}{c}\) cercana a \(-1.5676\).

Probemos \(c = 6\). Entonces \(y = \frac{a - \sqrt{b}}{6}\). Necesitamos \(a - \sqrt{b} \approx -9.4056\), luego \(\sqrt{b} \approx a + 9.4056\).

Probemos \(a = 3\): \(\sqrt{b} \approx 12.4056\), \(b \approx 153.9\). No es claro.

Probemos \(c = 3\): \(y = \frac{a - \sqrt{b}}{3}\). \(\sqrt{b} \approx a + 4.7028\).

Si \(a=3\), \(\sqrt{b} \approx 7.7028\), \(b \approx 59.33\).

Si \(a=7\), \(\sqrt{b} \approx 11.7028\), \(b \approx 136.96 \approx 137\)? \(\sqrt{137} \approx 11.7047\). Entonces \(y = \frac{7 - \sqrt{137}}{3} \approx \frac{7 - 11.7047}{3} = -1.5682\). Cercano.

Si \(a=2\), \(\sqrt{b} \approx 6.7028\), \(b \approx 44.93\).

Probemos \(y = \frac{7 - \sqrt{137}}{3} \approx -1.5682\). Nuestra raíz es \(\approx -1.5676\). No exacto.

Probemos \(c=4\): \(y = \frac{a - \sqrt{b}}{4}\). \(\sqrt{b} \approx a + 6.2704\).

Si \(a=1\), \(\sqrt{b} \approx 7.2704\), \(b\approx 52.86\).

Si \(a=5\), \(\sqrt{b} \approx 11.2704\), \(b \approx 127.02\).

Si \(a=7\), \(\sqrt{b} \approx 13.2704\), \(b \approx 176.1\).

Probemos \(c=8\): \(y = \frac{a - \sqrt{b}}{8}\). \(\sqrt{b} \approx a + 12.5408\).

Si \(a=3\), \(\sqrt{b}\approx 15.5408\), \(b\approx 241.5\).

Si \(a=7\), \(\sqrt{b}\approx 19.5408\), \(b\approx 381.8\).

Probemos \(c=2\): \(y = \frac{a - \sqrt{b}}{2}\). \(\sqrt{b} \approx a + 3.1352\).

Si \(a=4\), \(\sqrt{b} \approx 7.1352\), \(b\approx 50.91\).

Si \(a=7\), \(\sqrt{b}\approx 10.1352\), \(b\approx 102.72\).

Si \(a=10\), \(\sqrt{b}\approx 13.1352\), \(b\approx 172.53\).

Probemos \(c=5\): \(y=\frac{a-\sqrt{b}}{5}\). \(\sqrt{b} \approx a + 7.838\).

Si \(a=3\), \(\sqrt{b} \approx 10.838\), \(b\approx 117.47\).

Si \(a=7\), \(\sqrt{b}\approx 14.838\), \(b\approx 220.16\).

Probemos \(c=7\): \(y=\frac{a-\sqrt{b}}{7}\). \(\sqrt{b} \approx a + 10.9732\).

Si \(a=1\), \(\sqrt{b}\approx 11.9732\), \(b\approx 143.36\).

Si \(a=5\), \(\sqrt{b}\approx 15.9732\), \(b\approx 255.15\).

Probemos \(c=9\): \(y = \frac{a-\sqrt{b}}{9}\). \(\sqrt{b}\approx a + 14.1084\).

Si \(a=5\), \(\sqrt{b}\approx 19.1084\), \(b\approx 365.13\).

Probemos \(c=10\): \(y=\frac{a-\sqrt{b}}{10}\). \(\sqrt{b}\approx a + 15.676\).

Si \(a=1\), \(\sqrt{b}\approx 16.676\), \(b\approx 278.1\).

Si \(a=9\), \(\sqrt{b}\approx 24.676\), \(b\approx 608.9\).

Esto no converge a una forma simple. Quizá la raíz exacta sea más complicada y no corresponda a \(y\) directo con enteros pequeños.

Espera, quizá me equivoqué al descartar las soluciones. Revisemos si hay una solución exacta más elegante al sistema original.

## 25. Reconsiderar el sistema de ecuaciones

El punto de intersección satisface:

\[
y = x^2 - 4, \tag{A}
\]

y también \(R_{60}(x,y) = (s, s^2 - 4)\).

Quizá convenga pensar en la simetría rotacional. La composición de la rotación de \(60^\circ\) y la reflexión... Hmm.

Otra idea: la parábola \(y = x^2 - 4\) intersecta a su imagen rotada en hasta 4 puntos. Uno de ellos está en el cuarto cuadrante.

Podemos parametrizar la parábola con \(t\): \((t, t^2 -4)\). Su rotado es \((\frac12 t - \frac{\sqrt3}{2}(t^2-4), \frac{\sqrt3}{2}t + \frac12(t^2-4))\). Imponemos que este rotado esté en la parábola, lo que dio la cuártica en \(t\).

La cuártica en \(t\) es:

\[
3t^4 - 2\sqrt3 t^3 - 25t^2 + 6\sqrt3 t + 40 = 0.
\]

En \(x\) es la misma. En \(y\) obtuvimos otra cuártica. La raíz para \(y\) en el cuarto cuadrante es \(\approx -1.5676\).

Intentemos resolver la cuártica en \(y\) usando la fórmula de Ferrari o buscando una factorización con radicales.

La cuártica:

\[
9y^4 - 18y^3 - 143y^2 - 84y + 96 = 0.
\]

Dividamos por 9:

\[
y^4 - 2y^3 - \frac{143}{9}y^2 - \frac{28}{3}y + \frac{32}{3} = 0.
\]

Hagamos la sustitución \(y = z + \frac12\) (para eliminar el término cúbico, ya que \(b/a = -2\), el shift es \(b/(4a) = -2/(-4)? \). En general, para \(y^4 + py^3 + qy^2 + ry + s\), el shift \(y = z - p/4\).

Aquí \(p = -2\), así que \(y = z - (-2)/4 = z + 1/2\).

Sea \(y = z + \frac12\). Entonces:

\[
y^2 = z^2 + z + \frac14.
\]

\[
y^3 = z^3 + \frac32 z^2 + \frac34 z + \frac18.
\]

\[
y^4 = z^4 + 2z^3 + \frac32 z^2 + \frac12 z + \frac1{16}.
\]

Sustituyendo en \(y^4 - 2y^3 - \frac{143}{9}y^2 - \frac{28}{3}y + \frac{32}{3}\):

- \(y^4\): \(z^4 + 2z^3 + \frac32 z^2 + \frac12 z + \frac1{16}\).

- \(-2y^3\): \(-2z^3 - 3z^2 - \frac32 z - \frac14\).

- \(-\frac{143}{9}y^2\): \(-\frac{143}{9}z^2 - \frac{143}{9}z - \frac{143}{36}\).

- \(-\frac{28}{3}y\): \(-\frac{28}{3}z - \frac{14}{3}\).

- \(+\frac{32}{3}\).

Ahora sumamos coeficiente por coeficiente.

Coeficiente de \(z^4\): 1.

Coeficiente de \(z^3\): \(2 - 2 = 0\). Bien.

Coeficiente de \(z^2\): \(\frac32 - 3 - \frac{143}{9}\).

\[
\frac32 = \frac{27}{18}? 
\]

Convertimos a denominador 18:

\[
\frac32 = \frac{27}{18}, \quad -3 = -\frac{54}{18}, \quad -\frac{143}{9} = -\frac{286}{18}.
\]

Suma: \(\frac{27 - 54 - 286}{18} = \frac{-313}{18}\).

Coeficiente de \(z\): \(\frac12 - \frac32 - \frac{143}{9} - \frac{28}{3}\).

Convertimos a denominador 18:

\[
\frac12 = \frac{9}{18}, \quad -\frac32 = -\frac{27}{18}, \quad -\frac{143}{9} = -\frac{286}{18}, \quad -\frac{28}{3} = -\frac{168}{18}.
\]

Suma: \(\frac{9 - 27 - 286 - 168}{18} = \frac{-472}{18} = -\frac{236}{9}\).

Constante: \(\frac1{16} - \frac14 - \frac{143}{36} - \frac{14}{3} + \frac{32}{3}\).

Convertimos a denominador 144:

\[
\frac1{16} = \frac{9}{144}, \quad -\frac14 = -\frac{36}{144}, \quad -\frac{143}{36} = -\frac{572}{144}, \quad -\frac{14}{3} = -\frac{672}{144}, \quad +\frac{32}{3} = +\frac{1536}{144}.
\]

Suma: \(\frac{9 - 36 - 572 - 672 + 1536}{144} = \frac{265}{144}\).

Entonces la cuártica en \(z\) es:

\[
z^4 - \frac{313}{18} z^2 - \frac{236}{9} z + \frac{265}{144} = 0.
\]

Multiplicamos por 144 para evitar fracciones:

\[
144z^4 - 2504 z^2 - 3776 z + 265 = 0. \tag{9}
\]

Ahora intentamos expresar (9) como \((12z^2 + \alpha z + \beta)(12z^2 + \gamma z + \delta) = 0\) o usar Ferrari.

Ferrari: queremos escribir

\[
(z^2 + A)^2 - (Bz + C)^2 = 0
\]

que expandido es

\[
z^4 + (2A - B^2)z^2 - 2BC\, z + (A^2 - C^2).
\]

Comparando con (9), dividimos (9) entre 144:

\[
z^4 - \frac{2504}{144} z^2 - \frac{3776}{144} z + \frac{265}{144} = 0.
\]

Simplificando:

\[
z^4 - \frac{313}{18}z^2 - \frac{236}{9}z + \frac{265}{144} = 0.
\]

Entonces:

\[
2A - B^2 = -\frac{313}{18},
\]

\[
-2BC = -\frac{236}{9} \implies 2BC = \frac{236}{9} \implies BC = \frac{118}{9},
\]

\[
A^2 - C^2 = \frac{265}{144}.
\]

De \(2A - B^2 = -\frac{313}{18}\), \(B^2 = 2A + \frac{313}{18}\).

De \(BC = \frac{118}{9}\), \(B^2 C^2 = \left(\frac{118}{9}\right)^2 = \frac{13924}{81}\).

Pero \(C^2 = A^2 - \frac{265}{144}\).

Entonces:

\[
\left(2A + \frac{313}{18}\right)\left(A^2 - \frac{265}{144}\right) = \frac{13924}{81}.
\]

Esta es la cúbica resolvente de Ferrari:

\[
(2A + \frac{313}{18})(A^2 - \frac{265}{144}) - \frac{13924}{81} = 0.
\]

Multipliquemos por 144 (o un múltiplo) para simplificar.

Primero, notemos que \(2A + \frac{313}{18} = \frac{36A + 313}{18}\).

Entonces:

\[
\frac{36A + 313}{18} \cdot \left(A^2 - \frac{265}{144}\right) = \frac{(36A+313)(144A^2 - 265)}{18 \cdot 144}.
\]

Igual a \(\frac{13924}{81}\).

Multiplicando por \(18\cdot 144\):

\[
(36A + 313)(144A^2 - 265) = \frac{13924}{81} \cdot 18 \cdot 144.
\]

Calculemos el lado derecho:

\[
\frac{13924}{81} \cdot 2592 = 13924 \cdot 32 = 445568.
\]

Entonces:

\[
(36A + 313)(144A^2 - 265) = 445568.
\]

Desarrollemos el lado izquierdo:

\[
36A \cdot 144A^2 = 5184 A^3,
\]

\[
36A \cdot (-265) = -9540 A,
\]

\[
313 \cdot 144A^2 = 45072 A^2,
\]

\[
313 \cdot (-265) = -82945.
\]

Entonces:

\[
5184 A^3 + 45072 A^2 - 9540 A - 82945 = 445568.
\]

\[
5184 A^3 + 45072 A^2 - 9540 A - 528513 = 0.
\]

Esta es la cúbica en \(A\). Podemos intentar encontrar una raíz racional. Escalamos para simplificar: dividimos entre 3:

\[
1728 A^3 + 15024 A^2 - 3180 A - 176171 = 0.
\]

Busquemos raíces racionales de la forma \(A = \frac{p}{q}\).

Reescribamos:

\[
1728A^3 + 15024A^2 - 3180A - 176171 = 0.
\]

Intentemos \(A = \frac{25}{12}\):

\[
A^2 = \frac{625}{144}, \quad A^3 = \frac{15625}{1728}.
\]

\[
1728 \cdot \frac{15625}{1728} = 15625.
\]

\[
15024 \cdot \frac{625}{144} = 15024/144 \cdot 625 = 104.333... \cdot 625.
\]

\(15024 / 144 = 104.333...\). Mejor simplifiquemos: \(15024/144 = 104.333...\), no es exacto. \(15024 = 16\cdot 939\), \(144 = 16\cdot 9\), así que \(15024/144 = 939/9 = 104.333...\). Hmm, \(939/9 = 104.333...\), sigue sin ser exacto. Entonces no es raíz racional con denominador simple.

Esto se está complicando mucho. Tal vez haya un error en mi planteamiento o una solución más elegante.

## 26. Revisar el planteamiento inicial

Vuelvo a revisar la ecuación de la imagen rotada.

La parábola original: \(y = x^2 - 4\).

Rotación antihoraria de \(60^\circ\): \((x, y) \mapsto (x\cos60 - y\sin60, x\sin60 + y\cos60) = (\frac12 x - \frac{\sqrt3}{2}y, \frac{\sqrt3}{2}x + \frac12 y)\).

Un punto \((X, Y)\) está en la imagen rotada si existe \((x,y)\) en la original tal que:

\[
X = \frac12 x - \frac{\sqrt3}{2}y, \quad Y = \frac{\sqrt3}{2}x + \frac12 y.
\]

Inversa (rotación horaria de \(60^\circ\)):

\[
x = \frac12 X + \frac{\sqrt3}{2}Y, \quad y = -\frac{\sqrt3}{2}X + \frac12 Y.
\]

Imponiendo \(y = x^2 - 4\):

\[
-\frac{\sqrt3}{2}X + \frac12 Y = \left(\frac12 X + \frac{\sqrt3}{2}Y\right)^2 - 4.
\]

Multiplicando por 4:

\[
-2\sqrt3 X + 2Y = (X + \sqrt3 Y)^2 - 16.
\]

\[
(X + \sqrt3 Y)^2 + 2\sqrt3 X - 2Y - 16 = 0.
\]

Esto es correcto.

En la sección anterior, al sustituir \(y = x^2 - 4\), obtuvimos la cuártica en \(x\):

\[
3x^4 - 2\sqrt3 x^3 - 25x^2 + 6\sqrt3 x + 40 = 0.
\]

Y al sustituir \(x^2 = y+4\), obtuvimos la cuártica en \(y\):

\[
9y^4 - 18y^3 - 143y^2 - 84y + 96 = 0.
\]

Ambas son correctas.

Quizá la raíz que buscamos para \(y\) no sea \(\approx -1.5676\) sino otra. Revisemos los signos de \(C(y)\) en los puntos que probamos. Definimos \(C(y) = 9y^4 - 18y^3 - 143y^2 - 84y + 96\).

\(C(-1.55) \approx 1.62 > 0\), \(C(-1.6) \approx -2.97 < 0\). Entonces hay una raíz entre \(-1.6\) y \(-1.55\). Esta corresponde a un \(x>0\) (ya que \(x^2 = y+4\), y para \(y \approx -1.5676\), \(x^2 \approx 2.4324\), \(x \approx 1.5597 > 0\)). Es la raíz que nos interesa.

## 27. Probar una factorización directa con radicales para \(C(y)\)

Tal vez la cuártica en \(y\) factoriza como dos cuadráticos con coeficientes que involucran \(\sqrt{3}\) o \(\sqrt{13}\), etc.

Intentemos \((3y^2 + (p+q\sqrt3)y + (r+s\sqrt3))(3y^2 + (p'-q'\sqrt3)y + (r'-s'\sqrt3))\). Esto es engorroso.

Otra idea: dado que el problema proviene de una olimpiada, quizá la intersección relevante no requiera la cuártica completa, porque el punto en el cuarto cuadrante satisface además alguna condición geométrica más directa.

Por ejemplo, la parábola \(y = x^2 - 4\) y su imagen bajo rotación de \(60^\circ\). El vértice de la original es \((0, -4)\). Su imagen es \((\frac12\cdot 0 - \frac{\sqrt3}{2}(-4), \frac{\sqrt3}{2}\cdot 0 + \frac12(-4)) = (2\sqrt3, -2)\).

La parábola original tiene foco \((0, -15/4)\), y la imagen tiene foco \((\frac{15\sqrt3}{8}, -15/8)\).

Las dos parábolas podrían intersecarse en puntos que no involucran números feos. Busquemos puntos de intersección especiales.

## 28. Buscar intersecciones "bonitas"

Probemos si hay una intersección con \(x\) o \(y\) con valores simples. Ya vimos que la raíz en el cuarto cuadrante tiene \(y \approx -1.5676\), no es un valor común.

Verifiquemos si hay intersecciones en el eje \(y\) (\(x=0\)):

Original: \(y = -4\).

Imagen: sustituimos \(x=0\) en la ecuación (1):

\[
(\sqrt3 y)^2 + 2\sqrt3\cdot 0 - 2y - 16 = 3y^2 - 2y - 16 = 0.
\]

\[
3y^2 - 2y - 16 = 0 \implies y = \frac{2 \pm \sqrt{4 + 192}}{6} = \frac{2 \pm 14}{6}.
\]

Soluciones: \(y = \frac{16}{6} = \frac{8}{3}\) y \(y = \frac{-12}{6} = -2\).

Entonces la imagen intersecta el eje \(y\) en \((0, 8/3)\) y \((0, -2)\). La original en \((0, -4)\). No coinciden.

Intersección en el eje \(x\) (\(y=0\)):

Original: \(y = x^2 -4 = 0 \implies x = \pm 2\). Puntos \((2,0)\) y \((-2,0)\).

Imagen: \(y=0\) en (1):

\[
x^2 + 2\sqrt3 x - 16 = 0.
\]

\[
x = \frac{-2\sqrt3 \pm \sqrt{12+64}}{2} = \frac{-2\sqrt3 \pm \sqrt{76}}{2} = -\sqrt3 \pm \sqrt{19}.
\]

Entonces la imagen cruza el eje \(x\) en \(x = -\sqrt3 \pm \sqrt{19}\). La original en \(x = \pm 2\). No coinciden.

## 29. Usar la intersección de las dos parábolas y la simetría de la rotación

La rotación de \(60^\circ\) es un movimiento rígido. La parábola es cóncava hacia arriba. La imagen también es cóncava hacia arriba (rotada 60°, sigue siendo cóncava "hacia arriba" en su propio eje).

Consideremos la recta \(L\) que pasa por el origen y el punto de intersección \((x, y)\). Sea \(\theta\) el ángulo de \(L\) con el eje \(x\). El punto \((x,y) = r(\cos\theta, \sin\theta)\).

El punto rotado \(60^\circ\) es \(r(\cos(\theta+60^\circ), \sin(\theta+60^\circ))\).

Ambos están sobre la parábola \(y = x^2 -4\). Entonces:

\[
r\sin\theta = r^2\cos^2\theta - 4,
\]

\[
r\sin(\theta+60^\circ) = r^2\cos^2(\theta+60^\circ) - 4.
\]

Restando:

\[
r[\sin(\theta+60^\circ) - \sin\theta] = r^2[\cos^2(\theta+60^\circ) - \cos^2\theta].
\]

Si \(r \neq 0\), dividimos por \(r\) y usamos identidades.

\[
\sin(\theta+60) - \sin\theta = 2\cos(\theta+30)\sin30 = \cos(\theta+30).
\]

\[
\cos^2(\theta+60) - \cos^2\theta = -\sin(2\theta+60)\sin60? 
\]

Usemos \(\cos^2 A - \cos^2 B = -\sin(A+B)\sin(A-B)\).

Aquí \(A = \theta + 60\), \(B = \theta\). Entonces \(A+B = 2\theta + 60\), \(A-B = 60\).

\[
\cos^2(\theta+60) - \cos^2\theta = -\sin(2\theta+60)\sin60 = -\frac{\sqrt3}{2}\sin(2\theta+60).
\]

Entonces:

\[
r \cos(\theta+30) = r^2 \left(-\frac{\sqrt3}{2}\sin(2\theta+60)\right).
\]

Dividimos por \(r\) (suponiendo \(r\neq0\)):

\[
\cos(\theta+30) = -\frac{\sqrt3}{2} r \sin(2\theta+60).
\]

Además, de la ecuación original:

\[
r\sin\theta = r^2\cos^2\theta - 4 \implies \sin\theta = r\cos^2\theta - \frac{4}{r}.
\]

Esto se complica, pero quizá podamos hallar \(\theta\) directamente.

Otra observación: sumando las dos ecuaciones en lugar de restar, o usar la propiedad de que la diferencia de las dos parábolas es una recta (la diferencia de sus ecuaciones) en la que cae la intersección.

## 30. Diferencia de las ecuaciones

La ecuación de la original es \(y - x^2 + 4 = 0\).

La ecuación de la imagen es \((x+\sqrt3 y)^2 + 2\sqrt3 x - 2y - 16 = 0\), es decir, \(x^2 + 2\sqrt3 xy + 3y^2 + 2\sqrt3 x - 2y - 16 = 0\).

En un punto de intersección, ambas se anulan. La diferencia entre ambas (no lineal) no es directamente una recta. Sin embargo, podemos restar la primera ecuación multiplicada por algo para eliminar \(x^2\).

De la original: \(x^2 = y + 4\).

Sustituyendo en la imagen:

\[
(y+4) + 2\sqrt3 x y + 3y^2 + 2\sqrt3 x - 2y - 16 = 0.
\]

\[
3y^2 + 2\sqrt3 x y + 2\sqrt3 x - y - 12 = 0. \tag{10}
\]

Despejamos \(x\):

\[
2\sqrt3 x (y + 1) = -3y^2 + y + 12.
\]

\[
x = \frac{-3y^2 + y + 12}{2\sqrt3 (y+1)} = \frac{3y^2 - y - 12}{-2\sqrt3(y+1)}.
\]

Como \(y \approx -1.5676\), el denominador \(y+1 \approx -0.5676\) es negativo, y el numerador \(3y^2 - y -12\): \(3(2.457) - (-1.5676) -12 = 7.371 + 1.5676 -12 = -3.0614\). Entonces \(x\) positivo, coherente.

Elevando al cuadrado \(x^2 = y + 4\), recuperamos la cuártica en \(y\).

## 31. Relacionar con \(\tan\) o ángulos

Del sistema (10):

\[
2\sqrt3 x y + 2\sqrt3 x = 3y^2 - y -12? 
\]

Espera, reescribamos (10):

\[
3y^2 - y - 12 + 2\sqrt3 x(y+1) = 0.
\]

\[
2\sqrt3 x (y+1) = -3y^2 + y + 12 = -(3y^2 - y - 12).
\]

Entonces:

\[
x = \frac{-(3y^2 - y - 12)}{2\sqrt3 (y+1)} = \frac{3y^2 - y - 12}{-2\sqrt3(y+1)}.
\]

Esto es correcto.

También \(x^2 = y+4\).

Entonces:

\[
\left(\frac{3y^2 - y - 12}{-2\sqrt3(y+1)}\right)^2 = y+4.
\]

\[
\frac{(3y^2 - y - 12)^2}{12(y+1)^2} = y+4.
\]

\[
(3y^2 - y - 12)^2 = 12(y+4)(y+1)^2.
\]

Que es lo que teníamos.

## 32. Intentar factorizar la cuártica en \(y\) encontrando una raíz "bonita" exacta

Tal vez la raíz para \(y\) es exactamente \(-\frac{3+\sqrt{13}}{4}\) o algo así. Calculemos \(-\frac{3+\sqrt{13}}{4} \approx -\frac{3+3.6055}{4} = -1.6514\). No.

Probemos \(-\frac{5+\sqrt{13}}{6}\): \(-\frac{5+3.6055}{6} = -1.4343\). No.

Probemos \(-\frac{7+\sqrt{13}}{8}\): \(-1.3257\). No.

Nuestra raíz es \(\approx -1.5676\).

Busquemos una fracción \(-\frac{\sqrt{b} - a}{c}\) con \(b\) cuadrado perfecto cercano. Si \(y = \frac{a - \sqrt{b}}{c}\), y suponemos \(b\) no es cuadrado perfecto, entonces \(\sqrt{b}\) es irracional.

Podemos usar la cuártica en \(y\) para hallar \(y\) exactamente. La raíz que queremos es la única en el intervalo \((-1.6, -1.55)\) tal que además \(x>0\).

Resolvamos la cuártica en \(y\) de manera exacta usando la fórmula de Ferrari con más paciencia, o usemos el hecho de que el problema pide \(a+b+c\), lo cual sugiere que \(a, b, c\) son concretos y no muy grandes. Mi búsqueda por tanteo no encontró una forma obvia, quizá porque \(c\) es grande o porque \(b\) es grande.

Intentemos hallar la raíz con más precisión para luego identificar \(a, b, c\).

De los cálculos anteriores, \(C(-1.5677) \approx -0.0477\), \(C(-1.5675)\) determinemos el signo.

Calculé \(C(-1.5677) \approx -0.04766\). Calculemos \(C(-1.5675)\):

Usemos incremento. Derivada \(C'(y) = 36y^3 - 54y^2 - 286y - 84\).

En \(y=-1.5677\):

\[
y^2 \approx 2.4577, \quad y^3 \approx -3.8529.
\]

\[
36 y^3 \approx -138.7044, \quad -54y^2 \approx -132.7158, \quad -286y \approx 448.3622, \quad -84.
\]

Suma: \(-138.7044 -132.7158 +448.3622 -84 = 92.942\).

Entonces \(C'(y) \approx 92.94\) en ese punto. Para cambiar \(C\) de \(-0.0477\) a 0, necesitamos \(\Delta y \approx 0.0477/92.94 \approx 0.000513\). Entonces la raíz está en \(y \approx -1.5677 + 0.000513 = -1.567187\).

Verifiquemos \(C(-1.5672)\):

Aproximemos: \(y = -1.567187\).

Calculemos \(C(-1.5672)\) con suficiente precisión.

\(y = -1.5672\). \(y^2 = 1.5672^2 = 2.45611584\). \(y^3 = -2.45611584 \cdot 1.5672 = -3.850065...\). Calculemos: \(2.45611584 \cdot 1.5672 = 2.45611584 \cdot 1.5 = 3.68417376\), \(2.45611584 \cdot 0.0672 = 0.165... \) \(2.45611584 \cdot 0

<tool_use>
Tool: Bash
Command: "python3 - <<'PY'\nimport sympy as sp\ny=sp.symbols('y')\nC=9*y**4-18*y**3-143*y**2-84*y+96\nprint(sp.factor(C))\nprint(sp.roots(C))\n# also original x quartic roots\nx=sp.symbols('x')\nX=3*x**4-2*sp.sqrt(3)*x**3-25*x**2+6*sp.sqrt(3)*x+40\nprint(sp.factor(X, extension=sp.sqrt(3)))\nprint(sp.nroots(X))\nPY"</tool_use>