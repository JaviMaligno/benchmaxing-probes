Para encontrar la distancia entre las dos rectas paralelas, podemos seguir los siguientes pasos:

**Paso 1: Identificar un punto en cada recta y el vector director común.**
De la primera recta, tomamos el punto $P_1 = \begin{pmatrix} 1 \\ 5 \\ -2 \end{pmatrix}$ y el vector director $\mathbf{v} = \begin{pmatrix} 3 \\ -10 \\ 4 \end{pmatrix}$.

De la segunda recta, tomamos el punto $P_2 = \begin{pmatrix} 8 \\ -1 \\ 9 \end{pmatrix}$. Notamos que su vector director es $\begin{pmatrix} -6 \\ 20 \\ -8 \end{pmatrix} = -2\mathbf{v}$, por lo que podemos usar $\mathbf{v}$ como el vector director para ambas rectas.

**Paso 2: Encontrar el vector que conecta $P_1$ y $P_2$.**
Restamos las coordenadas de $P_1$ de las de $P_2$:
\[\mathbf{u} = P_2 - P_1 = \begin{pmatrix} 8 - 1 \\ -1 - 5 \\ 9 - (-2) \end{pmatrix} = \begin{pmatrix} 7 \\ -6 \\ 11 \end{pmatrix}.\]

**Paso 3: Proyectar el vector $\mathbf{u}$ sobre el vector director $\mathbf{v}$.**
La proyección ortogonal de $\mathbf{u}$ sobre $\mathbf{v}$ está dada por la fórmula:
\[\text{proy}_{\mathbf{v}} \mathbf{u} = \left( \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2} \right) \mathbf{v}\]

Calculamos el producto punto $\mathbf{u} \cdot \mathbf{v}$:
\[\mathbf{u} \cdot \mathbf{v} = (7)(3) + (-6)(-10) + (11)(4) = 21 + 60 + 44 = 125.\]

Calculamos la magnitud al cuadrado de $\mathbf{v}$:
\[\|\mathbf{v}\|^2 = 3^2 + (-10)^2 + 4^2 = 9 + 100 + 16 = 125.\]

Por lo tanto, la proyección es:
\[\text{proy}_{\mathbf{v}} \mathbf{u} = \frac{125}{125} \mathbf{v} = \mathbf{v} = \begin{pmatrix} 3 \\ -10 \\ 4 \end{pmatrix}.\]

**Paso 4: Encontrar la componente de $\mathbf{u}$ perpendicular a $\mathbf{v}$ y su magnitud.**
El vector perpendicular $\mathbf{d}$ que va de una recta a la otra es:
\[\mathbf{d} = \mathbf{u} - \text{proy}_{\mathbf{v}} \mathbf{u} = \begin{pmatrix} 7 \\ -6 \\ 11 \end{pmatrix} - \begin{pmatrix} 3 \\ -10 \\ 4 \end{pmatrix} = \begin{pmatrix} 4 \\ 4 \\ 7 \end{pmatrix}.\]

La distancia entre las dos rectas es la magnitud de este vector perpendicular $\mathbf{d}$:
\[\|\mathbf{d}\| = \sqrt{4^2 + 4^2 + 7^2} = \sqrt{16 + 16 + 49} = \sqrt{81} = 9.\]

\boxed{9}