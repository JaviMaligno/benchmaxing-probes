Voy a resolverlo paso a paso.

**Planteamiento.** Para un punto $(x, y)$ sobre la curva $y = \frac{1}{\sqrt{2}}(x^2-3)$, la distancia al origen es $d = \sqrt{x^2 + y^2}$, así que basta minimizar $f(x) = x^2 + y^2$.

**Sustitución.** Haciendo $u = x^2 \ge 0$:

$$f = u + \frac{1}{2}(u-3)^2 = \frac{1}{2}u^2 - 2u + \frac{9}{2}.$$

**Minimización.** Derivando respecto a $u$: $\frac{df}{du} = u - 2 = 0 \Rightarrow u = 2$, que es válido ($u \ge 0$). En los extremos: $f(0) = \frac{9}{2}$ y $f \to \infty$ cuando $u \to \infty$, así que $u = 2$ es el mínimo global.

$$f(2) = \frac{1}{2}(4) - 2(2) + \frac{9}{2} = \frac{5}{2}.$$

**Verificación geométrica.** En $x = \pm\sqrt{2}$: $y = \frac{1}{\sqrt{2}}(2-3) = -\frac{1}{\sqrt{2}}$. La condición de tangencia (radio perpendicular a la tangente) se cumple: pendiente de la tangente $y' = \sqrt{2}\,x = \pm 2$; pendiente del radio $\frac{y}{x} = \mp\frac{1}{2}$; producto $= -1$. ✓

**Conclusión.** La distancia mínima es

$$d = \sqrt{\frac{5}{2}} = \frac{\sqrt{10}}{2},$$

con $a = 10$ (libre de cuadrados) y $b = 2$, de modo que $a+b = 12$.

$$\boxed{12}$$