Voy a resolverlo analíticamente.

En el triángulo mediano $DEF$, los vértices son los puntos medios. Por el teorema de los puntos medios, $\triangle DEF$ es semejante a $\triangle ABC$, con lados paralelos a los de $ABC$.

Los ángulos de $\triangle ABC$ son:
- $\angle A = 84^\circ$
- $\angle B = 60^\circ$
- $\angle C = 36^\circ$

Como $D$, $E$, $F$ son puntos medios:
- $D$ es el punto medio de $BC$
- $E$ es el punto medio de $AC$
- $F$ es el punto medio de $AB$

Entonces $DE \parallel AB$, $EF \parallel BC$, $DF \parallel AC$.

Los ángulos de $\triangle DEF$:
- $\angle D = \angle A = 84^\circ$ (pues $DE \parallel AB$ y $DF \parallel AC$)
- $\angle E = \angle B = 60^\circ$
- $\angle F = \angle C = 36^\circ$

**Ahora los puntos de intersección:**

La circunferencia circunscrita de $\triangle DEF$ (círculo de los nueve puntos de $\triangle ABC$) interseca a $BD$, $AE$, $AF$.

**Punto $G$:** está en $BD$ (la mediana desde $B$). Como $BD$ es una mediana, y el círculo de nueve puntos interseca la mediana en $D$ y en otro punto $G$. $G$ es el punto medio de $BH$ donde $H$ es el ortocentro... pero mejor uso ángulos.

En el círculo de nueve puntos, el punto $D$ es el punto medio de $BC$. La recta $BD$ es la mediana. El punto $G$ es el punto medio del segmento desde $B$ hasta el ortocentro (propiedad del círculo de nueve puntos). Llamo $O$ al circuncentro de $ABC$ y $H_o$ al ortocentro.

Puntos del círculo de nueve puntos sobre las medianas:
- $G$ es el punto medio de $BH_o$ (sobre mediana desde $B$)
- $H$ es el punto medio de $AH_o$ (sobre mediana desde $A$)
- $J$ es el punto medio de $CH_o$... espera, $J$ está en $AF$, y $AF$ es la mediana desde $A$ hacia $BC$. Hmm, $J$ está en $AF$.

Déjame verificar: $AF$ es la mediana desde $A$ al lado $BC$ (punto medio $F$ de $AB$? No).

Espera, releo: $D$, $E$, $F$ son puntos medios de $BC$, $AC$, $AB$ respectivamente. Entonces:
- $D$: punto medio de $BC$
- $E$: punto medio de $AC$  
- $F$: punto medio de $AB$

$BD$ es la mediana desde $B$ al lado $AC$... no, $BD$ conecta $B$ con el punto medio de $BC$, que es $D$. Entonces $BD$ es la mitad del lado $BC$.

$AE$ conecta $A$ con el punto medio de $AC$; es la mitad del lado $AC$.

$AF$ conecta $A$ con el punto medio de $AB$; es la mitad del lado $AB$.

Así que los tres segmentos $BD$, $AE$, $AF$ son mitades de lados.

La circunferencia de $DEF$ (círculo de nueve puntos) interseca a $BD$ en $D$ y $G$. De manera similar, interseca $AE$ en $E$ y $H$, e interseca $AF$ en $F$ y $J$.

El círculo de nueve puntos pasa por los puntos medios de los tres lados: $D$, $E$, $F$. También pasa por los pies de las alturas y por los puntos medios entre los vértices y el ortocentro.

**Punto $G$ en $BD$:** $BD$ está sobre el lado $BC$. El círculo de nueve puntos interseca el lado $BC$ en $D$ y en el pie de la altura desde $A$. Como $BD$ es la mitad del lado $BC$, y el pie de la altura desde $A$ cae en algún punto de $BC$. Entonces $G$ es el pie de la altura desde $A$ sobre $BC$.

En efecto: el pie de la altura desde $A$ a $BC$ está en el círculo de nueve puntos y está en el lado $BC$ (no el segmento $BD$ necesariamente). En el problema se dice que interseca a $\overline{BD}$, o sea al segmento $BD$ (la mitad izquierda de $BC$ si $D$ está en el medio).

Con $\angle B = 60^\circ$, $\angle C = 36^\circ$, el pie de la altura desde $A$ está dentro del segmento $BC$. Además, como $\angle B < 90^\circ$ y $\angle C < 90^\circ$, el pie está entre $B$ y $C$. ¿Está entre $B$ y $D$? Depende de los segmentos. La distancia desde $B$ al pie de la altura: $BF_p = AB \cos 60^\circ = AB/2$. La distancia $BD = BC/2$.

Por ley de senos, $AB/BC = \sin 36^\circ / \sin 84^\circ$. Numéricamente, $\sin 36^\circ \approx 0.5878$, $\sin 84^\circ \approx 0.9945$, entonces $AB/BC \approx 0.591$. Luego $BF_p = AB/2 \approx 0.2955 \, BC$, y $BD = BC/2 = 0.5\, BC$. Así que el pie está entre $B$ y $D$. Entonces $G$ es el pie de la altura desde $A$.

**Punto $H$ en $AE$:** $AE$ está sobre el lado $AC$. El círculo de nueve puntos interseca $AC$ en $E$ y en el pie de la altura desde $B$ sobre $AC$. Entonces $H$ es el pie de la altura desde $B$.

**Punto $J$ en $AF$:** $AF$ está sobre el lado $AB$. La intersección es $F$ y el pie de la altura desde $C$ sobre $AB$. Entonces $J$ es el pie de la altura desde $C$.

Esto encaja con la propiedad: el círculo de nueve puntos pasa por los pies de las alturas.

Entonces el hexágono $G, D, E, H, J, F$ sobre el círculo de nueve puntos es el triángulo órtico $GHJ$ (triángulo prédal) junto con los puntos medios $D, E, F$.

**Cálculo de ángulos en la circunferencia:**

El círculo de nueve puntos es homotético al circuncírculo de $ABC$ con razón $1/2$ desde el ortocentro. Los arcos en el círculo de nueve puntos tienen las mismas medidas angulares (en grados) que los arcos correspondientes en el circuncírculo, porque la homotecia preserva ángulos.

Entonces trabajo con el circuncírculo de $ABC$. Los ángulos centrales correspondientes a arcos:
- Arco menor $BC$ (opuesto a $\angle A$) mide $2 \cdot \angle A = 168^\circ$
- Arco menor $CA$ mide $2 \cdot \angle B = 120^\circ$
- Arco menor $AB$ mide $2 \cdot \angle C = 72^\circ$

En el circuito ordenado $A, B, C$, tenemos los arcos $AB = 72^\circ$, $BC = 168^\circ$, $CA = 120^\circ$ (todos menores, suman $360^\circ$).

**Orden de puntos en el círculo de nueve puntos:**

En el círculo de nueve puntos, los puntos son imágenes bajo homotecia de razón $1/2$ centrada en el ortocentro. Los puntos $D, E, F$ son imágenes de los puntos medios, que corresponden... mejor pensar directo en el círculo de nueve puntos.

El círculo de nueve puntos pasa por los 9 puntos: $D, E, F$ (puntos medios), $G, H, J$ (pies de altura), y los tres puntos medios entre vértices y ortocentro.

El triángulo órtico $GHJ$ (pies de alturas) tiene ángulos:
Los ángulos del triángulo órtico:
- El ángulo en el pie de la altura desde $A$ (punto $G$): $\angle H G J = 180^\circ - 2\angle A = 180^\circ - 168^\circ = 12^\circ$. Espera, hay fórmula.

Para el triángulo órtico (con triángulo acutángulo), los ángulos son:
- Ángulo en el pie desde $A$: $\pi - 2A = 180^\circ - 168^\circ = 12^\circ$
- Ángulo en el pie desde $B$ (punto $H$): $\pi - 2B = 180^\circ - 120^\circ = 60^\circ$
- Ángulo en el pie desde $C$ (punto $J$): $\pi - 2C = 180^\circ - 72^\circ = 108^\circ$

Esto da suma $12 + 60 + 108 = 180^\circ$. Correcto.

**Arcos del hexágono en el círculo de nueve puntos:**

Los arcos entre puntos sobre el círculo: los seis puntos $D, E, H, J, F, G$. El enunciado dice que se dividen en seis arcos menores en el orden $G, D, E, H, J, F$ (según la figura).

Necesito las medidas de los arcos $\wideparen{DE}$, $\wideparen{HJ}$, $\wideparen{FG}$.

El ángulo inscrito que subtiende cada arco será útil. Alternativamente uso el circuncírculo grande y luego reduzco.

El círculo de nueve puntos es homotético al circuncírculo con centro en el ortocentro y factor $1/2$. Bajo esta homotecia:
- $D$ → el punto medio de $BC$ → en el circuncírculo, $D$ es la imagen del punto $D'$ donde $D'$ es el punto medio del arco... mejor, la homotecia inversa (factor 2 desde $H_o$) mapea el círculo de nueve puntos al circuncírculo.

$D$ (punto medio de $BC$): su imagen bajo la homotecia inversa es el punto $D'$ sobre el circuncírculo tal que $H_o D' = 2 H_o D$. Como $D$ es el punto medio de $BC$, y el ortocentro $H_o$ tiene cierta relación.

Esto se complica. Enfoque alternativo directo: uso propiedades del círculo de nueve puntos y ángulos inscritos.

**Ángulos inscritos en el círculo de nueve puntos:**

Por la homotecia, la tangente al círculo de nueve puntos en un punto medio es paralela al lado correspondiente del triángulo órtico... Alternativa estándar: los arcos del círculo de nueve puntos corresponden a ángulos en el triángulo de nueve puntos.

Déjame usar coordenadas o fórmulas conocidas.

**Propiedades conocidas del círculo de nueve puntos:**

El círculo de nueve puntos es homotético al circuncírculo con centro en el ortocentro $H_o$, factor $1/2$. Bajo homotecia inversa factor 2:
- El punto $D$ (punto medio de $BC$) se mapea a un punto $D'$ del circuncírculo que satisface $D' = H_o + 2(D - H_o) = 2D - H_o$.

Como $D = (B+C)/2$, $D' = B + C - H_o$. Pero $B + C - H_o$ en la geometría del circuncírculo: el reflejo del ortocentro sobre $BC$ cae en el circuncírculo. También el punto diametralmente opuesto a $A$ es $B + C - H_o$ (en coordenadas con circuncentro en origen). En efecto, el antípoda de $A$ respecto al circuncentro $O$ es $-A$, y se sabe $A+B+C = H_o$ (si $O$ en origen). Entonces $D' = B+C-H_o = -A$. 

Entonces $D'$ es el antípoda de $A$ en el circuncírculo.

De manera similar:
- $E = (A+C)/2$ → $E' = A + C - H_o = -B$, antípoda de $B$.
- $F = (A+B)/2$ → $F' = A + B - H_o = -C$, antípoda de $C$.

Para los pies de las alturas:
- $G$ es el pie desde $A$ sobre $BC$. Su imagen $G' = 2G - H_o$. Por propiedades, el pie de la altura $G$ es el punto medio de $H_o$ y el reflejo de $H_o$ en $BC$, digamos $H_{oB}$. El reflejo de $H_o$ en $BC$ cae en el circuncírculo, en un punto que llamo $P_A$ (reflejo del ortocentro sobre el lado $BC$). Se sabe $G = (H_o + P_A)/2$, luego $G' = P_A$, que está en el circuncírculo.

$P_A$ es el reflejo del ortocentro en $BC$. Sus propiedades angulares: el arco $BP_A =$ ... El reflejo del ortocentro sobre $BC$ es el punto en el circuncírculo tal que $\angle BAP_A = \angle CA P_A$... más simple: $P_A$ es el punto del circuncírculo diametralmente opuesto a... El reflejo de $H_o$ en $BC$ es el punto del circuncírculo con $\angle P_A BC = \angle P_A CB = 90^\circ - \angle A$? 

Recordatorio: el reflejo del ortocentro sobre el lado $BC$ es el punto del circuncírculo que satisface $\angle P_A B C = \angle H_o B C = 90^\circ - C$ (pues $H_o B$ es perpendicular a $AC$). En efecto, $H_o B \perp AC$, entonces $\angle H_o B C = 90^\circ - C$. Reflejando, $P_A B$ forma el mismo ángulo con $BC$ hacia abajo: $\angle P_A B C = 90^\circ - C$... Hmm, déjame verificar con vectores.

Alternativa más sencilla: el punto $P_A$ (reflejo del ortocentro en $BC$) tiene la propiedad de que los arcos $\widehat{BP_A} = 2\angle C$? No, calculemos.

En el circuncírculo, el ángulo $\angle B A P_A$: dado que $A, B, C, P_A$ son concíclicos, $\angle B A P_A = \angle B C P_A$ (mismo arco $BP_A$). El punto $P_A$ es el reflejo de $H_o$ en la recta $BC$; entonces $P_A$ y $H_o$ están en lados opuestos de $BC$. El ángulo $\angle B C H_o$: $CH_o \perp AB$, entonces $\angle B C H_o = 90^\circ - B$. Reflejando, $\angle B C P_A = -(90^\circ - B)$ o $\angle B C P_A = 90^\circ - B$ en el otro sentido.

Estoy dando vueltas. Voy a una construcción numérica o uso resultados estándar de arcos del círculo de nueve puntos.

**Resultado estándar:** En el círculo de nueve puntos, los seis puntos alternan: punto medio y pie de altura. La sucesión de arcos en el círculo de nueve puntos para un triángulo agudo viene dada por $180^\circ - 2A$, $180^\circ - 2B$, $180^\circ - 2C$, y estos son los arcos entre pies de altura (lados del triángulo órtico). Los arcos entre un punto medio y el pie vecino son $\angle A$, etc.

Mejor modelo el orden.

**Orden en el círculo de nueve puntos.** Tomo el circuncírculo grande y aplico la homotecia inversa (factor 2, centro en $H_o$). El orden de los puntos en el círculo de nueve puntos es el mismo que el orden de sus imágenes $D' = -A$, $E' = -B$, $F' = -C$, $G' = P_A$, $H' = P_B$, $J' = P_C$ en el circuncírculo.

Dado que en el circuncírculo el orden horario es $A, B, C$, sus antípodas $(-A, -B, -C)$ también están en orden: $-A, -B, -C$ (orden preservado por simetría central). En el problema, el orden es $D, E, F$ → corresponden a $-A, -B, -C$.

Espera, la homotecia de razón 2 centrada en $H_o$ mapea el círculo de nueve puntos al circuncírculo de forma que $D \mapsto -A$, $E \mapsto -B$, $F \mapsto -C$. El orden de $D, E, F$ es el orden de $-A, -B, -C$.

La figura muestra el hexágono en orden $G, D, E, H, J, F$ (el enunciado: "The points $G$, $D$, $E$, $H$, $J$, and $F$ divide the circumcircle... into six minor arcs, as shown"). Espero que sea una secuencia cíclica, típicamente en sentido horario o antihorario: $G \to D \to E \to H \to J \to F \to G$.

Si el orden de $D, E, F$ corresponde a $-A, -B, -C$ sucesivamente, entonces en el circuncírculo: $-A, P_A, -B, P_B, -C, P_C$? Necesito ubicar los reflejos $P_A, P_B, P_C$.

El reflejo $P_A$ del ortocentro en $BC$: ¿dónde está respecto a $-A$? 

En el circuncírculo, para el triángulo con ángulos $A=84^\circ, B=60^\circ, C=36^\circ$:

Angulos centrales (arco menor):
- $\widehat{AB} = 72^\circ$ (arco de $A$ a $B$ que no contiene $C$)
- $\widehat{BC} = 168^\circ$
- $\widehat{CA} = 120^\circ$

Ubico $A$ en $0^\circ$, entonces $B$ en $72^\circ$, $C$ en $72+168 = 240^\circ$ (el arco $CA$ es de $C=240^\circ$ a $A=360^\circ$, que mide $120^\circ$; correcto).

Antípodas: $-A$ en $180^\circ$, $-B$ en $252^\circ$, $-C$ en $60^\circ$.

Reflejo del ortocentro en $BC$ ($P_A$): el punto $P_A$ cumple que la recta $BC$ es la mediatriz de $H_o P_A$? No, es el reflejo, así que $BC$ es la perpendicular bisectriz del segmento $H_o P_A$.

Para ubicar $P_A$: $P_A$ está en el circuncírculo y $\angle B A P_A = \angle B C P_A$. Como $P_A$ es reflejo de $H_o$ en $BC$: el triángulo $BH_oC$ tiene ángulos: en $B$: $90^\circ - C = 54^\circ$, en $C$: $90^\circ - B = 30^\circ$, en $H_o$: $180 - 54 - 30 = 96^\circ$... realmente $\angle B H_o C = 180^\circ - A = 96^\circ$. Correcto.

Reflejando $H_o$ sobre $BC$ a $P_A$, el cuadrilátero $B H_o C P_A$ es simétrico respecto a $BC$. Así $\angle C B P_A = \angle C B H_o = 54^\circ$ (en el otro lado de $BC$) y $\angle B C P_A = \angle B C H_o = 30^\circ$.

Ahora, en el circuncírculo, $\angle C B P_A$ es un ángulo inscrito que subtiende el arco $C P_A$. Entonces arco $C P_A = 2 \cdot 54^\circ = 108^\circ$.

Con $C$ en $240^\circ$, y el arco menor de $C$ a $P_A$ mide $108^\circ$. ¿Hacia qué lado? $P_A$ es el reflejo de $H_o$ en $BC$; $H_o$ está en el interior del triángulo para un triángulo agudo, así que $P_A$ está al otro lado de $BC$ (fuera del triángulo). El circuncírculo entre $B$ y $C$: el arco mayor $BC$ (que contiene a $A$ y mide $192^\circ$) está del lado de $A$; el arco menor $BC$ (168°) no contiene a $A$. $P_A$ está del lado de $BC$ opuesto a $A$, o sea en el arco menor $BC$. Entonces $P_A$ está en el arco menor $BC$.

Arco menor $BC$ va de $B=72^\circ$ a $C=240^\circ$ (sentido antihorario, pasando por 180°). $P_A$ con $\widehat{CP_A} = 108^\circ$ — pero en arco menor $BC$ el punto $P_A$ debe estar entre $B$ y $C$: arco $B P_A + P_A C = 168^\circ$. Si $\widehat{P_A C} = 108^\circ$ (arco menor), entonces arco $B P_A = 60^\circ$. Entonces $P_A$ está en $72+60 = 132^\circ$.

Chequeo: $\angle C B P_A = 54^\circ$ subtende arco $CP_A = 108^\circ$. Con $P_A$ en 132°, arco de $C=240°$ a $P_A=132°$ es $108°$. ✓.

Así $P_A$ en $132^\circ$. Nota: $P_A$ está entre $B=72°$ y $-A=180°$.

Reflejo del ortocentro en $CA$ ($P_B$): $\angle A C P_B = \angle A C H_o$. $H_o C \perp AB$, $\angle A C H_o = 90^\circ - A = 6^\circ$. Entonces arco $A P_B = 2 \cdot 6^\circ = 12^\circ$. $P_B$ está del lado de $CA$ opuesto a $B$, o sea en el arco menor $CA$ (que va de $C=240°$ a $A=360°$, mide 120°).

$P_B$ en arco menor $CA$: con arco $A P_B = 12^\circ$, $P_B$ en $360 - 12 = 348^\circ$ (pues moviéndonos desde $A=360°$ hacia atrás hacia $C$). Entonces $P_B$ en $348°$. Chequeo: arco $C P_B = 348 - 240 = 108°$, y $\angle C A P_B$ subtendería $CP_B = 108°$, ángulo $54°$... estoy mezclando; verifiquemos con el ángulo correcto.

$\angle P_B C A$: $CH_o \perp AB$, entonces $\angle A C H_o = 90° - A = 6°$? El ángulo entre $CA$ y $CH_o$: $CH_o \perp AB$, y el ángulo entre $CA$ y $AB$ es $A = 84°$, entonces el ángulo entre $CA$ y la perpendicular a $AB$ es $90° - 84° = 6°$. Sí.

Entonces $\angle A C P_B = 6°$, que subtiende arco $A P_B = 12°$. ✓. Posición $348°$ (arco de $A$ a $P_B$ mide $360-348=12°$ en sentido antihorario).

Reflejo del ortocentro en $AB$ ($P_C$): $P_C$ está en el arco menor $AB$ (opuesto a $C$). $\angle C B P_C$... el ángulo entre $AB$ y $BH_o$: $BH_o \perp AC$, entonces $\angle A B H_o = 90° - A = 6°$, y como $H_o$ reflejado en $AB$, $\angle B A P_C = 6°$? El pie $J$ corresponde al pie de la altura desde $C$ sobre $AB$. El punto $P_C$ está en el arco menor $AB$.

Arco $A P_C = 2 \angle A B P_C$. El ángulo $\angle A B P_C = \angle A B H_o$? Reflejando sobre $AB$, el ángulo $\angle A B P_C = \angle A B H_o$ pero hacia abajo. $BH_o \perp AC$, entonces $\angle A B H_o = 90° - A = 6°$. Entonces arco $A P_C = 12°$, $P_C$ en $12°$ (desde $A=0°$ hacia $B=72°$).

Entonces posiciones:
- $A = 0°$
- $P_C = 12°$ (reflejo ortocentro en AB, imagen de $J$)
- $B = 72°$
- $P_A = 132°$ (reflejo en BC, imagen de $G$)
- $-A = 180°$ (imagen de $D$)
- $C = 240°$
- $-B = 252°$ (imagen de $E$)
- $P_B = 348°$ (reflejo en CA, imagen de $H$)
- $-C = 60°$ (imagen de $F$)

Espera, hay inconsistencia: necesito ordenar correctamente. Debería tener los seis puntos de interés en orden alrededor del circuncírculo: $D'=-A$, $E'=-B$, $F'=-C$, $G'=P_A$, $H'=P_B$, $J'=P_C$.

Las posiciones:
- $P_C$ (=$J'$): $12°$
- $-C$ (=$F'$): $60°$
- $B$: $72°$
- $P_A$ (=$G'$): $132°$
- $-A$ (=$D'$): $180°$
- $C$: $240°$
- $-B$ (=$E'$): $252°$
- $P_B$ (=$H'$): $348°$
- $A$: $0°/360°$

Orden cíclico antihorario de los seis puntos relevantes:
$J'$ (12°), $F'$ (60°), $G'$ (132°), $D'$ (180°), $E'$ (252°), $H'$ (348°), y de vuelta a $J'$.

Es decir: $J', F', G', D', E', H'$ en sentido antihorario. En sentido horario sería $J', H', E', D', G', F'$.

El enunciado dice orden $G, D, E, H, J, F$ (según la figura). Miremos: según figura, en el círculo, en sentido horario desde arriba: $H$ (arriba), $J$ (arriba izquierda), $F$ (izquierda... $J$ arriba izquierda, $F$ izquierda), $G$ (abajo izquierda), $D$ (abajo centro), $E$ (derecha). Entonces sentido horario: $H, J, F, G, D, E$ (desde arriba). El enunciado lista $G, D, E, H, J, F$ que es el mismo ciclo comenzando en $G$: $G, D, E, H, J, F$ (en sentido antihorario: $G \to D \to E$).

Verifiquemos con mis posiciones en sentido antihorario: $J' (12°), F' (60°), G' (132°), D' (180°), E' (252°), H' (348°)$. El ciclo antihorario es $J' \to F' \to G' \to D' \to E' \to H' \to J'$.

La figura lista $G, D, E, H, J, F$: esto es el ciclo $G \to D \to E \to H \to J \to F \to G$. En mis posiciones: $G'(132°) \to D'(180°) \to E'(252°) \to H'(348°) \to J'(12°) \to F'(60°) \to G'$. Sí, esto es antihorario y coincide. 

**Arcos solicitados:**

$\wideparen{DE}$: corresponde a $\wideparen{D'E'}$ en el circuncírculo: de $D'=180°$ a $E'=252°$, mide $72°$.

$\wideparen{HJ}$: de $H'=348°$ a $J'=12°$ (pasando por 360°/0°), mide $360 - 348 + 12 = 24°$.

$\wideparen{FG}$: de $F'=60°$ a $G'=132°$, mide $72°$.

Pero los arcos en el círculo de nueve puntos: la homotecia de razón $1/2$ preserva ángulos, así que los arcos en el círculo de nueve puntos tienen las mismas medidas en grados (los ángulos centrales son los mismos; la longitud de arco es la mitad, pero la medida angular es idéntica).

Entonces:
- $\wideparen{DE} = 72°$
- $\wideparen{HJ} = 24°$
- $\wideparen{FG} = 72°$

La expresión: $72 + 2 \cdot 24 + 3 \cdot 72 = 72 + 48 + 216 = 336$.

Espera, déjame verificar el arco $DE$: $D'=-A$ en $180°$ y $E'=-B$ en $252°$. La diferencia es $72°$ = $2C = 2\cdot36°$. Correcto, tiene sentido: el arco $DE$ corresponde a la cuerda $DE$ que es paralela a $AB$, arco $2C = 72°$.

Arco $HJ$: $H'=P_B$ en $348°$ y $J'=P_C$ en $12°$, arco $24°$. Hmm, esto es $2A + 2C - 180$... mejor verificar. La cuerda $HJ$ es el lado del triángulo órtico que está en el lado... $H$ pie desde $B$, $J$ pie desde $C$. En el circuncírculo, $P_B$ y $P_C$ son reflejos del ortocentro en $CA$ y $AB$. El arco entre $P_B$ (348°) y $P_C$ (12°) es 24°.

Verificación con fórmula del triángulo órtico: el ángulo inscrito $\angle P_B P_C ...$, no importa; el arco $P_B P_C$ debería satisfacer... La distancia angular entre $P_B$ y $P_C$: $P_B$ en $348°$, $P_C$ en $12°$. Diferencia $24°$. $2A - 2$... $2 \cdot 84 - 2\cdot 72...$; mejor fórmula: $2A + 2B + 2C = 360°$. Los puntos $P_B$ y $P_C$ subtenden el arco $2A - 2\cdot?$... 

Realmente voy a verificar con la construcción: los pies de altura desde $B$ y $C$. El punto $H$ (pie desde $B$ en $AC$) y $J$ (pie desde $C$ en $AB$). En el círculo de nueve puntos, el arco $HJ$ debería ser el doble del ángulo $HDJ$... otra forma: en el círculo de nueve puntos, el ángulo $\angle H D J$ con $D$ el punto medio de $BC$.

Ángulo $\angle H A J$? Hmm. $H$ está en $AC$, $J$ está en $AB$. El ángulo subtendido por arco $HJ$ en el punto $D$: $\angle H D J$. $D$ es punto medio de $BC$. $H$ en $AC$ y $J$ en $AB$.

De hecho el ángulo $\angle H D J$: $D$ en $BC$, los segmentos $DH$ y $DJ$... El ángulo $HDJ$ es el ángulo entre $DH$ y $DJ$.

Por el teorema del punto medio: $D$ punto medio de $BC$, $H$ pie de altura desde $B$ (en $AC$), $J$ pie de altura desde $C$ (en $AB$).

Hay una propiedad: el cuadrilátero $D H D'...$ Mejor, uso coordenadas o simetrías.

Alternativamente, verifico usando el hecho de que el triángulo órtico tiene ángulos $12°, 60°, 108°$. En el círculo de nueve puntos, el arco $HJ$ subtendido por el ángulo... El arco $HJ$ (lado del triángulo órtico entre pies desde $B$ y $C$): el ángulo opuesto en el triángulo órtico es el ángulo en $G$ (pie desde $A$), que mide $180° - 2A = 12°$. Entonces el arco $HJ$ (el que NO contiene a $G$) mide $2 \cdot 12° = 24°$, y el arco mayor $HJ$ mide $336°$. Como estamos hablando de arcos menores del hexágono, $\wideparen{HJ} = 24°$. ✓ Coincide con mi cálculo.

De manera similar, el arco $DE$: cuerda entre punto medio $D$ de $BC$ y punto medio $E$ de $AC$. $DE \parallel AB$. El ángulo subtendido por el arco $DE$: para $F$ en el círculo, $\angle D F E = \angle D F E$? Como $DF \parallel AC$ y $FE \parallel BC$, $\angle DFE = \angle C = 36°$. Entonces el arco $DE$ (que no contiene a $F$) mide $2 \cdot 36° = 72°$. ✓ Coincide.

Arco $FG$: cuerda entre $F$ (punto medio de $AB$) y $G$ (pie de altura desde $A$ en $BC$). El ángulo subtendido: necesito el ángulo inscrito que subtiende $FG$. Por ejemplo en $H$ o $E$: $\angle F H G$. Alternativamente, del cálculo anterior obtuvimos $72°$. Verifiquemos: arco menor $FG = 72°$, entonces ángulo subtendido $36°$. El ángulo que subtiende $FG$ desde $D$: $\angle F D G$. $F$ punto medio de $BA$, $G$ pie de altura desde $A$, $D$ punto medio de $BC$.

$DG$ y $DF$: $DF \parallel AC$ (línea media). $DG$: segmento desde $D$ hasta el pie $G$ en $BC$; $DG$ está sobre $BC$. Así $\angle F D G$ es el ángulo entre $DF$ (que es $\parallel AC$) y $BC$ (que es $DG$). El ángulo entre $AC$ y $BC$ es $\angle C = 36°$. Entonces $\angle F D G = 36°$. Esto subtendería el arco $FG$ = $72°$. ✓.

Todo consistente.

**Entonces:**
$\wideparen{DE} + 2 \cdot \wideparen{HJ} + 3 \cdot \wideparen{FG} = 72 + 2(24) + 3(72) = 72 + 48 + 216 = 336$.

Hmm, quiero verificar $\wideparen{HJ}$ una vez más porque es pequeño y clave.

En el circuncírculo, $P_B$ (reflejo de $H_o$ en $CA$) y $P_C$ (reflejo en $AB$). Calculé $P_B$ en $348°$ y $P_C$ en $12°$. 

Reviso $P_B$: reflejo del ortocentro en el lado $CA$. El ángulo $\angle C A H_o$: $AH_o \perp BC$? No, $A H_o$ es perpendicular a $BC$ (es la altura desde $A$). Y $CH_o \perp AB$. Entonces el ángulo entre $CA$ y $AH_o$: $AH_o \perp BC$, ángulo entre $CA$ y $BC$ es $C=36°$, entonces ángulo entre $CA$ y $AH_o$ es $90° - 36° = 54°$. Hmm, aquí hay una confusión.

Déjame ser cuidadoso. El reflejo del ortocentro en el lado $CA$: el punto $P_B$ está en el circuncírculo, y $\angle A C P_B = \angle A C H_o$ (ambos ángulos entre el rayo $CA$ y la línea a $P_B$ / $H_o$).

¿Cuál es $\angle A C H_o$? $CH_o$ es perpendicular a $AB$. El ángulo entre $CA$ (rayo de $C$ a $A$) y la recta $CH_o$ (que es perpendicular a $AB$): la recta $AB$ forma con $CA$ un ángulo $A = 84°$. Entonces la perpendicular a $AB$ forma con $CA$ un ángulo $90° - 84° = 6°$. Entonces $\angle A C H_o = 6°$. Por tanto arco $A P_B = 12°$, y $P_B$ está en $360° - 12° = 348°$ si $H_o$ está dentro del ángulo en $C$... 

$H_o$ está dentro del triángulo. En el vértice $C$, los rayos $CA$ (hacia $A$, dirección 0° respecto a la horizontal si...), pongamos en el plano: $C$ en $(6,0)$ aprox (de la figura TikZ: $C=(6,0)$, $B=(0,0)$, $A=(1.78,3.07)$). Entonces el lado $CA$ va de $C=(6,0)$ a $A=(1.78,3.07)$: dirección noroeste. El lado $CB$ va de $C=(6,0)$ a $B=(0,0)$: dirección oeste. El ángulo interior en $C$ es $36°$ (entre $CB$ oeste y $CA$ noroeste).

$CH_o$ es perpendicular a $AB$. $AB$ va de $A=(1.78,3.07)$ a $B=(0,0)$: dirección suroeste. La perpendicular a $AB$: dirección sureste-noroeste. $CH_o$ (desde $C$ hacia el interior) va hacia el noroeste. El ángulo entre $CA$ (noroeste) y $CH_o$ (noroeste, ligeramente más inclinado): pequeño, $6°$. $H_o$ está ligeramente hacia el lado $CB$ desde $CA$; reflejado en $CA$, $P_B$ está ligeramente al otro lado.

El arco $A P_B$: en el circuncírculo, $P_B$ es el reflejo. El ángulo inscrito $\angle A C P_B = 6°$ subtiende arco $A P_B$ que no contiene a $C$. Como $C$ está en el arco... en el ángulo $\angle A C P_B$, los rayos son $CA$ y $CP_B$. $P_B$ está al otro lado de $CA$ respecto a $B$, o sea en el arco menor $CA$ (el que no contiene a $B$, que mide $120°$). Entonces $P_B$ en el arco menor $CA$: sí, en $348°$ (entre $C=240°$ y $A=360°$). ✓ Coincide: arco de $A$ a $P_B$ mide $360 - 348 = 12°$. ✓

Reviso $P_C$: reflejo del ortocentro en $AB$. $\angle B A P_C = \angle B A H_o$? $AH_o \perp BC$, entonces ángulo entre $AB$ y $AH_o$: $AB$ y $BC$ forman ángulo $B = 60°$; $AH_o$ perpendicular a $BC$ forma con $AB$ un ángulo $90° - 60° = 30°$. Espera, antes dije $\angle B A P_C = 6°$; revisemos.

En el vértice $A$: rayos $AB$ (hacia $B=(0,0)$) y $AC$ (hacia $C=(6,0)$). Ángulo en $A = 84°$. Desde $A=(1.78,3.07)$: $AB$ va hacia suroeste, $AC$ hacia sureste.

$AH_o$ es perpendicular a $BC$. $BC$ es horizontal (de $(0,0)$ a $(6,0)$), entonces la perpendicular es vertical; $AH_o$ va hacia abajo (desde $A$ al interior del triángulo, hacia punto $(1.78,0)$). El ángulo entre $AB$ (suroeste) y $AH_o$ (vertical hacia abajo): la dirección de $AB$ es $70°$ al oeste del sur... El vector $B - A = (-1.78, -3.07)$; el ángulo respecto al eje vertical hacia abajo: $\tan = 1.78/3.07 = 0.58$, $\approx 30°$. Y la vertical hacia abajo forma $30°$ con $AB$? Eso daría $B=60°$; el triángulo $\triangle AB$con el pie... $(B=60°)$: en el triángulo rectángulo formado por la altura desde $A$, la hipotenusa $AB$ y el segmento $BC$. El ángulo en $B$ es $60°$, el ángulo en el pie es $90°$, el ángulo en $A$ (entre $AB$ y la altura $AH_o$) es $90° - 60° = 30°$. ✓

Entonces $\angle B A H_o = 30°$, no $6°$.

Entonces $\angle B A P_C = 30°$ (reflejo en $AB$: el ángulo entre $AB$ y $AP_C$ es el mismo que entre $AB$ y $AH_o$, pero al otro lado). Arco $B P_C = 2 \cdot 30° = 60°$ (el arco que no contiene a $A$).

$P_C$ está en el arco menor $AB$ (opuesto a $C$). Arco menor $AB$ va de $A=0°$ a $B=72°$. $P_C$ con arco $B P_C = 60°$: desde $B=72°$ hacia atrás, $P_C$ en $72 - 60 = 12°$. ✓ Coincide con mi valor anterior $12°$.

Así que $P_C$ en $12°$ está bien (aunque mi justificación previa con $6°$ era incorrecta; el resultado queda igual porque usé la ubicación correcta). Espera, verifiquemos: arco $A P_C = 12°$, arco $B P_C = 60°$, suma $72°$ ✓.

Reviso $P_A$: reflejo en $BC$. $\angle C B P_A = \angle C B H_o$. $BH_o \perp AC$, ángulo entre $BC$ y $AC$ es $36°$, entonces ángulo entre $BC$ y la perpendicular a $AC$ es $90° - 36° = 54°$. Arco $C P_A = 2 \cdot 54° = 108°$ (el que no contiene a $B$). $P_A$ en arco menor $BC$ (168°). Desde $C=240°$ hacia atrás: $240 - 108 = 132°$. ✓ Coincide.

Y también $\angle C B H_o$: en el triángulo rectángulo del pie $(C?)$... $BH_o \perp AC$, el triángulo $BC H_o$ con ángulo recto en el pie sobre $AC$? En realidad $H_o$ no está sobre $BC$; $\angle B C H_o = 90° - B = 30°$ (en $C$), y $\angle C B H_o = 90° - C = 54°$ (en $B$). Consistente. ✓

Así que mis posiciones están correctas.

Ahora, $\wideparen{HJ}$: $H' = P_B$ en $348°$, $J' = P_C$ en $12°$. Arco de $P_B$ a $P_C$ pasando por $360°$: $24°$. ✓

Pero espera, el hecho de que los arcos en el círculo de nueve puntos sean iguales a los del circuncírculo: sí, porque la homotecia (transformación de semejanza) preserva ángulos centrales. La medida de arco en grados es el ángulo central correspondiente en el centro del círculo. El centro del círculo de nueve puntos es $N$ (punto medio de $H_o$ y $O$), y bajo homotecia los ángulos se conservan. Entonces $\angle D N E$ (en el círculo de nueve puntos) es igual al ángulo $\angle D' O E'$ (en el circuncírculo)? La homotecia mapea $N \to O$, $D \to D'$, $E \to E'$, y preserva ángulos. Sí, $\angle D' O E' = \angle D N E$ porque las rectas $OD'$ y $ND$ son paralelas, y $OE'$ y $NE$ son paralelas. Entonces los arcos mide iguales. ✓

Así que la respuesta es $336$.

Déjame verificar el arco $DE$ una vez más directamente. $D$ punto medio de $BC$, $E$ punto medio de $AC$. En el círculo de nueve puntos, $\wideparen{DE}$: el ángulo central $\angle D N E$. ¿Es igual al arco entre $-A$ y $-B$ en el circuncírculo, que es el ángulo $\angle (-A) O (-B)$? El ángulo entre los rayos $O(-A)$ y $O(-B)$ es el mismo que entre $OA$ y $OB$: $\angle A O B$. Y $\angle A O B$ es el ángulo central que subtiende el arco menor $AB$, que mide $2C = 72°$. ✓

Igualmente, arco $FG$ corresponde a ángulo central entre $P_A$ (132°) y $-C$ (60°): $132 - 60 = 72°$. Coincide con $2C=72°$... hmm, $F'=-C$ y $G'=P_A$; el ángulo central entre ellos es $72°$. ✓

Arco $HJ$: $P_B$ y $P_C$: $24°$. ✓

Todo cuadra. La suma es $336$.

Espera — doble verificación del orden de los arcos en el hexágono. Necesito asegurarme de que los arcos solicitados ($DE$, $HJ$, $FG$) son los arcos menores del hexágono, no sus complementos. El problema dice "minor arcs" y el enunciado del hexágono los lista en orden; la figura confirma que son arcos menores adyacentes.

En el hexágono el orden es $G, D, E, H, J, F$ (y de vuelta a $G$). Los arcos menores adyacentes:
- $\wideparen{GD}$: $G$ (132°) a $D$ (180°): $48°$.
- $\wideparen{DE}$: $180°$ a $252°$: $72°$. ✓
- $\wideparen{EH}$: $252°$ a $348°$: $96°$.
- $\wideparen{HJ}$: $348°$ a $12°$ (vía 360°): $24°$. ✓
- $\wideparen{JF}$: $12°$ a $60°$: $48°$.
- $\wideparen{FG}$: $60°$ a $132°$: $72°$. ✓

Suma de los seis arcos menores: $48+72+96+24+48+72 = 360°$. ✓ Perfecto, consistente.

Entonces:
$72 + 2\cdot24 + 3\cdot72 = 72 + 48 + 216 = 336$.

Confirmo la respuesta final: $336$.## Resolución

El triángulo $DEF$ es el triángulo de los puntos medios, semejante a $ABC$, por lo que su circunferencia circunscrita es el **círculo de los nueve puntos** de $\triangle ABC$.

En esta circunferencia, además de los puntos medios $D$, $E$, $F$, se encuentran los pies de las alturas. Así:

- $G$ es el pie de la altura desde $A$ sobre $BC$.
- $H$ es el pie de la altura desde $B$ sobre $AC$.
- $J$ es el pie de la altura desde $C$ sobre $AB$.

El círculo de nueve puntos es homotético al circuncírculo de $ABC$ con razón $1/2$ centrada en el ortocentro, así que las medidas de los arcos (en grados) coinciden en ambas circunferencias.

Ubico los puntos en el circuncírculo tomando $A$ en $0°$ y avanzando en sentido antihorario. Con los ángulos dados $(A=84°, B=60°, C=36°)$:

- Arco menor $AB = 2C = 72°$, arco menor $BC = 2A = 168°$, arco menor $CA = 2B = 120°$.

Posiciones relevantes (con la homotecia inversa de razón 2):

- $D$ corresponde al antípoda de $A$: $180°$.
- $E$ corresponde al antípoda de $B$: $252°$.
- $F$ corresponde al antípoda de $C$: $60°$.
- $G$ corresponde al reflejo del ortocentro sobre $BC$: $132°$.
- $H$ corresponde al reflejo del ortocentro sobre $CA$: $348°$.
- $J$ corresponde al reflejo del ortocentro sobre $AB$: $12°$.

El orden cíclico del hexágono en el círculo es:

$$G\ (132°) \to D\ (180°) \to E\ (252°) \to H\ (348°) \to J\ (12°) \to F\ (60°) \to G.$$

Ahora calculo los arcos pedidos:

- $\wideparen{DE} = 252° - 180° = 72°$.
- $\wideparen{HJ} = 360° - 348° + 12° = 24°$.
- $\wideparen{FG} = 132° - 60° = 72°$.

Sustituyo en la expresión:

$$
72 + 2\cdot 24 + 3\cdot 72 = 72 + 48 + 216 = 336.
$$

$$\boxed{336}$$