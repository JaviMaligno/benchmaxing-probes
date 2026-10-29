Primero, notemos que con \(\gcd(a,b)=210\), podemos escribir:

\[
a = 210x,\quad b = 210y
\]

donde \(\gcd(x,y)=1\) (enteros positivos primos entre sí).

Además,

\[
\operatorname{lcm}[a,b] = \frac{ab}{\gcd(a,b)} = \frac{(210x)(210y)}{210} = 210xy.
\]

Nos dicen que \(\operatorname{lcm}[a,b]=210^3\), así que:

\[
210xy = 210^3
\]

\[
xy = 210^2.
\]

Por lo tanto, necesitamos contar los pares \((x,y)\) de enteros positivos con \(\gcd(x,y)=1\), \(xy=210^2\), y además \(a<b\), es decir \(210x < 210y\), o sea \(x<y\).

Primero factorizamos \(210\):

\[
210 = 2 \cdot 3 \cdot 5 \cdot 7.
\]

Entonces

\[
210^2 = 2^2 \cdot 3^2 \cdot 5^2 \cdot 7^2.
\]

Como \(xy = 210^2\) y \(\gcd(x,y)=1\), cada factor primo debe ir por completo a \(x\) o por completo a \(y\). Hay 4 primos distintos, así que hay:

\[
2^4 = 16
\]

pares posibles \((x,y)\) con los primos repartidos uno a cada lado.

De esos 16 pares, exactamente la mitad tendrá \(x<y\) y la otra mitad \(x>y\). Para confirmar, no hay caso \(x=y\), porque eso implicaría \(x=y=210\), y entonces

\[
\gcd(x,y)=210 \neq 1.
\]

Por lo tanto, el número de pares con \(x<y\) es:

\[
\frac{16}{2} = 8.
\]

Así que hay **8** valores posibles para \(a\).

\[
\boxed{8}
\]