## Planteamiento

Dentro de una caja con 4 bolas, cada bola necesita un vecino en la misma caja. Si descomponemos el contenido de una caja en sus bloques maximales de números consecutivos, ningún bloque puede tener tamaño 1. Como los tamaños suman 4, cada caja es:

- **Tipo A:** un intervalo de 4 consecutivos, o
- **Tipo B:** dos intervalos de 2 consecutivos, **no adyacentes entre sí** (si fueran adyacentes se fusionarían en un intervalo de 4, caso ya contado en el tipo A).

Entonces toda configuración válida corresponde a: ordenar bloques de tamaños 2 y 4 que cubren $1,\dots,16$, y emparejar los bloques de tamaño 2 en cajas, sin emparejar dos bloques de 2 adyacentes. Clasificamos por $k$ = número de cajas de tipo B (hay $2k$ bloques de 2 y $4-k$ bloques de 4).

## Conteo por casos

**$k=0$:** única opción $\{1\text{–}4\},\{5\text{–}8\},\{9\text{–}12\},\{13\text{–}16\}$: $1$ forma.

**$k=1$:** ordenamos 3 cuatros y 2 doses: $\binom{5}{2}=10$ órdenes; los dos doses van juntos en una caja, así que excluimos los órdenes donde son adyacentes ($4$). Total: $6$.

**$k=2$:** $\binom{6}{2}=15$ órdenes de 2 cuatros y 4 doses $t_1,\dots,t_4$. De los 3 emparejamientos, $\{t_1t_3,t_2t_4\}$ siempre vale; $\{t_1t_2,t_3t_4\}$ falla si $t_1t_2$ o $t_3t_4$ son adyacentes; $\{t_1t_4,t_2t_3\}$ falla si $t_2t_3$ son adyacentes. Según la estructura de rachas de los doses: una racha de 4 (3 órdenes): 1 emparejamiento válido; racha de 3 + suelto (6 órdenes): 1; dos rachas de 2 (3 órdenes): 2; racha de 2 + dos sueltos (3 órdenes): 2. Total: $3+6+6+6=21$.

**$k=3$:** $7$ órdenes (posición del único cuatro, que parte los 6 doses en rachas de tamaños $a$ y $6-a$). Contamos emparejamientos perfectos de 6 elementos (15 en total) que evitan las aristas de camino dentro de cada racha, por inclusión-exclusión con $N_j$ = formas de elegir $j$ aristas prohibidas disjuntas y $(5-2j)!!$ emparejamientos del resto:

- $a=0$ o $6$ (camino $P_6$): $15-5\cdot3+6\cdot1-1=5$ cada uno.
- $a=1$ o $5$ ($P_1+P_5$): $15-4\cdot3+3\cdot1-0=6$ cada uno.
- $a=2$ o $4$ ($P_2+P_4$): $15-4\cdot3+4\cdot1-1=6$ cada uno.
- $a=3$ ($P_3+P_3$): $15-4\cdot3+4\cdot1-0=7$.

Total: $2(5)+2(6)+2(6)+7=41$.

**$k=4$:** los 8 doses forman una sola racha ($P_8$, 7 aristas prohibidas). Emparejamientos de 8 elementos: $7!!=105$. Con $N_j=\binom{8-j}{j}$:
$$105-7\cdot15+15\cdot3-10\cdot1+1\cdot1=105-105+45-10+1=36.$$

## Total

$$1+6+21+41+36=105.$$

$$\boxed{105}$$