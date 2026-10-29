

Primero reescribimos las dos desigualdades.

Tenemos

\[
x-yz<y-zx
\]

si y solo si

\[
x-yz-y+zx<0
\]

es decir,

\[
(x-y)+z(x-y)<0 \quad\Longleftrightarrow\quad (x-y)(z+1)<0.
\]

Análogamente,

\[
y-zx<z-xy
\]

si y solo si

\[
y-z+xy-zx<0
\]

es decir,

\[
(y-z)+x(y-z)<0 \quad\Longleftrightarrow\quad (y-z)(x+1)<0.
\]

Por tanto, el conjunto pedido está definido en el plano \(x+y+z=87\) por

\[
(x-y)(z+1)<0,\qquad (y-z)(x+1)<0.
\]

Ahora analizamos los signos de \(z+1\) y \(x+1\).

---

### Caso 1: \(z+1>0\) y \(x+1>0\)

Entonces

\[
x-y<0,\qquad y-z<0,
\]

por lo que

\[
x<y<z.
\]

Como además \(x+1>0\), tenemos \(x>-1\). Esta región es

\[
x>-1,\qquad x<y<z,
\]

en el plano \(x+y+z=87\). Es acotada, porque está limitada por las rectas

\[
x=-1,\qquad x=y,\qquad y=z.
\]

Sus vértices son las intersecciones de esas tres rectas:

- \(x=-1,\ x=y\):  
  \[
  (-1,-1,89).
  \]

- \(x=-1,\ y=z\):  
  \[
  -1+y+y=87 \implies y=44,
  \]
  así que
  \[
  (-1,44,44).
  \]

- \(x=y,\ y=z\):  
  \[
  x=y=z,\qquad 3x=87 \implies x=29,
  \]
  así que
  \[
  (29,29,29).
  \]

Esta es la única región finita.

---

### Área del triángulo

Sean

\[
P=(-1,-1,89),\qquad Q=(-1,44,44),\qquad R=(29,29,29).
\]

Los vectores son

\[
\overrightarrow{PQ}=(0,45,-45),
\]

\[
\overrightarrow{PR}=(30,30,-60).
\]

El área del triángulo es

\[
\frac12\left\|\overrightarrow{PQ}\times\overrightarrow{PR}\right\|.
\]

Calculamos el producto cruz:

\[
\overrightarrow{PQ}\times\overrightarrow{PR}
=
\begin{vmatrix}
\mathbf i & \mathbf j & \mathbf k\\
0&45&-45\\
30&30&-60
\end{vmatrix}
=
(-1350,-1350,-1350).
\]

Su norma es

\[
\sqrt{(-1350)^2+(-1350)^2+(-1350)^2}
=1350\sqrt3.
\]

Por tanto, el área es

\[
\frac12\cdot 1350\sqrt3=675\sqrt3.
\]

Así,

\[
a=675,\qquad b=3,
\]

y como \(3\) es libre de cuadrados,

\[
a+b=675+3=678.
\]

\[
\boxed{678}
\]