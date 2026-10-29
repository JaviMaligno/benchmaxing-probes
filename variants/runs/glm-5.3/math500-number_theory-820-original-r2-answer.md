Paso 1: Como \(\gcd(a,b)=210\), escribimos
\[
a=210x,\qquad b=210y
\]
con \(\gcd(x,y)=1\).

Paso 2: Entonces
\[
\mathop{\text{lcm}}[a,b]=210xy=210^3,
\]
así que
\[
xy=210^2=2^2\cdot 3^2\cdot 5^2\cdot 7^2.
\]

Paso 3: Como \(\gcd(x,y)=1\), cada potencia prima completa \(2^2,3^2,5^2,7^2\) debe ir completa en \(x\) o en \(y\). Son \(4\) decisiones binarias, luego hay \(2^4=16\) parejas ordenadas \((x,y)\).

Paso 4: La condición \(a<b\) implica \(x<y\). Como ninguna pareja tiene \(x=y\), exactamente la mitad cumple \(x<y\):
\[
\frac{16}{2}=8.
\]

\[
\boxed{8}
\]