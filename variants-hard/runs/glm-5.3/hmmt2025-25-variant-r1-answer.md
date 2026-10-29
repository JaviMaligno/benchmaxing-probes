## Planteamiento

**Circunradio.** Para un triángulo equilátero de lado $9$, el circunradio es $R = \dfrac{9}{\sqrt3} = 3\sqrt{3}$, con centro $O$.

**Lugar geométrico de $Q$.** Como $\angle EQF = 120^\circ$ y $EF = 9$, el circunradio de $\triangle EFQ$ es
$$\frac{EF}{2\operatorname{sen}\angle EQF} = \frac{9}{2\cdot \frac{\sqrt3}{2}} = 3\sqrt{3} = R.$$
Es decir, $Q$ está sobre la circunferencia de radio $R$ con centro $O'$, el reflejo de $O$ respecto a la recta $EF$. Como $Q$ es interior y el ángulo es $120^\circ$ (no $60^\circ$), $Q$ está en el **arco menor** $EF$ de esa circunferencia.

**Coordenadas.** Pongo $O$ en el origen, $D = (R,0)$, $E$ y $F$ en ángulos $120^\circ$ y $240^\circ$. Entonces $O' = (-R, 0)$ y puedo escribir
$$Q = \big(R(\cos\varphi - 1),\; R\operatorname{sen}\varphi\big), \qquad |\varphi| < 60^\circ,$$
y $Y = (R\cos\psi, R\operatorname{sen}\psi)$ sobre la circunferencia circunscrita.

## Condición $DY = 7$

$$DY^2 = 2R^2(1 - \cos\psi) = 54(1-\cos\psi) = 49 \;\Longrightarrow\; \cos\psi = \frac{5}{54}. \tag{1}$$

## Condición de $Y$ en el círculo de diámetro $\overline{DQ}$

$Y$ está en el círculo de diámetro $DQ$ si y solo si $(Y-D)\cdot(Y-Q) = 0$. Sustituyendo $Y = R(\cos\psi,\operatorname{sen}\psi)$, $D = R(1,0)$, $Q = R(\cos\varphi - 1, \operatorname{sen}\varphi)$:

$$(Y-D)\cdot(Y-Q) = R^2\Big[\cos\psi - \cos(\psi - \varphi)\Big] \cdot(-1)\!\;\text{…}$$

concretamente el desarrollo da $(\cos\psi - 1)(\cos\psi + 1 - \cos\varphi) + \operatorname{sen}\psi(\operatorname{sen}\psi - \operatorname{sen}\varphi) = \cos\varphi - \cos(\psi - \varphi)$. Entonces:

$$\cos(\psi - \varphi) = \cos\varphi \;\Longrightarrow\; \psi = 0 \ (\text{descartado: } Y=D) \quad\text{o}\quad \boxed{\psi = 2\varphi}.$$

## Resolver

De $(1)$: $\cos 2\varphi = \dfrac{5}{54}$, luego
$$\cos^2\varphi = \frac{59}{108}, \qquad \operatorname{sen}^2\varphi = \frac{49}{108}, \qquad \cos\varphi = \frac{\sqrt{177}}{18} \approx 0.7391 \ (\varphi \approx \pm 42.3^\circ, \text{válido}).$$

**Cálculo de $YQ$.** Como $DQ$ es diámetro, $\angle DYQ = 90^\circ$, así que en el triángulo rectángulo $DYQ$:
$$DQ^2 = R^2\big[(2-\cos\varphi)^2 + \operatorname{sen}^2\varphi\big] = 27(5 - 4\cos\varphi) = 135 - 6\sqrt{177},$$
$$YQ^2 = DQ^2 - DY^2 = 86 - 6\sqrt{177}.$$

Finalmente, como $59 + 27 = 86$ y $2\cdot 3\sqrt{3}\cdot\sqrt{59} = 6\sqrt{177}$:
$$YQ^2 = \big(\sqrt{59} - 3\sqrt{3}\big)^2.$$

**Verificación numérica.** Con $\varphi \approx 42.35^\circ$: $Q \approx (-1.356,\, 3.5)$ (interior ✓), el producto punto en $Q$ da $\angle EQF = 120^\circ$ ✓, $(Y-D)\cdot(Y-Q) \approx 0$ ✓, $DY \approx 6.999$ ✓, y $YQ \approx 2.485 = \sqrt{59}-3\sqrt{3}$ ✓.

$$\boxed{\sqrt{59} - 3\sqrt{3}}$$