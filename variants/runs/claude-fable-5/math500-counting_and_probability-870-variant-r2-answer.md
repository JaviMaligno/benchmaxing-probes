Un planteamiento clásico. Fijemos primero las posiciones de los seis puntos en el círculo y consideremos solo su orden cíclico: con probabilidad 1 los seis puntos son distintos, y por simetría las etiquetas $P,Q,R,S,T,U$ se asignan a las seis posiciones de manera uniforme sobre las $6!$ permutaciones.

**Paso 1: reducir a emparejamientos.** Lo único que importa es cómo quedan emparejadas las seis posiciones: $\{P,Q\}$, $\{R,S\}$, $\{T,U\}$. Un conjunto de 6 puntos se puede partir en 3 parejas de $\frac{6!}{2^3 \cdot 3!} = 15$ maneras, todas equiprobables por simetría.

**Paso 2: contar los emparejamientos "buenos".** Etiquetemos las posiciones en orden cíclico como $1,2,3,4,5,6$. Dos cuerdas se cortan si y solo si sus extremos se alternan alrededor del círculo. Para que las tres cuerdas se corten dos a dos, cada cuerda debe separar los extremos de las otras dos. Eso obliga a que cada cuerda deje exactamente dos de los puntos restantes a cada lado, es decir, cada cuerda une puntos "opuestos": $\{1,4\}$, $\{2,5\}$, $\{3,6\}$. 

Verificación: $\{1,4\}$ y $\{2,5\}$ se alternan ($1,2,4,5$), $\{1,4\}$ y $\{3,6\}$ se alternan ($1,3,4,6$), y $\{2,5\}$ y $\{3,6\}$ también ($2,3,5,6$). Cualquier otro emparejamiento incluye una cuerda del tipo $\{i, i+1\}$ (vecinos) o $\{i, i+2\}$, que deja a un lado 0 o 1 puntos y por tanto no puede ser cruzada por las otras dos cuerdas a la vez. Así que hay exactamente **1** emparejamiento bueno de los 15.

**Paso 3: probabilidad.**
$$P = \frac{1}{15}$$

$$\boxed{\dfrac{1}{15}}$$