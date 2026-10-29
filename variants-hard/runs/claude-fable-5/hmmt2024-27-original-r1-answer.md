**Planteamiento.** Sean $D, E, F$ los pies de las alturas (triángulo órtico) y $Q$ el pie de la perpendicular desde $A$ a $EF$.

**Paso 1: hallar $\cos A$.** Es conocido que el triángulo $AEF$ es semejante al triángulo $ABC$ con razón $\cos A$ (pues $AE = AB\cos A$ y $AF = AC\cos A$). La altura desde $A$ en $AEF$ (que es $AQ$) corresponde a la altura desde $A$ en $ABC$ (que es $AD$), así que:
$$AQ = AD\cos A \implies 20 = 24\cos A \implies \cos A = \tfrac{5}{6},\quad \sin A = \tfrac{\sqrt{11}}{6}.$$

**Paso 2: circunradio y área de $ABC$.** Con $BC = a = 15$:
$$R = \frac{a}{2\sin A} = \frac{15}{2\cdot \frac{\sqrt{11}}{6}} = \frac{45}{\sqrt{11}},\qquad [ABC] = \tfrac12 \cdot BC \cdot AD = \tfrac12\cdot 15\cdot 24 = 180.$$

**Paso 3: perímetro del triángulo órtico.** Los lados del triángulo órtico miden $EF = a\cos A$, $FD = b\cos B$, $DE = c\cos C$, de modo que
$$p = a\cos A + b\cos B + c\cos C = R(\sin 2A+\sin 2B+\sin 2C) = 4R\sin A\sin B\sin C.$$
Como $[ABC] = 2R^2 \sin A \sin B \sin C$, se obtiene la fórmula $p = \dfrac{2[ABC]}{R}$. Por lo tanto:
$$p = \frac{2\cdot 180}{45/\sqrt{11}} = \frac{360\sqrt{11}}{45} = 8\sqrt{11}.$$

$$\boxed{8\sqrt{11}}$$