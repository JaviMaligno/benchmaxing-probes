Voy a razonar este problema de evolución de máximos locales en un círculo.

## Entendiendo el proceso

Tenemos $n = 1011$ números en un círculo. En cada paso, cada $x_i$ se reemplaza por $\max(x_{i-1}, x_i, x_{i+1})$.

La clave es entender la dinámica. Llamemos «semilla» a un valor que sobrevive en el tiempo. Observemos qué ocurre.

## Dinámica del máximo local

Un hecho fundamental: si un elemento es un **máximo local estricto** en el tiempo $t$ (es decir, $x_i > x_{i-1}$ y $x_i > x_{i+1}$), entonces en el tiempo $t+1$ ese valor:

- Se queda en $x_i$ (pues $\max(x_{i-1}, x_i, x_{i+1}) = x_i$).
- Se propaga a $x_{i-1}$: como $x_{i-1}$ ya era menor que $x_i$, su nuevo valor $\max(x_{i-2}, x_{i-1}, x_i) = x_i$. Lo mismo para $x_{i+1}$.

Es decir, cada máximo local en el tiempo $t$ genera en el tiempo $t+1$ un **bloque de tres** posiciones con su valor, y en general, tras $k$ pasos, un valor que era máximo local en el tiempo $t$ ocupa un bloque de longitud $2k+1$ (si no choca con otro bloque vecino).

## Valores que persisten

¿Qué valores sobreviven? Un valor sobrevive mucho tiempo solo si es dominante en su región. Los máximos locales son los valores que «expanden su territorio». Los valores que no son máximos locales son absorbidos por sus vecinos más grandes.

Consideremos los máximos locales del arreglo inicial. Los máximos locales van expandiendo su dominio hasta que dos dominios chocan. Cuando chocan, el valor mayor absorbe al menor, y la frontera entre ellos se establece.

**Cada máximo local inicial es un candidato a superviviente.** De hecho, los únicos valores que pueden sobrevivir a largo plazo son los valores que fueron máximos locales en el tiempo inicial $t=0$. Los demás son absorbidos.

## ¿Cuántos máximos locales iniciales hay?

Los valores iniciales son $n = 1011$ variables i.i.d. uniformes en $[0,1]$. Un elemento $x_i$ es máximo local si $x_i > x_{i-1}$ y $x_i > x_{i+1}$.

Como las variables son continuas, no hay empates casi con seguridad. La probabilidad de que $x_i$ sea el mayor entre $(x_{i-1}, x_i, x_{i+1})$ es $1/3$. Con $n$ variables en círculo, el número esperado de máximos locales es $n/3 = 1011/3 = 337$.

Además, alternan: en un círculo, el número de máximos locales es igual al número de mínimos locales (los mínimos son exactamente los elementos que no son ni máximos ni están en un «flanco»), pero para contar máximos basta con saber que el número esperado es $n/3$.

## ¿Qué pasa después de 60 minutos?

Cada máximo local inicial expande su dominio. Tras $k$ pasos, un máximo local que no ha sido absorbido ocupa un bloque de longitud $2k+1 = 121$ posiciones.

Con $n = 1011$ y bloques de longitud 121, caben a lo sumo $\lfloor 1011/121 \rfloor = 8$ bloques completos sin chocar. Pero hay 337 bloques iniciales (máximos locales) compitiendo.

Sin embargo, los bloques de máximos locales muy cercanos chocan pronto. La cuestión es cuántos máximos locales «sobreviven» hasta el tiempo 60, es decir, cuántos tienen dominio de longitud al menos 121 sin ser absorbidos.

En el tiempo 60, un máximo local inicial tiene un dominio de $121$ posiciones **si y solo si** en las $60$ posiciones a cada lado de él, hasta el siguiente máximo local a cada lado, su valor es mayor (es decir, absorbió a todos los valores en ese tramo de $120$ posiciones).

Para que un máximo local $x_i$ sobreviva hasta el tiempo 60 sin ser absorbido, necesitamos que los máximos locales vecinos a distancia ≤ 60 a cada lado tengan valor menor que $x_i$. Como los valores son i.i.d. uniformes y los máximos locales son aproximadamente valores i.i.d. (las alturas de los máximos locales son independientes para posiciones suficientemente separadas), podemos modelarlos.

## Conteo de supervivientes esperado al tiempo 60

Un máximo local inicial sobrevive al tiempo 60 si no choca con un vecino más grande antes de 60 pasos. La velocidad de avance de una frontera entre dos máximos es 1 por paso. Si dos máximos locales adyacentes (alrededor del círculo, considerando solo máximos) están a distancia $d$, chocan al tiempo aproximadamente $d/2$.

Entonces, un máximo local sobrevive al tiempo 60 si la distancia a cada máximo local vecino (en la secuencia de máximos) es al menos $2 \cdot 60 = 120$. Es decir, el máximo local sobrevive si los siguientes 60 «huecos» entre máximos a cada lado (en posiciones) suman distancia suficiente...

Más precisamente: consideremos la secuencia de máximos locales en el círculo. Entre un máximo local y el siguiente hay un cierto número de posiciones (incluyendo no-máximos). Para que un máximo sobreviva 60 pasos, necesita que su valor sea mayor que el de su vecino máximo local a cada lado, y que avance sin oposición 60 pasos hacia cada lado.

En término de distancias, un máximo local sobrevive 60 pasos si el número de posiciones entre él y el siguiente máximo local a cada lado es ≥ 120. Pero en promedio, la distancia entre máximos consecutivos es $n / (\text{nº de máximos}) = 1011 / 337 \approx 3$. Así que la distancia habitual entre máximos es solo 3 posiciones, mucho menor que 120.

## Cálculo preciso

Dado un máximo local, la distancia $D$ hasta el siguiente máximo local (contando posiciones desde el máximo actual hasta el justo antes del siguiente máximo) sigue una distribución geométrica truncada. La distancia a cada lado debe ser $\ge 120$ para que el máximo no sea absorbido en 60 pasos.

Además, incluso si la distancia es ≥ 120 a un lado, el máximo debe vencer a los vecinos. El vecino a distancia $D$ a la izquierda y el de distancia $D'$ a la derecha: el máximo local sobrevive 60 pasos hacia la izquierda si su valor es mayor que el del vecino izquierdo, y hacia la derecha si es mayor que el vecino derecho. La probabilidad de que el máximo local central sea el mayor de los tres es $1/3$ (los valores de máximos locales consecutivos son i.i.d., dado el condicionamiento).

Entonces, la probabilidad de que un máximo local dado sobreviva 60 pasos es:
\[
P(\text{sobrevive}) = P(D_L \ge 120,\ D_R \ge 120) \cdot \frac{1}{3}
\]
donde $D_L$ y $D_R$ son las distancias al máximo local previo y siguiente, respectivamente.

Las distancias $D_L$ y $D_R$ (en términos de número de pasos de la secuencia de máximos) no son independientes, pero para un máximo local dado, condicionar a que es máximo local introduce una dependencia.

Para calcular esto con exactitud, conviene modelar la secuencia circular. Un elemento es máximo local con probabilidad $1/3$. Las distancias entre máximos consecutivos (en posiciones de la circunferencia) son: la longitud de la «brecha» entre dos máximos consecutivos (excluyendo ambos máximos) es una variable geométrica.

La probabilidad de que haya exactamente $d$ no-máximos entre dos máximos consecutivos (es decir, distancia $d+1$ entre máximos) es $(2/3)^{d}(1/3)$ aproximadamente, con un factor de ajuste por el patrón de máximos/mínimos.

Pero necesitamos que a ambos lados haya al menos 120 posiciones hasta el siguiente máximo. Es decir, un tramo de 120 posiciones a cada lado debe estar libre de otros máximos locales.

## Cálculo de la distancia entre máximos

Centrémonos en la distancia desde un máximo local hasta el siguiente máximo local. Dado que $x_i$ es máximo local ($x_i > x_{i-1}$ y $x_i > x_{i+1}$), la siguiente posición $x_{i+1}$ no es máximo local (pues $x_{i+1} < x_i$, y sería máximo local solo si $x_{i+1} > x_{i+2}$).

Sea $y_j$ la secuencia de máximos locales. Queremos la distribución de la brecha entre máximos consecutivos.

Un patrón clásico: para i.i.d. uniformes, las «subidas y bajadas» del paseo. La distancia entre máximos consecutivos es impar: para que en el ciclo tengamos máximos y mínimos alternando, la distancia entre picos consecutivos (en posiciones) es: pico a valle es variable, y valle a pico es variable, así que la distancia total no es necesariamente impar de forma fija.

Calculemos directamente la probabilidad de que, partiendo de un máximo en $x_i$, la siguiente posición $x_{i+1}, x_{i+2}, \ldots$ no tenga máximos hasta, digamos, $x_{i+d+1}$ sea el siguiente máximo.

Dado $x_i$ máximo ($x_i > x_{i-1}, x_i > x_{i+1}$):
- $x_{i+1} < x_i$.
- Para que $x_{i+2}$ sea máximo: necesitamos $x_{i+2} > x_{i+1}$ y $x_{i+2} > x_{i+3}$. Probabilidad, dado $x_{i+1}< x_i$, ... esto no es fácil sin condicionar todos los valores.

Se puede resolver con la teoría de «records» en permutaciones aleatorias. Las posiciones de los máximos locales (including su valor) forman un proceso de renovación.

Sin embargo, para el problema, hay un enfoque más sencillo usando la linealidad de la esperanza y la estructura de la secuencia de máximos en un círculo con $n=1011$ y 60 pasos.

## Enfoque con la linealidad y simetría

Consideremos una posición fija $i$. Queremos saber la probabilidad de que $x_i$ (en el tiempo 60) sea un «valor superviviente» que provino de un máximo local inicial.

Mejor: contemos el número esperado de **bloques de valores distintos** al tiempo 60. Al tiempo 60, cada valor superviviente ocupa un bloque contiguo de posiciones. El número de valores distintos es el número de bloques.

Cada bloque al tiempo 60 proviene de un máximo local inicial que expandió su dominio durante 60 pasos. Los límites de los bloques están a mitad de camino entre máximos locales vecinos.

En el tiempo 60:
- Un máximo local inicial en la posición $p$ con valor $v$ tiene un dominio de posiciones que se extiende hasta donde encontró un máximo local de mayor valor, o hasta el punto medio del hueco entre él y su vecino, lo que ocurra primero.
- La frontera entre dos máximos locales vecinos (con valores $a > b$) avanza a velocidad 1 hacia el menor. La posición de la frontera al tiempo $t$ es: si la distancia entre los máximos es $d$, el mayor avanza $\min(t, \lfloor d/2 \rfloor)$ posiciones hacia el menor.

Para que al tiempo 60 haya $k$ bloques distintos (es decir, $k$ valores distintos supervivientes), necesitamos que $k$ máximos locales iniciales tengan dominios no vacíos al tiempo 60.

Un máximo local tiene dominio no vacío al tiempo 60 si no fue completamente absorbido para ese tiempo. Frontera absorbe al menor: el menor deja de tener dominio cuando el mayor lo alcanza. La distancia del mayor al menor es $d$; el mayor alcanza al menor al tiempo $d$ (avanzando 1 posición por paso). Pero el menor también avanza hacia el mayor a velocidad 1 si el menor es el mayor en la otra dirección... espera, un máximo local solo expande en las direcciones donde es mayor.

Reconsideremos: un máximo local $M$ con valor $v$ expande hacia la izquierda a velocidad 1 mientras el valor a la izquierda (que se va encontrando) sea menor que $v$. Si en la posición a distancia $d$ a la izquierda hay otro máximo local $M'$ con valor $v' > v$, entonces $M'$ expande hacia la derecha (hacia $M$) y $M$ no puede expandir hacia la izquierda una vez que la frontera se encuentra. La frontera se mueve: inicialmente $M'$ domina la posición justo a su derecha (avanza 1), y $M$ domina la posición justo a su izquierda... en realidad si $v' > v$, entonces $M'$ avanza hacia la izquierda de $M$ y $M$ puede avanzar hacia $M'$ solo si $v$ es mayor que los valores intermedios, pero como $v' > v$, cuando los dominios se encuentren el valor $v'$ absorberá todo.

La frontera entre $M'$ (mayor, a la izquierda) y $M$ (menor, a la derecha): $M'$ avanza hacia la derecha 1 por paso, y $M$ avanza hacia la izquierda 1 por paso (pues los valores intermedios son menores que $v$). Se encuentran al tiempo $\lceil d/2 \rceil$ en el punto medio.

Entonces, al tiempo 60, $M$ mantiene un dominio no vacío si la frontera con el vecino mayor no lo alcanza antes de 60 pasos. La frontera más cercana es con el siguiente máximo local en cada dirección.

## Distancia al siguiente máximo mayor

Sea $M$ un máximo local. Considere el vecino máximo local más cercano a la izquierda con valor > v_M y el más cercano a la derecha con valor > v_M. La frontera con ellos se mueve hacia $M$ a velocidad 1 por paso (el mayor avanza a velocidad 1 hacia $M$, y $M$ no avanza hacia el mayor porque los valores intermedios menores que $v_M$, $M$ avanza también — pero el mayor absorbe todo cuando llegan al punto medio).

En términos simples: al tiempo 60, $M$ sobrevive si en el radio de 60 posiciones a cada lado no hay ningún máximo local con valor mayor que $v_M$. Es decir, $M$ es el mayor entre todos los máximos locales en un entorno de 60 posiciones a cada lado.

Por lo tanto:
\[
P(M \text{ sobrevive al tiempo } 60) = P\big(\text{no hay máximo local con valor mayor en las } 60\text{ posiciones a cada lado}\big)
\]

Esto es equivalente a que $v_M$ sea el máximo entre los valores de los máximos locales en una ventana de 121 posiciones centrada en $M$.

## Conteo de los máximos locales en la ventana

El número de máximos locales en 121 posiciones consecutivas tiene una distribución. En promedio, esperamos $121/3 \approx 40.33$ máximos en esa ventana.

Para que $M$ sobreviva, $M$ debe tener el mayor valor entre esos ~40 máximos. Por simetría (valores i.i.d.), la probabilidad de que un máximo dado sea el mayor entre $m$ máximos es $1/m$. Pero hay que tomar el valor esperado del recíproco del número de máximos en la ventana.

Sea $X$ el número de máximos locales en una ventana de 121 posiciones que contiene a $M$ (con $M$ en el centro). $M$ está incluido en $X$. La probabilidad de que $M$ tenga el mayor valor entre estos $X$ máximos es $1/X$.

Entonces:
\[
P(M \text{ sobrevive}) = E\left[\frac{1}{X}\right]
\]

donde $X$ es el número de máximos locales en 121 posiciones (incluyendo la posición central que es un máximo).

## Cálculo de $E[1/X]$

En $m = 121$ posiciones alrededor (60 a cada lado + la central), el número de máximos locales $X$ entre estas posiciones...

Necesitamos la distribución de $X$. La posición central es un máximo local por hipótesis. Las posiciones adyacentes (a distancia 1) no pueden ser máximos locales (porque son menores que el máximo central).

El número de máximos en una secuencia de longitud $m$ de variables i.i.d. continuas: cada posición tiene probabilidad $1/3$ de ser máximo local (mayor que sus dos vecinas). Pero con el condicionamiento de que la central es máximo local, las posiciones a distancia 1 no son máximos, y el resto son aproximadamente independientes con probabilidad $1/3$.

Para $m = 121$ con 1 máximo garantizado en el centro y 2 no-máximos garantizados (los vecinos), los otros $121 - 3 = 118$ posiciones: las posiciones a distancia ≥ 2 del centro en el arreglo circular Efectivamente, condicionar central como máximo afecta a sus 2 vecinos, pero las posiciones a distancia ≥ 2 tienen probabilidad $1/3$ de ser máximos independientemente (aproximadamente, con correcciones por bordes de la ventana).

Así que $X \approx 1 + \text{Binomial}(118, 1/3)$, aproximadamente.

Pero hay una complicación: dentro de una ventana abierta (no circular), las posiciones de la ventana tienen 2 vecinos dentro de la ventana salvo los bordes. Para un conteo exacto, los bordes de la ventana (posiciones a distancia exactamente 60 del centro) tienen solo 1 vecino dentro de la ventana, así que su probabilidad de ser máximo local dentro de la ventana es diferente. Pero si consideramos la ventana como parte del círculo grande, todos los elementos tienen 2 vecinos, y la probabilidad de ser máximo local dados los condicionamientos del centro es $1/3$ para posiciones a distancia ≥ 2.

Entonces, para una ventana de 121 posiciones en el círculo con la central condicionada a ser máximo local:
- Posición central: máximo local (probabilidad 1).
- Posiciones a distancia 1: no máximos (probabilidad 0 de ser máximo).
- Posiciones a distancia $k \ge 2$ (hasta 60): cada una es máximo local con probabilidad $1/3$, independientemente (en el límite; en realidad hay dependencia débil por la estructura de máximos alternantes en el círculo, pero para esperanza de $1/X$, este nivel de detalle puede importar).

## La estructura exacta: máximos y mínimos alternan

En un círculo, si vamos marcando los elementos: algunos son máximos, otros mínimos, otros «intermedios» (ni máximo ni mínimo, es decir, monótonos locales). En una secuencia i.i.d. continua, las categorías son: máximo local (valor mayor que ambos vecinos) con prob $1/3$, mínimo local con prob $1/3$, y «pendiente» (mayor que un vecino, menor que el otro) con prob $1/3$.

Entre dos máximos consecutivos hay exactamente un mínimo, y algunos elementos intermedios. La distancia entre máximos consecutivos es la suma de: (número de intermedios hasta el mínimo) + 1 (el mínimo) + (número de intermedios hasta el siguiente máximo) + 1.

En términos de la secuencia de categorías, la probabilidad de transición: de un máximo, la siguiente posición no puede ser máximo (prob 0), puede ser pendiente o mínimo. De una pendiente, la siguiente puede ser otra pendiente, un mínimo, o un máximo. Etcétera.

La distancia entre máximos consecutivos $D$ (en posiciones, medida de máximo a máximo) tiene distribución con cola geométrica. Calculemos su cola.

Para que desde un máximo $x_i$, la siguiente posición $x_{i+1}$ (pendiente o mínimo, no máximo) no sea máximo, y luego una secuencia... Más fácil: usar la propiedad de que las posiciones de máximos en la secuencia i.i.d. forman un proceso de renovación con función de masa de la brecha.

La probabilidad de que un máximo en la posición $j$ sea seguido por el siguiente máximo exactamente en la posición $j+d$ (es decir, brecha $d$) se puede calcular como la probabilidad de que las posiciones $j+1, \ldots, j+d-1$ no sean máximos y $j+d$ sí lo sea, dado que $j$ es máximo.

Usemos los resultados estándar para una secuencia i.i.d. continua. Sea $P(d)$ la probabilidad de que la brecha entre máximos consecutivos sea exactamente $d$. Se sabe que la brecha entre máximos locales en una secuencia i.i.d. tiene una distribución con media 3 y con una fórmula para $P(d)$.

Calculemos $P(d)$ para valores pequeños y generalicemos.

Primero, la brecha mínima es 2: no puede haber dos máximos adyacentes (brecha 1 imposible). La brecha 2 ocurre con patrón Máx–Mín–Máx. La probabilidad de que $x_{i+1}$ sea mínimo y $x_{i+2}$ sea máximo, dado $x_i$ máximo.

Dado $x_i$ máximo ($x_i > x_{i-1}, x_i > x_{i+1}$):
- $x_{i+1} < x_i$.
- Para que $x_{i+1}$ sea mínimo: $x_{i+1} < x_{i+2}$.
- Para que $x_{i+2}$ sea máximo: $x_{i+2} > x_{i+1}$ y $x_{i+2} > x_{i+3}$.

Dado $x_i > x_{i+1}$: la probabilidad de que $x_{i+2} > x_{i+1}$ es $1/2$ (intercambiables dados los condicionamientos). Dado $x_{i+2} > x_{i+1}$ y $x_i > x_{i+1}$, la probabilidad de que $x_{i+2} > x_{i+3}$ es $1/2$ (independiente de $x_{i+3}$). Y necesitamos que $x_{i+1}$ sea el mínimo entre $x_i, x_{i+1}, x_{i+2}$, lo cual ya está.

Entonces $P(2) = 1/4$.

Para la brecha $d \ge 3$: patrón Máx, [no-máximos], ... , Máx. El «no-máximo» en la posición $j+1$ puede ser pendiente o mínimo.

Un enfoque más sistemático: usemos la representación de los signos de las diferencias consecutivas. Los máximos locales son exactamente los picos del paseo de las diferencias. Sea $s_i = \text{sign}(x_{i+1} - x_i)$ (con $s_0 = \text{sign}(x_1 - x_n)$). Un máximo local en $x_i$ corresponde a $s_{i-1} = +$ y $s_i = -$. Los mínimos corresponden a $s_{i-1} = -$ y $s_i = +$.

Los signos $s_i$ son i.i.d. con $P(+) = P(-) = 1/2$ (simetría). Además, los signos son independientes entre sí. ¡Esta es una simplificación muy útil!

Entonces, $x_i$ es máximo local $\iff s_{i-1} = +, s_i = -$, lo cual ocurre con probabilidad $1/4$. Espera, pero la probabilidad de máximo local es $1/3$, no $1/4$. Revisemos: la probabilidad de que $x_i$ sea mayor que $x_{i-1}$ y $x_i > x_{i+1}$. Por simetría, $P(x_i > x_{i-1}) = 1/2$, y $P(x_i > x_{i+1}) = 1/2$, pero no son independientes. Conditional en $x_i$, las variables $x_{i-1}, x_{i+1}$ son independientes uniformes, así que $P(x_i > x_{i-1}, x_i > x_{i+1}) = E[(x_i)^2] = 1/3$. Correcto, $1/3$.

Los signos $s_{i-1} = \mathbf{1}[x_i > x_{i-1}] \cdot (+)$, $s_i = \mathbf{1}[x_{i+1} > x_i]\cdot(+)$. Si $x_i$ es máximo: $x_i > x_{i-1}$ ($s_{i-1}=+$) y $x_{i+1} < x_i$ ($s_i = -$). Entonces $s_{i-1}=+, s_i=-$. La probabilidad de que $s_{i-1}=+, s_i=-$ es $1/4$, pero la probabilidad de máximo local es $1/3$. La condición $s_{i-1}=+, s_i=-$ es necesaria pero no suficiente para máximo: además necesitamos que efectivamente $x_i > x_{i-1}$ y $x_i > x_{i+1}$, pero dado $s_{i-1}=+, s_i=-$ esto ya es la definición. Espera: $s_{i-1}=+$ significa $x_i > x_{i-1}$, y $s_i=-$ significa $x_{i+1} < x_i$. Así que $s_{i-1}=+, s_i=-$ es exactamente «$x_i$ es máximo local». Entonces la probabilidad de $s_{i-1}=+, s_i=-$ debería ser $1/3$, no $1/4$. El error: los signos $s_i$ NO son independientes entre sí. No, los signos de las diferencias son dependientes porque comparten variables.

Entonces los signos no son i.i.d. Esto complica la brecha.

Afortunadamente, no necesitamos la distribución completa de la brecha para este problema: solo necesitamos el número esperado de máximos supervivientes al tiempo 60, y podemos usar la linealidad directamente sin calcular $E[1/X]$ exactamente... Veamos.

## Enfoque directo: conteo de supervivientes por linealidad

El número esperado de valores distintos al tiempo 60 es el número esperado de máximos locales iniciales que sobreviven al tiempo 60 (los bloques de valor en el tiempo 60 corresponden uno a uno con los máximos supervivientes).

Un máximo local en la posición $i$ sobrevive al tiempo 60 si su valor es el mayor entre todos los valores en las 60 posiciones a su izquierda y 60 a su derecha (en realidad, necesita ser mayor que los valores de los máximos locales en ese entorno, pero como los máximos locales son los únicos que expanden, y expanden absorbiendo todo a su paso, la condición es que no haya máximo local con mayor valor en esas 60 posiciones a cada lado).

Más precisamente: $x_i$ máximo local sobrevive si para todo $j$ con $1 \le |j-i| \le 60$ (módulo 1011) tal que $x_j$ es máximo local, se cumple $x_j < x_i$.

Por linealidad de la esperanza:
\[
E[\text{supervivientes}] = \sum_{i} P(x_i \text{ máximo local y } x_i > x_j \text{ para todo máximo local } j \text{ con } |j-i| \le 60)
\]

Por simetría, todas las posiciones tienen la misma probabilidad. Sea $P_{\text{surv}}$ esa probabilidad para una posición fija (digamos $i = 0$).

Entonces:
\[
E[\text{supervivientes}] = n \cdot P_{\text{surv}}
\]

## Cálculo de $P_{\text{surv}}$

$P_{\text{surv}}$ es la probabilidad de que $x_0$ sea máximo local y sea mayor que todos los máximos locales en las posiciones $\{1, \ldots, 60\} \cup \{n-60, \ldots, n-1\}$ (en el círculo).

Equivalentemente, $x_0$ es el máximo de todos los valores en un conjunto de 121 posiciones que incluyen a $x_0$ y sus 60 vecinos a cada lado.

Sea $Y$ el máximo de los valores en las 121 posiciones. La probabilidad de que $x_0$ sea el máximo es $1/121$ (todas las posiciones i.i.d. uniformes, la probabilidad de ser el máximo entre 121 es $1/121$).

Pero además necesitamos que $x_0$ sea máximo local. Condicionemos a que $x_0$ sea el máximo de las 121 posiciones. Dado esto, ¿cuál es la probabilidad de que $x_0$ sea máximo local?

$x_0$ es máximo local si $x_0 > x_{-1}$ y $x_0 > x_1$. Dado que $x_0$ es el mayor de las 121 posiciones, en particular $x_0 > x_1$ y $x_0 > x_{-1}$ con seguridad, ¡porque $x_1$ y $x_{-1}$ están en las 121 posiciones (son los vecinos inmediatos, a distancia 1 ≤ 60)!

Entonces, si $x_0$ es el mayor de las 121 posiciones, automáticamente $x_0 > x_1$ y $x_0 > x_{-1}$, así que $x_0$ es máximo local. Por lo tanto:

\[
P(x_0 \text{ es máximo local y mayor que máximos locales en el entorno}) = P(x_0 \text{ es el mayor de las 121 posiciones})
\]

porque si $x_0$ es el mayor entre las 121 posiciones, entonces $x_0$ es mayor que $x_1, x_{-1}$ (es máximo local), y mayor que todos los máximos locales del entorno (pues todos esos máximos locales están en las 121 posiciones y tienen valor menor que $x_0$).

Y además, ¿es necesario que $x_0$ sea máximo local para sobrevivir? Si $x_0$ es el mayor de las 121 posiciones, sobrevive; pero ¿puede un no-máximo local sobrevivir? No, solo los máximos locales iniciales pueden tener dominios no vacíos. Pero ya mostramos que ser el mayor de las 121 posiciones implica ser máximo local, así que no hay problema.

Por lo tanto:
\[
P_{\text{surv}} = P(x_0 \text{ es el mayor entre } x_{-60}, \ldots, x_{60}) = \frac{1}{121}
\]

¡porque las 121 variables son i.i.d. uniformes, y cada una tiene la misma probabilidad de ser la mayor!

## Resultado

\[
E[\text{valores distintos al tiempo } 60] = n \cdot P_{\text{surv}} = 1011 \cdot \frac{1}{121}
\]

Calculamos:
\[
121 = 11^2 = 121
\]
\[
1011 = 11 \cdot 91 = 11 \cdot 7 \cdot 13
\]
\[
\frac{1011}{121} = \frac{11 \cdot 91}{11 \cdot 11} = \frac{91}{11}
\]

\[
\frac{91}{11} = 8 + \frac{3}{11} = \frac{91}{11}
\]

Verifiquemos: $11 \times 8 = 88$, $91 - 88 = 3$, así que $\frac{91}{11} = 8.2727\ldots$

Entonces:
\[
E = \frac{1011}{121} = \frac{91}{11}
\]

## Verificación con el caso límite

- Si el número de pasos fuera 0 (sin evolución), $x_0$ sobrevive si es máximo local en un entorno de 0 posiciones a cada lado, es decir, solo consideramos la posición central: $P = P(x_0 \text{ máximo local}) = 1/3$, y $E = 1011/3 = 337$. Correcto.

- Si consideramos $k$ pasos en lugar de 60: la ventana tiene $2k+1$ posiciones, y $P_{\text{surv}} = 1/(2k+1)$, dando $E = n/(2k+1)$.

Para $k = 60$: $E = 1011 / 121 = 91/11$.

Este resultado es consistente y limpio.

## Conclusión

La respuesta es $\frac{91}{11}$.

Final:
\[
\boxed{\frac{91}{11}}
\]