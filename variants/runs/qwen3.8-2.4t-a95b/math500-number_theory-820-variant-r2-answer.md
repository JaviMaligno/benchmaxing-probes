

Sea \(2310=2\cdot 3\cdot 5\cdot 7\cdot 11\).

Para cada primo \(p\in\{2,3,5,7,11\}\), si los exponentes de \(p\) en \(m\) y \(n\) son \(a\) y \(b\), entonces:

- \(\gcd(m,n)=2310\) implica \(\min(a,b)=1\).
- \(\operatorname{lcm}(m,n)=2310^3\) implica \(\max(a,b)=3\).

Por tanto, para cada primo debemos tener \((a,b)=(1,3)\) o \((3,1)\). Como hay \(5\) primos, esto da

\[
2^5=32
\]

pares ordenados \((m,n)\).

Además, \(m\neq n\), y cada par \((m,n)\) tiene su versión intercambiada \((n,m)\). Exactamente uno de los dos cumple \(m<n\), así que el número de valores posibles de \(m\) es

\[
\frac{32}{2}=16.
\]

\[
\boxed{16}
\]