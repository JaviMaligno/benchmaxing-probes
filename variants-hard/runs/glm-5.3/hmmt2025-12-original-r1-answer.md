# Solución paso a paso

**Configuración.** Denotamos las casillas del tablero $3\times 3$:

$$\begin{array}{ccc} a & b & c \\ d & e & f \\ g & h & i \end{array}$$

donde $g$ es la casilla inferior-izquierda (partida) y $c$ la superior-derecha (destino).

**Traducción del problema.** Quitamos 4 casillas de las 7 casillas restantes $\{a,b,d,e,f,h,i\}$ (las casillas $g$ y $c$ deben quedar). Equivalentemente, elegimos un subconjunto $S$ de **3 casillas que permanecen**, y contamos cuántos de esos subconjuntos **no** permiten llegar de $g$ a $c$. En total hay $\binom{7}{3} = 35$ opciones.

**Casillas críticas.** Los únicos vecinos de $g$ son $d$ y $h$; los únicos vecinos de $c$ son $b$ y $f$. Además, ninguna casilla de $\{d,h\]$ es adyacente a ninguna de $\{b,f\}$, así que cualquier camino de $g$ a $c$ necesita casillas intermedias conectando ambos lados.

**Clave: caminos mínimos.** La distancia de Manhattan de $g$ a $c$ es $2+2 = 4$ saltos, así que el camino más corto usa exactamente $3$ casillas intermedias. Como $S$ solo tiene $3$ casillas, $g$ y $c$ quedan conectados **si y solo si** $S$ forma exactamente un camino mínimo (un mono tono con 2 saltos hacia arriba y 2 hacia la derecha).

El número de tales caminos es $\binom{4}{2} = 6$:

- $g\!-\!d\!-\!a\!-\!b\!-\!c$
- $g\!-\!d\!-\!e\!-\!b\!-\!c$
- $g\!-\!h\!-\!e\!-\!b\!-\!c$
- $g\!-\!d\!-\!e\!-\!f\!-\!c$
- $g\!-\!h\!-\!e\!-\!f\!-\!c$
- $g\!-\!h\!-\!i\!-\!f\!-\!c$

(Estos 6 subconjuntos son $\{a,b,d\},\{b,d,e\},\{b,e,h\},\{d,e,f\},\{e,f,h\},\{f,h,i\}$, y una enumeración directa confirma que ningún otro subconjunto de tamaño 3 conecta a $g$ con $c$.)

**Conclusión.** Las configuraciones donde Kelvin **no** puede llegar a casa son:
$$\binom{7}{3} - 6 = 35 - 6 = 29$$

$\boxed{29}$