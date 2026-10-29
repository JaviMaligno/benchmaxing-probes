Resuelvo el problema de geometría paso a paso.

**Configuración.** En el triángulo acutángulo $XYZ$, los pies de las alturas $P, R, S$ forman el triángulo órtico. Uso la similitud clásica: como $XR = XY\cos X$ y $XS = XZ\cos X$, el triángulo $XSR$ es semejante al triángulo $XZY$ con razón $\cos X$.

**Hallar $\cos X$.** En esa semejanza, la altura desde $X$ hasta $RS$ (que es $XT$) corresponde a la altura desde $X$ hasta $YZ$ (que es $XP$), escalada por $\cos X$:
$$XT = XP\cos X \implies 15 = 20\cos X \implies \cos X = \tfrac34,\quad \sin X = \tfrac{\sqrt7}{4}.$$

**Datos derivados.** El circunradio de $XYZ$:
$$R_{\text{circ}} = \frac{YZ}{2\sin X} = \frac{16}{2\cdot \frac{\sqrt7}{4}} = \frac{32}{\sqrt7}.$$
El área de $XYZ$:
$$[XYZ] = \tfrac12 \cdot YZ \cdot XP = \tfrac12\cdot 16\cdot 20 = 160.$$

**Perímetro del triángulo órtico.** Cada lado del triángulo órtico vale (lado opuesto)·(coseno del ángulo correspondiente), así que el perímetro es
$$a\cos A + b\cos B + c\cos C = R_{\text{circ}}(\sin 2A+\sin 2B+\sin 2C) = 4R_{\text{circ}}\sin A\sin B\sin C = \frac{2\,[XYZ]}{R_{\text{circ}}}.$$

Sustituyendo:
$$\text{perímetro} = \frac{2\cdot 160}{32/\sqrt7} = \frac{320\sqrt7}{32} = 10\sqrt7.$$

(Verificación rápida: $RS = 16\cos X = 12$, consistente con la semejanza.)

$$\boxed{10\sqrt{7}}$$