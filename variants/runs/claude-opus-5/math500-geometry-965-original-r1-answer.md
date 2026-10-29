## Planteamiento

Sea $\angle CAD = \theta$.

**Paso 1: $\triangle ABC$ es isósceles.**
Como $\overline{AD}\parallel\overline{BC}$, los ángulos alternos internos dan $\angle BCA = \angle CAD = \theta$. Y como $\overline{AC}$ bisecta $\angle BAD$, se tiene $\angle BAC = \theta$. Luego $\angle BAC = \angle BCA$.

**Paso 2: Calcular las bases en términos de $AC$.**

En $\triangle ACD$, con ángulo recto en $C$:
$$AD = \frac{AC}{\cos\theta}$$

En $\triangle ABC$, con $\angle ABC = 180^\circ - 2\theta$, por ley de senos:
$$BC = \frac{AC\sin\theta}{\sin(180^\circ-2\theta)} = \frac{AC\sin\theta}{\sin 2\theta} = \frac{AC}{2\cos\theta}$$

Por lo tanto $\dfrac{BC}{AD} = \dfrac{1}{2}$.

**Paso 3: Comparar áreas.**
Los triángulos $ABC$ y $ACD$ tienen la misma altura (la distancia entre las rectas paralelas $AD$ y $BC$), con bases $BC$ y $AD$:
$$\frac{[\triangle ABC]}{[\triangle ACD]} = \frac{BC}{AD} = \frac12$$

Entonces:
$$42 = [ABCD] = [\triangle ABC] + [\triangle ACD] = \tfrac12[\triangle ACD] + [\triangle ACD] = \tfrac32[\triangle ACD]$$

$$[\triangle ACD] = \frac{2}{3}\cdot 42 = 28$$

\boxed{28}