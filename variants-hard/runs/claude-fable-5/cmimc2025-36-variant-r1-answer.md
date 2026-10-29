## Planteamiento

Coloco el 24-gono regular con circunradio $R$ y centro $O$. La clave es que, al dibujar todas las cuerdas $\overline{B_iB_{i+k}}$, el polígono central es la intersección de los 24 semiplanos (que contienen a $O$) delimitados por esas cuerdas.

**Distancia de cada cuerda al centro.** La cuerda $\overline{B_iB_{i+k}}$ subtiende un arco de $k\cdot\frac{2\pi}{24}$, así que su distancia a $O$ es
$$d_k = R\cos\!\left(\frac{k\pi}{24}\right).$$

**Direcciones de las normales.** La normal a $\overline{B_iB_{i+k}}$ apunta hacia el punto medio del arco, en el ángulo $\left(i+\tfrac{k}{2}\right)\cdot 15°$. Al variar $i$, tanto para $k=10$ como para $k=11$ se obtienen 24 direcciones distintas espaciadas $15°$. Por lo tanto, la intersección de los 24 semiplanos es un 24-gono regular cuyo **apotema** es exactamente $d_k$.

## Cálculo de la razón

- Primer 24-gono ($k=10$): apotema $a_1 = R\cos 75° = R\sin 15°$.
- Segundo 24-gono ($k=11$): apotema $a_2 = R\cos 82.5° = R\sin 7.5°$.

Como son polígonos semejantes, la razón de áreas es el cuadrado de la razón de apotemas:
$$\frac{A_1}{A_2} = \frac{\sin^2 15°}{\sin^2 7.5°}.$$

Usando $\sin 15° = 2\sin 7.5°\cos 7.5°$:
$$\frac{A_1}{A_2} = 4\cos^2 7.5° = 2\left(1+\cos 15°\right) = 2 + 2\cdot\frac{\sqrt6+\sqrt2}{4} = \frac{4+\sqrt2+\sqrt6}{2}.$$

Numéricamente, esto es $\approx 3.9319$.

$$\boxed{\dfrac{4+\sqrt{2}+\sqrt{6}}{2}}$$