Primero, definimos la notación: 

\[
\underline{abcd} = 1000a + 100b + 10c + d
\]
con \(a \neq 0\) y \(a,b,c,d\) dígitos.

La condición dada es:

\[
\sqrt{1000a + 100b + 10c + d}
=
a\sqrt{100b + 10c + d}
\]

Elevamos al cuadrado ambos lados:

\[
1000a + 100b + 10c + d
=
a^2(100b + 10c + d)
\]

Sea

\[
N = 100b + 10c + d
\]

el número de tres dígitos \(\underline{bcd}\). Entonces:

\[
1000a + N = a^2 N
\]

\[
1000a = a^2 N - N = N(a^2 - 1)
\]

\[
1000a = N(a-1)(a+1)
\]

Por lo tanto,

\[
N = \frac{1000a}{(a-1)(a+1)} = \frac{1000a}{a^2 - 1}
\]

Ahora probamos los posibles valores de \(a\), desde 1 hasta 9.

- \(a=1\): \(N = \frac{1000}{0}\), no definido.
- \(a=2\): \(N = \frac{2000}{3}\), no entero.
- \(a=3\): \(N = \frac{3000}{8} = 375\), entero.
- \(a=4\): \(N = \frac{4000}{15}\), no entero.
- \(a=5\): \(N = \frac{5000}{24}\), no entero.
- \(a=6\): \(N = \frac{6000}{35}\), no entero.
- \(a=7\): \(N = \frac{7000}{48}\), no entero.
- \(a=8\): \(N = \frac{8000}{63}\), no entero.
- \(a=9\): \(N = \frac{9000}{80} = 112{,}5\), no entero.

El único valor entero es \(N=375\) con \(a=3\).

Verificamos:

\[
\underline{abcd} = 3375
\]

\[
\sqrt{3375} = 15\sqrt{15}
\]

y

\[
3\sqrt{375} = 3 \cdot 5\sqrt{15} = 15\sqrt{15}
\]

Ambas expresiones son iguales. Por lo tanto, el único número posible es:

\[
\boxed{3375}
\]