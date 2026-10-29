## Solución

Etiqueto los vértices del 28-ágono como $0, 1, \dots, 27$. Todos los segmentos tienen la misma longitud, lo que significa que todos son cuerdas del mismo "paso" $k$ (conectan $i$ con $i+k \pmod{28}$), para algún $k$ con $1 \le k \le 14$, ya que longitudes distintas corresponden a pasos distintos.

Para cada $k$ fijo, las cuerdas de paso $k$ forman un grafo circulante que se descompone en $g = \gcd(28, k)$ ciclos, cada uno de longitud $m = 28/g$. Un ciclo de longitud par $m \ge 4$ tiene exactamente $2$ emparejamientos perfectos; si $m$ es impar no tiene ninguno; y si $m = 2$ (diámetros, caso $k=14$) hay exactamente $1$ forma. Por lo tanto, el número de formas para cada $k$ es $2^g$ si $m$ es par ($m\ge 4$), $0$ si $m$ es impar, y $1$ si $k = 14$.

Analizo cada $k$ (con $28 = 4 \cdot 7$):

- **$k$ impar, $k \ne 7$** ($k = 1, 3, 5, 9, 11, 13$): $g = 1$, $m = 28$ → $2$ formas cada uno → $6 \cdot 2 = 12$.
- **$k = 7$**: $g = 7$, $m = 4$ → $2^7 = 128$.
- **$k = 2, 6, 10$**: $g = 2$, $m = 14$ → $2^2 = 4$ cada uno → $3 \cdot 4 = 12$.
- **$k = 4, 8, 12$**: $g = 4$, $m = 7$ impar → $0$.
- **$k = 14$**: $14$ diámetros, una única forma → $1$.

Sumando todo:

$$12 + 128 + 12 + 0 + 1 = 153 - 4 = 149$$

(Verificación de la suma: $12 + 128 = 140$; $140 + 12 = 152$; $152 + 1 = 153$... recalculo con cuidado: $6\cdot 2 = 12$, más $128$ da $140$, más $3 \cdot 4 = 12$ da $152$, más $1$ da $153$. Reviso el caso $k=7$: $\gcd(7,28)=7$, hay $7$ ciclos de longitud $4$, cada uno con $2$ emparejamientos: $2^7 = 128$. Correcto. La suma correcta es $153$... pero verifico de nuevo los $k$ impares: los impares entre $1$ y $13$ son $1,3,5,7,9,11,13$ — siete valores, de los cuales $k=7$ es especial, quedando $6$ con $g=1$. Sí: $12 + 128 + 12 + 1 = 153$.)

Como comprobación del método, aplicado al problema análogo del 24-ágono con 12 segmentos da $1 + 8 + 8 + 8 + 4 + 16 + 64 + 4 = 113$, que es la respuesta conocida, confirmando el procedimiento.

$$\boxed{153}$$