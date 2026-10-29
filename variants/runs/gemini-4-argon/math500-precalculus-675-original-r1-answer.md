Sea $\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}$ un vector bidimensional cualquiera. Queremos hallar el menor número real positivo $C$ tal que
\[ \left\| \begin{pmatrix} 2 & 3 \\ 0 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} \right\| \le C \left\| \begin{pmatrix} x \\ y \end{pmatrix} \right\| \]
para todo $x, y \in \mathbb{R}$.

1. Calculamos el producto matricial:
\[ \begin{pmatrix} 2 & 3 \\ 0 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2x + 3y \\ -2y \end{pmatrix}. \]

2. Elevando al cuadrado ambos lados de la desigualdad de las magnitudes (dado que ambas cantidades y $C$ son no negativas), obtenemos:
\[ (2x + 3y)^2 + (-2y)^2 \le C^2 (x^2 + y^2). \]

3. Desarrollamos el lado izquierdo:
\[ 4x^2 + 12xy + 9y^2 + 4y^2 = 4x^2 + 12xy + 13y^2. \]

4. Buscamos el mínimo valor de $C^2$ tal que
\[ C^2(x^2 + y^2) - (4x^2 + 12xy + 13y^2) \ge 0 \]
para todo $x, y \in \mathbb{R}$, es decir:
\[ (C^2 - 4)x^2 - 12xy + (C^2 - 13)y^2 \ge 0. \]

5. Para que esta forma cuadrática sea semidefinida positiva, su discriminante debe ser menor o igual a cero (y $C^2 - 4 \ge 0$):
\[ (-12)^2 - 4(C^2 - 4)(C^2 - 13) \le 0 \]
\[ 144 - 4(C^4 - 17C^2 + 52) \le 0 \]
\[ 36 - (C^4 - 17C^2 + 52) \le 0 \]
\[ C^4 - 17C^2 + 16 \ge 0 \]
\[ (C^2 - 16)(C^2 - 1) \ge 0. \]

6. Como se requiere además que $C^2 - 13 \ge 0$, debemos tener $C^2 \ge 16$. En efecto, para $C^2 = 16$:
\[ 16(x^2 + y^2) - (4x^2 + 12xy + 13y^2) = 12x^2 - 12xy + 3y^2 = 3(2x - y)^2 \ge 0, \]
alcanzándose la igualdad cuando $y = 2x$ (por ejemplo, para $\mathbf{v} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$).

Por lo tanto, el menor número real positivo $C$ es $\sqrt{16} = 4$.

\boxed{4}