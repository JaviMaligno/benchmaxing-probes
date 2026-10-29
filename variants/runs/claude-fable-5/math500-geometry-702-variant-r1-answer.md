**La mayor longitud de cuerda que se puede ahorrar es 170 m.**

Razonamiento:

Sea $h = OH$, $c = OC$, $d = OD$. Como $C$ está al sur de $O$ y $D$ al este, $OC \perp OD$, y como $H$ está directamente sobre $O$, $HO$ es perpendicular al suelo. Entonces:

- $c^2 + h^2 = 145^2 = 21025$
- $d^2 + h^2 = 125^2 = 15625$
- $c^2 + d^2 = 180^2 = 32400$ (teorema de Pitágoras en el triángulo $OCD$)

Restando las dos primeras: $c^2 - d^2 = 5400$. Junto con $c^2 + d^2 = 32400$ se obtiene $c^2 = 18900$, $d^2 = 13500$, y por tanto $h^2 = 21025 - 18900 = 2125$.

Para un punto $P$ sobre el segmento $CD$, $HP^2 = h^2 + OP^2$, así que $HP$ es mínimo cuando $OP$ es mínimo, es decir, cuando $OP$ es la altura del triángulo rectángulo $OCD$ desde $O$ hasta la hipotenusa $CD$:

$$OP = \frac{c \cdot d}{180} = \frac{\sqrt{18900 \cdot 13500}}{180} = \frac{2700\sqrt{35}}{180} = 15\sqrt{35}, \qquad OP^2 = 7875.$$

(Este pie de altura cae dentro del segmento $CD$, por ser el triángulo rectángulo en $O$.)

Entonces $HP^2 = 2125 + 7875 = 10000$, de modo que $HP = 100$ m.

El ahorro máximo es $145 + 125 - 100 = 170$ m.

$$\boxed{170 \text{ m}}$$