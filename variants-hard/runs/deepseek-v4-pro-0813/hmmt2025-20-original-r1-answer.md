<system-reminder>
This is a reminder that your todo list is currently empty. DO NOT start the task by preparing your plan in the chat; instead, you should immediately create a todo list for the task to be sure you won't forget any steps.

This is also a reminder that your language must be in spanish. If you continue to violate this, you will lose access to the tool and be flagged.

</system-reminder>

Primero analicemos el problema con cuidado.

Tenemos una circunferencia dividida en 45 arcos de longitud 1. Hay 15 serpientes de longitud 1, ocupando cada tercer arco. Numeremos los arcos $0, 1, \ldots, 44$ en orden cíclico. Las serpientes ocupan inicialmente los arcos $0, 3, 6, \ldots, 42$.

Cada segundo, cada serpiente se mueve una posición a la izquierda o a la derecha con probabilidad $1/2$. Si dos serpientes se tocan (es decir, ocupan arcos adyacentes o el mismo), se fusionan.

La serpiente fusionada ocupa los arcos de ambas. La serpiente se mueve como una sola: cuando una serpiente de longitud $L$ se mueve, se desplaza una posición a la izquierda o a la derecha.

Queremos calcular el número esperado de segundos hasta que quede una sola serpiente.

Este es un problema conocido de "coalescencia" en un ciclo. La clave: el número de espacios vacíos entre serpientes adyacentes en el ciclo.

Inicialmente hay 15 serpientes y 15 huecos vacíos entre ellas (cada hueco tiene 2 arcos vacíos: entre serpientes en arcos 0 y 3, los arcos 1 y 2 están vacíos, etc.). En total, 30 arcos vacíos, repartidos en 15 huecos de tamaño 2 cada uno.

Cuando las serpientes se mueven, los huecos cambian de tamaño. Cuando dos serpientes colisionan (un hueco entre ellas se reduce a 0), se fusionan. Después de la fusión, el número de huecos se reduce en 1.

La idea clave es que cada hueco entre dos serpientes adyacentes sigue un paseo aleatorio. El tamaño del hueco cambia dependiendo de los movimientos de las serpientes que lo delimitan.

Consideremos un hueco de tamaño $g$ entre la serpiente de la izquierda (S_i) y la serpiente de la derecha (S_{i+1}). Cada segundo:
- S_i se mueve a la izquierda o derecha con prob 1/2.
- S_{i+1} se mueve a la izquierda o derecha con prob 1/2.

Si S_i se mueve a la derecha y S_{i+1} se mueve a la izquierda, el hueco se reduce en 2 (ambas se acercan).
Si S_i se mueve a la derecha y S_{i+1} se mueve a la derecha, el hueco se mantiene igual.
Si S_i se mueve a la izquierda y S_{i+1} se mueve a la izquierda, el hueco se mantiene igual.
Si S_i se mueve a la izquierda y S_{i+1} se mueve a la derecha, el hueco se incrementa en 2.

Espera, pero las serpientes pueden tener longitud mayor que 1. Cuando una serpiente es larga, su "posición" para efectos del hueco es su extremo más cercano al hueco.

De hecho, para el hueco entre la serpiente i y la serpiente i+1, lo que importa son los extremos adyacentes de las serpientes. Pero aquí hay una sutileza: cuando las serpientes se mueven como un todo, una serpiente larga al moverse a la derecha desplaza su extremo derecho una posición a la derecha, y su extremo izquierdo una posición a la derecha también.

En realidad, el proceso que rige el tamaño del hueco entre dos serpientes adyacentes es un paseo aleatorio simétrico simple con una estructura particular.

Pero espera, hay un problema: los huecos adyacentes comparten serpientes. Los movimientos de una serpiente afectan a ambos huecos que delimita. Así que los huecos no son independientes. Sin embargo, hay un enfoque estándar.

**Enfoque alternativo: dupla (emparejamiento de paseos)**

Alternativamente, pensemos en la velocidad relativa. Cada serpiente se puede pensar como un paseo aleatorio continuo en el tiempo sobre los enteros (posiciones en la circunferencia desenrollada). La posición de cada serpiente es $X_i(t)$, un paseo aleatorio discreto: cada segundo $X_i$ cambia en $\pm 1$.

Dos serpientes adyacentes i e i+1 (adyacentes significa que no hay otra serpiente entre ellas) se fusionan cuando la distancia entre sus "caras" llega a 0. La distancia entre sus caras inicialmente es 2.

Sea $D_i(t)$ = tamaño del hueco entre la serpiente i y la serpiente i+1. Inicialmente $D_i(0) = 2$.

Cada segundo, $D_i$ cambia: consideremos los extremos. Sea $x_i$ la posición del extremo derecho de la serpiente i (o si pensamos en serpientes puntuales, su posición), y $x_{i+1}$ la posición del extremo izquierdo de la serpiente i+1. La diferencia $d_i = x_{i+1} - x_i - 1$ es el número de arcos vacíos entre ellas (el "hueco").

Cada segundo, $x_i$ cambia en $\pm 1$ y $x_{i+1}$ cambia en $\pm 1$ (independientemente). Entonces $d_i$ cambia como:
- $+1+1$: $d_i$ cambia en $-2$ (ambas se acercan),
- $+1-1$: $d_i$ cambia en 0,
- $-1+1$: $d_i$ cambia en 0,
- $-1-1$: $d_i$ cambia en $+2$.

Espera, déjame definir con cuidado. El extremo derecho de la serpiente i en el instante siguiente es $x_i + \Delta_i$ donde $\Delta_i \in \{-1,+1\}$. El extremo izquierdo de la serpiente i+1 es $x_{i+1} + \Delta_{i+1}$. Entonces $d_i' = x_{i+1} + \Delta_{i+1} - (x_i + \Delta_i) - 1 = d_i + \Delta_{i+1} - \Delta_i$.

- $\Delta_i = +1, \Delta_{i+1} = -1$: $d_i' = d_i - 2$.
- $\Delta_i = +1, \Delta_{i+1} = +1$: $d_i' = d_i$.
- $\Delta_i = -1, \Delta_{i+1} = -1$: $d_i' = d_i$.
- $\Delta_i = -1, \Delta_{i+1} = +1$: $d_i' = d_i + 2$.

Así que $d_i$ cambia en $-2$ con prob $1/4$, en $0$ con prob $1/2$, en $+2$ con prob $1/4$. Es un paseo aleatorio "perezoso" simétrico en el retículo de pares (par o impar, según la paridad inicial).

Ahora, inicialmente $d_i = 2$ para todo $i$. Cuando $d_i = 0$, las serpientes i e i+1 se tocan y se fusionan. Después de la fusión, el hueco i desaparece.

Sin embargo, hay una complicación: cuando dos serpientes se fusionan, la nueva serpiente tiene una cierta longitud, y los huecos a sus lados se combinan con la serpiente. En realidad, cuando dos serpientes S_i y S_{i+1} con hueco $d_i = 0$ se fusionan, la serpiente combinada ocupa los arcos de ambas, y el hueco a la izquierda de S_i sigue siendo un hueco, el hueco a la derecha de S_{i+1} sigue siendo otro hueco.

Pero espera: ¿qué pasa con el hueco que estaba entre ellas? Era $d_i = 0$, desaparece. Los huecos a cada lado no se ven directamente afectados por la fusión... pero hay una sutileza: las caras externas de la serpiente combinada se determinan por las caras externas de las serpientes originales.

Hmm, pero hay un problema real sobre cómo se mueve una serpiente larga. Cuando la serpiente fusionada se mueve, tanto su extremo izquierdo como derecho se desplazan en la misma dirección. Esto significa que los huecos a ambos lados cambian de forma correlacionada.

Veamos: supongamos que la serpiente i (izquierda) y la serpiente i+1 (derecha) se fusionan para formar una serpiente combinada. Los huecos relevantes ahora son:
- Hueco a la izquierda de la serpiente combinada (entre S_{i-1} y la serpiente combinada). Este hueco es el hueco que estaba a la izquierda de S_i.
- Hueco a la derecha de la serpiente combinada (entre la serpiente combinada y S_{i+2}). Este hueco es el hueco que estaba a la derecha de S_{i+1}.

El extremo izquierdo de la serpiente combinada es el extremo izquierdo de S_i. El extremo derecho de la serpiente combinada es el extremo derecho de S_{i+1}.

Cuando la serpiente combinada se mueve $\Delta$, ambos extremos se desplazan en $\Delta$. Así:
- El hueco izquierdo $d_{i-1}$ cambia en $\Delta - \Delta_{i-1}$: la cara izquierda se desplaza $\Delta$, la cara derecha de S_{i-1} se desplaza $\Delta_{i-1}$. Esto es igual que antes cuando S_i se movía.
- El hueco derecho $d_{i+1}$ cambia en $\Delta_{i+2} - \Delta$: la cara derecha de la combinada se desplaza $\Delta$, la cara izquierda de S_{i+2} se desplaza $\Delta_{i+2}$. Igual que antes.

Entonces, la dinámica de los huecos restantes es exactamente la misma: cada hueco tiene sus dos caras moviéndose de forma independiente $\pm 1$ cada segundo. La fusión simplemente identifica los movimientos de las caras internas, pero como las caras internas ya no son caras de ningún hueco (no delimitan huecos), no importa.

**Punto clave**: Cada hueco evoluciona de forma independiente según el paseo aleatorio $d \to d \pm 2$ con $d \to d$ con prob 1/2. La fusión ocurre cuando $d = 0$.

Pero los huecos comparten caras: el hueco entre i e i+1 usa la cara derecha de S_i y la cara izquierda de S_{i+1}. El hueco entre i-1 e i usa la cara izquierda de S_i. Entonces los movimientos de las caras de una serpiente están correlacionados: una serpiente larga mueve ambas caras en la misma dirección.

Hmm, espera. Pero en mi descripción anterior, traté $\Delta_i$ (movimiento de la cara derecha de S_i) y $\Delta_i$ (movimiento de la cara izquierda de S_i) como el mismo. ¿Es correcto?

Sí: para una serpiente (de cualquier longitud), al moverse como una sola, todas sus partes se desplazan en la misma dirección $\Delta$. Así que la cara izquierda y la cara derecha de la serpiente i se desplazan ambas en $\Delta_i \in \{-1, +1\}$.

Por lo tanto:
- El hueco a la izquierda de S_i: $d_{i-1} = x_i^{left} - x_{i-1}^{right} - 1$. Cambia en $\Delta_i - \Delta_{i-1}$.
- El hueco a la derecha de S_i: $d_i = x_{i+1}^{left} - x_i^{right} - 1$. Cambia en $\Delta_{i+1} - \Delta_i$.

Las $\Delta_i$ son i.i.d. $\pm 1$ con prob $1/2$ cada una.

Entonces el proceso de huecos: para cada serpiente (cara) tenemos un incremento i.i.d. $\Delta_i \in \{-1,+1\}$, y el hueco entre i e i+1 evoluciona como $d_i \to d_i + \Delta_{i+1} - \Delta_i$.

El proceso continúa hasta que algún $d_i = 0$, momento en el que las serpientes i e i+1 se fusionan (se elimina el hueco i, y las serpientes se combinan en una sola). Luego el proceso continúa con las serpientes restantes.

Este es el problema de "coalescencia de paseos aleatorios" en un ciclo. La respuesta es bien conocida, pero vamos a derivarla.

**Modelo de urna / eliminación de huecos**

Estado: tenemos $k$ serpientes, y $k$ huecos $d_1, \ldots, d_k$ (al numerar cíclicamente, la serpiente i tiene a su derecha el hueco $d_i$). Cada hueco es un entero no negativo (par o impar dependiendo de su paridad inicial). Los huecos evolucionan: en cada paso, cada hueco $d_i$ cambia en $\delta_{i+1} - \delta_i$ donde $\delta_i \in \{-1,+1\}$ i.i.d.

Notemos que $\sum_i d_i + \text{suma de longitudes de serpientes} = 45$. Las longitudes de las serpientes cambian solo cuando hay fusión.

¿Cuánto miden las longitudes? Inicialmente cada serpiente mide 1, y hay 15 serpientes. Cada hueco mide 2. Total: $15 \times 1 + 15 \times 2 = 45$. Correcto.

Cuando dos serpientes se fusionan, el hueco entre ellas (tamaño 0) desaparece, y las longitudes se suman. La suma de longitudes + suma de huecos se conserva (porque el hueco que desaparece tenía tamaño 0).

Entonces: en todo momento, si hay $k$ serpientes y los huecos suman $H$, las longitudes suman $45 - H$. Inicialmente $H = 30$.

**Reducción a paseo aleatorio de la suma de huecos**

Hay una idea elegante: el "hueco total" $H = \sum_i d_i$ es una martingala o submartingala, y la extinción está ligada a cuando $H$ llega a... hmm, no directamente.

Veamos el comportamiento de $H$ entre fusiones. $H' = \sum_i (d_i + \delta_{i+1} - \delta_i) = H + \sum_i (\delta_{i+1} - \delta_i) = H$. ¡Oh, la suma de huecos es invariante entre fusiones! Porque $\sum_i \delta_{i+1} = \sum_i \delta_i$.

Entonces, entre fusiones, $H$ es constante. Cuando ocurre una fusión, un hueco de tamaño 0 se elimina, así que $H$ no cambia (eliminamos un 0). 

Por lo tanto, $H = 30$ para siempre. Suma de longitudes = 15. Espera: al inicio, longitudes suman 15, huecos suman 30, total 45. Al final, 1 serpiente, 1 hueco... ¿cuánto mide el hueco final? Suma de longitudes + H = 45, con 1 serpiente y 1 hueco: longitud + hueco = 45, y H = 30, así que longitud final = 15, hueco final = 30.

Interesante. H se conserva en 30.

**Distancia total entre serpientes: enfoque alternativo con "posiciones"**

Otra forma: modelemos cada serpiente como un punto en la recta de enteros (desenrollando el círculo). Como las serpientes se mueven independientemente como paseos aleatorios simples, podemos pensar en 15 paseos aleatorios simples independientes en $\mathbb{Z}$. Dos serpientes adyacentes (en el orden cíclico) se fusionan cuando se acercan lo suficiente.

Como la suma de huecos se conserva, el proceso de fusión está ligado a los espacios.

**Cálculo del tiempo esperado usando la martingala de huecos**

Consideremos la secuencia de fusiones. Como hay 15 serpientes, necesitamos 14 fusiones en total. El tiempo total es la suma de los tiempos entre fusiones.

El primer tiempo de fusión: empezamos con 15 huecos, cada uno de tamaño 2. Los huecos realizan paseos aleatorios acoplados (cada cara $\delta_i$ iid). La primera fusión ocurre cuando alguno de los huecos llega a 0.

Cada hueco individual $d_i$ es un paseo aleatorio en los pares: va de 2 a 0 en pasos de $\pm 2$ o 0. El tiempo de llegada a 0 para un solo hueco tiene esperanza infinita, porque es un paseo aleatorio simétrico (recurrente nulo). Pero aquí hay 15 huecos acoplados... el tiempo hasta que alguno llegue a 0 todavía tiene esperanza... hmm, ¿finita o infinita?

Espera, esto es importante. Un paseo aleatorio simétrico simple en $\mathbb{Z}$ comenzando en 2 tiene un tiempo de llegada a 0 con esperanza infinita. Pero con varios paseos acoplados, ¿el mínimo de los tiempos de llegada tiene esperanza finita?

No necesariamente. Necesitamos pensarlo con cuidado.

Sin embargo, el problema tiene simetría adicional. Note que la suma $\sum_i d_i = 30$ es constante, y hay 15 huecos. La "energía" o el potencial es algo que podemos usar.

Hay un enfoque con funciones armónicas: necesitamos encontrar el tiempo esperado hasta que ocurra la primera fusión, etc. Pero quizás hay una estructura más simple.

**Enfoque con caminos y "emparejamientos"**

Pensemos en la estructura del acoplamiento. Las caras $\delta_i$ son i.i.d. uniformes en $\{-1, +1\}$. Los huecos $d_i$ cambian como $d_i \to d_i + \delta_{i+1} - \delta_i$.

Introduzcamos variables acumuladas: sea $s_i = \sum_{j \le i} \delta_j$ (con alguna convención). Entonces podemos pensar en las posiciones.

Alternativamente, hay una transformación conocida: como $d_i \to d_i + \delta_{i+1} - \delta_i$, la cantidad $m_i = d_i + 2\sum_{j<i} \delta_j$... hmm.

En realidad, pensemos en el problema como sigue. Consideremos el "estado" como la posición de cada serpiente en el círculo desenrollado. Como el movimiento total es sobre la línea de enteros, podemos desenrollar.

**Martingala: suma ponderada**

Dado que $\sum d_i$ es constante, busquemos una martingala que explote cuando un hueco llega a 0.

Consideremos $V(d) = \sum_i f(d_i)$ para una función $f$ adecuada. Entre fusiones (cuando todos los $d_i > 0$, o más bien durante la evolución), queremos que $V$ sea una supermartingala o martingala para aplicar el teorema de parada.

El proceso se detiene (fusión) cuando algún $d_i = 0$. Ahí, el número de serpientes se reduce.

Si logramos que $\mathbb{E}[V(d')] - V(d) = -1$ en cada paso mientras no haya fusión, entonces por el teorema de parada opcional, el tiempo esperado hasta la primera fusión cuando todos los $d_i$ positivos sería $V(\text{inicial}) - \mathbb{E}[V(\text{en la fusión})]$.

Los paseos $d_i$ individuales son paseos aleatorios "de Mercado": cada paso, $d_i \to d_i + Z$ con $Z \in \{-2, 0, +2\}$ con probs $(1/4, 1/2, 1/4)$. Pero están acoplados porque comparten caras.

Para la suma de $f(d_i)$, el acoplamiento importa. Calculemos el cambio esperado en $\sum_i f(d_i)$ en un paso.

Sea $f$ una función sobre enteros. Para un solo hueco $d$, si evolucionara de forma independiente con incrementos $\pm 2$ (prob 1/4 cada uno) y 0 (prob 1/2), el cambio esperado de $f$ sería $\frac14 f(d+2) + \frac12 f(d) + \frac14 f(d-2) - f(d) = \frac14 [f(d+2) - 2f(d) + f(d-2)]$, que es $\frac14$ veces el laplaciano discreto de paso 2.

Pero con el acoplamiento $\delta_i$ iid, el cambio de $d_i$ es $\Delta_{i+1} - \Delta_i$. Consideremos $\sum_i f(d_i)$. En el nuevo estado, $d_i' = d_i + \Delta_{i+1} - \Delta_i$. Entonces:

$$\sum_i f(d_i') = \sum_i f(d_i + \Delta_{i+1} - \Delta_i).$$

Esto es complicado, pero podemos elegir $f$ conveniente.

**Funciones de Bessel / $f$ adecuada para el acoplamiento**

Si elegimos $f$ que sea una función "aditiva" tipo $\lambda^{d}$, entonces $f(d_i + \Delta_{i+1} - \Delta_i) = \lambda^{d_i} \lambda^{\Delta_{i+1} - \Delta_i}$, y el producto sobre $i$ factoriza... pero estamos sumando, no multiplicando.

Probemos con $f(d) = \lambda^d$:

$$\mathbb{E}\left[\sum_i \lambda^{d_i + \Delta_{i+1} - \Delta_i}\right] = \sum_i \lambda^{d_i} \mathbb{E}[\lambda^{\Delta_{i+1} - \Delta_i}] = \sum_i \lambda^{d_i} \cdot \mathbb{E}[\lambda^{\Delta_{i+1}}] \mathbb{E}[\lambda^{-\Delta_i}] = \sum_i \lambda^{d_i} \cdot \left(\frac{\lambda + \lambda^{-1}}{2}\right)^2.$$

Queremos que esto sea igual a (o menor que) $V(d) - c$ para alguna martingala.

Si tomamos $\lambda$ tal que $\left(\frac{\lambda + \lambda^{-1}}{2}\right)^2$ ... hmm, vemos que el factor es $\cosh^2(\ln \lambda)$. Eso es $\ge 1$. Entonces $\mathbb{E}[\lambda^d]$ crece, es una submartingala, no martingala.

Necesitamos otra función. Consideremos $f(d) = d$ o $d^2$.

Para $f(d) = d^2$:

$$d_i' = d_i + \Delta_{i+1} - \Delta_i.$$

$f(d_i') = d_i^2 + 2 d_i(\Delta_{i+1} - \Delta_i) + (\Delta_{i+1} - \Delta_i)^2$.

Sumando sobre $i$ y tomando esperanza:

- $\sum_i d_i^2$: término principal.
- $2\sum_i d_i(\Delta_{i+1} - \Delta_i)$: esperanza 0 (los $\Delta$ tienen media 0).
- $\sum_i (\Delta_{i+1} - \Delta_i)^2 = \sum_i (\Delta_{i+1}^2 + \Delta_i^2 - 2\Delta_{i+1}\Delta_i) = \sum_i (1 + 1 - 2\Delta_{i+1}\Delta_i) = 2k - 2\sum_i \Delta_{i+1}\Delta_i$.

Esperanza de esto: $2k - 2\sum_i \mathbb{E}[\Delta_{i+1}\Delta_i] = 2k - 0 = 2k$ (ya que $\Delta$ son independientes y media 0).

Entonces $\mathbb{E}\left[\sum_i d_i'^2\right] = \sum_i d_i^2 + 2k$.

Espera, pero el término cruzado $2 d_i(\Delta_{i+1} - \Delta_i)$ tiene esperanza 0, pero al sumar, es una martingala (los incrementos centrados). Así que el drift es $+2k$ por paso. Entonces $\sum_i d_i^2$ es una submartingala con drift $+ 2k$ por paso.

Consideremos la martingala $M_t = \sum_i d_i(t)^2 - 2 k_t \cdot t$... no, el drift depende de $k$ que cambia en las fusiones.

Hmm, pero entre fusiones, $k$ es constante, así que $S_t := \sum_i d_i^2 - 2k t$ es una martingala entre fusiones.

El teorema de parada: cuando ocurre la primera fusión (algún $d_i = 0$), parémonos. El tiempo $T$ de primera fusión. Entonces:

$$\mathbb{E}\left[\sum_i d_i(T)^2\right] = \sum_i d_i(0)^2 + 2k_0 \mathbb{E}[T].$$

Espera, necesitamos que la martingala $S_t$ tenga $\mathbb{E}[S_T] = S_0$, usando parada opcional (si aplica). Entonces:

$\mathbb{E}[\sum_i d_i(T)^2 - 2k_0 T] = \sum_i d_i(0)^2$.

Entonces $2k_0 \mathbb{E}[T] = \mathbb{E}[\sum_i d_i(T)^2] - \sum_i d_i(0)^2$.

Esto requiere conocer $\mathbb{E}[\sum_i d_i(T)^2]$ en el instante de la primera fusión, lo cual no es inmediato porque depende de qué huecos colisionan.

**Enfoque con la regla de exclusión / mapeo a coalescencia de paseos**

Hay una conexión hermosa: este proceso de fusión es equivalente al proceso de "coalescencia" de paseos aleatorios simples con la regla de que cuando chocan, se pegan.

En particular, hay una dualidad con el movimiento browniano / paseos en un circuito.

Vamos a replantear el problema de forma más simple usando la observación de que el flujo total es conservado.

**Representación de las serpientes como "frentes"**

Cada serpiente tiene una cara izquierda y una cara derecha. Inicialmente, la serpiente ocupa 1 arco, así que su cara izquierda y derecha están a distancia 1. En total hay 30 caras (15 serpientes × 2 caras). 

Consideremos solo las caras: hay 30 caras en el círculo. Inicialmente están dispuestas como: cara derecha de S_1 en arco 0, cara izquierda de S_1 en arco 0... espera, una serpiente de longitud 1 ocupa un solo arco. Su cara izquierda y derecha están en el mismo arco (o mejor, la serpiente ocupa exactamente el arco, con caras en los extremos). Es más limpio pensar en la serpiente ocupando un arco, y las caras como los "bordes" izquierdo y derecho del arco.

Hmm, quizás sea más simple pensar en posiciones de las serpientes como puntos y la fusión cuando coinciden, ignorando longitudes, y luego ajustar.

Vamos a repensar con coordenadas de puntos móviles.

**Modelo con puntos que se fusionan al tocarse**

Cada serpiente se modela por su "centro" (o por un extremo). Como las longitudes suman 15 siempre, y hay inicialmente 15 serpientes de longitud 1, quizás podamos escalar.

Realmente, el resultado del problema debería depender solo de $n = 15$ serpientes y del tamaño de los huecos, no de las longitudes particulares, porque las longitudes no afectan a los huecos.

Así que el modelo reducido es: $N = 15$ partículas en un círculo de 30 posiciones relevantes (los huecos ocupan 30 unidades de "espacio de hueco", y las partículas son los límites de los huecos).

Bueno, sigamos con el enfoque de martingala de $d^2$ y las fusiones; es el método más prometedor.

**Estructura del proceso de fusión y la martingala $Q = \sum d_i^2$**

Reorganicemos: después de la primera fusión, tenemos $k = 14$ serpientes y 14 huecos. La suma de huecos sigue siendo 30. Uno de los huecos (el que colisionó) desapareció, y los otros dos huecos adyacentes... espera, cuidado.

Cuando el hueco $d_i = 0$, las serpientes S_i y S_{i+1} se fusionan. En el nuevo ordenamiento, la serpiente combinada S tiene a su izquierda el hueco $d_{i-1}$ y a su derecha el hueco $d_{i+1}$. Los huecos $d_{i-1}$ y $d_{i+1}$ no cambian instantáneamente al fusionarse (las caras externas no se mueven). Así que después de la fusión, los huecos son $d_1, \ldots, d_{i-1}, d_{i+1}, \ldots, d_k$ (se elimina $d_i = 0$).

Entonces $\sum d^2$ en el instante de fusión es $\sum_{j \ne i} d_j^2 = \sum_j d_j^2$ (ya que $d_i = 0$).

Muy bien. Vamos a intentar seguir el proceso completo con la martingala.

En cada fase (con $k$ serpientes), entre fusiones, $\sum d_i^2$ es submartingala con drift $2k$ por paso. El tiempo esperado de la fase $k$ (desde que tenemos $k$ serpientes hasta la próxima fusión, con $k-1$ serpientes) está relacionado con la diferencia de $\mathbb{E}[\sum d^2]$ (o $\mathbb{E}\sum d^2$) entre el inicio y el final de la fase.

Necesitamos $\mathbb{E}[\sum d^2]$ en el inicio de cada fase. Al inicio de la fase $k$, el estado es: $k$ huecos no nulos que suman 30, y "típicamente" el que acaba de fusionarse era 0, los demás podrían estar en una distribución.

Aquí es donde se complica. Pero hay un principio de "estado estacionario" o simetría.

**Cambio de perspectiva: tempo de coalescencia global**

En lugar de seguir fase por fase, consideremos una cantidad global cuya evolución sea una martingala sencilla y cuyo valor en el "absorbido" sea conocido.

Consideremos $Q(t) = \sum_i d_i(t)^2$. Entre fusiones, $Q$ crece con drift $2k$ donde $k$ es el número actual de serpientes. Total en el tiempo: cada paso incrementa $\mathbb{E}[Q]$ en $2k$. 

Entonces la martingala es $Q(t) - 2\int_0^t k(s)\,ds$, es decir, $Q(t) - 2\sum_{s=1}^{t} k(s)$.

En el instante final $T_{\text{final}}$ (cuando queda 1 serpiente), hay 1 hueco (de tamaño 30) y $Q = 900$. Al inicio, $Q_0 = 15 \times 2^2 = 60$.

Para usar parada opcional, el proceso debe ser tal que la martingala se conserve. Definamos $M(t) = Q(t) - 2\sum_{s \le t} k(s)$, donde $k(s)$ es el número de serpientes en el instante $s$. ¿Es $M$ una martingala?

Entre distintas fusiones, $k$ constante, y $\mathbb{E}[Q(t+1) - Q(t)] = 2k$. En los instantes de fusión, $Q$ no cambia (se elimina un cero), y $k$ decrece. No hay salto en $M$ en la fusión, porque $Q$ no cambia, y $\sum k$ es una suma sobre instantes, no hay salto. Así que $M$ es una martingala (habría que comprobar el drift en cada paso, que es $2k$).

Entonces, en el instante inicial, $M(0) = Q_0 = 60$.

En el instante final $T$, $Q(T) = 900$, y $\sum_{s=1}^{T} k(s)$ es la suma del número de serpientes a lo largo del tiempo. 

Necesitamos relacionar $\sum_{s=1}^T k(s)$ con el número esperado...

Espera, lo que queremos es $\mathbb{E}[T]$, el tiempo total. Y tenemos $M(T) = 900 - 2 \sum_{s=1}^{T} k(s)$.

Por parada opcional, $\mathbb{E}[M(T)] = M(0) = 60$, así que

$$900 - 2\,\mathbb{E}\!\left[\sum_{s=1}^T k(s)\right] = 60,$$

$$\mathbb{E}\!\left[\sum_{s=1}^T k(s)\right] = \frac{900 - 60}{2} = 420.$$

Hmm, pero esto involucra $\sum_{s=1}^T k(s) = \sum_{k=1}^{15} k \cdot (\text{tiempo en fase } k)$. Necesitamos $\mathbb{E}[T] = \sum_k \mathbb{E}[T_k]$, no $\sum_k k\, \mathbb{E}[T_k]$.

Necesitamos una segunda martingala para separar.

**Segunda martingala: $\sum_i d_i$**

$\sum_i d_i = 30$ es constante, no da información.

**Tercera: número de serpientes vs. huecos**

¿Hay una martingala que involucre directamente el tiempo? Consideremos una función $g(k, d)$.

Alternativamente, hay otra martingala natural: la suma de las posiciones al cuadrado o algo que permita despejar el tiempo.

Pensemos en las caras. Hay $2k$ caras en la fase $k$. Cada cara se mueve $\pm 1$ independientemente. Consideremos la suma de las posiciones de las caras al cuadrado. Como las caras son paseos aleatorios independientes, $\sum x_{\text{cara}}^2$ crece con drift $2 \times (\text{número de caras}) = 4k$ por paso (cada cara contribuye drift 2 a su cuadrado).

Pero las caras no son independientes a lo largo del tiempo (las caras internas desaparecen al fusionarse). Cuidado.

Hmm. Vamos a buscar una martingala $M_2$ cuyo drift sea proporcional a $k$, como $M_1$ ($Q - 2\sum k$). Si encontramos otra martingala como $N(t) = R(t) - c\sum_{s\le t} k(s)$ con el mismo drift en $k$, podemos combinar.

En realidad, $M_1 = Q - 2\sum_{s \le t} k(s)$ tiene drift $2k$. Para obtener una martingala con drift en $k$ y así poder despejar tanto $\mathbb{E}\sum k(s)$ como $\mathbb{E}\sum 1$, necesitamos otra cantidad con drift $ck$ y valor final conocido.

**Martingala con drift proporcional al número de serpientes: "energía de las caras"**

Consideremos las $2k$ caras del sistema. Cada cara (extremo de serpiente) es un paseo aleatorio simple: en cada paso se mueve $\pm 1$ independientemente.

Sea $P(t) = \sum_{\text{caras}} x_{\text{cara}}^2$ (donde $x$ es la posición desenrollada en la recta, y cuidado con la paridad/desenrollado).

En un paso, cada cara $x \to x + \delta$, $x^2 \to x^2 + 2x\delta + \delta^2$. Esperanza: $x^2 + 1$ (puesto que $2x\delta$ tiene esperanza 0, $\delta^2 = 1$). Así que drift $+1$ por cara, es decir, $+2k$ por paso.

Cuando dos serpientes se fusionan, las dos caras internas desaparecen: pasamos de $2k$ a $2(k-1)$ caras. La contribución a $P$ de esas dos caras se elimina. Pero en la fusión, las dos caras internas coinciden en la misma posición (se tocan), así que sus posiciones son iguales, y su contribución a $P$ es $2x^2$, que se elimina. Las caras externas no cambian.

Hmm, fusionemos: antes, caras: $x_L$ (izq de S_i), $x_R$ (derecha de S_{i+1})? Espera. S_i tiene caras $(a_i, b_i)$, S_{i+1} tiene caras $(a_{i+1}, b_{i+1})$. La cara derecha de S_i es $b_i$, la cara izquierda de S_{i+1} es $a_{i+1}$. Al fusionarse, $b_i = a_{i+1} - 1$ (se tocan: hueco 0 significa $a_{i+1} - b_i - 1 = 0$). Así que las caras internas están en posiciones $b_i = a_{i+1} - 1$, adyacentes.

La serpiente combinada tiene caras izquierda $a_i$ y derecha $b_{i+1}$. Las caras $b_i$ y $a_{i+1}$ ya no existen. Su contribución a $P$ era $b_i^2 + a_{i+1}^2$; al eliminarlas, $P$ pierde $b_i^2 + a_{i+1}^2$. Y la serpiente combinada sigue teniendo las caras $a_i, b_{i+1}$ (ya incluidas). Así que $P$ salta en $-b_i^2 - a_{i+1}^2$ en el instante de fusión.

Por lo tanto, $P$ no es continuo en las fusiones; tiene saltos negativos. Esto complica el uso directo, pero podemos incorporar los saltos si sabemos su esperanza.

En el instante de fusión, las caras internas cumplen $a_{i+1} = b_i + 1$. Los valores absolutos de las posiciones dependen del sistema de coordenadas (punto de referencia con deriva). Los $x$ realizan paseos aleatorios, así que sus valores dependen del tiempo y del desenrollado. Este enfoque se complica por la necesidad de elegir origen y desenrollado.

**Evitemos las posiciones; quedémonos con la estructura de huecos.**

Necesitamos una segunda cantidad con drift $c_k k$ por paso y valores finales/iniciales conocidos. 

Notemos que $\sum d_i$ tiene drift 0 (martingala constante). Consideremos $\sum_i d_i^2$ que tiene drift $2k$. ¿Qué tal $\sum_i (d_i - \bar d)^2$? Como $\bar d = 30/k$ es constante entre fusiones, $\sum (d_i - \bar d)^2 = \sum d_i^2 - 2\bar d \sum d_i + k\bar d^2 = \sum d_i^2 - 2\bar d \cdot 30 + k \cdot (900/k^2) = \sum d_i^2 - 60\bar d + 900/k = \sum d_i^2 - 1800/k + 900/k = \sum d_i^2 - 900/k$.

Así que la varianza de los huecos es $Q - 900/k$ (con drift de $Q$ igual a $2k$). Aún depende de $Q$.

**Otra martingala: producto o suma de exponenciales con autovalor correcto**

Volvamos a funciones exponenciales. Queremos una martingala. Consideremos la suma de $\lambda^{d_i}$ con $\lambda$ raíz de la unidad o soluciones específicas.

El factor por el que se multiplica en esperanza es $c(\lambda)^2$ donde $c(\lambda) = (\lambda + \lambda^{-1})/2$. Para que sea martingala, necesitamos... la esperanza de $\sum \lambda^{d_i}$ bajo el acoplamiento es $c(\lambda)^2 \sum \lambda^{d_i}$. Queremos que $c(\lambda)^2 = 1$, i.e. $c(\lambda) = \pm 1$, que requiere $\lambda = 1$ (o $\lambda = -1$ con ajustes de paridad). Para $\lambda = 1$, obtenemos el número de huecos $k$, que decrece en las fusiones: no es una martingala con drift temporal útil.

Hmm, pero podemos considerar $\lambda$ complejo con $|\lambda| = 1$: $\lambda = e^{i\theta}$, $c(\lambda) = \cos\theta$. Entonces $|c(\lambda)^2| = \cos^2\theta \le 1$. Entonces $\mathbb{E}|\sum\lambda^{d_i}|$ decrece: supermartingala. En realidad $\sum \lambda^{d_i}$ se multiplica en esperanza por $\cos^2\theta$, que es < 1 para $\theta \ne 0$. Así que $\mathbb{E}[\sum\lambda^{d_i}]$ decae geométricamente como $(\cos^2\theta)^t$: entonces $\sum \lambda^{d_i}$ es una "función propia" con autovalor $\cos^2\theta$. 

Esto da que $\sum_i \cos(\theta d_i)$ (parte real) satisface $\mathbb{E}[\sum\cos(\theta d_i')] = \cos^2\theta \sum \cos(\theta d_i)$ (¿con correcciones? A verificar).

Entonces $\Phi_\theta(t) = \sum_i \cos(\theta d_i(t))$ decae como $(\cos^2\theta)^t$ en esperanza, hasta que ocurren fusiones. Las fusiones eliminan un término $\cos(0)=1$ cuando $d_i=0$.

Esto sugiere un enfoque con funciones generatrices, pero el tiempo esperado todavía requiere integrar.

**Idea clave: la esperanza del tiempo de fusión está ligada a la "resistencia" y puede calcularse vía suma de $1/(\text{drift del número de huecos})$? No.**

Demos un paso atrás. Hay literatura sobre "coalescencia de paseos aleatorios" y "el proceso de los espacios vacíos". El problema de las serpientes es equivalente al siguiente:

**Reducción a coalescencia simétrica estándar**

Consideremos $N=15$ paseos aleatorios simples simétricos en $\mathbb{Z}$, moviéndose todos con pasos $\pm 1$. Cuando dos paseos adyacentes están a distancia 2 (hueco 2) o menos... inicialmente a distancia 3 (un arco ocupado + 2 vacíos = distancia 3 entre centros). Cuando la distancia entre centros de dos serpientes adyacentes llega a 1 (o 0), se fusionan.

Espera: inicialmente las serpientes están en arcos 0,3,6,...,42. Centros a distancia 3. Un hueco de 2 vacíos entre dos serpientes, más la propia serpiente ocupa 1. La "distancia" (hueco) mide espacios vacíos.

Si modelamos cada serpiente por un punto que se mueve en $\mathbb{Z}$ con paso $\pm 1$ cada segundo, y la condición de fusión de serpientes adyacentes cuando sus huecos llegan a 0, el hueco es $d = X_{i+1} - X_i - L$ para alguna constante $L$ de longitud.

Inicialmente $X_{i+1} - X_i = 3$ (distancia entre centros). El hueco es $X_{i+1} - X_i - 1 = 2$. Fusión cuando hueco 0, i.e. $X_{i+1} - X_i = 1$.

Así que serpientes adyacentes se fusionan cuando la distancia entre sus centros llega a 1 (y la serpiente fusionada se comporta con una cierta longitud, pero para el ordenamiento lo que importa es que el "centro" efectivo de la combinada... hmm, la longitud crece y complica la distancia).

**Reescalado para eliminar longitudes: el truco de las "cuentas"**

La suma de longitudes es 15 constante, suma de huecos 30. Si pensamos en los 45 arcos como recursos, realmente el sistema es equivalente a $N=15$ partículas. 

Propongo el siguiente modelo equivalente limpio: Hay $N=15$ partículas en un círculo con $45$ posiciones, y el proceso es el "modelo de votante / coalescencia aleatoria" en el que cada partícula se mueve... 

**Simplificación mediante la representación de "espacios en una fila"**

Alternativa concreta: como el hueco total es 30 y hay $k$ serpientes, la evolución de los huecos $(d_1,\ldots,d_k)$ con $d_i \to d_i + \Delta_{i+1} - \Delta_i$ es exactamente el proceso de "reordenamiento aleatorio": coloquemos $k$ caras móviles (las $\Delta$), y los huecos son las diferencias $d_i = c_{i+1} - c_i$ para "posiciones" acumuladas $c_i = \sum_{j < i} \Delta_j$ más una base.

Precisamente: define $c_i = \sum_{j \le i} \delta_j$ (posiciones acumuladas de las caras). Entonces $d_i = c_{i+1} - c_i - 1$... ajustemos.

Si las caras se mueven todas, y reindexamos, la $i$-ésima cara (parcial) en tiempo $t$ tiene posición $C_i(t) = C_i(0) + \sum_{s\le t} \delta_i(s)$. Los huecos $d_i(t) = C_{i+1}(t) - C_i(t) - 1$.

Esto es exactamente: los huecos son las "espaciaturas" entre líneas de un proceso de "empates" aleatorios. Cada cara es un paseo aleatorio simple, todos independientes, y los huecos son los gaps entre caras consecutivas. La fusión (hueco 0) corresponde a dos caras vecinas que están a distancia 1 (gap 0 significa $C_{i+1} - C_i = 1$, es decir, posiciones consecutivas). Cuando dos caras están a distancia 1, la serpiente combinada "une" las caras, y las caras internas dejan de contarse como caras de huecos.

En términos de las caras $C_i$: son paseos aleatorios simples independientes (en el desenrollado de la recta). Las serpientes adyacentes i e i+1 se fusionan cuando $C_{i+1} - C_i = 1$ (el hueco $d_i = 0$).

Cuando se fusionan, las caras $C_{i+1}$ (izquierda de S_{i+1}) y $C_i$ (derecha de S_i) siguen existiendo como paseos aleatorios, pero ya no definen huecos; la nueva serpiente combinada tiene caras externas dadas por... la cara izquierda de S_i (que es $C_i$? no...). 

Reorganicemos índices. Sea serpiente i con cara izquierda $L_i$ y cara derecha $R_i$. Hueco $d_i$ entre $R_i$ y $L_{i+1}$: $d_i = L_{i+1} - R_i - 1$. Hueco $d_{i-1}$ entre $R_{i-1}$ y $L_i$: $d_{i-1} = L_i - R_{i-1} - 1$.

Si $d_i = 0$ ($L_{i+1} = R_i + 1$), serpientes i y i+1 se fusionan. Nueva serpiente $S$ con cara izquierda $L_i$ y cara derecha $R_{i+1}$. Las caras $R_i$ y $L_{i+1}$ dejan de ser "caras" (dejan de definir huecos). El nuevo hueco entre $R_{i-1}$ y $L_i$ (que es $d_{i-1}$) sigue gobernado por $L_i$ y $R_{i-1}$. El nuevo hueco entre $R_{i+1}$ y $L_{i+2}$ (que era $d_{i+1}$) sigue gobernado por $R_{i+1}$ y $L_{i+2}$.

En resumen: **el sistema es exactamente equivalente a $2N = 30$ paseos aleatorios simples independientes (las caras originales), y cuando dos caras que delimitan un hueco quedan a distancia 1, ese hueco se "cierra" y las caras correspondientes ya no se consideran límites, pero siguen moviéndose sin ser observadas. Las caras activas siguen siendo paseos aleatorios simples independientes hasta que su hueco asociado se cierra.**

El tiempo en que se cierra un hueco es el tiempo en que dos paseos aleatorios independientes (sus caras límite) quedan a distancia $d_i$ inicial... es decir, la diferencia de dos paseos aleatorios simples independientes, que es un paseo aleatorio "compuesto" en $\mathbb{Z}$ con pasos $\{-2,0,2\}$.

La esperanza de que un hueco específico se cierre es infinita (paseo recurrente nulo en 1D). Por tanto, **el tiempo hasta la primera fusión tiene esperanza infinita**. 

¡Cuidado! Si el tiempo esperado de la primera fusión fuera infinito, la respuesta sería infinita. Pero el problema pide "el número esperado de segundos", lo cual sugiere respuesta finita. Hay una sutil contradicción que debemos resolver.

Miremos de nuevo: ¿es realmente recurrente nulo el gap? El gap evoluciona con pasos $\{-2,0,2\}$ (prob 1/4,1/2,1/4). Escalado al tiempo, es un paseo aleatorio simétrico "perezoso" en el retículo $2\mathbb{Z}$. Comenzando en 2, llega a 0 con probabilidad 1 (recurrente), pero el tiempo esperado de llegada es infinito.

Sin embargo, con 15 huecos acoplados, estamos preguntando el mínimo sobre soportes. El mínimo de varios tiempos de llegada de paseos recurrentes nulos tiene esperanza finita solo si hay suficiente acoplamiento... no podemos concluir directamente.

¡Pero! Recordemos que los huecos no son independientes: están acoplados y su suma es constante. Esa restricción cambia las cosas. Si un hueco quiere llegar a 0 manteniéndose positivo, los demás se ajustan. Comenzando en 2 cada uno, para que uno llegue a 0, una cara va hacia otra. No hay cota finita obvia.

Sin embargo, consideremos el acoplamiento: si miramos el hueco 1 ($d_1$), su proceso de transiciones depende de $\delta_2 - \delta_1$. Los otros huecos involucran $\delta_2, \delta_3, \ldots$, etc. La suma de todos es constante 30.

¿Podemos acotar el acoplamiento? Notemos que cada hueco es la diferencia de dos paseos simples, y conjuntamente, los gaps son las diferencias ordenadas de $k$ paseos simples. El "borde de menor gap" es como el mínimo de $k-1$ diferencias consecutivas.

Para que un hueco llegue a 0, dos paseos consecutivos (caras) deben coincidir (diferencia 0 en la versión reescalada). Entonces la primera fusión es cuando dos de los $k$ paseos (caras) coinciden por primera vez.

Espera, reformulemos con "cara izquierda = cara derecha de la serpiente anterior". Uno los huecos: $d_i = C_{i+1} - C_i - 1$. Hay $k$ caras $C_1, \ldots, C_k$ (cada serpiente separada por una cara), en orden $C_1 < C_2 < \cdots < C_k$ con gaps $d_i = C_{i+1} - C_i - 1$ (el espacio vacío). Cada cara $C_i$ es un paseo aleatorio simple independiente... no exactamente: el hueco entre serpiente i e i+1 está delimitado por la cara derecha de la serpiente i y la cara izquierda de la serpiente i+1. En la numeración desenrollada, la cara derecha de la serpiente i es $C_i^{(R)}$, y la cara izquierda de la serpiente i+1 es $C_{i+1}^{(L)}$. Ambas son paseos aleatorios simples independientes.

Para el hueco $d_i$, definimos $C_i^{(R)}$ y $C_{i+1}^{(L)}$, y $d_i = C_{i+1}^{(L)} - C_i^{(R)} - 1$.

Cada serpiente tiene dos caras independientes: eso sería $2k$ paseos. Pero el movimiento de una serpiente desplaza ambas caras juntas, así que $C_i^{(R)}$ y $C_i^{(L)}$ se mueven con el mismo $\delta_i$. Entonces hay $k$ "movimientos" $\delta_1, \ldots, \delta_k$ iid, y las caras se construyen como: $C_i^{(R)} = C_i^{(L)} + L_i$ (longitud de la serpiente), y ambas se desplazan en $\delta_i$.

Para el hueco $d_i = C_{i+1}^{(L)} - C_i^{(R)} - 1$, el cambio es $\delta_{i+1} - \delta_i$ como antes.

El hueco $d_{i-1} = C_i^{(L)} - C_{i-1}^{(R)} - 1$, cambio $\delta_i - \delta_{i-1}$.

Ok, coincide.

**Cota de esperanza finita mediante el acoplamiento de martingala**

Aunque cada hueco individual tiene tiempo de llegada infinito esperado, la primera llegada de uno entre varios acoplados puede tener esperanza finita. Hay un resultado: para una familia de martingalas, el mínimo de sus tiempos de llegada puede ser finito.

Consideremos el caso más simple: 2 serpientes, 2 huecos. Inicialmente d1 = 15, d2 = 15 (N=2, huecos suman 30). Las caras son 2 movimientos δ1, δ2. d1 cambia δ2-δ1, d2 cambia δ1-δ2 = -d1_incremento. Así que d2 = 30 - d1. El sistema es 1D: d1 paseo aleatorio (perezoso) en pares, desde 15, hasta llegar a 0 (con lo que d2=30). El tiempo esperado de d1 de 15 a 0 es $\mathbb{E}[T] = \infty$ (paseo simétrico). Entonces, con N=2, ¡la esperanza es infinita!

¿Significa eso que la respuesta al problema con N=15 es infinita? Hmm, pero el problema dice "compute the expected number of seconds", y es de una competencia (probablemente HMMT o similar), así que probablemente hay una respuesta finita específica. Debo haber modelado mal algo.

Repensemos si los movimientos de las serpientes están tan desacoplados.

"Cada serpiente se mueve independientemente una posición a la izquierda o a la derecha, cada una con probabilidad 1/2." 

Cuando una serpiente ocupa $L$ arcos, moverse a la izquierda/derecha desplaza toda la serpiente. Pero hay una sutilidad: una serpiente de longitud $L$ al moverse en una dirección, un extremo "tapa" un arco y el otro lo "libera". Los huecos a ambos lados cambian correlacionados como describí (ambas caras se desplazan en δ). Eso es correcto.

El caso N=2 con huecos 15 y 15: d1 hace paseo aleatorio perezoso desde 15 hasta 0, esperando infinito. Entonces para N=2 la respuesta sería infinita. Para N=15 con huecos 2 cada uno, cada hueco individual va de 2 a 0 con esperanza infinita, pero hay 15 intentos... 

Sin embargo, hay una diferencia crucial: para N=2, hay solo 2 huecos y están perfectamente anticorrelacionados (una dimensión). Suma constante fuerza d1 = 30 - d2, un único paseo 1D, recurrente nulo: esperanza infinita.

Para N=15, tenemos 15 huecos con suma fija 30, viviendo en un símplex de dimensión 14. Los gaps son las diffeas de 15 paseos acoplados. ¿Sigue siendo recurrente? El problema de coalescencia de paseos en 1D es recurrente (todos coalescen con probabilidad 1), pero el tiempo esperado de coalescencia completa es **infinito** en 1D. De hecho, es un resultado estándar: coalescencia completa de paseos aleatorios simples en $\mathbb{Z}$ tiene tiempo esperado infinito (porque la coalescencia del último par es un paseo recurrente nulo).

Pero aquí las fusiones "pegan" serpientes, y hay una cota superior: una vez fusionadas, se mueven juntas. La coalescencia de 2 paseos en 1D tiene tiempo esperado infinito. Por tanto, **el tiempo total para reducir a 1 serpiente debe tener esperanza infinita**, dado que la última fusión (de 2 a 1) es como un paseo 1D recurrente nulo.

A menos que la geometría circular (módulo 45) convierta el paseo en recurrente positivo (estado finito). ¡Ah, claro! El círculo es finito: 45 arcos. La diferencia entre serpientes está acotada (los huecos suman 30). Al ser un estado finito (el número de configuraciones es finito), la cadena de Markov es finita, y el tiempo de absorción esperado es **finito** siempre que la absorción sea alcanzable con probabilidad 1. 

Sí, en un círculo finito, las posiciones están módulo 45, y la diferencia entre serpientes adyacentes (hueco) está en $\{0, 1, \ldots, 42\}$ más la paridad. La cadena es finita. Por lo tanto, el tiempo esperado es finito. Mi modelo en $\mathbb{Z}$ desenrollado perdió la compacidad, pero como la suma de huecos es constante (30), el hueco máximo está acotado por 30, y cada hueco está en $\{0,\ldots,30\}$ con la paridad apropiada. Estado finito.

Entonces, cada hueco individual está acotado entre 0 y 30. Es un paseo aleatorio simétrico "perezoso" sobre un intervalo finito $[0, 30]$ (en pares), con absorción en 0. El tiempo esperado de llegar a 0 desde 2 (sin reflexión en 30, sino que la suma con otros huecos lo impone). En una cadena finita, el tiempo de absorción esperado desde el interior es finito.

Para el caso N=2, d1 está en $[0,30]$ y al llegar a 0 ocurre fusión. Con dos serpientes, d1 paseo en el intervalo finito $\{0,2,4,\ldots,28,30\}$ (paridad par), absorción en 0, y en el extremo 30 refleja. El tiempo esperado de absorción desde 15 sería finito. Mi afirmación de "esperanza infinita" era errónea porque ignoré la cota superior de 30 impuesta por el círculo.

Precisamente: con 2 serpientes, d1 + d2 = 30, d1 ∈ [0,30], y "absorbing" en d1=0. En el otro extremo d1=30 (d2=0) también absorbe. El paseo d1 en el intervalo finito {0,2,...,30} con absorción en ambos extremos. Título esperado desde 15 es finito (típicamente $15 \cdot 15/2$ en el paseo simple, escalado).

Bien. Entonces toda la configuración es una cadena de Markov finita; el tiempo esperado de absorción es finito.

**Ahora, la martingala $Q - 2\sum k$ y otra martingala para despejar el tiempo**

Con estados finitos, el teorema de parada opcional se aplica sin problema. Encontré $M_1(t) = Q(t) - 2\sum_{s\le t} k(s)$ es una martingala, con $Q = \sum d_i^2$, $k(s)$ = número de serpientes en el paso $s$ (o más formalmente, martingala continua en tiempo discreto: $\mathbb{E}[Q(t+1) - Q(t) | \mathcal{F}_t] = 2 k(t)$).

En el tiempo inicial $t=0$: $k_0 = 15$, $Q_0 = 15 \cdot 2^2 = 60$.
En el tiempo final $T$: $k_T = 1$, $Q_T = 30^2 = 900$.

Entonces $\mathbb{E}[900 - 2\sum_{s=1}^{T} k(s)] = 60$, luego $\mathbb{E}\sum_{s=1}^T k(s) = 420$ (como antes).

Necesitamos $\mathbb{E}[T] = \sum_T$. Pero $\sum_{s=1}^T k(s) \ge T$ siempre, no da T directamente.

Busquemos otra martingala $M_2$ con drift proporcional a $k$ (o a 1). Consideremos $\sum_i d_i = 30$ constante — no sirve.

¿Cuál es otra martingala que involucre $k$?

**Martingala del "potencial logarítmico" o armónico que dé drift unitario**

En una cadena finita, para calcular tiempos esperados se resuelve el sistema $T(x) = 1 + \sum P_{xy} T(y)$. Encontrar una martingala es equivalente a una solución armónica.

Alternativamente, consideremos la cantidad $\sum_i d_i^2$ con drift $2k$. Si encontramos otra cantidad con drift $2$ (constante) y valores finales conocidos, podemos combinar.

¿Existe una cantidad $R$ con $\mathbb{E}[R(t+1)-R(t)] = c$ constante (independiente de k) y valor final $R(T)$ conocido? Entonces $\mathbb{E}[R(T)] = R(0) + c\,\mathbb{E}[T]$.

La cantidad $\sum_i d_i^2$ tiene drift $2k$. Consideremos $\sum_i d_i^2 + 2\sum_{j<i}\ldots$? Busquemos algo con drift 2.

Notemos que para una cadena finita, $T$ es finito y podemos construir $R$ como la solución del sistema, pero necesitamos una cantidad explícita.

**Otra observación: resuelve el sistema de forma directa con la estructura de acoplamiento**

Quizás la manera correcta sea usar la dualidad con el número de caras y notar que el proceso es equivalente a coalescencia de glauber. Pero intentemos encontrar martingalas.

Consideremos la "frontera activa": cada hueco tiene dos caras. Un paseo aleatorio $X(t)$ con pasos ±1 en intervalo finito con absorción en ambos extremos tiene tiempo esperado $\mathbb{E}T = a b$ (para paseo simple, $h(x) = \mathbb{E}_x[T] = x\,(L - x)$... en pasos ±1, satisfaciendo $h(x) = 1 + (h(x-1)+h(x+1))/2$, solución $h(x) = x(L-x)$). En nuestro caso el paseo es perezoso con pasos $\{-2,0,2\}$, que es una versión "perezosa": en 2 pasos equivalentes a un paseo simple en el retículo de pares.

Vamos a escalar: nuestro hueco $d \in 2\mathbb{Z}$, transición a $d\pm2$ con prob 1/4 cada uno, y queda con prob 1/2. Reescalado $u = d/2$: $u \to u\pm1$ con prob 1/4 cada, queda con prob 1/2. Tiempo de llegada esperado $h(u)$ satisface $h(u) = 1 + \frac14 h(u-1) + \frac12 h(u) + \frac14 h(u+1)$ (en el interior, lejos de bordes). Reordenando: $\frac12 h(u) = 1 + \frac14(h(u-1)+h(u+1))$, i.e. $2 h(u) = 4 + h(u-1) + h(u+1)$, i.e. $h(u) = 4 + (h(u-1)+h(u+1))/2$. Comparado con paseo simple: $h = 1 + (h(u-1)+h(u+1))/2$. Entonces el tiempo esperado para el paseo perezoso es 4 veces el del paseo simple (intuitivo: cada paso perezoso avanza con probabilidad 1/2, así que se necesitan 4 veces más tiempo).

Para un hueco individual acotado en $[0, L]$ con absorción, el tiempo esperado desde $u_0$ hacia 0 es aproximadamente $4 \cdot u_0 \cdot (\text{distancia en u})$ ... pero debemos incluir el otro extremo.

Si ignoramos el acoplamiento y pensamos en un hueco aislado con absorción en 0 y reflectante en el extremo superior, el tiempo esperado desde 2 (u=1) sería $4 \cdot 1 \cdot (L_u - 1) = 4(L_u - 1)$... y con L=30, u_max=15: $4 \cdot 1 \cdot 14 = 56$. Hmm.

Pero el acoplamiento y las múltiples fases complican. Mejor buscar la martingala correcta.

**Martingala de la suma $\sum d_i$ no da tiempo; busquemos $S = \sum_i d_i(i)$?**

Las coordenadas de los huecos... hmm.

Volvamos a la observación de que el sistema se descompone en paseos independientes (caras) y las fusiones son eventos de "emparejamiento". 

Consideremos el siguiente punto: el proceso de huecos es exactamente la evolución de espaciados entre las trayectorias de un conjunto fijo de paseos aleatorios simples ($\delta$'s), pero las $\delta$'s originales siguen siendo iid incluso después de fusiones (las serpientes fusionadas eligen una sola $\delta$, y las caras internas ya no se observan, pero conceptualmente podemos mantener las $\delta$'s internas moviéndose iid sin afectar los huecos observados, ¡porque la elección de $\delta$ para la serpiente fusionada es una sola variable, y las caras internas, de continuar moviéndose iid, coinciden con esa variable? No, no exactamente).

Pero aquí hay un truco estándar: dado que las caras internas ya no se observan, podemos **ignorar** las caras internas y solo seguir las caras externas, que siguen siendo paseos simples independientes. En cualquier momento, hay $2k$ caras externas (2 por serpiente). La serpiente fusionada tiene 1 movimiento común; sus dos caras externas se mueven con el mismo δ. Eso es correcto.

Así que el sistema con $k$ serpientes: $k$ variables δ iid, y $2k$ caras externas dispuestas como pares (cada serpiente: cara izquierda y derecha, diferencia = longitud de la serpiente, fija entre fusiones). Los huecos son entre cara derecha de i y cara izquierda de i+1.

El hueco $d_i$ es la diferencia entre dos caras cuyas velocidades son δ_{i+1} y δ_i. Las caras de la misma serpiente comparten δ.

**Martingala con $d$ en términos de sumas parciales de δ**

Como $d_i \to d_i + \delta_{i+1} - \delta_i$, a lo largo del tiempo $d_i(t) = d_i(0) + \sum_{s \le t}[\delta_{i+1}(s) - \delta_i(s)] = d_i(0) + S_{i+1}(t) - S_i(t)$, donde $S_i(t) = \sum_{s\le t}\delta_i(s)$.

Aquí $S_i$ son paseos aleatorios simples independientes.

Los huecos finales: cuando solo queda 1 serpiente, hay 1 hueco de tamaño 30. ¿Cuál es la longitud final? Longitud final = 15, hueco 30.

Y los huecos se relacionan con las posiciones de las serpientes. La posición (en la recta desenrollada) de la cara derecha de la serpiente i es $X_i(t) = X_i(0) + S_i(t)$ (más contribución de longitud, que es constante entre fusiones, ¡pero cambia en fusiones! Hmm, la longitud afecta a la posición de la cara, pero solo añade una constante).

Vamos a usar únicamente las variables de hueco, que no dependen de longitudes.

**Buscar una martingala adicional: $\sum d_i^2$ ya da vínculo; necesitamos algo como $\sum_i i \cdot d_i$ (primer momento ponderado).**

Calculemos el drift de $W = \sum_i a_i d_i$ con pesos $a_i$ fijos: drift 0. No.

Calculemos $\sum d_i^2$ con drift $2k$ (ya lo tenemos). ¿Qué función daría drift $2$? No hay función local con drift constante 2 de forma obvia, porque el drift de cualquier $f(d)$ para un solo hueco es $\frac14[f(d+2)+f(d-2) - 2f(d)]$ (espera, el drift es $\frac14 f(d+2) + \frac12 f(d) + \frac14 f(d-2) - f(d) = \frac14[f(d+2) - 2f(d) + f(d-2)]$). Para $f=d^2$: $\frac14[2(d^2+4) - 2d^2] = \frac14[2d^2+8-2d^2] = 2$. Así que **por hueco, el drift de $d^2$ es 2** (no $2k$ total). Ajustemos: la contribución individual de un hueco al drift es 2 (dado que el hueco está lejos de los bordes que imponen restricciones por la suma). Pero en el acoplamiento, la suma sobre huecos del drift de $d^2$ es $2 \times (\text{número de huecos}) = 2k$, por aditividad. Sin embargo, ojo: el drift por hueco es 2 independientemente de k, lo que sugiere que el drift total es $2k$ porque hay k huecos.

¿Hay una función $f$ con drift **1** por hueco (constante, no dependiendo de d)? Por ejemplo $f(d) = d/2$? Drift de $f(d)=d$ es 0 (simétrico). 

Consideremos $f(d) = |d - c|$ para algún centro: más complicado.

Consideremos $f(d) = \mathbf{1}[d \text{ algo}]$... no.

¿$f(d) = d(d-2)$? Drift: $\frac14[(d+2)(d) + (d-2)(d-4) - 2d(d-2)]$. Calculemos: $d(d+2) = d^2 + 2d$; $(d-2)(d-4) = d^2 - 6d + 8$; suma = $2d^2 -4d + 8$; $-2 d(d-2) = -2d^2 + 4d$; total interno = 8. Drift = $8/4 = 2$. Mismo drift 2.

De hecho el drift es proporcional a la "segunda derivada" de $f$. Para drift 1, necesitamos $f$ con $\Delta^2 f = 1$, i.e. $f(d) = \frac14 d^2$ (drift 1/4 del laplaciano = 1/4 * 4 = ...). Es decir, $f = d^2/4$ da drift $1/2$ por hueco. En general, si $g(d)$ satisface $\frac14[g(d+2) - 2g(d) + g(d-2)] = c$ (constante), entonces $g$ es cuadrática $g(d) = c d^2 +$ términos lineales (los lineales dan drift 0).

Así que todas las funciones con drift constante son cuadráticas con drift $\frac14\Delta^2 g$: para $g = \alpha d^2 + \beta d + \gamma$, drift = $2\alpha$ por hueco (β,γ contribuyen 0). Para drift 1 por hueco, $\alpha = 1/2$. Es decir $g(d) = \frac12 d^2$ da drift 1 por hueco. (El drift de $\frac12 d^2$ es $\frac12 \cdot 2 = 1$. ¡Ah, drift 1!)

Así que $g(d) = \frac12 d^2$ tiene drift 1 por hueco, y $Q = \sum d_i^2$ corresponde a $\alpha = 1$ con drift $2k$. 

Para drift total 1 (independiente de k), usaríamos $\sum \frac12 d_i^2 = \frac12 Q$ con drift $k$. No ayuda directamente.

Necesitamos una cantidad con drift constante (como 1) total, no proporcional a k. El problema: el drift se acumula por hueco, así que cualquier cantidad natural da drift proporcional a k. Para drift constante, necesitaríamos una cantidad que dependa inversamente de k, como un promedio.

**Martingala del promedio: $\frac{1}{k}\sum d_i^2$?**

$\frac{1}{k}Q$ tiene drift $\frac{1}{k}\cdot 2k = 2$ constante. Pero $k$ cambia en fusiones, generando saltos. Definamos en la fase con $k$ serpientes $V_k = \frac{1}{k}\sum d_i^2$. Entre fusiones, drift 2. En una fusión de $k \to k-1$: $V$ salta de $\frac{Q}{k}$ a $\frac{Q}{k-1}$ (ya que Q no cambia al eliminarse un 0). El salto es $\frac{Q}{k(k-1)}$.

Además, en la fusión, el hueco que colisiona es 0, y no cambia Q, correcto.

Si definimos $M(t) = \frac{Q(t)}{k(t)} - 2t$: entre fusiones, $\mathbb{E}[\Delta M] = 0$ (drift 2 de Q/k menos 2). En la fusión, M salta por $Q/(k(k-1))$. Esperanza del salto desconocida.

Sabemos Q ≥ ... en cualquier caso. En el estado final, Q/k = 900/1 = 900. Inicial Q/k = 60/15 = 4.

Entonces $M(T) = 900 - 2T$. Inicial $M(0)=4$. Suma de saltos en fusiones: $M(T) - M(0) = 900 - 2T - 4 = \sum_{\text{fusiones}} \text{salto}_j$, donde salto_j = $\frac{Q_j}{k_j(k_j-1)}$ (de k_j a k_j-1).

Por martingala, $\mathbb{E}[M(T)] = M(0) + \mathbb{E}[\sum \text{saltos}]$, pero los saltos están en la misma probabilidad... Si M es una martingala (incluyendo saltos con esperanza condicional 0?), el salto en la fusión es determinista dado el estado: $\frac{Q}{k(k-1)} > 0$, esperanza positiva. Entonces M no es martingala a través de las fusiones; es submartingala (salta hacia arriba). Entonces $\mathbb{E}[M(T)] > M(0)$, y

$900 - 2\mathbb{E}T > 4$, luego $\mathbb{E}T < 448$.

No es suficiente. Necesitamos contabilizar los saltos.

Hmm, los saltos $\frac{Q}{k(k-1)}$ en cada fusión. Si sumamos sobre las 14 fusiones, con k de 15 bajando a 2, los saltos son $\sum_{k=2}^{15} \frac{Q_{\text{justo antes de la fusión de k a k-1}}}{k(k-1)}$.

Esto reintroduce la dependencia en Q en cada fusión. Necesitaríamos conocer $\mathbb{E}[Q]$ antes de cada fusión. 

**Retomar Q-martingale por fases y resolver el sistema de forma recursiva**

Dado que el estado es finito y hay estructura, planteemos las martingalas por fase con la esperanza condicional de Q.

Para la fase k (k serpientes, k huecos, suma de huecos = 30, absorción cuando alguno llega a 0). Las transiciones de huecos: en cada paso, cada hueco $d_i \to d_i + \delta_{i+1}-\delta_i$ con $\delta$ iid ±1. Las posiciones de huecos acoplados.

Cantidad central $Q = \sum d_i^2$. En cada paso (en el interior del símplex, sin alcanzar borde), $\mathbb{E}[\Delta Q] = 2k$.

En el instante de absorción (algún hueco 0), Q es igual a $\sum_{j \ne i} d_j^2$ con $d_i=0$.

El valor esperado de Q justo antes de la absorción menos... ¿podemos encontrar $\mathbb{E}[Q_{\text{antes de fusión}}]$? Por parada opcional de la martingala $Q - 2k t$ entre fusiones:

Sea $T_k$ el tiempo de la fase k (desde k serpientes hasta k-1). Sea $Q_k^{\text{start}}$ el valor de Q al inicio de la fase k, y $Q_k^{\text{end}}$ el valor al final de la fase (inicio de fase k-1). Como Q no cambia en la fusión, $Q_{k-1}^{\text{start}} = Q_k^{\text{end}}$.

Por parada opcional de la martingala $Q(t) - 2k t$ hasta el tiempo $T_k$:

$$\mathbb{E}[Q_k^{\text{end}}] - \mathbb{E}[Q_k^{\text{start}}] = 2k\,\mathbb{E}[T_k].$$

Necesitamos $\mathbb{E}[Q_k^{\text{end}} - Q_k^{\text{start}}]$, es decir, cuánto aumenta Q durante la fase. Eso requiere conocer la distribución. Hay un vínculo adicional: en el instante de fusión, el hueco que colisiona es 0, y los demás... su distribución condicionada al evento de fusión es complicada.

Pero podemos usar otra martingala por fase: la cantidad $Q$ es submartingala, no hay una martingala obvia de segundo orden con valor final conocido.

**Enfoque diferente: resolución mediante la "caja" y las caras esenciales**

De nuevo, notemos que el proceso de huecos es un proceso de **coalescencia** muy específico. Hay un resultado estándar para el problema "N partículas en el círculo, se mueven con paso ±1, se pegan al chocar" que da una fórmula cerrada. Vamos a derivarlo.

**El tiempo esperado de coalescencia completa para caminatas que se pegan en un ciclo: resultado de coalescencia de paseos**

Modelo equivalente limpio: Consideremos $N$ paseos aleatorios simples independientes en $\mathbb{Z}_m$ (ciclo de longitud m), empezando en posiciones distintas, moviéndose con pasos ±1. Cuando dos paseos (adyacentes en el orden) coinciden, se fusionan y se mueven juntos (se "pegan"). ¿Cuál es el tiempo esperado hasta que todos estén fusionados?

En realidad, lo que hemos derivado (huecos con suma conservada) representa la estructura correcta. Con $N$ partículas en ciclo de longitud $m = 45$, y espacios iniciales.

La versión continua de este problema (movimiento Browniano en el círculo con coalescencia al contacto) tiene una respuesta conocida por el "proceso de Kingman" o por la suma de tiempos de pares, pero la versión discreta es lo que tenemos.

**La clave: conexión con paseos en $\mathbb{Z}$ desenrollado sin perder finitud**

Como el círculo es finito, los huecos están en $\{0, 1, \ldots, 30\}$, pero con la suma total fija 30 y las paridades. En particular, en la fase k, los huecos son $k$ enteros no negativos (de cierta paridad) que suman 30. La cadena de Markov es el "proceso de exclusión" sobre estos huecos.

Para una cadena finita, el tiempo esperado satisface el sistema lineal. Podemos resolverlo aprovechando que **la suma de huecos es constante y el drift de Q es $2k$** junto con **otra martingala: el número de huecos en 0**... Hmm.

**Tal vez la respuesta esté ligada a $\sum_{k=2}^{N} \mathbb{E}[T_k]$ con una fórmula por fase usando el potencial armónico de "energía"**

Hay una técnica para coalescencia en 1D: el tiempo de coalescencia se puede analizar con la martingala $\sum_{1 \le i < j \le N} |X_i - X_j|$ o con las "estadísticas de los gaps".

Para nuestro proceso en el círculo, la cantidad $Q = \sum d_i^2$ tiene drift $2k$. En el paso final (k=2), los huecos son $d_1 = x$, $d_2 = 30 - x$ con $x \in \{0,2,\ldots,30\}$, y Q = $x^2 + (30-x)^2$. El hueco absorbe en $x=0$ o $x=30$.

Podemos resolver la fase k=2 exactamente. Después, por inducción, quizás.

**Cálculo de la fase k=2 (dos serpientes)**

Dos serpientes, huecos $x$ y $30-x$, $x$ par. En cada paso, $\delta_1, \delta_2 \in \{\pm1\}$ iid.

$d_1 \to d_1 + \delta_2 - \delta_1$. Como $d_2 = 30 - d_1$, todo se reduce a $d_1 = x$. Incremento $\delta_2 - \delta_1 \in \{-2, 0, 2\}$ con probs $(1/4, 1/2, 1/4)$.

En $x \in \{2, 4, \ldots, 28\}$ interior, $x \to x \pm 2$ (prob 1/4 cada) o queda (1/2). En $x = 30$, $\delta_2 - \delta_1 = -2$ lo manda a 28; $\delta_2-\delta_1=0$ lo deja; $\delta_2 - \delta_1 = 2$ lo mandaría a 32 pero eso no es posible porque d2 sería -2. Ah, cuidado: con la suma fija 30, $d_1 = x$, $d_2 = 30-x$. Si $x=30$, $d_2=0$, ya es absorción (fusión). Entonces realmente $x$ puede llegar a 30 solo si no ha habido absorción... pero $x=30$ significa $d_2=0$, ya fusionadas. Entonces el estado absorbente es x=0 o x=30; el estado inicial de la fase 2 es $x \in \{2,4,\ldots,28\}$ par.

Transición en el interior $x \in \{2,\ldots,28\}$: a $x-2$ prob 1/4, a $x$ prob 1/2, a $x+2$ prob 1/4. Absorción en $x=0$ o $x=30$.

En términos de $u = x/2$, $u \in \{1, \ldots, 14\}$, transición a $u\pm1$ prob 1/4, queda prob 1/2. Absorción en $u=0$ o $u=15$.

Sea $h(u)$ el tiempo esperado desde $u$ (interior $1 \le u \le 14$) hasta absorción en $\{0, 15\}$.

Ecuación: para $1 \le u \le 14$:

$$h(u) = 1 + \frac14 h(u-1) + \frac12 h(u) + \frac14 h(u+1),$$

con $h(0) = h(15) = 0$.

Espera, en $u=14$: transición a 15 con prob 1/4 (absorción, h(15)=0), a 14 con prob 1/2, a 13 con prob 1/4. Correcto.

Reordenando: $\frac12 h(u) = 1 + \frac14[h(u-1)+h(u+1)]$, luego

$$2 h(u) = 4 + h(u-1) + h(u+1),$$

$$h(u+1) - 2h(u) + h(u-1) = -4.$$

Solución general: $h(u) = A + Bu - 2u^2$ (puesto que la segunda diferencia de $u^2$ es 2, la de $-2u^2$ es $-4$).

Condiciones: $h(0)=0 \Rightarrow A = 0$. $h(15) = 0$: $15B - 2\cdot 225 = 0 \Rightarrow 15B = 450 \Rightarrow B = 30$.

Entonces $h(u) = 30u - 2u^2 = 2u(15 - u)$.

Para la fase 2 con $u$ inicial igual a... al inicio de la fase 2, ¿cuál es $u$? Cuando las últimas dos serpientes se forman (fusión de 3→2), el hueco final entre las dos serpientes restantes es un valor. Pero recordemos que al inicio de la fase 2 (después de que quedan 2 serpientes), hay 2 huecos que suman 30. ¿Cuál es su distribución? Simétrica; en promedio cada hueco es 15, pero es aleatorio. Concretamente, al pasar de 3 a 2 serpientes, el hueco eliminado era 0, y los dos huecos restantes (originalmente los otros dos) quedan. A lo largo del proceso, la distribución de huecos en la fase k tiene cierta estructura.

Pero notemos que la martingala Q da el vínculo. Para la fase 2, $\mathbb{E}[T_2] = \mathbb{E}[h(u)]$. Si la distribución de $u$ al inicio de la fase 2 es uniforme sobre $\{1,\ldots,14\}$ (simétrica), entonces $\mathbb{E}[h(u)]$ se promedia. Pero no sabemos si es uniforme.

**¡Idea! Usar la martingala Q en la fase 2 para despejar $\mathbb{E}[T_2]$ en términos de $\mathbb{E}[Q]$ inicial y final.**

En la fase 2, $Q = x^2 + (30-x)^2 = 2x^2 - 60x + 900$. En $u = x/2$: $x = 2u$, $Q = 8u^2 - 120u + 900 = 8u^2 - 120u + 900$. Hmm.

En términos de h: ya la resolvimos.

**Enfoque global con dos martingalas: Q y el "grado" (número de serpientes)**

Tenemos $M_1(t) = Q(t) - 2\sum_{s\le t} k(s)$ martingala (usando k(s) = número de serpientes en el paso s). Esto es correcto.

Construyamos $M_2(t) = N(t) - \sum_{s \le t} 1$ claramente $N(t) =$ número de serpientes $k(t)$, que satisface $\mathbb{E}[k(t+1) - k(t)] =$ esperanza del cambio en número de serpientes. No es 1; el número de serpientes decrece de a una, y decrece solo en fusiones. Entre fusiones, $k$ constante. Así que $k(t)$ no tiene drift en tiempo; es una "martingala" trivial con saltos. 

Definamos correctamente $M_2(t) = k(t) + \sum_{\text{fusiones} \le t} 1$, que es constante = 15. Inútil.

**Buscar martingala cuyo drift sea 1 y valor final conocido**

¿Qué tal $L(t) = \sum_{i} d_i \log$? El drift de una función de un solo hueco es $\frac14 \Delta^2 f$. Solo las cuadráticas tienen drift constante. Hmm.

¿Qué tal una función del estado global, como $\sum_{i} d_i^2 d_j$? El drift sería polinomio en d y k, no constante.

**Enfoque de martingala con peso $2^k$ o similar para absorber las fusiones**

Consideremos la cantidad $R(t) = Q(t) + 2\sum_{j=1}^{t} k(j)$ ya es martingala. Otra idea: la cantidad $P(t) = \sum_i d_i^2 + 2 \sum_{j<i} \ldots$ no.

**Vamos a resolver el sistema completo mediante la estructura de "paseos que no se cruzan"**

Para una cadena de Markov sobre configuraciones con estructura simétrica de intercambio, quizás el tiempo esperado solo depende de $N$ y de la suma total, y se puede obtener argumentando que el proceso es igual al de **paseos coalescentes en el círculo**, para el cual hay una fórmula conocida: el tiempo esperado de coalescencia total sobre $m$ posiciones con $N$ partículas es

$$\mathbb{E}[T] = \frac{m^2}{4}\sum_{k=2}^{N}\frac{1}{k(k-1)}\cdot (\text{algo})$$

No recuerdo. Derivemos con cuidado usando el sistema PE (proceso de exclusión).

**Formulación alternativa vía "diferencias antipodales" — el proceso de He / Balanced**

Consideremos la transformación $d_i / 2 = u_i$ con $u_i$ positivos sumando $S = 15$ (ya que $\sum d_i = 30 \Rightarrow \sum u_i = 15$). En la fase con k serpientes, hay k huecos con $\sum u_i = 15$ (u_i enteros). Cada u_i hace un "paseo perezoso": u_i -> u_i ± 1 prob 1/4, queda prob 1/2, con el acoplamiento de que la suma se conserva. Este es el proceso de exclusión simétrica **perezoso** en un grafo completo: los huecos son como "huecos" y la partícula... 

En realidad, este proceso es el **proceso de coagulación** dual al proceso de coalescencia. Los u_i representan los tamaños de los espacios.

Consideremos la dualidad: El vector de huecos $(u_1, \ldots, u_k)$ con suma 15 evoluciona de la siguiente manera: hay un único "token" de incremento/decremento en cada hueco por cada sello. Más precisamente: cada paso, cada hueco trata de incrementar o decrementar en 1, pero el acoplamiento es: para cada hueco i, hay un signo $\epsilon_i \in \{-1,+1\}$ (el movimiento de la cara derecha) y un signo $\epsilon_{i-1}$ (cara izquierda): $u_i \to u_i + (\epsilon_i - \epsilon_{i-1})/2$... con la restricción de que la suma se conserve (lo cual se da automáticamente). 

En términos de los $\epsilon_i$ iid ±1: las "partículas activas" son los $\epsilon_i$, y cada hueco $u_i$ cambia en $(\epsilon_i - \epsilon_{i-1})/2$. Si $\epsilon_i = \epsilon_{i-1}$, hueco i no cambia; si $\epsilon_i \ne \epsilon_{i-1}$, hueco i cambia en ±1 simétricamente.

Espera, $(\epsilon_i - \epsilon_{i-1})/2 \in \{-1, 0, 1\}$: -1 si $\epsilon_i=-1, \epsilon_{i-1}=+1$; 0 si iguales; +1 si $\epsilon_i=+1, \epsilon_{i-1}=-1$. Correcto, prob: +1 con 1/4, 0 con 1/2, -1 con 1/4.

La absorción (fusión) ocurre cuando algún $u_i = 0$... espera, $u_i$ es el hueco $d_i/2$. $d_i=0 \iff u_i = 0$. Al fusionarse, ese u_i se elimina, y las serpientes se unen.

**Dualidad con "unificación de monedas"**

El vector de gaps con suma fija 15, cada paso intercambia flujo: el proceso de exclusión simétrico sobre el "grafo de huecos" es en realidad el proceso de **intercambio aleatorio** de las "etapas": los $\epsilon$ representan "peldaños" y los huecos son las diferencias.

Consideremos la suma parcial $S_j = \sum_{i<j} u_i$ (el tamaño cumulativo). Cada $u_i = S_{i+1} - S_i$. Al hacer $u_i \to u_i + (\epsilon_i - \epsilon_{i-1})/2$, la suma parcial $S_j \to S_j + \epsilon_{j-1}/2 - \epsilon_0/2$? Espera, la suma de cambios hasta j: $\sum_{i<j} (u_i + \epsilon_i/2 - \epsilon_{i-1}/2) = S_j + \epsilon_{j-1}/2 - \epsilon_{-1}/2$. Con condiciones periódicas $\epsilon_{-1} = \epsilon_{k-1}$ (si numeramos cíclicamente, la cara de la serpiente 1 es $\epsilon_1$, y el hueco k usa $\epsilon_1 - \epsilon_k$).

Entonces $S_j \to S_j + \epsilon_{j}/2 - \epsilon_{k}/2$? Definamos con cuidado cíclico. Numeremos las caras (serpientes) $1, \ldots, k$. Hueco $u_i$ entre cara i y cara i+1 (con i+1 módulo k). Cambio $u_i \to u_i + (\epsilon_{i+1} - \epsilon_i)/2$.

Sumas parciales: definamos $T_j = 2\sum_{i<j} u_i$. Entonces $T_{j} - T_{j-1} = 2 u_{j-1}$. Tras un paso, $2u_i' = 2u_i + \epsilon_{i+1} - \epsilon_i$. Entonces $T_j' = \sum_{i<j} 2u_i' = T_j + \sum_{i<j}(\epsilon_{i+1}-\epsilon_i) = T_j + \epsilon_{j} - \epsilon_1$. 

Entonces $T_j$, la posición cumulativa de la cara j (en coordenadas de huecos), cambia como $T_j \to T_j + \epsilon_j - \epsilon_1$. Donde $\epsilon_j \in \{\pm1\}$ es un paseo aleatorio simple.

Vamos a definir la posición real de la cara j: $P_j(t) = P_j(0) + \sum_{s\le t}\epsilon_j(s)$. Es un paseo aleatorio simple.

Y $2u_i(t) = P_{i+1}(t) - P_i(t)$. ¡Esto es limpio! El hueco $u_i = (P_{i+1} - P_i)/2$, y $P_j$ son paseos aleatorios simples independientes en $\mathbb{Z}$.

Fusión cuando $u_i = 0 \iff P_{i+1} - P_i = 0$, es decir, dos paseos consecutivos coinciden.

Al fusionar serpientes i e i+1 (cuando $P_{i+1} = P_i$), la serpiente combinada tiene un solo movimiento; conceptualmente, eliminamos el paseo $P_{i+1}$ (o $P_i$) del conjunto de fronteras. Los paseos restantes siguen siendo paseos simples independientes.

**Resultado crucial**: El proceso es idéntico al siguiente modelo: $N=15$ paseos aleatorios simples independientes en $\mathbb{Z}$, empezando en posiciones $0, 3, 6, \ldots, 42$ (distancias entre $P$ corresponden a $2u = d$). Dos paseos consecutivos en el orden se fusionan (uno de ellos se elimina) cuando coinciden. Queremos el tiempo esperado hasta que quede un solo paseo.

Ojo, pero la fusión no es "coincidir" exactamente, sino $P_{i+1} - P_i = 0$. Comenzando con $P_{i+1} - P_i = 2u_i = d_i = 2$, i.e. diferencia 2. La fusión ocurre cuando la diferencia llega a 0.

Espera, $P$ están en $\mathbb{Z}$ y los huecos originales son $d_i = 2$, así que $P_{i+1}(0) - P_i(0) = 2$. Fusión cuando diferencia 0.

Dos paseos simples independientes con diferencia inicial 2 coalescen (diferencia 0) con probabilidad 1. Una vez que la diferencia toca 0, se fusionan y uno se elimina.

Cuando quede 1 paseo, fin.

Este es exactamente el proceso de **coalescencia secuencial de paseos aleatorios simples en $\mathbb{Z}$**, donde las partículas (fronteras) se mueven independientemente y, cuando dos partículas adyacentes coinciden, una se elimina.

La diferencia entre partículas adyacentes $i$ e $i+1$ es un paseo aleatorio simple (pasos ±2 compuestos, o dobles), desde 2 hasta 0. En $\mathbb{Z}$ desenrollado no hay cota, pero la suma total de diferencias está fija (30), así que en realidad el sistema está en un simplex compacto; sin embargo, en el modelo de paseos en $\mathbb{Z}$ las diferencias están acotadas por la suma total 30, así que está bien.

**La coalescencia de paseos en $\mathbb{Z}$ con suma de diferencias constante: construcción de la martingala con $\sum P_i^2$**

Ahora, en el modelo de paseos $P_1, \ldots, P_k$ independientes, cada uno $P_i \to P_i \pm 1$. La suma $V = \sum_i P_i^2$ tiene drift $k$ por paso (cada $P_i$: $E[P_i'^2] = P_i^2 + 1$). En las fusiones, se elimina un paseo (que coincide con otro), y V salta.

Los huecos $u_i = (P_{i+1} - P_i)/2$ y $Q = \sum d_i^2 = 4\sum u_i^2 = \sum (P_{i+1} - P_i)^2$.

Para la coalescencia de paseos con velocidades acopladas, hay una martingala clásica: consideremos $\sum_{1\le i<j\le k} |P_i - P_j|$. Al eliminar una partícula, esta cantidad salta. Como las partículas que se fusionan coinciden, y estamos en orden lineal, los pares adyacentes...

**Enfoque: coalescencia de paseos en 1D — tiempos de pares y la martingala $\Phi$**

Cuando dos paseos independientes se mueven con pasos ±1, su diferencia es un paseo simple (pasos -2,0,2), y el tiempo esperado para que su diferencia llegue a 0 desde 2 (sin interacción con otros) es infinito en $\mathbb{Z}$. Pero en el símplex acotado es finito. La finitud proviene de la cota por la suma total.

En el modelo de paseos en $\mathbb{Z}$ sin cota, coalescencia completa tiene tiempo esperado infinito. La finitud del círculo garantizado por $\sum d_i = 30$ constante es esencial. Entonces hay que incluir la cota en los paseos como sigue: como la suma de diferencias $2\sum u_i = 30$ es constante, cada $u_i \le 15$, y cada $P_{i+1} - P_i \le 30$. Es un sistema finito.

**Resolver el sistema vía exclusión simétrica perezosa en el símplex**

Tenemos en la fase k: $(u_1, \ldots, u_k)$ con $u_i \ge 0$, $\sum u_i = 15$ (ojo: $u_i = d_i/2$, con $d_i$ par, así que $u_i$ entero), y absorción cuando algún $u_i = 0$.

Transición: cada paso, $\epsilon_i \in \{\pm1\}$ iid ($i=1..k$), y cada $u_i \to u_i + (\epsilon_{i+1} - \epsilon_i)/2$.

Esto es el **proceso de exclusión simétrica perezoso** sobre $k$ sitios en un ciclo, con suma total 15, y hay un "sello" por sitio de la forma $(\epsilon_{i+1} - \epsilon_i)$ que suma 0.

Notemos que si $\epsilon_i = \epsilon_{i+1}$, hueco i no cambia; si difieren, hueco i cambia ±1. En cada paso, los "aristas activas" son aquellas donde $\epsilon_i \ne \epsilon_{i+1}$ (un dominio wall). En esas aristas, el hueco i cambia: +1 si $\epsilon_{i+1}=+1,\epsilon_i=-1$, o -1 en el caso opuesto.

La velocidad de cada hueco i es $\epsilon_{i+1} - \epsilon_i$, que es un gradiente de los $\epsilon$ en el ciclo. La suma de velocidades es 0.

Este es **exactamente** el proceso "tagged" asociado a colas, y es equivalente al proceso de **TASEP/SSEP en el ciclo** con velocidad por salto y el "hueco activo" es donde $\epsilon$ cambia de signo.

Hay un resultado clásico: el tiempo esperado de coalescencia para este proceso está relacionado con la **martingala de las posiciones de los $\epsilon$**.

Los $\epsilon_i$ son paseos aleatorios simples independientes con pasos ±1 cada uno, pero ¡ojo!, los $\epsilon_i$ en el tiempo no son los mismos que las "fronteras"; son las velocidades. Sin embargo, podemos pensar en $\epsilon_i(t)$ como las posiciones de **otras** partículas.

La composición del proceso: los huecos $u_i$ son diferencias de los $\epsilon$ acumulados... 

Definamos $\eta_i = \sum_{j \le i} \epsilon_j$ (suma parcial). Entonces $u_i(t) = u_i(0) + (\epsilon_{i+1} - \epsilon_i)$ acumulado = $u_i(0) + [\eta_{i+1}(t) - \eta_{i+1}(0)] - [\eta_i(t) - \eta_i(0)]$... donde $\eta_i(t) = \eta_i(0) + \sum_{s\le t}\epsilon_i(s)$. Pero $\eta_i$ no son independientes? Los $\epsilon_i$ sí son independientes entre sí (iid en cada instante e independientes entre instantes). Entonces $\eta_i(t) - \eta_i(0) = \sum_{s\le t}\epsilon_i(s) =:\epsilon_i^*(t)$ es un paseo simple, e independiente entre $i$'s.

Entonces el hueco $u_i(t) = \frac12(P_{i+1}(t) - P_i(t))$ con $P_i(t) = P_i(0) + \epsilon_i^*(t)$, donde $\epsilon_i^*$ son paseos simples independientes. Reconfirmado.

**Ahora, la coalescencia de paseos P en 1D: usar la martingala $\sum |P_i - P_j|$**

Para paseos aleatorios independientes $P_1, \ldots, P_k$ en $\mathbb{Z}$ (sin cota), la cantidad $\Phi(t) = \sum_{i<j} |P_i(t) - P_j(t)|$ tiene un drift. Calculemos: para dos paseos independientes con pasos ±1, la diferencia evoluciona como $D \to D + (\pm1 \mp1)$, es decir $D' = D + Z$ con $Z \in \{-2,0,2\}$ prob (1/4,1/2,1/4). El drift de $|D|$: 

Para $D = 0$: $|D'| \in \{0, 2, 2, 0\}$... transiciones: $Z=-2$: $|Z|=2$; $Z=0$: 0; $Z=+2$: 2. Esperanza de $|D'| = 1/4*2 + 1/2*0 + 1/4*2 = 1$. Drift de 0: +1.

Para $D > 0$ (digamos $D \ge 2$): $|D+Z|$: 
- Z=-2: D-2, |.|=D-2 (ya que D≥2).
- Z=0: D.
- Z+2: D+2.
Esperanza: (D-2)/4 + D/2 + (D+2)/4 = D. Drift 0.

Así que $|D|$ es una submartingala: drift 1 en D=0, drift 0 en D>0. ¡Interesante! La cantidad $\sum_{i<j}|P_i - P_j|$ crece solo cuando dos partículas coinciden (brevemente), con drift positivo.

Esto sugiere que podemos construir una martingala corrigiendo por las colisiones. En colisiones (D=0), los pares coinciden y el drift es 1 por cada par coincidente.

Planteemos la martingala $M(t) = \Phi(t) - \sum_{s< t} C(s)$, donde $C(s)$ es el número de pares de partículas coincidentes en el instante $s$ (después del paso...) — busca cuánto drift por colisión.

Este enfoque es más complejo; pero hay una martingala más simple.

**Coalescencia completa en 1D: respuesta vía la martingala $\sum |P_i - P_j|$ y la duplicación**

Para el **coalescente estándar de paseos en 1D** donde los paseos se fusionan al coincidir, el tiempo esperado de coalescencia completa es infinito (porque el último par es un paseo 1D). Pero aquí el sistema está acotado por la suma de gaps. Sin embargo, en el modelo de paseos P en $\mathbb{Z}$ sin cota, la suma de gaps es la diferencia $P_{max} - P_{min}$, que no está fija. Espera, ¿es constante?

En nuestro problema original, la suma de huecos es 30 y constante. En el modelo P, la suma de diferencias consecutivas $2\sum u_i = \sum (P_{i+1} - P_i) = P_{k+1} - P_k + \ldots$ con la convención cíclica: $P_{k+1}$ no se define linealmente en $\mathbb{Z}$; ¡usando el desenrollado circular, $P_{k+1}$ corresponde a $P_1$ más una vuelta! Es decir, en el círculo, la "suma de gaps" es la circunferencia total 30, fija. En el desenrollado, $P_{k+1} := P_1 + 30$ (ya que damos la vuelta completa). Entonces $\sum_{i=1}^k (P_{i+1} - P_i) = P_{k+1} - P_1 = 30$, siempre. Correcto: el círculo total 30 en unidades hueco (u suma 15, pero en términos de d, total 30). En el desenrollado, definimos $P_{k+1} = P_1 + 30$.

Por lo tanto, $P_{i+1} - P_i \ge 0$, con suma 30, y las $P_i$ forman una cadena creciente en $[P_1, P_1+30]$. Es un **sistema acotado**.

Ahora la coalescencia: cuando $P_{i+1} = P_i$ (gap 0), se fusionan, eliminando el paseo $P_{i+1}$ (o $P_i$, pero manteniendo la cadena). Después de eliminar, las diferencias de la cadena se recomponen: el gap entre $P_{i-1}$ y $P_{i+2}$ se vuelve $P_{i+2} - P_{i-1}$, que es la suma de los gaps anteriores $P_{i+1}-P_{i-1} + P_{i+2}-P_{i+1}$ (con $P_{i+1}=P_i$). La suma total sigue 30.

Así que en términos de gaps, es lo mismo.

La clave es que los $P_i$ son paseos aleatorios simples **ordenados** (gracias al acoplamiento, se mantienen ordenados, no se cruzan porque al coincidir se fusionan). Es el proceso de **no cruce: paseos "ordenados" en un intervalo, con fusión al contacto**.

Ahora, en este proceso, la cantidad $\sum_{i=1}^{k} (P_i - \bar P)^2$, o mejor, $\Phi = \sum_{i<j} (P_j - P_i) = \sum_i (2i-k-1) P_i$ (para orden fijo) es una **martingala** o tiene drift controlado.

Las posiciones $P_i$ son paseos aleatorios simples independientes mientras no choquen, y el orden se mantiene. El "centro de masa" $\sum P_i$ tiene drift 0 (martingala). La "inercia" $\sum P_i^2$ tiene drift $k$ por paso (ya que cada $P_i$ suma +1 a su cuadrado esperado).

En la fusión, se elimina un paseo. Necesitamos saber la esperanza de la eliminación. En el instante de fusión, $P_{i+1} = P_i$, y eliminamos $P_{i+1}$ (decimos que $P_{i+1}$ es absorbido por $P_i$). La inercia $\sum P^2$ pierde $P_{i+1}^2$. Como $P_{i+1} = P_i$ en ese instante, ambos tienen el mismo valor; al eliminarlo, no altera el orden ni el centro de gravedad, solo reduce k por 1 y la inercia por $P_i^2$.

¡Problema! El valor de $P_i^2$ en la fusión es desconocido y no acotado (depende de cuánto tiempo ha pasado). Sin embargo, dado que el sistema es acotado módulo la circunferencia, $P_i$ puede desplazarse arbitrariamente lejos en $\mathbb{Z}$ (el círculo puede girar). La "deriva" del círculo (posición absoluta) es una martingala sin importancia para los gaps, pero la inercia absoluta $\sum P_i^2$ no está acotada y complica. Necesitamos trabajar solo con diferencias (gaps), no posiciones absolutas.

Así que volvemos a $Q = \sum d_i^2$ (gaps), que es lo que usamos antes.

**Encontrar la segunda martingala usando la estructura ordenada: los gaps únicamente**

La única información que sobrevive a la rotación es la configuración de gaps. $Q = \sum d_i^2$ tiene drift $2k$. ¿Hay una martingala **global** con drift solo 1 que entregue $\mathbb{E}[T]$? 

Consideremos la fase final por separado y quizás las demás fases se resuelven con una martingala de segundo orden apropiada.

**Cálculo por fases con la distribución estacionaria del "quemado"**

Hay una forma más ingeniosa: el proceso de gaps $(u_i)$ con $\sum u_i = 15$ y transición $u_i \to u_i + (\epsilon_{i+1}-\epsilon_i)/2$ es reversible con respecto a la medida uniforme sobre los $(u_i)$ con suma 15 (composiciones de 15 en k partes). En cada paso, de acuerdo con los $\epsilon$ iid, la transición es una mezcla de subidas y bajadas. La medida uniforme es estacionaria (esto es el proceso de exclusión simétrica sobre el grfo de composiciones, reversible uniforme). 

Cuando $u_i = 0$, se absorbe (fusión). La absorción elimina la coordenada 0 y redefine la suma.

Esta dualidad de reversibilidad sugiere que podemos usar el **potencial de "energía"** y calcular el tiempo esperado de absorción vía la fórmula del "campo medio".

**Método de martingala con la función $\sum u_i^2$ y la condición de parada**

Conocíamos $M_1 = Q - 2\sum k\, dt$. Para T esperado necesitamos otra: la cantidad $A(t) = \sum_i u_i^2$ (con $u_i$ = huecos enteros, $Q = 4A$). Drift de $A$: cada $u_i \to u_i + (\epsilon_{i+1}-\epsilon_i)/2$. 

$A' = \sum u_i'^2 = \sum [u_i^2 + u_i(\epsilon_{i+1}-\epsilon_i) + (\epsilon_{i+1}-\epsilon_i)^2/4]$.

Esperanza: $\sum u_i^2 + \sum E[(\epsilon_{i+1}-\epsilon_i)^2]/4 = A + \sum_{i} \frac{2}{4} = A + k/2$.

(Nota: $E[(\epsilon_{i+1}-\epsilon_i)^2] = E[\epsilon_{i+1}^2] + E[\epsilon_i^2] - 2E[\epsilon_{i+1}\epsilon_i] = 1+1-0 = 2$.)

Así que drift de $A$ es $k/2$ por paso. Coherente con $Q = 4A$: drift de Q es $4\cdot k/2 = 2k$.

Entonces $A(t) - \frac12 \sum_{s\le t} k(s)$ es martingala.

Inicial $A_0 = \sum u_i^2 = 15 \cdot 1^2 = 15$ (ya que $u_i = 1$ al inicio). Final: un hueco $u = 15$, $A_T = 225$.

Parada opcional: $\mathbb{E}[A_T] - \frac12 \mathbb{E}[\sum_{s\le T} k(s)] = A_0$, 

$\Rightarrow 225 - \frac12 \mathbb{E}\sum k(s) = 15 \Rightarrow \mathbb{E}\sum k(s) = 420$. Igual que antes.

Necesitamos $\mathbb{E}T$. Otra cantidad con drift $\frac12$ por... idealmente drift $c$ (constante) para despejar.

**Otra función aditiva: $\sum_i (u_i - \frac{15}{k})^2$, el "varianzo"**

Como $\sum u_i = 15$ fijo, defina $V_k = \sum (u_i - \bar u)^2$ con $\bar u = 15/k$. 

$V_k = A - 2\bar u \sum u_i + k \bar u^2 = A - 2\bar u \cdot 15 + k\bar u^2 = A - 30 \cdot (15/k) + k (225/k^2) = A - 450/k + 225/k = A - 225/k$.

Drift de $V_k$ entre pasos = drift de $A = k/2$. Entonces $V_k - \frac{k}{2} t$ es martingala local (entre pasos). Pero $\bar u$ depende de k que cambia en fusiones; en fusiones, $V$ salta.

**Martingala del "segundo momento" con corrección de fusiones**

Notemos que $\sum (u_i - \bar u)^2$ en el estado final (k=1, u=15) es 0. En el estado inicial (k=15, u_i=1) es 0. 

Interesante: inicial y final tienen varianza 0.

La varianza $V$ tiene drift $k/2$ por paso. En una fusión (cuando un $u_i = 0$), se elimina la coordenada 0, y las demás se renormalizan: la nueva $\bar u = 15/(k-1)$.

Calculemos el cambio de $V$ en una fusión de k → k-1, cuando $u_i = 0$:

Antes: $V_{\text{antes}} = \sum_{j} (u_j - 15/k)^2$ (con el $u_i = 0$ incluido).
Después: quito la coordenada $u_i = 0$, queda $\sum_{j \ne i}(u_j - 15/(k-1))^2$.

Diferencia incluye el término $(0 - 15/k)^2$ removido y el corrimiento del centro.

Esto es complicado pero quizás sumando sobre todas las fusiones se simplifique con la martingala.

**Estrategia alternativa: ciclo completo vía martingala en $A$ con saltos de fusión corregidos**

Definamos $V(t) = \sum (u_i(t) - \bar u_{k(t)})^2$ donde $\bar u_k = 15/k$. 

Como $V(T) = 0$ y $V(0) = 0$, si logramos que $V(t) - (\text{drift acumulado})$ sea una martingala exacta incluyendo saltos, la diferencia $V(T)-V(0)=0$ implicaría $\mathbb{E}[\text{drift acumulado}] = 0$, que no serviría (drift sería 0).

Hmm.

**Usar la dualidad con la fórmula del "arma de Bessel" para SSEP**

El proceso de gaps con transiciones $u_i \to u_i + (\epsilon_{i+1}-\epsilon_i)/2$ con $\epsilon$ iid es reversible respecto a la uniforme en composiciones. El tiempo esperado hasta que una coordenada llega a 0, desde la configuración inicial, es un problema de SSEP en anillo.

Existe una fórmula explícita para el tiempo esperado de absorción en el **proceso de exclusión simétrica con absorbedor (coalescencia de huecos)**. Dado que es SSEP con un "hueco" que desaparece, hay una dualidad con la coalescencia de partículas etiquetadas.

**Dualidad SSEP ↔ coalescencia aleatoria (intercambios)**

SSEP (Symmetric Simple Exclusion Process) en anillo es dual al proceso de **intercambio aleatorio** donde las partículas intercambian posiciones. Nuestros gaps representan el número de "huecos" (posiciones vacías) entre "partículas". 

Hagamos la biyección con una configuración de SSEP: consideremos un anillo con 45 sitios, 15 partículas (serpientes delimitadas) y 30 huecos (espacios). La evolución: cada "sello" corresponde a mover... 

En SSEP estándar, las partículas saltan a huecos adyacentes con cierta tasa. Aquí, el movimiento está dado por: en cada paso, cada serpiente (partícula de tamaño posiblemente ~1) intenta moverse ±1, lo cual intercambia con un hueco adyacente.

Nuestras serpientes son como "partículas" y los gaps son los espacios. La evolución de gaps $u_i \to u_i + (\epsilon_{i+1}-\epsilon_i)/2$ con $\epsilon$ = ±1 iid. Si miramos las **fronteras** (lugares donde el estado cambia), la configuración del anillo en términos de "hueco-vacío" es una palabra binaria de longitud 45 con 15 "X" (serpiente) y 30 "·" (vacío). El movimiento: cada paso, cada serpiente (bloque X de longitud L) se desplaza ±1... Esto desplaza tanto su borde izquierdo como derecho.

En SSEP, cada gap u_i evoluciona por el movimiento de las fronteras de la serpiente (que son como partículas excitadas). En particular, la evolución de los gaps $u_i \to u_i + (\epsilon_{i+1}-\epsilon_i)/2$ es **dual** a una CTMC de "intercambios" donde en cada paso se mueve una "mancha" entre huecos.

**Ro: el proceso de gaps es SSEP "perezoso" en el grafo completo de k sitios, con un absorbedor en 0.**

SSEP reversible uniforme: el tiempo esperado de absorción desde la composición (1,1,...,1) con suma 15.

Hay una fórmula por la "medida armónica": el tiempo esperado hasta tocar el hiperplano $u_i=0$ comenzando en composición uniforme. 

**Vamos a resolverlo con la martingala armónica exacta $h(u) = \sum c_k$ via función propia seno**

Para el proceso SSEP con absorción cuando una coordenada se anula, el tiempo esperado satisface $h(\mathbf{u}) = 1 + \sum P(\mathbf{u},\mathbf{v}) h(\mathbf{v})$ (interior), con $h=0$ si algún $u_i=0$. 

Conjetura: $h(\mathbf{u}) = C \cdot G(\mathbf{u})$ para una función simétrica, y por la estructura lineal, la solución es una combinación de funciones propias del laplaciano del símplex.

Como el drift de $A = \sum u_i^2$ es $k/2$, una martingala natural es $A - \frac12 k t$. Para que el tiempo esperado aparezca como martingala, necesitamos una función $f(\mathbf{u})$ con drift 1 (constante) — es decir $f$ resuelve el "problema de Dirichlet inverso" parcial. 

Cualquier $f(\mathbf{u})$ con laplaciano (segundo momento de incrementos) = -1 en todo el interior daría $\mathbb{E}[T] = f(\mathbf{u}_0) - \mathbb{E}[f(\mathbf{u}_T)]$ con $f(\mathbf{u}_T) = 0$ en el borde absorbente... si además $f=0$ en el borde absorbente. 

El laplaciano (drift) de $f$ entre pasos es $\mathcal{L} f = \frac14 \sum_i [f(\mathbf{u}+\mathbf{e}_i - \mathbf{e}_{i-1}) - f(\mathbf{u}) + f(\mathbf{u}-\mathbf{e}_i + \mathbf{e}_{i-1}) - f(\mathbf{u})]$. Queremos $f$ con $\mathcal{L} f = -1$, f=0 en el borde.

Para el paseo simple en 1D sobre [0,15], $h(u) = 2u(15-u)$ resuelve eso (con la constante 4 por el perezoso). En dimensión k con el símplex, la función $\sum_i u_i^2$ tiene laplaciano $2k$ (¿chequeado? el drift de $A$ es $k/2$; y el "laplaciano" aquí es en pasos: $\mathcal{L}A = k/2$;). Para $f = c \sum u_i^2$, $\mathcal{L} f = c \cdot k/2$. 

Necesitamos $\mathcal{L} f = -1$, pero $\mathcal{L}$ de $\sum u_i^2$ = k/2, que depende de k. En la fase k fija, $h_k(\mathbf{u}) = \frac{2}{k}\sum u_i^2$... $\mathcal{L}(\frac2k \sum u_i^2) = \frac2k \cdot \frac{k}{2} = 1$. Con signo: definamos $f_k(\mathbf{u}) = -\frac{2}{k}\sum u_i^2 + \text{corrección de borde}$.

Pero ojo, la fase k está en el símplex $u_i \ge 0$, $\sum u_i = 15$. Las ecuaciones de borde (cuando algún $u_i = 0$, se absorbe) requieren h=0. La solución armónica con $h=0$ en el borde y $\mathcal{L} h = -1$ en el interior para el conjunto de composiciones (suma fija 15) con $u_i \ge 1$ en el interior (positivo).

En 1D (k=2): h(u) = 2u(15-u), y $\sum u_i^2 = u^2 + (15-u)^2 = 2u^2 - 30u + 225$. No es múltiplo de h. Añadimos términos lineales (drift 0) y constantes para ajustar borde: h = c + a (u_1+u_2) + b (u_1^2+u_2^2)... con $\sum u = 15$ fijo, lineal = constante, y $u_1^2+u_2^2 = 2u_1^2 - 30u_1 + 225$, así que es cuadrático en u_1, y podemos ajustar para que se anule en u_1=0 y u_1=15. En efecto, h = 2u(15-u) es múltiplo de $(u^2+(15-u)^2) - 225$... calculemos: $2u(15-u) = 30u - 2u^2$. Y $u^2+(15-u)^2 = 2u^2 -30u + 225$. Entonces $-(u^2+(15-u)^2) + 225 = -2u^2+30u = 2u(15-u)$. ¡Sí! Así que h = $225 - \sum u_i^2$ (para k=2). Y $\mathcal{L}[\sum u_i^2] = k/2 = 1$ (k=2), así que $\mathcal{L}h = -1$. Correcto.

Generalizando a k dimensiones: la función homogénea que se anula cuando algún $u_i = 0$ y tiene laplaciano lineal es

$$h_k(\mathbf{u}) = C_k\left(\sum_i u_i\right)^2 - \sum_i u_i^2 = C_k S^2 - A,$$

donde $S = \sum u_i = 15$ (fija).

$\mathcal{L}$ de $S^2$ es 0 (S martingala). $\mathcal{L}$ de $A$ es $k/2$. Así que $\mathcal{L} h_k = -k/2 \cdot$... 

Queremos $\mathcal{L} h_k = -1$. Con $h_k = \alpha (S^2) - \beta A$: $\mathcal{L} h = -\beta \cdot (k/2)$. Sea $\beta = 2/k$, $\alpha$ para ajuste de borde.

Además, en el borde absorbente (algún $u_i = 0$), queremos $h_k = 0$. El problema: cuando un $u_i=0$, se absorbe y pasamos a la fase k-1. Para el tiempo de la fase k (hasta la primera fusión), la condición de parada es $h=0$ cuando algún $u_i = 0$.

Necesitamos $\alpha, \beta$ tal que $h_k = \alpha S^2 - \beta A$ se anule cuando $u_i=0$ para algún i, CON S = 15 fijos. Entonces un término $\alpha S^2$ constante, y $A$ en el borde (con un $u_i=0$) es un valor... no sabemos cuánto vale A en el borde; varía según la configuración de borde.

Por lo tanto, una función $h_k = \alpha S^2 - \beta A$ no puede anularse en todo el borde, salvo ajuste. En k=2 sí, porque el borde tiene solo 2 puntos (u=0, u=15) con A y S constantes, y ajustamos para que ambos den 0 (porque S^2=225 y A toma el mismo valor 225 en ambos bordes, ya que en k=2 $A = u^2+(15-u)^2$, en u=0 da 225, en u=15 da 225). Para k>2, el borde es más rico.

**Función armónica correcta para el símplex: $h(\mathbf{u}) = \sum_i u_i(15-u_i)$ no; veamos el laplaciano.**

En general, la solución del problema de Dirichlet en el símplex con $\mathcal{L}h = -1$ es $h(\mathbf{u}) = \sum_{i<j} u_i u_j$ (a veces), o una función $\sum u_i(S - u_i)$.

$S = 15$, $S^2 = \sum_i u_i^2 + 2\sum_{i<j}u_i u_j$. Entonces $\sum_{i<j} u_i u_j = \frac12(S^2 - \sum_i u_i^2) = \frac12 S^2 - \frac12 A$.

$\mathcal{L}[\sum_{i<j}u_i u_j] = -\frac12 \mathcal{L} A = -k/4$.

Así que $\mathcal{L}[\sum_{i<j} u_i u_j] = -k/4$. Dividiendo: $h = \frac{4}{k}\sum_{i<j} u_i u_j$ tiene laplaciano $\frac{4}{k}\cdot(-k/4) = -1$. 

Y en el borde ($u_i = 0$): $\sum_{i<j}u_i u_j$ no es 0; es $\sum_{\substack{i<j \\ i,j \ne \text{ese}}} u_i u_j = \frac12((15)^2 - \sum_{j \ne \cdot} u_j^2)$, que es positivo en general, no 0. Entonces no cumple h=0 en borde.

El problema de Dirichlet para el tiempo de absorción es más complicado: el valor en el borde es 0, pero en el interior hay una solución única. Para k=2, $h = \sum_{i<j} u_i u_j = u_1 u_2 = u(15-u)$, que se anula en u=0 y u=15. Bien. Y coincide con 2u(15-u) salvo constante... en k=2, $u_1 u_2 = u(15-u)$, y aquí $\mathcal{L}u_1u_2 = -1/2$ (k=2 => -k/4 = -1/2). Entonces $2u_1u_2$ tiene $\mathcal{L} = -1$ y h=0 en borde. Pero espera, en k=2 el laplaciano de A = 1 = k/2 = 1, y $u_1u_2 = (S^2 - A)/2$, $\mathcal{L}u_1u_2 = -1/2$. Correcto.

Para k=2, h = 2u(15-u) es la solución. Y $4/k \sum_{i<j} = 2u_1u_2 = 2u(15-u)$. Correcto.

Para k>2, la solución de Dirichlet no es solo $\sum_{i<j}u_i u_j$ porque no se anula en el borde. Requiere una serie de Bessel/coeficiente.

**Uf, este problema es más difícil que lo esperado.**

Tal vez haya una interpretación más simple del problema de serpientes que dé una respuesta cerrada sencilla.

**Reexaminar movimientos de serpientes: ¿las serpientes chocan cuando SOLO se tocan, y la serpiente fusionada "mueve como una", lo cual en la práctica conecta las piezas?**

El problema dice: "Cuando dos serpientes se tocan, se fusionan... y la serpiente fusionada se mueve como una serpiente." La clave puede ser que la longitud de la serpiente no importa para los gaps (como ya vimos). El proceso de gaps es exactamente SSEP con absorción.

Quizás la respuesta sea una simple martingala que no notamos.

**La cantidad crucial: el número medio de arcos vacíos por hueco**

En el estado inicial, cada hueco tiene 2 vacíos. En general, hueco promedio = 30/k.

Planteemos $Z(t) = \sum_i d_i \cdot (\text{posición})$. 

**Una martingala alterna: $\sum_i d_i$ (constante), pero considera $\sum_i d_i^2 - 2 \sum_{s} k_s = M$. La martingala M en el instante final da 420 = $\mathbb{E}\sum k_s$. Para despejar $\mathbb{E}T$, necesitamos $-2\sum_t 1$ con el mismo 900.**

Consideremos la cantidad $W(t) = k(t)\cdot$ ... definamos $B(t) = \sum_i d_i^2 + 2\sum_{s \le t}(k(s) - c)$. Elegimos c... M_1 = Q - 2∑k es martingala con valores finales conocidos. Si definimos M_2 = Q - 2∑(k) - 2c∑(1)? Buscamos $c$ tal que $M_2 = Q - 2\sum(15 - k)$... porque $15 - k(t) =$ número de fusiones hasta t. 

Nota: $k(t) = 15 - N_{\text{fusiones}}(t)$, donde $N_{\text{fusiones}}$ es el número de fusiones hasta t. Entonces $Q(t) - 2\sum_{s\le t} k(s) = Q(t) - 2\sum_{s\le t}(15 - N_{\text{fus}}(s))## Modelado de los huecos

Numeremos las serpientes en orden cíclico. Definimos

\[
d_i=\text{número de arcos vacíos entre la serpiente }i\text{ y la }i+1.
\]

Inicialmente hay 15 huecos, cada uno con \(d_i=2\) arcos vacíos. La suma total de arcos vacíos es

\[
\sum_i d_i=45-15=30.
\]

Cada segundo cada serpiente se mueve \(\pm1\). El hueco \(d_i\) está delimitado por la serpiente \(i\) y la \(i+1\). Si \(\eta_i=\pm1\) es el movimiento de la serpiente \(i\), entonces el hueco cambia según

\[
d_i \to d_i+\eta_{i+1}-\eta_i.
\]

Definimos \(m_i=d_i/2\). Como \(d_i\) siempre es par, \(m_i\) es entero y cambia como

\[
m_i \to m_i+\frac{\eta_{i+1}-\eta_i}{2}.
\]

Es decir, \(m_i\) cambia en \(+1\) con probabilidad \(1/4\), en \(-1\) con probabilidad \(1/4\), y en \(0\) con probabilidad \(1/2\). Además se conserva

\[
\sum_i m_i=\frac{30}{2}=15.
\]

La fusión ocurre cuando algún \(m_i\) llega a \(0\), y entonces ese sitio se elimina.

## La martingala clave

Consideremos la cantidad

\[
\Psi(t)=\sum_i m_i(t)^3.
\]

Para un único sitio con valor \(m\), el cambio esperado en \(m^3\) es

\[
\frac14(m+1)^3+\frac12 m^3+\frac14(m-1)^3
= m^3+\frac32 m.
\]

Por tanto, condicionando al estado actual,

\[
\mathbb{E}[\Psi(t+1)-\Psi(t)]=\frac32\sum_i m_i=\frac32\cdot 15=\frac{45}{2}.
\]

Este incremento es constante, no depende de cuántas serpientes haya. Además, cuando se produce una fusión el sitio que se elimina tiene \(m=0\), así que \(\Psi\) no sufre saltos.

En consecuencia,

\[
\Psi(t)-\frac{45}{2}t
\]

es una martingala.

## Tiempo esperado

Inicialmente, cada \(m_i=1\), así que

\[
\Psi(0)=15\cdot 1^3=15.
\]

Al final queda una sola serpiente: todo el espacio vacío está en un único hueco de tamaño \(m=15\), luego

\[
\Psi(T)=15^3=3375.
\]

Por el teorema de parada opcional,

\[
\mathbb{E}[\Psi(T)]-\frac{45}{2}\mathbb{E}[T]=\Psi(0),
\]

\[
3375-\frac{45}{2}\mathbb{E}[T]=15.
\]

Despejando,

\[
\mathbb{E}[T]=(3375-15)\cdot\frac{2}{45}=\frac{6720}{45}=\frac{448}{3}.
\]

\[
\boxed{\frac{448}{3}}
\]