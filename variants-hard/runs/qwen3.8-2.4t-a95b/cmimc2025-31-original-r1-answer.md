

Sea \(m\) el mes y \(d\) el día. La concatenación es

\[
N = m\cdot 10^k + d,
\]

donde \(k\) es la cantidad de dígitos de \(d\).

Para que sea un “buen día”, necesitamos:

1. \(m \mid N\). Como \(m \mid m\cdot 10^k\), esto equivale a \(m \mid d\).
2. \(d \mid N\). Como \(N = m\cdot 10^k + d\), esto equivale a \(d \mid m\cdot 10^k\).

Ahora revisamos cada mes.

### Marzo: \(m=3\), días \(1\) a \(31\)

Días múltiplos de \(3\):  
\[
3,6,9,12,15,18,21,24,27,30
\]

- Para \(d=3,6,9\), se necesita \(d \mid 30\): cumplen \(3,6\).
- Para \(d\ge 10\), se necesita \(d \mid 300\): cumplen \(12,15,30\).

Total en marzo: \(5\).

### Abril: \(m=4\), días \(1\) a \(30\)

Días múltiplos de \(4\):  
\[
4,8,12,16,20,24,28
\]

- Para \(d=4,8\), se necesita \(d \mid 40\): cumplen \(4,8\).
- Para \(d\ge 10\), se necesita \(d \mid 400\): cumplen \(16,20\).

Total en abril: \(4\).

### Mayo: \(m=5\), días \(1\) a \(31\)

Días múltiplos de \(5\):  
\[
5,10,15,20,25,30
\]

- Para \(d=5\), se necesita \(5 \mid 50\): cumple.
- Para \(d\ge 10\), se necesita \(d \mid 500\): cumplen \(10,20,25\).

Total en mayo: \(4\).

Por lo tanto, el número total de días buenos es

\[
5+4+4=13.
\]

\[
\boxed{13}
\]