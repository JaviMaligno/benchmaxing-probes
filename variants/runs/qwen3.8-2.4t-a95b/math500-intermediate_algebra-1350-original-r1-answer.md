

Sean \(r_1,\dots,r_n\) las raíces. Como el coeficiente principal es \(2\),

\[
f(x)=2\prod_{i=1}^n (x-r_i).
\]

Por las fórmulas de Vieta,

\[
a_0=2(-1)^n\prod_{i=1}^n r_i=66,
\]

así que

\[
\prod_{i=1}^n r_i = (-1)^n 33.
\]

En particular,

\[
\left|\prod_{i=1}^n r_i\right|=33=3\cdot 11.
\]

Además,

\[
a_{n-1}=-2\sum_{i=1}^n r_i,
\]

por lo que queremos minimizar \(2\left|\sum r_i\right|\).

Como las raíces son enteros distintos y no nulos, sus valores absolutos deben multiplicarse a \(33\). Las únicas posibilidades son:

1. Una raíz con valor absoluto \(33\), pudiendo añadir \(1\) y/o \(-1\).
2. Dos raíces con valores absolutos \(3\) y \(11\), pudiendo añadir \(1\) y/o \(-1\).

También se debe cumplir \(\prod r_i=(-1)^n33\), lo cual equivale a que el número de raíces positivas sea par.

Analicemos los casos:

- Si el valor absoluto principal es \(33\), las sumas válidas posibles tienen magnitud al menos \(33\).

- Si los valores absolutos son \(3\) y \(11\):
  - Sin unidades: \(\{3,11\}\) o \(\{-3,-11\}\), con suma \(\pm 14\).
  - Con una unidad: por ejemplo,
    \[
    \{3,-11,1\}
    \]
    tiene suma
    \[
    3-11+1=-7.
    \]
    Esto cumple la condición del término constante.
  - Con dos unidades \(1,-1\), la menor magnitud de suma posible es \(8\).

Por tanto, la menor suma posible en valor absoluto es

\[
\left|\sum r_i\right|=7.
\]

Entonces

\[
|a_{n-1}|=2\cdot 7=14.
\]

Esto se logra con las raíces \(3,-11,1\):

\[
f(x)=2(x-3)(x+11)(x-1)=2x^3+14x^2-82x+66.
\]

\[
\boxed{14}
\]