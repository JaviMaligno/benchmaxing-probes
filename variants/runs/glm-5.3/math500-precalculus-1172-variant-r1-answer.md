## Planteamiento

**Paso 1: Verificar que son paralelas.**

Los vectores dirección son:
$$\mathbf{d}_1 = \begin{pmatrix} 3 \\ -10 \\ 4 \end{pmatrix}, \qquad \mathbf{d}_2 = \begin{pmatrix} -6 \\ 20 \\ -8 \end{pmatrix} = -2\,\mathbf{d}_1$$

Efectivamente, $\mathbf{d}_2$ es múltiplo escalar de $\mathbf{d}_1$, así que las rectas son paralelas.

**Paso 2: Vector entre un punto de cada recta.**

Tomamos $P_1 = (1, 5, -2)$ y $P_2 = (8, -1, 9)$:
$$\mathbf{w} = \overrightarrow{P_1 P_2} = \begin{pmatrix} 7 \\ -6 \\ 11 \end{pmatrix}$$

**Paso 3: Fórmula de la distancia entre rectas paralelas.**

$$\text{dist} = \frac{\|\mathbf{w} \times \mathbf{d}_1\|}{\|\mathbf{d}_1\|}$$

Calculamos el producto cruz $\mathbf{w} \times \mathbf{d}_1$:
$$\mathbf{w} \times \mathbf{d}_1 = \begin{pmatrix} (-6)(4) - (11)(-10) \\ (11)(3) - (7)(4) \\ (7)(-10) - (-6)(3) \end{pmatrix} = \begin{pmatrix} -24 + 110 \\ 33 - 28 \\ -70 + 18 \end{pmatrix} = \begin{pmatrix} 86 \\ 5 \\ -52 \end{pmatrix}$$

**Paso 4: Normas.**

$$\|\mathbf{w} \times \mathbf{d}_1\|^2 = 86^2 + 5^2 + (-52)^2 = 7396 + 25 + 2704 = 10125$$
$$\|\mathbf{d}_1\|^2 = 3^2 + (-10)^2 + 4^2 = 9 + 100 + 16 = 125$$

**Paso 5: Distancia.**

$$\text{dist} = \sqrt{\frac{10125}{125}} = \sqrt{81} = 9$$

$\boxed{9}$