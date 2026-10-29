## Razonamiento

Sea $w + \dfrac{1}{w} = \dfrac{\sqrt5-1}{2}$.

**Paso 1: identificar el ángulo.**
Si escribimos $w = e^{i\theta}$, entonces $w + \frac1w = 2\cos\theta$, de modo que
$$\cos\theta = \frac{\sqrt5-1}{4} \approx 0{,}309.$$

Este es exactamente el valor conocido $\cos 72^\circ = \cos\frac{2\pi}{5} = \frac{\sqrt5-1}{4}$.

Por tanto $w = e^{\pm 2\pi i/5}$.

**Paso 2: verificación algebraica.**
De $w+\frac1w = \frac{\sqrt5-1}{2}$ se obtiene $w^2 - \frac{\sqrt5-1}{2}w + 1 = 0$. Como $\frac{\sqrt5-1}{2}$ satisface $x^2 + x - 1 = 0$, un cálculo directo da que $w$ es raíz de
$$w^4 + w^3 + w^2 + w + 1 = 0,$$
es decir, $w$ es una raíz quinta primitiva de la unidad: $w^5 = 1$.

*(Comprobación: $w^2+\frac{1}{w^2} = \left(\frac{\sqrt5-1}{2}\right)^2 - 2 = \frac{3-\sqrt5}{2}-2 = \frac{-1-\sqrt5}{2}$, y entonces $w+\frac1w + w^2+\frac1{w^2} = \frac{\sqrt5-1}{2}+\frac{-1-\sqrt5}{2} = -1$, lo que confirma $1+w+w^2+w^3+w^4=0$.)*

**Paso 3: reducir el exponente.**
Como $95 = 5 \cdot 19$,
$$w^{95} = (w^5)^{19} = 1^{19} = 1.$$

Luego
$$w^{95} + \frac{1}{w^{95}} = 1 + 1 = 2.$$

\boxed{2}