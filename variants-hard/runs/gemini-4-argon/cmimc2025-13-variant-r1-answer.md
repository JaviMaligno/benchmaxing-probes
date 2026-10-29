Para encontrar la probabilidad de que Priya y Tomas bailen juntos en la misma ronda, podemos analizar el juego utilizando la simetría y el conteo de parejas.

**Paso 1: Determinar el número total de rondas**
Comenzamos con $45$ amigos. En cada ronda, participan $5$ personas en el duelo de baile, $1$ gana y se queda, y las otras $4$ quedan eliminadas. Por lo tanto, el número de jugadores disminuye en $4$ después de cada ronda.
Para que quede solo $1$ jugador al final, deben ser eliminados $45 - 1 = 44$ jugadores.
El número total de rondas es:
$$\frac{44}{4} = 11 \text{ rondas}$$

**Paso 2: Contar cuántas parejas bailan juntas en todo el juego**
En cada ronda participan $5$ personas. La cantidad de parejas de jugadores que se enfrentan entre sí en una sola ronda es:
$$\binom{5}{2} = \frac{5 \times 4}{2} = 10 \text{ parejas}$$

Observemos que, de las $5$ personas que participan en una ronda, a lo sumo $1$ continúa en el juego (el ganador). Esto significa que es imposible que dos personas que hayan bailado juntas en una ronda vuelvan a coincidir en una ronda futura, ya que al menos una de las dos habrá sido eliminada. 

En consecuencia, las parejas que se enfrentan en cada ronda son completamente disjuntas. A lo largo de las $11$ rondas, el número total de parejas distintas que llegan a bailar juntas es:
$$11 \times 10 = 110 \text{ parejas}$$

**Paso 3: Calcular la probabilidad para Priya y Tomas**
El número total de parejas posibles que se pueden formar entre los $45$ amigos es:
$$\binom{45}{2} = \frac{45 \times 44}{2} = 990 \text{ parejas}$$

Dado que en cada ronda la selección es aleatoria y todos los amigos tienen la misma probabilidad de ganar, por simetría todas las parejas de amigos tienen exactamente la misma probabilidad de enfrentarse en algún momento del juego.

Por lo tanto, la probabilidad de que la pareja formada por Priya y Tomas sea una de las $110$ parejas que bailan juntas es:
$$P = \frac{110}{990} = \frac{1}{9}$$

\boxed{\frac{1}{9}}