## Razonamiento

Los cuatro puntos, con probabilidad 1, son distintos y ocupan posiciones en el círculo que podemos recorrer en orden cíclico. Llamemos $P_1, P_2, P_3, P_4$ a los cuatro puntos ordenados según su posición alrededor de la circunferencia.

Dos cuerdas determinadas por estos cuatro puntos se cruzan si y solo si sus extremos **se alternan** al recorrer el círculo, es decir, si cada cuerda separa los dos extremos de la otra.

Hay exactamente tres formas de emparejar cuatro puntos en dos cuerdas:

1. $P_1P_2$ con $P_3P_4$ — no se cruzan
2. $P_1P_4$ con $P_2P_3$ — no se cruzan
3. $P_1P_3$ con $P_2P_4$ — **sí se cruzan**

Como las etiquetas $A, B, C, D$ se asignan de manera independiente y uniforme, cada una de las $4! = 24$ ordenaciones posibles de las etiquetas sobre las posiciones cíclicas es igualmente probable. Por simetría, el emparejamiento $\{A,B\}, \{C,D\}$ tiene la misma probabilidad de corresponder a cualquiera de las tres configuraciones anteriores.

Verificación por conteo: de las $\binom{4}{2} = 6$ maneras de elegir qué dos de las cuatro posiciones cíclicas ocupan $A$ y $B$, las que producen alternancia son $\{P_1,P_3\}$ y $\{P_2,P_4\}$, o sea 2 de 6.

$$P = \frac{2}{6} = \frac{1}{3}$$

\boxed{\dfrac{1}{3}}