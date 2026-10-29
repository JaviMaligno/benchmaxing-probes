## Planteamiento

Esta es la configuración clásica del **teorema de Sawayama–Thébault**: dado un punto $X$ sobre $QR$, las circunferencias $\gamma_1$ (inscrita en el ángulo $\angle PXQ$, tangente internamente a $\Gamma$) y $\gamma_2$ (inscrita en $\angle PXR$, tangente a $\Gamma$) satisfacen, con $\angle PXQ = 2\theta$:

$$r = r_1\cos^2\theta + r_2\sin^2\theta,$$

donde $r$ es el inradio de $\triangle PQR$ (el incentro queda sobre la recta que une los centros $O_1O_2$).

## Distancia entre centros

- $O_1$ está sobre la bisectriz de $\angle PXQ = 2\theta$, a distancia $XO_1 = \dfrac{r_1}{\sin\theta}$.
- $O_2$ está sobre la bisectriz de $\angle PXR = \pi - 2\theta$, a distancia $XO_2 = \dfrac{r_2}{\cos\theta}$.

El ángulo entre ambas bisectrices es $\theta + \left(\tfrac{\pi}{2}-\theta\right) = 90^\circ$, así que el triángulo $O_1XO_2$ es rectángulo en $X$:

$$d^2 = \frac{r_1^2}{\sin^2\theta} + \frac{r_2^2}{\cos^2\theta}.$$

## Ecuación

Con $r_1 = 4$, $r_2 = 6$, $d = 11$ y $s = \sin^2\theta$:

$$\frac{16}{s} + \frac{36}{1-s} = 121 \;\Longrightarrow\; 16(1-s) + 36s = 121s(1-s) \;\Longrightarrow\; 121s^2 - 101s + 16 = 0.$$

El discriminante es $10201 - 7744 = 2457 > 0$, con raíces $s = \dfrac{101 \pm 3\sqrt{273}}{242} \approx 0.622$ y $0.212$, ambas en $(0,1)$, de modo que las dos configuraciones son válidas (corresponden a inclinar $PX$ hacia un lado u otro).

Por Vieta: $s_1 + s_2 = \dfrac{101}{121}$.

## Inradio

$$r = 4\cos^2\theta + 6\sin^2\theta = 4 + 2s.$$

La suma de los posibles valores:

$$r_{(1)} + r_{(2)} = 8 + 2(s_1+s_2) = 8 + \frac{202}{121} = \frac{968 + 202}{121} = \frac{1170}{121}.$$

(Nótese que si se intercambia la asignación de $\theta$, la ecuación se transforma con $s \leftrightarrow 1-s$ y la suma resulta la misma, así que el resultado no depende de esa convención.)

$$\boxed{\dfrac{1170}{121}}$$