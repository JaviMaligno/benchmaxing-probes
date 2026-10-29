Sean \(r\) y \(s\) las raíces de la ecuación (posiblemente iguales). La condición dice que, si definimos

\[
T(x)=x^2-2,
\]

entonces \(T(r)\) y \(T(s)\) también deben ser raíces. Como solo hay dos raíces, debe cumplirse

\[
T(r),T(s)\in\{r,s\}.
\]

Analizamos los casos posibles.

---

**1. Ambas raíces son puntos fijos de \(T\)**

\[
T(x)=x \implies x^2-2=x \implies x^2-x-2=0.
\]

Las soluciones son \(x=2\) y \(x=-1\). Entonces las raíces son \(\{2,-1\}\), y la ecuación es

\[
(x-2)(x+1)=x^2-x-2.
\]

---

**2. Las raíces se intercambian bajo \(T\)**

Entonces son soluciones no fijas de \(T(T(x))=x\). Calculamos:

\[
T(T(x))-x=(x^2-2)^2-2-x=x^4-4x^2-x+2.
\]

Factorizando:

\[
x^4-4x^2-x+2=(x^2-x-2)(x^2+x-1).
\]

Los puntos fijos ya corresponden al caso anterior. Las otras soluciones satisfacen

\[
x^2+x-1=0.
\]

Por tanto, la ecuación es

\[
x^2+x-1.
\]

---

**3. Una raíz es fija y la otra se transforma en ella**

Si la raíz fija es \(2\), la otra cumple

\[
x^2-2=2 \implies x^2=4 \implies x=\pm2.
\]

La raíz distinta es \(-2\). Entonces la ecuación es

\[
(x-2)(x+2)=x^2-4.
\]

Si la raíz fija es \(-1\), la otra cumple

\[
x^2-2=-1 \implies x^2=1 \implies x=\pm1.
\]

La raíz distinta es \(1\). Entonces la ecuación es

\[
(x+1)(x-1)=x^2-1.
\]

---

**4. Raíz doble fija**

Si la ecuación tiene una única raíz \(r\), debe cumplirse \(T(r)=r\). De nuevo \(r=2\) o \(r=-1\). Esto da:

\[
(x-2)^2=x^2-4x+4
\]

y

\[
(x+1)^2=x^2+2x+1.
\]

---

Las seis ecuaciones obtenidas son:

\[
x^2-x-2,\quad x^2+x-1,\quad x^2-4,\quad x^2-1,\quad x^2-4x+4,\quad x^2+2x+1.
\]

Por lo tanto, el número de ecuaciones es

\[
\boxed{6}
\]