Numeremos los vértices módulo \(28\). Una longitud de segmento corresponde a un paso fijo \(k\), con \(1\le k\le 14\): cada segmento une \(i\) con \(i+k\).

Para \(k<14\), estos segmentos forman \(d=\gcd(28,k)\) ciclos, cada uno de longitud \(28/d\). Cada ciclo debe tener longitud par y, en ese caso, admite exactamente \(2\) emparejamientos. Por tanto, hay \(2^d\) posibilidades.

- Si \(\gcd(28,k)=1\), ocurre para \(6\) valores de \(k\): aportan \(6\cdot2=12\).
- Si \(k=7\), hay \(7\) ciclos de longitud \(4\): aportan \(2^7=128\).
- Si \(k=2,6,10\), hay \(2\) ciclos de longitud par: aportan \(3\cdot2^2=12\).
- Si \(k=4,8,12\), los ciclos tienen longitud \(7\): no aportan ninguna.
- Si \(k=14\), los segmentos son diámetros y el emparejamiento es único: aporta \(1\).

En total,
\[
12+128+12+1=\boxed{153}.
\]