Vamos a resolver el problema paso a paso.

### Paso 1. Notación y dadas

Tenemos un trapecio $ABCD$ con $\overline{AD}\parallel \overline{BC}$.
Además:

- $\overline{AC}\perp \overline{CD}$, es decir, $\angle ACD = 90^\circ$.
- $\overline{AC}$ biseca $\angle BAD$, o sea, $\angle BAC = \angle CAD$.
- $[ABCD] = 42$.

Queremos $[\triangle ACD]$.

### Paso 2. Configuración de ángulos

Como $AD \parallel BC$ y $AC$ es transversal:

$$
\angle CAD = \angle ACB
$$

por ángulos alternos internos. Pero como $AC$ biseca $\angle BAD$, tenemos

$$
\angle BAC = \angle CAD.
$$

Por lo tanto,

$$
\angle BAC = \angle CAD = \angle ACB =: \theta.
$$

### Paso 3. Relación en el triángulo ABC

En $\triangle ABC$, los ángulos en $A$ y $C$ son iguales ($\angle BAC = \angle ACB = \theta$), así que $\triangle ABC$ es isósceles:

$$
AB = BC.
$$

### Paso 4. Relaciones métricas en el triángulo ACD

En $\triangle ACD$, tenemos $\angle ACD = 90^\circ$ y $\angle CAD = \theta$, entonces

$$
\angle ADC = 90^\circ - \theta.
$$

Ahora bien, como $AD \parallel BC$ y $CD$ es transversal, los ángulos $\angle ADC$ y $\angle BCD$ son suplementarios porque son ángulos consecutivos internos:

$$
\angle ADC + \angle BCD = 180^\circ.
$$

Entonces

$$
\angle BCD = 90^\circ + \theta.
$$

En el triángulo $BCD$, observamos que:

- $\angle BCD = 90^\circ + \theta$,
- $\angle BDC = \angle ADC = 90^\circ - \theta$,
- $\angle CBD = ?$

La suma da:

$$
(90^\circ + \theta) + (90^\circ - \theta) = 180^\circ.
$$

Esto significa que el tercer ángulo $\angle CBD = 0^\circ$, lo que no es posible. Por lo tanto, $B$, $C$ y $D$ no forman un triángulo; esto sugiere que $B$, $C$ y $D$ están alineados, lo que no ocurre en un trapecio.

Revisemos la configuración: en un trapecio con $AD \parallel BC$, los lados no paralelos son $AB$ y $CD$. El ángulo $\angle BCD$ es exterior al triángulo $BCD$; en realidad debemos usar que $\angle ADC$ y $\angle BCD$ miden $90^\circ-\theta$ y $90^\circ-\theta$? Veamos la orientación.

Quizá conviene pasar directamente a longitudes.

### Paso 5. Longitudes

Sea:

- $AD = a$ (base mayor),
- $BC = b$ (base menor),
- Altura del trapecio $= h$.

La diagonal $AC$ forma ángulo $\theta$ con $AD$ y con $BC$.

En $\triangle ACD$, rectángulo en $C$, con hipotenusa $AD = a$, tenemos:

$$
CD = a \sin\theta,\qquad AC = a \cos\theta.
$$

Pero en ese triángulo, $\angle CAD = \theta$ es el ángulo en $A$, y el ángulo recto está en $C$, así que:

- Cateto opuesto a $\theta$: $CD = a\sin\theta$,
- Cateto adyacente a $\theta$: $AC = a\cos\theta$.

Como $AD \parallel BC$ y $BC$ está sobre la misma horizontal, la proyección horizontal de $AC$ sobre $AD$ es $AC\cos\theta$.

De hecho, la altura del trapecio es la distancia perpendicular entre $AD$ y $BC$. En el triángulo rectángulo $ACD$, esa altura es precisamente $CD$, porque $CD$ es perpendicular a $AC$, no necesariamente a las bases. Mejor usemos otra relación.

### Paso 6. Coordenadas

Pongamos coordenadas.

Sea $D=(0,0)$, $C=(u,0)$, $A=(u,v)$, porque $\angle ACD=90^\circ$. Entonces $AC$ es vertical, $CD$ horizonal.

Entonces:

- $AD$ es la recta de $(0,0)$ a $(u,v)$.
- $BC$ es paralela a $AD$, y pasa por $C=(u,0)$.

El ángulo $\angle BAD$ es entre $BA$ y $DA$, y lo biseca $AC$, que es vertical. Por tanto, los rayos $AB$ y $AD$ son simétricos respecto a la línea vertical $AC$.

El rayo $AD$ va de $A=(u,v)$ a $D=(0,0)$; su vector es $(-u,-v)$.

Entonces el rayo $AB$, simétrico respecto a la vertical, tendrá vector $(u,-v)$.

Por lo tanto, partiendo de $A$, el punto $B$ está en la dirección $(u,-v)$:

$$
B = (u,v) + t(u,-v) = (u+ut,\; v-vt)
$$

con $t>0$.

Como $BC \parallel AD$, la dirección de $BC$ debe ser paralela a $(-u,-v)$, o equivalentemente a $(u,v)$.

El vector $BC$ es $C-B$, pero para que $B$ sea tal que $BC \parallel AD$, necesitamos que $B$ esté en la paralela a $AD$ que pasa por $C$:

Recta por $C=(u,0)$ con dirección $(-u,-v)$, que es la misma recta $AD$ desplazada.

Su ecuación paramétrica:

$$
(x,y) = (u,0) + s(-u,-v).
$$

Además, $B$ también debe estar en la recta desde $A$ en dirección $(u,-v)$:

$$
(u+ut,\; v-vt) = (u - us,\; -vs).
$$

Igualando:

- Primera coordenada: $u+ut = u-us \implies t = -s$.
- Segunda coordenada: $v - vt = -vs$. Con $s = -t$:

$$
v - vt = v t \implies v = 2vt \implies t = \frac12.
$$

Entonces $s = -\frac12$, y el punto $B$ es:

$$
B = A + \frac12(u,-v) = \left(u+\frac{u}{2},\, v-\frac{v}{2}\right) = \left(\frac{3u}{2},\, \frac{v}{2}\right).
$$

### Paso 7. Área del trapecio

Las bases $AD$ y $BC$ son paralelas. Su longitud:

$$
AD = \sqrt{u^2+v^2},\qquad
BC = \sqrt{u^2+v^2}/2.
$$

Porque $C=(u,0)$ y $B=(3u/2,v/2)$, así que

$$
BC = \sqrt{(u/2)^2+(v/2)^2} = \frac12\sqrt{u^2+v^2}.
$$

La altura del trapecio es la distancia entre las rectas $AD$ y $BC$, que es la distancia de $C$ a la recta $AD$.

Recta $AD$ pasa por $(0,0)$ y $(u,v)$; ecuación $vx - uy=0$.

Distancia de $C=(u,0)$:

$$
h = \frac{|vu-u\cdot0|}{\sqrt{u^2+v^2}} = \frac{uv}{\sqrt{u^2+v^2}}.
$$

Entonces el área:

$$
[ABCD] = \frac{AD+BC}{2}\cdot h
= \frac{\sqrt{u^2+v^2}+\frac12\sqrt{u^2+v^2}}{2}\cdot \frac{uv}{\sqrt{u^2+v^2}}.
$$

Simplificamos:

$$
= \frac{\frac32\sqrt{u^2+v^2}}{2}\cdot \frac{uv}{\sqrt{u^2+v^2}}
= \frac34 uv.
$$

Dado $[ABCD]=42$:

$$
\frac34 uv = 42
\implies uv = 56.
$$

### Paso 8. Área del triángulo ACD

$$
[\triangle ACD] = \frac12\cdot CD\cdot AC = \frac12\cdot u\cdot v = \frac12 uv = \frac12\cdot 56 = 28.
$$

### Respuesta final

$$
\boxed{28}
$$