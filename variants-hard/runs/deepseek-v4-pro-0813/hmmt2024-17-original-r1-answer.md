Voy a razonar sobre el problema.

Tenemos una franja de altura 2 que se extiende infinitamente hacia la derecha. Las celdas forman dos filas. Philip empieza en una esquina, digamos en la celda de la fila superior de la columna 0 (la celda marcada con estrella).

Entre celdas adyacentes hay puertas, cada una abierta con probabilidad \(1/2\), independientemente.

Queremos el número esperado de celdas alcanzables desde la celda inicial.

Sea la celda inicial en la columna 0, fila superior. Las columnas son \(0,1,2,\dots\).

Estructura de puertas:
- Puertas horizontales: en cada fila, entre la columna \(n\) y \(n+1\).
- Puertas verticales: entre las dos filas, en cada columna \(n\).

Hay una puerta vertical en la columna 0 que conecta la celda superior con la inferior de esa columna.

Philip empieza en la esquina (columna 0, fila superior). Puede moverse por puertas abiertas.

Queremos el número esperado de celdas en el componente conexo que contiene la celda inicial en este grafo aleatorio (la franja infinita con puertas Bernoulli).

Este es un problema clásico de percolación en una franja (strip) de anchura 2. El número esperado de celdas en el clúster de un vértice en una franja infinita.

Vamos a modelar esto de forma exacta.

Etiquetemos las celdas por columna \(n \ge 0\) y fila \(r \in \{0,1\}\). Digamos fila 0 = superior, fila 1 = inferior. La celda inicial es \((0,0)\).

Definamos las puertas:
- \(H_{n}^{(r)}\): puerta horizontal entre \((n,r)\) y \((n+1,r)\), abierta con prob \(1/2\), para \(n\ge 0\), \(r\in\{0,1\}\).
- \(V_n\): puerta vertical entre \((n,0)\) y \((n,1)\), abierta con prob \(1/2\), para \(n\ge 0\).

Queremos \(E[|C(0,0)|]\).

Como la franja es de anchura 2, podemos analizar el clúster columna por columna. La franja es formalmente el grafo de escalera (ladder) infinito.

En cada columna \(n\), hay un subgrafo con dos vértices y una posible arista vertical \(V_n\). El clúster dentro de una columna depende de \(V_n\). Entre columnas hay aristas horizontales \(H_n^{(0)}\) y \(H_n^{(1)}\).

Podemos pensar en el estado del clúster en la columna \(n\): qué vértices de la columna \(n\) están ocupados por el clúster (conectados a la celda inicial). Como solo hay 2 filas, los posibles estados de ocupación en una columna son: ninguno, solo superior, solo inferior, o ambos.

El proceso se extiende hacia la derecha a partir de la columna 0. Inicialmente en la columna 0, el vértice superior está ocupado. Si \(V_0\) está abierta, entonces ambos vértices de la columna 0 están ocupados; si no, solo el superior.

Luego, de la columna \(n\) a la \(n+1\), la ocupación se propaga a través de las puertas horizontales \(H_n^{(0)}, H_n^{(1)}\), y luego dentro de la columna \(n+1\) a través de \(V_{n+1}\).

Como las puertas son i.i.d., este es un proceso de Markov sobre los estados de columna.

Estados:
0: ninguno ocupado (absorbente) — el clúster termina.
1: solo superior ocupado.
2: solo inferior ocupado.
3: ambos ocupados.

Empezamos en la columna 0 con el estado dependiente de \(V_0\). Pero es más limpio: en la columna 0, inicialmente ocupado el superior; después de considerar \(V_0\), el estado es 3 con prob \(1/2\) y 1 con prob \(1/2\).

Para contar el número esperado de celdas, sumamos sobre columnas el número esperado de vértices ocupados en la columna \(n\).

Calculemos la matriz de transición para pasar de la columna \(n\) a la \(n+1\) (estado de ocupación en \(n+1\), dados qué vértices de la columna \(n\) estaban ocupados).

La transición depende de las puertas horizontales \(H_n^{(0)}, H_n^{(1)}\) y de la vertical \(V_{n+1}\).

Dado el estado en la columna \(n\):

**Estado 1: solo superior ocupado.**

Entonces la celda superior de la columna \(n+1\) recibe conexión si \(H_n^{(0)}=1\) (abierta). La celda inferior de la columna \(n+1\) no recibe conexión directa porque la inferior de la columna \(n\) no está ocupada (asumiendo que \(H_n^{(1)}\) no importa; incluso si estuviera abierta no hay fuente).

Sea \(A = H_n^{(0)}\), \(B = V_{n+1}\).

- Si \(A=0\): la superior de \(n+1\) no está conectada. El estado en \(n+1\) es 0 (absorbente), sin importar \(B\).
- Si \(A=1\): la superior de \(n+1\) está conectada. Si \(B=1\), entonces la inferior también queda conectada (estado 3). Si \(B=0\), solo superior (estado 1).

Entonces desde estado 1:
- a estado 0 con prob \(P(A=0) = 1/2\).
- a estado 3 con prob \(P(A=1, B=1) = 1/2 \cdot 1/2 = 1/4\).
- a estado 1 con prob \(P(A=1, B=0) = 1/2 \cdot 1/2 = 1/4\).

**Estado 2: solo inferior ocupado.** Simétrico:
- a estado 0 con prob \(1/2\).
- a estado 3 con prob \(1/4\).
- a estado 2 con prob \(1/4\).

**Estado 3: ambos ocupados.**

Ahora ambas celdas de la columna \(n\) están ocupadas. La superior de \(n+1\) queda conectada si \(H_n^{(0)}=1\); la inferior de \(n+1\) queda conectada si \(H_n^{(1)}=1\). Sea \(A=H_n^{(0)}\), \(C=H_n^{(1)}\), \(B=V_{n+1}\).

En la columna \(n+1\), antes de \(B\), los ocupados son: superior si \(A=1\), inferior si \(C=1\).

Luego \(B=V_{n+1}\) puede conectar ambos si \(B=1\) y al menos uno de los dos está ocupado. Si \(B=1\), ambos quedan ocupados (porque \(B\) conecta superior e inferior; si al menos uno está conectado a la fuente, el otro también a través de \(B\)). Si \(B=0\), cada uno permanece según \(A, C\).

Casos (\(A,C,B\) i.i.d. Bernoulli(1/2)):

- \(A=1, C=1\): ambos ocupados antes de \(B\), con \(B\) da estado 3 siempre. Prob \(1/4\).
- \(A=1, C=0\): superior ocupado, inferior no. Si \(B=1\), estado 3; si \(B=0\), estado 1. Prob del caso: \(1/4\). Sub: \(B=1\) prob \(1/2\) → estado 3; \(B=0\) → estado 1.
- \(A=0, C=1\): inferior ocupado, superior no. Si \(B=1\) → estado 3; si \(B=0\) → estado 2.
- \(A=0, C=0\): nadie ocupado → estado 0, sin importar \(B\). Prob \(1/4\).

Sumando:
- Estado 3: \(P(A=C=1)=1/4\) más \(P(A=1,C=0,B=1)=1/4\cdot1/2=1/8\) más \(P(A=0,C=1,B=1)=1/8\). Total \(1/4+1/8+1/8 = 1/2\).
- Estado 1: \(P(A=1,C=0,B=0)=1/8\).
- Estado 2: \(P(A=0,C=1,B=0)=1/8\).
- Estado 0: \(P(A=0,C=0)=1/4\).

Desde estado 3:
- a 0: \(1/4\)
- a 1: \(1/8\)
- a 2: \(1/8\)
- a 3: \(1/2\).

Todo coherente: las probabilidades suman 1.

Ahora queremos el número esperado de celdas totales. Sea \(S\) el número total de celdas alcanzables. Podemos descomponer por columnas:

Para la columna 0: número esperado de celdas ocupadas en la columna 0 = \(1 + P(V_0=1) = 1 + 1/2 = 3/2\). Es decir, la celda inicial más la celda inferior si la vertical está abierta.

Para columnas \(n\ge 1\), necesitamos \(E[\text{número de celdas ocupadas en columna } n]\).

Definamos para cada columna el indicador de ocupación. Podemos usar la distribución del estado.

Alternativamente, formulemos con Markov y resolvamos las expectativas.

Sea \(p_n^{(s)}\) la probabilidad de que el estado en la columna \(n\) sea \(s\), donde el estado en la columna \(n\) se define después de procesar las puertas horizontales desde \(n-1\) a \(n\) y la vertical \(V_n\). O sea, la ocupación de la columna \(n\) considerando toda la conexión.

El estado inicial en la columna 0: antes de \(V_0\), el superior está ocupado. Después de \(V_0\): estado 3 con prob \(1/2\), estado 1 con prob \(1/2\). Definimos ese como distribución inicial en la columna 0.

Pero cuidado: la definición de estado en columna 0 con \(V_0\) es consistente.

Entonces para \(n\ge 0\):

\( \pi_n = \pi_0 P^n \), donde \(P\) es la matriz de transición de 4 estados (con estado 0 absorbente), y

\( \pi_0 = (0, 1/2, 0, 1/2) \) en el orden (estado 0, estado 1, estado 2, estado 3).

El número de celdas ocupadas en la columna \(n\): si estado \(s\), el número de celdas ocupadas es \(n(s)\), con \(n(0)=0, n(1)=1, n(2)=1, n(3)=2\).

Entonces el número esperado total de celdas es:

\( E[S] = \sum_{n=0}^{\infty} E[\text{celdas en columna } n] = \sum_{n=0}^\infty \pi_n \cdot \mathbf{n} \),

donde \(\mathbf{n} = (0,1,1,2)^T\).

Esto es un sistema lineal. Podemos resolverlo de forma cerrada.

Alternativamente, planteemos ecuaciones de expectativas condicionadas por el estado inicial.

Sea \(E_s\) el número esperado total de celdas alcanzables (incluyendo las de la columna actual y hacia la derecha) dado que el estado en la columna actual es \(s\) (habiendo contado ya la columna actual). Mejor: definamos \(F_s\) = número esperado de celdas alcanzables en la columna actual y todas las columnas siguientes, dado que el estado actual (al inicio de procesar esta columna) es \(s\), sin incluir celdas ya contadas.

Para el estado absorbente \(s=0\): \(F_0 = 0\).

Para el estado 1 (solo superior ocupado en esta columna): la columna actual aporta 1 celda (la superior). Luego la transición a la siguiente columna con las probabilidades dadas. Entonces:

\( F_1 = 1 + \frac12 F_0 + \frac14 F_1 + \frac14 F_3 = 1 + \frac14 F_1 + \frac14 F_3 \).

Para el estado 2: simétrico, \( F_2 = 1 + \frac14 F_2 + \frac14 F_3 \). Por simetría \(F_1 = F_2\).

Para el estado 3 (ambos ocupados): la columna actual aporta 2 celdas. Luego:

\( F_3 = 2 + \frac14 F_0 + \frac18 F_1 + \frac18 F_2 + \frac12 F_3 = 2 + \frac18 F_1 + \frac18 F_2 + \frac12 F_3 \).

Como \(F_1 = F_2 =: G\):

- \( G = 1 + \frac14 G + \frac14 F_3 \)  → \( G = 1 + \frac14 G + \frac14 F_3 \). Multiplicando: \( G - \frac14 G = 1 + \frac14 F_3 \) → \( \frac34 G = 1 + \frac14 F_3 \) → \( G = \frac43 + \frac13 F_3 \).

- \( F_3 = 2 + \frac18 G + \frac18 G + \frac12 F_3 = 2 + \frac14 G + \frac12 F_3 \). Entonces \( F_3 - \frac12 F_3 = 2 + \frac14 G \) → \( \frac12 F_3 = 2 + \frac14 G \) → \( F_3 = 4 + \frac12 G \).

Sustituyendo:

\( G = \frac43 + \frac13(4 + \frac12 G) = \frac43 + \frac43 + \frac16 G = \frac83 + \frac16 G \).

\( G - \frac16 G = \frac83 \) → \( \frac56 G = \frac83 \) → \( G = \frac83 \cdot \frac65 = \frac{48}{15} = \frac{16}{5} = 3.2 \).

Entonces \( F_3 = 4 + \frac12 G = 4 + \frac{16}{10} = 4 + 1.6 = 5.6 = \frac{28}{5} \).

Entonces \( G = 16/5\), \(F_3 = 28/5\).

Ahora, el estado inicial: empezamos en la celda superior de la columna 0. Antes de procesar la columna 0, el estado es 1 (solo superior ocupado), y estamos a punto de contar la columna 0. Pero ojo: nuestra definición de \(F_1\) cuenta la columna actual (que tiene solo la celda superior ocupada, 1 celda) y luego aplica la transición a la siguiente columna. La transición desde estado 1 ya incluye las puertas horizontales \(H_0\) y la vertical \(V_1\).

Sin embargo, en la columna 0 hay además la puerta vertical \(V_0\) que conecta la superior con la inferior de la columna 0. Si \(V_0\) está abierta, la celda inferior de la columna 0 también es alcanzable.

Entonces, ¿cómo incorporamos \(V_0\)?

Nuestra definición de estados en la columna \(n\) consideraba la ocupación después de la vertical \(V_n\). En la columna 0, el estado «real» después de \(V_0\) es 1 con prob \(1/2\) y 3 con prob \(1/2\), como dijimos.

La celda inicial ya está contada. Entonces el número esperado total es:

\( E[S] = 1 + E[\text{celdas adicionales}] \).

Donde las celdas adicionales incluyen: la celda inferior de la columna 0 si \(V_0=1\), y todas las celdas de columnas \(\ge 1\).

Alternativamente, usemos directamente: el estado en la columna 0 después de \(V_0\) es 1 (prob \(1/2\)) o 3 (prob \(1/2\)). A partir de ahí, el proceso hacia la derecha usa la matriz \(P\).

Contemos el total incluyendo la columna 0. Si el estado en la columna 0 es 1, la columna 0 aporta 1 celda; si es 3, aporta 2 celdas. Luego hacia la derecha, desde la columna 0 a la 1 con \(P\), etc.

Podemos reutilizar \(F_s\): \(F_s\) cuenta la columna actual más todas las siguientes, dado el estado \(s\) al inicio de la columna *antes de la vertical de esa columna*. Pero cuidado con la definición: en el cálculo de \(F_1\), asumimos que en la columna actual solo la superior está ocupada, y la transición a la siguiente columna considera \(H_n\) y \(V_{n+1}\). En la columna actual, ¿consideramos \(V_n\)? En mi definición, \(F_s\) es el número de celdas en la columna actual y siguientes dado que el estado al *comienzo* de la columna es \(s\), donde el estado ya refleja la ocupación de la columna actual, y luego para pasar a la siguiente columna usamos \(H_n\) y \(V_{n+1}\). En este esquema, la vertical \(V_n\) de la columna actual debe tratarse aparte si el estado no la incluye.

Mejor reconciliemos con la definición de estados: definí los estados de columna como la ocupación *después* de procesar \(V_n\). Entonces el estado de la columna \(n\) es la ocupación de las celdas de la columna \(n\) considerando \(V_n\) y las conexiones previas. En la columna 0, el estado inicial es 1 o 3 dependiendo de \(V_0\) (después de procesar \(V_0\)). Una vez definido el estado en la columna \(n\), el número de celdas ocupadas en esa columna es 1 si el estado es 1 o 2, y 2 si el estado es 3.

La transición \(P\) del estado \(s\) en columna \(n\) al estado \(s'\) en columna \(n+1\) usa \(H_n^{(0)}, H_n^{(1)}, V_{n+1}\), como calculamos.

Entonces, dado el estado \(s\) en la columna \(n\), \(F_s\) debe ser el número esperado de celdas en la columna \(n\) y todas las siguientes. Eso es exactamente lo que calculé:

- \(F_0 = 0\) (ninguna celda ocupada, clúster terminado).
- \(F_1\): estado 1 en columna actual → 1 celda en esta columna + transición. Correcto.
- \(F_3\): estado 3 → 2 celdas + transición. Correcto.

Y la transición desde estado 1 incluye \(H_n^{(0)}\) y \(V_{n+1}\). No incluye \(V_n\) porque el estado ya es posterior a \(V_n\). Correcto.

Entonces el total esperado dado que el estado inicial en la columna 0 (después de \(V_0\)) es 1 o 3:

\( E[S] = \frac12 F_1 + \frac12 F_3 = \frac12 \cdot \frac{16}{5} + \frac12 \cdot \frac{28}{5} = \frac{16}{10} + \frac{28}{10} = \frac{44}{10} = \frac{22}{5} = 4.4 \).

Espera, verifiquemos que \(F_s\) está definido para incluir la columna actual incluso si la transición solo ocurre después. Sí.

Pero un matiz: \(F_1\) cuenta 1 celda de la columna actual (la superior) y luego la transición. La transición desde estado 1 usa las puertas horizontales hacia la columna siguiente. Correcto, porque en la columna actual solo la superior está ocupada.

Sin embargo, en la columna 0, cuando el estado es 1 después de \(V_0\), significa que \(V_0=0\), y solo la celda superior (inicial) está ocupada. Entonces la columna 0 aporta 1 celda. Correcto.

Cuando el estado es 3 después de \(V_0\), \(V_0=1\) y ambas celdas de la columna 0 están ocupadas; la columna 0 aporta 2 celdas. Correcto.

Entonces \(E[S] = \frac12 F_1 + \frac12 F_3 = 22/5 = 4.4\).

Pero déjame verificar con otro método directo, usando la suma sobre columnas y la matriz \(P\), para estar seguro.

Distribución inicial en columna 0 (después de \(V_0\)): \(\pi_0 = (0, 1/2, 0, 1/2)\).

Queremos \(E[S] = \sum_{n=0}^\infty \pi_n \cdot \mathbf{n}\), con \(\mathbf{n}=(0,1,1,2)^T\), \(\pi_n = \pi_0 P^n\).

Alternativamente, resolvamos el sistema de expectativas totales por columna. Podemos definir \(T_s\) = número esperado de celdas en columnas \(\ge 0\) dado el estado en la columna 0 es \(s\). Eso es lo mismo que \(F_s\). Ya lo resolvimos.

Déjame comprobar la validez de la transición desde el estado 3 con un cálculo más cuidadoso, porque quizá hay dependencia de \(V_{n+1}\) con las puertas horizontales.

Desde el estado 3 en la columna \(n\), las celdas ocupadas son ambas. Consideremos la columna \(n+1\):

- La celda superior de \(n+1\) está conectada a la fuente si \(H_n^{(0)}=1\). La celda inferior de \(n+1\) está conectada si \(H_n^{(1)}=1\). Luego, \(V_{n+1}\) conecta superior e inferior; si \(V_{n+1}=1\) y al menos una de las dos celdas de \(n+1\) está conectada, ambas quedan conectadas.

Estados resultantes:
- 0: ocurre si \(H_n^{(0)}=0\) y \(H_n^{(1)}=0\) (y \(V_{n+1}\) no importa porque no hay conexión). Prob \(1/4\). ✓.
- 3: ocurre si ambas horizontales abiertas (\(1/4\)), o exactamente una horizontal abierta y \(V_{n+1}=1\) (\(1/2 \cdot 1/2 \cdot 2 = 1/2\) pero ojo: exactamente una horizontal abierta tiene prob \(1/2\), y \(V_{n+1}=1\) prob \(1/2\), total \(1/4\); espera, calculemos: \(P(\text{exactamente una de } A,C =1)=2\cdot(1/2)(1/2)=1/2\). Con \(B=1\): \(1/2 \cdot 1/2 = 1/4\). Entonces total estado 3: \(1/4 + 1/4 = 1/2\). ✓.
- 1: \(A=1, C=0, B=0\): prob \(1/8\). ✓.
- 2: \(A=0, C=1, B=0\): prob \(1/8\). ✓.

Correcto.

Desde el estado 1 en la columna \(n\): solo superior ocupada.
- \(H_n^{(0)}=0\): estado 0, prob \(1/2\). ✓.
- \(H_n^{(0)}=1\): superior de \(n+1\) conectada. Si \(V_{n+1}=1\), ambas conectadas (estado 3) prob \(1/2\cdot1/2=1/4\). Si \(V_{n+1}=0\), estado 1, prob \(1/4\). ✓.

Bien.

Ahora, la puerta vertical \(V_0\): ¿afecta la transición a la columna 1? No, \(V_0\) solo conecta superior e inferior de la columna 0. Si \(V_0=1\), la inferior de la columna 0 queda ocupada, lo que permite que la inferior de la columna 1 se conecte a través de \(H_0^{(1)}\). Eso ya está capturado: el estado en la columna 0 es 3 con prob \(1/2\), y desde el estado 3 la transición usa \(H_0^{(1)}\). Correcto.

Por lo tanto, el resultado \(22/5\).

Déjame hacer una verificación numérica rápida con simulación mental o suma de columnas para confirmar.

Calculemos las probabilidades de estado por columna y las celdas esperadas por columna.

\(\pi_0 = (0, 1/2, 0, 1/2)\).

Celdas esperadas en columna 0: \(1/2 \cdot 1 + 1/2 \cdot 2 = 3/2 = 1.5\).

Columna 1: \(\pi_1 = \pi_0 P\).

Calculemos \(\pi_1\):
- Desde estado 1 (prob \(1/2\)): a 0 con \(1/2\) → \(1/4\); a 3 con \(1/4\) → \(1/8\); a 1 con \(1/4\) → \(1/8\).
- Desde estado 3 (prob \(1/2\)): a 0 con \(1/4\) → \(1/8\); a 1 con \(1/8\) → \(1/16\); a 2 con \(1/8\) → \(1/16\); a 3 con \(1/2\) → \(1/4\).

Suma \(\pi_1\):
- 0: \(1/4 + 1/8 = 3/8\).
- 1: \(1/8 + 1/16 = 3/16\).
- 2: \(1/16\).
- 3: \(1/8 + 1/4 = 3/8\).

Verificar suma: \(3/8 + 3/16 + 1/16 + 3/8 = 6/16 + 3/16 + 1/16 + 6/16 = 16/16 = 1\). ✓.

Celdas esperadas columna 1: \(1 \cdot 3/16 + 1 \cdot 1/16 + 2 \cdot 3/8 = 4/16 + 6/8 = 1/4 + 3/4 = 1\). Espera, \(4/16 = 1/4\), \(2\cdot 3/8 = 6/8 = 3/4\), total 1.0.

Columna 0: 1.5, columna 1: 1.0. Suma parcial 2.5.

Sigamos. \(\pi_2 = \pi_1 P\).

Calculemos desde \(\pi_1\):

Para estado 0 (prob \(3/8\)): contribuye solo a 0 con \(3/8\).

Estado 1 (prob \(3/16\)): a 0 \(1/2\) → \(3/32\); a 3 \(1/4\) → \(3/64\); a 1 \(1/4\) → \(3/64\).

Estado 2 (prob \(1/16\)): a 0 \(1/2\) → \(1/32\); a 3 \(1/4\) → \(1/64\); a 2 \(1/4\) → \(1/64\).

Estado 3 (prob \(3/8\)): a 0 \(1/4\) → \(3/32\); a 1 \(1/8\) → \(3/64\); a 2 \(1/8\) → \(3/64\); a 3 \(1/2\) → \(3/16\).

Sumemos \(\pi_2\):
- 0: \(3/8 + 3/32 + 1/32 + 3/32 = 3/8 + 7/32 = 12/32 + 7/32 = 19/32\).
- 1: \(3/64 + 3/64 = 6/64 = 3/32\).
- 2: \(1/64 + 3/64 = 4/64 = 1/16\).
- 3: \(3/64 + 1/64 + 3/16 = 4/64 + 12/64 = 16/64 = 1/4\).

Suma: \(19/32 + 3/32 + 1/16 + 1/4 = 22/32 + 2/32 + 8/32 = 32/32\). ✓.

Celdas esperadas columna 2: \(1\cdot 3/32 + 1 \cdot 1/16 + 2\cdot 1/4 = 3/32 + 2/32 + 16/32 = 21/32 = 0.65625\).

Suma parcial: 1.5 + 1 + 0.65625 = 3.15625.

Columna 3: \(\pi_3 = \pi_2 P\).

Estado 0 (19/32): → 0: 19/32.

Estado 1 (3/32): a 0: \(3/64\); a 3: \(3/128\); a 1: \(3/128\).

Estado 2 (1/16 = 2/32): a 0: \(2/64 = 1/32\); a 3: \(1/64 = 2/128\); a 2: \(1/64 = 2/128\).

Estado 3 (1/4 = 8/32): a 0: \(8/128 = 1/16\); a 1: \(8/256 = 1/32\); a 2: \(1/32\); a 3: \(8/64 = 1/8\).

Sumemos con denominador común 256 quizá. Usemos decimales o fracciones.

Voy a sumar con denominador 256.

\(\pi_3^{(0)} = 19/32 + 3/64 + 1/32 + 1/16\).

Convertir: \(19/32 = 152/256\), \(3/64 = 12/256\), \(1/32 = 8/256\), \(1/16 = 16/256\). Suma = \(152+12+8+16 = 188/256 = 47/64\).

\(\pi_3^{(1)} = 3/128 + 1/32\). \(3/128 = 6/256\), \(1/32 = 8/256\). Suma \(14/256 = 7/128\).

\(\pi_3^{(2)} = 2/128 + 1/32\). \(2/128 = 4/256\), \(1/32 = 8/256\). Suma \(12/256 = 3/64\).

\(\pi_3^{(3)} = 3/128 + 2/128 + 1/8\). \(3/128 = 6/256\), \(2/128 = 4/256\), \(1/8 = 32/256\). Suma \(42/256 = 21/128\).

Suma total: \(188 + 14 + 12 + 42 = 256\). ✓.

Celdas esperadas columna 3: \(1 \cdot 7/128 + 1 \cdot 3/64 + 2 \cdot 21/128 = 7/128 + 6/128 + 42/128 = 55/128 = 0.4296875\).

Suma parcial: 3.15625 + 0.4296875 = 3.5859375.

Columna 4: sigamos. La suma total debería acercarse a 4.4.

\(\pi_4 = \pi_3 P\).

Estado 0 (47/64): → 0: 47/64.

Estado 1 (7/128): a 0: \(7/256\); a 3: \(7/512\); a 1: \(7/512\).

Estado 2 (3/64 = 6/128): a 0: \(3/128 = 6/256\); a 3: \(6/512 = 3/256\); a 2: \(3/256\).

Estado 3 (21/128): a 0: \(21/512\); a 1: \(21/1024\); a 2: \(21/1024\); a 3: \(21/256\).

Usemos denominador 1024.

\(\pi_4^{(0)} = 47/64 + 7/256 + 6/256 + 21/512\).

Convertir:
- \(47/64 = 752/1024\).
- \(7/256 = 28/1024\).
- \(6/256 = 24/1024\).
- \(21/512 = 42/1024\).

Suma = \(752+28+24+42 = 846/1024\).

\(\pi_4^{(1)} = 7/512 + 21/1024 = 14/1024 + 21/1024 = 35/1024\).

\(\pi_4^{(2)} = 3/256 + 21/1024 = 12/1024 + 21/1024 = 33/1024\).

\(\pi_4^{(3)} = 7/512 + 3/256 + 21/256 = 14/1024 + 12/1024 + 84/1024 = 110/1024\).

Suma: \(846 + 35 + 33 + 110 = 1024\). ✓.

Celdas esperadas columna 4: \(1\cdot 35/1024 + 1\cdot 33/1024 + 2 \cdot 110/1024 = (35+33+220)/1024 = 288/1024 = 0.28125\).

Suma parcial: 3.5859375 + 0.28125 = 3.8671875.

Columna 5: \(\pi_5 = \pi_4 P\).

Estado 0 (846/1024): → 0: 846/1024.

Estado 1 (35/1024): a 0: \(35/2048\); a 3: \(35/4096\); a 1: \(35/4096\).

Estado 2 (33/1024): a 0: \(33/2048\); a 3: \(33/4096\); a 2: \(33/4096\).

Estado 3 (110/1024): a 0: \(110/4096\); a 1: \(110/8192\); a 2: \(110/8192\); a 3: \(110/2048\).

Usemos denominador 8192.

\(\pi_5^{(0)} = 846/1024 + 35/2048 + 33/2048 + 110/4096\).

Convertir:
- \(846/1024 = 6768/8192\).
- \(35/2048 = 140/8192\).
- \(33/2048 = 132/8192\).
- \(110/4096 = 220/8192\).

Suma = \(6768+140+132+220 = 7260/8192\).

\(\pi_5^{(1)} = 35/4096 + 110/8192 = 70/8192 + 110/8192 = 180/8192\).

\(\pi_5^{(2)} = 33/4096 + 110/8192 = 66/8192 + 110/8192 = 176/8192\).

\(\pi_5^{(3)} = 35/4096 + 33/4096 + 110/2048 = 70/8192 + 66/8192 + 440/8192 = 576/8192\).

Suma: \(7260 + 180 + 176 + 576 = 8192\). ✓.

Celdas esperadas columna 5: \(1\cdot 180/8192 + 1\cdot 176/8192 + 2\cdot 576/8192 = (180+176+1152)/8192 = 1508/8192 = 0.18408203125\).

Suma parcial: 3.8671875 + 0.18408203125 = 4.05126953125.

Columna 6: \(\pi_6 = \pi_5 P\).

Estado 0 (7260/8192): → 0: 7260/8192.

Estado 1 (180/8192): a 0: \(180/16384\); a 3: \(180/32768\); a 1: \(180/32768\).

Estado 2 (176/8192): a 0: \(176/16384\); a 3: \(176/32768\); a 2: \(176/32768\).

Estado 3 (576/8192): a 0: \(576/32768\); a 1: \(576/65536\); a 2: \(576/65536\); a 3: \(576/16384\).

Usemos denominador 65536.

\(\pi_6^{(0)} = 7260/8192 + 180/16384 + 176/16384 + 576/32768\).

Convertir:
- \(7260/8192 = 58080/65536\).
- \(180/16384 = 720/65536\).
- \(176/16384 = 704/65536\).
- \(576/32768 = 1152/65536\).

Suma = \(58080+720+704+1152 = 60656/65536\).

\(\pi_6^{(1)} = 180/32768 + 576/65536 = 360/65536 + 576/65536 = 936/65536\).

\(\pi_6^{(2)} = 176/32768 + 576/65536 = 352/65536 + 576/65536 = 928/65536\).

\(\pi_6^{(3)} = 180/32768 + 176/32768 + 576/16384 = 360/65536 + 352/65536 + 2304/65536 = 3016/65536\).

Suma: \(60656 + 936 + 928 + 3016 = 65536\). ✓.

Celdas esperadas columna 6: \((936 + 928 + 2\cdot 3016)/65536 = (936+928+6032)/65536 = 7896/65536 = 0.1204833984375\).

Suma parcial: 4.05126953125 + 0.1204833984375 = 4.1717529296875.

Columna 7: \(\pi_7 = \pi_6 P\).

Estado 0 (60656/65536): → 0: 60656/65536.

Estado 1 (936/65536): a 0: \(936/131072\); a 3: \(936/262144\); a 1: \(936/262144\).

Estado 2 (928/65536): a 0: \(928/131072\); a 3: \(928/262144\); a 2: \(928/262144\).

Estado 3 (3016/65536): a 0: \(3016/262144\); a 1: \(3016/524288\); a 2: \(3016/524288\); a 3: \(3016/131072\).

Usemos denominador 524288.

\(\pi_7^{(0)} = 60656/65536 + 936/131072 + 928/131072 + 3016/262144\).

Convertir:
- \(60656/65536 = 485248/524288\).
- \(936/131072 = 3744/524288\).
- \(928/131072 = 3712/524288\).
- \(3016/262144 = 6032/524288\).

Suma = \(485248 + 3744 + 3712 + 6032 = 498736/524288\).

\(\pi_7^{(1)} = 936/262144 + 3016/524288 = 1872/524288 + 3016/524288 = 4888/524288\).

\(\pi_7^{(2)} = 928/262144 + 3016/524288 = 1856/524288 + 3016/524288 = 4872/524288\).

\(\pi_7^{(3)} = 936/262144 + 928/262144 + 3016/131072 = 1872/524288 + 1856/524288 + 12064/524288 = 15792/524288\).

Suma: \(498736 + 4888 + 4872 + 15792 = 524288\). ✓.

Celdas esperadas columna 7: \((4888 + 4872 + 2\cdot 15792)/524288 = (4888+4872+31584)/524288 = 41344/524288 = 0.078857421875\).

Suma parcial: 4.1717529296875 + 0.078857421875 = 4.2506103515625.

Columna 8: \(\pi_8 = \pi_7 P\).

Estado 0 (498736/524288): → 0: 498736/524288.

Estado 1 (4888/524288): a 0: \(4888/1048576\); a 3: \(4888/2097152\); a 1: \(4888/2097152\).

Estado 2 (4872/524288): a 0: \(4872/1048576\); a 3: \(4872/2097152\); a 2: \(4872/2097152\).

Estado 3 (15792/524288): a 0: \(15792/2097152\); a 1: \(15792/4194304\); a 2: \(15792/4194304\); a 3: \(15792/1048576\).

Usemos denominador 4194304.

\(\pi_8^{(0)} = 498736/524288 + 4888/1048576 + 4872/1048576 + 15792/2097152\).

Convertir:
- \(498736/524288 = 3989888/4194304\).
- \(4888/1048576 = 19552/4194304\).
- \(4872/1048576 = 19488/4194304\).
- \(15792/2097152 = 31584/4194304\).

Suma = \(3989888 + 19552 + 19488 + 31584 = 4060512/4194304\).

\(\pi_8^{(1)} = 4888/2097152 + 15792/4194304 = 9776/4194304 + 15792/4194304 = 25568/4194304\).

\(\pi_8^{(2)} = 4872/2097152 + 15792/4194304 = 9744/4194304 + 15792/4194304 = 25536/4194304\).

\(\pi_8^{(3)} = 4888/2097152 + 4872/2097152 + 15792/1048576 = 9776/4194304 + 9744/4194304 + 63168/4194304 = 82688/4194304\).

Suma: \(4060512 + 25568 + 25536 + 82688 = 4194304\). ✓.

Celdas esperadas columna 8: \((25568 + 25536 + 2\cdot 82688)/4194304 = (25568+25536+165376)/4194304 = 216480/4194304 = 0.05161285400390625\).

Suma parcial: 4.2506103515625 + 0.05161285400390625 = 4.302223205566406.

Columna 9: \(\pi_9 = \pi_8 P\).

Estado 0 (4060512/4194304): → 0.

Estado 1 (25568/4194304): a 0: \(25568/8388608\); a 3: \(25568/16777216\); a 1: \(25568/16777216\).

Estado 2 (25536/4194304): a 0: \(25536/8388608\); a 3: \(25536/16777216\); a 2: \(25536/16777216\).

Estado 3 (82688/4194304): a 0: \(82688/16777216\); a 1: \(82688/33554432\); a 2: \(82688/33554432\); a 3: \(82688/8388608\).

Usemos denominador 33554432.

\(\pi_9^{(0)} = 4060512/4194304 + 25568/8388608 + 25536/8388608 + 82688/16777216\).

Convertir:
- \(4060512/4194304 = 32484096/33554432\).
- \(25568/8388608 = 102272/33554432\).
- \(25536/8388608 = 102144/33554432\).
- \(82688/16777216 = 165376/33554432\).

Suma = \(32484096 + 102272 + 102144 + 165376 = 32853888/33554432\).

\(\pi_9^{(1)} = 25568/16777216 + 82688/33554432 = 51136/33554432 + 82688/33554432 = 133824/33554432\).

\(\pi_9^{(2)} = 25536/16777216 + 82688/33554432 = 51072/33554432 + 82688/33554432 = 133760/33554432\).

\(\pi_9^{(3)} = 25568/16777216 + 25536/16777216 + 82688/8388608 = 51136/33554432 + 51072/33554432 + 330752/33554432 = 432960/33554432\).

Suma: \(32853888 + 133824 + 133760 + 432960 = 33554432\). ✓.

Celdas esperadas columna 9: \((133824 + 133760 + 2\cdot 432960)/33554432 = (133824+133760+865920)/33554432 = 1133504/33554432 = 0.033782958984375\).

Suma parcial: 4.302223205566406 + 0.033782958984375 = 4.336006164550781.

Columna 10: \(\pi_{10} = \pi_9 P\).

Estado 0 (32853888/33554432): → 0.

Estado 1 (133824/33554432): a 0: \(133824/67108864\); a 3: \(133824/134217728\); a 1: \(133824/134217728\).

Estado 2 (133760/33554432): a 0: \(133760/67108864\); a 3: \(133760/134217728\); a 2: \(133760/134217728\).

Estado 3 (432960/33554432): a 0: \(432960/134217728\); a 1: \(432960/268435456\); a 2: \(432960/268435456\); a 3: \(432960/67108864\).

Usemos denominador 268435456.

\(\pi_{10}^{(0)} = 32853888/33554432 + 133824/67108864 + 133760/67108864 + 432960/134217728\).

Convertir:
- \(32853888/33554432 = 262831104/268435456\).
- \(133824/67108864 = 535296/268435456\).
- \(133760/67108864 = 535040/268435456\).
- \(432960/134217728 = 865920/268435456\).

Suma = \(262831104 + 535296 + 535040 + 865920 = 262801360/268435456\).

\(\pi_{10}^{(1)} = 133824/134217728 + 432960/268435456 = 267648/268435456 + 432960/268435456 = 700608/268435456\).

\(\pi_{10}^{(2)} = 133760/134217728 + 432960/268435456 = 267520/268435456 + 432960/268435456 = 700480/268435456\).

\(\pi_{10}^{(3)} = 133824/134217728 + 133760/134217728 + 432960/67108864 = 267648/268435456 + 267520/268435456 + 1731840/268435456 = 2267008/268435456\).

Suma: \(262801360 + 700608 + 700480 + 2267008 = 268435456\). ✓.

Celdas esperadas columna 10: \((700608 + 700480 + 2\cdot 2267008)/268435456 = (700608+700480+4534016)/268435456 = 5935104/268435456 = 0.0221099853515625\).

Suma parcial: 4.336006164550781 + 0.0221099853515625 = 4.358116149902344.

Sigue acercándose a 4.4. La suma parcial hasta la columna 10 es ~4.3581. El resto a 4.4 es ~0.0419. Como la serie decrece geométricamente con razón ~0.65 (más o menos), el resto es consistente con el valor final 4.4.

Columna 11: estimemos aproximadamente. La razón entre celdas esperadas consecutivas: col9/col10 ≈ 0.03378/0.02211 ≈ 1.53... Espera, las celdas esperadas por columna: col0=1.5, col1=1, col2=0.656, col3=0.4297, col4=0.28125, col5=0.1841, col6=0.1205, col7=0.0789, col8=0.0516, col9=0.0338, col10=0.0221. La razón entre términos consecutivos tiende a ~0.65. Entonces el resto desde col10 es ~0.0221 * 0.65/(1-0.65) = 0.0221*0.65/0.35 ≈ 0.0410. Suma total ≈ 4.3581 + 0.0410 = 4.3991, muy cerca de 4.4. ✓.

Por lo tanto, el resultado exacto es \(22/5 = 4.4\).

Déjame también verificar mediante la solución del sistema. Ya teníamos \(F_1 = 16/5 = 3.2\), \(F_3 = 28/5 = 5.6\). Entonces \(E[S] = (F_1 + F_3)/2 = (3.2 + 5.6)/2 = 4.4\). Coincide con la suma numérica.

Además, otra comprobación: el número esperado de celdas en la columna 0 es 1.5, y la suma total es 4.4. Entonces el número esperado de celdas en columnas \(\ge 1\) es \(4.4 - 1.5 = 2.9\). De la simulación parcial, columnas 1–10 suman ~2.858. El resto ~0.042. Total ~2.9. ✓.

Por lo tanto, la respuesta es \(\frac{22}{5}\).

Antes de finalizar, consideremos si la definición del problema incluye celdas en ambas direcciones. Dice: «una cuadrícula de altura 2 que se extiende infinitamente en una dirección». Entonces solo hay una dirección infinita, con la esquina (celda inicial) en un extremo. La altura es 2. Philip empieza en la celda de la esquina (extremo izquierdo, fila superior o inferior).

¿Podría haber una celda a la izquierda de la esquina? No, porque la esquina es el extremo en esa dirección; la cuadrícula se extiende infinitamente en una sola dirección. Supongo que la dirección infinita es hacia la derecha y la celda inicial está en la columna más a la izquierda.

Confirmación: el problema dice «grid of height 2 stretching infinitely in one direction» y «Philip starts in a corner of the grid (in the starred cell)». La celda con estrella es una esquina, es decir, en el extremo. Por lo tanto, no hay celdas a la izquierda.

Además, la celda inferior de la columna 0 es una esquina también (hay dos esquinas: arriba-izquierda y abajo-izquierda). Philip está en una de ellas, digamos arriba-izquierda.

El resultado no depende de cuál esquina elija, por simetría. De hecho, si empieza abajo-izquierda, por simetría es lo mismo.

Por tanto, la respuesta es \(\boxed{\frac{22}{5}}\).

Voy a escribir una explicación clara en español, paso a paso, y finalmente la respuesta en \boxed{}.

Déjame redactar la solución de forma concisa pero completa.

**Resumen del razonamiento:**

1. Modelo: franja de dos filas infinitas a la derecha, columnas \(n=0,1,2,\dots\). Puertas horizontales \(H_n^{(0)}, H_n^{(1)}\) y verticales \(V_n\), cada una abierta con probabilidad \(1/2\).

2. Estados de una columna: 0 (ninguna alcanzable), 1 (solo superior), 2 (solo inferior), 3 (ambas).

3. Matriz de transición \(P\) entre columnas consecutivas:
   - Desde 1: \(0\) con \(1/2\), \(1\) con \(1/4\), \(3\) con \(1/4\).
   - Desde 2: \(0\) con \(1/2\), \(2\) con \(1/4\), \(3\) con \(1/4\).
   - Desde 3: \(0\) con \(1/4\), \(1\) con \(1/8\), \(2\) con \(1/8\), \(3\) con \(1/2\).

4. Definimos \(F_s\) = número esperado de celdas alcanzables desde la columna actual en adelante, dado el estado \(s\) de la columna actual. \(F_0 = 0\), y por simetría \(F_1 = F_2 = G\).

   Ecuaciones:
   \(G = 1 + \frac14 G + \frac14 F_3\)
   \(F_3 = 2 + \frac14 G + \frac12 F_3\)

   Resolviendo:
   \(G = \frac{16}{5}\), \(F_3 = \frac{28}{5}\).

5. Estado inicial: en la columna 0, con \(V_0\) abierta (prob \(1/2\)) el estado es 3; con \(V_0\) cerrada (prob \(1/2\)) el estado es 1. Entonces:

   \(E = \frac12 F_1 + \frac12 F_3 = \frac12\cdot\frac{16}{5} + \frac12\cdot\frac{28}{5} = \frac{22}{5}\).

Por lo tanto, la respuesta final es:

\[
\boxed{\frac{22}{5}}
\]

Esto es correcto y verificado numéricamente.Voy a resolverlo paso a paso.

## Planteamiento

Tenemos una franja de altura 2 que se extiende infinitamente a la derecha. Numeremos las columnas \(n=0,1,2,\dots\). En cada columna hay dos celdas: fila superior e inferior.

Puertas, cada una abierta con probabilidad \(1/2\):

- \(H_n^{(0)}\): horizontal superior entre columnas \(n\) y \(n+1\).
- \(H_n^{(1)}\): horizontal inferior entre columnas \(n\) y \(n+1\).
- \(V_n\): vertical entre las dos celdas de la columna \(n\).

Philip empieza en la celda superior de la columna \(0\).

## Estados de una columna

Estado de la columna \(n\) (qué celdas pertenecen al componente alcanzable):

- \(0\): ninguna,
- \(1\): solo la superior,
- \(2\): solo la inferior,
- \(3\): ambas.

## Matriz de transición entre columnas

Desde el estado \(1\) (solo superior ocupada):

- La superior de la columna siguiente se alcanza si \(H_n^{(0)}\) está abierta.
- Si no: estado \(0\), probabilidad \(1/2\).
- Si sí y \(V_{n+1}\) abierta: estado \(3\), probabilidad \(1/4\).
- Si sí y \(V_{n+1}\) cerrada: estado \(1\), probabilidad \(1/4\).

Desde el estado \(3\), analizando los casos de \(H_n^{(0)}, H_n^{(1)}, V_{n+1}\):

- a \(0\): \(1/4\),
- a \(1\): \(1/8\),
- a \(2\): \(1/8\),
- a \(3\): \(1/2\).

## Ecuaciones de expectativa

Sea \(F_s\) el número esperado de celdas alcanzables en la columna actual y las siguientes, dado el estado \(s\). Claramente \(F_0=0\), y por simetría \(F_1=F_2=G\). Además:

\[
G=1+\frac14G+\frac14F_3,
\]

(la columna actual aporta 1 celda) y

\[
F_3=2+\frac18G+\frac18G+\frac12F_3
=2+\frac14G+\frac12F_3.
\]

De la primera:

\[
\frac34G=1+\frac14F_3
\implies G=\frac43+\frac13F_3.
\]

De la segunda:

\[
\frac12F_3=2+\frac14G
\implies F_3=4+\frac12G.
\]

Sustituyendo:

\[
G=\frac43+\frac13\left(4+\frac12G\right)
=\frac83+\frac16G.
\]

Por tanto:

\[
\frac56G=\frac83
\implies G=\frac{16}{5}.
\]

Y

\[
F_3=4+\frac12\cdot\frac{16}{5}=4+\frac85=\frac{28}{5}.
\]

## Estado inicial

En la columna \(0\), Philip empieza en la celda superior. Si la puerta vertical \(V_0\) está abierta, el estado es \(3\); si está cerrada, el estado es \(1\). Ambos casos tienen probabilidad \(1/2\).

Entonces el número esperado total de celdas alcanzables es:

\[
E=\frac12F_1+\frac12F_3
=\frac12\cdot\frac{16}{5}+\frac12\cdot\frac{28}{5}
=\frac{8}{5}+\frac{14}{5}
=\frac{22}{5}.
\]

Por lo tanto, la respuesta final es:

\[
\boxed{\frac{22}{5}}
\]