## Planteamiento

Los seis puntos son intercambiables, así que conviene separar dos cosas independientes:

1. **Las posiciones** de los seis puntos en la circunferencia (con probabilidad 1 son distintos).
2. **La asignación** de las etiquetas $P,Q,R,S,T,U$ a esas posiciones, que es uniforme entre todas las permutaciones.

Lo que importa es únicamente qué **emparejamiento** inducen los tres segmentos sobre los seis puntos ordenados cíclicamente. Numeremos las posiciones $1,2,3,4,5,6$ según el orden cíclico. El emparejamiento resultante es uniforme entre todos los emparejamientos perfectos de 6 elementos, y hay

$$5 \cdot 3 \cdot 1 = 15$$

emparejamientos posibles, todos equiprobables.

## Condición de cruce

Dos cuerdas se cortan si y solo si sus extremos **se alternan** alrededor del círculo: es decir, cada cuerda separa los dos extremos de la otra.

Busquemos los emparejamientos en los que las tres cuerdas se alternan dos a dos. La cuerda que contiene al punto $1$ debe dejar dos puntos a cada lado para poder ser cruzada por las otras dos cuerdas (si dejara uno o ningún punto a un lado, alguna cuerda quedaría entera en un arco y no cruzaría). Eso fuerza la cuerda $1\text{–}4$. Quedan $\{2,3\}$ de un lado y $\{5,6\}$ del otro, y las dos cuerdas restantes deben cruzar a $1\text{–}4$, luego cada una toma un punto de cada lado. Las opciones son $\{2\text{–}5,\,3\text{–}6\}$ o $\{2\text{–}6,\,3\text{–}5\}$; en la segunda, $3\text{–}5$ y $2\text{–}6$ **no** se alternan (3 y 5 están ambos entre 2 y 6). Así que solo sirve

$$\{1\text{–}4,\; 2\text{–}5,\; 3\text{–}6\}.$$

Hay exactamente **un** emparejamiento favorable.

**Verificación** con la distribución del número de cruces en emparejamientos de 6 puntos: $5$ sin cruces (número de Catalan $C_3=5$), $6$ con un cruce, $3$ con dos y $1$ con tres; en total $5+6+3+1=15$. ✓

## Probabilidad

$$\frac{1}{15}$$

\boxed{\dfrac{1}{15}}