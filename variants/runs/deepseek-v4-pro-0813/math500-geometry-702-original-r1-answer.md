## Planteamiento

Los puntos $A$, $B$, $C$, $D$ están situados al norte, oeste, sur y este de $O$, respectivamente, sobre una misma recta en cada par opuesto. Como $C$ está al sur y $D$ al este, el segmento $CD$ es la hipotenusa de un triángulo rectángulo con catetos $OC$ y $OD$.

Llamemos:

- $h = OH$ (altura del globo sobre $O$)
- $x = OC$ (distancia de $O$ a $C$)
- $y = OD$ (distancia de $O$ a $D$)

Sabemos que:

- $HC = 150$ m
- $HD = 130$ m
- $CD = 140$ m

## Relaciones geométricas

Como $H$ está directamente encima de $O$, el triángulo $HOC$ es rectángulo en $O$. Por el teorema de Pitágoras:

$$
HC^2 = h^2 + x^2 \implies h^2 + x^2 = 150^2 = 22500
$$

Análogamente para $HOD$:

$$
HD^2 = h^2 + y^2 \implies h^2 + y^2 = 130^2 = 16900
$$

Para el triángulo $COD$ en el suelo, rectángulo en $O$:

$$
CD^2 = x^2 + y^2 \implies x^2 + y^2 = 140^2 = 19600
$$

## Resolución

Sumamos las dos primeras ecuaciones:

$$
2h^2 + x^2 + y^2 = 22500 + 16900 = 39400
$$

Sustituyendo $x^2 + y^2 = 19600$:

$$
2h^2 + 19600 = 39400
$$

$$
2h^2 = 19800
$$

$$
h^2 = 9900
$$

Entonces:

$$
x^2 = 22500 - 9900 = 12600 \implies x = \sqrt{12600} = 30\sqrt{14}
$$

$$
y^2 = 16900 - 9900 = 7000 \implies y = \sqrt{7000} = 10\sqrt{70}
$$

Verificamos:

$$
x^2 + y^2 = 12600 + 7000 = 19600 = 140^2 \quad \checkmark
$$

## Optimización

Queremos reemplazar las dos cuerdas $HC$ y $HD$ por una sola cuerda $HP$, con $P$ sobre el segmento $CD$. El ahorro es:

$$
\text{Ahorro} = HC + HD - HP = 150 + 130 - HP = 280 - HP
$$

Para maximizar el ahorro, debemos **minimizar** $HP$.

Como $H$ está en la vertical de $O$, la distancia $HP$ es:

$$
HP = \sqrt{h^2 + OP^2}
$$

donde $OP$ es la distancia horizontal de $O$ a $P$. Para minimizar $HP$, debemos minimizar $OP$, es decir, tomar $P$ como el punto de $CD$ más cercano a $O$. Ese punto es el pie de la perpendicular desde $O$ a la recta $CD$.

Como $P$ debe estar **sobre el segmento** $CD$ (no solo sobre la recta), y el pie de la perpendicular cae efectivamente dentro del segmento en un triángulo acutángulo — aquí el triángulo $COD$ es rectángulo en $O$, así que el pie de la altura cae sobre la hipotenusa —, ese punto interior existe.

La distancia mínima $OP = d$ es la altura del triángulo rectángulo $COD$ sobre la hipotenusa:

$$
d = \frac{x \cdot y}{CD} = \frac{(30\sqrt{14})(10\sqrt{70})}{140}
$$

$$
d = \frac{300\sqrt{980}}{140} = \frac{300\sqrt{980}}{140}
$$

Simplificamos $\sqrt{980} = \sqrt{49 \cdot 20} = 7\sqrt{20} = 7 \cdot 2\sqrt{5} = 14\sqrt{5}$:

$$
d = \frac{300 \cdot 14\sqrt{5}}{140} = \frac{4200\sqrt{5}}{140} = 30\sqrt{5}
$$

Entonces:

$$
HP_{\min} = \sqrt{h^2 + d^2} = \sqrt{9900 + (30\sqrt{5})^2} = \sqrt{9900 + 4500} = \sqrt{14400} = 120
$$

## Cálculo final

$$
\text{Ahorro máximo} = 280 - 120 = 160
$$

Por tanto, la mayor longitud de cuerda que se puede ahorrar es:

$$
\boxed{160}
$$