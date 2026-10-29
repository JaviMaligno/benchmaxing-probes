Voy a resolver el problema paso a paso.

Tenemos la ecuación:

\[
\frac{1}{x^2 - 1} + \frac{2}{x^2 - 2} + \frac{3}{x^2 - 3} + \frac{4}{x^2 - 4} = 2022x - 4.
\]

Queremos la suma de todas las **raíces complejas**.

---

**Paso 1: Simplificar el lado izquierdo**

Observemos las fracciones:

\[
\frac{k}{x^2 - k} = \frac{x^2 - (x^2 - k)}{x^2 - k} = \frac{x^2}{x^2 - k} - 1.
\]

Entonces:

\[
\sum_{k=1}^4 \frac{k}{x^2 - k} = \sum_{k=1}^4 \left(\frac{x^2}{x^2 - k} - 1\right)
= x^2 \sum_{k=1}^4 \frac{1}{x^2 - k} - 4.
\]

La ecuación queda:

\[
x^2 \sum_{k=1}^4 \frac{1}{x^2 - k} - 4 = 2022x - 4.
\]

Los \(-4\) se cancelan:

\[
x^2 \sum_{k=1}^4 \frac{1}{x^2 - k} = 2022x.
\]

---

**Paso 2: Reducir la suma de fracciones**

\[
\sum_{k=1}^4 \frac{1}{x^2-k} = \frac{1}{x^2-1} + \frac{1}{x^2-2} + \frac{1}{x^2-3} + \frac{1}{x^2-4}.
\]

Pongamos \(t = x^2\). El producto de los denominadores es

\[
P(t) = (t-1)(t-2)(t-3)(t-4).
\]

La suma de fracciones es \(\dfrac{P'(t)}{P(t)}\), donde la derivada es respecto a \(t\).

Calculamos:

\[
P(t) = (t-1)(t-2)(t-3)(t-4).
\]

La derivada logarítmica:

\[
\frac{P'(t)}{P(t)} = \sum_{k=1}^4 \frac{1}{t-k}.
\]

Entonces la ecuación es:

\[
x^2 \cdot \frac{P'(t)}{P(t)} = 2022 x, \qquad t = x^2.
\]

Es decir:

\[
x \cdot \frac{P'(x^2)}{P(x^2)} = 2022, \qquad x \neq 0.
\]

(Notemos que \(x = 0\) no es raíz porque haría la expresión indefinida, además la ecuación original se simplificó dividiendo implícitamente entre \(x\)).

---

**Paso 3: Multiplicar en cruz**

\[
x P'(x^2) = 2022 P(x^2).
\]

Aquí \(P\) es de grado 4, \(P'\) de grado 3, así que el lado izquierdo es un polinomio en \(x\) de grado \(2\cdot 3 + 1 = 7\). El lado derecho es de grado \(8\). Por tanto es una ecuación polinómica de grado 8 en \(x\). Como no hay término lineal suelto, veamos su estructura.

Primero expandamos \(P(t)\):

\[
P(t) = (t-1)(t-2)(t-3)(t-4).
\]

Multiplicamos por pares:

\[
(t-1)(t-4) = t^2 - 5t + 4,
\]
\[
(t-2)(t-3) = t^2 - 5t + 6.
\]

Por tanto:

\[
P(t) = (t^2 - 5t + 4)(t^2 - 5t + 6).
\]

Sea \(u = t^2 - 5t\). Entonces:

\[
P(t) = (u+4)(u+6) = u^2 + 10u + 24.
\]

Volviendo a \(t\):

\[
u^2 = (t^2 - 5t)^2 = t^4 - 10t^3 + 25t^2,
\]
\[
10u = 10t^2 - 50t.
\]

Así:

\[
P(t) = t^4 - 10t^3 + 35t^2 - 50t + 24.
\]

La derivada:

\[
P'(t) = 4t^3 - 30t^2 + 70t - 50.
\]

---

**Paso 4: Sustituir \(t = x^2\)**

La ecuación es:

\[
x P'(x^2) = 2022 P(x^2).
\]

Escribimos:

\[
P'(x^2) = 4x^6 - 30x^4 + 70x^2 - 50,
\]
\[
P(x^2) = x^8 - 10x^6 + 35x^4 - 50x^2 + 24.
\]

Entonces:

\[
x(4x^6 - 30x^4 + 70x^2 - 50) = 2022(x^8 - 10x^6 + 35x^4 - 50x^2 + 24).
\]

Expandimos el lado izquierdo:

\[
4x^7 - 30x^5 + 70x^3 - 50x = 2022x^8 - 20220x^6 + 70770x^4 - 101100x^2 + 48528.
\]

Pasamos todo a un lado:

\[
-2022x^8 + 4x^7 + 20220x^6 - 30x^5 - 70770x^4 + 70x^3 + 101100x^2 - 50x - 48528 = 0.
\]

Multiplicamos por \(-1\) para comodidad, con coeficiente principal positivo:

\[
2022x^8 - 4x^7 - 20220x^6 + 30x^5 + 70770x^4 - 70x^3 - 101100x^2 + 50x + 48528 = 0.
\]

---

**Paso 5: Suma de las raíces**

Por las fórmulas de Vieta, la suma de las 8 raíces (contando multiplicidad) de

\[
a_8 x^8 + a_7 x^7 + \cdots + a_0 = 0
\]

es:

\[
-\frac{a_7}{a_8}.
\]

Aquí \(a_8 = 2022\) y \(a_7 = -4\). Por lo tanto:

\[
\text{Suma} = -\frac{-4}{2022} = \frac{4}{2022} = \frac{2}{1011}.
\]

---

**Paso 6: Comprobación de casos excluidos**

Al multiplicar cruzado, la ecuación original exige \(x^2 \neq 1,2,3,4\), es decir \(x \neq \pm 1, \pm \sqrt{2}, \pm \sqrt{3}, \pm 2\). Revisemos si alguna de esas podría ser raíz del polinomio resultante y, en tal caso, habría que descontarla.

- Si \(x = \pm 1, \pm\sqrt2, \pm\sqrt3, \pm 2\), entonces \(P(x^2) = 0\), pero también \(P'(x^2)\) es en general distinto de cero (raíces simples de \(P\)). La ecuación polinómica \(xP'(x^2) = 2022P(x^2)\) en esos puntos da \(xP'(x^2) = 0\), lo que implicaría \(x = 0\) o \(P'(x^2)=0\), lo cual no ocurre porque \(x \ne 0\) y las raíces de \(P\) son simples. Por lo tanto **ninguno** de esos valores son raíces de la ecuación polinómica. Así que no hay raíces extrañas que descontar.

También \(x=0\): el polinomio da término constante \(48528 \neq 0\), así que \(x=0\) no es raíz.

Por tanto las 8 raíces complejas son exactamente las raíces del polinomio y su suma es \(\frac{2}{1011}\).

---

**Respuesta final:**

\[
\boxed{\frac{2}{1011}}
\]