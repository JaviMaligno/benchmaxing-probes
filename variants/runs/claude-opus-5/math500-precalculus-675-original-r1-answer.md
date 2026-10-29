## Planteamiento

El menor $C$ válido es la norma de operador de la matriz, es decir, la raíz de su mayor valor singular.

Sea $A=\begin{pmatrix} 2 & 3 \\ 0 & -2\end{pmatrix}$. Entonces

$$A^TA=\begin{pmatrix} 2 & 0 \\ 3 & -2\end{pmatrix}\begin{pmatrix} 2 & 3 \\ 0 & -2\end{pmatrix}=\begin{pmatrix} 4 & 6 \\ 6 & 13\end{pmatrix}$$

Como $\|A\mathbf v\|^2=\mathbf v^T A^TA\,\mathbf v$, el cociente $\|A\mathbf v\|^2/\|\mathbf v\|^2$ alcanza su máximo en el mayor valor propio de $A^TA$.

## Valores propios

$$\det(A^TA-\lambda I)=\lambda^2-17\lambda+(52-36)=\lambda^2-17\lambda+16=(\lambda-1)(\lambda-16)$$

El mayor es $\lambda=16$, por lo que $\|A\mathbf v\|\le 4\|\mathbf v\|$.

## Verificación de que es óptimo

El valor se alcanza con el vector propio asociado a $\lambda=16$: resolviendo $(4-16)v_1+6v_2=0$ se obtiene $\mathbf v=\begin{pmatrix}1\\2\end{pmatrix}$, con

$$A\mathbf v=\begin{pmatrix}8\\-4\end{pmatrix},\qquad \|A\mathbf v\|=\sqrt{80}=4\sqrt5=4\|\mathbf v\|$$

Por tanto la igualdad se cumple y $C=4$ no puede reducirse.

\boxed{4}