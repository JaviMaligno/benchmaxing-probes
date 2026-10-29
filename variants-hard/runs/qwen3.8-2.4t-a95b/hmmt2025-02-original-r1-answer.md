

Sea \(M=\underline{bcd}=100b+10c+d\). Entonces

\[
\underline{abcd}=1000a+M.
\]

La igualdad dada es

\[
\sqrt{1000a+M}=a\sqrt{M}.
\]

Elevando al cuadrado:

\[
1000a+M=a^2M
\]

\[
1000a=(a^2-1)M
\]

\[
M=\frac{1000a}{a^2-1}.
\]

Como \(a\) es un dígito nonzero, \(a\in\{1,2,\dots,9\}\). Además \(M\) debe ser entero.

- Si \(a=1\), el denominador es \(0\), imposible.
- Probamos los demás valores:

\[
\begin{aligned}
a=2&:\ M=\frac{2000}{3}\notin\mathbb{Z}\\
a=3&:\ M=\frac{3000}{8}=375\\
a=4&:\ M=\frac{4000}{15}\notin\mathbb{Z}\\
a=5&:\ M=\frac{5000}{24}\notin\mathbb{Z}\\
a=6&:\ M=\frac{6000}{35}\notin\mathbb{Z}\\
a=7&:\ M=\frac{7000}{48}\notin\mathbb{Z}\\
a=8&:\ M=\frac{8000}{63}\notin\mathbb{Z}\\
a=9&:\ M=\frac{9000}{80}=112.5
\end{aligned}
\]

La única opción válida es \(a=3\), \(M=375\). Por tanto,

\[
\underline{abcd}=3375.
\]

Verificación:

\[
\sqrt{3375}=\sqrt{9\cdot 375}=3\sqrt{375}.
\]

\[
\boxed{3375}
\]