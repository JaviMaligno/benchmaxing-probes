## Planteamiento

Las dos rectas son paralelas porque $(-6, 20, -8) = -2(3, -10, 4)$. Para la distancia tomamos un punto de cada recta y proyectamos el vector que los une sobre la dirección común.

**Vector entre los puntos base:**
$$\vec{v} = \begin{pmatrix} 8 \\ -1 \\ 9 \end{pmatrix} - \begin{pmatrix} 1 \\ 5 \\ -2 \end{pmatrix} = \begin{pmatrix} 7 \\ -6 \\ 11 \end{pmatrix}$$

**Dirección:** $\vec{d} = (3, -10, 4)$, con $\|\vec{d}\|^2 = 9 + 100 + 16 = 125$.

**Proyección sobre $\vec{d}$:**
$$\vec{v} \cdot \vec{d} = 21 + 60 + 44 = 125 \quad \Longrightarrow \quad \text{proj}_{\vec{d}}\,\vec{v} = \frac{125}{125}\,\vec{d} = \begin{pmatrix} 3 \\ -10 \\ 4 \end{pmatrix}$$

**Componente perpendicular:**
$$\vec{v} - \text{proj}_{\vec{d}}\,\vec{v} = \begin{pmatrix} 7 - 3 \\ -6 + 10 \\ 11 - 4 \end{pmatrix} = \begin{pmatrix} 4 \\ 4 \\ 7 \end{pmatrix}$$

**Distancia:**
$$\sqrt{16 + 16 + 49} = \sqrt{81} = 9$$

\boxed{9}