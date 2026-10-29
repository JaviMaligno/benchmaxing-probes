## Planteamiento

Este problema usa el **teorema de Sawayama–Thébault**: si $\angle ADB = 2\varphi$, y $\omega_2$, $\omega_3$ son las circunferencias de Thébault con radios $r_2, r_3$, entonces el inradio de $\triangle ABC$ es
$$r = r_2\cos^2\varphi + r_3\sin^2\varphi.$$

## Distancia entre centros

El centro $O_2$ está sobre la bisectriz de $\angle ADB$, a distancia $d_2 = \dfrac{5}{\sin\varphi}$ de $D$ (pues su distancia a $BC$ es 5). El centro $O_3$ está sobre la bisectriz de $\angle ADC = \pi - 2\varphi$, a distancia $d_3 = \dfrac{7}{\cos\varphi}$ de $D$.

Como $\angle ADB$ y $\angle ADC$ son suplementarios, sus bisectrices son **perpendiculares**, así que
$$O_2O_3^2 = \frac{25}{\sin^2\varphi} + \frac{49}{\cos^2\varphi} = 169.$$

## Resolviendo

Sea $s = \sin^2\varphi$:
$$\frac{25}{s} + \frac{49}{1-s} = 169 \;\Longrightarrow\; 25(1-s) + 49s = 169\,s(1-s) \;\Longrightarrow\; 169s^2 - 145s + 25 = 0.$$

El discriminante es $145^2 - 4\cdot169\cdot25 = 21025 - 16900 = 4125 > 0$, y ambas raíces están en $(0,1)$ (suma $\tfrac{145}{169}$, producto $\tfrac{25}{169}$), por lo que ambas configuraciones son válidas.

## Inradio

$$r = 5\cos^2\varphi + 7\sin^2\varphi = 5 + 2s.$$

La suma sobre las dos raíces es
$$\sum r = 10 + 2(s_1 + s_2) = 10 + 2\cdot\frac{145}{169} = \frac{1690 + 290}{169} = \frac{1980}{169}.$$

$$\boxed{\dfrac{1980}{169}}$$