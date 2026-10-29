Para hallar la distancia entre las dos rectas paralelas, primero identificamos un punto en cada recta y el vector director común.

Sea $\mathbf{p}_1 = \begin{pmatrix} 3 \\ -10 \\ 1 \end{pmatrix}$ un punto en la primera recta y $\mathbf{p}_2 = \begin{pmatrix} -5 \\ -3 \\ 6 \end{pmatrix}$ un punto en la segunda recta.

El vector director de la primera recta es $\mathbf{d} = \begin{pmatrix} 2 \\ -9 \\ -2 \end{pmatrix}$. Como el vector director de la segunda recta es $\begin{pmatrix} 4 \\ -18 \\ -4 \end{pmatrix} = 2\mathbf{d}$, ambas rectas tienen la misma dirección definida por $\mathbf{d}$.

Calculamos el vector $\mathbf{v}$ que va de $\mathbf{p}_1$ a $\mathbf{p}_2$:
\[\mathbf{v} = \mathbf{p}_2 - \mathbf{p}_1 = \begin{pmatrix} -5 - 3 \\ -3 - (-10) \\ 6 - 1 \end{pmatrix} = \begin{pmatrix} -8 \\ 7 \\ 5 \end{pmatrix}.\]

La proyección de $\mathbf{v}$ sobre el vector director $\mathbf{d}$ está dada por:
\[\text{proy}_{\mathbf{d}} \mathbf{v} = \frac{\mathbf{v} \cdot \mathbf{d}}{\|\mathbf{d}\|^2} \mathbf{d}.\]

Calculamos el producto escalar $\mathbf{v} \cdot \mathbf{d}$ y la magnitud al cuadrado $\|\mathbf{d}\|^2$:
\[\mathbf{v} \cdot \mathbf{d} = (-8)(2) + (7)(-9) + (5)(-2) = -16 - 63 - 10 = -89,\]
\[\|\mathbf{d}\|^2 = 2^2 + (-9)^2 + (-2)^2 = 4 + 81 + 4 = 89.\]

Por lo tanto, la proyección es:
\[\text{proy}_{\mathbf{d}} \mathbf{v} = \frac{-89}{89} \begin{pmatrix} 2 \\ -9 \\ -2 \end{pmatrix} = -\begin{pmatrix} 2 \\ -9 \\ -2 \end{pmatrix} = \begin{pmatrix} -2 \\ 9 \\ 2 \end{pmatrix}.\]

El componente de $\mathbf{v}$ perpendicular a $\mathbf{d}$ es:
\[\mathbf{v}_{\perp} = \mathbf{v} - \text{proy}_{\mathbf{d}} \mathbf{v} = \begin{pmatrix} -8 \\ 7 \\ 5 \end{pmatrix} - \begin{pmatrix} -2 \\ 9 \\ 2 \end{pmatrix} = \begin{pmatrix} -6 \\ -2 \\ 3 \end{pmatrix}.\]

La distancia entre las dos rectas es la magnitud de este vector perpendicular:
\[D = \|\mathbf{v}_{\perp}\| = \sqrt{(-6)^2 + (-2)^2 + 3^2} = \sqrt{36 + 4 + 9} = \sqrt{49} = 7.\]

\boxed{7}