El problema pide contar los pares ordenados de enteros \((a,b)\) tales que

\[
|a+bi|=\sqrt{a^2+b^2}\le 5.
\]

Elevando al cuadrado:

\[
a^2+b^2\le 25.
\]

Debemos contar los puntos con coordenadas enteras \((a,b)\) que están dentro o sobre la circunferencia de radio \(5\) centrada en el origen.

Contamos por valores de \(a\). Como \(|a|\le 5\), los posibles valores son \(-5,-4,\dots,4,5\).

Para cada entero \(a\), el número de enteros \(b\) que satisfacen

\[
b^2\le 25-a^2
\]

es \(2\lfloor\sqrt{25-a^2}\rfloor+1\).

Calculamos:

- \(a=0\): \(2\lfloor 5\rfloor+1=11\)
- \(a=\pm 1\): \(2\lfloor\sqrt{24}\rfloor+1=2\cdot 4+1=9\)
- \(a=\pm 2\): \(2\lfloor\sqrt{21}\rfloor+1=2\cdot 4+1=9\)
- \(a=\pm 3\): \(2\lfloor 4\rfloor+1=9\)
- \(a=\pm 4\): \(2\lfloor 3\rfloor+1=7\)
- \(a=\pm 5\): \(2\lfloor 0\rfloor+1=1\)

Sumamos:

\[
11 + 4\cdot 9 + 2\cdot 7 + 2\cdot 1 = 11+36+14+2=63.
\]

Por tanto, el número de pares ordenados es

\[
\boxed{63}
\]