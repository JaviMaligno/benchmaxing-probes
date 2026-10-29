Para hallar el área del cuadrilátero $QXYR$, descomponemos el triángulo rectángulo $\triangle PQR$ utilizando los puntos interiores $X$ e $Y$.

### Paso 1: Análisis de ángulos y lados en función de $s = 26$
Sea $s = 26$. Como $PX = PY = XY = s$, el triángulo $\triangle PXY$ es equilátero, por lo que $\angle XPY = 60^\circ$.

Dado que $X$ e $Y$ están dentro de $\triangle PQR$ y $\angle QPR = 90^\circ$, definimos $\alpha = \angle QPX$ y $\beta = \angle YPR$. Entonces:
$$\alpha + \beta = 90^\circ - 60^\circ = 30^\circ.$$

En el triángulo isósceles $\triangle PQX$, tenemos $PX = QX = s$. Trazando la altura desde $X$ hacia $PQ$, obtenemos:
$$PQ = 2s \cos \alpha.$$

De manera análoga, en el triángulo isósceles $\triangle PYR$, como $PY = RY = s$, tenemos:
$$PR = 2s \cos \beta.$$

### Paso 2: Uso del teorema de Pitágoras en $\triangle PQR$
En el triángulo rectángulo $\triangle PQR$, se cumple $PQ^2 + PR^2 = QR^2$. Sustituyendo $QR = 4\sqrt{301}$ y $s = 26$:
$$4s^2 (\cos^2 \alpha + \cos^2 \beta) = (4\sqrt{301})^2 = 16 \cdot 301.$$

Como $4s^2 = 4 \cdot 26^2 = 16 \cdot 169$, dividimos ambos lados por $16 \cdot 169$:
$$\cos^2 \alpha + \cos^2 \beta = \frac{301}{169}.$$

Usando la identidad trigonométrica $\cos^2 \alpha + \cos^2 \beta = 1 + \cos(\alpha + \beta)\cos(\alpha - \beta)$ y sabiendo que $\alpha + \beta = 30^\circ$:
$$1 + \frac{\sqrt{3}}{2}\cos(\alpha - \beta) = \frac{301}{169} \implies \frac{\sqrt{3}}{2}\cos(\alpha - \beta) = \frac{132}{169}.$$

Despejando $\cos(\alpha - \beta)$:
$$\cos(\alpha - \beta) = \frac{264}{169\sqrt{3}} = \frac{88\sqrt{3}}{169}.$$

### Paso 3: Cálculo del área de $QXYR$
El área del cuadrilátero $QXYR$ se obtiene restando del área total de $\triangle PQR$ las áreas de los triángulos $\triangle PQX$, $\triangle PYR$ y $\triangle PXY$:
$$\text{Área}(QXYR) = \text{Área}(\triangle PQR) - \left(\text{Área}(\triangle PQX) + \text{Área}(\triangle PYR)\right) - \text{Área}(\triangle PXY).$$

Calculamos cada término en función de $s$:
1. $\text{Área}(\triangle PQR) = \frac{1}{2} PQ \cdot PR = 2s^2 \cos \alpha \cos \beta = s^2 \left(\cos(\alpha - \beta) + \cos(\alpha + \beta)\right) = s^2 \left(\cos(\alpha - \beta) + \frac{\sqrt{3}}{2}\right).$
2. $\text{Área}(\triangle PQX) + \text{Área}(\triangle PYR) = \frac{1}{2} s \cdot PQ \sin \alpha + \frac{1}{2} s \cdot PR \sin \beta = \frac{s^2}{2}(\sin 2\alpha + \sin 2\beta) = s^2 \sin(\alpha + \beta)\cos(\alpha - \beta) = \frac{1}{2}s^2 \cos(\alpha - \beta).$
3. $\text{Área}(\triangle PXY) = \frac{\sqrt{3}}{4}s^2.$

Sustituyendo estas expresiones en la ecuación del área:
$$\text{Área}(QXYR) = s^2 \left( \cos(\alpha - \beta) + \frac{\sqrt{3}}{2} - \frac{1}{2}\cos(\alpha - \beta) - \frac{\sqrt{3}}{4} \right) = s^2 \left( \frac{1}{2}\cos(\alpha - \beta) + \frac{\sqrt{3}}{4} \right).$$

Reemplazando $s^2 = 26^2 = 4 \cdot 169$ y $\cos(\alpha - \beta) = \frac{88\sqrt{3}}{169}$:
$$\text{Área}(QXYR) = 4 \cdot 169 \left( \frac{44\sqrt{3}}{169} + \frac{\sqrt{3}}{4} \right) = 4 \cdot 44\sqrt{3} + 169\sqrt{3} = 176\sqrt{3} + 169\sqrt{3} = 345\sqrt{3}.$$

Por lo tanto, el valor de $n$ es $345$.

\boxed{345}