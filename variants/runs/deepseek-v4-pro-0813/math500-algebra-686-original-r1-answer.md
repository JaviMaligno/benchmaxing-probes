Primero, identificamos la serie geométrica:

\[
4+\frac{12}{a}+\frac{36}{a^2}+\cdots
\]

El primer término es \(4\) y la razón es \(\frac{3}{a}\), ya que:

\[
\frac{12/a}{4} = \frac{3}{a}
\]

La suma de una serie geométrica infinita con \(|r|<1\) es:

\[
S = \frac{4}{1 - \frac{3}{a}} = \frac{4a}{a-3}
\]

Queremos que esta suma sea un cuadrado perfecto. Como \(a\) es un entero positivo, la razón debe cumplir \(\left|\frac{3}{a}\right| < 1\), es decir \(a > 3\).

Entonces \(a-3\) debe dividir a \(4a\). Observemos:

\[
\frac{4a}{a-3} = 4 + \frac{12}{a-3}
\]

Para que \(S\) sea entero (requisito para ser cuadrado perfecto), \(a-3\) debe dividir a \(12\). Los divisores positivos de \(12\) son:

\[
1, 2, 3, 4, 6, 12
\]

Por lo tanto, \(a = 4, 5, 6, 7, 9, 15\).

Calculamos \(S\) para cada uno:

- \(a=4\): \(S = \frac{16}{1} = 16 = 4^2\)
- \(a=5\): \(S = \frac{20}{2} = 10\)
- \(a=6\): \(S = \frac{24}{3} = 8\)
- \(a=7\): \(S = \frac{28}{4} = 7\)
- \(a=9\): \(S = \frac{36}{6} = 6\)
- \(a=15\): \(S = \frac{60}{12} = 5\)

El único cuadrado perfecto es \(16\), que corresponde a \(a=4\).

Como \(a\) debe ser positivo y mayor que \(3\), el menor valor posible es \(4\).

\[
\boxed{4}
\]