Para hallar la distancia entre dos rectas paralelas, tomo un punto de cada recta, formo el vector que los une y calculo la componente de ese vector perpendicular a la dirección común.

**Paso 1: Verificar paralelismo y fijar la dirección.**
El segundo vector director es $(-6, 20, -8) = -2(3, -10, 4)$, así que ambas rectas tienen dirección $\mathbf{d} = (3, -10, 4)$.

**Paso 2: Vector entre puntos de las rectas.**
$$\mathbf{v} = \begin{pmatrix} 8 \\ -1 \\ 9 \end{pmatrix} - \begin{pmatrix} 1 \\ 5 \\ -2 \end{pmatrix} = \begin{pmatrix} 7 \\ -6 \\ 11 \end{pmatrix}$$

**Paso 3: Distancia mediante el producto vectorial**, usando $\text{dist} = \dfrac{\|\mathbf{v} \times \mathbf{d}\|}{\|\mathbf{d}\|}$:

$$\mathbf{v} \times \mathbf{d} = \begin{pmatrix} (-6)(4) - (11)(-10) \\ (11)(3) - (7)(4) \\ (7)(-10) - (-6)(3) \end{pmatrix} = \begin{pmatrix} 86 \\ 5 \\ -52 \end{pmatrix}$$

**Paso 4: Normas.**
$$\|\mathbf{v} \times \mathbf{d}\| = \sqrt{86^2 + 5^2 + 52^2} = \sqrt{7396 + 25 + 2704} = \sqrt{10125} = 45\sqrt{5}$$
$$\|\mathbf{d}\| = \sqrt{9 + 100 + 16} = \sqrt{125} = 5\sqrt{5}$$

**Paso 5: Distancia.**
$$\text{dist} = \frac{45\sqrt{5}}{5\sqrt{5}} = 9$$

$$\boxed{9}$$