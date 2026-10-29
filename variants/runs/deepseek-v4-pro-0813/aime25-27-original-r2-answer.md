Vamos a resolver el problema paso a paso.

## 1. Análisis geométrico

Sea $O = A_1$ el origen. Para cada $2 \le i \le 10$, consideramos los tres puntos $A_i$, $A_1 = O$, $A_{i+1}$.

Denotemos:
- $r_i = |\overrightarrow{OA_i}| = A_1 A_i$
- El ángulo $\angle A_i A_1 A_{i+1} = \angle A_i O A_{i+1}$.

Sabemos que $\cos(\angle A_i O A_{i+1}) = \frac{12}{13}$, así que $\sin(\angle A_i O A_{i+1}) = \pm \frac{5}{13}$.

El área del triángulo $A_i O A_{i+1}$ está dada por:
$$\frac{1}{2} r_i r_{i+1} \sin(\angle A_i O A_{i+1}).$$

Como el área es igual a $1$:
$$\frac{1}{2} r_i r_{i+1} \cdot \frac{5}{13} = 1,$$
lo que implica:
$$r_i r_{i+1} = \frac{26}{5}.$$

Esto es válido para $2 \le i \le 10$, es decir, hay 9 ecuaciones. Por tanto, $r_2, r_3, \ldots, r_{11}$ forman una sucesión alternante:
$$r_2 = r_4 = r_6 = r_8 = r_{10} = a,$$
$$r_3 = r_5 = r_7 = r_9 = r_{11} = b,$$
donde $ab = \frac{26}{5}$.

## 2. El giro entre vectores consecutivos

El ángulo $\angle A_i O A_{i+1}$ tiene coseno $\frac{12}{13}$, así que el ángulo (módulo signo) es $\theta$, con:
$$\cos\theta = \frac{12}{13}, \quad \sin\theta = \frac{5}{13}.$$

Debido a que el polígono es no convexo, algunos de estos ángulos pueden ser orientados hacia un lado u otro. Pero el producto $r_i r_{i+1}$ siempre es $\frac{26}{5}$ porque el área usa $|\sin\theta|$.

Vamos a suponer que el polígono «avanza» con un ángulo central $\theta$ y que es simple. La manera estándar de construir un polígono estrellado o no convexo con estas condiciones es que todos los ángulos centrales entre $OA_i$ y $OA_{i+1}$ sean iguales en magnitud y con el mismo signo (por ejemplo todos $\theta$), y que el polígono dé una vuelta completa de $2\pi$ alrededor de $O$.

## 3. Suma de ángulos

Como hay 9 pasos entre $A_2, A_3, \ldots, A_{11}$ (los pares $(A_2,A_3), \ldots, (A_{10},A_{11})$), y suponemos que cada giro tiene la misma dirección, el ángulo total girado de $A_2$ a $A_{11}$ es $9\theta$. Para que el polígono no se cierre de forma trivial y sea simple (no convexo), el segmento $A_{11}A_2$ junto con la cadena de 9 triángulos debe encerrar a $O$ y dar una vuelta completa. 

Para que el polígono sea simple y no convexo, los 9 ángulos centrales iguales suman $2\pi + 2\alpha$ o algo así. En realidad examinemos mejor: los puntos $A_2, A_3, \ldots, A_{11}$ están sobre dos rayos alternados (porque $r$ alterna entre $a$ y $b$). Si cada ángulo entre rayos consecutivos es $\theta$, entonces los pares se alternan entre dos direcciones separadas por $\theta$.

El ángulo entre $A_i$ y $A_{i+2}$ (ambos con el mismo radio) es $2\theta$. Para $i=2,4,6,8$, el i-ésimo vértice está sobre el rayo $\phi_i$, y el $(i+2)$-ésimo sobre el mismo rayo.

## 4. Cierre del polígono y perímetro

El polígono completo consiste en:
- La cadena $A_2 \to A_3 \to \cdots \to A_{11}$ (9 segmentos de triángulos),
- Los segmentos $A_{11}A_1$ y $A_1A_2$.

El perímetro es:
$$P = \sum_{i=2}^{10} A_i A_{i+1} + A_{11}A_1 + A_1A_2.$$

Dado que $A_i O = r_i$, $A_{i+1} O = r_{i+1}$, y el ángulo entre ellos es $\theta$:
$$A_i A_{i+1}^2 = r_i^2 + r_{i+1}^2 - 2 r_i r_{i+1} \cos\theta.$$

Con $\cos\theta = \frac{12}{13}$ y $r_i r_{i+1} = \frac{26}{5}$:
$$A_i A_{i+1}^2 = r_i^2 + r_{i+1}^2 - 2 \cdot \frac{26}{5} \cdot \frac{12}{13} = r_i^2 + r_{i+1}^2 - \frac{48}{5}.$$

Además $A_{11}A_1 = b$ y $A_1 A_2 = a$.

Como $a$ y $b$ alternan, las longitudes $A_i A_{i+1}$ alternan entre dos valores:
- Cuando $r_i = a, r_{i+1} = b$: $d_{ab}^2 = a^2 + b^2 - \frac{48}{5}$,
- Cuando $r_i = b, r_{i+1} = a$: misma cosa, $d_{ba} = d_{ab}$.

Así que todos los 9 segmentos de la cadena tienen la misma longitud $d$, con:
$$d^2 = a^2 + b^2 - \frac{48}{5}.$$

Por lo tanto, el perímetro:
$$P = 9d + a + b = 20.$$

## 5. Relación entre $a$ y $b$

Sabemos que $ab = \frac{26}{5}$.

Además, para que el polígono sea simple, los puntos $A_2$ y $A_{11}$ deben estar «cerca» en términos de ángulo para que el segmento $A_{11}A_2$ no cruce la cadena. 

Consideremos que los ángulos centrales todos son $+\theta$, así que la dirección de $A_{i+1}$ es la de $A_i$ girada $\theta$.

Los radios:
$$A_2: a, \text{ ángulo } 0.$$
$A_3$: $b$, ángulo $\theta$.
$A_4$: $a$, ángulo $2\theta$.
...
$A_{11}$: $b$, ángulo $9\theta$.

Para que el polígono sea simple, la suma total de ángulos desde $A_2$ a $A_{11}$ debe ser casi una vuelta completa, y concretamente el segmento $A_{11}A_2$ debe pasar por el «exterior». En estos problemas clásicos (como la versión de un rompecabezas similar), se toma $9\theta = 2\pi - 2\alpha$, con $\alpha$ el ángulo del triángulo $A_1 A_{11} A_2$.

En el triángulo $A_2 A_1 A_{11}$:
- $A_1 A_2 = a$,
- $A_1 A_{11} = b$,
- El ángulo en $A_1 = \angle A_{11} A_1 A_2$.

Si la dirección de $A_2$ es 0 y la de $A_{11}$ es $9\theta$, el ángulo entre ellas (módulo $2\pi$) es:
$$2\pi - 9\theta \quad \text{ si } 9\theta < 2\pi.$$

Ese ángulo es justamente $\angle A_{11} A_1 A_2$. Llamémoslo $\gamma = 2\pi - 9\theta$.

En el triángulo $A_2 O A_{11}$, con lados $a$, $b$, y ángulo comprendido $\gamma$:
$$A_2 A_{11}^2 = a^2 + b^2 - 2ab\cos\gamma.$$

Aquí viene la condición clave para que el polígono $\ldots A_2 A_3 \cdots A_{11} A_2$ (sin $A_1$) no sea autointersecante. Por construcción geométrica conocida, para que sea simple se necesita que el segmento $A_2 A_{11}$ sea paralelo a unos de los lados de los triángulos, formando una especie de «estrella» que cierra.

En realidad, el enfoque más limpio es el siguiente: como todos los triángulos tienen área 1 y el mismo lado $OA$ relativo, los triángulos $A_i O A_{i+1}$ son congruentes salvo escala. La condición de simplicidad impone que el ángulo central subtendido por la cadena $A_2, \ldots, A_{11}$ sea $2\pi - 2\phi$, donde $\phi$ es el ángulo del triángulo $OA_2A_{11}$ en $O$.

## 6. Determinación de $a$ y $b$ por cierre vectorial

La condición de que el polígono sea cerrado y simple se traduce en una ecuación vectorial. Como $\cos\theta = \frac{12}{13}$, el vector de giro es un número complejo $w = \cos\theta + i\sin\theta = \frac{12}{13} + i\frac{5}{13}$.

Tomemos $A_2 = a$ (en el eje real), y cada $A_{i+1} = A_i \cdot w$ en dirección (pero con radio alternado).

En realidad, la forma correcta de verlo: los vectores posición $\overrightarrow{OA_i}$ son:
- $\overrightarrow{OA_2} = a$,
- $\overrightarrow{OA_3} = b\, w$,
- $\overrightarrow{OA_4} = a\, w^2$,
- ...
- $\overrightarrow{OA_{11}} = b\, w^9$.

Como $w$ tiene módulo 1, esto está bien. Pero el radio alterna según la paridad, y la magnitud de $w^k$ es 1.

Nos falta la condición de simplicidad. En este tipo de problemas, la condición es que el ángulo de $A_2$ a $A_{11}$ sea $9\theta = 2\pi - 2\alpha$, con $\alpha$ el ángulo central en $O$ del triángulo $O A_2 A_{11}$.

Además, el triángulo $O A_2 A_{11}$ debe tener ángulo en $O$ igual a $\alpha$, y el área del polígono $A_2 A_3 \cdots A_{11}$ más el triángulo $A_{11} A_1 A_2$ debe ser $9 + \text{área}(A_2 O A_{11})$.

## 7. Método con suma vectorial

Para que el polígono sea cerrado, necesitamos que el punto $A_{11}$, seguido del segmento $A_{11}A_2$, cierre bien con $A_2$. Pero ya son cerrados: el polígono es $A_1 A_2 A_3 \cdots A_{11} A_1$.

Lo importante es la simplicidad. Consideremos el polígono formado por los 9 triángulos como una «pared» que encierra a $O$, y el triángulo $A_{11} A_1 A_2$ cierra el hueco. Para que sea simple, el segmento $A_{11} A_2$ no puede cruzar ninguno de los segmentos $A_i A_{i+1}$ internos, y $A_1$ debe quedar fuera o dentro de forma consistente.

La configuración estándar (este es un problema conocido, variante de una pregunta de la AIME/USAMO) es que el ángulo entre $OA_2$ y $OA_{11}$ es $9\theta - 2\pi$ o $2\pi - 9\theta$. 

Probemos que $9\theta = 2\pi - 2\beta$, donde $\beta = \angle A_2 A_1 A_{11}/2$ o algo así. Mejor resolvamos el sistema directamente.

## 8. Sistema de ecuaciones

Sabemos $ab = \frac{26}{5}$ y queremos $9d + a + b = 20$ con $d^2 = a^2 + b^2 - \frac{48}{5}$.

Escribamos $s = a + b$ y $p = ab = \frac{26}{5}$. Entonces:
$$a^2 + b^2 = s^2 - 2p = s^2 - \frac{52}{5}.$$
Por tanto:
$$d^2 = s^2 - \frac{52}{5} - \frac{48}{5} = s^2 - 20,$$
luego $d = \sqrt{s^2 - 20}$.

La ecuación del perímetro:
$$9\sqrt{s^2 - 20} + s = 20.$$

Resolverla:
$$9\sqrt{s^2 - 20} = 20 - s.$$
Elevando al cuadrado:
$$81(s^2 - 20) = 400 - 40s + s^2.$$
$$81s^2 - 1620 = 400 - 40s + s^2.$$
$$80s^2 + 40s - 2020 = 0.$$
$$2s^2 + s - \frac{101}{2} = 0,$$
multiplicando por 2:
$$4s^2 + 2s - 101 = 0.$$
$$s = \frac{-2 \pm \sqrt{4 + 1616}}{8} = \frac{-2 \pm \sqrt{1620}}{8} = \frac{-2 \pm 18\sqrt5}{8}.$$
Tomando la positiva (pues $a,b>0$):
$$s = \frac{-2 + 18\sqrt5}{8} = \frac{9\sqrt5 - 1}{4}.$$

## 9. ¿Cumple la condición de simplicidad?

Aquí está el punto sutil. Si simplemente resolvemos la ecuación del perímetro sin imponer la simplicidad, obtenemos $s = \frac{9\sqrt5 - 1}{4}$, y por tanto:
$$A_1 A_2 + A_1 A_{11} = a + b = s = \frac{9\sqrt5 - 1}{4}.$$

Esto ya tiene la forma $\frac{m\sqrt n - p}{q}$ con $m = 9$, $n = 5$, $p = 1$, $q = 4$, y $m+n+p+q = 9 + 5 + 1 + 4 = 19$.

Necesitamos verificar que la condición de simplicidad es compatible con esta solución. La solución aparentemente es única por la ecuación del perímetro, siempre que los ángulos centrales sumen $2\pi - \gamma$, lo cual es automático si la construcción es la estándar de un polígono en espiral no convexo.

Verifiquemos la compatibilidad. Tenemos $s = \frac{9\sqrt5 - 1}{4} \approx \frac{9 \cdot 2.236 - 1}{4} \approx \frac{20.124 - 1}{4} \approx 4.781$.

Además $p = \frac{26}{5} = 5.2$. Como $p > s^2/4 \approx 5.7...$? Revisemos: $s^2/4 \approx 4.781^2/4 \approx 5.71 > 5.2$, así que sí hay dos raíces reales.

Las raíces:
$$a,b = \frac{s \pm \sqrt{s^2 - 4p}}{2} = \frac{s \pm \sqrt{s^2 - \frac{104}{5}}}{2}.$$
$s^2 = \left(\frac{9\sqrt5 - 1}{4}\right)^2 = \frac{(9\sqrt5 - 1)^2}{16} = \frac{405 - 18\sqrt5 + 1}{16} = \frac{406 - 18\sqrt5}{16} = \frac{203 - 9\sqrt5}{8}$.

$s^2 - \frac{104}{5} = \frac{203 - 9\sqrt5}{8} - \frac{104}{5}$. Convertimos a común denominador 40:
$$\frac{5(203) - 45\sqrt5 - 832}{40} = \frac{1015 - 832 - 45\sqrt5}{40} = \frac{183 - 45\sqrt5}{40}.$$

Esto es positivo porque $183 - 45\sqrt5 \approx 183 - 100.623 \approx 82.38 > 0$, así que todo está bien.

Por tanto $a$ y $b$ son reales positivos.

## 10. Conclusión

La respuesta buscada es:
$$A_1 A_2 + A_1 A_{11} = \frac{9\sqrt5 - 1}{4},$$
así que $m = 9$, $n = 5$, $p = 1$, $q = 4$, y:
$$m + n + p + q = 9 + 5 + 1 + 4 = 19.$$

Por tanto:
$$\boxed{19}$$