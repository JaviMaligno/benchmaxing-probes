Voy a resolver el problema paso a paso.

**Paso 1: Establecer el marco geométrico**

El círculo $\omega$ tiene centro $O$ y pasa por $B$, $C$, $B'$, $C'$. Como $B$ y $C$ están en $\omega$, el centro $O$ está en la mediatriz de $BC$.

Además, $B'$ está en $AB$ y $C'$ está en $AC$. Los puntos $A$, $B'$, $B$ son colineales, y $A$, $C'$, $C$ son colineales.

**Paso 2: Propiedad de las potencias**

Como $\omega$ corta a la recta $AB$ en $B$ y $B'$, y a la recta $AC$ en $C$ y $C'$, por potencia de $A$ respecto de $\omega$:
$$AB \cdot AB' = AC \cdot AC'$$

Sustituyendo $AB = 18$ y $AC = 36$:
$$18 \cdot AB' = 36 \cdot AC'$$
$$AB' = 2 \cdot AC'$$

Sea $AC' = x$, entonces $AB' = 2x$.

**Paso 3: El punto de tangencia $T$**

Las circunferencias con diámetros $BB'$ y $CC'$ son tangentes exteriormente en $T$. 

Primero, calculemos los centros y radios de estos círculos.

- Para el círculo con diámetro $BB'$: su centro $M$ es el punto medio de $BB'$, y su radio es $r_B = \frac{BB'}{2}$.

- Para el círculo con diámetro $CC'$: su centro $N$ es el punto medio de $CC'$, y su radio es $r_C = \frac{CC'}{2}$.

Como $BB' = AB - AB' = 18 - 2x$ y $CC' = AC - AC' = 36 - x$:
$$r_B = \frac{18 - 2x}{2} = 9 - x$$
$$r_C = \frac{36 - x}{2} = 18 - \frac{x}{2}$$

**Paso 4: Relación con el punto $A$**

Observemos que ambos círculos con diámetros $BB'$ y $CC'$ pasan por $A$. ¿Por qué?

Por el teorema de Tales, el ángulo $\angle BAB'$ es $180°$ (es una línea recta), así que $A$ está en el círculo con diámetro $BB'$ (ya que el ángulo $\angle BAB'$ inscrito que subtiende el diámetro $BB'$ es recto). Específicamente, $A$, $B$, $B'$ son colineales, y el círculo con diámetro $BB'$ contiene a cualquier punto $P$ tal que $\angle BPB' = 90°$. Pero como $A$, $B$, $B'$ son colineales, $A$ no está "entre" $B$ y $B'$ en general, y el ángulo $\angle BAB' = 0°$ o $180°$, no $90°$.

Déjame reconsiderar. En realidad, el círculo con diámetro $BB'$ es el conjunto de puntos $P$ tales que $\angle BPB' = 90°$. Como $A$ está en la línea $BB'$, el ángulo $\angle BAB'$ no es $90°$ salvo que $A = B$ o $A = B'$. Así que $A$ no está en esos círculos.

**Paso 5: Potencia espectral de $A$ respecto al círculo con diámetro $BB'$**

Para el círculo con diámetro $BB'$, la potencia de $A$ es:
$$\text{Pot}(A) = AM^2 - r_B^2$$

El centro $M$ está en $AB$ (punto medio de $B$ y $B'$). Sea $AB = 18$ y $AB' = 2x$. Entonces la distancia $AM$ es la distancia de $A$ al punto medio de $B$ y $B'$.

Dependiendo del orden de los puntos en la línea $AB$: como $B'$ está entre $A$ y $B$ (porque $AB' < AB$ cuando $x > 0$ y $2x < 18$, es decir $x < 9$), tenemos la línea $A - B' - B$.

Entonces $AB' = 2x$ y $AB = 18$. El punto medio $M$ de $B$ y $B'$ tiene distancia desde $A$:
$$AM = \frac{AB + AB'}{2} = \frac{18 + 2x}{2} = 9 + x$$

El radio $r_B = \frac{BB'}{2} = \frac{18 - 2x}{2} = 9 - x$.

Entonces la potencia de $A$ respecto al círculo con diámetro $BB'$:
$$\text{Pot}_B(A) = AM^2 - r_B^2 = (9+x)^2 - (9-x)^2 = 36x$$

**Paso 6: Potencia de $A$ respecto al círculo con diámetro $CC'$**

De manera similar, en la línea $AC$, tenemos $A - C' - C$ (asumiendo $AC' = x < AC = 36$). El centro $N$ de $CC'$ tiene distancia desde $A$:
$$AN = \frac{AC + AC'}{2} = \frac{36 + x}{2} = 18 + \frac{x}{2}$$

El radio $r_C = \frac{CC'}{2} = \frac{36 - x}{2} = 18 - \frac{x}{2}$.

Entonces la potencia de $A$ respecto al círculo con diámetro $CC'$:
$$\text{Pot}_C(A) = AN^2 - r_C^2 = \left(18 + \frac{x}{2}\right)^2 - \left(18 - \frac{x}{2}\right)^2 = 36x$$

Vemos que la potencia de $A$ es la misma, $36x$, para ambos círculos. De hecho, ambos círculos pasan por $A$. Específicamente, el producto de las distancias desde $A$ a los extremos del diámetro es $AB \cdot AB' = 18 \cdot 2x = 36x$, y $AC \cdot AC' = 36 \cdot x = 36x$.

**Paso 7: $A$ está en ambos círculos**

Para el círculo con diámetro $BB'$, la potencia de $A$ es $AB \cdot AB' = 36x$. Si $A$ estuviera en el círculo, su potencia sería $0$. Como la potencia es $36x \neq 0$, $A$ no está en el círculo.

La potencia de un punto $P$ respecto a un círculo con centro $M$ y radio $r$ es $PM^2 - r^2$. También es igual al producto de las distancias de $P$ a las intersecciones de cualquier línea a través de $P$ con el círculo. Para el círculo con diámetro $BB'$, una línea a través de $A$ que interseca al círculo en $B$ y $B'$ da potencia $AB \cdot AB' = 18 \cdot 2x = 36x$.

Esto coincide con nuestro cálculo.

**Paso 8: Tangencia de los círculos**

Los círculos con diámetros $BB'$ y $CC'$ son tangentes exteriormente en $T$. Para que dos círculos sean tangentes exteriormente, la distancia entre sus centros es la suma de sus radios:
$$MN = r_B + r_C$$

**Paso 9: Relación con $AT$**

El punto $T$ es el punto de tangencia. Al ser tangentes exteriormente, $T$ está en la línea $MN$ (la línea de los centros). Además, $T$ divide a $MN$ en la razón $MT : TN = r_B : r_C$.

Dado que $A$ es un punto tal que ambos círculos tienen la misma potencia $36x$, hay una relación con el eje radical. El eje radical de los dos círculos es la línea que pasa por $T$ y es perpendicular a $MN$ (para círculos tangentes, el eje radical es la tangente común en $T$).

La potencia de $A$ respecto a ambos círculos es igual ($36x$), lo que significa que $A$ está en el eje radical. Por lo tanto, $A$ está en la tangente común en $T$, es decir, $AT$ es perpendicular a $MN$ (o más bien, $AT$ está en el eje radical).

En realidad, para dos círculos tangentes exteriormente en $T$, el eje radical es la tangente común en $T$, perpendicular a la línea de centros $MN$. Como $A$ está en el eje radical, la línea $AT$ es perpendicular a $MN$, y $T$ es el pie de la perpendicular desde $A$ a $MN$.

Por lo tanto, $AT \perp MN$ y $AT = 12$.

**Paso 10: Geometría del triángulo $AMN$**

En el triángulo $AMN$:
- $AM = 9 + x$
- $AN = 18 + \frac{x}{2}$
- $MN = r_B + r_C = (9-x) + (18 - \frac{x}{2}) = 27 - \frac{3x}{2}$
- $AT \perp MN$ con $AT = 12$

El área del triángulo $AMN$ es:
$$\text{Área} = \frac{1}{2} \cdot MN \cdot AT = \frac{1}{2} \cdot \left(27 - \frac{3x}{2}\right) \cdot 12 = 6\left(27 - \frac{3x}{2}\right) = 162 - 9x$$

Alternativamente, usando la fórmula de Herón o el teorema de la altura:
$$AT^2 = AM^2 - MT^2 = AN^2 - NT^2$$

donde $MT + NT = MN$.

Además, $MT = r_B = 9 - x$ (porque $T$ es el punto de tangencia, así que $MT$ es el radio del círculo con centro $M$, y $NT = r_C = 18 - \frac{x}{2}$).

Verifiquemos: $MT = r_B = 9 - x$ y $NT = r_C = 18 - \frac{x}{2}$. Entonces $MT + NT = 27 - \frac{3x}{2} = MN$. ✓

**Paso 11: Teorema de Pitágoras en $\triangle AMT$ y $\triangle ANT$**

En $\triangle AMT$ (rectángulo en $T$):
$$AM^2 = AT^2 + MT^2$$
$$(9+x)^2 = 12^2 + (9-x)^2$$

Desarrollando:
$$81 + 18x + x^2 = 144 + 81 - 18x + x^2$$
$$81 + 18x + x^2 = 225 - 18x + x^2$$
$$81 + 18x = 225 - 18x$$
$$36x = 144$$
$$x = 4$$

**Paso 12: Verificación con $\triangle ANT$**

Con $x = 4$:
- $AN = 18 + \frac{4}{2} = 18 + 2 = 20$
- $NT = r_C = 18 - \frac{4}{2} = 18 - 2 = 16$

Verificamos: $AN^2 = AT^2 + NT^2$:
$$20^2 = 12^2 + 16^2 = 144 + 256 = 400 = 20^2$$ ✓

Con $x = 4$:
- $AM = 9 + 4 = 13$
- $MT = 9 - 4 = 5$
- $13^2 = 12^2 + 5^2 = 144 + 25 = 169$ ✓

**Paso 13: Encontrar $AO$**

Ahora tenemos $x = 4$, así que:
- $AB' = 2x = 8$
- $AC' = x = 4$

Necesitamos encontrar $AO$, el radio de $\omega$ y distancia desde $O$ a $A$.

Sabemos que $O$ está en $\omega$, y $\omega$ contiene a $B$, $B'$, $C$, $C'$. El centro $O$ es el centro de $\omega$.

Los puntos $B$ y $B'$ están en la línea $AB$, y los puntos $C$ y $C'$ están en la línea $AC$. El centro $O$ está en la intersección de las mediatrices de las cuerdas $BB'$ y $CC'$.

La mediatriz de $BB'$ es perpendicular a $AB$ y pasa por el punto medio $M$ de $BB'$. La mediatriz de $CC'$ es perpendicular a $AC$ y pasa por el punto medio $N$ de $CC'$.

Entonces $O$ es la intersección de:
- La línea perpendicular a $AB$ a través de $M$
- La línea perpendicular a $AC$ a través de $N$

Esto significa que $OM \perp AB$ y $ON \perp AC$.

**Paso 14: Calcular $AO$**

Del paso anterior, sabemos:
- $OM = AT = 12$? No, veamos.

Espera. $M$ es el centro del círculo con diámetro $BB'$. La línea $OM$ es perpendicular a $AB$ (porque $O$ es el centro de $\omega$ y $M$ es el punto medio de la cuerda $BB'$, entonces $OM \perp BB'$, es decir, $OM \perp AB$).

Similarmente, $ON \perp AC$, y $N$ es el punto medio de $CC'$.

Ahora, necesitamos establecer la relación entre $M$, $N$, $A$, y $O$.

Sabemos $AM = 13$ (desde el paso 12). También sabemos que $OM$ es la distancia desde $O$ a $M$ a lo largo de la perpendicular a $AB$.

Y $AN = 20$, con $ON$ perpendicular a $AC$.

Como $O$ es el centro de $\omega$, los radios $OB$, $OB'$, $OC$, $OC'$ son todos iguales.

Para el círculo $\omega$:
- $OB^2 = OM^2 + MB^2$
- $OC^2 = ON^2 + NC^2$

donde $MB = r_B = 9 - x = 5$ y $NC = r_C = 18 - \frac{x}{2} = 16$.

Espera, $MB = \frac{BB'}{2} = 5$ y $NC = \frac{CC'}{2} = 16$.

Entonces si $R = AO$ es el radio de $\omega$:
$$R^2 = OM^2 + 5^2 = ON^2 + 16^2$$

Además, $OM$ y $ON$ están relacionados con $AT$ y la geometría del triángulo.

**Paso 15: Relación entre $O$, $M$, $N$ y $T$**

Recordemos que $T$ es el punto de tangencia de los círculos con diámetros $BB'$ y $CC'$. Los círculos tienen centros $M$ y $N$ respectivamente, y son tangentes en $T$. Por lo tanto, $M$, $T$, $N$ son colineales, con $MT = 5$ y $TN = 16$ (para $x=4$).

Ahora, $AT \perp MN$ (como establecimos). También hemos visto que $OM \perp AB$ y $ON \perp AC$.

¿Cuál es la relación entre las líneas $AB$ y $MN$? Y ¿entre $AC$ y $MN$?

**Paso 16: Ángulos y coordenadas**

Establezcamos coordenadas para claridad. Pongamos $A$ en el origen $(0,0)$. 

Como $AB' = 8$ y $AB = 18$, pongamos $B'$ en $(8, 0)$ y $B$ en $(18, 0)$ a lo largo del eje $x$.

Para el lado $AC$, con $AC' = 4$ y $AC = 36$, pongamos $C'$ y $C$ a lo largo de un rayo desde $A$ que forma un ángulo $\theta$ con $AB$.

Entonces:
- $C' = (4\cos\theta, 4\sin\theta)$
- $C = (36\cos\theta, 36\sin\theta)$

**Paso 17: Centros $M$ y $N$**

- $M$ es el punto medio de $B = (18,0)$ y $B' = (8,0)$, así que $M = (13, 0)$.
- $N$ es el punto medio de $C = (36\cos\theta, 36\sin\theta)$ y $C' = (4\cos\theta, 4\sin\theta)$, así que $N = (20\cos\theta, 20\sin\theta)$.

Esto confirma $AM = 13$ y $AN = 20$.

**Paso 18: La condición de tangencia**

Los círculos con diámetros $BB'$ y $CC'$ son tangentes exteriormente, así que $MN = 5 + 16 = 21$.

Calculamos $MN$:
$$MN^2 = (20\cos\theta - 13)^2 + (20\sin\theta)^2$$
$$= 400\cos^2\theta - 520\cos\theta + 169 + 400\sin^2\theta$$
$$= 400(\cos^2\theta + \sin^2\theta) - 520\cos\theta + 169$$
$$= 400 - 520\cos\theta + 169 = 569 - 520\cos\theta$$

Igualando a $21^2 = 441$:
$$569 - 520\cos\theta = 441$$
$$520\cos\theta = 128$$
$$\cos\theta = \frac{128}{520} = \frac{16}{65}$$

**Paso 19: El punto $T$**

El punto $T$ divide a $MN$ en la razón $MT : TN = 5 : 16$, así que $T = M + \frac{5}{21}(N - M)$.

$$T = (13, 0) + \frac{5}{21}(20\cos\theta - 13, 20\sin\theta)$$
$$T_x = 13 + \frac{5}{21}(20\cos\theta - 13)$$
$$T_y = \frac{5}{21} \cdot 20\sin\theta = \frac{100}{21}\sin\theta$$

Dado que $AT \perp MN$ y $AT = 12$, verificamos que esto es consistente.

$AT^2 = T_x^2 + T_y^2 = 144$. Verifiquemos:

$T_x = 13 + \frac{5}{21}(20 \cdot \frac{16}{65} - 13) = 13 + \frac{5}{21}(\frac{320}{65} - 13) = 13 + \frac{5}{21}(\frac{64}{13} - 13)$

$= 13 + \frac{5}{21}(\frac{64 - 169}{13}) = 13 + \frac{5}{21} \cdot \frac{-105}{13} = 13 - \frac{525}{273} = 13 - \frac{25}{13} = \frac{169 - 25}{13} = \frac{144}{13}$

$T_y = \frac{100}{21} \cdot \sin\theta$. Como $\cos\theta = \frac{16}{65}$,
$$\sin\theta = \sqrt{1 - \frac{256}{4225}} = \sqrt{\frac{3969}{4225}} = \frac{63}{65}$$

$$T_y = \frac{100}{21} \cdot \frac{63}{65} = \frac{6300}{1365} = \frac{420}{91} = \frac{60}{13}$$

$$AT^2 = \left(\frac{144}{13}\right)^2 + \left(\frac{60}{13}\right)^2 = \frac{20736 + 3600}{169} = \frac{24336}{169} = 144$$ ✓

**Paso 20: Encontrar $O$**

El centro $O$ de $\omega$ es la intersección de:
1. La mediatriz de $BB'$, que es la línea perpendicular a $AB$ a través de $M = (13,0)$. Esta es la línea vertical $x = 13$.
2. La mediatriz de $CC'$, que es la línea perpendicular a $AC$ a través de $N = (20\cos\theta, 20\sin\theta)$.

De (1), $O_x = 13$.

De (2), $O$ está en la línea perpendicular a $AC$ a través de $N$. La dirección de $AC$ es $(\cos\theta, \sin\theta)$, así que la dirección perpendicular es $(-\sin\theta, \cos\theta)$. Por lo tanto, $O = N + t(-\sin\theta, \cos\theta)$ para algún $t$:
$$O_x = 20\cos\theta - t\sin\theta = 13$$
$$O_y = 20\sin\theta + t\cos\theta$$

De la primera ecuación:
$$t\sin\theta = 20\cos\theta - 13 = 20 \cdot \frac{16}{65} - 13 = \frac{320}{65} - 13 = \frac{64}{13} - 13 = \frac{64 - 169}{13} = -\frac{105}{13}$$

$$t = -\frac{105}{13\sin\theta} = -\frac{105}{13 \cdot \frac{63}{65}} = -\frac{105 \cdot 65}{13 \cdot 63} = -\frac{6825}{819} = -\frac{25}{3}$$

Entonces:
$$O_y = 20\sin\theta + t\cos\theta = 20 \cdot \frac{63}{65} + \left(-\frac{25}{3}\right) \cdot \frac{16}{65} = \frac{1260}{65} - \frac{400}{195}$$

$$= \frac{1260}{65} - \frac{400}{195} = \frac{3780 - 400}{195} = \frac{3380}{195} = \frac{52}{3}$$

**Paso 21: Calcular $AO$**

$$AO^2 = O_x^2 + O_y^2 = 13^2 + \left(\frac{52}{3}\right)^2 = 169 + \frac{2704}{9} = \frac{1521 + 2704}{9} = \frac{4225}{9}$$

$$AO = \frac{65}{3}$$

**Verificación adicional:**
El radio de $\omega$ es $OA = OB$:
$$OB^2 = (18 - 13)^2 + (0 - \frac{52}{3})^2 = 25 + \frac{2704}{9} = \frac{225 + 2704}{9} = \frac{2929}{9}$$

Espera, esto no coincide con $AO^2 = \frac{4225}{9}$. Hay un error.

Déjame revisar. $OB^2$ debería ser igual a $AO^2$ si $O$ es el centro de $\omega$ y $B$ está en $\omega$.

$OB^2 = (B - O)^2 = (18 - 13)^2 + (0 - \frac{52}{3})^2 = 25 + \frac{2704}{9} = \frac{225}{9} + \frac{2704}{9} = \frac{2929}{9}$.

Pero $AO^2 = \frac{4225}{9}$. Estos no son iguales, lo que significa que hay un error.

**Paso 22: Corregir el error**

Déjame reconsiderar. El hecho de que $\omega$ pase por $B$ significa que $OB$ es el radio. Pero también $\omega$ pasa por $B'$. Entonces $OB = OB'$.

$OB'^2 = (8 - 13)^2 + (0 - \frac{52}{3})^2 = 25 + \frac{2704}{9} = \frac{2929}{9}$.

Así que $OB = OB' = \sqrt{\frac{2929}{9}}$. Pero $A$ no está en $\omega$, así que $AO$ no es el radio. $AO$ es simplemente la distancia desde $A$ al centro $O$.

De hecho, $AO^2 = 13^2 + (\frac{52}{3})^2 = 169 + \frac{2704}{9} = \frac{1521 + 2704}{9} = \frac{4225}{9}$, y $AO = \frac{65}{3}$.

Esto es correcto. El radio de $\omega$ es $OB = \sqrt{\frac{2929}{9}} = \frac{\sqrt{2929}}{3}$, pero lo que se pide es $AO$, no el radio.

Así que $AO = \frac{65}{3}$.

**Verificación de que $OB = OC$:**

$OC^2 = (36\cos\theta - 13)^2 + (36\sin\theta - \frac{52}{3})^2$
$36\cos\theta = 36 \cdot \frac{16}{65} = \frac{576}{65}$, y $36\sin\theta = 36 \cdot \frac{63}{65} = \frac{2268}{65}$.

$OC^2 = \left(\frac{576}{65} - \frac{845}{65}\right)^2 + \left(\frac{2268}{65} - \frac{52}{3}\right)^2$
$= \left(\frac{-269}{65}\right)^2 + \left(\frac{2268}{65} - \frac{3380}{195}\right)^2$
$= \frac{72361}{4225} + \left(\frac{6804 - 3380}{195}\right)^2$
$= \frac{72361}{4225} + \left(\frac{3424}{195}\right)^2 = \frac{72361}{4225} + \frac{11723776}{38025}$

$= \frac{651249}{38025} + \frac{11723776}{38025} = \frac{12375025}{38025}$

Pero $OB^2 = \frac{2929}{9} = \frac{2929 \cdot 4225}{9 \cdot 4225} = \frac{12375025}{38025}$. ✓ 

Todo coincide.

**Respuesta final:**

$$\boxed{\frac{65}{3}}$$