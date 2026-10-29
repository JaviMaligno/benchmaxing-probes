

Queremos maximizar
\[
\frac{x-y}{x^4+y^4+6}.
\]

Como el denominador es siempre positivo, basta probar una cota superior. Usamos la desigualdad
\[
4t \le t^4+3 \quad \text{para todo } t\in\mathbb{R}.
\]
Esto es cierto porque
\[
t^4+3-4t=(t-1)^2(t^2+2t+3)\ge 0.
\]

Aplicándola a \(x\) y a \(-y\), obtenemos
\[
4x \le x^4+3
\]
y
\[
-4y \le y^4+3.
\]

Sumando ambas desigualdades:
\[
4(x-y)\le x^4+y^4+6.
\]

Por tanto,
\[
\frac{x-y}{x^4+y^4+6}\le \frac14.
\]

La igualdad ocurre cuando \(x=1\) y \(-y=1\), es decir, \(y=-1\). En ese punto,
\[
\frac{1-(-1)}{1^4+(-1)^4+6}=\frac{2}{8}=\frac14.
\]

Así que el valor máximo es

\[
\boxed{\frac14}
\]