Para determinar el mayor número real $k$ tal que la desigualdad $2b_1 + 3b_2 > k\,b_3$ se cumpla para todo polígono cerrado simple $Q$ trazado sobre las líneas de la cuadrícula, demostraremos que $k = \frac{3}{2}$ (o $1.5$).

---

### 1. Demostración de que $2b_1 + 3b_2 > \frac{3}{2} b_3$ para todo polígono $Q$

Sea $Q$ un polígono cerrado sobre la cuadrícula que no se cruza ni se toca a sí mismo. Esto significa que la frontera de $Q$, vista como un subgrafo de la cuadrícula infinita, es un ciclo simple en el cual todo vértice de la cuadrícula tiene grado $0$ o $2$.

Consideremos cualquier celda unitaria $C$ (ya sea interior o exterior a $Q$) que tenga exactamente $3$ de sus lados sobre la frontera de $Q$ (es decir, una celda que contribuye a $b_3$). 
- Los $3$ lados de $C$ que pertenecen a $Q$ forman un camino de longitud $3$ a lo largo del borde de $C$: llamemos $e_1, e_2, e_3$ a estas tres aristas en orden consecutivo, de modo que $e_2$ es la arista central (la «base» de la forma en U) y $e_1, e_3$ son las dos aristas paralelas laterales.
- Sean $u$ y $v$ los dos vértices extremos de la arista central $e_2$. En la celda $C$, el vértice $u$ incide en $e_1$ y $e_2$, mientras que el vértice $v$ incide en $e_2$ y $e_3$.
- Como $e_1, e_2, e_3$ pertenecen a $Q$ y todo vértice de $Q$ tiene grado exactamente $2$, ninguna otra arista de la cuadrícula que incida en $u$ o en $v$ puede pertenecer a $Q$.

Ahora consideremos la celda unitaria $C'$ adyacente a $C$ que comparte la arista central $e_2$. Los cuatro lados de $C'$ son:
1. La arista $e_2$, que pertenece a $Q$.
2. Dos aristas perpendiculares a $e_2$, las cuales inciden en $u$ y $v$ respectivamente. Por lo observado anteriormente, **ninguna de estas dos aristas puede pertenecer a $Q$**.
3. La arista $e_2'$ opuesta a $e_2$, que puede o no pertenecer a $Q$.

De esto se deduce que la celda $C'$ tiene únicamente $1$ o $2$ lados en $Q$ (es decir, $C'$ contribuye a $b_1$ o a $b_2$):
- Si $C'$ es una celda de tipo $b_1$, su único lado en $Q$ es $e_2$, por lo que $C'$ recibe la arista central de **a lo sumo una** celda de tipo $b_3$.
- Si $C'$ es una celda de tipo $b_2$, sus únicos dos lados en $Q$ son los lados opuestos $e_2$ y $e_2'$, por lo que $C'$ puede recibir la arista central de **a lo sumo dos** celdas de tipo $b_3$.

Sumando sobre todas las celdas de tipo $b_3$, obtenemos la cota fundamental:
$$b_3 \le b_1 + 2b_2.$$

Además, en cualquier polígono cerrado finito $Q$, si consideramos un segmento horizontal en la frontera superior de su caja delimitadora (con coordenada $y$ máxima), la celda unitaria situada inmediatamente encima de dicho segmento solo puede tocar a $Q$ en su lado inferior, lo que garantiza que $b_1 \ge 1$ (de hecho, $b_1 \ge 4$ considerando los cuatro extremos de la caja delimitadora).

Por lo tanto:
$$2b_1 + 3b_2 = \frac{3}{2}(b_1 + 2b_2) + \frac{1}{2}b_1 \ge \frac{3}{2}b_3 + \frac{1}{2}b_1 > \frac{3}{2}b_3.$$
Esto prueba que la desigualdad se cumple para $k = \frac{3}{2}$.

---

### 2. Construcción que muestra que $k$ no puede ser mayor que $\frac{3}{2}$

Para ver que $\frac{3}{2}$ es el valor máximo posible, construimos una familia de polígonos $Q_{M, L}$ donde el cociente $\frac{2b_1 + 3b_2}{b_3}$ se aproxima arbitrariamente a $\frac{3}{2}$ cuando $M, L \to \infty$.

Para enteros grandes $M$ (par) y $L$:
- En cada franja horizontal $2m \le y \le 2m+1$ (para $m = 0, 1, \dots, M-1$) y $0 \le x \le 2L$, trazamos una onda en zig-zag que alterna entre $y = 2m$ e $y = 2m+1$ en cada paso entero de $x$:
  - Para $m$ par, la onda avanza de izquierda a derecha:
    $$(0, 2m+1) \to (0, 2m) \to (1, 2m) \to (1, 2m+1) \to (2, 2m+1) \to (2, 2m) \to \dots \to (2L, 2m).$$
  - Para $m$ impar, la onda avanza de derecha a izquierda en fase opuesta verticalmente:
    $$(2L, 2m+1) \to (2L, 2m) \to (2L-1, 2m) \to (2L-1, 2m+1) \to \dots \to (0, 2m).$$
- Conectamos el final de la onda $m$ con el inicio de la onda $m+1$ mediante pequeños giros exteriores en $x = 2L+1$ (para $m$ par) y en $x = -1$ (para $m$ impar), y finalmente cerramos el ciclo desde $(0, 2M-2)$ hasta $(0, 1)$ rodeando por la izquierda a lo largo de la recta $x = -2$.

Contemos las celdas para $M, L$ grandes:
1. En cada una de las $M$ franjas $2m \le y \le 2m+1$, las $2L$ celdas unitarias para $0 \le x \le 2L$ tienen exactamente $3$ lados sobre $Q$. Por tanto:
   $$b_3 = 2ML + O(M + L).$$
2. En cada una de las $M-1$ franjas intermedias $2m+1 \le y \le 2m+2$, las celdas con $x$ impar tienen sus lados superior e inferior sobre $Q$ (y ningún lado vertical), contribuyendo a $b_2$, mientras que las celdas con $x$ par tienen $0$ lados sobre $Q$. Por tanto:
   $$b_2 = (M-1)L + O(M + L) = ML + O(M + L).$$
3. Las celdas de tipo $b_1$ solo aparecen en el contorno exterior del conjunto de ondas, por lo que:
   $$b_1 = O(M + L).$$

Tomando el límite cuando $M, L \to \infty$, obtenemos:
$$\lim_{M, L \to \infty} \frac{2b_1 + 3b_2}{b_3} = \lim_{M, L \to \infty} \frac{3ML + O(M + L)}{2ML + O(M + L)} = \frac{3}{2}.$$

Por consiguiente, el mayor número real $k$ es $\frac{3}{2}$.

\boxed{\frac{3}{2}}