# Distancia entre dos rectas paralelas

## Verificar el paralelismo

Los vectores dirección son $\mathbf{d} = (3, -10, 4)$ y $\mathbf{e} = (-6, 20, -8)$. Como
$$\mathbf{e} = -2\,\mathbf{d},$$
los vectores son proporcionales, así que las rectas son efectivamente paralelas.

## Fórmula

Para rectas paralelas, la distancia es la longitud de la componente del vector entre un punto de cada recta, perpendicular a $\mathbf{d}$:
$$D = \frac{\|\mathbf{v} \times \mathbf{d}\|}{\|\mathbf{d}\|}, \quad \text{donde } \mathbf{v} = \overrightarrow{P_0Q_0}.$$

## Paso 1: Vector entre los puntos

Con $P_0 = (1, 5, -2)$ y $Q_0 = (8, -1, 9)$:
$$\mathbf{v} = (8-1,\; -1-5,\; 9+2) = (7, -6, 11).$$

## Paso 2: Producto cruz $\mathbf{v} \times \mathbf{d}$

$$\mathbf{v} \times \mathbf{d} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 7 & -6 & 11 \\ 3 & -10 & 4 \end{vmatrix}$$

- Componente $x$: $(-6)(4) - (11)(-10) = -24 + 110 = 86$
- Componente $y$: $(11)(3) - (7)(4) = 33 - 28 = 5$
- Componente $z$: $(7)(-10) - (-6)(3) = -70 + 18 = -52$

$$\mathbf{v} \times \mathbf{d} = (86, 5, -52)$$

## Paso 3: Normas

$$\|\mathbf{v} \times \mathbf{d}\| = \sqrt{86^2 + 5^2 + 52^2} = \sqrt{7396 + 25 + 2704} = \sqrt{10125} = 45\sqrt{5}$$

$$\|\mathbf{d}\| = \sqrt{9 + 100 + 16} = \sqrt{125} = 5\sqrt{5}$$

## Paso 4: Distancia

$$D = \frac{45\sqrt{5}}{5\sqrt{5}} = 9$$

**Verificación** (proyecciones): $\|\mathbf{v}\|^2 = 206$, $\ \mathbf{v}\cdot\mathbf{d} = 125$, así que
$$D = \sqrt{206 - \tfrac{125^2}{125}} = \sqrt{206 - 125} = \sqrt{81} = 9. \checkmark$$

$$\boxed{9}$$