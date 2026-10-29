## Razonamiento

**Identificar el ángulo.** Si escribimos $w + \dfrac1w = 2\cos\theta$, entonces
$$\cos\theta = \frac{\sqrt5-1}{4}.$$

Este es un valor conocido: $\cos 72^\circ = \dfrac{\sqrt5-1}{4}$.

(Verificación: si $c=\cos 72^\circ$, entonces $4c^2+2c-1=0$, cuya raíz positiva es $\frac{-1+\sqrt5}{4}$.)

**Determinar $w$.** Por tanto $\theta = 72^\circ = \dfrac{2\pi}{5}$, y
$$w = e^{\pm 2\pi i/5},$$
una raíz quinta primitiva de la unidad, es decir $w^5 = 1$.

(Alternativamente, sin trigonometría: de $w+\frac1w=\frac{\sqrt5-1}{2}$ se obtiene $w^2 - \frac{\sqrt5-1}{2}w + 1 = 0$. Multiplicando y usando que $\frac{\sqrt5-1}{2}$ satisface $x^2+x-1=0$, se llega a $w^4+w^3+w^2+w+1=0$, luego $w^5=1$ con $w \neq 1$.)

**Reducir el exponente.** Como $95 = 5 \cdot 19$:
$$w^{95} = (w^5)^{19} = 1^{19} = 1.$$

**Concluir.**
$$w^{95} + \frac{1}{w^{95}} = 1 + 1 = 2.$$

$$\boxed{2}$$