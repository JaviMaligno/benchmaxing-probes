**Razonamiento:**

Queremos calcular \(f^{-1}(0)+f^{-1}(6)\). Como la función es definida a trozos, debemos buscar los valores de \(x\) tales que \(f(x)=0\) y \(f(x)=6\).

**Paso 1: Encontrar \(f^{-1}(0)\)**

Caso \(x \le 3\):
\[
f(x) = 3-x = 0 \implies x = 3.
\]
Aquí \(x=3\) está en el dominio \(x\le 3\), así que es válido.

Caso \(x > 3\):
\[
f(x) = -x^3+2x^2+3x = 0.
\]
Factorizamos:
\[
-x^3+2x^2+3x = -x(x^2-2x-3) = -x(x-3)(x+1).
\]
Las raíces son \(x=0\), \(x=3\), \(x=-1\). Ninguna cumple \(x>3\), así que no hay solución en este tramo.

Por lo tanto, \(f^{-1}(0)=3\).

**Paso 2: Encontrar \(f^{-1}(6)\)**

Caso \(x \le 3\):
\[
3-x = 6 \implies x = -3.
\]
Aquí \(x=-3 \le 3\), así que es válido.

Caso \(x>3\):
\[
-x^3+2x^2+3x = 6.
\]
Reordenamos:
\[
-x^3+2x^2+3x-6 = 0.
\]
Probamos \(x=2\):
\[
-8+8+6-6 = 0.
\]
Entonces \(x=2\) es raíz, pero no cumple \(x>3\).

Factorizamos:
\[
-x^3+2x^2+3x-6 = -(x-2)(x^2+3).
\]
El factor cuadrático \(x^2+3\) no tiene raíces reales. Por lo tanto, no hay solución en \(x>3\).

Así que \(f^{-1}(6)=-3\).

**Paso 3: Suma final**

\[
f^{-1}(0)+f^{-1}(6) = 3 + (-3) = 0.
\]

\[
\boxed{0}
\]