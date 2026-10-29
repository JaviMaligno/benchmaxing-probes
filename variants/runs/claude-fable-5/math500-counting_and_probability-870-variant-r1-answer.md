## Razonamiento

**Paso 1: Reducir el problema a un orden circular.**
Como los seis puntos se eligen de manera independiente y uniforme, podemos pensarlo así: primero se fijan seis posiciones en la circunferencia, y luego las etiquetas $P, Q, R, S, T, U$ se asignan a esas posiciones de manera uniformemente aleatoria. La probabilidad buscada solo depende de cómo quedan emparejadas las posiciones (qué posición queda unida con cuál por una cuerda).

**Paso 2: Contar los emparejamientos posibles.**
El número de formas de dividir 6 puntos en 3 parejas no ordenadas es
$$\frac{6!}{2^3 \cdot 3!} = \frac{720}{48} = 15,$$
y por simetría los 15 emparejamientos son igualmente probables.

**Paso 3: Contar los emparejamientos favorables.**
Numeremos las posiciones $1, 2, 3, 4, 5, 6$ en orden alrededor del círculo. Dos cuerdas se cruzan si y solo si sus extremos se alternan en la circunferencia. Para que las tres cuerdas se crucen dos a dos, cada cuerda debe separar los extremos de las otras dos. Esto obliga a que cada cuerda una puntos "opuestos": el único emparejamiento que funciona es
$$\{1,4\}, \{2,5\}, \{3,6\}.$$
Cualquier otro emparejamiento une dos puntos con menos de dos puntos entre ellos por algún lado, y esa cuerda deja a alguna otra cuerda completamente de un lado, sin cruzarla. Por lo tanto hay exactamente **1** emparejamiento favorable de los 15.

**Paso 4: Concluir.**
$$P = \frac{1}{15}.$$

$$\boxed{\dfrac{1}{15}}$$