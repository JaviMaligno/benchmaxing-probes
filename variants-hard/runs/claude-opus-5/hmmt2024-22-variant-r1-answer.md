## Planteamiento

Sean los catetos $c = PQ$, $b = PR$ y la hipotenusa $a = QR$. Midiendo distancias desde $Q$ sobre el lado $QR$:

- **Altura**: $QX = \dfrac{c^2}{a}$
- **Bisectriz**: como $QY/YR = c/b$, resulta $QY = \dfrac{ac}{b+c}$
- **Mediana**: $QZ = \dfrac{a}{2}$

## Cálculo de los segmentos

$$XY = \frac{ac}{b+c} - \frac{c^2}{a} = \frac{c(a^2 - cb - c^2)}{a(b+c)} = \frac{bc(b-c)}{a(b+c)}$$

$$YZ = \frac{a}{2} - \frac{ac}{b+c} = \frac{a(b-c)}{2(b+c)}$$

Dividiendo, casi todo se cancela:

$$\frac{XY}{YZ} = \frac{2bc}{a^2} = \frac{5}{13} \quad\Longrightarrow\quad bc = \frac{5a^2}{26}$$

## Sistema en $s = b+c$, $d = b-c$

Del teorema de Pitágoras: $s^2 + d^2 = 2(b^2+c^2) = 2a^2$.
De $bc$: $s^2 - d^2 = 4bc = \dfrac{10a^2}{13}$.

Resolviendo:
$$s^2 = \frac{18a^2}{13}, \qquad d^2 = \frac{8a^2}{13}$$

Ahora se usa $YZ = 13$, es decir $\dfrac{ad}{2s} = 13 \Rightarrow ad = 26s$. Elevando al cuadrado:

$$a^2 \cdot \frac{8a^2}{13} = 676 \cdot \frac{18a^2}{13} \quad\Longrightarrow\quad 8a^2 = 676\cdot 18 \quad\Longrightarrow\quad a^2 = 1521$$

## Verificación

Con $a = 39$: $s = \sqrt{2106} \approx 45.89$, $d = \sqrt{936} \approx 30.59$, luego $c \approx 7.65$, $b \approx 38.24$, y $b^2+c^2 \approx 1521$ ✓. Además $XZ = \dfrac{sd}{2a} = \dfrac{1403.8}{78} \approx 18 = 5+13$ ✓.

$$\boxed{39}$$