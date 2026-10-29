Voy a razonar paso a paso.

Tenemos un círculo grande con centro $Q$ y radio 14. Los radios $AQ$ y $BQ$ forman un ángulo recto, es decir, forman un sector de $90^\circ$ (un cuarto de círculo).

Dentro de ese sector (la región "grande") hay dos regiones más pequeñas que son semicírculos tangentes. En este tipo de problema clásico, la disposición es: el cuarto de círculo de radio 14 contiene dos semicírculos tangentes entre sí y tangentes a los radios.

Llamemos $r$ al radio del semicírculo menor y $R$ al radio del semicírculo mayor. La configuración habitual es que el semicírculo mayor tiene su diámetro sobre un radio (por ejemplo $AQ$), y el semicírculo menor tiene su diámetro sobre el otro lado o está en la esquina.

En estos problemas, la clave es considerar un cuarto de círculo de radio $14$ que contiene dos círculos (o semicírculos) mutuamente tangentes y tangentes a los lados.

Para el caso estándar: dos círculos dentro de un cuadrante, cada uno tangente a ambos lados del cuadrante y tangentes entre sí, con radios $R$ y $r$. Si el círculo mayor es tangente a ambos lados y su centro está a distancia $R$ de cada lado, y el menor igual con $r$, la distancia entre centros debe ser $R+r$ (tangencia externa).

Los centros están en la línea $y=x$ para círculos simétricos, pero aquí no son simétricos. En la versión con semicírculos (diámetros sobre los lados), el semicírculo mayor tiene su diámetro sobre $AQ$ y es tangente a $BQ$ y al arco.

Consideremos las coordenadas: $Q=(0,0)$, $AQ$ sobre el eje $x$ de $(0,0)$ a $(14,0)$, y $BQ$ sobre el eje $y$ de $(0,0)$ a $(0,14)$.

El semicírculo mayor tiene diámetro sobre el eje $x$, desde $x=0$ hasta $x=d$, con $d=2R$. Su centro está en $(R,0)$, radio $R$. Es tangente al arco del cuarto de círculo, así que la distancia del centro al origen más el radio es $14$:
$R + QR = 14$? No; el arco está a distancia 14 del origen, y el semicírculo mayor está centrado en el eje $x$. Para ser tangente internamente al cuarto de círculo, la distancia desde $Q$ al punto más lejano del semicírculo debe ser 14.

El semicírculo mayor centrado en $(R,0)$, tangente al eje $y$ (radio $BQ$) en $x=0$, y al arco. El punto del arco tangente está a lo largo de la línea desde $Q$ al centro. La distancia del centro a $Q$ es $R$, así que la tangencia con el arco requiere:
distancia de $Q$ al centro + radio del semicírculo = radio 14
Es decir, $R + R = 14$, o sea $2R=14$, $R=7$. El semicírculo mayor tiene radio 7, diámetro 14, ocupando de $x=0$ a $x=14$ sobre el eje $x$. Eso es un semicírculo de diámetro 14 con diámetro sobre $AQ$ completo.

Ahora el semicírculo menor está en la esquina entre el eje $y$ y el semicírculo mayor, o entre el arco y el eje $y$. En la versión típica, el semicírculo menor tiene su diámetro sobre el eje $y$ y es tangente al semicírculo mayor y al arco.

Sea $r$ el radio del semicírculo menor, con centro en $(0, r)$ sobre el eje $y$, diámetro en el eje $y$ desde $(0,0)$ hasta $(0,2r)$.

El semicírculo menor es tangente al semicírculo mayor. El centro del mayor está en $(7,0)$, el menor en $(0,r)$. La distancia entre centros es $\sqrt{7^2 + r^2}$. Como son tangentes externamente (los semicírculos se tocan), $\sqrt{49 + r^2} = 7 + r$.

Elevando al cuadrado: $49 + r^2 = 49 + 14r + r^2$, lo que da $0 = 14r$, o sea $r=0$. Contradicción. Entonces el semicírculo mayor no tiene diámetro 14 completo.

Revisemos. En realidad los dos semicírculos están tangentes entre sí y tangentes a los lados. El semicírculo mayor tiene diámetro sobre el eje $x$, pero no necesariamente de longitud 14; es tangente al arco.

La condición de tangencia con el arco para el semicírculo mayor centrado en $(R,0)$: el punto del semicírculo más alejado del origen está en la dirección del centro, a distancia $R$ (centro) + $R$ (radio) = $2R$. Como el semicírculo está dentro del cuarto de círculo y es tangente al arco, $2R = 14$, luego $R=7$. Eso parece correcto, da $R=7$ con diámetro 14, tocando $Q$ y el punto $(14,0)$.

Entonces el semicírculo menor, ¿dónde está tangente? Si el mayor ocupa todo desde $x=0$ a $x=14$, el menor no cabe junto al eje $y$. El menor debe estar entre el mayor y el eje $y$ cerca del origen, pero el mayor ya toca el origen... 

Déjame reconsiderar la figura. La descripción: "Los radios $AQ$ y $BQ$ forman un ángulo recto. Las dos regiones más pequeñas son semicírculos tangentes." Probablemente la figura muestra el cuarto de círculo con dos semicírculos, uno más grande tangente a los dos radios y al arco, y otro más pequeño en la esquina, tangente a un radio, al otro semicírculo, y al arco.

Configuración alternativa: un semicírculo con diámetro sobre $AQ$, tangente a $BQ$ y al arco; otro semicírculo con diámetro sobre $BQ$, tangente a $AQ$... pero no pueden ser ambos porque se cruzarían.

Configuración clásica real (de MATHCOUNTS): un cuarto de círculo contiene dos semicírculos: el grande tiene diámetro en un radio y es tangente al arco y al otro radio; el pequeño tiene diámetro en el otro radio y es tangente al arco y al semicírculo grande.

El grande: centro en $(x_1, 0)$ con $x_1 = R$ (tangente al eje $y$ requiere centro a distancia $R$ del eje $y$, o sea $x_1=R$). Tangente al arco: $x_1 + R = 14$? El punto más lejano en dirección del origen está a lo largo de $x$. Distancia del origen al centro: $x_1 = R$. Punto más lejano: $x_1 + R = 2R = 14$, $R=7$. Otra vez $R=7$.

El pequeño sobre el eje $y$: centro $(0, r)$, tangente al arco: $2r=14$, $r=7$. Ambos de radio 7. Entonces tangencia entre ellos: distancia entre $(7,0)$ y $(0,7)$ es $7\sqrt2 \approx 9.9$, no $14$. No tangentes.

Así que no es esa configuración. Debe ser: un semicírculo grande con diámetro sobre un radio, y el pequeño también sobre el mismo radio, apilados, o el pequeño en la esquina del arco.

Otra configuración estándar: El semicírculo grande es tangente a BQ (eje y) y al arco, con diámetro sobre AQ (eje x), pero NO toca el origen; y el pequeño es tangente al eje y (o al arco) y está en la esquina.

Sea el grande con centro $(a,0)$ y radio $R=a$? No. Tangente al eje $y$ en $x=0$ si está a la izquierda del eje $y$... está dentro del cuadrante $x>0$. Un semicírculo con diámetro sobre el eje $x$ puede ser tangente al eje $y$ solo si su diámetro comienza en $x=0$. Entonces su centro está en $(R,0)$ y toca el eje y.

Hmm, reconsideremos: quizá el semicírculo mayor tiene su diámetro sobre el eje $x$ en la parte derecha y es tangente al arco y tangente al semicírculo menor, que está en la esquina inferior izquierda con diámetro sobre el eje $y$. El mayor no toca el eje $y$.

Sean: semicírculo menor, centro $(0,r)$, radio $r$, diámetro sobre eje $y$ de $0$ a $2r$. Es tangente al arco: punto más lejano a lo largo del eje $y$ debe estar a distancia 14, así que $2r=14$, $r=7$. Tampoco cabe otro.

Está claro que no puede haber dos semicírculos tangentes ambos al arco alineados con los ejes. El grande debe ser tangente al arco, y el pequeño tangente al grande y a un lado, pero no al arco. O el pequeño es tangente al arco y el grande no.

Déjame buscar la configuración real. Es el problema típico donde el semicírculo pequeño está entre el semicírculo grande y el arco, tangente a ambos radios y al semicírculo grande. Con "$AQ$ y $BQ$ forman un ángulo recto" y "dos regiones más pequeñas son semicírculos tangentes".

Configuración real (famosa, respuesta 14/3? o 7/3?): Considere el cuarto de círculo de radio 14. Un semicírculo grande cuelga del radio $AQ$ (su diámetro coincide con parte de $AQ$), tangente al arco. El otro semicírculo pequeño cuelga del radio $BQ$, tangente al arco y al semicírculo grande. Entonces el grande no toca $BQ$ y el pequeño no toca $AQ$.

El grande: diámetro sobre eje $x$, centro $(a, 0)$, radio $R$. Es tangente al arco del cuarto de círculo. El punto del arco más cercano en la dirección radial... El semicírculo está dentro del cuadrante, su "borde superior" es un arco de su propio círculo. La condición de tangencia al arco grande ($x^2+y^2=14^2$) cuando su diámetro está en el eje $x$: el punto más lejano del semicírculo respecto del origen está en la dirección $(a,0)$, a distancia $a + R$. Para tangencia, $a + R = 14$.

El pequeño: diámetro sobre el eje $y$, centro $(0, b)$, radio $r$, tangente al arco: $b + r = 14$.

Y tangentes entre sí: distancia entre centros $\sqrt{a^2 + b^2} = R + r$.

Tenemos $R = 14 - a$, $r = 14 - b$.

Además, ¿hay más restricciones? El diámetro del semicírculo está sobre el radio; el diámetro va desde el centro hasta $a+R$... el semicírculo ocupa de $x=a-R$ a $x=a+R$ en el eje $x$ (diámetro de longitud $2R$). Para estar dentro del cuadrante, $a - R \ge 0$, es decir $a \ge R$, o sea $a \ge 14 - a$, $a \ge 7$. Similarmente $b \ge 7$.

Necesitamos otra ecuación. La tangencia con el arco es interna (el semicírculo dentro del cuarto de círculo). ¿Los semicírculos son tangentes al arco exactamente en un punto? Sí, eso da dos condiciones.

Pero tenemos 4 incógnitas ($a, b, R, r$) y 3 ecuaciones (dos de tangencia al arco y una de tangencia mutua). Falta una. La condición adicional es que los semicírculos son tangentes a los radios *que forman el ángulo recto*, quizá al radio opuesto. Espera: el semicírculo con diámetro sobre $AQ$ es tangente a $BQ$ (el radio perpendicular). Eso significa que el punto más a la izquierda del semicírculo toca el eje $y$, o sea $a - R = 0$, luego $a = R$. Combinado con $a+R=14$: $2a=14$, $a=7$, $R=7$. Eso es lo de antes.

El pequeño tangente a $AQ$ (eje x): $b - r = 0$, $b=r$, con $b+r=14$ da $r=7$. De nuevo ambos 7.

Entonces no tangentes entre sí. Por tanto, tangente à ese radio no.

Vamos a mirar el problema de otro modo: quizá los dos semicírculos son tangentes entre sí y tangentes a los dos radios, y están dentro del cuarto de círculo, y ambos son tangentes al cuarto de círculo (el arco). La suma de las tangencias da el sistema correcto.

Para un semicírculo centrado en $(x, y)$ con diámetro sobre el eje $x$ (centro en $y=0$), radio $R$, tangente al arco: punto más lejano al origen a distancia $x+R = 14$? No, eso asume la dirección radial coincide con el eje $x$, lo cual es cierto solo si el centro está sobre el eje $x$. Si el centro está en $(x,0)$, el punto más lejano está en $(x+R, 0)$, distancia $x+R$. Para tangencia al arco: $x+R=14$. Correcto.

Para el pequeño centrado en $(0, y)$, tangente al arco: $y + r = 14$ (punto más lejano $(0, y+r)$).

Tangencia mutua: $\sqrt{x^2 + y^2} = R + r$.

Y las tangencias a los radios: el grande es tangente a $BQ$ (eje $y$): $x = R$. El pequeño tangente a $AQ$ (eje $x$): $y = r$. Esto da de nuevo $x=R=7$, $y=r=7$. Tangencia mutua: $\sqrt{49+49}=7\sqrt2 \neq 14$. No funciona.

Por lo tanto, debe ser: el grande tangente a $BQ$ y al arco, el pequeño tangente solo al grande y al arco (no al eje $x$), con su diámetro sobre $AQ$? O el pequeño tangente a $AQ$ y al grande.

Pruebo: grande en eje $x$, centro $(a, 0)$, tangente a $BQ$: $a=R$. Tangente al arco: $a+R=14$ ⇒ $a=R=7$.

Pequeño también en eje $x$, centro $(c, 0)$, radio $r$, a la derecha del grande, tangente al arco: $c + r = 14$. Tangente al grande: distancia $c - a = R + r$ ⇒ $c - 7 = 7 + r$ ⇒ $c = 14 + r$. Pero $c+r=14$ ⇒ $r=0$. Contradicción. No.

Pequeño a la izquierda? No hay espacio ($a=R=7$, diámetro va de $0$ a $14$).

Entonces el grande no toca $BQ$; en cambio, es tangente al arco y al pequeño, y el grande tangente a $AQ$ solo por su diámetro. Falta una condición. La condición que falta: el grande es tangente al arco en un punto donde su normal es radial, pero eso ya lo usamos.

Alternativa famosa: solo hay un semicírculo pequeño y uno grande, y el círculo grande (el cuarto de círculo) tiene radio 14. Los dos semicírculos están en la "esquina" entre los dos radios y el arco, tangentes entre sí, cada uno tangente a uno de los radios y al arco. Sus diámetros NO están sobre los radios, sino que cada centro caería en la bisectriz... pero son semicírculos, su diámetro es un segmento.

Replanteo: un semicírculo tiene su diámetro sobre el radio $AQ$; el otro sobre el radio $BQ$. El que está sobre $AQ$ es tangente al arco y tangente al otro semicírculo. El que está sobre $BQ$ es tangente a $AQ$ (no al arco) y al otro. O viceversa.

Caso: grande sobre $AQ$ (centro $(a,0)$, radio $R$), tangente al arco: $a+R=14$. Pequeño sobre $BQ$ (centro $(0,b)$, radio $r$), tangente a $AQ$ (eje $x$): $b - r \ge 0$... tangente al eje $x$ significa el diámetro del pequeño está sobre el eje $y$, y el semicírculo se extiende hacia $x>0$; ser tangente al eje $x$ (AQ) requeriría tocar $y=0$, lo que no pasa salvo que el diámetro esté en $y=0$. Un semicírculo con diámetro sobre el eje $y$ no toca el eje $x$ salvo en el origen si el diámetro incluye el origen. Entonces "el pequeño es tangente a $AQ$" significa que su diámetro sobre $BQ$ empieza en $y=0$: $b = r$. Entonces el pequeño llega hasta $y=2r$ en el eje $y$.

Entonces grande tangente al arco: $a+R=14$. Pequeño: $b=r$ (tan a $AQ$). Tangencia mutua: $\sqrt{a^2+b^2}=R+r$, con $a^2+b^2 = a^2+r^2$.

Además el grande es tangente a $BQ$? No se dijo. El pequeño es tangente al arco? No se dijo. Necesitamos otra condición. Quizá el grande es tangente a $BQ$: $a=R$, entonces $a=7$, y tangencia mutua $\sqrt{49+r^2}=7+r$ ⇒ $r=0$. No.

Quizá el pequeño es tangente al arco: $b+r=14$. Con $b=r$: $r=7$. Y tangencia mutua $\sqrt{a^2 + 49} = R + 7$, con $a+R=14$ ⇒ $a=14-R$. Y el grande tangente a $BQ$? No.

Tenemos $a+r=14$? No: pequeño tangente al arco da $b+r=14$ con $b=r$ ⇒ $r=7$. Tangencia: $\sqrt{(14-R)^2+49}=R+7$. Elevamos: $(14-R)^2 + 49 = R^2 + 14R + 49$ ⇒ $196 - 28R + R^2 + 49 = R^2 + 14R + 49$ ⇒ $196 - 28R = 14R$ ⇒ $196 = 42R$ ⇒ $R = 196/42 = 14/3$? 196/42 = 14/3 ≈ 4.667. Entonces grande radio $14/3$, y $a = 14 - 14/3 = 28/3$. Verifica tangente a $BQ$? No, $a=28/3 > R=14/3$, el diámetro va de $a-R=14/3$ a $a+R=14$: toca el arco en $x=14$ y termina el diámetro en $x=14/3$, no toca el eje $y$. Parece razonable y consistente. El pequeño radio 7, pero entonces el pequeño es más grande que el "large" — inconsistente con el lenguaje de "menor". Hmm r=7 mayor que R=14/3, entonces el pequeño sería el grande. No encaja con "radio del semicírculo menor" siendo una fracción.

Intento otra asignación: grande tangente al arco y a $BQ$; pequeño tangente al arco y a $AQ$; y mutuamente tangentes.

Grande sobre $AQ$ (eje x): tangente a $BQ$ ⇒ $a=R$; tangente al arco ⇒ $a+R=14$ ⇒ $R=7$.

Pequeño sobre $BQ$ (eje y): tangente a $AQ$ ⇒ $b=r$; tangente al arco ⇒ $b+r=14$ ⇒ $r=7$.

Mutuamente tangentes: distancia $\sqrt{49+49} = 7\sqrt2$, pero $R+r=14$. No.

Así que "grande/y tangente a un eje y al arco" no puede coexistir con "pequeño tangente al otro eje y al arco". Por tanto la configuración debe ser: grande tangente a BQ y al arco (sobre AQ); pequeño tangente SOLO al grande y a BQ, con diámetro sobre BQ, sin tocar arco. O pequeño tangente a AQ y al grande.

Caso: grande sobre AQ (centro $(R,0)$, radio $R=7$). Pequeño sobre BQ (centro $(0,r)$, radio $r$), tangente a AQ (eje x): esto solo ocurre si $r=0$ o si el centro está sobre el eje $x$; no es. Entonces el pequeño es tangente a $BQ$ por construcción (diámetro sobre $BQ$). El pequeño es tangente al grande. Esa es la configuración: dos semicírculos, grande con diámetro sobre AQ tangente al arco y a BQ; pequeño con diámetro sobre BQ, tangente al grande. ¡Y el pequeño no toca el arco ni el otro radio!

La condición de tangencia: centro pequeño $(0, r)$, grande $(7, 0)$, distancia $=7+r$:
$\sqrt{49 + r^2} = 7 + r$ ⇒ $49 + r^2 = 49 + 14r + r^2$ ⇒ $r=0$. Contradicción de nuevo.

Imposible porque el grande toca el origen (su diámetro va de $0$ a $14$), dejando cero espacio para el pequeño en la esquina. Así que el grande NO debe tocar BQ; su diámetro no empieza en $x=0$.

Configuración final plausible: el grande sobre AQ, tangente al arco (radio $R$), y tangente a BQ **pero no simultáneamente**; el pequeño sobre BQ, tangente al arco, y ambos tangentes entre sí.

Grande sobre AQ: centro $(a,0)$, tangente al arco ⇒ $a+R=14$.
Pequeño sobre BQ: centro $(0,b)$, tangente al arco ⇒ $b+r=14$.
Tangencia mutua: $\sqrt{a^2+b^2} = R+r$.

Son 3 ecuaciones, 4 incógnitas. Falta: los diámetros yacen sobre los radios, pero además cada semicírculo es tangente al OTRO radio formando el ángulo recto. Grande sobre AQ tangente a BQ ⇒ $a=R$? Eso es lo que da $R=7$ y $r=0$. Pequeño sobre BQ tangente a AQ ⇒ $b=r$, da $r=7$. Si aplicamos ambas, $R=7$, $r=7$, mutua tangencia falla.

¿Y si el grande es tangente a BQ (a=R=7) y el pequeño es tangente al arco (b+r=14) y tangente al grande? Ya vimos: tangencia da $\sqrt{49+b^2}=7+r$, con $b=14-r$: $\sqrt{49+(14-r)^2}=7+r$. Elevo: $49 + (14-r)^2 = 49 + 14r + r^2$ ⇒ $(14-r)^2 = 14r + r^2$ ⇒ $196 -28r + r^2 = 14r + r^2$ ⇒ $196 = 42r$ ⇒ $r = 196/42 = 14/3$.

¡Esta da $r = 14/3$, una fracción común razonable! Verifiquemos: grande $R=7$, centro $(7,0)$. Pequeño radio $r=14/3$, centro $(0, 14-r) = (0, 28/3)$. Tangencia mutua: distancia $\sqrt{49 + (28/3)^2} = \sqrt{49 + 784/9} = \sqrt{(441+784)/9} = \sqrt{1225/9} = 35/3$. Y $R+r = 7 + 14/3 = 21/3 + 14/3 = 35/3$. ✓. Tangente al arco: $b+r = 28/3 + 14/3 = 42/3 = 14$ ✓. Grande tangente a BQ: centro $x=7$, radio 7, diámetro de $x=0$ a $x=14$ ✓. Pero ojo: el pequeño con centro $(0, 28/3)$ y radio $14/3$ tiene su diámetro sobre el eje $y$ desde $y = 28/3 - 14/3 = 14/3$ hasta $y = 28/3 + 14/3 = 14$. Así que su diámetro NO empieza en $y=0$; no es tangente a $AQ$. Es tangente al arco y al grande, y su diámetro está sobre $BQ$. Consistente.

En esta configuración, el semicírculo grande tiene radio $7$ (diámetro 14 sobre AQ), y el pequeño radio $14/3$. El pequeño está en la parte superior, tangente al arco en el punto $(0,14)$ (el extremo de $BQ$ sobre el arco) y al semicírculo grande.

Entonces $r = 14/3$.

Esta es una respuesta de fracción común, perfecta. La respuesta es $\frac{14}{3}$.

Final: $\boxed{\frac{14}{3}}$