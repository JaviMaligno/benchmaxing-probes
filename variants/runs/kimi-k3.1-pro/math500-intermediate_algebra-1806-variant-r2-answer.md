Sea \(w=e^{i\theta}\). Entonces
\[
|1+w|=2\left|\cos\frac{\theta}{2}\right|.
\]
Además, como \(|w|=1\),
\[
|1-w+w^2|
=|w^{-1}-1+w|
=|2\cos\theta-1|.
\]
Por tanto, la expresión original es
\[
2\left|\cos\frac{\theta}{2}\right|+2|2\cos\theta-1|.
\]

Sea \(x=\left|\cos\frac{\theta}{2}\right|\in[0,1]\). Como \(\cos\theta=2x^2-1\), debemos maximizar
\[
f(x)=2x+2|4x^2-3|.
\]

- Si \(0\le x\le \frac{\sqrt3}{2}\), entonces
  \[
  f(x)=2x+6-8x^2,
  \]
  cuyo máximo se alcanza en \(x=\frac18\), dando
  \[
  f\left(\frac18\right)=\frac{49}{8}.
  \]

- Si \(\frac{\sqrt3}{2}\le x\le1\), entonces
  \[
  f(x)=8x^2+2x-6,
  \]
  que es creciente en este intervalo y tiene máximo \(f(1)=4\).

Como \(\frac{49}{8}>4\), y el valor \(x=\frac18\) es alcanzable, el máximo buscado es
\[
\boxed{\frac{49}{8}}
\]