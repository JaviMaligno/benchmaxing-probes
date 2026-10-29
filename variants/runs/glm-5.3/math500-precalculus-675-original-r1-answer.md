# Solución

**Paso 1: Plantear el problema**

Buscamos el máximo de $\frac{\|A\mathbf{v}\|}{\|\mathbf{v}\|}$ sobre todos los $\mathbf{v} \neq \mathbf{0}$, donde
$$A = \begin{pmatrix} 2 & 3 \\ 0 & -2 \end{pmatrix}.$$
El menor $C$ que satisface la desigualdad es exactamente ese máximo (la norma de operador de $A$).

**Paso 2: Usar $A^T A$**

Como $\|A\mathbf{v}\|^2 = \mathbf{v}^T (A^T A)\,\mathbf{v}$, el máximo de $\frac{\|A\mathbf{v}\|^2}{\|\mathbf{v}\|^2}$ es el mayor valor propio de $A^T A$.

Calculamos:
$$A^T A = \begin{pmatrix} 2 & 0 \\ 3 & -2 \end{pmatrix}\begin{pmatrix} 2 & 3 \\ 0 & -2 \end{pmatrix} = \begin{pmatrix} 4 & 6 \\ 6 & 13 \end{pmatrix}.$$

**Paso 3: Valores propios de $A^T A$**

Con traza $4 + 13 = 17$ y determinante $4\cdot 13 - 36 = 16$:
$$\lambda^2 - 17\lambda + 16 = 0 \implies (\lambda - 16)(\lambda - 1) = 0,$$
así que $\lambda_{\max} = 16$.

**Paso 4: Concluir**

$$C = \sqrt{\lambda_{\max}} = \sqrt{16} = 4.$$

**Verificación:** el vector propio correspondiente a $\lambda = 16$ cumple $(4-16)x + 6y = 0 \Rightarrow y = 2x$. Con $\mathbf{v} = (1,2)$:
$$A\mathbf{v} = \begin{pmatrix} 2+6 \\ -4 \end{pmatrix} = \begin{pmatrix} 8 \\ -4 \end{pmatrix}, \quad \frac{\|A\mathbf{v}\|}{\|\mathbf{v}\|} = \frac{\sqrt{80}}{\sqrt{5}} = \frac{4\sqrt{5}}{\sqrt{5}} = 4. \checkmark$$

$$\boxed{4}$$