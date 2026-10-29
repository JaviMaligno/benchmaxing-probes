Para encontrar el número $N$ de subconjuntos de 8 sillas de un total de 16 sillas en fila que cumplen con la condición dada, podemos representar la fila de sillas como una cadena binaria de longitud 16, donde un $1$ representa una silla ocupada y un $0$ representa una silla vacía.

La cadena tiene exactamente ocho $1$s (sillas ocupadas) y ocho $0$s (sillas vacías). La condición de que "ninguna persona se siente junto a otras dos personas" significa que ninguna silla ocupada puede tener sillas ocupadas tanto a su izquierda como a su derecha; es decir, no puede haber tres o más $1$s consecutivos (no aparece la subcadena $111$).

Por lo tanto, los bloques maximales de $1$s consecutivos solo pueden ser de longitud 1 ($1$) o de longitud 2 ($11$).

Sea $k$ el número de bloques de longitud 2 ($11$) y $m$ el número de bloques de longitud 1 ($1$). Como hay ocho $1$s en total, se cumple que:
$$2k + m = 8$$
donde $k$ puede tomar los valores $0, 1, 2, 3, 4$.

Para un valor fijo de $k$:
1. El número de bloques de longitud 1 es $m = 8 - 2k$.
2. El número total de bloques de $1$s es $B = k + m = 8 - k$.
3. El número de formas de ordenar estos $B$ bloques (eligiendo cuáles $k$ de ellos son de longitud 2) es $\binom{8-k}{k}$.
4. Estos $B$ bloques deben estar separados por al menos un $0$. Como hay ocho $0$s, estos generan $8 + 1 = 9$ espacios posibles (incluyendo los extremos) donde podemos colocar a lo sumo un bloque de $1$s por espacio. El número de formas de elegir los espacios para los $B = 8 - k$ bloques es $\binom{9}{8-k} = \binom{9}{k+1}$.

Así, el número total de subconjuntos válidos $N$ está dado por la suma sobre todos los valores posibles de $k$:
$$N = \sum_{k=0}^{4} \binom{8-k}{k} \binom{9}{k+1}$$

Calculamos cada término de la suma:
- Para $k = 0$: $\binom{8}{0} \binom{9}{1} = 1 \times 9 = 9$
- Para $k = 1$: $\binom{7}{1} \binom{9}{2} = 7 \times 36 = 252$
- Para $k = 2$: $\binom{6}{2} \binom{9}{3} = 15 \times 84 = 1260$
- Para $k = 3$: $\binom{5}{3} \binom{9}{4} = 10 \times 126 = 1260$
- Para $k = 4$: $\binom{4}{4} \binom{9}{5} = 1 \times 126 = 126$

Sumando todos los casos obtenemos:
$$N = 9 + 252 + 1260 + 1260 + 126 = 2907$$

Al dividir $N = 2907$ entre $1000$, el residuo es $907$.

\boxed{907}