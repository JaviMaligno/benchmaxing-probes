Para encontrar la distancia entre las dos rectas paralelas, primero identificamos un punto en cada recta y el vector director común.

De las ecuaciones dadas, podemos tomar el punto $P_1 = \begin{pmatrix} 3 \\ -10 \\ 1 \end{pmatrix}$ en la primera recta y el punto $P_2 = \begin{pmatrix} -5 \\ -3 \\ 6 \end{pmatrix}$ en la segunda recta. 

Como el vector director de la segunda recta es $\begin{pmatrix} 4 \\ -18 \\ -4 \end{pmatrix} = 2 \begin{pmatrix} 2 \\ -9 \\ -2 \end{pmatrix}$, ambas rectas tienen la dirección dada por el vector:
$$\mathbf{d} = \begin{pmatrix} 2 \\ -9 \\ -2 \end{pmatrix}$$

1. **Calculamos el vector $\mathbf{v}$ que conecta $P_2$ con $P_1$:**
$$\mathbf{v} = P_1 - P_2 = \begin{pmatrix} 3 - (-5) \\ -10 - (-3) \\ 1 - 6 \end{pmatrix} = \begin{pmatrix} 8 \\ -7 \\ -5 \end{pmatrix}$$

2. **Proyectamos el vector $\mathbf{v}$ sobre el vector director $\mathbf{d}$:**
Primero calculamos el producto escalar $\mathbf{v} \cdot \mathbf{d}$ y la norma al cuadrado de $\mathbf{d}$:
$$\mathbf{v} \cdot \mathbf{d} = (8)(2) + (-7)(-9) + (-5)(-2) = 16 + 63 + 10 = 89$$
$$\|\mathbf{d}\|^2 = 2^2 + (-9)^2 + (-2)^2 = 4 + 81 + 4 = 89$$

Por lo tanto, la proyección de $\mathbf{v}$ sobre $\mathbf{d}$ es:
$$\text{proy}_{\mathbf{d}}\mathbf{v} = \frac{\mathbf{v} \cdot \mathbf{d}}{\|\mathbf{d}\|^2} \mathbf{d} = \frac{89}{89} \begin{pmatrix} 2 \\ -9 \\ -2 \end{pmatrix} = \begin{pmatrix} 2 \\ -9 \\ -2 \end{pmatrix}$$

3. **Encontramos el componente ortogonal $\mathbf{w}$:**
Restamos la proyección al vector $\mathbf{v}$ para obtener el vector perpendicular a ambas rectas:
$$\mathbf{w} = \mathbf{v} - \text{proy}_{\mathbf{d}}\mathbf{v} = \begin{pmatrix} 8 \\ -7 \\ -5 \end{pmatrix} - \begin{pmatrix} 2 \\ -9 \\ -2 \end{pmatrix} = \begin{pmatrix} 6 \\ 2 \\ -3 \end{pmatrix}$$

4. **Calculamos la distancia entre las rectas:**
La distancia es la magnitud del vector ortogonal $\mathbf{w}$:
$$\|\mathbf{w}\| = \sqrt{6^2 + 2^2 + (-3)^2} = \sqrt{36 + 4 + 9} = \sqrt{49} = 7$$

\boxed{7}