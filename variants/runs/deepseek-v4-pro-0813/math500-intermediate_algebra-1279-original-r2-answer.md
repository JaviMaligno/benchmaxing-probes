Voy a resolverlo con cuidado.

Queremos la suma de todas las soluciones complejas de

\[
\frac{1}{x^2-1}+\frac{2}{x^2-2}+\frac{3}{x^2-3}+\frac{4}{x^2-4}=2010x-4.
\]

## 1. Observación clave del grado

Sea \(t=x^2\). El miembro izquierdo es

\[
L(t)=\frac{1}{t-1}+\frac{2}{t-2}+\frac{3}{t-3}+\frac{4}{t-4}.
\]

El denominador común es
\[
Q(t)=(t-1)(t-2)(t-3)(t-4).
\]

El numerador de \(L(t)\) será un polinomio de grado a lo sumo \(3\), porque \(L(t)\) tiende a \(0\) cuando \(t\to\infty\). Como \(L(t)\) es par en \(x\), el miembro izquierdo es una **función racional par** de \(x\).

Al igualar a \(2010x-4\) y multiplicar por \(Q(x^2)\), obtenemos una ecuación polinómica en \(x\):

\[
P(x)=2010x\,Q(x^2)-4Q(x^2)-N(x^2)=0,
\]

donde \(N(t)\) es el numerador de \(L(t)\). Notemos:

- \(Q(x^2)\) tiene grado \(8\) en \(x\), y es par.
- \(xQ(x^2)\) tiene grado \(9\), y es impar.
- \(N(x^2)\) tiene grado a lo sumo \(6\).

Por tanto, \(P(x)\) es un polinomio de grado \(9\) (el término dominante viene de \(2010x\cdot x^8\)).

## 2. Suma de raíces por Vieta

Necesitamos el coeficiente de \(x^8\) y el de \(x^9\).

### Coeficiente de \(x^9\)

Solo lo aporta \(2010x\,Q(x^2)\). El término dominante de \(Q(x^2)\) es

\[
(x^2)^4=x^8.
\]

Luego

\[
2010x\,Q(x^2)=2010x\cdot x^8+\cdots = 2010x^9+\cdots.
\]

Por tanto, el coeficiente de \(x^9\) es

\[
a_9=2010.
\]

### Coeficiente de \(x^8\)

Debemos calcularlo con cuidado. Hay tres contribuciones:

1. De \(2010x\,Q(x^2)\): necesitamos el término en \(x^7\) de \(Q(x^2)\). Pero \(Q(x^2)\) solo tiene potencias pares de \(x\), así que no tiene término en \(x^7\). Por tanto, esta parte **no contribuye** a \(x^8\).

2. De \(-4Q(x^2)\): es \(-4\) por el término en \(x^8\) de \(Q(x^2)\). Como \(Q(x^2)\approx x^8+\cdots\), el término de \(Q(x^2)\) que es múltiplo de \(x^8\) es el coeficiente de \(t^4\), que es \(1\). Entonces la contribución es

\[
-4\cdot 1=-4.
\]

3. De \(-N(x^2)\): \(N(t)\) tiene grado a lo sumo \(3\), así que \(N(x^2)\) tiene grado a lo sumo \(6\), y **no contribuye** a \(x^8\).

Por lo tanto,

\[
a_8=-4.
\]

### Suma de las raíces

Por las fórmulas de Vieta, la suma de las \(9\) raíces de \(P(x)\) es

\[
S=-\frac{a_8}{a_9}=-\frac{-4}{2010}=\frac{4}{2010}=\frac{2}{1005}.
\]

## 3. Verificación de que no hay raíces perdidas

Al multiplicar por \(Q(x^2)\), ¿podemos introducir raíces espurias? No, multiplicar por una cantidad no nula no introduce raíces en la ecuación. Lo único que podría pasar es que \(Q(x^2)=0\), es decir, \(x^2\in\{1,2,3,4\}\). Pero para esos valores el miembro izquierdo tiene polos, así que no son soluciones de la ecuación original. Por tanto, el conjunto de soluciones complejas coincide exactamente con las raíces del polinomio \(P\) de grado \(9\), y no hay soluciones extraviadas.

Además, \(P\) tiene grado exactamente \(9\) porque \(a_9=2010\neq0\), así que hay exactamente \(9\) soluciones complejas contadas con multiplicidad.

## 4. Respuesta

\[
\boxed{\frac{2}{1005}}
\]