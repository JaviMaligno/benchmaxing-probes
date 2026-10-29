Voy a resolverlo paso a paso.

Sea $G$ el baricentro de $\triangle ABC$. La recta por $G$ paralela a $BC$ corta $AB$ en $M$ y $AC$ en $N$.

**Paso 1: Posición del baricentro**

El baricentro $G$ divide cada mediana en razón $2:1$ desde el vértice. En particular, sobre la mediana $AD$ (con $D$ en $BC$), tenemos $AG:GD = 2:1$, es decir:

$$AG = \frac{2}{3}AD.$$

**Paso 2: ¿Dónde queda $N$?**

Como $GN \parallel BC$, el triángulo $AGN$ es semejante al triángulo $ADB$ (o al considerar desde $A$), con razón de semejanza $\frac{AG}{AD} = \frac{2}{3}$.

Entonces:

$$\frac{AN}{AC} = \frac{2}{3}.$$

Es decir, $N$ está a $\frac{2}{3}$ de $AC$ desde $A$, y a $\frac{1}{3}$ de $C$.

**Paso 3: Analizamos el triángulo $ENG$**

El punto $E$ es el punto medio de $AC$. Como $N$ está en $AC$ con $AN = \frac{2}{3}AC$, tenemos:

$$AE = \frac{1}{2}AC, \qquad AN = \frac{2}{3}AC.$$

Por lo tanto, $EN = AN - AE = \frac{2}{3}AC - \frac{1}{2}AC = \frac{1}{6}AC$ a lo largo de la recta $AC$.

**Paso 4: Altura del triángulo $ENG$**

El segmento $GN$ es paralelo a $BC$. La distancia de $G$ a la recta $AC$ es una fracción de la distancia de $B$ a $AC$ (la altura del $\triangle ABC$ sobre el lado $AC$).

Como $G$ está a $\frac{2}{3}$ de la mediana desde $A$, la distancia perpendicular de $G$ a $AC$ es $\frac{1}{3}$ de la distancia de $B$ a $AC$.

En efecto, si $h_B$ es la altura de $B$ sobre $AC$, entonces la distancia de $G$ a $AC$ es $\frac{1}{3}h_B$.

**Paso 5: Calcular el área de $\triangle ENG$**

Usamos como base $EN = \frac{1}{6}AC$ y altura $\frac{1}{3}h_B$:

$$\text{Área}(\triangle ENG) = \frac{1}{2} \cdot EN \cdot \frac{h_B}{3}.$$

Sustituimos $EN = \frac{1}{6}AC$:

$$\text{Área}(\triangle ENG) = \frac{1}{2} \cdot \frac{AC}{6} \cdot \frac{h_B}{3} = \frac{AC \cdot h_B}{36}.$$

Pero el área de $\triangle ABC$ es:

$$\text{Área}(\triangle ABC) = \frac{1}{2} AC \cdot h_B = 144.$$

Entonces:

$$AC \cdot h_B = 288.$$

Por lo tanto:

$$\text{Área}(\triangle ENG) = \frac{288}{36} = 8.$$

$$\boxed{8}$$