## Solución paso a paso

**Paso 1: Verificar el paralelismo.**
Los vectores dirección son $\mathbf{d}_1 = \begin{pmatrix} 2 \\ -9 \\ -2 \end{pmatrix}$ y $\mathbf{d}_2 = \begin{pmatrix} 4 \\ -18 \\ -4 \end{pmatrix} = 2\mathbf{d}_1$, así que las rectas son efectivamente paralelas.

**Paso 2: Vector entre puntos de ambas rectas.**
Tomamos $P_1 = (3, -10, 1)$ y $P_2 = (-5, -3, 6)$:
$$\vec{P_1P_2} = \begin{pmatrix} -8 \\ 7 \\ 5 \end{pmatrix}$$

**Paso 3: Distancia entre rectas paralelas.**
La distancia es
$$\text{dist} = \frac{|\vec{P_1P_2} \times \mathbf{d}_1|}{|\mathbf{d}_1|}$$

Calculamos el producto cruz:
$$\begin{pmatrix} -8 \\ 7 \\ 5 \end{pmatrix} \times \begin{pmatrix} 2 \\ -9 \\ -2 \end{pmatrix} = \begin{pmatrix} (7)(-2) - (5)(-9) \\ (5)(2) - (-8)(-2) \\ (-8)(-9) - (7)(2) \end{pmatrix} = \begin{pmatrix} 31 \\ -6 \\ 58 \end{pmatrix}$$

Su magnitud:
$$|\vec{P_1P_2} \times \mathbf{d}_1| = \sqrt{31^2 + (-6)^2 + 58^2} = \sqrt{961 + 36 + 3364} = \sqrt{4361}$$

Y $|\mathbf{d}_1| = \sqrt{2^2 + (-9)^2 + (-2)^2} = \sqrt{89}$.

**Paso 4: Resultado.**
$$\text{dist} = \frac{\sqrt{4361}}{\sqrt{89}} = \sqrt{\frac{4361}{89}} = \sqrt{49} = 7$$

La distancia entre las dos rectas es $\boxed{7}$.