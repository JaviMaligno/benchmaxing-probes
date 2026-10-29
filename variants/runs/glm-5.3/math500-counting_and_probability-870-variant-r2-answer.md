Como la distribución es continua, casi seguro no hay empates, así que solo importa el orden cíclico de las seis etiquetas.

Fijemos \(P\) en una posición. Los otros cinco puntos tienen \(5!=120\) órdenes cíclicos igualmente probables.

1. Para que \(PQ\) cruce tanto \(RS\) como \(TU\), los cuatro puntos restantes deben quedar repartidos en los dos arcos entre \(P\) y \(Q\): un punto de la pareja \(RS\) y un punto de la pareja \(TU\) en cada arco. Por lo tanto, cada arco debe tener exactamente dos puntos, así que \(Q\) debe ser el cuarto punto del orden cíclico. Esto tiene probabilidad
\[
\frac15.
\]

2. Con \(P\) y \(Q\) en posiciones opuestas, los cuatro lugares restantes forman dos pares opuestos. Para que \(RS\) y \(TU\) también se crucen entre sí, \(R,S\) deben ocupar uno de esos pares opuestos y \(T,U\) el otro. Hay \(2\) elecciones para el par de \(RS\), y \(2\) órdenes internos en cada pareja, es decir
\[
2\cdot 2\cdot 2=8
\]
órdenes favorables de los \(4!=24\) posibles. La probabilidad condicional es \(8/24=1/3\).

Por lo tanto,
\[
\frac15\cdot\frac13=\frac1{15}.
\]

\[
\boxed{\frac{1}{15}}
\]