Queremos la norma operador de la matriz, es decir, el máximo de $\|A\mathbf{v}\|$ sobre vectores unitarios $\mathbf{v}$.

**Paso 1: Plantear la cantidad a maximizar.** Con $\mathbf{v} = (x, y)$ y $x^2 + y^2 = 1$:

$$A\mathbf{v} = \begin{pmatrix} 2x + 3y \\ -2y \end{pmatrix}, \qquad \|A\mathbf{v}\|^2 = (2x+3y)^2 + 4y^2 = 4x^2 + 12xy + 13y^2.$$

**Paso 2: Usar $A^T A$.** El máximo de $\|A\mathbf{v}\|^2$ en la esfera unitaria es el mayor autovalor de

$$A^T A = \begin{pmatrix} 2 & 0 \\ 3 & -2 \end{pmatrix}\begin{pmatrix} 2 & 3 \\ 0 & -2 \end{pmatrix} = \begin{pmatrix} 4 & 6 \\ 6 & 13 \end{pmatrix}.$$

**Paso 3: Calcular los autovalores.** El polinomio característico es

$$\lambda^2 - 17\lambda + (4\cdot 13 - 36) = \lambda^2 - 17\lambda + 16 = (\lambda - 16)(\lambda - 1),$$

así que los autovalores son $16$ y $1$. El mayor es $16$.

**Paso 4: Concluir.** El máximo de $\|A\mathbf{v}\|$ sobre vectores unitarios es $\sqrt{16} = 4$, y se alcanza (por ejemplo, con el autovector asociado a $\lambda = 16$, proporcional a $(1, 2)$: entonces $A\mathbf{v} = (8, -4)$, de norma $\sqrt{80} = 4\sqrt{5} = 4\|\mathbf{v}\|$). Por lo tanto, el menor $C$ que funciona para todo $\mathbf{v}$ es

$$\boxed{4}$$