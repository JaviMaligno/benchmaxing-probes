## Planteamiento

El menor $C$ válido es la norma espectral de la matriz, es decir, su mayor valor singular: la raíz cuadrada del mayor autovalor de $A^TA$.

## Cálculo

Con $A = \begin{pmatrix} 2 & 3 \\ 0 & -2 \end{pmatrix}$:

$$A^TA = \begin{pmatrix} 2 & 0 \\ 3 & -2 \end{pmatrix}\begin{pmatrix} 2 & 3 \\ 0 & -2 \end{pmatrix} = \begin{pmatrix} 4 & 6 \\ 6 & 13 \end{pmatrix}$$

El polinomio característico es
$$\lambda^2 - 17\lambda + (52 - 36) = \lambda^2 - 17\lambda + 16 = (\lambda - 1)(\lambda - 16),$$

con autovalores $\lambda = 1$ y $\lambda = 16$.

Entonces $\|A\mathbf{v}\|^2 = \mathbf{v}^TA^TA\,\mathbf{v} \le 16\|\mathbf{v}\|^2$, de donde $\|A\mathbf{v}\| \le 4\|\mathbf{v}\|$.

## Verificación de que la cota se alcanza

El autovector asociado a $\lambda = 16$ cumple $(4-16)x + 6y = 0 \Rightarrow y = 2x$; tomando $\mathbf{v} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ se obtiene $A\mathbf{v} = \begin{pmatrix} 8 \\ -4 \end{pmatrix}$, con $\|A\mathbf{v}\| = 4\sqrt{5} = 4\|\mathbf{v}\|$. Por tanto ningún $C$ menor sirve.

\boxed{4}