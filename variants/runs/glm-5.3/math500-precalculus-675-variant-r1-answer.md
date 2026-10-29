## Planteamiento

Sea $A = \begin{pmatrix} 3 & 8 \\ 0 & -3 \end{pmatrix}$. La menor constante $C$ que cumple $\|A\mathbf{w}\| \le C\|\mathbf{w}\|$ para todo $\mathbf{w}$ es la **norma del operador** de $A$ inducida por la norma euclidiana:

$$C = \max_{\mathbf{w} \neq \mathbf{0}} \frac{\|A\mathbf{w}\|}{\|\mathbf{w}\|}.$$

## Paso 1: Reducir a un problema de valores propios

Como $\|A\mathbf{w}\|^2 = \mathbf{w}^T A^T A \, \mathbf{w}$, maximizando sobre $\|\mathbf{w}\| = 1$ (el cociente de Rayleigh), el máximo de $\|A\mathbf{w}\|^2$ es el mayor valor propio de $A^T A$. Entonces $C = \sqrt{\lambda_{\max}(A^T A)}$.

## Paso 2: Calcular $A^T A$

$$A^T A = \begin{pmatrix} 3 & 0 \\ 8 & -3 \end{pmatrix}\begin{pmatrix} 3 & 8 \\ 0 & -3 \end{pmatrix} = \begin{pmatrix} 9 & 24 \\ 24 & 73 \end{pmatrix}.$$

## Paso 3: Valores propios

$$\det(A^T A - \lambda I) = (9-\lambda)(73-\lambda) - 24^2 = \lambda^2 - 82\lambda + 657 - 576 = \lambda^2 - 82\lambda + 81.$$

Resolviendo: $\lambda = \dfrac{82 \pm \sqrt{82^2 - 4\cdot 81}}{2} = \dfrac{82 \pm \sqrt{6400}}{2} = \dfrac{82 \pm 80}{2}$, es decir $\lambda_1 = 81$ y $\lambda_2 = 1$.

## Paso 4: Conclusión y verificación

$$C = \sqrt{81} = 9.$$

Comprobación con el vector propio de $A^T A$ para $\lambda = 81$: de $(9-81)x + 24y = 0$ sale $y = 3x$; tomando $\mathbf{w} = (1, 3)$, con $\|\mathbf{w}\| = \sqrt{10}$:
$$A\mathbf{w} = \begin{pmatrix} 3\cdot 1 + 8\cdot 3 \\ -3\cdot 3 \end{pmatrix} = \begin{pmatrix} 27 \\ -9 \end{pmatrix}, \quad \frac{\|A\mathbf{w}\|}{\|\mathbf{w}\|} = \frac{\sqrt{729+81}}{\sqrt{10}} = \frac{\sqrt{810}}{\sqrt{10}} = 9,$$
y el cociente nunca supera $9$ por ser este el valor singular máximo.

$$\boxed{C = 9}$$