Voy a resolver el problema paso a paso.

**Planteamiento.** Sea $\angle BAD = 2\alpha$, de modo que $\angle BAC = \angle CAD = \alpha$ (pues $AC$ biseca $\angle BAD$).

**Paso 1: El triángulo $ABC$ es isósceles.** Como $\overline{AD}\parallel \overline{BC}$, los ángulos alternos internos dan $\angle BCA = \angle CAD = \alpha$. Entonces $\angle BAC = \angle BCA = \alpha$, así que $AB = BC$.

**Paso 2: Relacionar $BC$ con $AD$.** Sea $AD = d$. En el triángulo rectángulo $ACD$ (recto en $C$, con $\angle CAD = \alpha$):
$$AC = d\cos\alpha.$$

En el triángulo $ABC$, el ángulo en $B$ es $\pi - 2\alpha$. Por la ley de senos:
$$\frac{BC}{\sin\alpha} = \frac{AC}{\sin(\pi - 2\alpha)} = \frac{d\cos\alpha}{\sin 2\alpha} = \frac{d\cos\alpha}{2\sin\alpha\cos\alpha} = \frac{d}{2\sin\alpha}.$$

Por lo tanto $BC = \dfrac{d}{2}$, es decir, $BC = \dfrac{AD}{2}$.

**Paso 3: Comparar áreas.** Los triángulos $ABC$ (base $BC$) y $ACD$ (base $AD$) tienen la misma altura: la distancia $h$ entre las rectas paralelas $BC$ y $AD$. Entonces:
$$\frac{[\triangle ABC]}{[\triangle ACD]} = \frac{BC}{AD} = \frac{1}{2}.$$

**Paso 4: Usar el área total.**
$$[ABCD] = [\triangle ABC] + [\triangle ACD] = \frac{1}{2}[\triangle ACD] + [\triangle ACD] = \frac{3}{2}[\triangle ACD] = 42.$$

De aquí:
$$[\triangle ACD] = 42\cdot\frac{2}{3} = 28.$$

$$\boxed{28}$$