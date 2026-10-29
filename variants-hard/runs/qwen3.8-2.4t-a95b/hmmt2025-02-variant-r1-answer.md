Sea \(N=\underline{abcde}=10000a+x\), donde \(x=\underline{bcde}\). La igualdad es

\[
\sqrt{10000a+x}=a\sqrt{x}.
\]

Elevando al cuadrado:

\[
10000a+x=a^2x
\]

\[
10000a=(a^2-1)x
\]

\[
x=\frac{10000a}{a^2-1}.
\]

Como \(a\) es un dígito de \(1\) a \(9\), y \(a=1\) no funciona, probamos \(a=2,\dots,9\). Como \(\gcd(a,a^2-1)=1\), necesitamos que \(a^2-1\) divida a \(10000=2^4\cdot 5^4\).

Los valores de \(a^2-1\) son:

\[
3,8,15,24,35,48,63,80.
\]

Solo \(8\) y \(80\) dividen a \(10000\), correspondientes a \(a=3\) y \(a=9\).

- Si \(a=3\):

\[
x=\frac{10000\cdot 3}{8}=3750,
\]

así que \(N=33750\).

- Si \(a=9\):

\[
x=\frac{10000\cdot 9}{80}=1125,
\]

así que \(N=91125\).

La suma de todos los números posibles es

\[
33750+91125=124875.
\]

\[
\boxed{124875}
\]