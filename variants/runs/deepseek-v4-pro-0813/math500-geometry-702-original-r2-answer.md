Voy a resolver el problema paso a paso.

## 1. Entender la geometría

Tenemos un campo plano con sistema de coordenadas centrado en $O$:

- $A$: directamente al norte de $O$ → eje $y$ positivo.
- $B$: directamente al oeste de $O$ → eje $x$ negativo.
- $C$: directamente al sur de $O$ → eje $y$ negativo.
- $D$: directamente al este de $O$ → eje $x$ positivo.

La distancia $CD = 140$ m.

La cuerda $HC$ mide $150$ m y $HD$ mide $130$ m. Como $H$ está directamente sobre $O$, el triángulo $HOC$ es rectángulo en $O$, al igual que $HOD$.

Sea $OC = c$ y $OD = d$, y sea $h = OH$ la altura del globo.

## 2. Plantear ecuaciones

Del teorema de Pitágoras:

- $h^2 + c^2 = 150^2 = 22500$
- $h^2 + d^2 = 130^2 = 16900$

Además, por el dato del problema, la distancia entre $C$ y $D$ es:

$$c + d = 140$$

pues $C$ está al sur ($y$ negativo) y $D$ al este ($x$ positivo), de modo que el segmento $CD$ forma un triángulo rectángulo con catetos $c$ y $d$.

## 3. Resolver el sistema

De las dos primeras ecuaciones:

$$c^2 - d^2 = 22500 - 16900 = 5600$$

$$(c - d)(c + d) = 5600$$

Como $c + d = 140$:

$$(c - d) \cdot 140 = 5600 \implies c - d = 40$$

Entonces:

$$c = \frac{140 + 40}{2} = 90,\qquad d = \frac{140 - 40}{2} = 50$$

La altura $h$:

$$h^2 = 22500 - 90^2 = 22500 - 8100 = 14400 \implies h = 120$$

Verificamos con $d$:

$$h^2 + 50^2 = 14400 + 2500 = 16900 = 130^2 \ \checkmark$$

## 4. Nueva cuerda $HP$ con $P$ sobre $CD$

Queremos reemplazar $HC + HD = 150 + 130 = 280$ por una sola cuerda $HP$, donde $P$ está en el segmento $CD$, minimizando $HP$ (para maximizar el ahorro).

La longitud $HP$ es:

$$HP = \sqrt{h^2 + OP^2} = \sqrt{14400 + OP^2}$$

Por tanto, minimizar $HP$ equivale a minimizar $OP$.

## 5. Minimizar $OP$

$O$ está en el origen; $C = (0, -90)$ y $D = (50, 0)$.

La recta que pasa por $C$ y $D$:

Pendiente $m = \dfrac{0 - (-90)}{50 - 0} = \dfrac{90}{50} = \dfrac{9}{5}$.

Ecuación: $y + 90 = \dfrac{9}{5}(x - 0)$, es decir $y = \dfrac{9}{5}x - 90$.

Multiplicando por 5: $5y = 9x - 450$, o $9x - 5y = 450$.

La distancia mínima desde $O=(0,0)$ a esta recta es:

$$OP_{\min} = \frac{|9\cdot 0 - 5\cdot 0 - 450|}{\sqrt{9^2 + 5^2}} = \frac{450}{\sqrt{81 + 25}} = \frac{450}{\sqrt{106}}$$

Debemos verificar que el pie de la perpendicular cae dentro del segmento $CD$.

## 6. Verificar que el pie está dentro del segmento

La recta perpendicular a $9x - 5y = 450$ que pasa por $O$ tiene dirección $(9, -5)$. El pie $P_0$ satisface:

$P_0 = t(9, -5)$ y además $9x - 5y = 450$.

Sustituyendo: $9(9t) - 5(-5t) = 81t + 25t = 106t = 450$, luego:

$$t = \frac{450}{106} = \frac{225}{53} \approx 4{,}245$$

Entonces $P_0 = \left(\dfrac{2025}{53}, -\dfrac{1125}{53}\right)$.

Ahora, ¿está $P_0$ en el segmento $CD$?

Los extremos son $C=(0,-90)$ y $D=(50,0)$. Parametrizamos $CD$ como $C + s(D - C)$, con $s\in[0,1]$:

$D - C = (50, 90)$. Entonces:

$x = 50s$, $y = -90 + 90s$.

Igualamos con $P_0$:

$$50s = \frac{2025}{53} \implies s = \frac{2025}{53\cdot 50} = \frac{2025}{2650} = \frac{81}{106} \approx 0{,}764$$

Y para $y$:

$$-90 + 90s = -90 + 90\cdot \frac{81}{106} = -90 + \frac{7290}{106} = -\frac{9540}{106} + \frac{7290}{106} = -\frac{2250}{106} = -\frac{1125}{53}$$

Coincide. Como $s = \dfrac{81}{106}\in[0,1]$, el pie está dentro del segmento. Por tanto, el mínimo de $OP$ sobre el segmento es $\dfrac{450}{\sqrt{106}}$.

## 7. Calcular $HP_{\min}$

$$HP_{\min} = \sqrt{h^2 + OP_{\min}^2} = \sqrt{14400 + \frac{450^2}{106}} = \sqrt{14400 + \frac{202500}{106}}$$

$$\frac{202500}{106} = \frac{101250}{53}$$

$$HP_{\min} = \sqrt{\frac{14400\cdot 53 + 101250}{53}} = \sqrt{\frac{763200 + 101250}{53}} = \sqrt{\frac{864450}{53}}$$

Verificamos que sea menor que la suma $280$ y que de hecho sea el mínimo.

## 8. Comprobar si el mínimo podría estar mejorando en un extremo

En $C$: $HP = 150$.

En $D$: $HP = 130$.

En el pie de la perpendicular:

$$HP_{\min} = \sqrt{\frac{864450}{53}}$$

Calculamos el valor numérico:

$$\frac{864450}{53} \approx 16310{,}377$$

$$\sqrt{16310{,}377} \approx 127{,}71$$

Como $127{,}71 < 130$, efectivamente el mínimo es en el interior del segmento, no en los extremos. Por tanto el ahorro máximo es:

$$(HC + HD) - HP_{\min} = 280 - \sqrt{\frac{864450}{53}}$$

## 9. Simplificar la expresión

Notemos que $450^2 = 202500$ y $14400 = 120^2$.

Podemos simplificar $\sqrt{\dfrac{864450}{53}}$:

Factorizamos $864450$:

$$864450 = 2 \cdot 432225 = 2 \cdot 3^2 \cdot 48025$$

$\ldots$ Verifiquemos: $432225 / 9 = 48025$, y $48025 = 5^2 \cdot 1921 = 5^2 \cdot 17 \cdot 113$.

Entonces:

$$864450 = 2 \cdot 3^2 \cdot 5^2 \cdot 17 \cdot 113 = (3\cdot 5)^2 \cdot 2\cdot 17\cdot 113 = 15^2 \cdot 3842$$

$$\sqrt{\frac{864450}{53}} = 15\sqrt{\frac{3842}{53}}$$

Comprobamos $3842 = 2\cdot 17\cdot 113 = 2\cdot 1921$, y $53$ es primo, no divide a $3842$ (en efecto $53 \cdot 72 = 3816$, resto $26$). No se simplifica más racionalmente.

Por tanto:

$$HP_{\min} = 15\sqrt{\frac{3842}{53}}$$

Y el ahorro:

$$\text{ahorro} = 280 - 15\sqrt{\frac{3842}{53}}$$

## 10. Resultado final

$$\boxed{280 - 15\sqrt{\dfrac{3842}{53}}\ \text{m}}$$

Equivalencias alternativas:

$$280 - \sqrt{\dfrac{864450}{53}}\ \text{m} \quad \text{o}\quad \approx 152{,}29\ \text{m}$$