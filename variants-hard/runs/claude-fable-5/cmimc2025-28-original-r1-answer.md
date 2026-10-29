## Planteamiento

Como $\overline{AB}$ es diámetro, $\angle ADB = \angle ACB = 90°$. Entonces, en el triángulo $EAB$, $D$ es el pie de la altura desde $B$ y $C$ el pie de la altura desde $A$. De los triángulos rectángulos:
$$\cos A = \frac{AD}{AB} = \frac{7}{20}, \qquad \cos B = \frac{BC}{AB} = \frac{13}{20}.$$

Por tanto $\sin A = \frac{3\sqrt{39}}{20}$, $\sin B = \frac{\sqrt{231}}{20}$, y el triángulo $ECD$ es semejante a $EBA$ con razón $\cos E$ (configuración órtica): $EC = EA\cos E$, $ED = EB\cos E$, $CD = AB\cos E$.

## El excentro cae sobre $\overline{AB}$

El $E$-excírculo de $ECD$ tiene centro $L$ sobre la bisectriz interna desde $E$, con $EL = \dfrac{s'}{\cos(E/2)}$, donde $s' = s\cos E$ es el semiperímetro de $ECD$ ($s$ el de $EAB$).

Comparando con el punto $P$ donde la bisectriz desde $E$ corta a $\overline{AB}$ (cuya distancia es $EP = \frac{2\,EA\cdot EB\cos(E/2)}{EA+EB}$), la igualdad $EL = EP$ se reduce, tras usar $\cos^2\frac{E}{2} = \frac{s(s-c)}{ab}$ y la ley de cosenos, a la condición
$$\cos A + \cos B = 1,$$
que aquí se cumple exactamente: $\frac{7}{20}+\frac{13}{20}=1$. **Entonces $L$ está sobre $\overline{AB}$**, en el pie de la bisectriz desde $E$. (Verificado numéricamente: $L \approx (-1.042,\,0)$ con $O$ en el origen.)

## Cálculo de $OL$

Por el teorema de la bisectriz, $AL = \dfrac{AB\cdot EA}{EA+EB} = \dfrac{20\sin B}{\sin A + \sin B}$:

$$AL = \frac{20\sqrt{231}}{3\sqrt{39}+\sqrt{231}} = \frac{20\sqrt{77}}{3\sqrt{13}+\sqrt{77}} = \frac{20\sqrt{77}\,(\sqrt{77}-3\sqrt{13})}{77-117} = \frac{3\sqrt{1001}-77}{2}.$$

Como $O$ está a distancia $10$ de $A$:

$$OL = 10 - AL = 10 - \frac{3\sqrt{1001}-77}{2} = \frac{97 - 3\sqrt{1001}}{2} \approx 1.0421.$$

$$\boxed{\dfrac{97 - 3\sqrt{1001}}{2}}$$