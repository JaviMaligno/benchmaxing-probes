Numeramos los vértices módulo \(24\). Si la longitud común corresponde a una cuerda que une vértices a distancia \(k\), hay un solo valor de \(k\in\{1,\dots,12\}\) para todos los segmentos.

Para \(k<12\), sea \(d=\gcd(24,k)\). Los vértices se dividen en \(d\) ciclos, cada uno con \(24/d\) vértices. Cada ciclo debe emparejarse mediante aristas alternas:

- Si \(24/d\) es impar, no hay emparejamiento.
- Si \(24/d\) es par, cada ciclo tiene exactamente \(2\) emparejamientos, lo que da \(2^d\) posibilidades.

Así, los números para \(k=1,\dots,11\) son
\[
2,\ 4,\ 8,\ 16,\ 2,\ 64,\ 2,\ 0,\ 8,\ 4,\ 2.
\]
Para \(k=12\), todos los segmentos son diámetros y el emparejamiento es único.

Por tanto, el total es
\[
2+4+8+16+2+64+2+0+8+4+2+1=\boxed{113}.
\]