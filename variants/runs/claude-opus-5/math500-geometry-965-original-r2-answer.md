## Planteamiento

Sea $\angle CAD = \theta$. Como $AC$ biseca $\angle BAD$, también $\angle BAC = \theta$.

**Triángulo $ABC$ es isósceles:** por ser $AD \parallel BC$, los ángulos alternos internos dan $\angle BCA = \angle CAD = \theta$. Junto con $\angle BAC = \theta$, resulta $\angle ABC = 180^\circ - 2\theta$.

**Cálculo de las bases:**

En el triángulo rectángulo $ACD$ (ángulo recto en $C$, ángulo $\theta$ en $A$):
$$AD = \frac{AC}{\cos\theta}$$

En el triángulo $ABC$, por ley de senos:
$$BC = \frac{AC \sin\theta}{\sin(180^\circ - 2\theta)} = \frac{AC\sin\theta}{2\sin\theta\cos\theta} = \frac{AC}{2\cos\theta}$$

Por tanto:
$$\frac{BC}{AD} = \frac{1}{2}$$

**Razón de áreas:** los triángulos $ABC$ y $ACD$ comparten la misma altura (la distancia entre las rectas paralelas $AD$ y $BC$), con bases $BC$ y $AD$ respectivamente:
$$\frac{[\triangle ABC]}{[\triangle ACD]} = \frac{BC}{AD} = \frac12$$

Entonces:
$$[ABCD] = [\triangle ABC] + [\triangle ACD] = \tfrac12[\triangle ACD] + [\triangle ACD] = \tfrac32[\triangle ACD] = 42$$

$$[\triangle ACD] = 28$$

\boxed{28}