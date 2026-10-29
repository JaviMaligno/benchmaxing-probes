El número total de puertas (aristas del grafo) es

\[
9\cdot 12+13\cdot 8=108+104=212.
\]

En una caminata cerrada sin repetir puertas, las puertas usadas forman un subgrafo conexo con todos los grados pares. Por lo tanto, las puertas **no usadas** deben tener grado impar exactamente en los vértices de grado impar del grafo original.

Los vértices de grado impar son las habitaciones del borde que no son esquinas:

\[
2(13-2)+2(9-2)=22+14=36.
\]

Estos 36 vértices impares deben emparejarse mediante caminos de puertas no usadas. En cada lado hay una cantidad impar de ellos: \(11,11,7,7\). Así, al menos un vértice de cada lado debe emparejarse con otro lado, lo que obliga a tener al menos dos caminos entre lados distintos. La distancia mínima entre lados contiguos es \(2\) (a través de una esquina). Las otras \(16\) parejas pueden ser de puertas adyacentes, de longitud \(1\).

Por lo tanto, al menos

\[
16\cdot 1+2\cdot 2=20
\]

puertas deben quedar sin usar. Luego, como máximo puede usar

\[
212-20=192
\]

puertas.

Esa cota es alcanzable: se dejan sin usar 20 puertas apropiadas en el borde, de modo que todos los grados quedan pares y el subgrafo restante, salvo dos esquinas aisladas, es una componente conexa con \(192\) puertas. Esa componente admite un circuito euleriano, que da la caminata deseada.

\[
\boxed{192}
\]