## Planteamiento

Escribimos $z + \dfrac1z = 2\cos\theta$ tomando $z = e^{i\theta}$ (válido porque $\left|\frac{1+\sqrt5}{2}\right| = 1{,}618 < 2$, así que $z$ está en el círculo unidad).

Entonces
$$2\cos\theta = \frac{1+\sqrt5}{2} \quad\Longrightarrow\quad \cos\theta = \frac{1+\sqrt5}{4}.$$

## Identificación del ángulo

El valor $\frac{1+\sqrt5}{4} \approx 0{,}80902$ es exactamente $\cos 36^\circ = \cos\frac{\pi}{5}$.

Comprobación: si $c = \cos 36^\circ$, se sabe que $\cos 36^\circ = \frac{\sqrt5+1}{4}$, y numéricamente $\frac{1+2{,}23607}{4} = 0{,}80902$. ✓

Luego $z = e^{i\pi/5}$ (la otra raíz es su conjugada, y da el mismo resultado).

## Cálculo de la potencia

$$z^{85} = e^{i\cdot 85\pi/5} = e^{i\cdot 17\pi} = e^{i\pi} = -1,$$

ya que $17$ es impar. Por tanto $\dfrac{1}{z^{85}} = -1$ también, y

$$z^{85} + \frac{1}{z^{85}} = -1 + (-1) = -2.$$

(Alternativamente: $z^{85} + z^{-85} = 2\cos(17\pi) = -2$.)

\boxed{-2}