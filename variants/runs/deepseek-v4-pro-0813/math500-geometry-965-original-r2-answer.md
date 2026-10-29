Resolveré el problema paso a paso.

## 1. Interpretación de los datos

Como $\overline{AC}$ biseca al ángulo $\angle BAD$, se cumple

$$
\angle BAC = \angle CAD.
$$

Además, como $\overline{AD} \parallel \overline{BC}$ y $\overline{AC}$ es una transversal, los ángulos alternos internos son iguales:

$$
\angle DAC = \angle ACB.
$$

Por lo tanto,

$$
\angle BAC = \angle CAD = \angle ACB.
$$

En el triángulo $ABC$, los ángulos en $A$ y en $C$ son iguales, así que $ABC$ es isósceles con

$$
AB = BC.
$$

## 2. Relación entre las áreas

El trapecio queda dividido por la diagonal $AC$ en dos triángulos:

$$
[ABCD] = [ABC] + [ACD].
$$

Llamemos $\alpha = \angle CAD$. Como $ABC$ es isósceles y $\angle BAC = \angle ACB = \alpha$, el ángulo en $B$ es

$$
\angle ABC = 180^\circ - 2\alpha.
$$

Y en el triángulo rectángulo $ACD$ (pues $\overline{AC} \perp \overline{CD}$), el ángulo en $C$ es recto:

$$
\angle ACD = 90^\circ.
$$

## 3. Cálculo de las áreas

Sea $\overline{AC} = d$. En el triángulo rectángulo $ACD$:

$$
CD = d \tan\alpha.
$$

Entonces

$$
[ACD] = \frac{1}{2} \cdot AC \cdot CD
       = \frac{1}{2}\, d \cdot d \tan\alpha
       = \frac{1}{2}\, d^2 \tan\alpha.
$$

Ahora, en el triángulo isósceles $ABC$, los lados iguales son $AB = BC = \ell$. La base es $AC = d$, y como el ángulo en $B$ es $180^\circ - 2\alpha$,

$$
d = 2\ell \sin\alpha.
$$

Por otro lado,

$$
[ABC] = \frac{1}{2}\,\ell^2 \sin(180^\circ - 2\alpha)
      = \frac{1}{2}\,\ell^2 \sin 2\alpha.
$$

Como $d = 2\ell \sin\alpha$, tenemos $\ell^2 = \dfrac{d^2}{4\sin^2\alpha}$. Sustituyendo:

$$
[ABC] = \frac{1}{2} \cdot \frac{d^2}{4\sin^2\alpha} \cdot 2\sin\alpha \cos\alpha
      = \frac{d^2 \cos\alpha}{4 \sin\alpha}
      = \frac{d^2}{4\tan\alpha}.
$$

## 4. Relación entre las dos áreas

Entonces:

$$
\frac{[ABC]}{[ACD]}
= \frac{\frac{d^2}{4\tan\alpha}}{\frac{1}{2}\,d^2\tan\alpha}
= \frac{1}{2\tan^2\alpha}.
$$

Este resultado depende de $\alpha$, así que necesitamos una relación adicional. La condición $\overline{AC} \perp \overline{CD}$ junto con $\overline{AD} \parallel \overline{BC}$ y la bisectriz determinan geométricamente que $\tan\alpha$ toma un valor específico.

## 5. Determinación geométrica de $\alpha$

Coloquemos coordenadas:

- $D = (0,0)$,
- $C = (c,0)$, con $\overline{CD}$ horizontal,
- como $\overline{AC} \perp \overline{CD}$, entonces $\overline{AC}$ es vertical: $A = (c,h)$.

Entonces

$$
AC = h,\qquad CD = c,\qquad \tan\alpha = \frac{CD}{AC} = \frac{c}{h}.
$$

Como $\overline{AD} \parallel \overline{BC}$, la recta por $B$ y $C$ tiene la misma pendiente que $AD$. La pendiente de $AD$ es $\dfrac{h}{c}$, así que $B$ está en la recta

$$
y = \frac{h}{c}(x - c).
$$

Además, como $AC$ biseca $\angle BAD$, el ángulo entre $AB$ y la vertical $AC$ es igual a $\alpha$. Tomando $B$ a la derecha de $A$, con $B = (x_B, y_B)$:

$$
\tan\alpha = \frac{x_B - c}{h - y_B}
          = \frac{x_B - c}{h - \frac{h}{c}(x_B - c)}.
$$

Igualando con $\tan\alpha = \dfrac{c}{h}$:

$$
\frac{x_B - c}{h - \frac{h}{c}(x_B - c)} = \frac{c}{h}.
$$

Simplificando,

$$
\frac{x_B - c}{2c - x_B} = 1
\quad\Longrightarrow\quad
x_B = \frac{3c}{2}.
$$

Entonces

$$
y_B = \frac{h}{c}\left(\frac{3c}{2} - c\right) = \frac{h}{2}.
$$

## 6. Cálculo final del área

- Triángulo rectángulo $ACD$:

$$
[ACD] = \frac{1}{2} \cdot AC \cdot CD
       = \frac{1}{2}\, h \cdot c
       = \frac{1}{2}ch.
$$

- Triángulo $ABC$, tomando como base la vertical $AC = h$ y como altura la distancia horizontal desde $B$ hasta $AC$, que es

$$
\frac{3c}{2} - c = \frac{c}{2},
$$

entonces

$$
[ABC] = \frac{1}{2} \cdot h \cdot \frac{c}{2}
      = \frac{1}{4}ch.
$$

Por lo tanto,

$$
[ABCD] = [ACD] + [ABC]
       = \frac{1}{2}ch + \frac{1}{4}ch
       = \frac{3}{4}ch.
$$

Como $[ABCD] = 42$,

$$
\frac{3}{4}ch = 42
\quad\Longrightarrow\quad
ch = 56.
$$

Finalmente,

$$
[ACD] = \frac{1}{2}ch = \frac{1}{2} \cdot 56 = 28.
$$

Respuesta final:

$$
\boxed{28}
$$