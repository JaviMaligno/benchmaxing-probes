

La condición es

\[
|x+yi| \le 6 \iff \sqrt{x^2+y^2}\le 6 \iff x^2+y^2 \le 36.
\]

Contamos los pares enteros \((x,y)\) fijando \(x\) y contando los valores enteros posibles de \(y\).

Para cada \(x\), necesitamos

\[
y^2 \le 36-x^2,
\]

así que el número de valores enteros de \(y\) es

\[
2\left\lfloor \sqrt{36-x^2}\right\rfloor+1.
\]

Como \(x\) puede ir de \(-6\) a \(6\):

\[
\begin{array}{c|c}
x & \text{número de } y \\ \hline
0 & 13 \\
\pm 1 & 11 \text{ cada uno} \\
\pm 2 & 11 \text{ cada uno} \\
\pm 3 & 11 \text{ cada uno} \\
\pm 4 & 9 \text{ cada uno} \\
\pm 5 & 7 \text{ cada uno} \\
\pm 6 & 1 \text{ cada uno}
\end{array}
\]

Entonces el total es

\[
13+2(11+11+11+9+7+1)=13+2(50)=113.
\]

\[
\boxed{113}
\]