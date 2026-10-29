Vamos a resolverlo paso a paso.

**Paso 1: Identificar el ángulo.** Recordemos que $\frac{1+\sqrt{5}}{2} = 2\cos 36^\circ = 2\cos\frac{\pi}{5}$ (es un valor clásico asociado al pentágono regular). Entonces la ecuación es:

$$z + \frac{1}{z} = 2\cos\frac{\pi}{5}.$$

**Paso 2: Resolver para $z$.** Multiplicando por $z$: $z^2 - 2\cos\frac{\pi}{5}\,z + 1 = 0$, cuyas soluciones son $z = e^{\pm i\pi/5}$.

**Paso 3: Elevar a la potencia 85.** Tomemos $z = e^{i\pi/5}$ (el otro caso da el mismo resultado por simetría, ya que $z^{85} + z^{-85}$ es invariante al cambiar $z \to 1/z$):

$$z^{85} + \frac{1}{z^{85}} = 2\cos\!\left(\frac{85\pi}{5}\right) = 2\cos(17\pi).$$

**Paso 4: Reducir el ángulo.** Como $17\pi = 16\pi + \pi$ y el coseno tiene período $2\pi$:

$$2\cos(17\pi) = 2\cos(\pi) = -2.$$

$$\boxed{-2}$$