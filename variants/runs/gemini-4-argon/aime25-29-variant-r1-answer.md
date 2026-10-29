Para hallar el área del cuadrilátero $QXYR$, analicemos primero la configuración geométrica del triángulo rectángulo $\triangle PQR$.

### Paso 1: Planteamiento geométrico y ángulos
Sea $a = 26$. Sabemos que:
$$PX = PY = QX = RY = XY = a = 26.$$

Como $PX = PY = XY = a$, el triángulo $\triangle PXY$ es equilátero, por lo que $\angle XPY = 60^\circ$.
Además, dado que $PX = QX = a$, el triángulo $\triangle PQX$ es isósceles con base $PQ$. De manera análoga, como $PY = RY = a$, el triángulo $\triangle PRY$ es isósceles con base $PR$.

Sean $\alpha = \angle QPX$ y $\beta = \angle RPY$. Como $X$ e $Y$ se encuentran en el interior de $\triangle PQR$ y $\angle QPR = 90^\circ$, los rayos $PX$ y $PY$ dividen el ángulo recto en tres partes tales que:
$$\alpha + 60^\circ + \beta = 90^\circ \implies \alpha + \beta = 30^\circ.$$
*(Nota: Si los rayos $PX$ y $PY$ estuvieran cruzados en orden inverso, tendríamos $\alpha + \beta = 150^\circ$, lo que situaría a $X$ e $Y$ fuera del triángulo $\triangle PQR$).*

### Paso 2: Relación con la hipotenusa $QR$
Trazando las alturas desde $X$ hacia $PQ$ y desde $Y$ hacia $PR$ en los triángulos isósceles $\triangle PQX$ y $\triangle PRY$, obtenemos las longitudes de los catetos de $\triangle PQR$:
$$PQ = 2a \cos \alpha, \qquad PR = 2a \cos \beta.$$

Por el teorema de Pitágoras en $\triangle PQR$, tenemos:
$$PQ^2 + PR^2 = QR^2 \implies 4a^2(\cos^2 \alpha + \cos^2 \beta) = (4\sqrt{301})^2.$$

Sustituyendo $a = 26$:
$$4(26^2)(\cos^2 \alpha + \cos^2 \beta) = 16 \times 301 \implies 169(\cos^2 \alpha + \cos^2 \beta) = 301 \implies \cos^2 \alpha + \cos^2 \beta = \frac{301}{169}.$$

Usando las identidades de reducción de potencias y suma a producto:
$$\cos^2 \alpha + \cos^2 \beta = \frac{1 + \cos 2\alpha}{2} + \frac{1 + \cos 2\beta}{2} = 1 + \cos(\alpha + \beta)\cos(\alpha - \beta).$$

Dado que $\alpha + \beta = 30^\circ$, sabemos que $\cos(\alpha + \beta) = \frac{\sqrt{3}}{2}$. Sustituyendo esto en la ecuación anterior:
$$1 + \frac{\sqrt{3}}{2}\cos(\alpha - \beta) = \frac{301}{169} \implies \frac{\sqrt{3}}{2}\cos(\alpha - \beta) = \frac{132}{169} \implies \cos(\alpha - \beta) = \frac{88\sqrt{3}}{169}.$$

### Paso 3: Cálculo del área de $QXYR$
El área del cuadrilátero $QXYR$ se obtiene restando del área total del triángulo $\triangle PQR$ las áreas de los triángulos $\triangle PQX$, $\triangle PRY$ y $\triangle PXY$:
$$[QXYR] = [\triangle PQR] - [\triangle PQX] - [\triangle PRY] - [\triangle PXY].$$

Calculamos cada término en función de $a$, $\alpha$ y $\beta$:
1. $[\triangle PQR] = \frac{1}{2} PQ \cdot PR = 2a^2 \cos\alpha \cos\beta = a^2\big(\cos(\alpha + \beta) + \cos(\alpha - \beta)\big) = a^2\left(\frac{\sqrt{3}}{2} + \cos(\alpha - \beta)\right)$.
2. $[\triangle PQX] + [\triangle PRY] = \frac{1}{2} a^2 \sin 2\alpha + \frac{1}{2} a^2 \sin 2\beta = a^2 \sin(\alpha + \beta)\cos(\alpha - \beta) = \frac{1}{2}a^2 \cos(\alpha - \beta)$.
3. $[\triangle PXY] = \frac{\sqrt{3}}{4}a^2$.

Combinando todas las expresiones:
$$[QXYR] = a^2\left(\frac{\sqrt{3}}{2} + \cos(\alpha - \beta) - \frac{1}{2}\cos(\alpha - \beta) - \frac{\sqrt{3}}{4}\right) = a^2\left(\frac{\sqrt{3}}{4} + \frac{1}{2}\cos(\alpha - \beta)\right).$$

Sustituyendo $a^2 = 26^2 = 676$ y $\cos(\alpha - \beta) = \frac{88\sqrt{3}}{169}$:
$$[QXYR] = 676\left(\frac{\sqrt{3}}{4} + \frac{44\sqrt{3}}{169}\right) = 169\sqrt{3} + 4(44\sqrt{3}) = 169\sqrt{3} + 176\sqrt{3} = 345\sqrt{3}.$$

Por lo tanto, el valor de $n$ es $345$.

\boxed{345}