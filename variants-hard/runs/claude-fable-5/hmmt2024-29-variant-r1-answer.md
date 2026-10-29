## Solución

**Planteamiento.** Sea $\theta = \angle YRP$ y sea $F$ el pie de la perpendicular desde $Q$ a $PR$ (de modo que $Q$, $T$, $F$ son colineales, con $QF \perp PR$).

**Paso 1: Ángulos.** Como $\angle QYR = 60^\circ$, entonces $\angle PYR = 120^\circ$. En el triángulo $PYR$: $\angle P = 60^\circ - \theta$.

En el triángulo rectángulo $RFT$: $\angle RTF = 90^\circ - \theta$. Como $\angle QTY$ y $\angle RTF$ son opuestos por el vértice, $\angle QTY = 90^\circ - \theta$, y por lo tanto $\angle TQY = 180^\circ - 60^\circ - (90^\circ - \theta) = 30^\circ + \theta$.

**Paso 2: Ley de senos.** En el triángulo $QTY$ (con $QT = 3$ y $\angle QYT = 60^\circ$):

$$QY = \frac{3\sin(90^\circ-\theta)}{\sin 60^\circ} = 2\sqrt{3}\cos\theta, \qquad TY = \frac{3\sin(30^\circ+\theta)}{\sin 60^\circ} = 2\sqrt{3}\sin(30^\circ+\theta).$$

En el triángulo $PYR$ (con $PR = 8$ y $\angle PYR = 120^\circ$):

$$PY = \frac{8\sin\theta}{\sin 120^\circ} = \frac{16}{\sqrt{3}}\sin\theta, \qquad RY = \frac{16}{\sqrt{3}}\sin(60^\circ-\theta).$$

**Paso 3: Usar $PQ = 6$.** De $PY + QY = 6$:

$$\frac{16}{\sqrt{3}}\sin\theta + 2\sqrt{3}\cos\theta = 6 \quad\Longrightarrow\quad 16\sin\theta + 6\cos\theta = 6\sqrt{3}. \tag{$\star$}$$

**Paso 4: Expresar $RT$.** Como $RT = RY - TY$ y $\sin(60^\circ-\theta) = \cos(30^\circ+\theta)$, expandiendo:

$$RT = \frac{16}{\sqrt{3}}\cos(30^\circ+\theta) - 2\sqrt{3}\sin(30^\circ+\theta) = (8-\sqrt{3})\cos\theta - \frac{8\sqrt{3}+9}{3}\sin\theta.$$

De $(\star)$: $\cos\theta = \sqrt{3} - \tfrac{8}{3}\sin\theta$. Sustituyendo:

$$RT = (8-\sqrt{3})\sqrt{3} - \frac{64-8\sqrt{3}}{3}\sin\theta - \frac{8\sqrt{3}+9}{3}\sin\theta = 8\sqrt{3} - 3 - \frac{73}{3}\sin\theta.$$

**Paso 5: Resolver para $\sin\theta$.** Sustituyendo $\cos\theta = \sqrt{3} - \tfrac{8}{3}\sin\theta$ en $\sin^2\theta + \cos^2\theta = 1$:

$$73\sin^2\theta - 48\sqrt{3}\,\sin\theta + 18 = 0 \quad\Longrightarrow\quad \sin\theta = \frac{48\sqrt{3} \pm 6\sqrt{46}}{146} = \frac{3(8\sqrt{3} \pm \sqrt{46})}{73},$$

ya que el discriminante es $6912 - 5256 = 1656 = 36\cdot 46$.

**Paso 6: Conclusión.** Entonces

$$RT = 8\sqrt{3} - 3 - (8\sqrt{3} \pm \sqrt{46}) = -3 \mp \sqrt{46}.$$

Como $RT > 0$, debe tomarse el signo que da $RT = \sqrt{46} - 3 \approx 3.782$ (la verificación numérica confirma una configuración válida: $\theta \approx 16.9^\circ$, $Y$ en el interior de $\overline{PQ}$ y $T$ en el interior de $\overline{RY}$).

$$\boxed{\sqrt{46}-3}$$