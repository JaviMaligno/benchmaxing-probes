Para calcular el perímetro del cuadrilátero convexo $WXYZ$, nombremos los ángulos dados como:
$$\alpha = \angle QWX = \angle QZW, \quad \beta = \angle QWZ = \angle QZY, \quad \gamma = \angle QXW = \angle QYX, \quad \delta = \angle QXY = \angle QYZ.$$

### Paso 1: Relación entre los ángulos y longitud de $QZ$
Consideremos los cuatro triángulos que comparten el vértice $Q$: $\triangle QWX$, $\triangle QXY$, $\triangle QYZ$ y $\triangle QZW$. La suma de los ángulos internos de estos cuatro triángulos alrededor de $Q$ es $360^\circ$:
$$\angle WQX + \angle XQY + \angle YQZ + \angle ZQW = 360^\circ$$
$$(180^\circ - \alpha - \gamma) + (180^\circ - \gamma - \delta) + (180^\circ - \beta - \delta) + (180^\circ - \alpha - \beta) = 360^\circ$$
Simplificando, obtenemos:
$$\alpha + \beta + \gamma + \delta = 180^\circ.$$

Por lo tanto, los ángulos en el punto $Q$ son:
- $\angle WQX = 180^\circ - (\alpha + \gamma) = \beta + \delta$
- $\angle YQZ = 180^\circ - (\beta + \delta) = \alpha + \gamma$
- $\angle XQY = 180^\circ - (\gamma + \delta) = \alpha + \beta$
- $\angle ZQW = 180^\circ - (\alpha + \beta) = \gamma + \delta$

Aplicando la Ley de Senos en cada uno de los cuatro triángulos:
1. En $\triangle QWX$: $\frac{\sin\alpha}{\sin\gamma} = \frac{QX}{QW} = \frac{5}{3}$.
2. En $\triangle QXY$: $\frac{\sin\delta}{\sin\gamma} = \frac{QY}{QX} = \frac{10}{5} = 2$.
3. En $\triangle QZW$: $\frac{\sin\beta}{\sin\alpha} = \frac{QZ}{QW} = \frac{QZ}{3}$.
4. En $\triangle QYZ$: $\frac{\sin\beta}{\sin\delta} = \frac{QY}{QZ} = \frac{10}{QZ}$.

Dividiendo las expresiones de (3) y (4) y comparando con (1) y (2):
$$\frac{\sin\delta}{\sin\alpha} = \frac{QZ^2}{3 \cdot 10} = \frac{2}{5/3} = \frac{6}{5} \implies QZ^2 = 36 \implies QZ = 6.$$

Si definimos $t = \frac{\sin\gamma}{3}$, entonces:
$$\sin\gamma = 3t, \quad \sin\alpha = 5t, \quad \sin\delta = 6t, \quad \sin\beta = 10t.$$

---

### Paso 2: Cálculo de $WX$ y $YZ$
Por la Ley de Senos en $\triangle QWX$ y $\triangle QYZ$:
$$WX = \frac{QW \sin(\alpha+\gamma)}{\sin\gamma} = \frac{\sin(\alpha+\gamma)}{t}, \quad YZ = \frac{QZ \sin(\beta+\delta)}{\sin\delta} = \frac{6\sin(\alpha+\gamma)}{6t} = \frac{\sin(\alpha+\gamma)}{t}.$$
De aquí deducimos que $WX = YZ$.

Aplicando la Ley de Cosenos en $\triangle QWX$ (donde $\angle WQX = 180^\circ - (\alpha+\gamma)$) y en $\triangle QYZ$ (donde $\angle YQZ = \alpha+\gamma$):
$$WX^2 = 3^2 + 5^2 - 2(3)(5)\cos(180^\circ - (\alpha+\gamma)) = 34 + 30\cos(\alpha+\gamma)$$
$$YZ^2 = 6^2 + 10^2 - 2(6)(10)\cos(\alpha+\gamma) = 136 - 120\cos(\alpha+\gamma)$$

Como $WX^2 = YZ^2$, igualamos ambas expresiones:
$$34 + 30\cos(\alpha+\gamma) = 136 - 120\cos(\alpha+\gamma) \implies 150\cos(\alpha+\gamma) = 102 \implies \cos(\alpha+\gamma) = \frac{17}{25}.$$

Sustituyendo este valor obtenemos:
$$WX^2 = YZ^2 = 34 + 30\left(\frac{17}{25}\right) = \frac{272}{5} = \frac{16 \cdot 85}{25} \implies WX = YZ = \frac{4\sqrt{85}}{5}.$$

---

### Paso 3: Cálculo de $XY$ y $ZW$
Por la Ley de Senos en $\triangle QXY$ y $\triangle QZW$:
$$XY = \frac{QX \sin(\gamma+\delta)}{\sin\gamma} = \frac{5\sin(\gamma+\delta)}{3t}, \quad ZW = \frac{QW \sin(\alpha+\beta)}{\sin\alpha} = \frac{3\sin(\gamma+\delta)}{5t}.$$
Por lo tanto, la razón entre ambos lados es $\frac{XY}{ZW} = \frac{25}{9}$.

Aplicando la Ley de Cosenos en $\triangle QXY$ (donde $\angle XQY = 180^\circ - (\gamma+\delta)$) y en $\triangle QZW$ (donde $\angle ZQW = \gamma+\delta$):
$$XY^2 = 5^2 + 10^2 - 2(5)(10)\cos(180^\circ - (\gamma+\delta)) = 125 + 100\cos(\gamma+\delta) = 25\big(5 + 4\cos(\gamma+\delta)\big)$$
$$ZW^2 = 3^2 + 6^2 - 2(3)(6)\cos(\gamma+\delta) = 45 - 36\cos(\gamma+\delta) = 9\big(5 - 4\cos(\gamma+\delta)\big)$$

Usando que $\frac{XY^2}{ZW^2} = \left(\frac{25}{9}\right)^2$:
$$\frac{25\big(5 + 4\cos(\gamma+\delta)\big)}{9\big(5 - 4\cos(\gamma+\delta)\big)} = \frac{25^2}{9^2} \implies 9\big(5 + 4\cos(\gamma+\delta)\big) = 25\big(5 - 4\cos(\gamma+\delta)\big)$$
$$45 + 36\cos(\gamma+\delta) = 125 - 100\cos(\gamma+\delta) \implies 136\cos(\gamma+\delta) = 80 \implies \cos(\gamma+\delta) = \frac{10}{17}.$$

Sustituyendo para hallar $XY$ y $ZW$:
$$XY = 5\sqrt{5 + \frac{40}{17}} = 5\sqrt{\frac{125}{17}} = \frac{25\sqrt{85}}{17}$$
$$ZW = 3\sqrt{5 - \frac{40}{17}} = 3\sqrt{\frac{45}{17}} = \frac{9\sqrt{85}}{17}$$

---

### Paso 4: Perímetro de $WXYZ$
Sumando las longitudes de los cuatro lados:
$$\text{Perímetro} = WX + YZ + XY + ZW = \frac{4\sqrt{85}}{5} + \frac{4\sqrt{85}}{5} + \frac{25\sqrt{85}}{17} + \frac{9\sqrt{85}}{17} = \frac{8\sqrt{85}}{5} + 2\sqrt{85} = \frac{18\sqrt{85}}{5}.$$

\boxed{\frac{18\sqrt{85}}{5}}