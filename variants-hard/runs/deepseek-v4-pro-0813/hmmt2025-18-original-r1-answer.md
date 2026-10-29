Vamos a razonar paso a paso.

## 1. Entender la dinámica

Tenemos $N = 2025$ números en un círculo. Cada segundo, cada número se reemplaza por el máximo entre él y sus dos vecinos. Es decir:

\[
a_i' = \max(a_{i-1}, a_i, a_{i+1})
\]

con índices tomados módulo $N = 2025$.

Esta operación hace que cada valor "se propague" a los vecinos. Concretamente, después de $t$ segundos, el valor en la posición $i$ es el máximo de los valores originales en posiciones $j$ tales que la distancia en el círculo entre $j$ e $i$ es a lo sumo $t$:

\[
a_i^{(t)} = \max_{j : \operatorname{dist}(i,j) \le t} a_j^{(0)}.
\]

## 2. Cuándo quedan valores distintos

Con el tiempo, todo converge al máximo global $M = \max(a_1, \dots, a_N)$, que vale casi seguramente menos que $1$. Como $N = 2025$ y $t = 100$, la "ventana" de influencia $t$ es menor que $\frac{N-1}{2} = 1012$, así que tras 100 segundos la operación todavía no ha hecho que todo el círculo sea igual al máximo global. De hecho, cada posición mira un arco de $2t+1 = 201$ posiciones.

Entonces, ¿cuándo es cierto que dos posiciones adyacentes $i$ e $i+1$ tienen el mismo valor tras $t$ segundos?

Sea $M_{i,t}$ el máximo del arco de $2t+1$ posiciones centrado en $i$ (es decir, desde $i-t$ hasta $i+t$), y $M_{i+1,t}$ el máximo del arco centrado en $i+1$ (desde $i+1-t$ hasta $i+1+t$). Los arcos se solapan mucho: la única diferencia es que el arco de $i$ contiene la posición $i-t$ y no la posición $i+1+t$, mientras que el arco de $i+1$ contiene $i+1+t$ y no $i-t$.

Por lo tanto:

- Si el **máximo global** de la unión de ambos arcos está en la intersección (que son $2t$ posiciones), entonces $a_i^{(t)} = a_{i+1}^{(t)}$.
- Si el máximo de la unión cae en la posición exclusiva $i-t$ o en la posición exclusiva $i+1+t$, los valores difieren.

De hecho, en este problema con $t = 100$ y valores continuos, $a_i^{(t)} \ne a_{i+1}^{(t)}$ exactamente cuando el máximo entre los $2t+2 = 202$ números $a_{i-t}, \dots, a_{i+1+t}$ está en una de las dos posiciones extremas (la primera o la última de ese bloque).

## 3. Probabilidad de que haya una "ruptura" entre posiciones adyacentes

Consideremos un bloque de $2t+2 = 202$ variables continuas i.i.d. en $[0,1]$. La probabilidad de que el máximo esté en una de las dos posiciones extremas es:

\[
p = \frac{2}{2t+2} = \frac{2}{202} = \frac{1}{101}.
\]

Esto se debe a que, por simetría, el máximo es igualmente probable que esté en cualquiera de las $202$ posiciones.

Aquí la interpretación es importante: "ruptura" significa que $a_i^{(t)} \ne a_{i+1}^{(t)}$, es decir, que el valor cambia al pasar de la posición $i$ a la $i+1$ en el círculo.

## 4. Contar valores distintos

En un círculo con $N$ posiciones, el número de valores distintos tras $t$ segundos es igual al número de "aristas de ruptura" entre posiciones adyacentes, **siempre que haya al menos una ruptura**. Pero si no hay ninguna ruptura, todos los valores son iguales y hay exactly $1$ valor distinto (aunque ocurre con probabilidad que tiende a 0 cuando $N$ crece; aquí es ínfima, pero hay que tener cuidado).

De hecho, como los valores forman bloques contiguos con el mismo valor y los bloques se alternan con rupturas, el número de valores distintos en el círculo es exactamente igual al número de rupturas, salvo cuando hay $0$ rupturas, en cuyo caso hay $1$ valor distinto.

Para $N = 2025$ y $p = 1/101$, la probabilidad de $0$ rupturas es aproximadamente $(1-p)^N$, absolutamente despreciable. Así que podemos suponer que:

\[
\text{número de valores distintos} = \text{número de rupturas}.
\]

## 5. Calcular el valor esperado

Hay $N = 2025$ aristas entre posiciones adyacentes en el círculo. Cada arista es una ruptura con probabilidad $p = 1/101$, pero las rupturas **no son independientes** en general. Sin embargo, para calcular el valor esperado solo necesitamos la linealidad de la esperanza, que no requiere independencia:

\[
\mathbb{E}[\text{número de valores distintos}] \approx \sum_{i=1}^{N} \mathbb{P}(\text{ruptura en la arista } i) = N \cdot p.
\]

Con $N = 2025$ y $p = 1/101$:

\[
N \cdot p = \frac{2025}{101} = \frac{2025}{101} = 20 + \frac{2025 - 2020}{101} = 20 + \frac{5}{101}.
\]

Veamos: $101 \times 20 = 2020$, y $2025 - 2020 = 5$. Por tanto:

\[
\frac{2025}{101} = 20 + \frac{5}{101} = \frac{2025}{101} \approx 20.0495.
\]

¿Es esta la respuesta exacta? Casi, pero hay que revisar un matiz: el suceso de $0$ rupturas. En ese caso el número de valores distintos es $1$, no $0$. La corrección sería:

\[
\mathbb{E}[\text{valores distintos}] = N p + \mathbb{P}(0 \text{ rupturas}) \cdot (1 - 0).
\]

¿Cuánto vale $\mathbb{P}(0 \text{ rupturas})$? Es la probabilidad de que el máximo global esté a distancia $\le t$ de todas las posiciones (o equivalentemente, que todos los arcos de tamaño $2t+1$ contengan al máximo global). En términos más simples, que el máximo global $M$ esté en un arco que interseca a todos los arcos de tamaño $2t+1$; como $2t+1 = 201 < N/2$, para que no haya rupturas el máximo global tiene que estar en la intersección de todos los arcos de tamaño $201$, lo cual es imposible salvo que... de hecho aquí hay que pensarlo bien.

Para que no haya ruptura en una arista concreta, el máximo del bloque de $202$ elementos no puede estar en un extremo. Para que no haya ninguna ruptura en todo el círculo, es necesario que no exista ningún bloque de $202$ elementos con máximo en un extremo. Esto fuerza a que el máximo global esté "centrado" respecto de todas las aristas, lo cual es imposible con $202 < N$. Por tanto la probabilidad de $0$ rupturas es exactamente $0$ (porque en un conjunto de $2025$ variables continuas, siempre existirá una arista cuyo bloque asociado tenga su máximo en un extremo, de hecho hay al menos dos extremos globales). 

En efecto: sea $M$ el máximo global. Considérese la arista a distancia $\lfloor N/2 \rfloor + 1$ a ambos lados del máximo. En uno de los dos semiarcos de longitud $\lfloor N/2 \rfloor$, el máximo de un bloque de $202$ quedará en un extremo. Más rigurosamente, el número de rupturas es siempre al menos $2$? No: puede ser $1$ si el máximo está concentrado de forma peculiar. Pero la probabilidad de $0$ rupturas es $0$ porque los números son continuos (casi seguramente distintos) y con $N$ grande siempre hay alguna arista donde el bloque de $202$ tiene máximo en un extremo.

Así:

\[
\mathbb{E} = N p = \frac{2025}{101}.
\]

## 6. Respuesta

\[
\boxed{\frac{2025}{101}}
\]