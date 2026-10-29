## Planteamiento

El menor $C$ válido es la norma espectral de la matriz $A=\begin{pmatrix} 3 & 8 \\ 0 & -3\end{pmatrix}$, es decir, su mayor valor singular: la raíz del mayor autovalor de $A^TA$.

## Cálculo

$$A^TA=\begin{pmatrix} 3 & 0 \\ 8 & -3\end{pmatrix}\begin{pmatrix} 3 & 8 \\ 0 & -3\end{pmatrix}=\begin{pmatrix} 9 & 24 \\ 24 & 73\end{pmatrix}$$

Polinomio característico:

$$\lambda^2-82\lambda+(9\cdot 73-24^2)=\lambda^2-82\lambda+81=0$$

$$\lambda=\frac{82\pm\sqrt{6724-324}}{2}=\frac{82\pm 80}{2}\;\Longrightarrow\;\lambda=81\ \text{o}\ \lambda=1$$

Por tanto $\|A\|=\sqrt{81}=9$.

## Verificación

El valor se alcanza: para el autovector asociado a $\lambda=81$, por ejemplo $\mathbf{w}=\begin{pmatrix}1\\3\end{pmatrix}$, se tiene $A\mathbf{w}=\begin{pmatrix}27\\-9\end{pmatrix}$, con $\|A\mathbf{w}\|=9\sqrt{10}$ y $\|\mathbf{w}\|=\sqrt{10}$. La igualdad se cumple, así que ningún $C$ menor sirve.

\boxed{9}