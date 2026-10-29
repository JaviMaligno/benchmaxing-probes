## Planteamiento

Etiquemos la cuadrícula (fila 1 = arriba):

| | col 1 | col 2 | col 3 |
|---|---|---|---|
|fila 1| A | **H** | C |
|fila 2| D | E | F |
|fila 3| **S** | G | I |

donde $S=(3,1)$ es Kelvin y $H=(1,2)$ es su casa. Hay que quitar 4 de las 7 casillas restantes, es decir **conservar 3** de $\{A,C,D,E,F,G,I\}$. En total $\binom{7}{3}=35$ configuraciones.

## Caminos de $S$ a $H$

Enumero todos los caminos simples y su interior (vértices intermedios):

- $S$–$D$–$A$–$H$: interior $\{D,A\}$
- $S$–$D$–$E$–$H$: interior $\{D,E\}$
- $S$–$G$–$E$–$H$: interior $\{G,E\}$
- Todos los demás ($S$–$G$–$I$–$F$–$C$–$H$, $S$–$D$–$E$–$F$–$C$–$H$, $S$–$G$–$E$–$F$–$C$–$H$, $S$–$G$–$I$–$F$–$E$–$H$, $S$–$G$–$E$–$D$–$A$–$H$, etc.) tienen **al menos 4** vértices interiores.

Como solo conservamos 3 casillas intermedias, Kelvin llega a casa **si y solo si** el conjunto conservado contiene $\{D,A\}$, $\{D,E\}$ o $\{G,E\}$.

## Conteo por inclusión–exclusión

Conjuntos de tamaño 3 que contienen cada par: $\binom{5}{1}=5$ en cada caso.

- Intersecciones: $\{D,A\}\cap\{D,E\} \Rightarrow \{A,D,E\}$: 1 conjunto. $\{D,E\}\cap\{G,E\} \Rightarrow \{D,E,G\}$: 1 conjunto. $\{D,A\}$ con $\{G,E\}$ exigiría 4 casillas: 0.
- Triple intersección: 0.

$$|A\cup B\cup C| = 5+5+5-1-0-1+0 = 13$$

Hay 13 configuraciones en las que **sí** puede llegar, luego las que lo dejan aislado son

$$35 - 13 = 22.$$

\boxed{22}