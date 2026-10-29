## Planteamiento

Observamos que
$$\frac{1+\sqrt5}{2} = 2\cos 36^\circ,$$
ya que $\cos 36^\circ = \frac{1+\sqrt5}{4}$.

Si escribimos $z = e^{i\theta}$, entonces $z + \frac1z = 2\cos\theta$, de modo que $\theta = 36^\circ$ (la otra raíz, $\theta=-36^\circ$, da el mismo resultado por simetría).

## Cálculo

Por la fórmula de De Moivre:
$$z^{85} + \frac{1}{z^{85}} = 2\cos(85 \cdot 36^\circ) = 2\cos(3060^\circ).$$

Reducimos el ángulo: $3060 = 8\cdot 360 + 180$, luego
$$2\cos(3060^\circ) = 2\cos(180^\circ) = 2(-1) = -2.$$

**Verificación alternativa:** $z$ es raíz de $z^2 - \varphi z + 1 = 0$, con $z^{10}=1$ y $z^5 = -1$ (pues $5\cdot36^\circ = 180^\circ$). Entonces $z^{85} = (z^5)^{17} = (-1)^{17} = -1$, y por tanto $z^{85} + z^{-85} = -1 + (-1) = -2$.

$$\boxed{-2}$$