Para encontrar el perímetro del triángulo órtico $\triangle PRS$ del triángulo acutángulo $\triangle XYZ$, procedemos paso a paso:

### Paso 1: Relación de semejanza y cálculo de $\cos X$ y $\sin X$
Sean $R$ y $S$ los pies de las alturas desde $Y$ y $Z$ hacia los lados $\overline{ZX}$ y $\overline{XY}$, respectivamente. Como $\angle YRZ = \angle YSZ = 90^\circ$, el cuadrilátero $YZRS$ es cíclico con diámetro $\overline{YZ}$.

Por las propiedades de los cuadriláteros cíclicos, los ángulos interiores opuestos son suplementarios, lo que implica que $\angle XRS = \angle XYZ$ y $\angle XSR = \angle XZY$. Por lo tanto, los triángulos $\triangle XRS$ y $\triangle XYZ$ son semejantes ($\triangle XRS \sim \triangle XYZ$).

En el triángulo rectángulo $\triangle XRY$, tenemos que $\cos X = \frac{XR}{XY}$, por lo que la razón de semejanza entre $\triangle XRS$ y $\triangle XYZ$ es $\cos X$. 

Dado que $\overline{XT}$ es la altura desde $X$ hacia $\overline{RS}$ en $\triangle XRS$, y $\overline{XP}$ es la altura correspondiente desde $X$ hacia $\overline{YZ}$ en $\triangle XYZ$, la razón entre estas alturas es igual a la razón de semejanza de los triángulos:
$$\frac{XT}{XP} = \cos X$$

Sustituyendo los valores dados $XT = 15$ y $XP = 20$:
$$\cos X = \frac{15}{20} = \frac{3}{4}$$

Como el triángulo $\triangle XYZ$ es acutángulo, $\sin X > 0$, y por la identidad pitagórica obtenemos:
$$\sin X = \sqrt{1 - \cos^2 X} = \sqrt{1 - \left(\frac{3}{4}\right)^2} = \sqrt{1 - \frac{9}{16}} = \frac{\sqrt{7}}{4}$$

---

### Paso 2: Cálculo del circunradio y el área de $\triangle XYZ$
Sea $R_c$ el circunradio del triángulo $\triangle XYZ$. Por la Ley de los Senos aplicada a $\triangle XYZ$:
$$2R_c = \frac{YZ}{\sin X} = \frac{16}{\frac{\sqrt{7}}{4}} = \frac{64}{\sqrt{7}} \implies R_c = \frac{32}{\sqrt{7}}$$

Por otro lado, el área $[XYZ]$ del triángulo $\triangle XYZ$ es:
$$[XYZ] = \frac{1}{2} \cdot YZ \cdot XP = \frac{1}{2} \cdot 16 \cdot 20 = 160$$

---

### Paso 3: Perímetro del triángulo órtico $\triangle PRS$
De manera análoga a la semejanza $\triangle XRS \sim \triangle XYZ$ con razón $\cos X$, se cumple que $\triangle YPR \sim \triangle YZX$ con razón $\cos Y$ y $\triangle ZSP \sim \triangle ZXY$ con razón $\cos Z$. Por consiguiente, las longitudes de los lados del triángulo órtico $\triangle PRS$ son:
$$RS = YZ \cos X, \quad PR = XZ \cos Y, \quad PS = XY \cos Z$$

Usando la Ley de los Senos ($YZ = 2R_c \sin X$, $XZ = 2R_c \sin Y$, $XY = 2R_c \sin Z$), el perímetro $\mathcal{P}$ de $\triangle PRS$ se expresa como:
$$\mathcal{P} = 2R_c (\sin X \cos X + \sin Y \cos Y + \sin Z \cos Z) = R_c (\sin 2X + \sin 2Y + \sin 2Z)$$

Para cualquier triángulo donde $X + Y + Z = 180^\circ$, se cumple la identidad trigonométrica $\sin 2X + \sin 2Y + \sin 2Z = 4 \sin X \sin Y \sin Z$. Además, sabemos que el área de un triángulo en función de su circunradio es $[XYZ] = 2R_c^2 \sin X \sin Y \sin Z$. Combinando ambas expresiones:
$$\mathcal{P} = 4R_c \sin X \sin Y \sin Z = \frac{2[XYZ]}{R_c}$$

*(Nota: Como $2[XYZ] = YZ \cdot XP$ y $R_c = \frac{YZ}{2\sin X}$, esto también se simplifica directamente a $\mathcal{P} = 2 \cdot XP \cdot \sin X$).*

Sustituyendo los valores obtenidos:
$$\mathcal{P} = \frac{2 \cdot 160}{\frac{32}{\sqrt{7}}} = \frac{320 \sqrt{7}}{32} = 10\sqrt{7}$$

\boxed{10\sqrt{7}}