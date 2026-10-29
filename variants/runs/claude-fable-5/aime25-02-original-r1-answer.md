## Resolución

**Paso 1: Ubicar los puntos con razones.**

Sobre $\overline{AB}$: $AD = 4$, $AE = 20$, $AB = 28$, así que $\frac{AD}{AB} = \frac{1}{7}$ y $\frac{AE}{AB} = \frac{5}{7}$.

Sobre $\overline{AC}$: $AF = 13$, $AG = 65$, $AC = 91$, así que $\frac{AF}{AC} = \frac{1}{7}$ y $\frac{AG}{AC} = \frac{5}{7}$.

**Paso 2: Hallar el área de $\triangle ABC$.**

Como $\triangle ADF \sim \triangle ABC$ con razón $\frac{1}{7}$ y $\triangle AEG \sim \triangle ABC$ con razón $\frac{5}{7}$:

$$[DEGF] = [AEG] - [ADF] = \left(\frac{25}{49} - \frac{1}{49}\right)[ABC] = \frac{24}{49}[ABC] = 288 \implies [ABC] = 588.$$

**Paso 3: Calcular el heptágono con coordenadas.**

El problema es afín-invariante (solo involucra razones y áreas), así que elijo $A = (0,0)$, $B = (28,0)$, $C = (0,42)$, lo que da $[ABC] = \frac{1}{2}\cdot 28 \cdot 42 = 588$. Entonces:

- $D = (4,0)$, $E = (20,0)$, $F = (0,6)$, $G = (0,30)$.
- Verificación: el shoelace de $DEGF$ da efectivamente $288$. ✓
- $M = 2F - D = (-4, 12)$ y $N = 2E - G = (40, -30)$.

**Paso 4: Shoelace del heptágono $AFNBCEM$** con vértices $A(0,0)$, $F(0,6)$, $N(40,-30)$, $B(28,0)$, $C(0,42)$, $E(20,0)$, $M(-4,12)$:

$$\sum (x_i y_{i+1} - x_{i+1} y_i) = 0 - 240 + 840 + 1176 - 840 + 240 + 0 = 1176$$

$$[\text{heptágono}] = \frac{1176}{2} = 588.$$

El área del heptágono coincide exactamente con la del triángulo: las reflexiones intercambian regiones de igual área (el triángulo $\triangle MFE$ compensa lo que se pierde, y la zona añadida por $N$ fuera de $AB$ compensa el cuadrilátero $DEGF$ removido).

$$\boxed{588}$$