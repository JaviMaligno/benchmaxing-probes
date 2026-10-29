## Planteamiento

**Paso 1: el triángulo $AEF$ es semejante a $ABC$.**

Como $BEF C$... más directamente: $B$, $C$, $E$, $F$ son concíclicos (circunferencia de diámetro $BC$), de donde $\angle AFE = \angle ACB$. Entonces $\triangle AEF \sim \triangle ABC$ con razón $\cos A$.

**Paso 2: calcular $\cos A$.**

Bajo esa semejanza, la altura $AQ$ de $\triangle AEF$ corresponde a la altura $AD$ de $\triangle ABC$:
$$AQ = AD\cos A \quad\Longrightarrow\quad \cos A = \frac{20}{24} = \frac56,\qquad \sin A = \frac{\sqrt{11}}{6}.$$

**Paso 3: área y circunradio.**

$$[ABC] = \tfrac12\cdot BC\cdot AD = \tfrac12\cdot 15\cdot 24 = 180,\qquad R = \frac{a}{2\sin A} = \frac{15}{2\cdot\frac{\sqrt{11}}{6}} = \frac{45}{\sqrt{11}}.$$

**Paso 4: perímetro del triángulo órtico.**

Los lados son $EF = a\cos A$, $FD = b\cos B$, $DE = c\cos C$, luego
$$p = a\cos A + b\cos B + c\cos C = R(\sin 2A+\sin 2B+\sin 2C) = 4R\sin A\sin B\sin C = \frac{2[ABC]}{R}.$$

Por tanto
$$p = \frac{2\cdot 180}{45/\sqrt{11}} = \frac{360\sqrt{11}}{45} = 8\sqrt{11}.$$

(Comprobación: con estos datos $b\approx 26.96$, $c\approx 24.15$, el triángulo es acutángulo y la suma de lados del órtico da $\approx 26.53 = 8\sqrt{11}$.)

\boxed{8\sqrt{11}}