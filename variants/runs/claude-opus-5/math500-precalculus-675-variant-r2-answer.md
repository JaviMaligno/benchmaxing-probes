## Planteamiento

El menor $C$ válido es la norma espectral de $A=\begin{pmatrix}3&8\\0&-3\end{pmatrix}$, es decir, la raíz del mayor valor propio de $A^TA$.

## Cálculo

$$A^TA=\begin{pmatrix}3&0\\8&-3\end{pmatrix}\begin{pmatrix}3&8\\0&-3\end{pmatrix}=\begin{pmatrix}9&24\\24&73\end{pmatrix}$$

Polinomio característico:

$$\lambda^2-82\lambda+(9\cdot73-24^2)=\lambda^2-82\lambda+81=(\lambda-1)(\lambda-81)$$

El mayor valor propio es $\lambda=81$, luego $C=\sqrt{81}=9$.

## Verificación

Para $\mathbf{w}=\begin{pmatrix}1\\3\end{pmatrix}$ (vector propio asociado a $81$): $A\mathbf{w}=\begin{pmatrix}27\\-9\end{pmatrix}$, con $\|A\mathbf{w}\|=9\sqrt{10}$ y $\|\mathbf{w}\|=\sqrt{10}$. La igualdad se alcanza, así que $C=9$ no puede reducirse.

\boxed{9}