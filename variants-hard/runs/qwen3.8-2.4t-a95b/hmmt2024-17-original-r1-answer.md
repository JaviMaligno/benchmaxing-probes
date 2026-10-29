

Sea la rejilla una escalera semiinfinita con columnas \(0,1,2,\ldots\) y dos celdas por columna. Philip empieza en la celda superior de la columna \(0\). Contamos la celda inicial como alcanzable.

Definamos tres cantidades auxiliares:

- \(q\): probabilidad de que la otra celda de la primera columna sea alcanzable empezando desde una esquina.
- \(E\): valor esperado del número de celdas alcanzables empezando desde una sola celda esquina. Esta es la cantidad pedida.
- \(F\): valor esperado del número de celdas alcanzables si ambas celdas de la primera columna ya son alcanzables.

Primero calculamos \(q\). Para alcanzar la otra celda de la columna \(0\):

- con probabilidad \(1/2\), la puerta vertical de la columna \(0\) está abierta, y la celda es alcanzable inmediatamente;
- si esa puerta está cerrada, hay que salir por la puerta horizontal superior, llegar a la columna \(1\), conectar allá la celda superior con la inferior, y regresar por la puerta horizontal inferior. Esto ocurre con probabilidad
\[
\frac12\cdot \frac12\cdot q=\frac{q}{8},
\]
pues la subrejilla desde la columna \(1\) es una copia independiente del mismo problema.

Así,
\[
q=\frac12+\frac{q}{8}\implies \frac78 q=\frac12\implies q=\frac47.
\]

Ahora calculamos \(F\). Si ambas celdas de la columna \(0\) son alcanzables, ya aportan \(2\) celdas. Las dos puertas horizontales hacia la columna \(1\) deciden cuántas celdas de la siguiente copia son alcanzables inicialmente:

- con probabilidad \(1/4\), ninguna está abierta: no hay celdas nuevas;
- con probabilidad \(1/2\), exactamente una está abierta: se obtiene una copia con una sola fuente, expectativa \(E\);
- con probabilidad \(1/4\), ambas están abiertas: se obtiene una copia con dos fuentes, expectativa \(F\).

Por tanto,
\[
F=2+\frac12 E+\frac14 F.
\]
De aquí,
\[
\frac34 F=2+\frac12 E\implies F=\frac83+\frac23 E.
\]

Finalmente calculamos \(E\). Empezando solo en la celda superior:

- con probabilidad \(1/2\), la puerta vertical está abierta, y el problema se reduce a \(F\);
- con probabilidad \(1/2\), la puerta vertical está cerrada. En ese caso:
  - si la puerta horizontal superior está cerrada, solo se alcanza la celda inicial: \(1\);
  - si la puerta horizontal superior está abierta, se alcanza la celda superior de la columna \(1\), aportando una copia independiente con expectativa \(E\), más la celda inicial. Además, la celda inferior de la columna \(0\) puede alcanzarse si la puerta horizontal inferior está abierta y la conexión correspondiente en la copia ocurre; esto aporta en expectativa \(\frac12 q\).

Así,
\[
E=\frac12 F+\frac12\left[\frac12\cdot 1+\frac12\left(1+E+\frac{q}{2}\right)\right].
\]
Simplificando,
\[
E=\frac12F+\frac12+\frac14E+\frac18q.
\]
Usando \(q=\frac47\),
\[
E=\frac12F+\frac12+\frac14E+\frac1{14}
=\frac12F+\frac14E+\frac47.
\]
Entonces
\[
\frac34E=\frac12F+\frac47\implies 3E=2F+\frac{16}{7}.
\]

Sustituyendo \(F=\frac83+\frac23E\):
\[
3E=2\left(\frac83+\frac23E\right)+\frac{16}{7}
=\frac{16}{3}+\frac43E+\frac{16}{7}.
\]
Luego
\[
\frac53E=\frac{16}{3}+\frac{16}{7}
=\frac{160}{21},
\]
y por tanto
\[
E=\frac{3}{5}\cdot\frac{160}{21}=\frac{32}{7}.
\]

\[
\boxed{\frac{32}{7}}
\]