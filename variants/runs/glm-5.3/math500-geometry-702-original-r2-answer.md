## Planteamiento

Como $C$ está al sur y $D$ al este de $O$, el triángulo $OCD$ es rectángulo en $O$, con hipotenusa $CD = 140$.

**Paso 1: Hallar $OC$, $OD$ y la altura del globo.**

Con $h$ la altura de $H$ sobre $O$:
$$h^2 + OC^2 = 150^2 = 22500, \qquad h^2 + OD^2 = 130^2 = 16900$$

Restando ambas ecuaciones:
$$OC^2 - OD^2 = 5600 \implies (OC - OD)(OC + OD) = 5600$$

Como $OC + OD = 140$ (catetos de un triángulo rectángulo con hipotenusa 140):
$$OC - OD = \frac{5600}{140} = 40$$

Resolviendo el sistema: $OC = 90$, $OD = 50$, y entonces $h^2 = 16900 - 2500 = 14400$, o sea $h = 120$.

**Paso 2: Minimizar $HP$.**

Para $P$ en el segmento $CD$, como $H$ está a altura fija $h = 120$ sobre $O$:
$$HP^2 = h^2 + OP^2 = 14400 + OP^2$$

Minimizar $HP$ equivale a minimizar $OP$, la distancia de $O$ al punto $P$. El mínimo se alcanza en el pie de la perpendicular desde $O$ a la recta $CD$; como $OCD$ es rectángulo en $O$, ese pie cae dentro de la hipotenusa $CD$, y la distancia es la altura sobre la hipotenusa:
$$OP = \frac{OC \cdot OD}{CD} = \frac{90 \cdot 50}{140} = \frac{450}{14}$$

Entonces:
$$HP_{\min} = \sqrt{14400 + \frac{202500}{196}} = \sqrt{\frac{864450}{53}} \approx 127.71 \text{ m}$$

**Paso 3: Ahorro máximo.**

La cuerda original tiene longitud $HC + HD = 150 + 130 = 280$:
$$\text{Ahorro} = 280 - HP_{\min} \approx 280 - 127.71 \approx 152.29 \text{ m}$$

\boxed{152.29 \text{ m}}