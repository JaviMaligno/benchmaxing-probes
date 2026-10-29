

Tenemos que contar los pares de enteros \((a,b)\) tales que

\[
|a+bi| \le 5.
\]

Como

\[
|a+bi|=\sqrt{a^2+b^2},
\]

la condición equivale a

\[
a^2+b^2 \le 25.
\]

Esto cuenta los puntos enteros dentro o sobre el círculo de radio \(5\) centrado en el origen.

Fijamos cada posible valor de \(a\) y contamos cuántos enteros \(b\) cumplen \(b^2 \le 25-a^2\):

- Si \(a=0\): \(b^2 \le 25\), entonces \(b=-5,-4,\dots,4,5\): \(11\) valores.
- Si \(a=\pm 1\): \(b^2 \le 24\), entonces \(|b|\le 4\): \(9\) valores para cada \(a\), total \(18\).
- Si \(a=\pm 2\): \(b^2 \le 21\), entonces \(|b|\le 4\): \(9\) valores para cada \(a\), total \(18\).
- Si \(a=\pm 3\): \(b^2 \le 16\), entonces \(|b|\le 4\): \(9\) valores para cada \(a\), total \(18\).
- Si \(a=\pm 4\): \(b^2 \le 9\), entonces \(|b|\le 3\): \(7\) valores para cada \(a\), total \(14\).
- Si \(a=\pm 5\): \(b^2 \le 0\), entonces \(b=0\): \(1\) valor para cada \(a\), total \(2\).

Sumando:

\[
11+18+18+18+14+2=81.
\]

\[
\boxed{81}
\]