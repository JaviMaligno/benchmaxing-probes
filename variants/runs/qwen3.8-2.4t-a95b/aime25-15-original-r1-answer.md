

Sea \(M=3^7=2187\). El conjunto \(\{1,2,\dots,3^6\}\) es un sistema completo de residuos módulo \(3^6\), pues \(3^6\equiv 0\pmod{3^6}\). Además \((3^6)^3=3^{18}\equiv 0\pmod{3^7}\), así que podemos contar ternas \((x,y,z)\) módulo \(3^6\) con

\[
x^3+y^3+z^3\equiv 0\pmod{3^7}.
\]

### 1. Cubos de unidades módulo \(3^7\)

Si \(u\) es unidad módulo \(3^6\), entonces \(u^3\equiv \pm1\pmod 9\). Hay

\[
2\cdot 3^{7-2}=2\cdot 3^5=486
\]

residuos módulo \(3^7\) congruentes a \(\pm1\pmod 9\), y también hay \(486\) unidades módulo \(3^6\).

Además, si \(x^3\equiv y^3\pmod{3^7}\) con \(x,y\)

unidades módulo \(3^6\), entonces \((xy^{-1})^3\equiv 1\pmod{3^7}\). Las raíces cúbicas de \(1\) módulo \(3^7\) son

\[
1,\quad 1+3^6,\quad 1+2\cdot 3^6,
\]

todas congruentes a \(1\pmod{3^6}\). Por tanto \(x\equiv y\pmod{3^6}\). Así, los cubos de las \(486\) unidades módulo \(3^6\) son exactamente, uno a uno, los \(486\) residuos módulo \(3^7\) congruentes a \(\pm1\pmod 9\).

Los múltiplos de \(3\) módulo \(3^6\) son \(243\), y sus cubos son divisibles por \(27\), luego también por \(9\).

Contamos según cuántas variables son unidades.

### Tres unidades
Sus cubos son \(\equiv \pm1\pmod 9\). La suma de tres signos \(\pm1\) nunca es \(0\pmod 9\), así que no hay soluciones.

### Una unidad
Los cubos de las otras dos variables son divisibles por \(3\), pero el cubo de la unidad es \(\equiv \pm1\pmod 3\). Imposible.

### Dos unidades
Elegimos la posición de la variable no unitaria: \(3\) formas. Esa variable puede ser cualquiera de los \(243\) múltiplos de \(3\). Sea \(t\) su cubo; entonces \(t\equiv0\pmod 9\).

Para cada elección de la primera unidad \(x\) (\(486\) formas), el valor

\[
-y^3 \equiv t+x^3\pmod{3^7}
\]

determina \(-t-x^3\), que también es congruo a \(\pm1\pmod 9\), por lo que es cubo de una única unidad \(y\). Así hay \(486\) pares ordenados \((x,y)\).

Contribución:

\[
3\cdot 243\cdot 486=354294.
\]

### Cero unidades
Todas las variables son divisibles por \(3\). Escribimos \(x=3x_1\), etc., con \(x_i\) módulo \(3^5\). La condición es

\[
27(x_1^3+y_1^3+z_1^3)\equiv0\pmod{3^7}
\]

o sea

\[
x_1^3+y_1^3+z_1^3\equiv0\pmod{3^4=81}.
\]

Cada residuo módulo \(81\) tiene exactamente \(3\) lifts módulo \(3^5\), así que esta contribución es \(27M\), donde \(M\) es el número de ternas módulo \(81\) con suma de cubos divisible por \(81\).

Calculamos \(M\). Módulo \(81\):

- Hay \(54\) unidades. Sus cubos son exactamente los \(18\) residuos \(\equiv \pm1\pmod 9\), cada uno con \(3\) preimágenes.
- Hay \(27\) múltiplos de \(3\). Sus cubos son \(0\) o \(\pm27\), todos divisibles por \(27\).

De nuevo, tres unidades es imposible módulo \(9\), y una unidad es imposible módulo \(3\).

Para dos unidades: elegimos la posición no unitaria (\(3\) formas) y el residuo no unitario (\(27\) formas). Para cada cubo no unitario \(t\), hay \(18\) pares de valores de cubos unitarios que suman \(-t\), y cada valor tiene \(3\) preimágenes, dando

\[
18\cdot 3\cdot 3=162
\]

pares ordenados de residuos unitarios. Contribución:

\[
3\cdot 27\cdot 162=13122.
\]

Para cero unidades: los residuos son divisibles por \(3\), digamos \(r=3s\) con \(s\) módulo \(27\). La condición queda

\[
s_1^3+s_2^3+s_3^3\equiv0\pmod 3,
\]

es decir \(s_1+s_2+s_3\equiv0\pmod 3\). Hay \(27^3/3=6561\) ternas.

Por tanto

\[
M=13122+6561=19683.
\]

La contribución de cero unidades al problema original es

\[
27M=27\cdot19683=531441.
\]

Finalmente,

\[
N=354294+531441=885735.
\]

El resto módulo \(1000\) es

\[
\boxed{735}
\]