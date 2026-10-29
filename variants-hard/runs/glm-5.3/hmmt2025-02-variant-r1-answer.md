Sea \(B=\underline{bcde}\). Entonces \(\underline{abcde}=10000a+B\), y la igualdad es

\[
\sqrt{10000a+B}=a\sqrt B.
\]

Al elebrar al cuadrado:

\[
10000a+B=a^2B
\]

entonces

\[
10000a=a^2B-B=(a^2-1)B,
\]

por lo que

\[
B=\frac{10000a}{a^2-1}.
\]

Como \(a\) es un dígito distinto de \(0\), probamos \(a=1,\dots,9\):

\[
\begin{array}{c|c}
a & B \\ \hline
2 & 20000/3 \\
3 & 3750 \\
4 & 8000/3 \\
5 & 6250/3 \\
6 & 12000/7 \\
7 & 4375/3 \\
8 & 80000/63 \\
9 & 1125
\end{array}
\]

Los únicos valores enteros son \(B=3750\) para \(a=3\), y \(B=1125\) para \(a=9\).

Así, los números posibles son

\[
33750 \quad \text{y} \quad 91125.
\]

Verificación:

\[
33750=9(3750)=3^2(3750),
\]

\[
91125=81(1125)=9^2(1125).
\]

Por lo tanto, la suma es

\[
33750+91125=124875.
\]

\[
\boxed{124875}
\]