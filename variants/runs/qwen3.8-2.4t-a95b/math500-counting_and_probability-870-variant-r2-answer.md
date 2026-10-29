

Como los puntos se eligen de forma continua e independiente, con probabilidad \(1\) los seis puntos son distintos. Además, solo importa el orden cíclico de las seis etiquetas alrededor del círculo.

Fijemos la posición de \(P\) como referencia. Las otras cinco etiquetas pueden ordenarse alrededor del círculo de

\[
5! = 120
\]

formas equiprobables.

Dos cuerdas \(AB\) y \(CD\) se cruzan si y solo si sus extremos se alternan en el orden cíclico. Para que \(PQ\) cruce tanto a \(RS\) como a \(TU\), cada uno de los pares \(\{R,S\}\) y \(\{T,U\}\) debe tener un extremo a cada lado de la cuerda \(PQ\). Por tanto, entre \(P\) y \(Q\) debe haber exactamente dos puntos por cada arco; es decir, \(Q\) debe estar en la posición opuesta a \(P\) dentro del orden cíclico.

Con \(P\) fija, esto obliga a que \(Q\) ocupe la cuarta posición. Quedan cuatro posiciones, formando dos pares opuestos. Para que \(RS\) y \(TU\) también se crucen entre sí, \(R,S\) deben ocupar uno de esos pares opuestos y \(T,U\) el otro.

Hay:

\[
2
\]

maneras de elegir cuál par opuesto ocupa \(\{R,S\}\), y luego

\[
2 \cdot 2 = 4
\]

maneras de orientar los pares \(\{R,S\}\) y \(\{T,U\}\). Así que hay

\[
2 \cdot 4 = 8
\]

ordenaciones favorables.

Por tanto, la probabilidad pedida es

\[
\frac{8}{120}=\frac{1}{15}.
\]

\[
\boxed{\frac{1}{15}}
\]