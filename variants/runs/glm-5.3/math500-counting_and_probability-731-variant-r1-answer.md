**Planteamiento.** Sea $R$ el circunradio del triángulo, con $O$ en el origen y vértices en ángulos $90^\circ$, $210^\circ$, $330^\circ$; el lado opuesto a $P$ es la recta $y = -R/2$. Por simetría, basta estudiar el sector $30^\circ \le \theta \le 90^\circ$ (un sexto del triángulo), donde el vértice más cercano es $P$.

**Regiones en coordenadas polares.**

- Lado $PR$ del triángulo ($y = R - \sqrt{3}\,x$): $\rho_{\text{tri}} = \dfrac{R}{2\sin(\theta + 60^\circ)}$.
- Mediatriz de $OP$ (donde $XO = XP$): $\rho = \dfrac{R}{2\sin\theta}$.

Las condiciones $XO < XQ$ y $XO < XR$ se cumplen automáticamente en el sector (en $30^\circ$ la de $R$-vértice empata), así que la única restricción activa es la mediatriz de $OP$.

**Comparación de fronteras.** $\sin(\theta+60^\circ) \ge \sin\theta$ para $\theta \in [30^\circ, 60^\circ]$ (todo el corte es favorable) y al revés para $\theta \in [60^\circ, 90^\circ]$ (la mediatriz corta antes). Se cruzan en $\theta = 60^\circ$.

**Área favorable en el sector.**

$$A_f = \int_{30^\circ}^{60^\circ} \frac{1}{2}\left(\frac{R}{2\sin(\theta+60^\circ)}\right)^2 d\theta + \int_{60^\circ}^{90^\circ} \frac{1}{2}\left(\frac{R}{2\sin\theta}\right)^2 d\theta = \frac{R^2}{8}\Big[-\cot u\Big] + \frac{R^2}{8}\Big[-\cot\theta\Big]$$

Primera integral (con $u = \theta + 60^\circ$): $\frac{R^2}{8}\left(\frac{1}{\sqrt3} - 0\right) = \frac{R^2}{8\sqrt3}$. Segunda: $\frac{R^2}{8}\left(\frac{1}{\sqrt3} - 0\right) = \frac{R^2}{8\sqrt3}$. Total: $A_f = \frac{R^2}{4\sqrt3}$.

**Probabilidad.** El sector vale $\frac{1}{6}\cdot\frac{3\sqrt3}{4}R^2 = \frac{\sqrt3}{8}R^2$, así que

$$\frac{A_f}{A_{\text{sector}}} = \frac{R^2/(4\sqrt3)}{\sqrt3 R^2/8} = \frac{8}{12} = \frac{2}{3}.$$

Verificación numérica rápida ($R=1$): área favorable total $\approx 0.866$, área del triángulo $\approx 1.299$, cociente $= 0.6667$. ✓

$$\boxed{\dfrac{2}{3}}$$