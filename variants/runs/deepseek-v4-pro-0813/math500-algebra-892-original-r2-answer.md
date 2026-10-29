Debemos exigir que el recorrido de \(f\) sea todo \(\mathbb{R}\).

- Si \(a=0\), \(f(x)=0\) para todo \(x\); no funciona.

**Caso \(a>0\):**
- Para \(x\ge a\): \(f(x)=ax^2\), con mínimo en \(x=a\), así que su recorrido es \([a^3,\infty)\).
- Para \(x<a\): \(f(x)=ax+2a\), cuyo recorrido es \((-\infty,\,a^2+2a)\).

Para cubrir todo \(\mathbb{R}\) se necesita
\[
a^2+2a\ge a^3
\]
que, dividiendo por \(a>0\), da
\[
a+2\ge a^2 \iff (a-2)(a+1)\le 0 \iff a\le 2.
\]
Así que el mayor \(a>0\) que funciona es \(a=2\).

**Caso \(a<0\):**
- Para \(x\ge a\): el recorrido es \((-\infty,0]\).
- Para \(x<a\): el recorrido es \((a^2+2a,\infty)\).

Se necesita \(a^2+2a\le 0\), es decir \(-2\le a<0\). Estos valores son todos menores que \(2\).

Por lo tanto, el mayor valor posible es

\[
\boxed{2}
\]