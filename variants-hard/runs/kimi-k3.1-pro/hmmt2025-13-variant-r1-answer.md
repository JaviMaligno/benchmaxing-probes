Cada frasco debe contener, necesariamente, una de estas dos configuraciones:

- Cuatro canicas consecutivas.
- Dos pares de canicas consecutivas, pues no puede haber componentes aisladas.

Así, los veinte números quedan divididos en bloques consecutivos de longitud \(2\) o \(4\). Cada bloque de longitud \(4\) forma un frasco, mientras que los bloques de longitud \(2\) se emparejan para formar los demás frascos.

Si hay \(k\) bloques de longitud \(4\), habrá \(10-2k\) bloques de longitud \(2\). El número de ordenaciones de estos bloques es
\[
\binom{10-k}{k},
\]
y el número de maneras de emparejar los bloques de longitud \(2\) es
\[
(10-2k-1)!!=(9-2k)!!.
\]
Por tanto, el total es
\[
\sum_{k=0}^{5}\binom{10-k}{k}(9-2k)!!
=945+945+420+105+15+1.
\]

\[
\boxed{2431}
\]