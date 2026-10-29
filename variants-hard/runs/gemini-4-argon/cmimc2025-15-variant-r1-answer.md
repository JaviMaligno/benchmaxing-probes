Para hallar el valor esperado de $N$ (el número de veces que descartamos cartas), analicemos qué ocurre con las cartas de un mismo valor durante el recorrido de izquierda a derecha.

### Paso 1: Descomposición por valores
El mazo tiene $12$ cartas con cuatro valores distintos ($5, 6, 7$ y $8$), y exactamente $3$ cartas de cada valor. Para cada valor $v \in \{5, 6, 7, 8\}$, sea $I_v$ el número de veces que realizamos un descarte provocado por un par de cartas de valor $v$. Entonces:
$$N = I_5 + I_6 + I_7 + I_8$$

Veamos qué valores puede tomar $I_v$ fijándonos, por ejemplo, en el valor $5$:
1. **Ningún par de $5$ está adyacente en el mazo:** Nunca encontraremos dos $5$ seguidos, por lo que $I_5 = 0$.
2. **Exactamente dos $5$ están adyacentes (en las posiciones $i-1$ e $i$) y el tercer $5$ está separado:** Para que el primer $5$ (en la posición $i-1$) hubiese sido descartado justo antes de compararse con el segundo $5$ (en la posición $i$), tendría que haber formado un par con la carta en la posición $i-2$. Pero eso requeriría que la carta en $i-2$ también fuera un $5$, lo cual contradice que solo esos dos $5$ están juntos. Por lo tanto, al llegar a la posición $i$ siempre se detectará el par de $5$ y se producirá exactamente un descarte ($I_5 = 1$). El tercer $5$, al estar solo, no podrá formar otro par.
3. **Los tres $5$ están adyacentes (en las posiciones $i-2, i-1$ e $i$):** Como solo hay tres $5$ en todo el mazo, la carta en la posición $i-3$ no es un $5$, así que el primer $5$ (en $i-2$) nunca se descarta al llegar a $i-2$. Al avanzar a $i-1$, los dos primeros $5$ forman un par y provocan un descarte. Como el proceso se reinicia desde la carta siguiente (el tercer $5$ en la posición $i$), este último $5$ queda solo al inicio del nuevo escaneo y no forma otro par. Por tanto, también en este caso $I_5 = 1$.

En conclusión, los descartes producidos por otros valores nunca interfieren con los pares adyacentes de un valor $v$, y $I_v$ es una variable indicadora que vale $1$ si y solo si al menos dos de las tres cartas de valor $v$ quedan adyacentes en el mazo, y $0$ en caso contrario.

### Paso 2: Cálculo de la probabilidad para un valor fijo
El número total de formas equiprobables de elegir las $3$ posiciones que ocupan las cartas de valor $5$ entre las $12$ posiciones del mazo es:
$$\binom{12}{3} = \frac{12 \times 11 \times 10}{6} = 220$$

El número de formas de elegir $3$ posiciones de entre $12$ de modo que **ninguna** pareja sea adyacente es:
$$\binom{12 - 3 + 1}{3} = \binom{10}{3} = \frac{10 \times 9 \times 8}{6} = 120$$

Por lo tanto, la probabilidad de que al menos dos cartas de valor $5$ estén adyacentes es:
$$\mathbb{E}[I_5] = P(I_5 = 1) = 1 - \frac{120}{220} = \frac{100}{220} = \frac{5}{11}$$

### Paso 3: Linealidad de la esperanza
Por simetría, $\mathbb{E}[I_v] = \frac{5}{11}$ para cada uno de los $4$ valores. Aplicando la linealidad de la esperanza:
$$\mathbb{E}[N] = \mathbb{E}[I_5] + \mathbb{E}[I_6] + \mathbb{E}[I_7] + \mathbb{E}[I_8] = 4 \times \frac{5}{11} = \frac{20}{11}$$

\boxed{\frac{20}{11}}