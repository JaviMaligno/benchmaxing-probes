La condición para que exista un triángulo con lados \(1\), \(x\) y \(y\) es la desigualdad triangular:

\[
1 < x+y,\quad x < 1+y,\quad y < 1+x.
\]

Como \(x,y > 0\), las condiciones \(x<1+y\) y \(y<1+x\) se cumplen automáticamente, salvo en la región \(x \ge 1+y\) o \(y \ge 1+x\). Dentro del cuadrado \((0,3)\times(0,3)\), la condición relevante que restringe es:

\[
x + y > 1.
\]

La condición \(x < 1+y\) se traduce en \(y > x-1\), y \(y < 1+x\) en \(y < x+1\). Dentro del cuadrado \((0,3)^2\), la región que satisface las tres desigualdades es:

- \(x+y > 1\),
- \(y < x+1\),
- \(y > x-1\).

El área total del cuadrado es \(3 \cdot 3 = 9\).

Calculamos el área favorable restando del cuadrado las regiones donde no se cumple alguna desigualdad:

1. **\(x+y \le 1\)** (triángulo en la esquina inferior izquierda): área \(\frac12 \cdot 1 \cdot 1 = \frac12\).

2. **\(y \ge x+1\)** (región sobre la recta \(y=x+1\)): dentro del cuadrado es un triángulo con vértices \((0,1),(2,3),(0,3)\), de área \(\frac12 \cdot 2 \cdot 2 = 2\).

3. **\(y \le x-1\)** (región bajo la recta \(y=x-1\)): triángulo simétrico con vértices \((1,0),(3,0),(3,2)\), de área \(2\).

Estas tres regiones no se solapan dentro del cuadrado. Por lo tanto, el área favorable es:

\[
9 - \frac12 - 2 - 2 = 9 - 4.5 = 4.5.
\]

La probabilidad es:

\[
\frac{4.5}{9} = \frac12.
\]

\[
\boxed{\frac12}
\]