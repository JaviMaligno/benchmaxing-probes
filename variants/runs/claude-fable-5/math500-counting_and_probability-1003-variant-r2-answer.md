Planteemos el problema. Sea $p = P(F)$ y sea $q$ la probabilidad de la cara opuesta a $F$.

**Suma de probabilidades:** las otras cuatro caras suman $4 \cdot \tfrac16 = \tfrac23$, así que $p + q = \tfrac13$, es decir $q = \tfrac13 - p$.

**Probabilidad de que la suma sea 7:** la suma es 7 exactamente cuando los dos dados muestran caras opuestas entre sí (pues las caras opuestas suman 7). Hay tres pares opuestos: el par $(F, \text{opuesta de }F)$ y dos pares formados por las cuatro caras justas. Entonces:

$$P(\text{suma}=7) = 2\,p\,q + 4\cdot\frac{1}{6}\cdot\frac{1}{6} = 2p\left(\frac13 - p\right) + \frac19 = \frac{71}{450}$$

**Resolvemos:**

$$2p\left(\frac13 - p\right) = \frac{71}{450} - \frac{50}{450} = \frac{21}{450} = \frac{7}{150}$$

$$p\left(\frac13 - p\right) = \frac{7}{300} \;\Longrightarrow\; 300p^2 - 100p + 7 = 0$$

$$p = \frac{100 \pm \sqrt{10000 - 8400}}{600} = \frac{100 \pm 40}{600}$$

Las raíces son $p = \tfrac{140}{600} = \tfrac{7}{30}$ y $p = \tfrac{60}{600} = \tfrac{1}{10}$. Como $p > \tfrac16$, tomamos $p = \tfrac{7}{30}$ (y la cara opuesta tiene probabilidad $\tfrac{1}{10} < \tfrac16$, consistente).

**Verificación:** $2\cdot\tfrac{7}{30}\cdot\tfrac{1}{10} + \tfrac19 = \tfrac{7}{150} + \tfrac19 = \tfrac{21}{450} + \tfrac{50}{450} = \tfrac{71}{450}$ ✓

Con $m = 7$, $n = 30$ (coprimos), $m + n = 37$.

$$\boxed{37}$$