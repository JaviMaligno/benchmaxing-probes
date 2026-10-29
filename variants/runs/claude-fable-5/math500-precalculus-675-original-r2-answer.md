El valor buscado es la norma de operador de la matriz, que coincide con su mayor valor singular.

**Planteamiento:** Si $\mathbf{v} = (x, y)$, entonces
$$A\mathbf{v} = \begin{pmatrix} 2x + 3y \\ -2y \end{pmatrix}, \qquad \|A\mathbf{v}\|^2 = (2x+3y)^2 + 4y^2 = 4x^2 + 12xy + 13y^2.$$

Queremos el máximo de $\dfrac{\|A\mathbf{v}\|^2}{\|\mathbf{v}\|^2} = \dfrac{4x^2 + 12xy + 13y^2}{x^2 + y^2}$.

**Vía valores propios de $A^TA$:** la forma cuadrática del numerador corresponde a
$$A^T A = \begin{pmatrix} 4 & 6 \\ 6 & 13 \end{pmatrix},$$
cuyo polinomio característico es
$$\lambda^2 - 17\lambda + (4\cdot 13 - 36) = \lambda^2 - 17\lambda + 16 = (\lambda - 16)(\lambda - 1).$$

Los valores propios son $\lambda = 16$ y $\lambda = 1$, así que el máximo de $\|A\mathbf{v}\|^2 / \|\mathbf{v}\|^2$ es $16$, y por tanto $\|A\mathbf{v}\| \le 4\|\mathbf{v}\|$ para todo $\mathbf{v}$.

**La cota se alcanza:** con el vector propio asociado a $\lambda = 16$, que satisface $4x + 6y = 16x$, es decir $y = 2x$. Tomando $\mathbf{v} = (1, 2)$:
$$A\mathbf{v} = \begin{pmatrix} 2 + 6 \\ -4 \end{pmatrix} = \begin{pmatrix} 8 \\ -4 \end{pmatrix}, \qquad \|A\mathbf{v}\| = \sqrt{64 + 16} = \sqrt{80} = 4\sqrt{5} = 4\|\mathbf{v}\|.$$

Como la desigualdad se cumple con $C = 4$ y hay un vector que la convierte en igualdad, ningún valor menor funciona.

$$\boxed{4}$$