Para que exista un triángulo con lados \(2\), \(a\) y \(b\), deben cumplirse las tres desigualdades triangulares:

\[
a+b>2,\qquad a+2>b,\qquad b+2>a.
\]

Las dos últimas equivalen a \(|a-b|<2\).

Como \(a,b\) se eligen de manera uniforme e independiente en \((0,4)\), el espacio muestral es el cuadrado \((0,4)\times(0,4)\) de área \(16\).

Las condiciones que fallan son:

1. \(a+b\le 2\), en el triángulo cercano al origen.
2. \(a-b\ge 2\), es decir \(a\ge b+2\).
3. \(b-a\ge 2\), es decir \(b\ge a+2\).

Por simetría, las tres regiones donde se incumple alguna desigualdad son triángulos rectángulos de catetos \(2\) y \(2\).

- La región \(a+b\le 2\) es un triángulo con vértices \((0,0)\), \((2,0)\), \((0,2)\); área \(\frac{1}{2}(2)(2)=2\).
- La región \(a\ge b+2\) es un triángulo con vértices \((2,0)\), \((4,0)\), \((4,2)\); área \(2\).
- La región \(b\ge a+2\) es un triángulo con vértices \((0,2)\), \((0,4)\), \((2,4)\); área \(2\).

Estas tres regiones no se solapan. Por tanto, el área total donde **no** se forma triángulo es

\[
2+2+2=6.
\]

El área donde sí se forma triángulo es

\[
16-6=10.
\]

La probabilidad pedida es

\[
\frac{10}{16}=\frac{5}{8}.
\]

\[
\boxed{\frac{5}{8}}
\]