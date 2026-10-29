## Solución

**Notación.** Escribo $\angle X,\angle Y,\angle Z$ para los ángulos en $X,Y,Z$ y $x=YZ=16$, $y=ZX$, $z=XY$, $h=XP=20$, $K$ = área. El triángulo $PRS$ es el *triángulo órtico* de $XYZ$.

**Paso 1: los triángulos $XRS$ y $XYZ$ son semejantes con razón $\cos X$.**

Como $\angle YRX=90^\circ$, en el triángulo rectángulo $YRX$ (con hipotenusa $XY$ y ángulo $\angle YXZ=\angle X$ en $X$):
$$XR = XY\cos X = z\cos X.$$
Análogamente $\angle XSZ=90^\circ$ da $XS = XZ\cos X = y\cos X$. Como $\angle RXS = \angle YXZ$, la semejanza $XRS\sim XYZ$ (con $X\leftrightarrow X$, $R\leftrightarrow Y$, $S\leftrightarrow Z$) tiene razón $\cos X$. Por lo tanto:

* la distancia de $X$ a $RS$ es $\cos X$ veces la distancia de $X$ a $YZ$: 
$$XT = XP\cos X = 20\cos X;$$
* $RS = YZ\cos X = 16\cos X$.

**Paso 2: determinar $\cos X$.**

$$\cos X = \frac{XT}{XP} = \frac{15}{20} = \frac34, \qquad \sin X = \frac{\sqrt7}{4}, \qquad RS = 16\cdot\tfrac34 = 12.$$

**Paso 3: los otros dos lados del órtico.**

El mismo argumento en el vértice $Z$: $ZP = ZX\cos Z$ y $ZR = ZY\cos Z$, así que $ZPR\sim ZXY$ con razón $\cos Z$, y $PR = XY\cos Z = z\cos Z$. Igualmente $PS = y\cos Y$. Entonces, con $x=2R_{circ}\sin X$ (ley de senos) y la identidad $\sin 2X+\sin 2Y+\sin 2Z = 4\sin X\sin Y\sin Z$ (válida pues $X+Y+Z=180^\circ$):

$$\text{Per\u00edim}(PRS) = R_{circ}(\sin 2X+\sin 2Y+\sin 2Z) = 4R_{circ}\sin X\sin Y\sin Z.$$

**Paso 4: simplificar todo.**

El área es $K = \tfrac12 xh = 160$ y $R_{circ} = \dfrac{xyz}{4K}$. Además, como $\angle XPY=\angle XPZ=90^\circ$, de los triángulos rectángulos $XPY$ y $XPZ$:
$$\sin Y = \frac{h}{z}, \qquad \sin Z = \frac{h}{y}.$$

Sustituyendo:

$$\text{Per\u00edim} = 4\cdot\frac{xyz}{4K}\cdot\sin X\cdot\frac{h}{z}\cdot\frac{h}{y} = \frac{x h^2 \sin X}{K} = \frac{x h^2\sin X}{xh/2} = 2h\sin X = 40\cdot\frac{\sqrt7}{4}=10\sqrt7.$$

(Comprobación numérica: con $PY\approx 2.82$, $PZ\approx 13.18$ se cumple $\cos X=\tfrac34$ y se obtiene $PR+PS+RS\approx 11.11+3.34+12.00\approx 26.46 = 10\sqrt7$. ✓)

\boxed{10\sqrt{7}}