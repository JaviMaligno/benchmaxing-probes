¡Vamos a resolver el problema paso a paso!

**Paso 1: Ubicar la configuración geométrica**

Tenemos una circunferencia $\omega$ con diámetro $\overline{AB}$, donde $AB = 20$. Por lo tanto, el radio es $R = 10$ y el centro $O$ está en el punto medio de $AB$.

Como $\overline{AB}$ es diámetro, cualquier ángulo $\angle ACB$ o $\angle ADB$ es recto (ángulo inscrito en semicircunferencia). Además, $C$ y $D$ están en el mismo lado de $\overline{AB}$.

Datos:
- $BC = 13$
- $AD = 7$

**Paso 2: Colocar coordenadas**

Pongamos $O$ en el origen. Como $AB$ es diámetro de longitud 20, podemos poner:
- $A = (-10, 0)$
- $B = (10, 0)$

La circunferencia tiene ecuación $x^2 + y^2 = 100$.

**Paso 3: Encontrar $C$**

Sabemos que $BC = 13$. El punto $B = (10,0)$ y $C$ está sobre la circunferencia. Además, $\angle ACB = 90°$, lo que significa que $C$ cae en la semicircunferencia superior (ya que $C$ y $D$ están en el mismo lado de $AB$).

Como $\angle ACB = 90°$, el triángulo $ABC$ es rectángulo en $C$. Tenemos $AB = 20$ (hipotenusa) y $BC = 13$. Por el teorema de Pitágoras:

$$AC = \sqrt{20^2 - 13^2} = \sqrt{400 - 169} = \sqrt{231}$$

Ahora, usando la proyección: en un triángulo rectángulo $ABC$ con hipotenusa $AB = 20$, cateto $BC = 13$, cateto $AC = \sqrt{231}$.

La coordenada $x$ de $C$ se puede hallar usando que $\angle ABC$ cumple $\cos \angle ABC = \frac{BC}{AB} = \frac{13}{20}$.

Mirando desde $B$, el vector hacia $C$ forma un ángulo $\theta$ con $\overrightarrow{BA}$, donde $\cos\theta = \frac{13}{20}$.

Alternativamente, podemos usar la relación $BC^2 = (x_C - 10)^2 + y_C^2 = 169$ junto con $x_C^2 + y_C^2 = 100$.

Restamos:
$$(x_C - 10)^2 + y_C^2 - (x_C^2 + y_C^2) = 169 - 100 = 69$$
$$x_C^2 - 20x_C + 100 + y_C^2 - x_C^2 - y_C^2 = 69$$
$$-20x_C + 100 = 69$$
$$-20x_C = -31$$
$$x_C = \frac{31}{20} = 1.55$$

Entonces $y_C = \sqrt{100 - (31/20)^2} = \sqrt{100 - 961/400} = \sqrt{\frac{40000-961}{400}} = \sqrt{\frac{39039}{400}}$.

Verifiquemos: $39039 = 40000 - 961$. Notamos que $39039 = 231 \cdot 169 = 231 \cdot 13^2$. Entonces:

$$y_C = \frac{\sqrt{39039}}{20} = \frac{13\sqrt{231}}{20}$$

**Paso 4: Encontrar $D$**

Sabemos que $AD = 7$. El punto $A = (-10, 0)$ y $D$ está en la semicircunferencia superior. Similarmente, $D = (x_D, y_D)$ cumple:

- $x_D^2 + y_D^2 = 100$
- $(x_D + 10)^2 + y_D^2 = 49$

Restamos:
$$(x_D + 10)^2 + y_D^2 - (x_D^2 + y_D^2) = 49 - 100 = -51$$
$$x_D^2 + 20x_D + 100 + y_D^2 - x_D^2 - y_D^2 = -51$$
$$20x_D + 100 = -51$$
$$20x_D = -151$$
$$x_D = -\frac{151}{20} = -7.55$$

Entonces $y_D = \sqrt{100 - (151/20)^2} = \sqrt{100 - 22801/400} = \sqrt{\frac{40000 - 22801}{400}} = \sqrt{\frac{17199}{400}}$.

Notemos que $17199 = 49 \cdot 351$ y también $17199 = 7^2 \cdot 351$. Verifiquemos: $351 = 27 \cdot 13$... En realidad, $17199 = 49 \cdot 351 = 49 \cdot 351$. Otra forma: $17199 = 7^2 \cdot 351$. Además $351 = 27 \cdot 13 = 3^3 \cdot 13$. Hmm, déjame verificar mejor.

En realidad, $231 \cdot 49 = 11319$... espera. Verifiquemos con el triángulo rectángulo $ADB$: $AB = 20$, $AD = 7$, entonces $BD = \sqrt{400 - 49} = \sqrt{351}$.

Para $D$, tenemos $AD = 7$. Usando el teorema en el triángulo rectángulo:

$(x_D + 10)^2 + y_D^2 = 49$
$x_D^2 + y_D^2 = 100$

Restando la segunda de la primera:
$(x_D + 10)^2 - x_D^2 = 49 - 100 = -51$
$20x_D + 100 = -51$
$x_D = -\frac{151}{20}$

Entonces $y_D^2 = 100 - \left(\frac{151}{20}\right)^2 = 100 - \frac{22801}{400} = \frac{40000 - 22801}{400} = \frac{17199}{400}$.

Notemos que $17199 = 9 \cdot 1911 = 9 \cdot 3 \cdot 637 = 27 \cdot 637$... Mejor: $40000 - 22801 = 17199$. Y $17199 = 49 \cdot 351$ (ya que $49 \cdot 351 = 17199$). Y $351 = 27 \cdot 13$. Así que $y_D = \frac{7\sqrt{351}}{20}$.

**Paso 5: Encontrar E (intersección de BC y AD)**

$E$ es la intersección de las rectas $BC$ y $AD$.

Recta $BC$: pasa por $B=(10,0)$ y $C=(31/20, 13\sqrt{231}/20)$.

La pendiente de $BC$ es:
$$m_{BC} = \frac{13\sqrt{231}/20 - 0}{31/20 - 10} = \frac{13\sqrt{231}/20}{(31-200)/20} = \frac{13\sqrt{231}/20}{-169/20} = -\frac{13\sqrt{231}}{169} = -\frac{\sqrt{231}}{13}$$

Recta $AD$: pasa por $A=(-10,0)$ y $D=(-151/20, 7\sqrt{351}/20)$.

La pendiente de $AD$ es:
$$m_{AD} = \frac{7\sqrt{351}/20 - 0}{-151/20 + 10} = \frac{7\sqrt{351}/20}{(-151+200)/20} = \frac{7\sqrt{351}/20}{49/20} = \frac{7\sqrt{351}}{49} = \frac{\sqrt{351}}{7}$$

**Ecuación de $BC$:**
$$y = -\frac{\sqrt{231}}{13}(x - 10)$$

**Ecuación de $AD$:**
$$y = \frac{\sqrt{351}}{7}(x + 10)$$

Igualamos para encontrar $E$:
$$-\frac{\sqrt{231}}{13}(x - 10) = \frac{\sqrt{351}}{7}(x + 10)$$

Multiplicamos por $91 = 13 \cdot 7$:
$$-7\sqrt{231}(x - 10) = 13\sqrt{351}(x + 10)$$
$$-7\sqrt{231}x + 70\sqrt{231} = 13\sqrt{351}x + 130\sqrt{351}$$
$$70\sqrt{231} - 130\sqrt{351} = (13\sqrt{351} + 7\sqrt{231})x$$
$$x_E = \frac{70\sqrt{231} - 130\sqrt{351}}{13\sqrt{351} + 7\sqrt{231}}$$

**Paso 6: Encontrar el excírculo E-excircle de ECD y su centro L**

El $E$-excircle de $\triangle ECD$ es el excírculo opuesto al vértice $E$ (es decir, tangente al lado $CD$ y a las extensiones de $EC$ y $ED$).

El centro de un excírculo queda en la intersección de la bisectriz del ángulo interno en $E$ y las bisectrices de los ángulos externos en $C$ y $D$.

**Key insight:** Los puntos $A$, $B$, $C$, $D$ están en la circunferencia $\omega$. Las rectas $BC$ y $AD$ se intersectan en $E$, que está fuera de la circunferencia. El ángulo entre $EB$ y $EA$ está determinado por la geometría.

Como $E$, $B$, $C$ son colineales y $E$, $A$, $D$ son colineales, el punto $E$ es la intersección de las secantes $EBC$ y $EAD$ a la circunferencia $\omega$.

**Paso 7: Observación clave sobre el centro L del E-excircle**

El $E$-excircle de $\triangle ECD$ está relacionado con la geometría de la circunferencia $\omega$. Específicamente, como $ABCD$ es cíclico con $AB$ como diámetro, hay una relación importante.

Notemos que el centro $L$ del $E$-excircle de $\triangle ECD$ está en la bisectriz del ángulo $\angle CED$. Dado que $BC$ y $AD$ se cruzan en $E$ y $AB$ es una cuerda de la circunferencia (el diámetro), el punto $O$ está en la bisectriz perpendicular de $AB$.

**Paso 8: Usar la fórmula para el incentro/excentro**

Para $\triangle ECD$, el $E$-excentro $L$ se puede calcular como:

$$L = \frac{|CD| \cdot E - |ED| \cdot C - |EC| \cdot D}{|CD| - |ED| - |EC|}$$

(baricentro ponderado con signos para excentro opuesto a $E$).

Sin embargo, hay una manera más elegante. Notemos que como $A$, $B$, $C$, $D$ son concíclicos y $AB$ es diámetro, tenemos simetrías.

**Paso 9: Perspectiva geométrica clave**

Como $\angle ACB = 90°$ y $\angle ADB = 90°$, las rectas $AC \perp BC$ y $AD \perp DB$. 

Pero $BC$ y $AD$ se intersectan en $E$. Notemos que si consideramos el triángulo $EAB$, los puntos $C$ y $D$ están sobre $EB$ y $EA$ respectivamente.

En realidad, reconsideremos. $C$ está sobre la semirrecta desde $E$ a través de $B$. $D$ está sobre la semirrecta desde $E$ a través de $A$. El orden depende de la configuración.

Dado que $BC = 13$ y $AD = 7$, y ambos $C$, $D$ están en la semicircunferencia superior, necesitamos determinar la posición de $E$ respecto a $A$, $B$, $C$, $D$.

Con $B=(10,0)$ y $C=(1.55, \approx 9.88)$, la recta $BC$ tiene pendiente negativa. Con $A=(-10,0)$ y $D=(-7.55, \approx 9.37)$, la recta $AD$ tiene pendiente positiva.

Las rectas se intersectan en $E$. Dado que la pendiente de $AD$ es positiva y la de $BC$ es negativa, se cruzan en algún punto. Evaluemos: para $x$ cerca de $-10$, AD está cerca de 0, BC está en $y \approx -\frac{\sqrt{231}}{13}(-10-10) = \frac{20\sqrt{231}}{13} \approx 23.4$. Entonces $E$ puede estar en la parte superior donde se cruzan.

**Paso 10: Cálculo refinado de E**

Simplifiquemos $x_E$ notando que $\sqrt{351} = \sqrt{9 \cdot 39} = 3\sqrt{39}$ y $\sqrt{231}$ no se simplifica más.

$x_E = \frac{70\sqrt{231} - 130 \cdot 3\sqrt{39}}{39\sqrt{39} + 7\sqrt{231}} = \frac{70\sqrt{231} - 390\sqrt{39}}{39\sqrt{39} + 7\sqrt{231}}$

Hmm, esto no se ve elegante. Quizá haya un enfoque más geométrico.

**Paso 11: Enfoque mediante homotecia y el punto medio**

Reconsideremos. Los puntos $A$, $B$, $C$, $D$ están en la circunferencia $\omega$ con centro $O$. 

El ángulo $\angle ACB = 90°$ implica que $AC \perp BC$. De manera similar $AD \perp DB$.

La recta $BC$ es perpendicular a $AC$ en $C$. La recta $AD$ es perpendicular a $DB$ en $D$.

Pero notemos: el ángulo en $E$ entre $BC$ (o $EC$) y $AD$ (o $ED$) es el mismo que el ángulo entre $AC$ y $DB$ (ya que $BC \perp AC$ y $AD \perp DB$).

Por el teorema del ángulo inscrito: $\angle ACB = 90°$, $\angle ADB = 90°$. 

**Paso 12: Relación con el excírculo**

El $E$-excircle de $\triangle ECD$ tiene centro en la intersección de la bisectriz interna de $\angle CED$ con las bisectrices externas en $C$ y $D$.

Como $A$, $B$, $C$, $D$ están en $\omega$, hay una relación: El centro $L$ del $E$-excircle de $\triangle ECD$ está en la recta $EO$ (la bisectriz del ángulo $\angle CED$ es la recta que pasa por $E$ y el punto medio del arco $CD$... hmm, en realidad hay varias rectas).

**Paso 13: Teorema clave sobre excentro y circunferencia**

Recordemos: Si $A$, $B$, $C$, $D$ son concíclicos y $E = AD \cap BC$, entonces el excentro del triángulo $ECD$ opuesto a $E$ (el $E$-excentro) está en la recta que pasa por $O$ y $E$, específicamente $O$, $E$, y $L$ pueden tener una relación.

De hecho, hay un teorema que dice que si $ABCD$ es cíclico y $E$ es la intersección de $BC$ y $AD$, entonces el incentro del triángulo $ECD$ y el $E$-excentro forman un arreglo armónico.

Más específicamente: el $E$-excentro de $\triangle ECD$ está en la perpendicular a $AB$ que pasa por... veamos.

**Paso 14: Usar potencia de un punto**

Como $E$ es la intersección de las secantes $EBC$ y $EAD$:
$$EB \cdot EC = EA \cdot ED = \text{Pot}(E)$$

También, $\text{Pot}(E) = EO^2 - R^2 = EO^2 - 100$.

**Paso 15: Determinar posiciones relativas**

Calculemos dónde cae $E$. Evaluemos las rectas en $x=0$:

$BC$: $y = -\frac{\sqrt{231}}{13}(0-10) = \frac{10\sqrt{231}}{13} \approx 11.69$

$AD$: $y = \frac{\sqrt{351}}{7}(0+10) = \frac{10\sqrt{351}}{7} \approx 26.77$

$AD$ está por encima de $BC$ en $x=0$. En $x=-10$: $BC$ vale $\approx 23.4$, $AD$ vale $0$. En $x=10$: $BC$ vale $0$, $AD$ vale $\approx 53.5$.

Entonces las rectas se cruzan donde $AD$ pasa de estar debajo de $BC$ (cerca de $x=-10$, AD ≈ 0 < BC ≈ 23.4) a estar por encima (en $x=10$, AD ≈ 53.5 > BC = 0). Se cruzan en algún $x$ negativo, cerca de -5 quizás.

Esto significa que $E$ está a la izquierda de $A$ (si $x_E < -10$) o entre $-10$ y $0$.

Calculemos $x_E$ más precisamente:
$$x_E = \frac{70\sqrt{231} - 130\sqrt{351}}{13\sqrt{351} + 7\sqrt{231}}$$

Sustituyamos valores aproximados: $\sqrt{231} \approx 15.1987$, $\sqrt{351} \approx 18.735$.

Numerador: $70(15.1987) - 130(18.735) = 1063.91 - 2435.55 = -1371.64$

Denominador: $13(18.735) + 7(15.1987) = 243.555 + 106.391 = 349.946$

$x_E \approx -1371.64 / 349.946 \approx -3.92$

Entonces $E \approx (-3.92, y_E)$ donde $y_E$ se puede calcular.

$y_E = \frac{\sqrt{351}}{7}(-3.92 + 10) = \frac{18.735}{7}(6.08) \approx 2.676 \cdot 6.08 \approx 16.27$

Así que $E$ está entre $A$ y $B$ (en $x$), por encima de $AB$. Específicamente, $E$ está sobre la semicircunferencia superior.

Esto quiere decir que en la recta $AD$: el orden es $A$, $D$, $E$ (ya que $D$ tiene $x=-7.55$ y $E$ tiene $x=-3.92$, y ambos están en la misma recta, con $D$ más cerca de $A$). En la recta $BC$: el orden es $B$, $C$, $E$ (ya que $C$ tiene $x=1.55$ y $E$ tiene $x=-3.92$, con $B$ en $x=10$).

Así que $C$ y $D$ están entre $A$/$B$ y $E$ respectivamente.

**Paso 16: Calcular distancias en el triángulo ECD**

$EC = EB - BC$ donde $EB$ es la distancia de $E$ a $B$. Similarmente $ED = EA - AD$.

$CD$: podemos usar geometría o coordenadas.

**Paso 17: El excentro L**

Para $\triangle ECD$ con vértice $E$ en la parte superior, el $E$-excentro está en la bisectriz del ángulo $\angle CED$ (la bisectriz interna), del lado opuesto a $E$.

La bisectriz del ángulo entre las rectas $EC$ (que es la recta $BC$) y $ED$ (que es la recta $AD$) es una recta que pasa por $E$. 

Notemos que la bisectriz de $\angle CED$ es perpendicular a la bisectriz del ángulo suplementario. Dado que $AB$ está entre los rayos $EC$ y $ED$ (en el sentido de que el ángulo desde $EC$ hasta $AB$ es pequeño y desde $AB$ hasta $ED$ es pequeño... en realidad $E$ está por encima de $AB$ y tanto $C$ como $D$ están por encima).

En realidad, el ángulo $\angle CED$ es el ángulo entre las rectas $EC$ y $ED$, que son las rectas $BC$ y $AD$ prolongadas. Como $A$ y $B$ están en $\omega$ y $C$, $D$ en el mismo arco, el ángulo $\angle CED$ es agudo.

**Paso 18: Relación armónica y el teorema de los excentros**

Hay un hermoso teorema: si $ABCD$ es cíclico y $E = AD \cap BC$, entonces $O$ (centro de la circunferencia) está en el $E$-excentro... más precisamente, el $E$-excentro de $\triangle ECD$ está en la perpendicular a $AB$ que pasa por $E$... o en algún lugar específico.

Déjame pensar geométricamente. El $E$-excentro $L$ está en la bisectriz del ángulo externo en $C$ y $D$ y en la bisectriz interna de $\angle E$.

Como $C$ está en la circunferencia y $AC \perp BC$ (o $EC$), la perpendicular a $EC$ en $C$ es $AC$. Como $C$ está entre $B$ y $E$, la semirrecta $CE$ apunta hacia $E$ y la perpendicular en $C$ apunta hacia $A$ (en una dirección).

De hecho, $AC$ es perpendicular a $BC$. Como $BC$ es la misma recta que $EC$, tenemos $AC \perp EC$. Por lo tanto, en el triángulo $ECD$, la recta $AC$ es perpendicular a $EC$ en $C$ (es la altura desde $C$ o una perpendicular al lado $EC$).

De manera similar, $DB \perp ED$ (ya que $DB \perp AD$ y $AD = ED$ como recta).

**Paso 19: Reconocer la geometría del excentro**

El centro del $E$-excircle de $\triangle ECD$ es el punto donde se intersectan:
- La bisectriz interna del ángulo $\angle CED$
- Las bisectrices de los ángulos externos en $C$ y $D$.

Como $AC \perp EC$ y $DB \perp ED$, y los puntos $A$, $B$ están sobre $\omega$ (la circunferencia con diámetro $AB$), hay una relación muy especial.

El ángulo $\angle CED$ tiene medida igual a $180° - \angle CBD$ (por propiedades de ángulos en una circunferencia). Específicamente, en el cuadrilátero cíclico $ABCD$, $\angle BCD + \angle BAD = 180°$. 

Hmm, déjame tomar otro enfoque.

**Paso 20: Enfoque coordinado con el excentro**

Para el triángulo $\triangle ECD$, el $E$-excentro $L$ tiene coordenadas baricéntricas:

$$L = \frac{CD \cdot E - ED \cdot C - EC \cdot D}{CD - ED - EC}$$

(donde $CD$, $ED$, $EC$ son las longitudes de los lados).

Calculemos las longitudes.

Primero, $EC$: como $B$ está entre $E$ y $C$ (verifiquemos: $E$ está en $x \approx -3.92$, $C$ en $x = 1.55$, $B$ en $x = 10$. Entonces el orden en la recta es $E$, $C$, $B$.). Entonces $EC = EB - BC = EB - 13$.

$EB$ es la distancia de $E$ a $B$. Usando coordenadas: $E \approx (-3.92, 16.27)$, $B = (10, 0)$, $EB \approx \sqrt{(13.92)^2 + 16.27^2} \approx \sqrt{193.8 + 264.7} \approx \sqrt{458.5} \approx 21.4$. Entonces $EC \approx 21.4 - 13 = 8.4$.

$ED$: $A=(-10,0)$, $E \approx (-3.92, 16.27)$, $D \approx (-7.55, 9.37)$. $EA \approx \sqrt{(6.08)^2 + 16.27^2} \approx \sqrt{36.97 + 264.7} \approx \sqrt{301.7} \approx 17.37$. Entonces $ED = EA - AD = 17.37 - 7 \approx 10.37$.

$CD$: distancia entre $C \approx (1.55, 9.88)$ y $D \approx (-7.55, 9.37)$: $CD \approx \sqrt{(9.1)^2 + 0.51^2} \approx \sqrt{82.8 + 0.26} \approx \sqrt{83.1} \approx 9.12$.

**Paso 21: Cálculo del excentro**

Usando la fórmula baricéntrica con $E$, $C$, $D$:

$CD \approx 9.12$, $ED \approx 10.37$, $EC \approx 8.4$.

$$L \approx \frac{9.12 E - 10.37 C - 8.4 D}{9.12 - 10.37 - 8.4} = \frac{9.12E - 10.37C - 8.4D}{-9.65}$$

Para $x$:
$x_L \approx \frac{9.12(-3.92) - 10.37(1.55) - 8.4(-7.55)}{-9.65} = \frac{-35.75 - 16.07 + 63.42}{-9.65} = \frac{11.60}{-9.65} \approx -1.20$

Para $y$:
$y_L \approx \frac{9.12(16.27) - 10.37(9.88) - 8.4(9.37)}{-9.65} = \frac{148.38 - 102.45 - 78.71}{-9.65} = \frac{-32.78}{-9.65} \approx 3.40$

Entonces $L \approx (-1.20, 3.40)$.

$OL = \sqrt{x_L^2 + y_L^2} \approx \sqrt{1.44 + 11.56} \approx \sqrt{13} \approx 3.61$.

Interesante, $OL \approx 3.6$, que es cercano a $\sqrt{13} \approx 3.606$. Esto sugiere que $OL = \sqrt{13}$.

**Paso 22: Verificación y prueba geométrica elegante**

Reconsideremos la geometría. Notamos que $y_L \approx 3.40$ y $x_L \approx -1.20$, lo que da $OL^2 \approx 13$.

Déjame verificar si hay una manera más elegante. 

Hay un teorema hermoso: si $ABCD$ es cíclico con diámetro $AB$, $E = AD \cap BC$, y $L$ es el $E$-excentro de $\triangle ECD$, entonces $OL$ tiene una relación específica con las longitudes dadas.

Notemos que $BC = 13 = \sqrt{169}$ y $AD = 7 = \sqrt{49}$. 

La relación $OL^2 = R^2 - AD \cdot BC$ ... veamos: $R^2 = 100$, $AD \cdot BC = 7 \cdot 13 = 91$, $100 - 91 = 9$, no da 13.

$OL^2 = (BC - AD)^2 = (13-7)^2 = 36$, no da 13.

$OL = \sqrt{BC \cdot AD - R^2} = \sqrt{91 - 100}$ no da real.

$OL^2 = BC^2 + AD^2 - R^2 = 169 + 49 - 100 = 118$, no da 13.

Hmm. Veamos otra relación. $OL^2 = R^2 - \frac{BC^2 + AD^2}{2} = 100 - \frac{169+49}{2} = 100 - 109 = -9$, no.

$OL^2 = R^2 + AD \cdot BC - (AB/2)^2... $ veamos: $100 + 91 - 178 = 13$. Espera: $100 + 91 - 178 = 13$. Y $178 = 169 + 9 = BC^2 + 3^2$... no muy natural.

En realidad, hay una fórmula conocida. Para un cuadrilátero cíclico con $AB$ como diámetro:

$$OL^2 = R^2 - \frac{(BC - AD)^2}{4} - \ldots$$

Déjame verificar con valores exactos.

**Paso 23: Cálculo exacto mediante coordenadas**

Usando datos exactos:
- $C = (31/20, 13\sqrt{231}/20)$
- $D = (-151/20, 7\sqrt{351}/20)$

Para $E$, la intersección de $BC$ y $AD$.

Observemos una relación importante. Notemos que $\sqrt{351} = \sqrt{9 \cdot 39} = 3\sqrt{39}$ y no tiene una relación obvia con $\sqrt{231}$.

Sin embargo, la configuración con $BC=13$ y $AD=7$ sugiere que quizá las medidas $13$ y $7$ son tales que dan una respuesta elegante.

**Paso 24: Relación clave con el excentro y el punto O**

Hay un teorema: el $E$-excentro de $\triangle ECD$ (donde $E$ es la intersección de los lados prolongados) está en la perpendicular a $AB$ que pasa por... no exactamente.

Déjame pensar en la bisectriz angular. La bisectriz interna de $\angle CED$ pasa por $E$. Como $EC$ es la recta $BC$ y $ED$ es la recta $AD$, la bisectriz de $\angle CED$ es una recta específica.

Por otro lado, $O$ está en la intersección de las mediatrices de $AB$, $BC$, etc. 

**Paso 25: Usar la proyección estereográfica o inversión**

Otra idea: aplicar una transformación que simplifique. Como $\omega$ tiene diámetro $AB$, y $C$, $D$ están en $\omega$, la recta $BC$ es perpendicular a $AC$ y la recta $AD$ es perpendicular a $BD$.

Esto sugiere que el cuadrilátero $ACDE$ o $BCDE$ tiene ángulos rectos. En particular, $AC \perp CE$ (ya que $CE$ es la recta $CB$) y $BD \perp DE$ (ya que $DE$ es la recta $DA$).

Así que en $\triangle ECD$:
- La perpendicular a $EC$ en $C$ es la recta $AC$ (que pasa por $A$).
- La perpendicular a $ED$ en $D$ es la recta $BD$ (que pasa por $B$).

**Paso 26: Identificar el excentro mediante bisectrices**

El $E$-excentro $L$ está sobre:
- La bisectriz interna del ángulo $\angle CED$.
- Las bisectrices de los ángulos externos en $C$ y $D$.

La bisectriz del ángulo externo en $C$ es perpendicular a la bisectriz del ángulo interno en $C$.

Consideremos la bisectriz del ángulo externo en $C$. El ángulo en $C$ del triángulo $ECD$ tiene como lados $CE$ (hacia $E$) y $CD$. El ángulo externo correspondiente tiene lados $CE$ y la prolongación de $CD$ (más allá de $C$).

**Paso 27: Relación con la circunferencia**

Como $A$, $B$, $C$, $D$ están en $\omega$, hay ángulos inscritos que nos ayudan. 

$\angle CED$ es el ángulo entre $EC$ (recta $CB$) y $ED$ (recta $DA$). Por el teorema del ángulo exterior de un cuadrilátero cíclico: $\angle CED = \angle CBD + \angle DAC$ (o similar).

En general, $\angle CED = |\angle CBA - \angle DAB|$ (usando que son ángulos inscritos).

Específicamente, $\angle CED = 180° - \angle BCD - \angle CDA$... mejor usemos el teorema del ángulo entre secantes desde un punto exterior.

Como $E$ está dentro de la circunferencia (en realidad, $E \approx (-3.92, 16.27)$ tiene $x^2 + y^2 \approx 15.37 + 264.7 \approx 280 > 100$, así que $E$ está FUERA de la circunferencia), el ángulo entre las secantes $ECB$ y $EDA$ es:

$$\angle CED = \frac{1}{2}(\text{arc } CD - \text{arc } BA)$$

(donde los arcos son los interceptados). Como $AB$ es diámetro, arc $BA = 180°$.

**Paso 28: Avance con el excentro L**

Dado que $AC \perp EC$ y $BD \perp DE$, y $L$ es el $E$-excentro, el punto donde la bisectriz externa en $C$ intersecta la bisectriz interna en $E$ es $L$.

Para el triángulo $\triangle ECD$, con $AC \perp EC$, la recta $AC$ es una altura (perpendicular a un lado). 

Si consideramos el pie de la perpendicular desde $D$ a $EC$, o algo similar...

**Paso 29: Resultado final con verificación numérica**

Usemos el cálculo numérico más preciso para confirmar $OL \approx \sqrt{13} \approx 3.606$.

Con coordenadas exactas y el cálculo simbólico, podemos derivar $L$ y $OL$.

Pero antes, notemos un patrón. La respuesta $OL = \sqrt{13}$ surge de $13 = BC$, lo cual es sospechoso.

Alternativamente, quizá $OL = \sqrt{AD \cdot BC - R^2 + 2R^2 - ...}$

Veamos: ¿qué pasa si $BC = 13$ y $AD = 7$? 

$R = 10$. Notemos que $13 = 10 + 3$ y $7 = 10 - 3$. Es decir, $BC = R + 3$ y $AD = R - 3$.

El número 3 aparece. Y $\sqrt{13}$... ¿acaso $OL^2 = 10^2 - 7^2 = 51$? No. $OL^2 = 13^2 - 10^2 = 69$? No. $OL^2 = 13^2 - 7^2 = 120$? No.

$OL^2 = 10^2 - 7 \cdot 13 = 100 - 91 = 9$, $OL = 3$. No era 3, era aproximadamente 3.6.

$OL^2 = 10^2 - 7 \cdot 13 + 7 + 13 = 100 - 91 + 20 = 29$, $OL = \sqrt{29}$. No.

$OL^2 = 13 \cdot 7 - 10^2 + 10 = 91 - 100 + 10 = 1$. No.

Hmm, quizá mi cálculo numérico es impreciso. Déjame recalcular con más cuidado.

**Paso 30: Recalcular con precisión**

Los valores exactos:

$\sqrt{231} = 15.198684...$
$\sqrt{351} = 18.734994...$

$C = (31/20, \frac{13\sqrt{231}}{20}) = (1.55, \frac{13 \cdot 15.198684}{20}) = (1.55, \frac{197.5829}{20}) = (1.55, 9.879145)$

$D = (-151/20, \frac{7\sqrt{351}}{20}) = (-7.55, \frac{7 \cdot 18.734994}{20}) = (-7.55, \frac{131.145}{20}) = (-7.55, 6.55725)$

Espera, antes calculé $y_D \approx 9.37$, pero esto da 6.557. Déjame revisar.

$y_D = \sqrt{100 - (151/20)^2} = \sqrt{100 - 22801/400} = \sqrt{(40000 - 22801)/400} = \sqrt{17199/400} = \sqrt{17199}/20$

$17199$ tiene raíz $\sqrt{17199} = 131.1449...$. Entonces $y_D = 131.1449/20 = 6.5572$.

¡Antes cometí un error! Calculé $\sqrt{17199}$ como $7\sqrt{351}$, pero esto es incorrecto. $7\sqrt{351} = 7 \cdot 18.735 = 131.145$, y $131.145^2 = 17199$, lo cual es correcto. Pero cometí el error al dividir: $7\sqrt{351}/20 = 131.145/20 = 6.557$, no $9.37$. Antes escribí incorrectamente $y_D \approx 9.37$.

Revisemos la distancia $AD$: $A = (-10,0)$, $D = (-7.55, 6.557)$. $AD = \sqrt{(2.45)^2 + 6.557^2} = \sqrt{6.0025 + 42.997} = \sqrt{49.0} = 7$. Correcto.

**Revisemos $C$:** $C = (1.55, 9.879)$. $BC = \sqrt{(1.55-10)^2 + 9.879^2} = \sqrt{(-8.45)^2 + 97.597} = \sqrt{71.4025 + 97.597} = \sqrt{169.0} = 13$. Correcto.

**Revisemos $D$:** Con $y_D = 6.557$, verifiquemos $BD$: $B=(10,0)$, $D=(-7.55, 6.557)$. $BD = \sqrt{(-17.55)^2 + 6.557^2} = \sqrt{308.0025 + 42.997} = \sqrt{351}$. Correcto, ya que $\sqrt{400-49} = \sqrt{351}$.

Así que $D$ tiene $y \approx 6.56$, no 9.37. Mi cálculo anterior de la línea $AD$ era incorrecto.

**Paso 31: Redeterminar E con coordenadas correctas**

Recta $AD$: pendiente $m_{AD} = \frac{6.557 - 0}{-7.55 - (-10)} = \frac{6.557}{2.45} \approx 2.676$. (Antes tenía $\sqrt{351}/7 \approx 18.735/7 \approx 2.676$, correcto, pero la altura de $D$ era menor.)

Entonces $AD$: $y = 2.676(x + 10)$.

Recta $BC$: pendiente $m_{BC} = \frac{9.879 - 0}{1.55 - 10} = \frac{9.879}{-8.45} \approx -1.169$. (Antes: $-\sqrt{231}/13 \approx -15.199/13 \approx -1.169$, correcto.)

Igualamos:
$2.676(x+10) = -1.169(x-10)$
$2.676x + 26.76 = -1.169x + 11.69$
$3.845x = -15.07$
$x_E \approx -3.92$ (mismo valor que antes, por suerte).

$y_E = 2.676(-3.92 + 10) = 2.676 \cdot 6.08 \approx 16.27$

Bien, el cálculo de $E$ era correcto.

**Paso 32: Recalcular CD**

$C = (1.55, 9.879)$, $D = (-7.55, 6.557)$.

$CD = \sqrt{(1.55 + 7.55)^2 + (9.879 - 6.557)^2} = \sqrt{9.1^2 + 3.322^2} = \sqrt{82.81 + 11.036} = \sqrt{93.846} \approx 9.687$.

Antes tenía $CD \approx 9.12$ (error por el valor incorrecto de $y_D$).

**Paso 33: Recalcular EC y ED**

$EC$: distancia de $E$ a $C$. $E \approx (-3.92, 16.27)$, $C \approx (1.55, 9.879)$.
$EC = \sqrt{(5.47)^2 + (-6.39)^2} = \sqrt{29.92 + 40.83} = \sqrt{70.75} \approx 8.41$.

$ED$: distancia de $E$ a $D$. $E \approx (-3.92, 16.27)$, $D \approx (-7.55, 6.557)$.
$ED = \sqrt{(-3.63)^2 + (-9.71)^2} = \sqrt{13.18 + 94.28} = \sqrt{107.46} \approx 10.37$.

**Paso 34: Recalcular el excentro L**

$CD \approx 9.69$, $ED \approx 10.37$, $EC \approx 8.41$.

$$L \approx \frac{9.69 E - 10.37 C - 8.41 D}{9.69 - 10.37 - 8.41} = \frac{9.69E - 10.37C - 8.41D}{-9.09}$$

$x_L \approx \frac{9.69(-3.92) - 10.37(1.55) - 8.41(-7.55)}{-9.09} = \frac{-37.98 - 16.07 + 63.50}{-9.09} = \frac{9.45}{-9.09} \approx -1.04$

$y_L \approx \frac{9.69(16.27) - 10.37(9.879) - 8.41(6.557)}{-9.09} = \frac{157.66 - 102.45 - 55.14}{-9.09} = \frac{0.07}{-9.09} \approx -0.008$

$OL = \sqrt{x_L^2 + y_L^2} \approx \sqrt{1.08 + 0.000064} \approx \sqrt{1.08} \approx 1.04$.

Interesante, ahora $OL \approx 1.04$, muy cercano a $1$, y $x_L \approx -1.04$, $y_L \approx 0$. Esto sugiere $L \approx (-1, 0)$ y $OL \approx 1$.

**Paso 35: Interpretación geométrica**

Con los cálculos corregidos, parece que $L$ está muy cerca del punto $(-1, 0)$ en el eje $x$. Esto sugiere que $L$ cae sobre $\overline{AB}$ (o su prolongación), cerca de $x=-1$.

Dado que la respuesta debe ser un valor exacto elegante, probablemente $OL = 1$ o algún valor racional simple.

Pero notemos que los valores numéricos usados para $E$ son aproximados, lo que introduce error. El valor $x_L \approx -1.04$ cercano a $-1$ es sugerente.

**Paso 36: Cálculo exacto**

Para obtener resultados exactos, necesitamos calcular $E$, luego $CD$, $EC$, $ED$ con fórmulas exactas, y luego el excentro.

Sin embargo, hay una manera más elegante. Notemos que el $E$-excentro $L$ está en la bisectriz del ángulo $\angle CED$ y en las bisectrices externas en $C$ y $D$.

**Paso 37: Teorema sobre el excentro y el diámetro**

Hay un resultado: si $ABCD$ es un cuadrilátero cíclico con $AB$ como diámetro, y $E = AD \cap BC$, entonces el $E$-excentro de $\triangle ECD$ está en la recta $AB$ (el diámetro), específicamente en la perpendicular a... 

Esto tiene sentido con el resultado numérico $y_L \approx 0$.

Veamos por qué. La bisectriz del ángulo externo en $C$ (del triángulo $ECD$) debe ser perpendicular a $EC$ si $EC = CD$... no, la bisectriz externa no es perpendicular.

Recordemos la propiedad: el excentro está en la intersección de la bisectriz interna de un ángulo y las externas de los otros dos. 

Para $\triangle ECD$, el $E$-excentro está en:
- Bisectriz interna de $\angle CED$ (en $E$).
- Bisectriz externa de $\angle ECD$ (en $C$).
- Bisectriz externa de $\angle EDC$ (en $D$).

Consideremos la bisectriz externa en $C$. Sabemos que $AC \perp EC$ (ya que $AC$ es perpendicular a la tangente... en realidad $AC \perp BC = EC$). 

La bisectriz del ángulo externo en $C$ biseca el ángulo entre $CE$ y la prolongación de $CD$ (o entre $CE$ y $CD$ en el ángulo externo).

**Paso 38: Relación con la circunferencia**

Como $A$, $B$, $C$, $D$ están en $\omega$, y $AB$ es diámetro, tenemos que $\angle ACB = 90°$ y $\angle ADB = 90°$.

La recta $AC$ es perpendicular a $EC$ en $C$. Esto significa que $AC$ es una altura del triángulo $ECD$ (perpendicular al lado $EC$).

De manera similar, $BD$ es perpendicular a $ED$ en $D$, así que $BD$ es una altura (perpendicular al lado $ED$).

**Paso 39: El excentro y las alturas**

El $E$-excentro $L$ de $\triangle ECD$ tiene coordenadas baricéntricas dadas por $(-a:b:c)$ (donde $a=CD$, $b=ED$, $c=EC$), relativas a los vértices $E$, $C$, $D$.

Específicamente:
$$L = \frac{aE - bC - cD}{a - b - c}$$

donde $a = CD$, $b = ED$, $c = EC$.

**Paso 40: Calcular las longitudes exactamente**

Necesitamos $CD$ exacto. Usemos coordenadas exactas.

$C = (31/20, 13\sqrt{231}/20)$
$D = (-151/20, 7\sqrt{351}/20)$

$CD^2 = \left(\frac{31 + 151}{20}\right)^2 + \left(\frac{13\sqrt{231} - 7\sqrt{351}}{20}\right)^2 = \left(\frac{182}{20}\right)^2 + \left(\frac{13\sqrt{231} - 7\sqrt{351}}{20}\right)^2$

$\frac{182}{20} = 9.1$. Entonces $CD^2 = 9.1^2 + \left(\frac{13\sqrt{231} - 7\sqrt{351}}{20}\right)^2$.

$9.1^2 = 82.81 = \frac{8281}{100}$.

$(13\sqrt{231})^2 = 169 \cdot 231 = 39039$.
$(7\sqrt{351})^2 = 49 \cdot 351 = 17199$.
$2 \cdot 13 \cdot 7 \cdot \sqrt{231 \cdot 351} = 182\sqrt{231 \cdot 351}$.

$231 \cdot 351 = 81081$. $\sqrt{81081} = \sqrt{9 \cdot 9009} = 3\sqrt{9009}$. Notemos que $9009 = 9 \cdot 1001 = 9 \cdot 7 \cdot 11 \cdot 13$. Así que $\sqrt{81081} = 3 \cdot 3 \cdot \sqrt{1001} = 9\sqrt{1001}$... espera: $\sqrt{81081} = \sqrt{9 \cdot 9009} = 3\sqrt{9009} = 3 \cdot \sqrt{9 \cdot 1001} = 3 \cdot 3\sqrt{1001} = 9\sqrt{1001}$. Y $1001 = 7 \cdot 11 \cdot 13$.

$1001 = 7 \cdot 143 = 7 \cdot 11 \cdot 13$. Correcto.

Entonces $182\sqrt{81081} = 182 \cdot 9\sqrt{1001} = 1638\sqrt{1001}$.

$CD^2 = \frac{8281}{100} + \frac{39039 + 17199 - 1638\sqrt{1001}}{400} = \frac{33124 + 56238 - 1638\sqrt{1001}}{400} = \frac{89362 - 1638\sqrt{1001}}{400}$.

Hmm, esto se está complicando. Quizá $CD$ tenga una forma más simple.

**Paso 41: Otra verificación**

Déjame verificar si $CD$ es un número racional. $C=(1.55, 9.879)$, $D=(-7.55, 6.557)$. $CD \approx 9.687$. No parece racional.

**Paso 42: Reconocer la forma del excentro**

Dado que numéricamente $L \approx (-1, 0)$ con $OL \approx 1$, la respuesta exacta probablemente sea $OL = 1$.

Pero necesito verificar con más precisión si $x_L = -1$ exactamente o si es otro valor como $-\sqrt{13}/4$ o similar.

**Paso 43: Cálculo más preciso**

Usemos el enfoque de que $L$ está sobre $AB$ (el eje $x$). Si esto es cierto, entonces $y_L = 0$ y $L = (x_L, 0)$.

Para el $E$-excentro $L$, las distancias a los lados $EC$ (recta $BC$), $ED$ (recta $AD$), y $CD$ son todas iguales (con signos según excírculo). Si $L$ está sobre el eje $x$, la distancia de $L$ a las rectas $BC$ y $AD$ debe ser igual (en valor absoluto) al inradio o exradio.

Como $L$ es el $E$-excentro, $L$ está del lado opuesto a $E$ respecto a $CD$, o más precisamente, $L$ está en el lado de $CD$ que no contiene a $E$ (para el excírculo opuesto a $E$).

$E$ está en la parte superior ($y_E > 0$), así que el $E$-excentro puede estar en la parte inferior o en un lugar específico.

Dado que numéricamente $L$ está cerca de $(-1, 0)$ (sobre el eje $x$), esto sugiere que $L$ está exactamente sobre $AB$ o su prolongación.

**Paso 44: Demostrar que L está sobre AB**

Vamos a demostrar que el punto $L$ (el $E$-excentro) cae sobre la recta $AB$ si ciertas condiciones se cumplen.

El $E$-excentro $L$ es el centro del excírculo opuesto a $E$. Está en la bisectriz interna del ángulo $\angle CED$ y en las bisectrices de los ángulos externos en $C$ y $D$.

La bisectriz del ángulo externo en $C$ es la recta que biseca el ángulo formado por $CE$ y la prolongación de $CD$. 

Dado que $AC \perp CE$, y considerando la geometría de la circunferencia, es plausible que las bisectrices relevantes se intersecten sobre $AB$.

En realidad, hay un teorema conocido: en un triángulo, el excentro opuesto a un vértice está en la intersección de la bisectriz del ángulo interno en ese vértice y las bisectrices de los ángulos externos en los otros dos vértices. Si el triángulo está inscripto en una configuración como esta, el excentro puede caer sobre una recta particular.

**Paso 45: Usar la propiedad de que AB es diámetro**

Como $AB$ es diámetro de $\omega$, y $C$, $D$ están en $\omega$, los ángulos $\angle ACB = 90°$ y $\angle ADB = 90°$.

La recta $AC$ es perpendicular a $EC$ (ya que $EC$ es la misma recta que $CB$). Por lo tanto, en el triángulo $\triangle ECD$, la recta $AC$ es perpendicular al lado $EC$ en $C$. Esto significa que $AC$ es una altura del triángulo (perpendicular a un lado, pasando por un vértice... en realidad $AC$ pasa por $C$ y es perpendicular a $EC$).

De manera similar, $BD$ es perpendicular a $ED$ en $D$, así que $BD$ es una altura.

El punto donde se intersectan las alturas de un triángulo es el ortocentro. Las rectas $AC$ y $BD$ se intersectan en $H$ (el ortocentro de $\triangle ECD$). 

Dado que $AC$ y $BD$ son también rectas en la configuración, $H = AC \cap BD$.

El ortocentro de $\triangle ECD$ está relacionado con la configuración. Como $AC$ y $BD$ se intersectan en $H$, y $A$, $B$, $C$, $D$ están en $\omega$...

**Paso 46: Identificar el ortocentro**

$H = AC \cap BD$. En el cuadrilátero cíclico $ABCD$, las diagonales $AC$ y $BD$ se intersectan en $H$.

Para $\triangle ECD$, el ortocentro es $H$ (la intersección de las alturas $AC$ y $BD$).

**Paso 47: Relación entre ortocentro y excentro**

En un triángulo, el ortocentro y los excentros están relacionados mediante ciertas configuraciones. En particular, el $E$-excentro $L$ tiene una relación específica con el ortocentro.

Recordemos que en un triángulo, si $H$ es el ortocentro, entonces el excentro opuesto a un vértice está en la recta que pasa por $H$ y el vértice (o en una configuración específica).

En general, no hay una relación directa entre el ortocentro y los excentros en un triángulo arbitrario. Sin embargo, en este caso específico, la configuración cíclica impone condiciones.

**Paso 48: Usar la fórmula del excentro con coordenadas baricéntricas**

Podemos calcular el excentro $L$ usando coordenadas baricéntricas generalizadas:

$$L = \frac{aE - bC - cD}{a - b - c}$$

donde $a = |CD|$, $b = |ED|$, $c = |EC|$.

Para demostrar que $L$ está sobre el eje $x$ (recta $AB$), necesitamos mostrar que $y_L = 0$.

Esto requiere relaciones específicas entre las coordenadas.

**Paso 49: Cálculo del excentro usando exradios**

Otra manera: usar la fórmula del excentro como intersección de bisectrices.

La bisectriz del ángulo $\angle CED$ tiene la propiedad de que para cualquier punto $P$ sobre ella, la razón de distancias a los lados $EC$ y $ED$ es 1 (con signos). Específicamente, $P$ satisface que las distancias (con signo) a las rectas $EC$ y $ED$ son iguales.

Las rectas $EC$ y $ED$ son $BC$ y $AD$ respectivamente. La bisectriz de $\angle CED$ es una recta que pasa por $E$ y cuya pendiente es el promedio (en cierto sentido) de las pendientes de $BC$ y $AD$.

Para que $L$ esté sobre $AB$ (eje $x$), la bisectriz del ángulo $\angle CED$ debe intersectar el eje $x$ en $L$.

**Paso 50: Encontrar la intersección de la bisectriz con AB**

La bisectriz del ángulo entre las rectas $BC$ y $AD$ (en $E$) intersecta $AB$ en un punto. Este punto podría ser $L$ solo si también es equidistante de los tres lados (propiedad del excentro).

En realidad, si $L$ está sobre $AB$ y es el excentro, entonces $L$ debe ser equidistante (con signos) de los lados $EC$, $ED$, y $CD$.

Para que $L$ sobre $AB$ sea el excentro, la distancia (con signo) de $L$ a $EC$ y $ED$ debe ser igual (propiedad de la bisectriz), lo cual impone que $L$ esté sobre la bisectriz de $\angle CED$.

Además, la distancia de $L$ a $CD$ debe ser igual (con signo opuesto, para el excírculo) a la distancia a $EC$ y $ED$.

**Paso 51: Calcular las rectas y la intersección**

Recta $BC$: pasa por $B=(10,0)$ y $C=(31/20, 13\sqrt{231}/20)$.

Ecuación: $\frac{y - 0}{x - 10} = \frac{13\sqrt{231}/20 - 0}{31/20 - 10} = -\frac{\sqrt{231}}{13}$.

O sea, $y = -\frac{\sqrt{231}}{13}(x - 10) = \frac{\sqrt{231}}{13}(10 - x)$.

Recta $AD$: $y = \frac{\sqrt{351}}{7}(x + 10)$.

La bisectriz del ángulo $\angle CED$ es la recta de puntos equidistantes de $BC$ y $AD$. Usando distancias con signo, la condición es:

$$\frac{|y - \frac{\sqrt{231}}{13}(10-x)|}{\sqrt{1 + \frac{231}{169}}} = \frac{|y - \frac{\sqrt{351}}{7}(x+10)|}{\sqrt{1 + \frac{351}{49}}}$$

Esto se simplifica notando que $\sqrt{1 + 231/169} = \sqrt{400/169} = 20/13$ y $\sqrt{1 + 351/49} = \sqrt{400/49} = 20/7$.

Así que la condición de equidistancia es:

$$|y \cdot 13/20 - \sqrt{231}(10-x)/20| = |7y/20 - \sqrt{351}(x+10)/20|$$

Para la bisectriz interna de $\angle CED$, tomamos signos apropiados.

Esto se está complicando. Dado el tiempo, aceptemos el resultado numérico y busquemos la respuesta exacta.

**Paso 52: Verificación numérica más precisa del excentro**

Usemos una calculadora mental más precisa. Los valores:

$C = (1.55, 9.879145...)$
$D = (-7.55, 6.557249...)$

Recta $BC$: pendiente $m_1 = -15.198684/13 = -1.1691295...$
Recta $AD$: pendiente $m_2 = 18.734994/7 = 2.6764277...$

Intersección $E$:
$m_2(x+10) = m_1(x-10)$
$2.6764277x + 26.764277 = -1.1691295x + 11.691295$
$3.8455572x = -15.072982$
$x_E = -3.919698...$

$y_E = 2.6764277 \cdot (6.080302) = 16.274547...$

Distancias:

$EC = \sqrt{(1.55 - (-3.919698))^2 + (9.879145 - 16.274547)^2} = \sqrt{(5.469698)^2 + (-6.395402)^2} = \sqrt{29.9176 + 40.9012} = \sqrt{70.8188} = 8.414797...$

$ED = \sqrt{(-7.55 - (-3.919698))^2 + (6.557249 - 16.274547)^2} = \sqrt{(-3.630302)^2 + (-9.717298)^2} = \sqrt{13.1791 + 94.4259} = \sqrt{107.605} = 10.372310...$

$CD = \sqrt{(1.55 + 7.55)^2 + (9.879145 - 6.557249)^2} = \sqrt{(9.1)^2 + (3.321896)^2} = \sqrt{82.81 + 11.035} = \sqrt{93.845} = 9.687363...$

**Excentro L:**

$a = CD = 9.687363$, $b = ED = 10.372310$, $c = EC = 8.414797$.

Denominador: $a - b - c = 9.687363 - 10.372310 - 8.414797 = -9.099744$.

$x_L = \frac{a x_E - b x_C - c x_D}{denom}$
$= \frac{9.687363(-3.919698) - 10.372310(1.55) - 8.414797(-7.55)}{-9.099744}$
$= \frac{-37.971 + (-16.077) + 63.532}{-9.099744}$
$= \frac{9.484}{-9.099744}$
$= -1.042296...$

$y_L = \frac{a y_E - b y_C - c y_D}{denom}$
$= \frac{9.687363(16.274547) - 10.372310(9.879145) - 8.414797(6.557249)}{-9.099744}$
$= \frac{157.658 - 102.470 - 55.177}{-9.099744}$
$= \frac{0.011}{-9.099744}$
$= -0.00121...$

$y_L$ es muy cercano a 0 (el error es numérico). Entonces $L$ está sobre el eje $x$, y $x_L \approx -1.0423$.

**Paso 53: Determinar x_L exacto**

El valor $x_L \approx -1.0423$ no es obviamente un número racional simple. Verifiquemos si corresponde a $-25/24 = -1.04167$, $-101/97 \approx -1.0412$, etc. 

Notemos que $x_L^2 \approx 1.0864$, lo que da $OL = |x_L| \approx 1.043$.

¿Podría ser $x_L = -10/9 \approx -1.111$, $x_L = -13/12 \approx -1.083$? El valor $-1.0423$ no coincide con fracciones simples evidentes.

Hmm, pero la precisión de mi cálculo puede ser limitada. Hay error numérico en las aproximaciones. El valor real podría ser $x_L = -1$ exactamente, o tal vez un valor algebraico.

Déjame abordar el problema de manera completamente exacta usando un enfoque algebraico.

**Paso 54: Enfoque algebraico exacto**

Usemos variables simbólicas. Sabemos:
- $A = (-10, 0)$, $B = (10, 0)$.
- $C = (x_C, y_C)$ con $x_C^2 + y_C^2 = 100$ y $(x_C - 10)^2 + y_C^2 = 169$, lo que da $x_C = 31/20$, $y_C = 13\sqrt{231}/20$.
- $D = (x_D, y_D)$ con $x_D^2 + y_D^2 = 100$ y $(x_D + 10)^2 + y_D^2 = 49$, lo que da $x_D = -151/20$, $y_D = 7\sqrt{351}/20$.

Recta $BC$: pendiente $m_1 = \frac{y_C - 0}{x_C - 10} = \frac{13\sqrt{231}/20}{31/20 - 200/20} = \frac{13\sqrt{231}/20}{-169/20} = -\frac{13\sqrt{231}}{169} = -\frac{\sqrt{231}}{13}$.

Espera, verifiquemos: $\frac{13}{169} = \frac{1}{13}$, así que $m_1 = -\frac{\sqrt{231}}{13}$. Correcto.

Recta $AD$: pendiente $m_2 = \frac{y_D - 0}{x_D - (-10)} = \frac{7\sqrt{351}/20}{-151/20 + 200/20} = \frac{7\sqrt{351}/20}{49/20} = \frac{7\sqrt{351}}{49} = \frac{\sqrt{351}}{7}$. Correcto.

Ahora, el $E$-excentro $L$ del triángulo $\triangle ECD$ está en la intersección de:
1) La bisectriz del ángulo $\angle CED$
2) La bisectriz del ángulo externo en $C$

En lugar de calcular $E$ y luego el excentro, usemos las propiedades de la bisectriz.

**Paso 55: Bisectriz del ángulo externo en C**

En $\triangle ECD$, el ángulo en $C$ es $\angle ECD$. Los lados del ángulo son $CE$ (hacia $E$) y $CD$. La bisectriz externa de este ángulo es la recta que biseca el ángulo suplementario a $\angle ECD$.

La bisectriz externa en $C$ es perpendicular a la bisectriz interna en $C$.

Para el $E$-excentro $L$, está en la bisectriz INTERNA de $\angle E$ y en las EXTERNAS de $\angle C$ y $\angle D$.

**Paso 56: Identificar la bisectriz externa en C**

Dado que $AC \perp CE$ (pues $AC \perp BC = CE$), consideremos si $AC$ es la bisectriz externa en $C$ de alguna manera.

La bisectriz del ángulo externo en $C$ forma un ángulo con $CE$ igual a la mitad del ángulo externo. Si el ángulo externo en $C$ vale $\pi - \angle ECD$, entonces la bisectriz externa forma un ángulo $\frac{\pi - \angle ECD}{2}$ con $CE$.

Por otro lado, $AC$ es perpendicular a $CE$, formando un ángulo $\pi/2$ con $CE$. Para que $AC$ sea la bisectriz externa, necesitaríamos $\frac{\pi - \angle ECD}{2} = \pi/2$, o sea $\angle ECD = -\pi/2$, lo cual no tiene sentido.

Así que $AC$ no es la bisectriz externa en general.

**Paso 57: Uso de la fórmula del excentro en términos de los lados**

Dado que el cálculo es complejo, y el resultado numérico sugiere $L \approx (-1.04, 0)$, intentemos determinar si el valor exacto es $OL = 1$ o algún otro valor.

Déjame ser más cuidadoso con la aritmética del excentro, usando más precisión.

Con alta precisión (usando valores exactos):

$\sqrt{231} = 15.198684153570664...$
$\sqrt{351} = 18.734993995195233...$

$C_x = 1.55$
$C_y = 13 \cdot 15.1986841536 / 20 = 197.5828939964 / 20 = 9.8791446998...$

$D_x = -7.55$
$D_y = 7 \cdot 18.7349939952 / 20 = 131.1449579664 / 20 = 6.5572478983...$

$m_1 = -15.1986841536/13 = -1.1691295503...$
$m_2 = 18.7349939952/7 = 2.6764277136...$

Intersección:
$m_2 x + 10 m_2 = m_1 x - 10 m_1$
$(m_2 - m_1)x = -10(m_1 + m_2)$
$x_E = \frac{-10(m_1 + m_2)}{m_2 - m_1} = \frac{-10(-1.1691295503 + 2.6764277136)}{2.6764277136 + 1.1691295503} = \frac{-10(1.5072981633)}{3.8455572639} = \frac{-15.072981633}{3.8455572639} = -3.919591...$

Calculemos con más precisión: $15.072981633 / 3.8455572639 = 3.91959...$. 

$3.8455572639 \cdot 3.91959 = 15.0729...$, así que $x_E \approx -3.91959$.

$y_E = m_2(x_E + 10) = 2.6764277136 \cdot 6.080409 = 16.27448...$

Distancias exactas (usando la relación con potencias):

$EC$: Podemos usar que en la recta $BC$, $EB \cdot EC = \text{Pot}(E)$, y $EB = \sqrt{(x_E - 10)^2 + y_E^2}$. Pero es más fácil calcular directamente.

$EC = \sqrt{(x_E - x_C)^2 + (y_E - y_C)^2}$.

Dado que en la recta $BC$, los puntos $E$, $C$, $B$ están colineales, podemos calcular $EC$ como:

$EC = |m_1(x_E - x_C)| \sqrt{1 + 1/m_1^2}$... más simple, usar la distancia a lo largo de la recta.

Como $E$, $C$, $B$ colineales, $EC = EB - BC$ (si $C$ está entre $E$ y $B$, que es el caso). 

$EB = \sqrt{(x_E - 10)^2 + y_E^2}$. Pero también, en la recta $BC$, la pendiente es $m_1$, así que $EB = |x_E - 10| \sqrt{1 + m_1^2}$.

$|x_E - 10| = 10 - x_E = 10 + 3.919591 = 13.919591$.

$\sqrt{1 + m_1^2} = \sqrt{1 + 231/169} = \sqrt{400/169} = 20/13$.

$EB = 13.919591 \cdot 20/13 = 1.0707377 \cdot 20 = 21.414754$.

$EC = EB - BC = 21.414754 - 13 = 8.414754$.

Esto es más preciso.

$ED$: En la recta $AD$, $E$, $D$, $A$ colineales, con $D$ entre $E$ y $A$. $ED = EA - AD$.

$EA = |x_E - x_A| \sqrt{1 + m_2^2} = |x_E + 10| \sqrt{1 + 351/49} = (x_E + 10) \sqrt{400/49} = (x_E + 10) \cdot 20/7$.

$x_E + 10 = 6.080409$. $EA = 6.080409 \cdot 20/7 = 17.372597$.

$ED = EA - 7 = 10.372597$.

$CD$: distancia directa: $CD = \sqrt{(x_C - x_D)^2 + (y_C - y_D)^2}$.

$CD^2 = (9.1)^2 + (9.8791447 - 6.5572479)^2 = 82.81 + (3.3218968)^2 = 82.81 + 11.0350 = 93.8450$.

$CD = \sqrt{93.8450} = 9.68736...$

**Excentro con precisión:**

$a = CD = 9.687363...$
$b = ED = 10.372597...$
$c = EC = 8.414754...$

$denom = a - b - c = 9.687363 - 10.372597 - 8.414754 = -9.099988$.

$x_L = \frac{a x_E - b x_C - c x_D}{denom}$
$= \frac{9.687363(-3.919591) - 10.372597(1.55) - 8.414754(-7.55)}{-9.099988}$
$= \frac{-37.9709 - 16.0775 + 63.5314}{-9.099988}$
$= \frac{9.4830}{-9.099988}$
$= -1.04209...$

$y_L = \frac{a y_E - b y_C - c y_D}{denom}$
$= \frac{9.687363(16.27448) - 10.372597(9.8791447) - 8.414754(6.5572479)}{-9.099988}$
$= \frac{157.6572 - 102.4707 - 55.1778}{-9.099988}$
$= \frac{0.0087}{-9.099988}$
$= -0.00096...$

$y_L$ es esencialmente 0 (el pequeño valor se debe a error numérico). Así que $L$ está sobre el eje $x$ con $x_L \approx -1.0421$.

**Paso 58: Determinar el valor exacto**

¿Es $x_L$ un valor notable? Probemos si $x_L = -AO/OD$ o alguna relación con las longitudes dadas.

Dado que $L$ está sobre el eje $x$ y es el excentro, y $OL = |x_L| \approx 1.0421$, necesitamos la forma exacta.

Pensemos geométricamente: $L$ está sobre $AB$ (el eje $x$). La distancia de $L$ al lado $CD$ debe ser igual al exradio.

Como $L$ está sobre $AB$, la distancia de $L$ a $CD$ es la distancia del punto $(-1.0421, 0)$ a la recta $CD$.

Los lados $EC$ y $ED$ son las rectas $BC$ y $AD$. La distancia de $L$ a $BC$ y $AD$ debe ser igual (pues $L$ está en la bisectriz del ángulo $\angle CED$).

Dado que $L$ está sobre el eje $x$, calculemos la distancia de $L$ a la recta $BC$:

Recta $BC$: $y = m_1(x - 10)$ con $m_1 = -\frac{\sqrt{231}}{13}$.

Distancia de $L = (x_L, 0)$ a $BC$:
$$d = \frac{|m_1(x_L - 10)|}{\sqrt{1 + m_1^2}} = \frac{|m_1| |x_L - 10|}{20/13} = \frac{\sqrt{231}/13 \cdot (10 - x_L)}{20/13} = \frac{\sqrt{231}(10 - x_L)}{20}$$

Distancia de $L$ a $AD$: Recta $AD$: $y = m_2(x + 10)$ con $m_2 = \frac{\sqrt{351}}{7}$.

Distancia de $L$ a $AD$:
$$d = \frac{|m_2(x_L + 10)|}{\sqrt{1 + m_2^2}} = \frac{\sqrt{351}/7 \cdot |x_L + 10|}{20/7} = \frac{\sqrt{351}|x_L + 10|}{20}$$

Para que $L$ sea equidistante (bisectriz), igualamos (con signos apropiados):
$$\sqrt{231}(10 - x_L) = \sqrt{351}(x_L + 10)$$

Esta es la misma ecuación que usamos para encontrar $E$ (con signos opuestos). Resolviendo:
$$\sqrt{231}(10 - x) = \sqrt{351}(x + 10)$$
$$10\sqrt{231} - x\sqrt{231} = x\sqrt{351} + 10\sqrt{351}$$
$$x(\sqrt{231} + \sqrt{351}) = 10(\sqrt{231} - \sqrt{351})$$
$$x = \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}}$$

Sustituyendo valores: $\sqrt{231} \approx 15.199$, $\sqrt{351} \approx 18.735$.

Numerador: $10(15.199 - 18.735) = 10(-3.536) = -35.36$.

Denominador: $15.199 + 18.735 = 33.934$.

$x = -35.36 / 33.934 = -1.0420...$. 

¡Esto coincide con $x_L \approx -1.0421$!

**Paso 59: Confirmación del valor exacto**

El valor exacto de $x_L$ (la coordenada del excentro sobre el eje $x$) es:

$$x_L = \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}}$$

Este es un número negativo, con $|x_L| \approx 1.0421$.

Notemos que $\sqrt{351} = \sqrt{9 \cdot 39} = 3\sqrt{39}$ y $\sqrt{231}$ no se simplifica más.

El valor $x_L$ se puede simplificar usando la conjugación:

$$x_L = \frac{10(\sqrt{231} - \sqrt{351})(\sqrt{231} - \sqrt{351})}{(\sqrt{231} + \sqrt{351})(\sqrt{231} - \sqrt{351})} = \frac{10(\sqrt{231} - \sqrt{351})^2}{231 - 351} = \frac{10(\sqrt{231} - \sqrt{351})^2}{-120} = \frac{(\sqrt{231} - \sqrt{351})^2}{-12}$$

Esto no simplifica a un número racional simple.

**Paso 60: Verificación con cálculo exacto del excentro**

Sin embargo, el hecho de que $x_L$ (la intersección de la bisectriz con $AB$) coincida con el excentro requiere que $L$ esté también sobre la bisectriz externa en $C$ (y en $D$). Si $L$ está sobre la bisectriz de $\angle E$ y es equidistante de $BC$ y $AD$, para ser el excentro también debe ser equidistante de $CD$.

Esto impone una condición adicional que determinaría $x_L$ de manera única, y podría no ser el mismo punto que la intersección de la bisectriz del ángulo $\angle E$ con $AB$.

Sin embargo, el cálculo numérico mostró que el excentro $L$ tiene $y_L \approx 0$ y $x_L \approx -1.0421$, lo cual coincide con la intersección de la bisectriz con el eje $x$.

**Paso 61: Cálculo exacto del excentro mediante la condición de equidistancia a CD**

Para confirmar, verifiquemos que el punto $L = (x_L, 0)$ con $x_L = \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}}$ es equidistante de $BC$, $AD$, y $CD$.

Ya sabemos que la distancia de $L$ a $BC$ y $AD$ es igual (por construcción, es la intersección de la bisectriz con el eje $x$). Falta verificar la distancia a $CD$.

La recta $CD$ pasa por $C = (31/20, 13\sqrt{231}/20)$ y $D = (-151/20, 7\sqrt{351}/20)$.

La recta $CD$ tiene pendiente $m_{CD} = \frac{13\sqrt{231}/20 - 7\sqrt{351}/20}{31/20 - (-151/20)} = \frac{13\sqrt{231} - 7\sqrt{351}}{182}$.

Distancia de $L$ a $CD$ debe ser igual a la distancia de $L$ a $BC$ (con signo opuesto para el excírculo).

Debido a la complejidad, la verificación algebraica exacta es extensa. Dado el tiempo, aceptemos el resultado.

**Paso 62: Resultado final y verificación con la fórmula del excentro**

El resultado $x_L = \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}}$ no parece ser la respuesta final elegante que se espera. Típicamente en problemas de olimpiada, la respuesta es un número racional o un radical simple.

Dado que numéricamente $|x_L| \approx 1.0421$, notemos que $1.0421^2 \approx 1.086$, lo cual no es obvio.

Sin embargo, veamos si $x_L$ tiene una forma más simple. Racionalicemos:

$x_L = \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}}$.

Multiplicando numerador y denominador por el conjugado:

$x_L = \frac{10(\sqrt{231} - \sqrt{351})^2}{231 - 351} = \frac{10(231 + 351 - 2\sqrt{231 \cdot 351})}{-120} = \frac{10(582 - 2\sqrt{81081})}{-120} = \frac{582 - 2\sqrt{81081}}{-12} = \frac{-582 + 2\sqrt{81081}}{12} = \frac{-291 + \sqrt{81081}}{6}$.

Dado que $\sqrt{81081} = 9\sqrt{1001} = 9\sqrt{7 \cdot 11 \cdot 13} \approx 9 \cdot 31.6386 = 284.747$, el valor es:

$x_L = \frac{-291 + 284.747}{6} = \frac{-6.253}{6} = -1.04217...$.

Hmm, $\sqrt{81081} \approx 284.747$. Y $81081 = 9 \cdot 9009 = 9 \cdot 9 \cdot 1001 = 81 \cdot 1001$. Espera: $81081 = 81 \cdot 1001$. Verifiquemos: $81 \cdot 1001 = 81081$. Correcto. Entonces $\sqrt{81081} = 9\sqrt{1001}$.

Así que $x_L = \frac{-291 + 9\sqrt{1001}}{6} = -48.5 + \frac{3\sqrt{1001}}{2} \approx -48.5 + 47.4575 = -1.0425$. 

Ahora, ¿es este el valor esperado? Parece complicado. Quizá haya un error en mi enfoque.

**Paso 63: Reconsiderar la interpretación de "E-excircle"**

El $E$-excircle de $\triangle ECD$ es el excírculo opuesto al vértice $E$. Confirma que esto es lo que calculé (con coordenadas baricéntricas $(-a : b : c)$, lo cual es el excentro opuesto a $E$).

Alternativamente, quizá "E-excircle" se refiere al excírculo tangente al lado $CD$ (el lado opuesto a $E$), que es exactamente el excírculo opuesto a $E$. Correcto.

**Paso 64: Verificación independiente con triángulo ECD**

Déjame verificar los cálculos del excentro de manera independiente usando la fórmula de tangencia.

El $E$-excentro $L$ de $\triangle ECD$ satisface que las distancias (con signos) a los tres lados son iguales en magnitud.

Los lados son:
- $EC$ = recta $BC$
- $ED$ = recta $AD$  
- $CD$ = recta $CD$

Si $L = (x, 0)$ sobre el eje $x$, las distancias son:

Distancia a $BC$: $d_1 = \frac{\sqrt{231}(10 - x)}{20}$ (para $x$ entre $-10$ y $10$, con $x < 10$).

Distancia a $AD$: $d_2 = \frac{\sqrt{351}(x + 10)}{20}$.

Para que $d_1 = d_2$ (bisectriz), tenemos $x = \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}}$.

Distancia a $CD$: la recta $CD$ en forma estándar. La recta $CD$ pasa por $C$ y $D$.

Ecuación de $CD$: $y - y_C = m_{CD}(x - x_C)$ con $m_{CD} = \frac{y_D - y_C}{x_D - x_C}$.

La distancia de $L$ a $CD$ es $\frac{|y_L - m_{CD}(x_L - x_C) - y_C|}{\sqrt{1 + m_{CD}^2}}$.

Para que $L$ sea el excentro, necesitamos $d_1 = d_2 = d_3$ (en magnitud).

Dado que el cálculo numérico mostró que $L$ con $y_L \approx 0$ es el excentro (ya que el cálculo directo con valores aproximados dio $y_L \approx 0$), la condición $d_1 = d_2 = d_3$ debe ser satisfecha por $x_L$.

Esto sugiere que $x_L$ es la solución de la ecuación $d_1 = d_3$ (o $d_2 = d_3$), y que coincide con la intersección de la bisectriz.

**Paso 65: Búsqueda de un patrón simple**

Dado que el problema es de olimpiada, la respuesta debe ser simple y elegante. Con $AB = 20$, $BC = 13$, $AD = 7$, todos números racionales, $OL$ probablemente es un número simple.

Numéricamente, $OL = |x_L| \approx 1.0421$. Los números racionales cercanos: $25/24 = 1.04167$, $13/12 = 1.083$, etc. Números algebraicos: $\sqrt{13}/3.46$... no.

¿Quizá el resultado exacto es $OL = \frac{\sqrt{39}}{6} \approx 1.0408$? O $\frac{\sqrt{13}}{3} \approx 1.201$? No.

¿O tal vez $OL = \frac{3\sqrt{13}}{10} = 1.0817$? No.

Dado que mi cálculo numérico tiene incertidumbre, podría ser que $OL = 1$ exactamente, y el error numérico (1.0421 vs 1) sea debido a aproximaciones.

Sin embargo, el cálculo con valores exactos sugiere $x_L \approx -1.0421$, lo cual no es 1.

**Paso 66: Reexaminar el cálculo del excentro**

Déjame verificar el cálculo del excentro usando la fórmula baricéntrica con más cuidado.

Los lados del triángulo $\triangle ECD$:
- $a = CD$ (opuesto a $E$)
- $b = ED$ (opuesto a $C$)
- $c = EC$ (opuesto a $D$)

La fórmula del $E$-excentro (opuesto a $E$) en coordenadas baricéntricas es:

$$L = \frac{-a E + b C + c D}{-a + b + c}$$

Espera, verifiquemos los signos. El incentro es $\frac{aA + bB + cC}{a + b + c}$. El excentro opuesto a $A$ es $\frac{-aA + bB + cC}{-a + b + c}$.

Para nuestro triángulo con vértices $E$, $C$, $D$ y lados $a = CD$ (opuesto a $E$), $b = ED$ (opuesto a $C$), $c = EC$ (opuesto a $D$):

El $E$-excentro (opuesto a $E$) es:
$$L = \frac{-aE + bC + cD}{-a + b + c}$$

Antes usé $L = \frac{aE - bC - cD}{a - b - c}$, lo cual es equivalente (multiplicando numerador y denominador por -1). Verifiquemos: $\frac{-aE + bC + cD}{-a + b + c} = \frac{aE - bC - cD}{a - b - c}$. Correcto, son equivalentes.

$denom = -a + b + c = -9.687 + 10.373 + 8.415 = 9.101$ (positivo).

$x_L = \frac{-a x_E + b x_C + c x_D}{denom} = \frac{-9.687(-3.9196) + 10.373(1.55) + 8.415(-7.55)}{9.101}$

$= \frac{37.971 + 16.077 - 63.532}{9.101} = \frac{-9.484}{9.101} = -1.0421$.

Mismo resultado. El cálculo es consistente.

**Paso 67: Verificación con la otra fórmula del excentro**

Otra manera de verificar: el excentro opuesto a $E$ debe satisfacer que la razón de distancias a los lados $EC$ y $ED$ (con signos apropiados) es igual al cociente de las longitudes.

El excentro opuesto a $E$ está sobre las bisectrices de los ángulos EXTERNOS en $C$ y $D$ y la bisectriz INTERNA en $E$.

El punto $L$ encontrado numéricamente satisface estas condiciones (aproximadamente). 

**Paso 68: Posible error en la interpretación de "E-excircle"**

Quizá "E-excircle" se refiere al excírculo tangente al lado opuesto a $E$, es decir, el excírculo opuesto a $E$, que es lo que calculamos.

O quizá se refiere al excírculo tangente al lado $EC$ o $ED$ (es decir, el $C$-excircle o $D$-excircle del triángulo $ECD$), pero el nombre "E-excircle" sugiere claramente el opuesto a $E$.

**Paso 69: Verificación de que L está sobre AB mediante argumento geométrico**

Veamos por qué $L$ está sobre $AB$. En $\triangle ECD$:
- $AC \perp EC$ (ya que $AC \perp BC = EC$).
- $BD \perp ED$ (ya que $BD \perp AD = ED$).

El ortocentro $H$ del triángulo $ECD$ es $AC \cap BD$.

Para un triángulo, los pies de las alturas y el ortocentro están relacionados. En particular, si $H$ es el ortocentro, las bisectrices de los ángulos del triángulo formado por las alturas tienen propiedades específicas.

Sin embargo, no hay un teorema estándar que diga que el excentro del triángulo original esté sobre una recta particular del triángulo de alturas.

**Paso 70: Reconsiderar la pregunta: ¿el excircle es del triángulo ECD o de otro triángulo?**

La pregunta dice "the E-excircle of ECD", que significa el excírculo opuesto a $E$ del triángulo $ECD$.

**Paso 71: Búsqueda de la solución mediante software**

Dado que esta es una pregunta de matemáticas, esperemos que la respuesta sea elegante. Mi cálculo numérico sugiere $OL \approx 1.042$, pero esto no es elegante. Posiblemente cometí un error en el cálculo del excentro.

Déjame verificar el excentro usando la fórmula de la distancia (exradio) directamente.

El exradio opuesto a $E$ es $r_a = \frac{K}{s - a}$, donde $K$ es el área, $s$ es el semiperímetro, y $a = CD$.

$s = \frac{a + b + c}{2} = \frac{9.687 + 10.373 + 8.415}{2} = \frac{28.475}{2} = 14.2375$.

$s - a = 14.2375 - 9.687 = 4.5505$.

$K = \sqrt{s(s-a)(s-b)(s-c)} = \sqrt{14.2375 \cdot 4.5505 \cdot (14.2375 - 10.373) \cdot (14.2375 - 8.415)} = \sqrt{14.2375 \cdot 4.5505 \cdot 3.8645 \cdot 5.8225}$.

$14.2375 \cdot 4.5505 \approx 64.79$. $3.8645 \cdot 5.8225 \approx 22.50$. $64.79 \cdot 22.50 \approx 1457.8$. $\sqrt{1457.8} \approx 38.18$.

$r_a = \frac{K}{s - a} = \frac{38.18}{4.5505} \approx 8.39$.

La distancia de $L \approx (-1.042, 0)$ a la recta $BC$ es $\frac{\sqrt{231}(10 - 1.042)}{20} = \frac{15.199 \cdot 8.958}{20} = \frac{136.15}{20} \approx 6.81$.

Hmm, $6.81 \neq 8.39$. Esto sugiere que mi cálculo del excentro es incorrecto o que el punto $L$ no es el excentro que calculé.

Déjame verificar. El exradio $r_a$ es la distancia del excentro a los lados. Si $L = (-1.042, 0)$ es el excentro, la distancia a $BC$ debe ser $r_a$.

Verifiquemos la distancia de $L$ a $BC$ con más cuidado.

Recta $BC$: $y = m_1(x - 10)$ con $m_1 = -\sqrt{231}/13$.

Distancia de $(x_L, 0)$: $d = \frac{|0 - m_1(x_L - 10)|}{\sqrt{1 + m_1^2}} = \frac{|m_1| \cdot |x_L - 10|}{\sqrt{1 + m_1^2}}$.

$|m_1| = \sqrt{231}/13$. $|x_L - 10| = 10 - x_L = 10 + 1.0421 = 11.0421$.

$\sqrt{1 + m_1^2} = \sqrt{1 + 231/169} = \sqrt{400/169} = 20/13$.

$d = \frac{(\sqrt{231}/13)(11.0421)}{20/13} = \frac{\sqrt{231} \cdot 11.0421}{20} = \frac{15.1987 \cdot 11.0421}{20} = \frac{167.82}{20} = 8.391$.

¡Esto coincide con $r_a \approx 8.39$! Cometí un error en el paso anterior al calcular $\frac{15.199 \cdot 8.958}{20}$ en lugar de $\frac{15.199 \cdot 11.042}{20}$.

Así que la distancia de $L$ a $BC$ es $\approx 8.39 = r_a$. Correcto, $L$ es el excentro.

**Paso 72: Recalcular la distancia correctamente**

La distancia de $L$ a $BC$: $d_1 = \frac{\sqrt{231}(10 - x_L)}{20}$ solo si $x_L$ está entre $-10$ y $10$... En realidad, $x_L \approx -1.042$, así que $10 - x_L \approx 11.042$, no $8.958$ como calculé antes. Error mío.

La distancia de $L$ a $AD$: $d_2 = \frac{\sqrt{351}(x_L + 10)}{20} = \frac{18.735 \cdot 8.958}{20} = \frac{167.82}{20} \approx 8.391$. Correcto.

Para verificar que $d_1 = d_2$: con $x_L$ de la bisectriz:
$\sqrt{231}(10 - x_L) = \sqrt{231}(10 + 1.0421) = 15.199 \cdot 11.0421 = 167.82$.
$\sqrt{351}(x_L + 10) = 18.735 \cdot 8.9579 = 167.82$. Correcto, $d_1 = d_2 = 8.391$.

El exradio es $r_a = 8.39$, lo cual coincide. Todo es consistente.

**Paso 73: Cálculo del excentro de manera exacta y elegante**

El $E$-excentro $L$ está sobre $AB$ en la posición $x_L = \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}}$.

Este valor puede tener una forma elegante si notamos que $\sqrt{231} = \sqrt{3 \cdot 7 \cdot 11}$ y $\sqrt{351} = \sqrt{27 \cdot 13} = 3\sqrt{39}$.

En realidad, déjame simplificar usando las propiedades del triángulo rectángulo.

$\sqrt{231} = \sqrt{231}$ y $\sqrt{351} = \sqrt{351}$. Notemos que $231 = 121 + 110 = 11^2 + 110$, no ayuda.

**Paso 74: Relación con los catetos de los triángulos rectángulos**

En $\triangle ABC$ (rectángulo en C):
- $AB = 20$ (hipotenusa)
- $BC = 13$ (cateto)
- $AC = \sqrt{400 - 169} = \sqrt{231}$

En $\triangle ABD$ (rectángulo en D):
- $AB = 20$ (hipotenusa)
- $AD = 7$ (cateto)
- $BD = \sqrt{400 - 49} = \sqrt{351}$

Así que $AC = \sqrt{231}$ y $BD = \sqrt{351}$.

**Paso 75: Encontrar la relación**

El excentro $L$ sobre $AB$ tiene coordenada $x_L = -\frac{10(AC - BD)}{AC + BD}$... veamos.

$x_L = \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}} = \frac{10(AC - BD)}{AC + BD}$.

Dado que $AC = \sqrt{231} \approx 15.2$ y $BD = \sqrt{351} \approx 18.7$, tenemos $AC - BD \approx -3.5$ y $AC + BD \approx 33.9$, así que $x_L \approx -1.04$.

$OL = |x_L| = 10 \cdot \frac{BD - AC}{AC + BD}$ (si $BD > AC$).

$\frac{BD - AC}{AC + BD} = \frac{\sqrt{351} - \sqrt{231}}{\sqrt{351} + \sqrt{231}}$.

Podemos racionalizar:
$OL^2 = 100 \cdot \frac{(\sqrt{351} - \sqrt{231})^2}{(\sqrt{351} + \sqrt{231})^2} = 100 \cdot \frac{351 + 231 - 2\sqrt{351 \cdot 231}}{351 + 231 + 2\sqrt{351 \cdot 231}} = 100 \cdot \frac{582 - 2\sqrt{81081}}{582 + 2\sqrt{81081}}$.

$\sqrt{81081} = 9\sqrt{1001} \approx 284.7$. $2\sqrt{81081} \approx 569.5$.

$OL^2 = 100 \cdot \frac{582 - 569.5}{582 + 569.5} = 100 \cdot \frac{12.5}{1151.5} \approx 100 \cdot 0.01086 = 1.086$.

$OL = \sqrt{1.086} \approx 1.042$.

**Paso 76: Expresión simplificada**

$OL = \frac{10|\sqrt{351} - \sqrt{231}|}{\sqrt{351} + \sqrt{231}}$, lo que se puede escribir como:

$OL = 10 \cdot \frac{\sqrt{351} - \sqrt{231}}{\sqrt{351} + \sqrt{231}}$.

Racionalizando:
$OL = 10 \cdot \frac{(\sqrt{351} - \sqrt{231})^2}{351 - 231} = \frac{10(582 - 2\sqrt{81081})}{120} = \frac{582 - 2\sqrt{81081}}{12} = \frac{291 - \sqrt{81081}}{6} = \frac{291 - 9\sqrt{1001}}{6}$.

Esto no es un número racional simple. Es $OL = \frac{291 - 9\sqrt{1001}}{6} \approx \frac{291 - 284.747}{6} \approx \frac{6.253}{6} \approx 1.042$.

Hmm, pero $291 - 9\sqrt{1001}$ es negativo (ya que 9\sqrt{1001} ≈ 284.75 < 291). Entonces $OL \approx 1.042 > 0$.

$OL = \frac{291 - 9\sqrt{1001}}{6}$? Verifiquemos: $9\sqrt{1001} = 9 \cdot 31.6386 = 284.747$. $291 - 284.747 = 6.253$. $6.253/6 = 1.0422$. Correcto.

Esta expresión no es elegante. Probablemente cometí un error en algún paso, o la respuesta esperada es un número más simple que he calculado incorrectamente.

**Paso 77: Reconsiderar el problema desde cero**

Quizá el error está en la identificación del excentro. Déjame reconsiderar.

En el triángulo $\triangle ECD$, el punto $E$ es la intersección de $BC$ y $AD$. Los lados del triángulo son:
- $EC$ = segmento de $BC$ desde $E$ hasta $C$ (que es la recta $BC$).
- $ED$ = segmento de $AD$ desde $E$ hasta $D$ (que es la recta $AD$).
- $CD$ = segmento entre $C$ y $D$.

El $E$-excircle es el círculo tangente a $CD$ (el lado opuesto a $E$) y a las prolongaciones de $EC$ y $ED$ (más allá de $C$ y $D$ respectivamente).

El centro $L$ está en la bisectriz del ángulo $\angle CED$ (la bisectriz interna) y en las bisectrices de los ángulos externos en $C$ y $D$.

**Paso 78: Verificación de la orientación**

El ángulo $\angle CED$ es el ángulo en $E$ entre $EC$ y $ED$. Dado que $E$ está por encima de $AB$, y $C$, $D$ están también por encima (pero más cerca de $AB$ que $E$), el ángulo $\angle CED$ es el ángulo entre las semirrectas $EC$ y $ED$ que van hacia abajo.

La bisectriz de este ángulo es una recta desde $E$ hacia abajo (hacia $AB$). Intersecciona $AB$ en algún punto (que es nuestro $x_L$).

**Paso 79: Verificación de que L está en la bisectriz**

Para cualquier punto $P$ sobre la bisectriz de $\angle CED$, las distancias a los lados $EC$ y $ED$ son iguales. Si $P$ está sobre $AB$, la condición es:

$\frac{\sqrt{231}(10 - x)}{20} = \frac{\sqrt{351}(x + 10)}{20}$ (con signos apropiados).

Esto da $x = \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}}$.

**Paso 80: ¿Es esta la única condición para el excentro?**

Para que $P$ sea el excentro $L$, también debe estar sobre la bisectriz del ángulo externo en $C$ (del triángulo $\triangle ECD$). La bisectriz del ángulo externo en $C$ es la recta que biseca el ángulo entre $CE$ (hacia $E$) y la prolongación de $CD$ (más allá de $C$ en dirección opuesta a $D$).

Si $P$ está sobre la bisectriz de $\angle E$ y sobre $AB$, y resulta ser también el excentro, entonces las tres condiciones se satisfacen. Esto se verifica numéricamente, pero necesitamos confirmar algebraicamente.

Dado que la verificación numérica muestra que $L$ tiene $y_L \approx 0$ y $x_L \approx -1.0421$, y que la distancia a $BC$ es igual a $r_a$ (el exradio), podemos confiar en el resultado.

**Paso 81: Búsqueda de la respuesta simplificada**

El problema pide $OL$, no $x_L$. Como $L$ está sobre $AB$ (el eje $x$) y $O$ está en el origen, $OL = |x_L|$.

$x_L = \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}} = \frac{10(AC - BD)}{AC + BD}$, donde $AC = \sqrt{231}$ y $BD = \sqrt{351}$.

Usando $AC = \sqrt{231}$ y $BD = \sqrt{351}$:

$OL = \left| \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}} \right| = 10 \cdot \frac{\sqrt{351} - \sqrt{231}}{\sqrt{351} + \sqrt{231}}$.

**Paso 82: Simplificación elegante**

$\frac{\sqrt{351} - \sqrt{231}}{\sqrt{351} + \sqrt{231}} = \frac{(\sqrt{351} - \sqrt{231})^2}{351 - 231} = \frac{351 + 231 - 2\sqrt{351 \cdot 231}}{120} = \frac{582 - 2\sqrt{351 \cdot 231}}{120}$.

Ahora, $\sqrt{351 \cdot 231} = \sqrt{351} \cdot \sqrt{231}$. Pero $351 = 27 \cdot 13$ y $231 = 3 \cdot 7 \cdot 11 = 3 \cdot 77 = 3 \cdot 7 \cdot 11$. Entonces $351 \cdot 231 = 27 \cdot 13 \cdot 3 \cdot 7 \cdot 11 = 81 \cdot 13 \cdot 7 \cdot 11 = 81 \cdot 1001$.

$\sqrt{351 \cdot 231} = \sqrt{81 \cdot 1001} = 9\sqrt{1001} = 9\sqrt{7 \cdot 11 \cdot 13}$.

No hay simplificación adicional sin factor común.

**Paso 83: Verificación con potencias y el teorema de Pitágoras**

Quizá el resultado se simplifica usando las relaciones del triángulo. En el triángulo $\triangle ABC$ (rectángulo en C), $\cos \angle ABC = 13/20$. En $\triangle ABD$ (rectángulo en D), $\cos \angle BAD = 7/20$.

Hay identidades trigonométricas que relacionan estos valores.

**Paso 84: Conclusión y resultado final**

Dado el análisis exhaustivo, el excentro $L$ está sobre $AB$ en $x_L = \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}}$, y por lo tanto:

$$OL = 10 \cdot \frac{\sqrt{351} - \sqrt{231}}{\sqrt{351} + \sqrt{231}}$$

Sin embargo, esta expresión es complicada. Verifiquemos si tiene una forma más simple.

Notemos que $\sqrt{351} = 3\sqrt{39}$ y $\sqrt{231} = \sqrt{3 \cdot 7 \cdot 11}$. No hay simplificación obvia.

Quizá cometí un error y el resultado es más simple. Revisemos la configuración una vez más.

**Paso 85: Reconsideración con homotecia**

Hay un teorema hermoso: si dos círculos exinscritos son homotéticos, la razón de homotecia está relacionada con los radios. En este caso, la circunferencia $\omega$ y el $E$-excircle de $\triangle ECD$ están relacionados.

Notemos que $EC$ es una recta tangente al $E$-excircle (en algún punto entre $C$ y $E$ o más allá). En realidad, el $E$-excircle es tangente a $EC$ en algún punto $T$ sobre la recta $BC$. De manera similar, es tangente a $ED$ en algún punto $U$ sobre $AD$, y a $CD$ en algún punto $V$ sobre $CD$.

La recta $EC$ (o $BC$) es perpendicular al radio del excircle en el punto de tangencia. El radio desde $L$ a $EC$ es perpendicular a $EC$ en el punto de tangencia.

Como $AC \perp EC$ (en $C$), y $L$ está sobre $AB$, el radio desde $L$ a $EC$ es paralelo a $AC$.

Esto sugiere una relación entre $L$ y el punto $A$.

En particular, el pie de la perpendicular desde $L$ a $EC$ (recta $BC$) es algún punto $T$ sobre $BC$. Como $LT \perp BC$ y $AC \perp BC$, tenemos $LT \parallel AC$.

Si $T$ estuviera en $C$, entonces $LT \parallel AC$ implicaría que $L$ está sobre la recta paralela a $AC$ que pasa por $C$, pero $L$ está sobre $AB$, lo que no es posible en general.

**Paso 86: Uso del ángulo y tangencia**

El $E$-excircle de $\triangle ECD$ es tangente a $CD$ (el lado opuesto a $E$). El punto de tangencia $V$ está sobre $CD$. El radio $LV$ es perpendicular a $CD$.

Como $L$ está sobre $AB$, $LV$ es perpendicular a $CD$ y pasa por $L$. Esto conectaría el punto $L$ sobre $AB$ con el lado $CD$ mediante una perpendicular.

**Paso 87: Búsqueda del resultado en la literatura**

Este problema parece ser de una competencia (quizá AIME o similar). Los problemas de AIME tienen respuestas enteras de 3 dígitos. Si $OL$ no es entero, hay un problema con la interpretación.

Releyendo el problema: "Find O L". En AIME, la respuesta sería un número de 3 dígitos (posiblemente con decimales). Si $OL \approx 1.04$, la respuesta AIME sería 104 (si se expresa en centésimas).

Sin embargo, $OL \approx 1.042$ no parece típico. Quizá la respuesta exacta es un número racional simple como $25/24 \approx 1.0417$.

**Paso 88: Búsqueda de una fracción simple**

$1.0421 \approx 25/24 = 1.04167$, $99/95 = 1.0421$, $52/50 = 1.04$.

¿Podría ser $OL = \sqrt{13}/12 \approx 0.300$? No.

¿$OL = \sqrt{3}/2 \approx 0.866$? No. ¿$OL = 2\sqrt{3}/3 \approx 1.155$? No. ¿$OL = \sqrt{7}/3 \approx 0.882$? No. ¿$OL = \sqrt{13}/4 \approx 0.901$? No.

Ninguno de estos coincide con 1.042.

**Paso 89: Reexaminar la ubicación de E**

Verifiquemos si $E$ está realmente fuera de la circunferencia. $E \approx (-3.92, 16.27)$, entonces $EO^2 = 3.92^2 + 16.27^2 = 15.37 + 264.71 = 280.08 > 100$. Sí, $E$ está fuera.

Potencia de $E$: $EO^2 - R^2 = 280.08 - 100 = 180.08$.

$EB \cdot EC = 21.41 \cdot 8.41 = 180.05$. Correcto (difieren por error numérico).

$EA \cdot ED = 17.37 \cdot 10.37 = 180.12$. Correcto.

**Paso 90: Uso de la inversión**

Apliquemos una inversión con centro en $E$ y potencia $EO^2 - R^2$ (la potencia de $E$ respecto a $\omega$). Esta inversión intercambia $B$ con $C$ y $A$ con $D$ (ya que $EB \cdot EC = EA \cdot ED = \text{Pot}(E)$).

Bajo esta inversión:
- $B \leftrightarrow C$
- $A \leftrightarrow D$
- La línea $AB$ se intercambia con una circunferencia que pasa por $E$, $C$, $D$ (ya que los puntos $A$, $B$ en $AB$ se intercambian con $D$, $C$ sobre la línea... en realidad, la recta $AB$ no pasa por $E$, se convierte en una circunferencia que pasa por $E$).

En particular, la recta $AB$ se convierte en la circunferencia que pasa por $E$, $C$, $D$, que es el circuncírculo de $\triangle ECD$.

El centro $O$ de $\omega$ está en la recta $AB$. Bajo la inversión, $O$ se convierte en $O'$ que está en el circuncírculo de $\triangle ECD$.

Además, la recta $AB$ es perpendicular al radio $OE$... (necesitamos más análisis).

**Paso 91: La inversión y el excentro**

Bajo inversión centrada en $E$, las rectas $EC$ y $ED$ pasan por el centro de inversión, así que se convierten en sí mismas. El punto $L$ (excentro) se convierte en $L'$ sobre la misma recta $EL$.

El $E$-excircle de $\triangle ECD$ es tangente a los lados $EC$ y $ED$. Bajo inversión centrada en $E$, las tangentes al excircle se convierten en... la inversión de un círculo que no pasa por el centro es otro círculo.

Esta es una técnica estándar para relacionar el excentro con la circunferencia original. De hecho, se sabe que el $E$-excentro de $\triangle ECD$ está relacionado con el centro $O$ de $\omega$ mediante la inversión.

**Paso 92: Teorema clave de la inversión**

El $E$-excentro de $\triangle ECD$ es la imagen de $O$ bajo una inversión centrada en $E$ (con potencia la potencia de $E$ respecto a $\omega$), o algo similar.

Déjame verificar. Bajo la inversión $\mathcal{I}$ centrada en $E$ con potencia $k = \text{Pot}(E) = EO^2 - R^2$, la circunferencia $\omega$ se invierte en sí misma (ya que $\omega$ es ortogonal a... en realidad, una circunferencia que pasa por puntos inversos se invierte en su complemento).

Como $E$ está fuera de $\omega$, la inversión intercambia los puntos donde las secantes desde $E$ intersectan $\omega$. Específicamente, $\mathcal{I}$ intercambia $B$ con $C$ y $A$ con $D$.

La recta $AB$ (que no pasa por $E$) se invierte en una circunferencia que pasa por $E$, $C$, $D$, que es el circuncírculo de $\triangle ECD$.

El centro $O$ de $\omega$ (que está sobre $AB$) se invierte en $O'$, que está sobre el circuncírculo de $\triangle ECD$.

Además, $O$ es el centro de $\omega$, y $\omega$ pasa por $A$, $B$, $C$, $D$. 

**Paso 93: Relación con el excentro mediante inversión**

La recta $AB$ es perpendicular al radio $OE$... en general no, $O$ está sobre $AB$ pero no hay perpendicularidad con $OE$.

La recta $AB$ es una cuerda de $\omega$ (el diámetro). El punto $O$ está sobre $AB$.

Bajo inversión, $O'$ es un punto sobre el circuncírculo de $\triangle ECD$.

Para $\triangle ECD$, el circuncírculo es el círculo que pasa por $E$, $C$, $D$. Su centro $O_c$ es distinto de $L$ (el excentro).

**Paso 94: Relación entre el excentro y el centro del circuncírculo**

Para un triángulo $\triangle ECD$:
- El circuncírculo tiene centro $O_c$ y radio $R_c$.
- El $E$-excentro $L$ tiene exradio $r_a$.

La distancia entre $O_c$ y $L$ satisface $O_c L^2 = R_c^2 + 2R_c r_a$ (para el excentro opuesto a $E$).

**Paso 95: Relación con la inversión de O**

Bajo la inversión centrada en $E$ con potencia $k$:
- $O' = \mathcal{I}(O)$ está sobre la semirrecta $EO$ con $EO \cdot EO' = k$.
- Como $EO^2 - R^2 = k$, tenemos $EO' = \frac{k}{EO} = \frac{EO^2 - R^2}{EO}$.

El punto $O'$ está sobre la circunferencia imagen de $AB$ (el circuncírculo de $\triangle ECD$).

**Paso 96: El excentro como imagen de un punto específico**

Quizá el $E$-excentro $L$ es la imagen de $O$ bajo una homotecia centrada en $E$ (no una inversión), con una razón específica.

Dado que la bisectriz de $\angle CED$ pasa por $E$, $O$, y $L$ (si $L$ está sobre $EO$), podemos usar la relación entre $EO$ y $EL$.

Numéricamente, $E \approx (-3.92, 16.27)$, $O = (0,0)$, $L \approx (-1.042, 0)$.

$EO \approx \sqrt{3.92^2 + 16.27^2} = 16.73$. $EL \approx \sqrt{(3.92 - 1.042)^2 + 16.27^2} = \sqrt{2.88^2 + 264.7} = \sqrt{8.3 + 264.7} = \sqrt{273} = 16.52$.

$EL/EO \approx 16.52/16.73 \approx 0.987$. Casi 1.

Esto sugiere que $L$ está muy cerca de $O$ en la recta $EO$. Esto es extraño.

Verifiquemos si $O$, $E$, $L$ son colineales. $O=(0,0)$, $E=(-3.92, 16.27)$, $L=(-1.042, 0)$.

Pendiente $OE$: $(16.27 - 0)/(-3.92 - 0) = -4.15$. Pendiente $OL$: $(0 - 0)/(-1.042 - 0) = 0$. No son colineales.

Así que $O$, $E$, $L$ no están en la misma recta. El excentro $L$ no está sobre $EO$.

**Paso 97: Reconsideración de la bisectriz**

La bisectriz de $\angle CED$ pasa por $E$ y por el punto sobre $AB$ que encontramos ($x_L$). Esta bisectriz no necesariamente pasa por $O$.

El excentro $L$ está sobre esta bisectriz. Como $L$ está sobre $AB$ (eje $x$) y sobre la bisectriz, $L$ es la intersección de la bisectriz con $AB$.

Esto no implica que $O$, $E$, $L$ sean colineales.

**Paso 98: Resultado final**

El resultado $OL = \left| \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}} \right| = 10 \cdot \frac{\sqrt{351} - \sqrt{231}}{\sqrt{351} + \sqrt{231}}$ es la solución.

Sin embargo, esta expresión no es elegante. Dado que el problema probablemente espera un valor más simple, quizá haya una simplificación adicional.

**Paso 99: Intento de simplificación adicional**

$\frac{\sqrt{351} - \sqrt{231}}{\sqrt{351} + \sqrt{231}} = \frac{\sqrt{9 \cdot 39} - \sqrt{231}}{\sqrt{9 \cdot 39} + \sqrt{231}} = \frac{3\sqrt{39} - \sqrt{231}}{3\sqrt{39} + \sqrt{231}}$.

Multiplicando numerador y denominador por $3\sqrt{39} - \sqrt{231}$:

$= \frac{(3\sqrt{39} - \sqrt{231})^2}{351 - 231} = \frac{9 \cdot 39 + 231 - 6\sqrt{39 \cdot 231}}{120} = \frac{351 + 231 - 6\sqrt{9009}}{120} = \frac{582 - 6\sqrt{9009}}{120} = \frac{97 - \sqrt{9009}}{20}$.

Entonces $OL = 10 \cdot \frac{97 - \sqrt{9009}}{20} = \frac{97 - \sqrt{9009}}{2}$.

Verifiquemos: $\sqrt{9009} = \sqrt{9 \cdot 1001} = 3\sqrt{1001} = 3 \cdot 31.6386 = 94.9158$. $97 - 94.9158 = 2.0842$. $2.0842/2 = 1.0421$. Correcto.

$OL = \frac{97 - 3\sqrt{1001}}{2} \approx 1.0421$.

Esta expresión es $OL = \frac{97 - 3\sqrt{1001}}{2}$. Aún complicada.

**Paso 100: Posible error en la identificación del excentro**

Déjame reconsiderar si el $E$-excentro es el excentro opuesto a $E$ o el excentro adyacente a $E$ (es decir, tangente al lado $EC$ o $ED$).

El término "$E$-excircle" en el contexto del triángulo $ECD$ se refiere al excircle tangente al lado opuesto a $E$, que es $CD$. Este es el excircle opuesto a $E$, con centro en la intersección de la bisectriz interna de $\angle E$ y las bisectrices externas de $\angle C$ y $\angle D$.

Esto es lo que calculé. Confiemos en el resultado.

**Paso 101: Verificación con el teorema del ángulo externo**

Otra manera de verificar: el $E$-excentro $L$ satisface que $\angle LCE = 90° - \angle ECD/2$ (propiedad del excentro y la bisectriz externa).

Como $AC \perp CE$, tenemos $\angle ACE = 90°$. La bisectriz externa en $C$ forma un ángulo con $CE$ igual a $\frac{\pi - \angle ECD}{2}$.

Para que $AC$ sea la bisectriz externa, necesitaríamos $\frac{\pi - \angle ECD}{2} = \frac{\pi}{2}$, lo que da $\angle ECD = -\frac{\pi}{2}$, absurdo. Así que $AC$ no es la bisectriz externa.

**Paso 102: Aceptación del resultado**

Dado el análisis, el resultado es:

$$OL = \frac{97 - 3\sqrt{1001}}{2}$$

Este es un número positivo (ya que $97 > 3\sqrt{1001}$ porque $97^2 = 9409$ y $(3\sqrt{1001})^2 = 9009$, y $9409 > 9009$).

$OL = \frac{97 - \sqrt{9009}}{2}$.

Alternativamente, $OL = \frac{97 - \sqrt{9009}}{2}$.

**Paso 103: Simplificación alternativa**

$9009 = 9 \cdot 1001 = 9 \cdot 7 \cdot 11 \cdot 13$. No hay simplificación.

El resultado es $OL = \frac{97 - 3\sqrt{1001}}{2} \approx 1.0421$.

Sin embargo, este resultado es extraño para un problema de olimpiada. Posiblemente cometí un error en el cálculo del excentro. Déjame hacer una verificación final usando la fórmula del excentro en términos de coordenadas exactas.

**Paso 104: Verificación con la fórmula del excentro usando coordenadas exactas**

Usemos la fórmula del excentro con las longitudes exactas de los lados.

Los lados del triángulo $\triangle ECD$:
- $EC$ = distancia entre $E$ y $C$
- $ED$ = distancia entre $E$ y $D$
- $CD$ = distancia entre $C$ y $D$

Ya calculamos:
- $EC = \frac{\sqrt{231}}{13}(10 - x_E) \cdot \frac{20}{13}$? No, usemos coordenadas exactas.

Sabemos que $E$, $C$, $B$ son colineales con $C$ entre $E$ y $B$. $EB = 13 + EC$. $EB \cdot EC = \text{Pot}(E) = EO^2 - 100$.

$EO^2$: $E$ es la intersección de $BC$ y $AD$. Podemos calcular $EO^2$ usando las ecuaciones de las rectas.

**Paso 105: Cálculo exacto de EO^2**

Usemos el resultado de que $E$ está en la recta $BC$ y en la recta $AD$.

De la ecuación de la bisectriz (que usamos para $x_L$), notemos que $x_E$ (la intersección de $BC$ y $AD$) satisface:

$m_1(x_E - 10) = m_2(x_E + 10)$ (ya que $E$ está en ambas rectas).

Esta es diferente de la ecuación de la bisectriz. La ecuación de $E$ es:
$-\frac{\sqrt{231}}{13}(x_E - 10) = \frac{\sqrt{351}}{7}(x_E + 10)$.

**Paso 106: Cálculo del excentro mediante la fórmula de exradio**

Dado que $L$ está sobre $AB$ y es el excentro, y ya verificamos que la distancia de $L$ a $BC$ y $AD$ es igual a $r_a$ (el exradio), podemos usar la siguiente propiedad:

$OL = |x_L| = \frac{10(\sqrt{351} - \sqrt{231})}{\sqrt{351} + \sqrt{231}}$.

**Paso 107: ¿Puede simplificarse esta expresión?**

$\frac{\sqrt{351} - \sqrt{231}}{\sqrt{351} + \sqrt{231}} = \frac{(\sqrt{351} - \sqrt{231})^2}{351 - 231} = \frac{582 - 2\sqrt{351 \cdot 231}}{120}$.

$351 \cdot 231 = 81081$. $\sqrt{81081} = 9\sqrt{1001}$.

Así que $OL = 10 \cdot \frac{582 - 2 \cdot 9\sqrt{1001}}{120} \cdot \frac{1}{2}$... espera, ya teníamos $OL = \frac{97 - 3\sqrt{1001}}{2}$.

**Paso 108: Verificación numérica final**

$OL = \frac{97 - 3\sqrt{1001}}{2}$.

$3\sqrt{1001} = 3 \cdot 31.63858 = 94.91575$.

$OL = \frac{97 - 94.91575}{2} = \frac{2.08425}{2} = 1.04213$.

Esto coincide con el cálculo numérico anterior.

**Paso 109: Consideración de la forma alternativa**

$OL = \frac{97 - 3\sqrt{1001}}{2}$ puede escribirse como $\frac{97}{2} - \frac{3\sqrt{1001}}{2}$.

Notemos que $97 = 49 + 48$ y $1001 = 7 \cdot 11 \cdot 13$. No hay simplificación obvia.

**Paso 110: Reconsiderar si el excentro está sobre AB o fuera**

Numéricamente, $L \approx (-1.042, 0)$, que está sobre $AB$ (entre $A$ y $B$). Esto es plausible.

**Paso 111: Verificación con la condición de tangencia al lado CD**

Para confirmar, verifiquemos la distancia de $L$ a $CD$.

La recta $CD$ pasa por $C=(1.55, 9.879)$ y $D=(-7.55, 6.557)$.

Pendiente de $CD$: $\frac{6.557 - 9.879}{-7.55 - 1.55} = \frac{-3.322}{-9.1} = 0.3651$.

Ecuación de $CD$: $y - 9.879 = 0.3651(x - 1.55)$.

$y = 0.3651x - 0.566 + 9.879 = 0.3651x + 9.313$.

Distancia de $L=(-1.042, 0)$ a $CD$:
$d = \frac{|0.3651(-1.042) + 9.313 - 0|}{\sqrt{1 + 0.3651^2}} = \frac{|9.313 - 0.380|}{\sqrt{1.133}} = \frac{8.933}{1.0645} = 8.392$.

Esto coincide con $r_a \approx 8.39$. Correcto.

**Paso 112: Conclusión final**

El resultado es:

$$OL = \frac{97 - 3\sqrt{1001}}{2} = \frac{97 - \sqrt{9009}}{2}$$

Sin embargo, dada la complejidad de esta expresión, me pregunto si hay una interpretación alternativa del problema que dé un resultado más simple.

**Paso 113: Reinterpretación del problema**

Quizá el problema asume $C$ y $D$ en lados opuestos de $AB$ en lugar del mismo lado. Releamos: "$C$ and $D$ on the same side of $\overline{AB}$". Sí, están en el mismo lado.

**Paso 114: Verificación con software de geometría**

Sin software disponible, confiemos en el análisis. La respuesta es:

$$OL = \frac{97 - 3\sqrt{1001}}{2}$$

Déjame verificar si esta expresión es positiva: $3\sqrt{1001} \approx 94.9 < 97$, así que $OL > 0$. Correcto.

**Paso 115: Expresión final en forma de caja**

El problema pide solo la respuesta final en \boxed{}. Dado que el valor numérico es aproximadamente 1.042, y no hay una forma más simple, la respuesta es:

$$\boxed{\frac{97 - 3\sqrt{1001}}{2}}$$

Sin embargo, voy a reconsiderar una vez más si hay una manera más elegante de expresar esto.

**Paso 116: Intento final de simplificación**

$OL = \frac{97 - 3\sqrt{1001}}{2}$.

$1001 = 7 \cdot 11 \cdot 13$.

$97 = 7 \cdot 13 + 6$. No hay factor común.

$3\sqrt{1001} = 3\sqrt{7 \cdot 11 \cdot 13}$.

No hay simplificación.

**Paso 117: Verificación de que L está sobre AB mediante el problema inverso**

Dado que numéricamente $L \approx (-1.04, 0)$, y para el excentro $L$ sobre $AB$, la distancia de $L$ a $BC$ es:

$d = \frac{\sqrt{231}(10 - x_L)}{20} = \frac{\sqrt{231}(10 - (-1.042))}{20} = \frac{15.199 \cdot 11.042}{20} = \frac{167.82}{20} = 8.391$.

El exradio $r_a = \frac{K}{s - a} = \frac{38.18}{4.55} = 8.39$. Correcto.

**Paso 118: Revisión de la derivación del excentro sobre AB**

Demostremos algebraicamente que el excentro $L$ está sobre $AB$. La bisectriz de $\angle CED$ intersecta $AB$ en $x_L = \frac{10(\sqrt{231} - \sqrt{351})}{\sqrt{231} + \sqrt{351}}$.

Para que este punto sea el excentro, la distancia a $CD$ debe ser igual (en magnitud) a la distancia a $BC$ y $AD$.

La distancia de $L$ a $BC$: $d_{BC} = \frac{\sqrt{231}(10 - x_L)}{20}$.

La distancia de $L$ a $CD$: usemos la fórmula de distancia punto-recta.

La recta $CD$ en forma estándar. Usando $C$ y $D$:

Ecuación de $CD$: $(y_D - y_C)x - (x_D - x_C)y + x_D y_C - y_D x_C = 0$.

Sustituyendo $y_D - y_C = 7\sqrt{351}/20 - 13\sqrt{231}/20 = \frac{7\sqrt{351} - 13\sqrt{231}}{20}$.

$x_D - x_C = -151/20 - 31/20 = -182/20 = -91/10$.

$x_D y_C - y_D x_C = (-151/20)(13\sqrt{231}/20) - (7\sqrt{351}/20)(31/20) = \frac{-151 \cdot 13\sqrt{231} - 7 \cdot 31\sqrt{351}}{400} = \frac{-1963\sqrt{231} - 217\sqrt{351}}{400}$.

La distancia de $L=(x_L, 0)$ a $CD$ es:

$d_{CD} = \frac{|(y_D - y_C)x_L + x_D y_C - y_D x_C|}{\sqrt{(y_D - y_C)^2 + (x_D - x_C)^2}}$.

Para que $d_{CD} = d_{BC}$, se requiere una relación que, en principio, podría no ser satisfecha por $x_L$ de la bisectriz. Sin embargo, el cálculo numérico mostró que sí se satisface.

**Paso 119: Demostración de que d_CD = d_BC con x_L de la bisectriz**

Hay una identidad algebraica que conecta estas distancias. Dado que la verificación numérica es consistente y el análisis es sólido, el resultado es correcto.

**Paso 120: Respuesta final**

$$\boxed{\frac{97 - 3\sqrt{1001}}{2}}$$

Equivalentemente, $\boxed{\frac{97 - \sqrt{9009}}{2}}$.

Voy a dejar esta como la respuesta final.Voy a resolver el problema paso a paso.

**Paso 1: Configuración del problema**

Coloquemos la circunferencia con centro<tool_use>
<invoke name="bash">
<parameter name="command" string="true">python3 - <<'PY'
import sympy as sp

a = sp.sqrt(231)
b = sp.sqrt(351)

def s(x): return sp.simplify(x)

# points
A = sp.Point(-10,0)
B = sp.Point(10,0)
xc = sp.Rational(31,20); yc = 13*a/20
xd = sp.Rational(-151,20); yd = 7*b/20
C = sp.Point(xc,yc)
D = sp.Point(xd,yd)

# E intersection of lines BC and AD
m1 = yc/(xc-10)   # slope BC
m2 = yd/(xd+10)   # slope AD
# param lines
# BC: B + lam(C-B); AD: A + mu(D-A)
v1x = xc-10; v1y = yc
v2x = xd+10; v2y = yd
# solve B + lam*v1 = A + mu*v2
lam, mu = sp.symbols('lam mu')
sol = sp.solve([sp.Eq(10 + lam*v1x, -10 + mu*v2x), sp.Eq(lam*v1y, mu*v2y)], [lam,mu], dict=True)[0]
lamE = sp.simplify(sol[lam]); muE = sp.simplify(sol[mu])
Ex = sp.simplify(10 + lamE*v1x); Ey = sp.simplify(lamE*v1y)
E = sp.Point(Ex,Ey)
print('lambda E (B->C scale):', lamE, '=', sp.nsimplify(lamE.evalf()))
print('muE:', muE)
print('E:', Ex.simplify(), Ey.simplify(), Ex.evalf(), Ey.evalf())

# side lengths of triangle ECD
# EC, ED, CD
EC = sp.simplify(sp.distance(E,C))
ED = sp.simplify(sp.distance(E,D))
CD = sp.simplify(sp.distance(C,D))
print('EC=', sp.simplify(EC), '=', EC.evalf())
print('ED=', sp.simplify(ED), '=', ED.evalf())
print('CD=', sp.simplify(CD), '=', CD.evalf())

# excenter opposite E: L = (-a*E + b*C + c*D)/( -a + b + c) where a=CD (opp E), b=ED(opp C), c=EC(opp D)
aa = CD; bb = ED; cc = EC
den = sp.simplify(-aa + bb + cc)
Lx = sp.simplify((-aa*Ex + bb*xc + cc*xd)/den)
Ly = sp.simplify((-aa*Ey + bb*yc + cc*yd)/den)
print('den=', den, den.evalf())
print('Lx=', sp.simplify(Lx), '=', Lx.evalf())
print('Ly=', sp.simplify(Ly), '=', Ly.evalf())
OL = sp.simplify(sp.sqrt(Lx**2 + Ly**2))
print('OL=', sp.simplify(OL), '=', OL.evalf())
# try radsimp / nsimplify guesses
print('Lx simplified:', sp.radsimp(Lx), sp.nsimplify(Lx.evalf(), [sp.sqrt(231),sp.sqrt(351),sp.sqrt(1001),sp.sqrt(13),sp.sqrt(39),sp.sqrt(3)]))
print('OL guess:', sp.nsimplify(OL.evalf(), [sp.sqrt(231),sp.sqrt(351),sp.sqrt(1001),sp.sqrt(13),sp.sqrt(39),sp.sqrt(3)]))
PY</parameter>
</invoke>
</tool_use>