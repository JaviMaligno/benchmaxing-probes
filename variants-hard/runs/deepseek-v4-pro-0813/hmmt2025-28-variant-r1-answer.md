 Today's date is 2026-10-29.Voy a resolver el problema paso a paso.

**Paso 1: Establecer coordenadas**

Coloquemos el trapecio en un plano de coordenadas. Como $PQ \parallel RS$ y es un trapecio isósceles, el eje de simetría es perpendicular a las bases.

Pongamos:
- $P = (-3, h)$
- $Q = (3, h)$
- $S = (-a, 0)$
- $R = (a, 0)$

donde $a > 3$ (porque $RS = 2a > 6 = PQ$). Aquí $h$ es la altura del trapecio.

La condición de trapecio isósceles se cumple automáticamente con esta simetría.

**Paso 2: Determinar $T$**

$T$ está sobre la recta $RS$ con $ST = 3$ y $S$ entre $T$ y $R$. Como $S = (-a, 0)$ y $R = (a, 0)$, el punto $T$ está a la izquierda de $S$:
$$T = (-a - 3, 0).$$

**Paso 3: Punto medio $N$ de $PT$**

$$N = \left(\frac{-3 + (-a-3)}{2}, \frac{h + 0}{2}\right) = \left(\frac{-a-6}{2}, \frac{h}{2}\right).$$

**Paso 4: Círculo que pasa por $P, Q, R, S$**

Por simetría, el centro del círculo está en el eje $y$. Llamémoslo $O = (0, k)$.

Como $R = (a, 0)$ y $S = (-a, 0)$ están en el círculo de radio $7$:
$$a^2 + k^2 = 49.$$

Como $P = (-3, h)$ está en el círculo:
$$9 + (h - k)^2 = 49 \implies (h - k)^2 = 40.$$

**Paso 5: Condición de que $N$ está en el círculo**

$N = \left(-\frac{a+6}{2}, \frac{h}{2}\right)$. La distancia desde $O = (0, k)$ a $N$ debe ser $7$:
$$\left(\frac{a+6}{2}\right)^2 + \left(\frac{h}{2} - k\right)^2 = 49.$$

Multiplicando por $4$:
$$(a+6)^2 + (h - 2k)^2 = 196.$$

**Paso 6: Resolver el sistema**

De $a^2 + k^2 = 49$ y $(h-k)^2 = 40$:
$$h = k \pm \sqrt{40} = k \pm 2\sqrt{10}.$$

De la segunda ecuación:
$$(a+6)^2 + (h - 2k)^2 = 196.$$

Sustituyamos $a^2 = 49 - k^2$.

Desarrollamos $(a+6)^2 = a^2 + 12a + 36 = (49 - k^2) + 12a + 36 = 85 - k^2 + 12a$.

Entonces:
$$85 - k^2 + 12a + (h - 2k)^2 = 196.$$

**Caso $h = k + 2\sqrt{10}$:**
$$h - 2k = 2\sqrt{10} - k.$$
$$85 - k^2 + 12a + (2\sqrt{10} - k)^2 = 196.$$
$$85 - k^2 + 12a + 40 - 4k\sqrt{10} + k^2 = 196.$$
$$125 + 12a - 4k\sqrt{10} = 196.$$
$$12a - 4k\sqrt{10} = 71.$$

**Caso $h = k - 2\sqrt{10}$:**
$$h - 2k = -2\sqrt{10} - k.$$
$$85 - k^2 + 12a + (2\sqrt{10} + k)^2 = 196.$$
$$85 - k^2 + 12a + 40 + 4k\sqrt{10} + k^2 = 196.$$
$$125 + 12a + 4k\sqrt{10} = 196.$$
$$12a + 4k\sqrt{10} = 71.$$

**Paso 7: Encontrar $NS$**

Calculemos la distancia $NS$. Tenemos:
$$N = \left(-\frac{a+6}{2}, \frac{h}{2}\right), \quad S = (-a, 0).$$

Entonces:
$$NS^2 = \left(-\frac{a+6}{2} + a\right)^2 + \left(\frac{h}{2}\right)^2 = \left(\frac{a-6}{2}\right)^2 + \frac{h^2}{4}.$$

$$NS^2 = \frac{(a-6)^2 + h^2}{4}.$$

Usemos las relaciones anteriores. De $a^2 + k^2 = 49$ y las ecuaciones lineales.

Combinemos las dos ecuaciones:
- Caso 1: $12a - 4k\sqrt{10} = 71$
- Caso 2: $12a + 4k\sqrt{10} = 71$

Además, $a^2 + k^2 = 49$.

**Caso 2:** $12a + 4k\sqrt{10} = 71 \implies 3a + k\sqrt{10} = \frac{71}{4}$.

Despejamos $k = \frac{71/4 - 3a}{\sqrt{10}}$.

Sustituimos en $a^2 + k^2 = 49$:
$$a^2 + \frac{(71/4 - 3a)^2}{10} = 49.$$
$$10a^2 + (17.75 - 3a)^2 = 490.$$
$$10a^2 + 9a^2 - 106.5a + 315.0625 = 490.$$
$$19a^2 - 106.5a - 174.9375 = 0.$$

Multiplicando por $16$ para evitar decimales: $304a^2 - 1704a - 2799 = 0$.

Dividiendo por... mejor usemos fracciones exactas: $\frac{71}{4}$.

$$a^2 + \frac{(\frac{71}{4} - 3a)^2}{10} = 49.$$

Multiplicando por $160$:
$$160a^2 + (71 - 12a)^2 = 7840.$$
$$160a^2 + 5041 - 1704a + 144a^2 = 7840.$$
$$304a^2 - 1704a - 2799 = 0.$$

Dividimos por... $304 = 16 \cdot 19$, $1704 = 16 \cdot 106.5$, no exacto. Dejemos así y usemos la fórmula cuadrática:

$304a^2 - 1704a - 2799 = 0$.

$$a = \frac{1704 \pm \sqrt{1704^2 + 4 \cdot 304 \cdot 2799}}{2 \cdot 304}.$$

$1704^2 = 2903616$. $4 \cdot 304 \cdot 2799 = 1216 \cdot 2799 = 3403584$.

Suma: $2903616 + 3403584 = 6307200$.

$\sqrt{6307200} = \sqrt{63072 \cdot 100} = 10\sqrt{63072}$.

$63072 = 64 \cdot 985.5$... mejor factoricemos: $6307200 = 63072 \cdot 100$. 

$63072 = 2^6 \cdot 3 \cdot ... $ Probemos: $63072 / 64 = 985.5$, no entero. 

$63072 = 2^5 \cdot 1971 = 32 \cdot 1971$. $1971 = 3 \cdot 657 = 3 \cdot 3 \cdot 219 = 9 \cdot 219 = 9 \cdot 3 \cdot 73 = 27 \cdot 73$.

Entonces $63072 = 32 \cdot 27 \cdot 73 = 864 \cdot 73$.

$6307200 = 86400 \cdot 73 = (120\sqrt{6})^2 \cdot 73$... no simplifica bonito.

Quizás el otro caso da una solución más limpia. Probemos una estrategia diferente.

**Estrategia alternativa: usar potencia o geometría**

Podemos usar la condición de que $N$ está en el círculo de otra manera.

Por el teorema de la potencia de un punto, o usando que $P, T, N$ son colineales y $N$ es el punto medio de $PT$.

Observemos que $P$ y $N$ están en el círculo, y $T$ está en la recta $PT$. La recta $PT$ interseca al círculo en $P$ y $N$ (ya que $N$ está en el círculo y en la recta $PT$).

Entonces $T$ tiene potencia $TP \cdot TN$ respecto al círculo. Pero además $T$ está en la recta $RS$, que interseca al círculo en $S$ y $R$. Entonces por potencia:

$$TS \cdot TR = TP \cdot TN.$$

Sabemos $TS = 3$, $TR = TS + SR = 3 + 2a$.

$N$ es el punto medio de $PT$, así que $PN = NT = \frac{PT}{2}$.

Entonces $TP \cdot TN = PT \cdot \frac{PT}{2} = \frac{PT^2}{2}$.

Por otro lado, $TS \cdot TR = 3 \cdot (3 + 2a)$.

Entonces:
$$3(3 + 2a) = \frac{PT^2}{2}.$$

Ahora, $PT^2 = (a+3)^2 + h^2$ (la distancia entre $P = (-3, h)$ y $T = (-a-3, 0)$):

$$PT^2 = (a+3-3)^2 + h^2 = a^2 + h^2... $$ 

Espera, recalculemos: $P = (-3, h)$, $T = (-a-3, 0)$.

Diferencia en $x$: $(-a-3) - (-3) = -a$. Diferencia en $y$: $0 - h = -h$.

$$PT^2 = a^2 + h^2.$$

¡Excelente! Entonces:
$$3(3 + 2a) = \frac{a^2 + h^2}{2}.$$
$$6(3 + 2a) = a^2 + h^2.$$
$$18 + 12a = a^2 + h^2.$$

Ahora, $NS^2 = \frac{(a-6)^2 + h^2}{4}$.

Tenemos $h^2 = 18 + 12a - a^2$, así que:

$$NS^2 = \frac{(a-6)^2 + 18 + 12a - a^2}{4}.$$
$$= \frac{a^2 - 12a + 36 + 18 + 12a - a^2}{4} = \frac{54}{4} = \frac{27}{2}.$$

¡Perfecto, se cancelan los términos con $a$! Entonces:

$$NS = \sqrt{\frac{27}{2}} = \frac{3\sqrt{6}}{2}.$$

Espera, pero también necesitamos verificar que realmente existe tal configuración con el radio $7$. La condición del círculo de radio $7$ nos da $a^2 + k^2 = 49$. Necesitamos confirmar que esto es consistente.

Del círculo: $P = (-3, h)$, $S = (-a, 0)$, con centro $O = (0, k)$:

Para $S$: $a^2 + k^2 = 49$.

Para $P$: $9 + (h-k)^2 = 49$, así que $(h-k)^2 = 40$.

También de la potencia: $18 + 12a = a^2 + h^2$.

Veamos si esto es consistente con $a^2 + k^2 = 49$ y $(h-k)^2 = 40$.

De $a^2 + k^2 = 49$: $a^2 = 49 - k^2$.

De $(h-k)^2 = 40$: $h^2 - 2hk + k^2 = 40$, así que $h^2 = 40 + 2hk - k^2$.

Sustituyendo en $18 + 12a = a^2 + h^2$:
$$18 + 12a = 49 - k^2 + 40 + 2hk - k^2.$$
$$18 + 12a = 89 - 2k^2 + 2hk.$$

Hmm, esto se complica. Pero quizás el valor de $NS$ es independiente de $a$ y $h$, como vimos.

**Verificación del resultado**

$NS = \frac{3\sqrt{6}}{2}$. Veamos si tiene una forma más simple: $\frac{3\sqrt{6}}{2} \approx 3.674$.

En realidad, notemos que $NS^2 = \frac{27}{2} = 13.5$, así que $NS = \frac{3\sqrt{6}}{2} = \frac{3\sqrt{6}}{2}$.

Alternativamente, $\frac{27}{2} = \frac{54}{4}$, así que $NS = \frac{\sqrt{54}}{2} = \frac{3\sqrt{6}}{2}$.

Pero esperemos: ¿debería ser un número entero o más "bonito"? Revisemos el cálculo.

Recalculemos $NS^2$:

$N = \left(\frac{-3 + (-a-3)}{2}, \frac{h}{2}\right) = \left(\frac{-a-6}{2}, \frac{h}{2}\right)$.

$S = (-a, 0)$.

$NS^2 = \left(-a - \frac{-a-6}{2}\right)^2 + \left(\frac{h}{2}\right)^2 = \left(-a + \frac{a+6}{2}\right)^2 + \frac{h^2}{4}$.

$-a + \frac{a+6}{2} = \frac{-2a + a + 6}{2} = \frac{6 - a}{2} = \frac{-(a-6)}{2}$.

Así que $NS^2 = \frac{(a-6)^2}{4} + \frac{h^2}{4} = \frac{(a-6)^2 + h^2}{4}$. ✓

$PT^2$: $P = (-3, h)$, $T = (-a-3, 0)$.

Diferencia en $x$: $-a - 3 - (-3) = -a$. Diferencia en $y$: $-h$.

$PT^2 = a^2 + h^2$. ✓

Potencia: $TS = 3$, $TR = TS + SR$. $SR = 2a$ (de $S=-a$ a $R=a$). Entonces $TR = 3 + 2a$. ✓

$TP \cdot TN$: $N$ es punto medio de $PT$, así que $TN = PT/2$. Entonces $TP \cdot TN = PT \cdot (PT/2) = PT^2/2$. ✓

Potencia: $TS \cdot TR = TP \cdot TN$ (con signo, pero aquí todo positivo). $3(3+2a) = PT^2/2$. ✓

$3(3+2a) = \frac{a^2 + h^2}{2} \implies 6(3+2a) = a^2 + h^2 \implies 18 + 12a = a^2 + h^2$. ✓

$NS^2 = \frac{(a-6)^2 + h^2}{4} = \frac{a^2 - 12a + 36 + h^2}{4} = \frac{(a^2 + h^2) - 12a + 36}{4}$.

$a^2 + h^2 = 18 + 12a$, entonces:

$NS^2 = \frac{18 + 12a - 12a + 36}{4} = \frac{54}{4} = \frac{27}{2}$. ✓

Entonces $NS = \sqrt{\frac{27}{2}} = \frac{3\sqrt{6}}{2}$.

Pero espera, esto es $\sqrt{27/2} = \sqrt{13.5} \approx 3.674$. ¿Es plausible dado el radio 7? Sí.

Sin embargo, necesitamos asegurarnos de que la configuración realmente exista (que haya una solución geométrica válida con radio 7). El problema afirma que existe tal configuración, así que podemos confiar en eso. El radio $7$ no se usó directamente en el cálculo de $NS$, lo cual es interesante pero válido: el resultado resultó independiente del radio. Aunque en realidad, el radio sí está implícito en la existencia.

Revisemos si hay alguna sutileza con el radio. La condición de que $N$ esté en el círculo ya se usó (vía potencia), así que la condición del radio 7 es redundante para calcular $NS$. Esto es consistente con que el resultado sea independiente de $a$ y $h$.

**Verificación adicional**

¿Podría haber otra interpretación? $T$ está en la línea $RS$ con $ST = 3$ y $S$ entre $T$ y $R$. Esto significa que $T$ está del lado de $S$ opuesto a $R$, como asumimos.

Además, $N$ es el punto medio de $PT$. Todo parece correcto.

Una verificación más: si $a = 6$, entonces $NS^2 = \frac{(0)^2 + h^2}{4} = \frac{h^2}{4}$, y $h^2 = 18 + 72 - 36 = 54$, así que $NS^2 = 13.5$. Consistente.

En realidad notemos que si $a = 6$, entonces $RS = 12$, $PQ = 6$, y el trapecio tendría una forma específica. Pero en general el resultado es independiente.

**Resultado final**

$$NS = \frac{3\sqrt{6}}{2}.$$

En realidad, $\frac{3\sqrt{6}}{2} = \frac{\sqrt{54}}{2} = \sqrt{\frac{27}{2}} \approx 3.674$.

Pero permíteme reconsiderar: ¿el resultado podría simplificarse a un entero? $\frac{3\sqrt{6}}{2} \approx 3.674$ no es un entero. ¿Quizás cometí un error en la potencia?

Revisemos la potencia de $T$ una vez más. La recta $PT$ interseca al círculo en $P$ y en $N$ (porque $N$ está en el círculo y está en la recta $PT$). La recta $RS$ interseca al círculo en $S$ y $R$.

Por potencia desde $T$:
$$TP \cdot TN = TS \cdot TR.$$

$TP$ es la distancia completa desde $T$ hasta $P$. $TN$ es la distancia desde $T$ hasta $N$. Como $N$ es el punto medio de $PT$, $TN = PT/2$. Entonces $TP \cdot TN = PT \cdot (PT/2) = PT^2/2$. 

$PT^2 = a^2 + h^2$ (correcto: $P=(-3,h)$, $T=(-a-3,0)$, la diferencia en x es $-a$, en y es $-h$).

Entonces $PT^2/2 = (a^2 + h^2)/2$.

$TS = 3$, $TR = 3 + 2a$ (correcto: $S = -a$, $R = a$, así que $SR = 2a$, y $T$ está 3 unidades a la izquierda de $S$, así que $TR = 3 + 2a$).

Entonces $TS \cdot TR = 3(3 + 2a) = 9 + 6a$.

Igualando: $(a^2 + h^2)/2 = 9 + 6a$, así que $a^2 + h^2 = 18 + 12a$. ✓

$NS^2 = \frac{(a-6)^2 + h^2}{4}$.

$(a-6)^2 = a^2 - 12a + 36$.

$NS^2 = \frac{a^2 - 12a + 36 + h^2}{4} = \frac{(a^2 + h^2) - 12a + 36}{4} = \frac{18 + 12a - 12a + 36}{4} = \frac{54}{4} = \frac{27}{2}$.

$NS = \sqrt{\frac{27}{2}} = \frac{3\sqrt{6}}{2}$.

Todo es consistente. El resultado es $\frac{3\sqrt{6}}{2}$.

Pero, hmm, ¿es posible que el radio 7 imponga una restricción que haga que solo ciertos valores de $a$ funcionen, y que mi resultado sea correcto? Sí, el radio 7 determina $a$ y $h$ específicos, pero $NS$ resulta ser constante. Esto es una propiedad interesante.

**Resultado final:**
$$\boxed{\frac{3\sqrt{6}}{2}}$$