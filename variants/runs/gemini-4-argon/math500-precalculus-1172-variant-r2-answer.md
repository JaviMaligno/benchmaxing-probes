Para hallar la distancia entre las dos rectas paralelas, primero identificamos un punto en cada recta y el vector director común.

De la primera recta, tenemos el punto $P_1 = \begin{pmatrix} 1 \\ 5 \\ -2 \end{pmatrix}$ y el vector director $\mathbf{d} = \begin{pmatrix} 3 \\ -10 \\ 4 \end{pmatrix}$.

De la segunda recta, tenemos el punto $P_2 = \begin{pmatrix} 8 \\ -1 \\ 9 \end{pmatrix}$. Su vector director es $\begin{pmatrix} -6 \\ 20 \\ -8 \end{pmatrix} = -2\mathbf{d}$, lo que confirma que las rectas son paralelas y podemos usar $\mathbf{d}$ como el vector director para ambas.

A continuación, calculamos el vector $\mathbf{v}$ que va de $P_1$ a $P_2$:
\[\mathbf{v} = P_2 - P_1 = \begin{pmatrix} 8 - 1 \\ -1 - 5 \\ 9 - (-2) \end{pmatrix} = \begin{pmatrix} 7 \\ -6 \\ 11 \end{pmatrix}.\]

Ahora proyectamos el vector $\mathbf{v}$ sobre el vector director $\mathbf{d}$:
\[\text{proy}_{\mathbf{d}} \mathbf{v} = \frac{\mathbf{v} \cdot \mathbf{d}}{\|\mathbf{d}\|^2} \mathbf{d}.\]

Calculamos el producto escalar $\mathbf{v} \cdot \mathbf{d}$ y la magnitud al cuadrado de $\mathbf{d}$:
\[\mathbf{v} \cdot \mathbf{d} = (7)(3) + (-6)(-10) + (11)(4) = 21 + 60 + 44 = 125,\]
\[\|\mathbf{d}\|^2 = 3^2 + (-10)^2 + 4^2 = 9 + 100 + 16 = 125.\]

Por lo tanto, la proyección es:
\[\text{proy}_{\mathbf{d}} \mathbf{v} = \frac{125}{125} \mathbf{d} = \mathbf{d} = \begin{pmatrix} 3 \\ -10 \\ 4 \end{pmatrix}.\]

El vector perpendicular a ambas rectas que las conecta es la componente ortogonal de $\mathbf{v}$ respecto a $\mathbf{d}$:
\[\mathbf{w} = \mathbf{v} - \text{proy}_{\mathbf{d}} \mathbf{v} = \begin{pmatrix} 7 \\ -6 \\ 11 \end{pmatrix} - \begin{pmatrix} 3 \\ -10 \\ 4 \end{pmatrix} = \begin{pmatrix} 4 \\ 4 \\ 7 \end{pmatrix}.\]

Finalmente, la distancia entre las dos rectas es la magnitud del vector $\mathbf{w}$:
\[\|\mathbf{w}\| = \sqrt{4^2 + 4^2 + 7^2} = \sqrt{16 + 16 + 49} = \sqrt{81} = 9.\]

\boxed{9}