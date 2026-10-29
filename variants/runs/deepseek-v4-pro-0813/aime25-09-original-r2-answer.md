Vamos a resolver el problema paso a paso.

## 1. Planteamiento

La parábola original es

\[
y = x^2 - 4.
\]

Al rotarla \(60^\circ\) en sentido antihorario alrededor del origen, la transformación de un punto \((x,y)\) es:

\[
\begin{cases}
x' = x\cos 60^\circ - y\sin 60^\circ = \dfrac{x}{2} - \dfrac{\sqrt{3}}{2}y,\\[6pt]
y' = x\sin 60^\circ + y\cos 60^\circ = \dfrac{\sqrt{3}}{2}x + \dfrac{y}{2}.
\end{cases}
\]

Por tanto, la parábola imagen está formada por los puntos \((x',y')\) que provienen de puntos de la parábola original. Sin embargo, para encontrar la intersección de la parábola original con su imagen, es más cómodo plantearlo usando la transformación inversa.

## 2. Ecuación de la imagen

Un punto \((x,y)\) pertenece a la imagen rotada si, al rotarlo \(-60^\circ\), cae sobre la parábola original. La rotación inversa de \(60^\circ\) es una rotación de \(-60^\circ\):

\[
\begin{cases}
X = x\cos 60^\circ + y\sin 60^\circ = \dfrac{x}{2} + \dfrac{\sqrt{3}}{2}y,\\[6pt]
Y = -x\sin 60^\circ + y\cos 60^\circ = -\dfrac{\sqrt{3}}{2}x + \dfrac{y}{2}.
\end{cases}
\]

Para que \((x,y)\) esté en la imagen, debe cumplirse:

\[
Y = X^2 - 4.
\]

Sustituyendo:

\[
-\frac{\sqrt{3}}{2}x + \frac{y}{2}
=
\left(\frac{x}{2} + \frac{\sqrt{3}}{2}y\right)^2 - 4.
\]

Desarrollamos el cuadrado:

\[
\left(\frac{x + \sqrt{3}y}{2}\right)^2
=
\frac{x^2 + 2\sqrt{3}xy + 3y^2}{4}.
\]

Así, la ecuación de la imagen es:

\[
-\frac{\sqrt{3}}{2}x + \frac{y}{2}
=
\frac{x^2 + 2\sqrt{3}xy + 3y^2}{4} - 4.
\]

## 3. Sistema para la intersección

La intersección debe satisfacer a la vez

\[
y = x^2 - 4
\]

y la ecuación anterior. Sustituimos \(y = x^2 - 4\) en la ecuación de la imagen.

Primero, la parte izquierda:

\[
-\frac{\sqrt{3}}{2}x + \frac{x^2 - 4}{2}.
\]

La parte derecha:

\[
\frac{x^2 + 2\sqrt{3}x(x^2 - 4) + 3(x^2 - 4)^2}{4} - 4.
\]

La ecuación completa queda:

\[
-\frac{\sqrt{3}}{2}x + \frac{x^2 - 4}{2}
=
\frac{x^2 + 2\sqrt{3}x(x^2 - 4) + 3(x^2 - 4)^2}{4} - 4.
\]

Multiplicamos por \(4\):

\[
-2\sqrt{3}x + 2x^2 - 8
=
x^2 + 2\sqrt{3}x(x^2 - 4) + 3(x^2 - 4)^2 - 16.
\]

Sumamos \(16\):

\[
-2\sqrt{3}x + 2x^2 + 8
=
x^2 + 2\sqrt{3}x(x^2 - 4) + 3(x^2 - 4)^2.
\]

Notemos que

\[
3(x^2-4)^2 = 3x^4 - 24x^2 + 48.
\]

Entonces el lado derecho es:

\[
x^2 + 2\sqrt{3}x^3 - 8\sqrt{3}x + 3x^4 - 24x^2 + 48.
\]

La ecuación queda:

\[
-2\sqrt{3}x + 2x^2 + 8
=
3x^4 + 2\sqrt{3}x^3 - 8\sqrt{3}x - 23x^2 + 48.
\]

Pasamos todo al lado derecho:

\[
0 = 3x^4 + 2\sqrt{3}x^3 - 8\sqrt{3}x - 23x^2 + 48 + 2\sqrt{3}x - 2x^2 - 8.
\]

Simplificamos:

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 + (-8\sqrt{3} + 2\sqrt{3})x + 40 = 0.
\]

Es decir:

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40 = 0.
\]

## 4. Factorización

Buscamos factorizar el polinomio separando términos con \(\sqrt{3}\):

\[
(3x^4 - 25x^2 + 40) + 2\sqrt{3}(x^3 - 3x) = 0.
\]

Observamos que:

\[
x^3 - 3x = x(x^2 - 3).
\]

Y

\[
3x^4 - 25x^2 + 40.
\]

Probemos si se puede escribir como \(\left(\sqrt{3}x^2 + \dots\right)\) multiplicado por algo.

Intentemos la factorización:

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40
=
\left(\sqrt{3}x^2 + bx + c\right)\left(\sqrt{3}x^2 + dx + e\right).
\]

El producto de los términos principales debe ser \(3x^4\), lo cual se cumple con \(\sqrt{3}\cdot\sqrt{3}=3\).

Probemos:

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40
=
(\sqrt{3}x^2 + ax + b)(\sqrt{3}x^2 + cx + d).
\]

Al multiplicar:

- Coeficiente de \(x^3\): \(\sqrt{3}(a+c) = 2\sqrt{3}\), luego \(a+c=2\).
- Coeficiente de \(x^2\): \(\sqrt{3}(ad+bc) + ac\).
- Coeficiente de \(x\): \(ad + bc\).
- Término constante: \(bd=40\).

Vamos a intentar con números sencillos. Si tomamos \(a=2\) y \(c=0\), entonces \(a+c=2\). Los coeficientes serían:

- Coeficiente de \(x\): \(ad+bc = 2d + 0\cdot b = 2d\).
- Término constante: \(bd = 40\).
- Coeficiente de \(x^2\): \(\sqrt{3}(2d) + 0 = 2\sqrt{3}d\).

Queremos que el coeficiente de \(x\) sea \(-6\sqrt{3}\), es decir:

\[
2d = -6\sqrt{3} \implies d = -3\sqrt{3}.
\]

Entonces \(bd = 40\), así que \(b = \dfrac{40}{-3\sqrt{3}} = -\dfrac{40}{3\sqrt{3}}\), que no es entero. No parece el camino.

Intentemos otra descomposición. Podemos agrupar de la siguiente forma:

\[
3x^4 - 25x^2 + 40 = (3x^2 - ?)(x^2 - ?).
\]

Buscamos factorizaciones de \(40\) y de \(-25\).

Probemos

\[
3x^4 - 25x^2 + 40 = (3x^2 - 10)(x^2 - 4).
\]

Multiplicamos:

\[
3x^4 - 12x^2 - 10x^2 + 40 = 3x^4 - 22x^2 + 40.
\]

No es \(-25x^2\). Probemos \((3x^2-8)(x^2-5)\):

\[
3x^4 - 15x^2 - 8x^2 + 40 = 3x^4 - 23x^2 + 40.
\]

Tampoco.

Probemos \((3x^2-4)(x^2-10)\):

\[
3x^4 - 30x^2 - 4x^2 + 40 = 3x^4 - 34x^2 + 40.
\]

No.

Factorizamos directamente el polinomio mediante cálculo asistido. La ecuación era:

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40 = 0.
\]

Probemos como producto:

\[
(\sqrt{3}x^2 + ax + b)(\sqrt{3}x^2 + cx + d).
\]

Desarrollamos con coeficientes a determinar:

\[
(\sqrt{3}x^2 + ax + b)(\sqrt{3}x^2 + cx + d)
= 3x^4 + \sqrt{3}(a+c)x^3 + (ac + \sqrt{3}(ad+bc))x^2 + (ad+bc)x + bd.
\]

Igualando:

1. \(\sqrt{3}(a+c) = 2\sqrt{3} \implies a+c=2\).
2. \(bd=40\).
3. \(ad+bc = -6\sqrt{3}\).
4. \(ac + \sqrt{3}(ad+bc) = -25\).

De la ecuación 3, \(ad+bc=-6\sqrt{3}\). Entonces:

\[
ac + \sqrt{3}(-6\sqrt{3}) = -25.
\]

Como \(\sqrt{3}\cdot\sqrt{3}=3\), tenemos:

\[
ac - 18 = -25 \implies ac = -7.
\]

Entonces tenemos:

\[
a+c=2,\qquad ac=-7.
\]

Las soluciones son las raíces de \(t^2 - 2t - 7 = 0\), es decir:

\[
t = \frac{2 \pm \sqrt{4+28}}{2} = \frac{2 \pm \sqrt{32}}{2} = 1 \pm 2\sqrt{2}.
\]

Esto nos llevaría a coeficientes irracionales, lo cual no es incorrecto, pero el enunciado sugiere que el resultado final tiene la forma sencilla \(\frac{a-\sqrt{b}}{c}\).

Ahora, de \(bd=40\) y \(ad+bc=-6\sqrt{3}\). Con \(a\) y \(c\) expresados arriba, podríamos resolver, pero será más cómodo resolver el polinomio directamente.

## 5. Resolución directa

Separamos la ecuación en parte racional y parte con \(\sqrt{3}\):

\[
3x^4 - 25x^2 + 40 = -2\sqrt{3}(x^3 - 3x).
\]

Elevar al cuadrado no es ideal porque introduce soluciones extrañas. Mejor buscamos raíces del polinomio original.

Probemos \(x = \sqrt{3}\):

\[
3(\sqrt{3})^4 + 2\sqrt{3}(\sqrt{3})^3 - 25(\sqrt{3})^2 - 6\sqrt{3}\cdot\sqrt{3} + 40.
\]

Calculamos:

\[
(\sqrt{3})^4 = 9,\quad 3\cdot 9 = 27.
\]

\[
(\sqrt{3})^3 = 3\sqrt{3},\quad 2\sqrt{3}\cdot 3\sqrt{3} = 2\cdot 3\cdot 3 = 18.
\]

\[
-25\cdot 3 = -75.
\]

\[
-6\sqrt{3}\cdot\sqrt{3} = -18.
\]

Sumamos:

\[
27 + 18 - 75 - 18 + 40 = 45 - 75 - 18 + 40 = -30 - 18 + 40 = -8.
\]

No es raíz.

Probemos \(x=2\):

\[
3\cdot 16 + 2\sqrt{3}\cdot 8 - 25\cdot 4 - 6\sqrt{3}\cdot 2 + 40.
\]

\[
48 + 16\sqrt{3} - 100 - 12\sqrt{3} + 40.
\]

\[
(48 - 100 + 40) + (16\sqrt{3} - 12\sqrt{3}) = -12 + 4\sqrt{3}.
\]

Tampoco.

Probemos \(x=\sqrt{5}\):

\[
x^2=5,\quad x^4=25.
\]

\[
3\cdot 25 = 75.
\]

\[
2\sqrt{3}\cdot 5\sqrt{5} = 10\sqrt{15}.
\]

\[
-25\cdot 5 = -125.
\]

\[
-6\sqrt{3}\cdot\sqrt{5} = -6\sqrt{15}.
\]

\[
75 + 10\sqrt{15} - 125 - 6\sqrt{15} + 40
= (75 - 125 + 40) + 4\sqrt{15}
= -10 + 4\sqrt{15}.
\]

No.

Probemos \(x = \sqrt{\frac{8}{3}}\) o valores que hagan racional el polinomio.

Intentemos factorizar numéricamente. Observamos que la ecuación puede verse como:

\[
3x^4 - 25x^2 + 40 = -2\sqrt{3}x(x^2-3).
\]

Elevando al cuadrado:

\[
(3x^4 - 25x^2 + 40)^2 = 12x^2(x^2-3)^2.
\]

Expandimos el lado izquierdo:

Sea \(t=x^2\). Entonces

\[
3t^2 - 25t + 40.
\]

La ecuación queda:

\[
(3t^2 - 25t + 40)^2 = 12t(t-3)^2.
\]

Ahora resolvamos esta ecuación en \(t\). Desarrollamos:

Lado izquierdo:

\[
(3t^2 - 25t + 40)^2.
\]

Calculemos con cuidado:

\[
(3t^2)^2 = 9t^4,
\]

\[
2\cdot 3t^2 \cdot (-25t) = -150t^3,
\]

\[
2\cdot 3t^2 \cdot 40 = 240t^2,
\]

\[
(-25t)^2 = 625t^2,
\]

\[
2\cdot (-25t)\cdot 40 = -2000t,
\]

\[
40^2 = 1600.
\]

Sumamos:

\[
9t^4 - 150t^3 + (240+625)t^2 - 2000t + 1600
=
9t^4 - 150t^3 + 865t^2 - 2000t + 1600.
\]

Lado derecho:

\[
12t(t-3)^2 = 12t(t^2 - 6t + 9) = 12t^3 - 72t^2 + 108t.
\]

Igualamos:

\[
9t^4 - 150t^3 + 865t^2 - 2000t + 1600 = 12t^3 - 72t^2 + 108t.
\]

Pasamos todo a la izquierda:

\[
9t^4 - 162t^3 + 937t^2 - 2108t + 1600 = 0.
\]

Buscamos raíces racionales. Los divisores de \(1600\) y \(9\) son muchos. Probemos \(t=4\):

\[
9\cdot 256 - 162\cdot 64 + 937\cdot 16 - 2108\cdot 4 + 1600.
\]

Calculamos:

\[
2304 - 10368 + 14992 - 8432 + 1600.
\]

\[
2304 - 10368 = -8064.
\]

\[
-8064 + 14992 = 6928.
\]

\[
6928 - 8432 = -1504.
\]

\[
-1504 + 1600 = 96.
\]

No.

Probemos \(t=8\):

\[
9\cdot 4096 - 162\cdot 512 + 937\cdot 64 - 2108\cdot 8 + 1600.
\]

\[
36864 - 82944 + 59968 - 16864 + 1600.
\]

\[
36864 - 82944 = -46080.
\]

\[
-46080 + 59968 = 13888.
\]

\[
13888 - 16864 = -2976.
\]

\[
-2976 + 1600 = -1376.
\]

No.

Probemos \(t = \frac{16}{3}\):

Sería engorroso. Mejor factoricemos el polinomio en \(t\).

Buscamos descomposición:

\[
9t^4 - 162t^3 + 937t^2 - 2108t + 1600.
\]

Probemos como producto de dos cuadráticos con coeficientes enteros:

\[
(3t^2 + at + b)(3t^2 + ct + d).
\]

El producto principal es \(9t^4\). Entonces:

- Coeficiente de \(t^3\): \(3(a+c) = -162\), así que \(a+c=-54\).
- Coeficiente de \(t^2\): \(3(ad+bc)+ac = 937\).
- Coeficiente de \(t\): \(ad+bc = -2108\).
- Término constante: \(bd=1600\).

De \(ad+bc=-2108\), tenemos:

\[
3(-2108) + ac = 937.
\]

\[
-6324 + ac = 937 \implies ac = 7261.
\]

Y \(a+c=-54\). Entonces \(a\) y \(c\) son raíces de:

\[
t^2 + 54t + 7261 = 0.
\]

El discriminante:

\[
54^2 - 4\cdot 7261 = 2916 - 29044 = -26128.
\]

Negativo, no hay factorización con coeficientes reales simples. Podría no factorizar en racionales.

Probemos con coeficientes \(1\) y \(9\):

\[
(t^2 + at + b)(9t^2 + ct + d).
\]

- Coeficiente de \(t^3\): \(c + 9a = -162\).
- Coeficiente de \(t^2\): \(d + ac + 9b = 937\).
- Coeficiente de \(t\): \(ad + bc = -2108\).
- Constante: \(bd=1600\).

Esto se complica. Recurramos a buscar raíces con un enfoque diferente.

## 6. Enfoque con la ecuación original y la forma de la solución

El enunciado dice que el punto único en el cuarto cuadrante donde se intersecan tiene \(y\)-coordenada

\[
\frac{a-\sqrt{b}}{c}.
\]

En el cuarto cuadrante, \(x>0\) e \(y<0\). Como \(y=x^2-4\), para que \(y<0\) necesitamos \(x^2<4\), es decir, \(0<x<2\).

Así que buscamos una solución con \(x\) entre \(0\) y \(2\).

Retomemos la ecuación original:

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40 = 0.
\]

Intentemos adivinar una solución de la forma \(x = \frac{\sqrt{3}\pm \sqrt{m}}{n}\) o similar.

Otra idea: como la parábola y su rotación se intersecan en el cuarto cuadrante, quizás convenga usar la simetría. La intersección está sobre la bisectriz del ángulo de rotación respecto al origen, es decir, a \(30^\circ\) del eje positivo \(x\). Eso no es exactamente cierto en general, pero las parábolas tienen una simetría especial.

De hecho, hay un argumento geométrico más elegante: si un punto \(P\) está sobre la parábola original y también sobre su rotación de \(60^\circ\), entonces \(P\) y su rotación inversa \(R_{-60^\circ}(P)\) están ambos sobre la parábola original.

Sea \(P=(x,y)\) con \(y=x^2-4\). Su rotación de \(-60^\circ\) es:

\[
P' = (x', y') = \left(\frac{x}{2}+\frac{\sqrt{3}}{2}y,\; -\frac{\sqrt{3}}{2}x+\frac{y}{2}\right).
\]

Y debe cumplir \(y' = x'^2 - 4\). Esto es exactamente lo que ya planteamos.

## 7. Resolución numérica y factorización exacta

Volvamos al polinomio en \(t\):

\[
9t^4 - 162t^3 + 937t^2 - 2108t + 1600 = 0.
\]

Pero recordemos que al elevar al cuadrado introdujimos posiblemente soluciones extrañas. Aun así, vamos a intentar factorizarlo.

Probemos búsqueda de raíces con \(t\) de la forma \(\frac{p}{q}\). Usamos el teorema de la raíz racional.

Posibles raíces racionales: divisores de \(1600\) sobre divisores de \(9\).

Probemos \(t=2\):

\[
9\cdot 16 - 162\cdot 8 + 937\cdot 4 - 2108\cdot 2 + 1600.
\]

\[
144 - 1296 + 3748 - 4216 + 1600.
\]

\[
144-1296 = -1152.
\]

\[
-1152+3748 = 2596.
\]

\[
2596-4216 = -1620.
\]

\[
-1620+1600 = -20.
\]

No.

\(t=1\):

\[
9 - 162 + 937 - 2108 + 1600 = 9-162=-153;\; -153+937=784;\; 784-2108=-1324;\; -1324+1600=276.
\]

No.

\(t=3\):

\[
9\cdot 81 - 162\cdot 27 + 937\cdot 9 - 2108\cdot 3 + 1600.
\]

\[
729 - 4374 + 8433 - 6324 + 1600.
\]

\[
729-4374=-3645;\; -3645+8433=4788;\; 4788-6324=-1536;\; -1536+1600=64.
\]

No.

\(t=4\) ya lo probamos, dio 96.

\(t=5\):

\[
9\cdot 625 - 162\cdot 125 + 937\cdot 25 - 2108\cdot 5 + 1600.
\]

\[
5625 - 20250 + 23425 - 10540 + 1600.
\]

\[
5625-20250=-14625;\; -14625+23425=8800;\; 8800-10540=-1740;\; -1740+1600=-140.
\]

No.

\(t=6\):

\[
9\cdot 1296 - 162\cdot 216 + 937\cdot 36 - 2108\cdot 6 + 1600.
\]

\[
11664 - 34992 + 33732 - 12648 + 1600.
\]

\[
11664-34992=-23328;\; -23328+33732=10404;\; 10404-12648=-2244;\; -2244+1600=-644.
\]

No.

\(t=7\):

\[
9\cdot 2401 - 162\cdot 343 + 937\cdot 49 - 2108\cdot 7 + 1600.
\]

\[
21609 - 55566 + 45913 - 14756 + 1600.
\]

\[
21609-55566=-33957;\; -33957+45913=11956;\; 11956-14756=-2800;\; -2800+1600=-1200.
\]

No.

\(t=8\) lo probamos, \(-1376\).

\(t=10\):

\[
9\cdot 10000 - 162\cdot 1000 + 937\cdot 100 - 2108\cdot 10 + 1600.
\]

\[
90000 - 162000 + 93700 - 21080 + 1600.
\]

\[
90000-162000=-72000;\; -72000+93700=21700;\; 21700-21080=620;\; 620+1600=2220.
\]

No.

Probemos fracciones como \(t=\frac{16}{3}\):

\[
9\left(\frac{16}{3}\right)^4 - 162\left(\frac{16}{3}\right)^3 + 937\left(\frac{16}{3}\right)^2 - 2108\cdot\frac{16}{3} + 1600.
\]

Esto se complica. Mejor usemos un método más sistemático.

## 8. Buscando la solución exacta de manera directa

Volvamos a la ecuación original sin elevar al cuadrado:

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40 = 0.
\]

Podemos intentar encontrar soluciones de la forma \(x = \frac{\sqrt{3} + k}{m}\) o algo así, pero quizá sea más simple notar que la intersección en el cuarto cuadrante probablemente tenga coordenadas sencillas.

Probemos valores de \(x\) entre \(0\) y \(2\) y busquemos cuál anula la ecuación.

Definamos:

\[
f(x) = 3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40.
\]

Evaluemos en \(x=1\):

\[
3 + 2\sqrt{3} - 25 - 6\sqrt{3} + 40
= (3-25+40) + (2\sqrt{3}-6\sqrt{3})
= 18 - 4\sqrt{3}.
\]

Es positivo, ya que \(18 - 4\sqrt{3} \approx 18 - 6.928 = 11.072\).

En \(x=2\):

\[
48 + 16\sqrt{3} - 100 - 12\sqrt{3} + 40
= -12 + 4\sqrt{3} \approx -12 + 6.928 = -5.072.
\]

Hay un cambio de signo entre \(1\) y \(2\), así que existe una raíz en ese intervalo.

Intentemos \(x=\sqrt{3}\approx 1.732\):

Dio \(-8\) antes. Entonces la raíz está entre \(1\) y \(\sqrt{3}\).

Probemos \(x=3/2\):

\[
3\cdot(3/2)^4 + 2\sqrt{3}\cdot(3/2)^3 - 25\cdot(3/2)^2 - 6\sqrt{3}\cdot(3/2) + 40.
\]

\[
(3/2)^4 = 81/16,\quad 3\cdot 81/16 = 243/16.
\]

\[
(3/2)^3 = 27/8,\quad 2\sqrt{3}\cdot 27/8 = 27\sqrt{3}/4.
\]

\[
(3/2)^2 = 9/4,\quad -25\cdot 9/4 = -225/4.
\]

\[
-6\sqrt{3}\cdot 3/2 = -9\sqrt{3}.
\]

Sumamos:

\[
\frac{243}{16} + \frac{27\sqrt{3}}{4} - \frac{225}{4} - 9\sqrt{3} + 40.
\]

Ponemos denominador \(16\):

\[
\frac{243}{16} + \frac{108\sqrt{3}}{16} - \frac{900}{16} - \frac{144\sqrt{3}}{16} + \frac{640}{16}.
\]

\[
= \frac{243 - 900 + 640}{16} + \frac{108\sqrt{3} - 144\sqrt{3}}{16}.
\]

\[
243 - 900 + 640 = -17.
\]

\[
108\sqrt{3} - 144\sqrt{3} = -36\sqrt{3}.
\]

Entonces:

\[
f(3/2) = \frac{-17 - 36\sqrt{3}}{16}.
\]

Es claramente negativo.

Probemos \(x=4/3 \approx 1.333\):

\[
(4/3)^4 = 256/81,\quad 3\cdot = 256/27.
\]

\[
(4/3)^3 = 64/27,\quad 2\sqrt{3}\cdot = 128\sqrt{3}/27.
\]

\[
(4/3)^2 = 16/9,\quad -25\cdot 16/9 = -400/9.
\]

\[
-6\sqrt{3}\cdot 4/3 = -8\sqrt{3}.
\]

\[
f(4/3) = \frac{256}{27} + \frac{128\sqrt{3}}{27} - \frac{400}{9} - 8\sqrt{3} + 40.
\]

Ponemos denominador \(27\):

\[
\frac{256}{27} + \frac{128\sqrt{3}}{27} - \frac{1200}{27} - \frac{216\sqrt{3}}{27} + \frac{1080}{27}.
\]

\[
= \frac{256 - 1200 + 1080}{27} + \frac{128\sqrt{3}-216\sqrt{3}}{27}
= \frac{136}{27} - \frac{88\sqrt{3}}{27}.
\]

Como \(88\sqrt{3} \approx 152.42\), entonces \(136 - 152.42 < 0\). Por tanto \(f(4/3) < 0\).

Probemos \(x=5/4=1.25\):

\[
(5/4)^4 = 625/256,\quad 3\cdot = 1875/256.
\]

\[
(5/4)^3 = 125/64,\quad 2\sqrt{3}\cdot = 125\sqrt{3}/32.
\]

\[
(5/4)^2 = 25/16,\quad -25\cdot 25/16 = -625/16.
\]

\[
-6\sqrt{3}\cdot 5/4 = -15\sqrt{3}/2.
\]

\[
f(5/4) = \frac{1875}{256} + \frac{125\sqrt{3}}{32} - \frac{625}{16} - \frac{15\sqrt{3}}{2} + 40.
\]

Denominador \(256\):

\[
\frac{1875}{256} + \frac{1000\sqrt{3}}{256} - \frac{10000}{256} - \frac{1920\sqrt{3}}{256} + \frac{10240}{256}.
\]

\[
= \frac{1875 - 10000 + 10240}{256} + \frac{1000\sqrt{3}-1920\sqrt{3}}{256}.
\]

\[
1875 - 10000 + 10240 = 2115.
\]

\[
1000\sqrt{3} - 1920\sqrt{3} = -920\sqrt{3}.
\]

\[
f(5/4) = \frac{2115 - 920\sqrt{3}}{256}.
\]

Como \(920\sqrt{3} \approx 1593.5\), entonces \(2115 - 1593.5 > 0\). Es positivo.

Así, la raíz está entre \(5/4\) y \(4/3\).

Sigamos acotando, pero lo importante es encontrar la forma exacta. Probemos una forma tipo \(x = \frac{\sqrt{3} - k}{m}\).

Dado que la raíz está cerca de \(1.3\), probemos formas como:

\[
x = \frac{5-\sqrt{3}}{3} \approx \frac{5-1.732}{3} = \frac{3.268}{3} \approx 1.089.
\]

Muy pequeño.

\[
x = \frac{9-\sqrt{3}}{6} \approx \frac{7.268}{6} \approx 1.211.
\]

\[
x = \frac{7-\sqrt{3}}{4} \approx \frac{5.268}{4} \approx 1.317.
\]

Este está cerca. Probemos \(x = \frac{7-\sqrt{3}}{4}\).

Calculamos \(x^2\):

\[
x^2 = \left(\frac{7-\sqrt{3}}{4}\right)^2 = \frac{49 - 14\sqrt{3} + 3}{16} = \frac{52 - 14\sqrt{3}}{16} = \frac{26 - 7\sqrt{3}}{8}.
\]

Entonces

\[
y = x^2 - 4 = \frac{26 - 7\sqrt{3}}{8} - 4 = \frac{26 - 7\sqrt{3} - 32}{8} = \frac{-6 - 7\sqrt{3}}{8}.
\]

El enunciado sugiere la forma \(\frac{a-\sqrt{b}}{c}\). Aquí tendríamos \(y = \frac{-6 - 7\sqrt{3}}{8}\), que no coincide con la forma \(a-\sqrt{b}\) en el numerador (es \(-6-7\sqrt{3}\), no \(6-\sqrt{147}\)).

Veamos: \(\frac{-6-7\sqrt{3}}{8}\) no tiene la forma \(\frac{a-\sqrt{b}}{c}\) con \(a,b,c\) positivos, porque el término racional es negativo.

Probemos otra forma para \(x\).

Probemos \(x = \frac{\sqrt{21}-3}{4}\). Como \(\sqrt{21}\approx 4.583\), \(x\approx \frac{1.583}{4}\approx 0.395\). Muy pequeño.

Probemos \(x = \frac{\sqrt{15}-1}{4} \approx \frac{3.873-1}{4} = \frac{2.873}{4}\approx 0.718\). Pequeño.

Probemos \(x = \frac{\sqrt{13}+1}{4}\approx \frac{3.606+1}{4}=1.151\).

Probemos \(x = \frac{5-\sqrt{3}}{2}\approx \frac{3.268}{2}=1.634\). Está entre 1.25 y 1.333? No, 1.634 es mayor que 1.333.

La raíz está aproximadamente en... evaluemos numéricamente:

\(f(1.3)\):

\[
x=1.3,\quad x^2=1.69,\quad x^3=2.197,\quad x^4=2.8561.
\]

\[
3x^4 = 8.5683.
\]

\[
2\sqrt{3}x^3 \approx 2\cdot 1.73205\cdot 2.197 = 3.4641\cdot 2.197 \approx 7.6107.
\]

\[
-25x^2 = -42.25.
\]

\[
-6\sqrt{3}x \approx -6\cdot 1.73205\cdot 1.3 = -10.3923\cdot 1.3 = -13.5099.
\]

\[
+40.
\]

Suma:

\[
8.5683 + 7.6107 = 16.179.
\]

\[
16.179 - 42.25 = -26.071.
\]

\[
-26.071 - 13.5099 = -39.5809.
\]

\[
-39.5809 + 40 = 0.4191.
\]

Positivo.

\(f(1.32)\):

\[
x^2 = 1.7424,\quad x^3 = 2.299968,\quad x^4 = 3.03595776.
\]

\[
3x^4 = 9.10787328.
\]

\[
2\sqrt{3}x^3 \approx 3.4641 \cdot 2.299968 \approx 7.966.
\]

\[
-25x^2 = -43.56.
\]

\[
-6\sqrt{3}x \approx -13.7179.
\]

\[
+40.
\]

Suma:

\[
9.1079 + 7.966 = 17.0739.
\]

\[
17.0739 - 43.56 = -26.4861.
\]

\[
-26.4861 - 13.7179 = -40.204.
\]

\[
-40.204 + 40 = -0.204.
\]

Negativo.

Así, la raíz está entre \(1.30\) y \(1.32\), aproximadamente \(1.313\).

Probemos una forma exacta con denominador pequeño. Por ejemplo:

\[
x = \frac{\sqrt{3}}{2} + \frac{1}{3} \approx 0.866 + 0.333 = 1.199.
\]

No.

\[
x = \sqrt{\frac{5}{3}} \approx 1.291.
\]

Probemos \(x = \sqrt{\frac{5}{3}}\):

\[
x^2 = \frac{5}{3},\quad x^3 = \frac{5}{3}\sqrt{\frac{5}{3}},\quad x^4 = \frac{25}{9}.
\]

Entonces:

\[
3x^4 = \frac{25}{3}.
\]

\[
2\sqrt{3}x^3 = 2\sqrt{3}\cdot \frac{5}{3}\sqrt{\frac{5}{3}}.
\]

Esto es un poco engorroso, pero evaluemos numéricamente:

\(x\approx 1.29099\). Ya vimos que \(f(1.29)\) da cercano a cero.

Probemos una forma con denominador \(4\) o \(5\).

Probemos \(x = \frac{5+\sqrt{3}}{5} \approx \frac{6.732}{5}=1.3464\). Demasiado grande.

Probemos \(x = \frac{4+\sqrt{3}}{4} \approx 1.433\). Grande.

Probemos \(x = \frac{3+\sqrt{3}}{3} \approx 1.577\). Grande.

Necesitamos algo alrededor de \(1.313\).

Probemos \(x = \frac{5\sqrt{3}-3}{5} \approx \frac{8.660-3}{5}=1.132\). Pequeño.

Probemos \(x = \frac{2+\sqrt{3}}{3} \approx 1.244\). Pequeño.

Probemos \(x = \frac{7-\sqrt{3}}{4}\) ya probado, dio \(1.317\). Cerca.

Veamos \(x = \frac{7-\sqrt{3}}{4} \approx 1.31699\). Evaluamos numéricamente:

\[
x^2 = \frac{26-7\sqrt{3}}{8}.
\]

Calculemos \(26 - 7\sqrt{3}\). \(\sqrt{3}\approx 1.73205\), \(7\sqrt{3}\approx 12.12435\).

\[
26 - 12.12435 = 13.87565.
\]

\[
x^2 \approx 13.87565/8 = 1.734456.
\]

\[
x^3 = x\cdot x^2 \approx 1.31699 \cdot 1.734456 \approx 2.2846.
\]

\[
x^4 = (x^2)^2 \approx 1.734456^2 \approx 3.0083.
\]

Ahora \(f\):

\[
3x^4 \approx 9.025.
\]

\[
2\sqrt{3}x^3 \approx 3.4641 \cdot 2.2846 \approx 7.913.
\]

\[
-25x^2 \approx -43.361.
\]

\[
-6\sqrt{3}x \approx -10.3923 \cdot 1.31699 \approx -13.686.
\]

\[
+40.
\]

Suma:

\[
9.025 + 7.913 = 16.938.
\]

\[
16.938 - 43.361 = -26.423.
\]

\[
-26.423 - 13.686 = -40.109.
\]

\[
-40.109 + 40 = -0.109.
\]

Negativo, cercano a cero.

Probemos \(x = \frac{10-\sqrt{3}}{6} \approx \frac{8.268}{6}=1.378\). Muy grande.

Probemos \(x = \frac{8-\sqrt{3}}{5} \approx \frac{6.268}{5}=1.2536\). Pequeño.

Probemos \(x = \frac{9-\sqrt{3}}{6}\approx 1.211\) ya descartado.

Probemos \(x = \frac{13-3\sqrt{3}}{6}\approx \frac{13-5.196}{6}=1.3007\). Cerca.

Probemos \(x = \frac{13-3\sqrt{3}}{6}\):

\[
x^2 = \frac{169 - 78\sqrt{3} + 27}{36} = \frac{196 - 78\sqrt{3}}{36} = \frac{98 - 39\sqrt{3}}{18}.
\]

Entonces

\[
y = x^2 - 4 = \frac{98 - 39\sqrt{3}}{18} - 4 = \frac{98 - 39\sqrt{3} - 72}{18} = \frac{26 - 39\sqrt{3}}{18}.
\]

La forma \(\frac{26 - 39\sqrt{3}}{18}\) podría escribirse como \(\frac{26 - \sqrt{4563}}{18}\). El enunciado dice \(\frac{a-\sqrt{b}}{c}\), con \(a,b,c\) positivos. Aquí \(a=26\), \(b=4563\), \(c=18\). Pero \(a\) y \(c\) deben ser relativamente primos: \(\gcd(26,18)=2\), así que no sirve directamente. Además, no sabemos si este \(x\) es exactamente la raíz.

Probemos con \(x = \frac{5-\sqrt{3}}{2}\):

Aproximadamente \(1.634\), no es la raíz.

Mejor busquemos la raíz exacta resolviendo la ecuación en \(t\) de manera más inteligente.

## 9. Reducción del problema con una sustitución trigonométrica o algebraica

Recordemos la ecuación original en \(x\):

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40 = 0. \tag{*}
\]

Intentemos descomponerla en dos cuadráticas con coeficientes con \(\sqrt{3}\). Supongamos:

\[
(\sqrt{3}x^2 + px + q)(\sqrt{3}x^2 + rx + s) = 0.
\]

Ya intentamos y obtuvimos \(p+r=2\), \(pr=-7\). Entonces \(p\) y \(r\) son

\[
1 \pm 2\sqrt{2}.
\]

No obstante, sigamos. Tenemos también

\[
ps + qr = -6\sqrt{3},\qquad qs=40.
\]

Con \(p = 1+2\sqrt{2}\) y \(r = 1-2\sqrt{2}\), resolvamos:

\[
(1+2\sqrt{2})s + (1-2\sqrt{2})q = -6\sqrt{3}.
\]

Sabemos \(qs=40\). Entonces \(q = 40/s\). Sustituyendo:

\[
(1+2\sqrt{2})s + (1-2\sqrt{2})\frac{40}{s} = -6\sqrt{3}.
\]

Multiplicando por \(s\):

\[
(1+2\sqrt{2})s^2 + 6\sqrt{3}s + 40(1-2\sqrt{2}) = 0.
\]

Esto da una cuadrática en \(s\), lo cual es factible pero engorroso. La raíz \(s\) resultaría con raíces anidadas.

Quizá haya una factorización más simple. Probemos:

\[
(\sqrt{3}x^2 + ax + b)(\sqrt{3}x^2 + cx + d)
\]

con \(a+c=2\), \(ac=-7\), \(bd=40\), \(ad+bc=-6\sqrt{3}\).

Ya vimos \(a = 1+2\sqrt{2}\), \(c = 1-2\sqrt{2}\).

Entonces la ecuación \(bd=40\) y \(ad+bc=-6\sqrt{3}\). Podemos despejar \(b\) y \(d\) para que todo encaje. Veamos si hay soluciones sencillas.

De \(ad+bc = a d + b c = -6\sqrt{3}\). Sustituimos \(c=2-a\).

Entonces:

\[
a d + b(2-a) = -6\sqrt{3}.
\]

Y \(bd=40\), así que \(d=40/b\) (suponiendo \(b\ne 0\)).

Entonces:

\[
a\frac{40}{b} + b(2-a) = -6\sqrt{3}.
\]

Multiplicamos por \(b\):

\[
40a + b^2(2-a) = -6\sqrt{3}b.
\]

Esto es cuadrático en \(b\):

\[
(2-a)b^2 + 6\sqrt{3}b + 40a = 0.
\]

Con \(a = 1+2\sqrt{2}\):

\[
(2 - (1+2\sqrt{2})) = 1 - 2\sqrt{2}.
\]

Entonces:

\[
(1-2\sqrt{2})b^2 + 6\sqrt{3}b + 40(1+2\sqrt{2}) = 0.
\]

El discriminante:

\[
\Delta = (6\sqrt{3})^2 - 4(1-2\sqrt{2})\cdot 40(1+2\sqrt{2}).
\]

\[
(6\sqrt{3})^2 = 108.
\]

Y el producto:

\[
(1-2\sqrt{2})(1+2\sqrt{2}) = 1 - 8 = -7.
\]

Entonces:

\[
4\cdot 40 \cdot (-7) = -1120.
\]

Restamos:

\[
\Delta = 108 - (-1120) = 1228.
\]

\[
b = \frac{-6\sqrt{3} \pm \sqrt{1228}}{2(1-2\sqrt{2})}.
\]

Como \(1228 = 4\cdot 307\), \(\sqrt{1228}=2\sqrt{307}\). Esto introduce \(\sqrt{307}\), poco elegante.

Quizá la solución final tenga \(\sqrt{307}\) en \(b\). Veamos qué \(y\) se obtiene.

La idea es que \(x\) es una raíz de una de las cuadráticas. Por ejemplo:

\[
\sqrt{3}x^2 + (1+2\sqrt{2})x + b = 0.
\]

La raíz positiva entre \(1\) y \(2\) podría venir de aquí.

Pero quizá hay una manera mucho más simple de resolver el problema sin tanta álgebra pesada.

## 10. Enfoque geométrico alternativo

La condición de que \((x,y)\) esté sobre la parábola original \(y=x^2-4\) y su rotación de \(60^\circ\) se puede expresar de forma vectorial.

Sea el punto \(P=(x,y)\). Al rotar \(-60^\circ\), obtenemos \(P'\), que también está sobre la parábola. Es decir:

\[
P' = R_{-60^\circ}P
\]

con \(P\) y \(P'\) en la parábola.

Consideremos la distancia al origen. Para \(P=(x,y)\) sobre la parábola:

\[
r^2 = x^2 + y^2 = x^2 + (x^2-4)^2.
\]

No parece simplificar demasiado.

Otra idea: las dos parábolas son congruentes, rotadas \(60^\circ\). Su intersección tiene 4 puntos, uno de ellos en el cuarto cuadrante. La bisectriz del ángulo entre sus ejes es la recta a \(30^\circ\). Quizá el punto de intersección en el cuarto cuadrante esté sobre la recta \(y = -\tan(30^\circ) x = -\frac{x}{\sqrt{3}}\), es decir, la bisectriz reflecta hacia el cuarto cuadrante.

Supongamos que el punto está en la recta \(y = -x/\sqrt{3}\). Entonces:

\[
y = x^2 - 4 = -\frac{x}{\sqrt{3}}.
\]

Entonces

\[
x^2 + \frac{x}{\sqrt{3}} - 4 = 0.
\]

Multiplicando por \(\sqrt{3}\):

\[
\sqrt{3}x^2 + x - 4\sqrt{3} = 0.
\]

Resolvemos:

\[
x = \frac{-1 \pm \sqrt{1 + 48}}{2\sqrt{3}} = \frac{-1 \pm 7}{2\sqrt{3}}.
\]

La solución positiva:

\[
x = \frac{6}{2\sqrt{3}} = \frac{3}{\sqrt{3}} = \sqrt{3}.
\]

Entonces \(x=\sqrt{3}\), y \(y = x^2-4 = 3-4 = -1\).

Este punto \((\sqrt{3}, -1)\) está en el cuarto cuadrante. Además, \(y=-1\), que en la forma \(\frac{a-\sqrt{b}}{c}\) sería \(a-\sqrt{b} = -c\). Pero \(a\), \(b\), \(c\) son positivos, y \(-1\) no puede escribirse como \(\frac{a-\sqrt{b}}{c}\) con positivos. Entonces quizá no sea la solución buscada, o el punto no está exactamente sobre la bisectriz.

De hecho, \(y=-1\) no coincide con la forma pedida. Por tanto, el punto de intersección no está sobre la bisectriz.

## 11. Volviendo a la ecuación cuadrática en \(t\)

La ecuación en \(t=x^2\) era:

\[
9t^4 - 162t^3 + 937t^2 - 2108t + 1600 = 0.
\]

Podemos intentar factorizarla numéricamente. Las raíces en \(t\) corresponden a las intersecciones. Para el cuarto cuadrante, necesitamos \(0<t<4\) y \(x>0\), \(y=x^2-4<0\), es decir, \(t<4\).

Probemos si \(t\) es de la forma sencilla. De la evaluación numérica, \(x\approx 1.313\), así que \(t = x^2 \approx 1.724\).

Probemos \(t = 7/4 = 1.75\):

\[
9\cdot(7/4)^4 - 162\cdot(7/4)^3 + 937\cdot(7/4)^2 - 2108\cdot(7/4) + 1600.
\]

Calculamos:

\[
(7/4)^4 = 2401/256,\quad 9\cdot = 21609/256.
\]

\[
(7/4)^3 = 343/64,\quad -162\cdot = -55566/64 = -222264/256.
\]

\[
(7/4)^2 = 49/16,\quad 937\cdot = 45913/16 = 734608/256.
\]

\[
-2108\cdot 7/4 = -3689.
\]

Ponemos \(-3689\) con denominador \(256\): \(-944384/256\).

\[
1600 = 409600/256.
\]

Suma de numeradores:

\[
21609 - 222264 + 734608 - 944384 + 409600.
\]

\[
21609 - 222264 = -200655.
\]

\[
-200655 + 734608 = 533953.
\]

\[
533953 - 944384 = -410431.
\]

\[
-410431 + 409600 = -831.
\]

No es cero. Cercano pero no exacto.

Probemos \(t = 9/5 = 1.8\):

Primero calculemos la función en \(t=1.8\) numéricamente:

\[
t^2 = 3.24,\quad t^3 = 5.832,\quad t^4 = 10.4976.
\]

\[
9t^4 = 94.4784.
\]

\[
-162t^3 = -944.784.
\]

\[
937t^2 = 3036. \quad (3.24\cdot 937 = 3036 - 0.01\cdot937? Revisemos: 937\cdot3=2811; 937\cdot0.24=224.88; total 3035.88.)
\]

\[
-2108t = -3794.4.
\]

\[
+1600.
\]

Suma:

\[
94.4784 - 944.784 + 3035.88 - 3794.4 + 1600.
\]

\[
94.4784 - 944.784 = -850.3056.
\]

\[
-850.3056 + 3035.88 = 2185.5744.
\]

\[
2185.5744 - 3794.4 = -1608.8256.
\]

\[
-1608.8256 + 1600 = -8.8256.
\]

Negativo.

Entonces la raíz en \(t\) está entre \(1.75\) y \(1.8\). La raíz en \(x\) es \(\sqrt{t}\approx 1.315\).

Probemos \(t = 7/4 + 831\) ... mejor busquemos una forma con radicales.

Intentemos \(t = \frac{5+\sqrt{3}}{4}\approx \frac{6.732}{4}=1.683\). Muy pequeño.

\(t = \frac{9-\sqrt{3}}{4} \approx \frac{7.268}{4}=1.817\). Cerca.

Probemos \(t = \frac{9-\sqrt{3}}{4}\). Calculamos si es raíz del polinomio en \(t\). Si \(t\) es raíz, entonces \(x=\sqrt{t}\) es la intersección.

Tenemos \(t = \frac{9-\sqrt{3}}{4}\). Entonces:

\[
t^2 = \frac{81 - 18\sqrt{3} + 3}{16} = \frac{84 - 18\sqrt{3}}{16} = \frac{42 - 9\sqrt{3}}{8}.
\]

\[
t^3 = t\cdot t^2 = \left(\frac{9-\sqrt{3}}{4}\right)\left(\frac{42 - 9\sqrt{3}}{8}\right).
\]

Numerador:

\[
(9-\sqrt{3})(42 - 9\sqrt{3}) = 9\cdot 42 - 81\sqrt{3} - 42\sqrt{3} + 9\cdot 3.
\]

\[
= 378 - 123\sqrt{3} + 27 = 405 - 123\sqrt{3}.
\]

Denominador \(32\). Entonces:

\[
t^3 = \frac{405 - 123\sqrt{3}}{32}.
\]

\[
t^4 = (t^2)^2 = \left(\frac{42 - 9\sqrt{3}}{8}\right)^2 = \frac{(42 - 9\sqrt{3})^2}{64}.
\]

\[
(42 - 9\sqrt{3})^2 = 1764 - 2\cdot 42\cdot 9\sqrt{3} + 81\cdot 3 = 1764 - 756\sqrt{3} + 243 = 2007 - 756\sqrt{3}.
\]

Entonces:

\[
t^4 = \frac{2007 - 756\sqrt{3}}{64}.
\]

Ahora evaluamos el polinomio \(P(t) = 9t^4 - 162t^3 + 937t^2 - 2108t + 1600\).

Calculamos cada término con denominador \(64\):

- \(9t^4 = \frac{9(2007 - 756\sqrt{3})}{64} = \frac{18063 - 6804\sqrt{3}}{64}\).

- \(-162t^3 = -162\cdot\frac{405 - 123\sqrt{3}}{32} = -\frac{162(405 - 123\sqrt{3})}{32} = -\frac{81(405 - 123\sqrt{3})}{16} = -\frac{81(405 - 123\sqrt{3})\cdot 4}{64} = -\frac{324(405 - 123\sqrt{3})}{64}\).

Calculamos \(324\cdot 405 = 131220\), y \(324\cdot 123 = 39852\).

Entonces:

\[
-162t^3 = \frac{-131220 + 39852\sqrt{3}}{64}.
\]

- \(937t^2 = 937\cdot\frac{42 - 9\sqrt{3}}{8} = \frac{937(42 - 9\sqrt{3})}{8} = \frac{937(42 - 9\sqrt{3})\cdot 8}{64} = \frac{7496(42 - 9\sqrt{3})}{64}\).

Calculamos \(7496\cdot 42\):

\[
7496\cdot 42 = 7496\cdot 40 + 7496\cdot 2 = 299840 + 14992 = 314832.
\]

\(7496\cdot 9 = 67464\).

Entonces:

\[
937t^2 = \frac{314832 - 67464\sqrt{3}}{64}.
\]

- \(-2108t = -2108\cdot\frac{9-\sqrt{3}}{4} = -\frac{2108(9-\sqrt{3})}{4} = -\frac{2108(9-\sqrt{3})\cdot 16}{64} = -\frac{33728(9-\sqrt{3})}{64}\).

Calculamos \(33728\cdot 9 = 303552\), y \(33728\cdot 1 = 33728\).

Entonces:

\[
-2108t = \frac{-303552 + 33728\sqrt{3}}{64}.
\]

- \(1600 = \frac{1600\cdot 64}{64} = \frac{102400}{64}\).

Sumamos todos los numeradores, separando parte racional y parte con \(\sqrt{3}\).

Parte racional:

\[
18063 - 131220 + 314832 - 303552 + 102400.
\]

Calculamos paso a paso:

\[
18063 - 131220 = -113157.
\]

\[
-113157 + 314832 = 201675.
\]

\[
201675 - 303552 = -101877.
\]

\[
-101877 + 102400 = 523.
\]

Parte con \(\sqrt{3}\):

\[
-6804 + 39852 - 67464 + 33728.
\]

\[
-6804 + 39852 = 33048.
\]

\[
33048 - 67464 = -34416.
\]

\[
-34416 + 33728 = -688.
\]

Entonces:

\[
P(t) = \frac{523 - 688\sqrt{3}}{64} \neq 0.
\]

No es raíz. Muy cercano, pero no exacto.

Probemos \(t = \frac{11-\sqrt{3}}{5}\). Numéricamente \(\sqrt{3}\approx 1.732\), entonces \(t\approx (11-1.732)/5 = 9.268/5 = 1.8536\). Demasiado grande.

Probemos \(t = \frac{7+\sqrt{3}}{5} \approx (8.732)/5 = 1.7464\). Cerca.

Evaluemos \(t = \frac{7+\sqrt{3}}{5}\). Podríamos hacer lo mismo, pero quizá haya una forma más sistemática.

Mejor usemos un CAS mental: busquemos la factorización del polinomio en \(t\) sobre \(\mathbb{Q}(\sqrt{3})\) o similar.

Retomemos la ecuación original en \(x\):

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40 = 0.
\]

Probemos la factorización:

\[
(\sqrt{3}x^2 + \alpha x + \beta)(\sqrt{3}x^2 + \gamma x + \delta).
\]

Con \(\alpha + \gamma = 2\), \(\alpha\gamma = -7\), \(\beta\delta = 40\), \(\alpha\delta + \beta\gamma = -6\sqrt{3}\).

Ya vimos \(\alpha = 1+2\sqrt{2}\), \(\gamma = 1-2\sqrt{2}\).

Resolvamos \(\beta\) y \(\delta\) de forma exacta. Tenemos:

\[
\alpha\delta + \beta\gamma = -6\sqrt{3}.
\]

Sustituimos \(\gamma = 2-\alpha\):

\[
\alpha\delta + \beta(2-\alpha) = -6\sqrt{3}.
\]

Y \(\beta\delta = 40\).

Despejamos \(\delta = 40/\beta\):

\[
\alpha\frac{40}{\beta} + \beta(2-\alpha) = -6\sqrt{3}.
\]

Multiplicamos por \(\beta\):

\[
40\alpha + (2-\alpha)\beta^2 = -6\sqrt{3}\beta.
\]

Es decir:

\[
(2-\alpha)\beta^2 + 6\sqrt{3}\beta + 40\alpha = 0.
\]

Con \(\alpha = 1+2\sqrt{2}\), \(2-\alpha = 1-2\sqrt{2}\).

La fórmula cuadrática para \(\beta\):

\[
\beta = \frac{-6\sqrt{3} \pm \sqrt{108 - 4(1-2\sqrt{2})\cdot 40(1+2\sqrt{2})}}{2(1-2\sqrt{2})}.
\]

Simplifiquemos el discriminante:

\[
(1-2\sqrt{2})(1+2\sqrt{2}) = 1 - 8 = -7.
\]

\[
4(1-2\sqrt{2})40(1+2\sqrt{2}) = 4\cdot 40\cdot (-7) = -1120.
\]

Entonces:

\[
\Delta = 108 - (-1120) = 1228.
\]

Así:

\[
\beta = \frac{-6\sqrt{3} \pm \sqrt{1228}}{2(1-2\sqrt{2})}.
\]

Esto es exacto pero poco amigable.

Aunque el enunciado pide \(y\) con la forma \(\frac{a-\sqrt{b}}{c}\), quizá \(b\) contenga el \(1228\) pero simplificado.

Veamos cuál es \(y\) para la raíz positiva. La raíz \(x\) de la cuadrática:

\[
\sqrt{3}x^2 + \alpha x + \beta = 0.
\]

Entonces:

\[
x = \frac{-\alpha \pm \sqrt{\alpha^2 - 4\sqrt{3}\beta}}{2\sqrt{3}}.
\]

Como \(y=x^2-4\), tendríamos:

\[
y = \left(\frac{-\alpha + \sqrt{\alpha^2 - 4\sqrt{3}\beta}}{2\sqrt{3}}\right)^2 - 4.
\]

Esto se vuelve muy complejo.

Quizá el problema tiene una solución más limpia de la que estamos hallando. Tal vez cometí un error algebraico.

## 12. Revisión de la ecuación de la imagen

Volvamos a verificar. La parábola original: \(y=x^2-4\).

Rotación de \(60^\circ\) antihorario:

\[
(x,y) \mapsto (X,Y) = \left(\frac{x}{2} - \frac{\sqrt{3}}{2}y,\; \frac{\sqrt{3}}{2}x + \frac{y}{2}\right).
\]

Entonces la imagen está formada por \((X,Y)\) tales que existe \((x,y)\) con \(y=x^2-4\) y

\[
X = \frac{x}{2} - \frac{\sqrt{3}}{2}y,\qquad Y = \frac{\sqrt{3}}{2}x + \frac{y}{2}.
\]

Para encontrar la ecuación de la imagen, invertimos la rotación. La rotación inversa de \(60^\circ\) antihorario es \(60^\circ\) horario:

\[
x = X\cos 60^\circ + Y\sin 60^\circ = \frac{X}{2} + \frac{\sqrt{3}}{2}Y,
\]

\[
y = -X\sin 60^\circ + Y\cos 60^\circ = -\frac{\sqrt{3}}{2}X + \frac{Y}{2}.
\]

Luego imponemos \(y = x^2 - 4\):

\[
-\frac{\sqrt{3}}{2}X + \frac{Y}{2} = \left(\frac{X}{2} + \frac{\sqrt{3}}{2}Y\right)^2 - 4.
\]

Esto coincide con lo que hicimos (llamando \(X,Y\) a las coordenadas finales).

Ahora, para la intersección, usamos además \(Y = X^2 - 4\). Sustituimos \(Y = X^2 - 4\) en la ecuación anterior.

Primero, la izquierda:

\[
-\frac{\sqrt{3}}{2}X + \frac{X^2 - 4}{2}.
\]

La derecha:

\[
\left(\frac{X}{2} + \frac{\sqrt{3}}{2}(X^2-4)\right)^2 - 4.
\]

Dentro del paréntesis:

\[
\frac{X}{2} + \frac{\sqrt{3}}{2}X^2 - 2\sqrt{3}.
\]

Elevamos al cuadrado:

\[
\left(\frac{X}{2} + \frac{\sqrt{3}}{2}X^2 - 2\sqrt{3}\right)^2.
\]

Esto es lo que expandimos antes y llegamos a:

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40 = 0.
\]

Verifiquemos la expansión.

Sea \(A = \frac{x}{2}\), \(B = \frac{\sqrt{3}}{2}x^2\), \(C = -2\sqrt{3}\).

\[
(A+B+C)^2 = A^2 + B^2 + C^2 + 2AB + 2AC + 2BC.
\]

\[
A^2 = \frac{x^2}{4}.
\]

\[
B^2 = \frac{3}{4}x^4.
\]

\[
C^2 = 4\cdot 3 = 12.
\]

\[
2AB = 2\cdot \frac{x}{2}\cdot \frac{\sqrt{3}}{2}x^2 = \frac{\sqrt{3}}{2}x^3.
\]

\[
2AC = 2\cdot \frac{x}{2}\cdot (-2\sqrt{3}) = -2\sqrt{3}x.
\]

\[
2BC = 2\cdot \frac{\sqrt{3}}{2}x^2 \cdot (-2\sqrt{3}) = -2\cdot 3 x^2 = -6x^2.
\]

Sumamos:

\[
\frac{3}{4}x^4 + \frac{\sqrt{3}}{2}x^3 + \frac{x^2}{4} - 6x^2 - 2\sqrt{3}x + 12.
\]

Simplificamos \(x^2\):

\[
\frac{x^2}{4} - 6x^2 = \frac{x^2 - 24x^2}{4} = -\frac{23x^2}{4}.
\]

Entonces el cuadrado es:

\[
\frac{3x^4}{4} + \frac{\sqrt{3}}{2}x^3 - \frac{23x^2}{4} - 2\sqrt{3}x + 12.
\]

Restamos \(4\):

\[
\frac{3x^4}{4} + \frac{\sqrt{3}}{2}x^3 - \frac{23x^2}{4} - 2\sqrt{3}x + 8.
\]

Esta es la derecha. La izquierda es:

\[
-\frac{\sqrt{3}}{2}x + \frac{x^2 - 4}{2} = -\frac{\sqrt{3}}{2}x + \frac{x^2}{2} - 2.
\]

Igualamos:

\[
-\frac{\sqrt{3}}{2}x + \frac{x^2}{2} - 2
=
\frac{3x^4}{4} + \frac{\sqrt{3}}{2}x^3 - \frac{23x^2}{4} - 2\sqrt{3}x + 8.
\]

Multiplicamos por \(4\):

\[
-2\sqrt{3}x + 2x^2 - 8
=
3x^4 + 2\sqrt{3}x^3 - 23x^2 - 8\sqrt{3}x + 32.
\]

Pasamos todo a la izquierda:

\[
-2\sqrt{3}x + 2x^2 - 8 - 3x^4 - 2\sqrt{3}x^3 + 23x^2 + 8\sqrt{3}x - 32 = 0.
\]

Simplificamos:

\[
-3x^4 - 2\sqrt{3}x^3 + 25x^2 + 6\sqrt{3}x - 40 = 0.
\]

Multiplicamos por \(-1\):

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40 = 0.
\]

Coincide con lo anterior. Bien.

## 13. Buscando soluciones por inspección con formas radicales

La raíz en \(x\) está cerca de \(1.315\). Intentemos formas como:

\[
x = \frac{\sqrt{3}+\sqrt{5}}{2} \approx \frac{1.732+2.236}{2} = 1.984. \quad \text{Grande}.
\]

\[
x = \frac{\sqrt{5}-\sqrt{3}}{2} \approx \frac{0.504}{2}=0.252. \quad \text{Pequeño}.
\]

\[
x = \frac{3-\sqrt{2}}{1?} \approx 1.586. \quad \text{Grande}.
\]

\[
x = \frac{4-\sqrt{3}}{2} \approx \frac{2.268}{2}=1.134.
\]

\[
x = \frac{8-\sqrt{3}}{5} \approx 1.2536.
\]

\[
x = \frac{11-2\sqrt{3}}{5} \approx \frac{11-3.464}{5}=1.507.
\]

\[
x = \frac{6-\sqrt{3}}{4} \approx 1.067.
\]

\[
x = \frac{9-2\sqrt{3}}{4} \approx \frac{5.536}{4}=1.384.
\]

\[
x = \frac{7-2\sqrt{3}}{3} \approx \frac{3.536}{3}=1.179.
\]

\[
x = \frac{5-\sqrt{7}}{2} \approx \frac{5-2.646}{2}=1.177.
\]

\[
x = \frac{6-\sqrt{7}}{3} \approx \frac{3.354}{3}=1.118.
\]

\[
x = \frac{9-\sqrt{7}}{5} \approx \frac{6.354}{5}=1.271.
\]

\[
x = \frac{11-\sqrt{7}}{6} \approx \frac{8.354}{6}=1.392.
\]

Probemos \(x = \frac{9-\sqrt{7}}{5}\approx 1.2708\). Evaluemos si es raíz. Aunque el enunciado pide \(y\) con \(\sqrt{b}\), donde \(b\) podría ser \(7\) u otro. Pero no sabemos.

Mejor resolvamos el sistema con una herramienta mental más robusta.

## 14. Uso de Gröbner / eliminación

Tenemos dos ecuaciones:

\[
y = x^2 - 4, \tag{1}
\]

\[
-\sqrt{3}x + y = \frac{1}{2}(x+\sqrt{3}y)^2 - 8? \quad \text{Revisemos}.
\]

Mejor usemos la forma intermedia:

\[
-\frac{\sqrt{3}}{2}x + \frac{y}{2} = \left(\frac{x}{2}+\frac{\sqrt{3}}{2}y\right)^2 - 4. \tag{2}
\]

Multiplicamos (2) por \(4\):

\[
-2\sqrt{3}x + 2y = (x+\sqrt{3}y)^2 - 16.
\]

Es decir:

\[
x^2 + 2\sqrt{3}xy + 3y^2 + 2\sqrt{3}x - 2y - 16 = 0. \tag{2'}
\]

Sustituimos \(y=x^2-4\) en (2'):

\[
x^2 + 2\sqrt{3}x(x^2-4) + 3(x^2-4)^2 + 2\sqrt{3}x - 2(x^2-4) - 16 = 0.
\]

Expandimos:

\[
x^2 + 2\sqrt{3}x^3 - 8\sqrt{3}x + 3x^4 - 24x^2 + 48 + 2\sqrt{3}x - 2x^2 + 8 - 16 = 0.
\]

Simplificamos:

\[
3x^4 + 2\sqrt{3}x^3 + (x^2 - 24x^2 - 2x^2) + (-8\sqrt{3}x + 2\sqrt{3}x) + (48 + 8 - 16) = 0.
\]

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40 = 0.
\]

De acuerdo. Correcto.

## 15. Resolviendo la cuártica en \(x\)

Podemos intentar una sustitución \(u = x + \frac{1}{x}\) o similar, pero el término \(\sqrt{3}\) complica.

Otra idea: dividir la ecuación por \(x^2\):

\[
3x^2 + 2\sqrt{3}x - 25 - \frac{6\sqrt{3}}{x} + \frac{40}{x^2} = 0.
\]

Agrupamos:

\[
3\left(x^2 + \frac{40}{3x^2}\right) + 2\sqrt{3}\left(x - \frac{3}{x}\right) - 25 = 0.
\]

Hmm, \(x^2 + \frac{40}{3x^2}\) no es simétrico.

Probemos con \(x = \sqrt{t}\), pero ya vimos que la cuártica en \(t\) no factoriza fácil.

## 16. Búsqueda numérica más precisa y reconocimiento de patrones

Estimemos la raíz con más precisión para intentar reconocer su forma.

Sabemos que \(f(1.3) \approx 0.4191\) y \(f(1.32)\approx -0.204\). Hagamos interpolación lineal:

La raíz aproximada \(x_0 \approx 1.3 + \frac{0.4191}{0.4191+0.204}\cdot 0.02 = 1.3 + \frac{0.4191}{0.6231}\cdot 0.02 \approx 1.3 + 0.01345 = 1.31345\).

Calculemos \(f(1.3135)\):

\[
x = 1.3135,\quad x^2 \approx 1.72528,\quad x^3 \approx 2.26618,\quad x^4 \approx 2.97672.
\]

\[
3x^4 \approx 8.93016.
\]

\[
2\sqrt{3}x^3 \approx 3.46410 \cdot 2.26618 \approx 7.85043.
\]

\[
-25x^2 \approx -43.13198.
\]

\[
-6\sqrt{3}x \approx -10.39230 \cdot 1.31350 \approx -13.65028.
\]

\[
+40.
\]

Suma:

\[
8.93016 + 7.85043 = 16.78059.
\]

\[
16.78059 - 43.13198 = -26.35139.
\]

\[
-26.35139 - 13.65028 = -40.00167.
\]

\[
-40.00167 + 40 = -0.00167.
\]

Muy cercano a cero. Entonces \(x \approx 1.31349\).

\(y = x^2 - 4 \approx 1.72528 - 4 = -2.27472\).

El enunciado dice:

\[
y = \frac{a - \sqrt{b}}{c}.
\]

Con \(a,b,c\) enteros positivos y \(a,c\) relativamente primos. Como \(y\approx -2.27472\), entonces \(\frac{a-\sqrt{b}}{c} \approx -2.27472\).

Entonces \(a-\sqrt{b} < 0\), así que \(\sqrt{b} > a\). Tiene sentido.

Probemos \(b=3\): \(\sqrt{3}\approx 1.73205\). Si \(a=8\), \(a-\sqrt{3}\approx 6.268\), dividido por \(c\approx -2.27472\) daría \(c\) negativo, no sirve.

Reordenamos:

\[
\frac{a-\sqrt{b}}{c} = -2.27472.
\]

Entonces:

\[
a - \sqrt{b} = -2.27472 c.
\]

Como \(a\) es positivo, por ejemplo si \(a=2\), \(a-\sqrt{b}\approx -2.27472c\). Si \(c=1\), \(a-\sqrt{b}\approx -2.27472\), entonces \(\sqrt{b} \approx a+2.27472\).

Probemos \(b\) cuadrados más cercanos. Si \(a=1\), \(\sqrt{b}\approx 3.27472\), \(b\approx 10.72\), no entero. Si \(a=2\), \(\sqrt{b}\approx 4.27472\), \(b\approx 18.27\). Si \(a=3\), \(\sqrt{b}\approx 5.27472\), \(b\approx 27.82\). Si \(a=4\), \(\sqrt{b}\approx 6.27472\), \(b\approx 39.37\).

Probemos \(c=2\): \(a-\sqrt{b}\approx -4.54944\). Si \(a=2\), \(\sqrt{b}\approx 6.54944\), \(b\approx 42.9\). Si \(a=3\), \(\sqrt{b}\approx 7.549\), \(b\approx 56.98\). Si \(a=5\), \(\sqrt{b}\approx 9.549\), \(b\approx 91.18\).

Probemos \(c=3\): \(a-\sqrt{b}\approx -6.82416\). Si \(a=2\), \(\sqrt{b}\approx 8.824\), \(b\approx 77.86\). Si \(a=3\), \(\sqrt{b}\approx 9.824\), \(b\approx 96.5\). Si \(a=4\), \(\sqrt{b}\approx 10.824\), \(b\approx 117.16\).

Probemos \(c=4\): \(a-\sqrt{b}\approx -9.09888\). Si \(a=2\), \(\sqrt{b}\approx 11.099\), \(b\approx 123.2\). Si \(a=3\), \(\sqrt{b}\approx 12.099\), \(b\approx 146.4\). Si \(a=5\), \(\sqrt{b}\approx 14.099\), \(b\approx 198.8\).

Probemos \(c=5\): \(a-\sqrt{b}\approx -11.3736\). Si \(a=2\), \(\sqrt{b}\approx 13.3736\), \(b\approx 178.85\). Si \(a=3\), \(\sqrt{b}\approx 14.3736\), \(b\approx 206.6\). Si \(a=4\), \(\sqrt{b}\approx 15.3736\), \(b\approx 236.35\). Si \(a=6\), \(\sqrt{b}\approx 17.3736\), \(b\approx 301.8\).

Probemos \(c=6\): \(a-\sqrt{b}\approx -13.6483\). Si \(a=3\), \(\sqrt{b}\approx 16.6483\), \(b\approx 277.2\). Si \(a=4\), \(\sqrt{b}\approx 17.6483\), \(b\approx 311.5\). Si \(a=5\), \(\sqrt{b}\approx 18.648\), \(b\approx 347.7\).

Probemos \(c=7\): \(a-\sqrt{b}\approx -15.923\). Si \(a=4\), \(\sqrt{b}\approx 19.923\), \(b\approx 396.9\). Si \(a=5\), \(\sqrt{b}\approx 20.923\), \(b\approx 437.8\).

Probemos \(c=8\): \(a-\sqrt{b}\approx -18.1978\). Si \(a=5\), \(\sqrt{b}\approx 23.1978\), \(b\approx 538.1\). Si \(a=6\), \(\sqrt{b}\approx 24.1978\), \(b\approx 585.5\).

Probemos \(c=9\): \(a-\sqrt{b}\approx -20.4725\). Si \(a=6\), \(\sqrt{b}\approx 26.4725\), \(b\approx 700.7\). Si \(a=7\), \(\sqrt{b}\approx 27.4725\), \(b\approx 754.7\).

Probemos \(c=10\): \(a-\sqrt{b}\approx -22.7472\). Si \(a=7\), \(\sqrt{b}\approx 29.7472\), \(b\approx 884.9\). Si \(a=8\), \(\sqrt{b}\approx 30.7472\), \(b\approx 945.3\).

Probemos \(c=11\): \(a-\sqrt{b}\approx -25.0219\). Si \(a=8\), \(\sqrt{b}\approx 33.0219\), \(b\approx 1090.4\).

Esto no converge rápidamente. Tal vez \(b\) no sea tan grande.

Probemos con \(b=13\): \(\sqrt{13}\approx 3.60555\). Para \(c=2\), \(a-\sqrt{13}\approx -4.54944\) implica \(a \approx 3.60555 - 4.54944 = -0.94389\), no positivo.

Para \(c=3\), \(a\approx 3.60555 - 6.82416 = -3.2186\), no.

Para \(c=1\), \(a\approx 3.60555 - 2.27472 = 1.33083\), no entero.

Probemos \(b=21\): \(\sqrt{21}\approx 4.58258\). \(c=2\): \(a\approx 4.58258 - 4.54944 = 0.03314\), no. \(c=3\): \(a\approx 4.58258 - 6.82416 = -2.24\).

Probemos \(b=40\): \(\sqrt{40}\approx 6.32456\). \(c=2\): \(a\approx 6.32456 - 4.54944 = 1.775\), no. \(c=3\): \(a\approx 6.32456 - 6.82416 = -0.4996\).

Probemos \(b=52\): \(\sqrt{52}\approx 7.2111\). \(c=2\): \(a\approx 7.2111 - 4.54944 = 2.6617\). \(c=3\): \(a\approx 7.2111 - 6.82416 = 0.3869\).

Probemos \(b=61\): \(\sqrt{61}\approx 7.8102\). \(c=3\): \(a\approx 7.8102 - 6.82416 = 0.986\). \(c=2\): \(a\approx 7.8102 - 4.54944 = 3.2608\).

Probemos \(b=73\): \(\sqrt{73}\approx 8.5440\). \(c=3\): \(a\approx 8.5440 - 6.82416 = 1.7198\). \(c=2\): \(a\approx 8.5440 - 4.54944 = 3.9946\), muy cerca de 4.

Con \(a=4\), \(b=73\), \(c=2\):

\[
\frac{4 - \sqrt{73}}{2} \approx \frac{4 - 8.5440}{2} = \frac{-4.5440}{2} = -2.2720.
\]

Nuestra \(y\approx -2.2747\). Muy cerca pero no exacto.

Probemos \(b=75\): \(\sqrt{75}\approx 8.66025\). \(a=4\), \(c=2\): \((4-8.66025)/2 = -2.33013\). No.

Probemos \(b=73\), \(a=4\), \(c=2\) da \(-2.2720\). La diferencia es \(0.0027\), que podría deberse a inexactitud numérica, pero la raíz exacta quizá corresponda a \(b=73\).

Probemos \(b=73\), \(a=4\), \(c=2\): \(a+b+c = 4+73+2 = 79\).

Pero antes de concluir, verifiquemos si \(y = \frac{4-\sqrt{73}}{2}\) es exactamente la solución.

Si \(y = \frac{4-\sqrt{73}}{2}\), entonces:

\[
x^2 = y+4 = \frac{4-\sqrt{73}}{2} + 4 = \frac{4-\sqrt{73}+8}{2} = \frac{12-\sqrt{73}}{2}.
\]

Entonces:

\[
x = \sqrt{\frac{12-\sqrt{73}}{2}}.
\]

¿Es esto raíz de la ecuación? Verifiquemos numéricamente:

\[
\sqrt{73} \approx 8.5440037.
\]

\[
y = \frac{4 - 8.5440037}{2} = \frac{-4.5440037}{2} = -2.2720018.
\]

\[
x^2 = y+4 = 1.7279982.
\]

\[
x \approx \sqrt{1.7279982} \approx 1.31453.
\]

Nuestra estimación anterior fue \(x\approx 1.31349\). La diferencia es \(0.001\), algo pequeña pero no despreciable. Puede que no sea exacta.

Probemos \(b=74\): \(\sqrt{74}\approx 8.60233\). No parece entero que encaje.

Probemos \(b=76\): \(\sqrt{76}\approx 8.7178\). \(a=5\), \(c=2\): \((5-8.7178)/2 = -1.8589\). No.

Probemos \(b=79\): \(\sqrt{79}\approx 8.8882\). \(a=5\), \(c=2\): \((5-8.8882)/2=-1.9441\). \(a=6\), \(c=2\): \((6-8.8882)/2=-1.4441\). No.

Probemos \(b=82\): \(\sqrt{82}\approx 9.0554\). \(a=6\), \(c=2\): \((6-9.0554)/2=-1.5277\). \(a=7\), \(c=2\): \((7-9.0554)/2=-1.0277\).

Probemos \(b=85\): \(\sqrt{85}\approx 9.2195\). \(a=7\), \(c=2\): \((7-9.2195)/2=-1.1098\). \(a=8\), \(c=2\): \((8-9.2195)/2=-0.60975\).

Probemos \(b=88\): \(\sqrt{88}\approx 9.3808\). \(a=8\), \(c=2\): \((8-9.3808)/2=-0.6904\).

Probemos \(b=91\): \(\sqrt{91}\approx 9.5394\). \(a=9\), \(c=2\): \((9-9.5394)/2=-0.2697\).

Probemos \(b=97\): \(\sqrt{97}\approx 9.8489\). \(a=10\), \(c=2\): \((10-9.8489)/2=0.0755\). No.

Probemos \(c=3\). \(y\approx -2.2747\). Buscamos \(a-\sqrt{b}\approx -6.82416\).

Probemos \(b=61\): \(\sqrt{61}\approx 7.81025\). \(a = 7.81025 - 6.82416 = 0.986\). \(a=1\): \((1-\sqrt{61})/3 \approx (1-7.81025)/3 = -2.27008\). Muy cerca.

Con \(a=1\), \(b=61\), \(c=3\):

\[
y = \frac{1-\sqrt{61}}{3} \approx \frac{1-7.81025}{3} = \frac{-6.81025}{3} = -2.27008.
\]

Diferencia con \(-2.2747\): \(0.0046\). Cerca, pero no exacto.

Probemos \(b=62\): \(\sqrt{62}\approx 7.8740\). \(a=1\): \((1-7.8740)/3 = -2.2913\). No.

Probemos \(b=59\): \(\sqrt{59}\approx 7.6811\). \(a=1\): \((1-7.6811)/3 = -2.2270\). No.

Probemos \(b=60\): \(\sqrt{60}=2\sqrt{15}\approx 7.7460\). \(a=1\): \((1-7.7460)/3 = -2.2487\). No.

Probemos \(b=65\): \(\sqrt{65}\approx 8.0623\). \(a=1\): \((1-8.0623)/3 = -2.3541\). \(a=2\): \((2-8.0623)/3 = -2.0208\).

Probemos \(b=67\): \(\sqrt{67}\approx 8.1854\). \(a=2\): \((2-8.1854)/3 = -2.0618\). \(a=1\): \((1-8.1854)/3 = -2.3951\).

Probemos \(b=70\): \(\sqrt{70}\approx 8.3666\). \(a=2\): \((2-8.3666)/3 = -2.1222\). \(a=3\): \((3-8.3666)/3 = -1.7889\).

Probemos \(b=71\): \(\sqrt{71}\approx 8.4261\). \(a=2\): \((2-8.4261)/3 = -2.1420\).

Probemos \(b=77\): \(\sqrt{77}\approx 8.7750\). \(a=2\): \((2-8.7750)/3 = -2.2583\). Muy cerca.

Con \(a=2\), \(b=77\), \(c=3\):

\[
y = \frac{2-\sqrt{77}}{3} \approx \frac{2-8.77496}{3} = \frac{-6.77496}{3} = -2.25832.
\]

Diferencia con \(-2.2747\): \(0.0164\). No es tan cercano.

Probemos \(b=78\): \(\sqrt{78}\approx 8.8318\). \(a=2\): \((2-8.8318)/3 = -2.2773\). ¡Muy cerca!

Con \(a=2\), \(b=78\), \(c=3\):

\[
y = \frac{2-\sqrt{78}}{3} \approx \frac{2 - 8.83176}{3} = \frac{-6.83176}{3} = -2.27725.
\]

Diferencia con \(-2.2747\): \(-0.00255\).

Probemos \(b=79\), \(a=3\), \(c=3\): \((3-\sqrt{79})/3 = (3-8.8882)/3 = -1.9627\). No.

Probemos \(b=80\), \(a=3\), \(c=3\): \((3-\sqrt{80})/3 = (3-8.9443)/3 = -1.9814\).

Probemos \(b=81\), \(a=3\), \(c=3\): \((3-9)/3 = -2\). No.

Probemos \(b=82\), \(a=3\), \(c=3\): \((3-\sqrt{82})/3 \approx (3-9.0554)/3 = -2.0185\).

Probemos \(b=83\), \(a=3\), \(c=3\): \((3-\sqrt{83})/3 \approx (3-9.1104)/3 = -2.0368\).

Probemos \(b=84\), \(a=3\), \(c=3\): \((3-\sqrt{84})/3 \approx (3-9.1652)/3 = -2.0551\).

Probemos \(b=85\), \(a=4\), \(c=3\): \((4-\sqrt{85})/3 = (4-9.2195)/3 = -1.7398\).

Probemos \(b=87\), \(a=4\), \(c=3\): \((4-\sqrt{87})/3 = (4-9.3274)/3 = -1.7758\).

Probemos \(b=89\), \(a=4\), \(c=3\): \((4-\sqrt{89})/3 = (4-9.4340)/3 = -1.8113\).

Probemos \(b=90\), \(a=4\), \(c=3\): \((4-\sqrt{90})/3 = (4-9.4868)/3 = -1.8289\).

Probemos \(b=91\), \(a=5\), \(c=3\): \((5-\sqrt{91})/3 = (5-9.5394)/3 = -1.5131\).

Probemos \(b=92\), \(a=5\), \(c=3\): \((5-\sqrt{92})/3 = (5-9.5917)/3 = -1.5306\).

Probemos \(b=93\), \(a=5\), \(c=3\): \((5-\sqrt{93})/3 = (5-9.6437)/3 = -1.5479\).

Probemos \(b=94\), \(a=5\), \(c=3\): \((5-\sqrt{94})/3 = (5-9.6954)/3 = -1.5651\).

Probemos \(b=95\), \(a=6\), \(c=3\): \((6-\sqrt{95})/3 = (6-9.7468)/3 = -1.2489\).

Probemos \(b=96\), \(a=6\), \(c=3\): \((6-\sqrt{96})/3 = (6-9.7980)/3 = -1.2660\).

Probemos \(b=97\), \(a=7\), \(c=3\): \((7-\sqrt{97})/3 = (7-9.8489)/3 = -0.9496\).

Probemos \(b=98\), \(a=7\), \(c=3\): \((7-\sqrt{98})/3 = (7-9.8995)/3 = -0.9665\).

Probemos \(b=100\), \(a=8\), \(c=3\): \((8-10)/3 = -0.6667\).

Probemos \(c=4\): \(a-\sqrt{b}\approx -9.0989\).

Probemos \(b=61\), \(a=1\): \((1-\sqrt{61})/4 = (1-7.81025)/4 = -1.70256\). No.

Necesitamos \(a-\sqrt{b}\approx -9.0989\), así que \(\sqrt{b} \approx a+9.0989\).

Probemos \(a=1\): \(\sqrt{b}\approx 10.0989\), \(b\approx 101.99\). Probemos \(b=102\): \(\sqrt{102}\approx 10.0995\). Entonces \((1-\sqrt{102})/4 \approx (1-10.0995)/4 = -9.0995/4 = -2.27488\). ¡Muy cerca!

Con \(a=1\), \(b=102\), \(c=4\):

\[
y = \frac{1-\sqrt{102}}{4} \approx \frac{1-10.09950}{4} = \frac{-9.09950}{4} = -2.274875.
\]

Nuestra estimación \(y\approx -2.2747\). Diferencia \(0.000175\). ¡Muy prometedor!

Probemos \(b=102\), \(a=1\), \(c=4\). Entonces \(a+b+c = 1+102+4 = 107\).

Verifiquemos si \(y = \frac{1-\sqrt{102}}{4}\) es exactamente la solución.

Entonces:

\[
x^2 = y + 4 = \frac{1-\sqrt{102}}{4} + 4 = \frac{1-\sqrt{102}+16}{4} = \frac{17-\sqrt{102}}{4}.
\]

Entonces:

\[
x = \sqrt{\frac{17-\sqrt{102}}{4}} = \frac{\sqrt{17-\sqrt{102}}}{2}.
\]

Comprobemos si \(x\) satisface la ecuación. Para ello, es más fácil verificar en términos de \(t = x^2\).

Con \(t = \frac{17-\sqrt{102}}{4}\), verifiquemos si satisface el polinomio en \(t\):

\[
9t^4 - 162t^3 + 937t^2 - 2108t + 1600 = 0.
\]

Vamos a calcularlo exactamente.

Sea \(t = \frac{17 - \sqrt{102}}{4}\). Entonces:

\[
t^2 = \frac{(17-\sqrt{102})^2}{16} = \frac{289 - 34\sqrt{102} + 102}{16} = \frac{391 - 34\sqrt{102}}{16}.
\]

\[
t^3 = t \cdot t^2 = \frac{17-\sqrt{102}}{4}\cdot \frac{391 - 34\sqrt{102}}{16} = \frac{(17-\sqrt{102})(391 - 34\sqrt{102})}{64}.
\]

Calculamos el numerador:

\[
17\cdot 391 = 6647.
\]

\[
17\cdot (-34\sqrt{102}) = -578\sqrt{102}.
\]

\[
(-\sqrt{102})\cdot 391 = -391\sqrt{102}.
\]

\[
(-\sqrt{102})\cdot (-34\sqrt{102}) = +34\cdot 102 = 3468.
\]

Sumamos:

\[
6647 + 3468 = 10115.
\]

\[
-578\sqrt{102} - 391\sqrt{102} = -969\sqrt{102}.
\]

Entonces:

\[
t^3 = \frac{10115 - 969\sqrt{102}}{64}.
\]

\[
t^4 = (t^2)^2 = \frac{(391 - 34\sqrt{102})^2}{256}.
\]

Calculamos:

\[
391^2 = 152881.
\]

\[
2\cdot 391 \cdot 34 = 782\cdot 34? \quad 391\cdot 34 = 13294,\quad 2\cdot 13294 = 26588.
\]

Así que \(-2\cdot 391\cdot 34\sqrt{102} = -26588\sqrt{102}\).

\[
(34\sqrt{102})^2 = 1156\cdot 102 = 117912.
\]

Sumamos:

\[
152881 + 117912 = 270793.
\]

Entonces:

\[
t^4 = \frac{270793 - 26588\sqrt{102}}{256}.
\]

Ahora evaluamos \(P(t) = 9t^4 - 162t^3 + 937t^2 - 2108t + 1600\).

Usamos denominador común \(256\):

- \(9t^4 = \frac{9(270793 - 26588\sqrt{102})}{256} = \frac{2437137 - 239292\sqrt{102}}{256}\).

- \(-162t^3 = -162\cdot\frac{10115 - 969\sqrt{102}}{64} = -\frac{162(10115 - 969\sqrt{102})}{64} = -\frac{648(10115 - 969\sqrt{102})}{256}\).

Calculamos \(648\cdot 10115\):

\[
10115\cdot 648 = 10115\cdot (600+48) = 6069000 + 485520 = 6554520.
\]

\(648\cdot 969 = 648\cdot (1000-31) = 648000 - 20088 = 627912\).

Entonces:

\[
-162t^3 = \frac{-6554520 + 627912\sqrt{102}}{256}.
\]

- \(937t^2 = 937\cdot\frac{391 - 34\sqrt{102}}{16} = \frac{937(391 - 34\sqrt{102})}{16} = \frac{14992(391 - 34\sqrt{102})}{256}\).

Calculamos \(14992\cdot 391\):

\[
14992\cdot 391 = 14992\cdot (400-9) = 5996800 - 134928 = 5861872.
\]

\(14992\cdot 34 = 509728\).

Entonces:

\[
937t^2 = \frac{5861872 - 509728\sqrt{102}}{256}.
\]

- \(-2108t = -2108\cdot\frac{17-\sqrt{102}}{4} = -\frac{2108(17-\sqrt{102})}{4} = -\frac{8432(17-\sqrt{102})}{16} = -\frac{33728(17-\sqrt{102})}{64} = -\frac{134912(17-\sqrt{102})}{256}\).

Calculamos \(134912\cdot 17\):

\[
134912\cdot 17 = 134912\cdot (10+7) = 1349120 + 944384 = 2293504.
\]

Entonces:

\[
-2108t = \frac{-2293504 + 134912\sqrt{102}}{256}.
\]

- \(1600 = \frac{1600\cdot 256}{256} = \frac{409600}{256}\).

Ahora sumamos los numeradores.

Parte racional:

\[
2437137 - 6554520 + 5861872 - 2293504 + 409600.
\]

Calculamos:

\[
2437137 - 6554520 = -4117383.
\]

\[
-4117383 + 5861872 = 1744489.
\]

\[
1744489 - 2293504 = -549015.
\]

\[
-549015 + 409600 = -139415.
\]

No es cero. Entonces \(t = \frac{17-\sqrt{102}}{4}\) no es raíz exacta.

Hmm. La aproximación numérica fue engañosa. El error en \(P(t)\) es \(-139415/256 \approx -544.6\), que no es pequeño. Me equivoqué al comparar \(y\) aproximado con la forma; aunque \(y\) coincida aproximadamente, la ecuación exige \(t\) exacto.

De hecho, mi estimación de \(y\approx -2.2747\) podría tener error mayor al pensar. Revisemos el cálculo numérico de la raíz.

## 17. Mejor estimación numérica

Rehagamos el cálculo de \(f(1.3135)\) con más cuidado.

\[
x = 1.3135.
\]

\[
x^2 = 1.3135^2.
\]

\(1.3135^2 = (1.3 + 0.0135)^2 = 1.69 + 2\cdot 1.3\cdot 0.0135 + 0.0135^2 = 1.69 + 0.0351 + 0.00018225 = 1.72528225\).

\[
x^3 = x^2 \cdot x = 1.72528225 \cdot 1.3135.
\]

Calculamos:

\[
1.72528225 \cdot 1.3135 = 1.72528225 \cdot 1.3 + 1.72528225 \cdot 0.0135.
\]

\[
1.72528225 \cdot 1.3 = 2.242867.
\]

Redondeemos: \(1.72528225 \cdot 1.3 = 2.242866925\).

\[
1.72528225 \cdot 0.0135 = 1.72528225 \cdot 0.01 + 1.72528225 \cdot 0.0035 = 0.0172528225 + 0.006038487875 = 0.023291310375.
\]

\[
x^3 \approx 2.242866925 + 0.023291310 = 2.266158235.
\]

\[
x^4 = (x^2)^2 = 1.72528225^2.
\]

\[
1.72528225^2 \approx 2.976598.
\]

Calculemos con más precisión:

\[
1.72528225^2 = (1.7 + 0.02528225)^2 = 2.89 + 2\cdot 1.7\cdot 0.02528225 + 0.02528225^2.
\]

\[
2\cdot 1.7\cdot 0.02528225 = 3.4\cdot 0.02528225 = 0.08595965.
\]

\[
0.02528225^2 \approx 0.00063919.
\]

\[
x^4 \approx 2.89 + 0.08595965 + 0.00063919 = 2.97659884.
\]

Ahora:

\[
3x^4 \approx 3\cdot 2.97659884 = 8.92979652.
\]

\[
\sqrt{3} \approx 1.7320508076.
\]

\[
2\sqrt{3} \approx 3.464101615.
\]

\[
2\sqrt{3}x^3 \approx 3.464101615 \cdot 2.266158235.
\]

\[
3.464101615 \cdot 2.266158235 \approx 3.464101615\cdot 2.2 = 7.6210235, \quad + 3.464101615\cdot 0.066158235 \approx 0.22918.
\]

\[
\approx 7.8502035 + 0.22918 \approx 7.85020? 
\]

Revisemos: \(3.464101615 \cdot 2.266158235\).

\[
2.266158235 \cdot 3.464101615 = 2.266158235\cdot 3 + 2.266158235\cdot 0.464101615.
\]

\[
2.266158235\cdot 3 = 6.798474705.
\]

\[
2.266158235\cdot 0.464101615 = 2.266158235\cdot 0.46 + 2.266158235\cdot 0.004101615.
\]

\[
2.266158235\cdot 0.46 = 1.042432788.
\]

\[
2.266158235\cdot 0.004101615 \approx 0.009296.
\]

\[
2.266158235\cdot 0.464101615 \approx 1.042432788 + 0.009296 = 1.0517288.
\]

\[
2\sqrt{3}x^3 \approx 6.798474705 + 1.0517288 = 7.8502035.
\]

\[
25x^2 = 25\cdot 1.72528225 = 43.13205625.
\]

\[
6\sqrt{3} \approx 10.392304845.
\]

\[
6\sqrt{3}x \approx 10.392304845 \cdot 1.3135.
\]

\[
10.392304845 \cdot 1.3135 = 10.392304845\cdot 1.3 + 10.392304845\cdot 0.0135.
\]

\[
10.392304845\cdot 1.3 = 13.5099963.
\]

\[
10.392304845\cdot 0.0135 = 10.392304845\cdot 0.01 + 10.392304845\cdot 0.0035 = 0.103923048 + 0.036373067 = 0.140296115.
\]

\[
6\sqrt{3}x \approx 13.5099963 + 0.140296115 = 13.6502924.
\]

Ahora sumamos:

\[
f = 3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40.
\]

\[
f \approx 8.92979652 + 7.8502035 - 43.13205625 - 13.6502924 + 40.
\]

\[
8.92979652 + 7.8502035 = 16.7800.
\]

Sumemos paso a paso:

\[
8.92979652 + 7.8502035 = 16.78000002.
\]

\[
16.78000002 - 43.13205625 = -26.35205623.
\]

\[
-26.35205623 - 13.6502924 = -40.00234863.
\]

\[
-40.00234863 + 40 = -0.00234863.
\]

Entonces \(f \approx -0.00235\), no \(-0.00167\) como dije antes. Aun así cercano a cero.

Hagamos \(x=1.31345\):

\[
x^2 = 1.31345^2.
\]

\[
1.31345^2 = (1.31 + 0.00345)^2 = 1.7161 + 2\cdot 1.31\cdot 0.00345 + 0.00345^2.
\]

\[
2\cdot 1.31\cdot 0.00345 = 2.62\cdot 0.00345 = 0.009039.
\]

\[
0.00345^2 = 0.0000119025.
\]

\[
x^2 \approx 1.7161 + 0.009039 + 0.0000119 = 1.7251509.
\]

\[
x^3 = x^2\cdot x \approx 1.7251509 \cdot 1.31345.
\]

\[
1.7251509\cdot 1.31 = 1.7251509\cdot 1.3 + 1.7251509\cdot 0.01 = 2.2426962 + 0.0172515 = 2.2599477.
\]

\[
1.7251509\cdot 0.00345 = 1.7251509\cdot 0.003 + 1.7251509\cdot 0.00045 = 0.00517545 + 0.000776318 = 0.00595177.
\]

\[
x^3 \approx 2.2599477 + 0.00595177 = 2.2658995.
\]

\[
x^4 = (x^2)^2 \approx 1.7251509^2.
\]

\[
1.7251509^2 \approx (1.725 + 0.0001509)^2 = 2.975625 + 2\cdot 1.725\cdot 0.0001509 + 0.0001509^2.
\]

\[
2\cdot 1.725\cdot 0.0001509 = 3.45\cdot 0.0001509 = 0.0005206.
\]

\[
0.0001509^2 \approx 2.27\times 10^{-8}.
\]

\[
x^4 \approx 2.975625 + 0.0005206 = 2.9761456.
\]

\[
3x^4 \approx 8.9284368.
\]

\[
2\sqrt{3}x^3 \approx 3.464101615\cdot 2.2658995.
\]

\[
2.2658995\cdot 3.464101615 = 2.2658995\cdot 3 + 2.2658995\cdot 0.464101615.
\]

\[
2.2658995\cdot 3 = 6.7976985.
\]

\[
2.2658995\cdot 0.464101615 \approx 2.2658995\cdot 0.46 + 2.2658995\cdot 0.004101615.
\]

\[
2.2658995\cdot 0.46 = 1.0423138.
\]

\[
2.2658995\cdot 0.004101615 \approx 0.0092942.
\]

\[
\approx 1.0516080.
\]

\[
2\sqrt{3}x^3 \approx 6.7976985 + 1.0516080 = 7.8493065.
\]

\[
25x^2 \approx 25\cdot 1.7251509 = 43.1287725.
\]

\[
6\sqrt{3}x \approx 10.392304845\cdot 1.31345.
\]

\[
10.392304845\cdot 1.31 = 10.392304845\cdot 1.3 + 10.392304845\cdot 0.01 = 13.5099963 + 0.103923048 = 13.61391935.
\]

\[
10.392304845\cdot 0.00345 = 10.392304845\cdot 0.003 + 10.392304845\cdot 0.00045 = 0.0311769145 + 0.004676537 = 0.0358534515.
\]

\[
6\sqrt{3}x \approx 13.61391935 + 0.03585345 = 13.6497728.
\]

\[
f \approx 8.9284368 + 7.8493065 - 43.1287725 - 13.6497728 + 40.
\]

\[
8.9284368 + 7.8493065 = 16.7777433.
\]

\[
16.7777433 - 43.1287725 = -26.3510292.
\]

\[
-26.3510292 - 13.6497728 = -40.0008020.
\]

\[
-40.0008020 + 40 = -0.0008020.
\]

Muy cercano a cero.

Hagamos \(x=1.31340\):

\[
x^2 = 1.31340^2.
\]

\[
1.3134^2 = (1.31 + 0.0034)^2 = 1.7161 + 2\cdot 1.31\cdot 0.0034 + 0.0034^2.
\]

\[
2\cdot 1.31\cdot 0.0034 = 2.62\cdot 0.0034 = 0.008908.
\]

\[
0.0034^2 = 0.00001156.
\]

\[
x^2 \approx 1.7161 + 0.008908 + 0.00001156 = 1.72501956.
\]

\[
x^3 = x^2\cdot x = 1.72501956\cdot 1.3134.
\]

\[
1.72501956\cdot 1.31 = 2.2597756.
\]

\[
1.72501956\cdot 0.0034 = 1.72501956\cdot 0.003 + 1.72501956\cdot 0.0004 = 0.0051750587 + 0.0006900078 = 0.0058650665.
\]

\[
x^3 \approx 2.2597756 + 0.0058651 = 2.2656407.
\]

\[
x^4 = (x^2)^2 \approx 1.72501956^2.
\]

\[
1.72501956^2 \approx (1.725 + 0.00001956)^2 = 2.975625 + 2\cdot 1.725\cdot 0.00001956 + 0.00001956^2.
\]

\[
2\cdot 1.725\cdot 0.00001956 = 3.45\cdot 0.00001956 = 0.000067482.
\]

\[
x^4 \approx 2.975625 + 0.0000675 = 2.9756925.
\]

\[
3x^4 \approx 8.9270775.
\]

\[
2\sqrt{3}x^3 \approx 3.464101615\cdot 2.2656407.
\]

\[
2.2656407\cdot 3 = 6.7969221.
\]

\[
2.2656407\cdot 0.464101615 \approx 2.2656407\cdot 0.46 + 2.2656407\cdot 0.004101615.
\]

\[
2.2656407\cdot 0.46 = 1.0421947.
\]

\[
2.2656407\cdot 0.004101615 \approx 0.0092932.
\]

\[
\approx 1.0514879.
\]

\[
2\sqrt{3}x^3 \approx 6.7969221 + 1.0514879 = 7.8484100.
\]

\[
25x^2 \approx 25\cdot 1.72501956 = 43.125489.
\]

\[
6\sqrt{3}x \approx 10.392304845\cdot 1.3134.
\]

\[
10.392304845\cdot 1.31 = 13.61391935. \quad (esto es para 1.31)
\]

\[
10.392304845\cdot 0.0034 = 10.392304845\cdot 0.003 + 10.392304845\cdot 0.0004 = 0.0311769145 + 0.0041569219 = 0.0353338364.
\]

\[
6\sqrt{3}x \approx 13.61391935 + 0.03533384 = 13.64925318.
\]

\[
f \approx 8.9270775 + 7.8484100 - 43.125489 - 13.6492532 + 40.
\]

\[
8.9270775 + 7.8484100 = 16.7754875.
\]

\[
16.7754875 - 43.125489 = -26.3500015.
\]

\[
-26.3500015 - 13.6492532 = -39.9992547.
\]

\[
-39.9992547 + 40 = 0.0007453.
\]

Positivo.

Entonces la raíz está entre \(1.31340\) (f positivo) y \(1.31345\) (f negativo). Aproximadamente \(1.313425\).

Calculemos \(y = x^2 - 4 \approx 1.72515 - 4 = -2.27485\).

Entonces \(y \approx -2.27485\).

Ahora busquemos \(a,b,c\) con:

\[
\frac{a-\sqrt{b}}{c} \approx -2.27485.
\]

Reordenamos: \(a-\sqrt{b} \approx -2.27485 c\).

Probemos valores:

\(c=4\): \(a-\sqrt{b}\approx -9.0994\).

Probemos \(b=102\): \(\sqrt{102}\approx 10.0995049\). \(a = \sqrt{b} - 9.0994 = 10.0995049 - 9.0994 = 1.0001049 \approx 1\). ¡Muy cerca!

Entonces \(a=1\), \(b=102\), \(c=4\):

\[
\frac{1-\sqrt{102}}{4} \approx \frac{1-10.0995049}{4} = \frac{-9.0995049}{4} = -2.2748762.
\]

Nuestra \(y\approx -2.27485\). Diferencia \(0.000026\). Esto es muy prometedor. Quizá la raíz exacta sea \(y = \frac{1-\sqrt{102}}{4}\).

Revisemos el polinomio en \(t\) con \(t = \frac{17-\sqrt{102}}{4}\), que obtuvimos antes, y dio \(P(t) = -139415/256 \neq 0\). Eso indica que no es raíz exacta. Pero revisemos los cálculos de \(P(t)\), porque pude haber cometido un error.

En lugar de \(t = \frac{17-\sqrt{102}}{4}\), verifiquemos si \(x = \sqrt{t}\) satisface la ecuación original en \(x\):

\[
3x^4 + 2\sqrt{3}x^3 - 25x^2 - 6\sqrt{3}x + 40 = 0.
\]

Con \(x^2 = t = \frac{17-\sqrt{102}}{4}\), tenemos \(x^4 = t^2\).

\[
t = \frac{17 - \sqrt{102}}{4}.
\]

Como \(102 = 2\cdot 3\cdot 17\), \(102\) no simplifica con \(17\) de forma obvia. Pero notemos que \(\sqrt{102}\) y \(\sqrt{3}\) aparecen en la ecuación.

Si \(x^2 = t = \frac{17-\sqrt{102}}{4}\), entonces \(x = \frac{\sqrt{17-\sqrt{102}}}{2}\).

Veamos si \(x\) tiene la forma \(\frac{\sqrt{17}-\sqrt{6}}{2}\) o similar, porque \(\sqrt{17-\sqrt{102}}\) podría simplificarse:

\[
(\sqrt{17} - \sqrt{6})^2 = 17 + 6 - 2\sqrt{102} = 23 - 2\sqrt{102}.
\]

No.

\[
\left(\sqrt{\frac{17}{2}} - \sqrt{...}\right)
\]

Intentemos: buscamos \(p,q\) tales que

\[
(\sqrt{p} - \sqrt{q})^2 = p+q - 2\sqrt{pq} = 17 - \sqrt{102}.
\]

Entonces \(p+q = 17\) y \(2\sqrt{pq} = \sqrt{102}\), es decir, \(4pq = 102\), \(pq = 25.5\). No es entero. Así que \(17-\sqrt{102}\) no es un cuadrado perfecto en \(\mathbb{Q}(\sqrt{102})\) de forma simple.

Entonces \(x\) no tiene una expresión radical simple.

Quizá la raíz exacta tenga \(t\) de la forma \(\frac{17 - \sqrt{102}}{4}\) aproximadamente pero no exacta, y el error en \(P(t)\) es grande porque \(P\) es muy sensible.

Espera, revisemos el cálculo de \(P(t)\) para \(t = \frac{17-\sqrt{102}}{4}\). Obtuve \(P(t) = -139415/256 \approx -544\). Eso es un error enorme si \(t\) estuviera cerca de la raíz. Eso sugiere que \(t = \frac{17-\sqrt{102}}{4}\) no está cerca de la raíz. Pero numéricamente \(t \approx (17-10.0995)/4 = 6.9005/4 = 1.725125\), que está cerca de \(1.72515\). Entonces \(t\) sí está cerca de la raíz. ¿Por qué \(P(t)\) dio \(-544\)?

Revisemos el cálculo de \(P(t)\). Quizá cometí un error aritmético.

Verifiquemos \(P(t)\) evaluando numéricamente en \(t = 1.725125\):

\[
t \approx 1.725125.
\]

\[
t^2 \approx 2.976059.
\]

\[
t^3 \approx 5.134? \quad \text{Revisemos: } t\cdot t^2 \approx 1.725125\cdot 2.976059 \approx 5.133? 
\]

\[
1.725125\cdot 2.976059 \approx 1.725125\cdot 3 - 1.725125\cdot 0.023941 \approx 5.175375 - 0.041301 = 5.134074.
\]

\[
t^4 = (t^2)^2 \approx 2.976059^2 \approx 8.8569.
\]

Ahora:

\[
9t^4 \approx 9\cdot 8.8569 = 79.712.
\]

\[
-162t^3 \approx -162\cdot 5.134074 = -831.72.
\]

\[
937t^2 \approx 937\cdot 2.976059 \approx 937\cdot 3 - 937\cdot 0.023941 = 2811 - 22.433 = 2788.567.
\]

\[
-2108t \approx -2108\cdot 1.725125 \approx -2108\cdot 1.7 - 2108\cdot 0.025125 = -3583.6 - 52.964 = -3636.564.
\]

\[
+1600.
\]

Suma:

\[
79.712 - 831.72 + 2788.567 - 3636.564 + 1600.
\]

\[
79.712 - 831.72 = -752.008.
\]

\[
-752.008 + 2788.567 = 2036.559.
\]

\[
2036.559 - 3636.564 = -1600.005.
\]

\[
-1600.005 + 1600 = -0.005.
\]

¡Ah! Ahora da \(-0.005\), no \(-544\). Entonces cometí un error en el cálculo simbólico de \(P(t)\). Mi cálculo algebraico de \(P(t)\) para \(t = \frac{17-\sqrt{102}}{4}\) estaba mal.

Revisemos el cálculo simbólico.

\(t = \frac{17-\sqrt{102}}{4}\). Ya calculé:

\[
t^2 = \frac{391 - 34\sqrt{102}}{16}.
\]

Verifiquemos:

\[
(17-\sqrt{102})^2 = 289 - 34\sqrt{102} + 102 = 391 - 34\sqrt{102}.
\]

Correcto.

\[
t^3 = t\cdot t^2 = \frac{17-\sqrt{102}}{4} \cdot \frac{391-34\sqrt{102}}{16} = \frac{(17-\sqrt{102})(391-34\sqrt{102})}{64}.
\]

\[
17\cdot 391 = 6647. \quad \checkmark
\]

\[
17\cdot (-34\sqrt{102}) = -578\sqrt{102}.
\]

\[
(-\sqrt{102})\cdot 391 = -391\sqrt{102}.
\]

\[
(-\sqrt{102})(-34\sqrt{102}) = +34\cdot 102 = 3468.
\]

\[
6647 + 3468 = 10115. \quad \checkmark
\]

\[
\sqrt{102}\text{ terms}: -578 - 391 = -969. \quad \checkmark
\]

\[
t^3 = \frac{10115 - 969\sqrt{102}}{64}.
\]

Evaluemos numéricamente: \(10115 - 969\cdot 10.0995 = 10115 - 9786.4 = 328.6\). Dividido entre \(64\): \(5.134\). Correcto.

\[
t^4 = (t^2)^2 = (391 - 34\sqrt{102})^2 / 256.
\]

\[
391^2 = 152881. \quad \checkmark
\]

\[
2\cdot 391\cdot 34 = 782\cdot 34 = 26588. \quad \checkmark
\]

\[
(34\sqrt{102})^2 = 1156\cdot 102 = 117912. \quad \checkmark
\]

\[
152881 + 117912 = 270793. \quad \checkmark
\]

\[
t^4 = \frac{270793 - 26588\sqrt{102}}{256}.
\]

Ahora \(9t^4\):

\[
9(270793) = 2437137. \quad \checkmark
\]

\[
9\cdot 26588 = 239292. \quad \checkmark
\]

\[
9t^4 = \frac{2437137 - 239292\sqrt{102}}{256}.
\]

\(-162t^3\):

\[
-162\cdot 10115 = -1638630.
\]

¡Espera! Antes escribí \(648\cdot 10115 = 6554520\). Revisemos:

\[
-162 \cdot \frac{10115 - 969\sqrt{102}}{64} = \frac{-162(10115 - 969\sqrt{102})}{64}.
\]

Para poner denominador \(256\), multiplicamos numerador y denominador por \(4\):

\[
\frac{-162\cdot 4 (10115 - 969\sqrt{102})}{256} = \frac{-648(10115 - 969\sqrt{102})}{256}.
\]

\[
648\cdot 10115 = ?
\]

\[
10115 \cdot 648 = 10115 \cdot (600 + 48) = 6069000 + 485520 = 6554520.
\]

Eso está correcto. Pero \(-162 \cdot 10115 = -1638630\). Dividido entre \(64\):

\[
-1638630/64 = -25603.6.
\]

Y \(6554520/256 = 25603.6\). Correcto, son equivalentes.

\[
648\cdot 969 = 627912. \quad \checkmark
\]

Entonces \(-162t^3 = \frac{-6554520 + 627912\sqrt{102}}{256}\).

\(937t^2\):

\[
937 \cdot \frac{391 - 34\sqrt{102}}{16} = \frac{937(391 - 34\sqrt{102})}{16}.
\]

Para denominador \(256\), multiplicamos por \(16\):

\[
937\cdot 16 = 14992.
\]

\[
14992\cdot 391 = ?
\]

\[
14992 \cdot 391 = 14992\cdot 400 - 14992\cdot 9 = 5996800 - 134928 = 5861872. \quad \checkmark
\]

\[
14992\cdot 34 = 509728. \quad \checkmark
\]

\[
937t^2 = \frac{5861872 - 509728\sqrt{102}}{256}.
\]

\(-2108t\):

\[
-2108 \cdot \frac{17-\sqrt{102}}{4} = \frac{-2108(17-\sqrt{102})}{4}.
\]

Para denominador \(256\), multiplicamos por \(64\):

\[
2108\cdot 64 = 2108\cdot 64 = 134912.
\]

\[
-2108t = \frac{-134912(17-\sqrt{102})}{256} = \frac{-2293504 + 134912\sqrt{102}}{256}.
\]

\[
134912\cdot 17 = ?
\]

\[
134912 \cdot 17 = 134912\cdot 10 + 134912\cdot 7 = 1349120 + 944384 = 2293504. \quad \checkmark
\]

\(1600 = 409600/256\). Correcto.

Ahora suma de numeradores racionales:

\[
2437137 - 6554520 + 5861872 - 2293504 + 409600.
\]

Revisemos:

\[
2437137 - 6554520 = -4117383. \quad \checkmark
\]

\[
-4117383 + 5861872 = 1744489. \quad \checkmark
\]

\[
1744489 - 2293504 = -549015. \quad \checkmark
\]

\[
-549015 + 409600 = -139415. \quad \checkmark
\]

Parte con \(\sqrt{102}\):

\[
-239292 + 627912 - 509728 + 134912.
\]

\[
-239292 + 627912 = 388620.
\]

\[
388620 - 509728 = -121108.
\]

\[
-121108 + 134912 = 13804.
\]

Entonces:

\[
P(t) = \frac{-139415 + 13804\sqrt{102}}{256}.
\]

Evaluemos numéricamente:

\[
\sqrt{102} \approx 10.0995049.
\]

\[
13804\cdot 10.0995049 \approx 13804\cdot 10 + 13804\cdot 0.0995049 = 138040 + 1373.5657 = 139413.5657.
\]

\[
-139415 + 139413.5657 = -1.4343.
\]

\[
P(t) \approx -1.4343/256 = -0.00560.
\]

Esto coincide con la estimación numérica \(-0.005\). Entonces \(P(t) \approx -0.0056\), no exactamente cero. Por tanto, \(t = \frac{17-\sqrt{102}}{4}\) no es la raíz exacta, solo una aproximación.

Necesitamos encontrar la raíz exacta. La diferencia \(P(t) \approx -0.0056\) es pequeña, lo que sugiere que la raíz exacta está muy cerca.

## 18. Búsqueda de la raíz exacta en \(t\)

Tenemos el polinomio en \(t\):

\[
P(t) = 9t^4 - 162t^3 + 937t^2 - 2108t + 1600.
\]

Buscamos raíces. Intentemos factorizar con números racionales o cuadráticos con \(\sqrt{3}\).

Ya vimos que \(P(t)\) no parece factorizar en racionales. Intentemos con \(\sqrt{3}\).

Supongamos que \(t\) es de la forma \(t = \frac{p + q\sqrt{3}}{r}\), o más general \(t \in \mathbb{Q}(\sqrt{3})\).

La ecuación original en \(x\) tiene coeficientes en \(\mathbb{Q}(\sqrt{3})\). Las raíces en \(x\) podrían estar en \(\mathbb{Q}(\sqrt{3}, \sqrt{m})\) o algo similar.

Sin embargo, el enunciado dice que \(y\) tiene la forma \(\frac{a-\sqrt{b}}{c}\), con \(b\) entero positivo. Entonces \(x^2 = y+4 = \frac{a-\sqrt{b}}{c}+4 = \frac{a+4c-\sqrt{b}}{c}\). Así que \(x^2 \in \mathbb{Q}(\sqrt{b})\).

Por tanto, \(t = x^2 = \frac{A-\sqrt{b}}{c}\) para algún entero \(A\). Entonces \(t\) está en \(\mathbb{Q}(\sqrt{b})\).

Sustituimos \(t = \frac{A-\sqrt{b}}{c}\) en \(P(t)=0\). Si \(b\) no es un cuadrado perfecto, entonces \(P(t)\) tiene una parte racional y una parte con \(\sqrt{b}\), ambas deben ser cero.

Esto nos da un sistema para \(A,b,c\). Pero \(b\) es incógnita.

Alternativamente, podemos usar el resultado numérico para acotar. Sabemos \(t \approx 1.72514\). Entonces:

\[
\frac{A-\sqrt{b}}{c} \approx 1.72514.
\]

Como \(t>0\), \(A-\sqrt{b}>0\), así que \(A>\sqrt{b}\).

Intentemos con valores pequeños. Si \(b=3\), \(\sqrt{3}\approx 1.73205\). Necesitamos \(A-\sqrt{3}\approx 1.72514 c\).

Para \(c=1\): \(A \approx 1.72514 + 1.73205 = 3.45719\), no entero.

Para \(c=2\): \(A \approx 2\cdot 1.72514 + 1.73205 = 3.45028 + 1.73205 = 5.18233\), no entero.

Para \(c=3\): \(A \approx 5.17542 + 1.73205 = 6.90747\), no.

Para \(c=4\): \(A \approx 6.90056 + 1.73205 = 8.63261\), no.

Para \(c=5\): \(A \approx 8.6257 + 1.73205 = 10.35775\), no.

Para \(c=6\): \(A \approx 10.35084 + 1.73205 = 12.08289\), no.

Para \(c=7\): \(A \approx 12.07598 + 1.73205 = 13.80803\), no.

Para \(c=8\): \(A \approx 13.80112 + 1.73205 = 15.53317\), no.

Para \(c=9\): \(A \approx 15.52626 + 1.73205 = 17.25831\), no.

Para \(c=10\): \(A \approx 17.2514 + 1.73205 = 18.98345\), no.

No parece.

Probemos \(b=13\): \(\sqrt{13}\approx 3.60555\). Necesitamos \(A - 3.60555 \approx 1.72514c\).

Para \(c=2\): \(A \approx 3.45028 + 3.60555 = 7.05583\), no entero.

\(c=3\): \(A \approx 5.17542 + 3.60555 = 8.78097\), no.

\(c=4\): \(A \approx 6.90056 + 3.60555 = 10.50611\), no.

\(c=5\): \(A \approx 8.6257 + 3.60555 = 12.23125\), no.

\(c=6\): \(A \approx 10.35084 + 3.60555 = 13.95639\), no.

\(c=7\): \(A \approx 12.07598 + 3.60555 = 15.68153\), no.

\(c=8\): \(A \approx 13.80112 + 3.60555 = 17.40667\), no.

\(c=9\): \(A \approx 15.52626 + 3.60555 = 19.13181\), no.

\(c=10\): \(A \approx 17.2514 + 3.60555 = 20.85695\), no.

Probemos \(b=22\): \(\sqrt{22}\approx 4.69042\).

\(c=3\): \(A \approx 5.17542 + 4.69042 = 9.86584\), no.

\(c=4\): \(A \approx 6.90056 + 4.69042 = 11.59098\), no.

\(c=5\): \(A \approx 8.6257 + 4.69042 = 13.31612\), no.

\(c=6\): \(A \approx 10.35084 + 4.69042 = 15.04126\), no.

\(c=7\): \(A \approx 12.07598 + 4.69042 = 16.76640\), no.

\(c=8\): \(A \approx 13.80112 + 4.69042 = 18.49154\), no.

\(c=9\): \(A \approx 15.52626 + 4.69042 = 20.21668\), no.

\(c=10\): \(A \approx 17.2514 + 4.69042 = 21.94182\), no.

Probemos \(b=31\): \(\sqrt{31}\approx 5.56776\).

\(c=4\): \(A \approx 6.90056 + 5.56776 = 12.46832\), no.

\(c=5\): \(A \approx 8.6257 + 5.56776 = 14.19346\), no.

\(c=6\): \(A \approx 10.35084 + 5.56776 = 15.91860\), no.

\(c=7\): \(A \approx 12.07598 + 5.56776 = 17.64374\), no.

\(c=8\): \(A \approx 13.80112 + 5.56776 = 19.36888\), no.

\(c=9\): \(A \approx 15.52626 + 5.56776 = 21.09402\), no.

\(c=10\): \(A \approx 17.2514 + 5.56776 = 22.81916\), no.

Probemos \(b=43\): \(\sqrt{43}\approx 6.55744\).

\(c=5\): \(A \approx 8.6257 + 6.55744 = 15.18314\), no.

\(c=6\): \(A \approx 10.35084 + 6.55744 = 16.90828\), no.

\(c=7\): \(A \approx 12.07598 + 6.55744 = 18.63342\), no.

\(c=8\): \(A \approx 13.80112 + 6.55744 = 20.35856\), no.

\(c=9\): \(A \approx 15.52626 + 6.55744 = 22.08370\), no.

\(c=10\): \(A \approx 17.2514 + 6.55744 = 23.80884\), no.

Probemos \(b=57\): \(\sqrt{57}\approx 7.54983\).

\(c=6\): \(A \approx 10.35084 + 7.54983 = 17.90067\), no.

\(La parábola original es

\[
y=x^2-4.
\]

Un punto \((x,y)\) que está también sobre la imagen rotada \(60^\circ\) debe cumplir que su rotación de \(-60^\circ\),

\[
\left(\frac{x+\sqrt3\,y}{2},\frac{- \sqrt3\,x+y}{2}\right),
\]

también está sobre la parábola original. Imponiendo esa condición junto con \(y=x^2-4\), se obtiene

\[
3x^4+2\sqrt3\,x^3-25x^2-6\sqrt3\,x+40=0.
\]

Factorizamos:

\[
3x^4+2\sqrt3\,x^3-25x^2-6\sqrt3\,x+40
=
(x^2+\sqrt3\,x-4)(3x^2-\sqrt3\,x-10).
\]

Las raíces del primer factor son

\[
x=\frac{-\sqrt3\pm \sqrt{19}}{2},
\]

y las del segundo factor son

\[
x=\frac{\sqrt3\pm \sqrt{123}}{6}.
\]

En el cuarto cuadrante se tiene \(x>0\) y \(y=x^2-4<0\), es decir, \(0<x<2\). La única raíz en ese intervalo es

\[
x=\frac{\sqrt{19}-\sqrt3}{2}.
\]

Entonces

\[
x^2=\frac{11-\sqrt{57}}{2},
\]

y por tanto

\[
y=x^2-4=\frac{11-\sqrt{57}}{2}-4
=\frac{3-\sqrt{57}}{2}.
\]

Así, \(a=3\), \(b=57\), \(c=2\), con \(\gcd(3,2)=1\). Luego

\[
a+b+c=3+57+2=62.
\]

\[
\boxed{62}
\]