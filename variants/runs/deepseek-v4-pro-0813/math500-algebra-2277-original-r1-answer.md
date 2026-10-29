Para calcular \(f^{-1}(0)+f^{-1}(6)\), necesitamos encontrar los valores de \(x\) tales que \(f(x)=0\) y \(f(x)=6\).

---

**1. Resolver \(f(x)=0\)**

- Para \(x \leq 3\): \(f(x)=3-x\)
  \[
  3-x=0 \implies x=3
  \]

- Para \(x>3\): \(f(x)=-x^3+2x^2+3x\)
  \[
  -x^3+2x^2+3x=0
  \]
  \[
  -x(x^2-2x-3)=0
  \]
  \[
  -x(x-3)(x+1)=0
  \]
  Las soluciones son \(x=0\), \(x=3\), \(x=-1\). Ninguna cumple \(x>3\).

Entonces la única solución de \(f(x)=0\) es \(x=3\), es decir,
\[
f^{-1}(0)=3.
\]

---

**2. Resolver \(f(x)=6\)**

- Para \(x \leq 3\): \(f(x)=3-x\)
  \[
  3-x=6 \implies x=-3
  \]
  Como \(-3 \leq 3\), es válida.

- Para \(x>3\): \(f(x)=-x^3+2x^2+3x\)
  \[
  -x^3+2x^2+3x=6
  \]
  \[
  -x^3+2x^2+3x-6=0
  \]
  \[
  x^3-2x^2-3x+6=0
  \]
  Factorizamos:
  \[
  x^2(x-2)-3(x-2)=0
  \]
  \[
  (x-2)(x^2-3)=0
  \]
  Las soluciones son \(x=2\), \(x=\sqrt{3}\), \(x=-\sqrt{3}\). Ninguna cumple \(x>3\).

Entonces la única solución de \(f(x)=6\) válida es \(x=-3\), es decir,
\[
f^{-1}(6)=-3.
\]

---

**3. Suma final**

\[
f^{-1}(0)+f^{-1}(6)=3+(-3)=0.
\]

\[
\boxed{0}
\]