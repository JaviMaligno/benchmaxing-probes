

Sea \(B=6\), y para cada número \(a\neq 6\), sea \(A=a\). Para calcular \(q(a)\), basta seguir las posiciones de \(A\) y \(B\): los demás números solo sirven como “ocupantes” con los que se intercambian.

Como primero se registra el número de la raíz y luego se hace el intercambio, \(a\) queda registrado si y solo si la posición de \(A\) llega a la raíz antes que la posición de \(B=6\). Así,

\[
q(a)=\mathbb P(\text{\(A\) llega a la raíz antes que \(B\)}).
\]

Usamos simetrías del árbol. Los nodos relevantes son la raíz, los dos hijos y las cuatro hojas.

---

### 1. Número \(2\)

Inicialmente, \(2\) está en el hijo izquierdo y \(6\) en el hijo derecho. Ambos están a la misma profundidad y en subárboles simétricos, por lo que

\[
q(2)=\frac12.
\]

---

### 2. Números \(1\) y \(3\)

Ambos son hojas del subárbol izquierdo, mientras que \(6\) está en el hijo derecho. Por simetría entre \(1\) y \(3\),

\[
q(1)=q(3).
\]

Llamemos \(x\) a la probabilidad de que una hoja en un subárbol gane contra \(6\) situado en el hijo del otro subárbol.

Desde ese estado, hay 6 aristas posibles:

- 1 arista hace subir \(A\) a hijo: quedan dos hijos en subárboles distintos, probabilidad \(1/2\).
- 2 aristas hacen bajar \(6\) a una hoja: quedan dos hojas en subárboles distintos, probabilidad \(1/2\).
- 1 arista hace subir \(6\) a la raíz: pierde \(A\), probabilidad \(0\).
- 2 aristas no mueven ni a \(A\) ni a \(6\): sigue en el mismo estado \(x\).

Entonces

\[
x=\frac16\cdot\frac12+\frac26\cdot\frac12+\frac26x.
\]

\[
x=\frac14+\frac{x}{3}
\]

\[
\frac{2x}{3}=\frac14
\]

\[
x=\frac38.
\]

Por tanto,

\[
q(1)=q(3)=\frac38.
\]

---

### 3. Números \(5\) y \(7\)

Ambos son hojas bajo el nodo donde está \(6\). Por simetría,

\[
q(5)=q(7).
\]

Llamemos \(y\) a la probabilidad de que \(A\) esté en una hoja y \(B=6\) en su padre.

Desde ese estado:

- 1 arista intercambia \(A\) y \(6\): ahora \(A\) es el hijo y \(6\) la hoja. Por complementariedad, esa probabilidad es \(1-y\).
- 1 arista mueve \(6\) a la otra hoja: quedan dos hojas hermanas, probabilidad \(1/2\).
- 1 arista mueve \(6\) a la raíz: pierde \(A\), probabilidad \(0\).
- 3 aristas no mueven ni a \(A\) ni a \(6\): sigue en el estado \(y\).

Así,

\[
y=\frac16(1-y)+\frac16\cdot\frac12+\frac36y.
\]

\[
y=\frac14+\frac{y}{3}
\]

\[
\frac{2y}{3}=\frac14
\]

\[
y=\frac38.
\]

Por tanto,

\[
q(5)=q(7)=\frac38.
\]

---

Finalmente,

\[
q(1)+q(2)+q(3)+q(5)+q(7)
=
\frac38+\frac12+\frac38+\frac38+\frac38.
\]

\[
=
\frac{3+4+3+3+3}{8}
=
\frac{16}{8}
=
2.
\]

\[
\boxed{2}
\]