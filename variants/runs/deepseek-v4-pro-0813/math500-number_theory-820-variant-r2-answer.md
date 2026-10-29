Factorizamos \(2310=2\cdot 3\cdot 5\cdot 7\cdot 11\), con \(5\) primos distintos.

Para cada primo \(p\in\{2,3,5,7,11\}\), si sus exponentes en \(m\) y \(n\) son \(a_p\) y \(b_p\), entonces:

- \(\gcd(m,n)=2310\) implica \(\min(a_p,b_p)=1\).
- \(\operatorname{mcm}(m,n)=2310^3\) implica \(\max(a_p,b_p)=3\).

Por lo tanto, para cada primo:

\[
\{a_p,b_p\}=\{1,3\}.
\]

Así, hay \(2\) opciones para cada uno de los \(5\) primos, lo que da \(2^5=32\) pares ordenados \((m,n)\).

Además, cada par ordenado tiene su pareja simétrica \((n,m)\), que también cumple las condiciones. Como no puede ocurrir \(m=n\), exactamente la mitad de los pares satisface \(m<n\).

Por tanto, el número de valores posibles de \(m\) es:

\[
\frac{32}{2}=16.
\]

\[
\boxed{16}
\]