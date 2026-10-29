Fijemos la longitud común de los segmentos. Sea \(d\) el número de lados del \(28\)-gono que separan los extremos de cada segmento, con \(1\le d\le 14\) (el caso \(d=14\) corresponde a vértices opuestos).

Para un \(d\) fijo, formamos el grafo cuyos vértices son los \(28\) y cuyas aristas unen vértices a distancia \(d\) en el polígono. Queremos contar emparejamientos perfectos de ese grafo.

Sea \(g=\gcd(28,d)\). El grafo se descompone en \(g\) componentes, cada una con \(28/g\) vértices, y cada componente es un ciclo (salvo \(d=14\), donde son aristas sueltas).

- Un ciclo de longitud par tiene exactamente \(2\) emparejamientos perfectos.
- Un ciclo de longitud impar no tiene ninguno.

Los casos son:

- \(d=1,3,5,9,11,13\): \(\gcd(28,d)=1\), un ciclo de \(28\) vértices \(\Rightarrow 2\) cada uno.  
  Total: \(6\cdot 2=12\).

- \(d=2,6,10\): \(\gcd(28,d)=2\), dos ciclos de \(14\) vértices \(\Rightarrow 2^2=4\) cada uno.  
  Total: \(3\cdot 4=12\).

- \(d=4,8,12\): \(\gcd(28,d)=4\), cuatro ciclos de \(7\) vértices, longitud impar \(\Rightarrow 0\).

- \(d=7\): \(\gcd(28,7)=7\), siete ciclos de \(4\) vértices \(\Rightarrow 2^7=128\).

- \(d=14\): catorce aristas sueltas \(\Rightarrow 1\).

Sumando:

\[
12+12+0+128+1=153.
\]

\[
\boxed{153}
\]