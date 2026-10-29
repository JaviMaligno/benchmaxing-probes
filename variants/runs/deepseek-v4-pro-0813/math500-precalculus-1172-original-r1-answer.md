Voy a razonar paso a paso.

**Paso 1. Verificar que las rectas son paralelas.**

La primera recta tiene vector director:

\[
\mathbf{d}_1 = \begin{pmatrix} 2 \\ -9 \\ -2 \end{pmatrix}.
\]

La segunda recta tiene vector director:

\[
\mathbf{d}_2 = \begin{pmatrix} 4 \\ -18 \\ -4 \end{pmatrix}.
\]

Observamos que \(\mathbf{d}_2 = 2\mathbf{d}_1\), así que efectivamente son paralelas.

**Paso 2. Un punto de cada recta.**

Tomamos:

\[
P = \begin{pmatrix} 3 \\ -10 \\ 1 \end{pmatrix}, \qquad
Q = \begin{pmatrix} -5 \\ -3 \\ 6 \end{pmatrix}.
\]

**Paso 3. Vector entre los dos puntos.**

\[
\overrightarrow{PQ} = Q - P = \begin{pmatrix} -5 - 3 \\ -3 - (-10) \\ 6 - 1 \end{pmatrix}
= \begin{pmatrix} -8 \\ 7 \\ 5 \end{pmatrix}.
\]

**Paso 4. Distancia entre rectas paralelas.**

La distancia entre dos rectas paralelas es:

\[
d = \frac{\|\overrightarrow{PQ} \times \mathbf{d}_1\|}{\|\mathbf{d}_1\|}.
\]

Calculamos el producto vectorial:

\[
\overrightarrow{PQ} \times \mathbf{d}_1
= \begin{pmatrix} -8 \\ 7 \\ 5 \end{pmatrix}
\times
\begin{pmatrix} 2 \\ -9 \\ -2 \end{pmatrix}.
\]

Usando la fórmula del producto cruz:

\[
= \begin{pmatrix}
7(-2) - 5(-9) \\
5(2) - (-8)(-2) \\
(-8)(-9) - 7(2)
\end{pmatrix}.
\]

Calculamos cada componente:

- Primera componente:
  \[
  7(-2) - 5(-9) = -14 + 45 = 31.
  \]

- Segunda componente:
  \[
  5(2) - (-8)(-2) = 10 - 16 = -6.
  \]

- Tercera componente:
  \[
  (-8)(-9) - 7(2) = 72 - 14 = 58.
  \]

Por lo tanto:

\[
\overrightarrow{PQ} \times \mathbf{d}_1 =
\begin{pmatrix} 31 \\ -6 \\ 58 \end{pmatrix}.
\]

**Paso 5. Normas.**

\[
\|\overrightarrow{PQ} \times \mathbf{d}_1\|
= \sqrt{31^2 + (-6)^2 + 58^2}
= \sqrt{961 + 36 + 3364}
= \sqrt{4361}.
\]

\[
\|\mathbf{d}_1\|
= \sqrt{2^2 + (-9)^2 + (-2)^2}
= \sqrt{4 + 81 + 4}
= \sqrt{89}.
\]

**Paso 6. Distancia.**

\[
d = \frac{\sqrt{4361}}{\sqrt{89}}
= \sqrt{\frac{4361}{89}}.
\]

Calculamos:

\[
\frac{4361}{89} = 49.
\]

Por lo tanto:

\[
d = 7.
\]

\[
\boxed{7}
\]