## Resolución

**Planteamiento.** Sea $\angle Q = \beta$ y $QR = c$. Coloco $Q$ en el origen y mido distancias a lo largo de $QR$. Como $\angle QPR = 90°$, los catetos son $PQ = c\cos\beta$ y $PR = c\sin\beta$.

**Posiciones de los tres pies sobre $QR$:**

- **Altura** ($X$): $QX = PQ\cos\beta = c\cos^2\beta$.
- **Bisectriz** ($Y$): divide $QR$ en razón $PQ:PR$, así que $QY = \dfrac{c\cos\beta}{\cos\beta+\sin\beta}$.
- **Mediana** ($Z$): $QZ = c/2$.

**Cálculo de los segmentos** (suponiendo $\beta > 45°$, de modo que el orden es $X, Y, Z$):

$$XY = QY - QX = \frac{c\cos\beta\sin\beta\,(\sin\beta-\cos\beta)}{\cos\beta+\sin\beta}, \qquad YZ = QZ - QY = \frac{c\,(\sin\beta-\cos\beta)}{2(\cos\beta+\sin\beta)}.$$

**Razón:** al dividir, casi todo se cancela:

$$\frac{XY}{YZ} = 2\sin\beta\cos\beta = \sin 2\beta = \frac{5}{13}.$$

**Hallar $c$:** uso las identidades

$$(\sin\beta-\cos\beta)^2 = 1-\sin 2\beta = \frac{8}{13}, \qquad (\sin\beta+\cos\beta)^2 = 1+\sin 2\beta = \frac{18}{13},$$

de donde $\dfrac{\sin\beta-\cos\beta}{\sin\beta+\cos\beta} = \sqrt{\dfrac{8/13}{18/13}} = \dfrac{2}{3}$.

Entonces:

$$YZ = \frac{c}{2}\cdot\frac{2}{3} = \frac{c}{3} = 13 \;\Longrightarrow\; c = 39.$$

**Verificación:** $XY = YZ\cdot\sin 2\beta = 13\cdot\frac{5}{13} = 5$. ✓

$$\boxed{39}$$