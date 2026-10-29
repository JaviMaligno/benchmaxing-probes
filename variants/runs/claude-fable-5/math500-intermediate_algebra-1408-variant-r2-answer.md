Observemos que $\frac{\sqrt{5}-1}{2} = 2\cos 72^\circ$, ya que $\cos 72^\circ = \frac{\sqrt{5}-1}{4}$.

**Paso 1: Identificar $w$.** Si escribimos $w = e^{i\theta}$ (como $w + 1/w$ es real y de módulo menor que 2, $w$ está en el círculo unitario), entonces
$$w + \frac{1}{w} = 2\cos\theta = \frac{\sqrt{5}-1}{2} \implies \cos\theta = \frac{\sqrt{5}-1}{4} = \cos 72^\circ.$$

Por lo tanto $w = e^{\pm 2\pi i/5}$, es decir, $w$ es una raíz quinta primitiva de la unidad: $w^5 = 1$.

**Verificación:** las raíces quintas primitivas de la unidad satisfacen $z^4+z^3+z^2+z+1=0$; dividiendo por $z^2$ y poniendo $u = z + 1/z$ se obtiene $u^2 + u - 1 = 0$, cuya raíz positiva es $u = \frac{-1+\sqrt{5}}{2}$, exactamente nuestro valor. ✓

**Paso 2: Calcular la potencia.** Como $95 = 5 \cdot 19$,
$$w^{95} = (w^5)^{19} = 1^{19} = 1.$$

Por lo tanto
$$w^{95} + \frac{1}{w^{95}} = 1 + 1 = 2.$$

$$\boxed{2}$$