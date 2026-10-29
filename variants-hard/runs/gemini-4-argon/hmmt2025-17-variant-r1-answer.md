Para encontrar el número de formas de ordenar $3$ copias de cada una de las $n = 24$ letras del alfabeto griego cumpliendo la condición dada, analicemos primero la restricción para cualquier par de letras distintas.

### Paso 1: Análisis para dos letras distintas
Sean $A$ y $B$ dos letras cualesquiera del alfabeto. La condición depende únicamente del orden relativo de las $3$ copias de $A$ ($A_1, A_2, A_3$ de izquierda a derecha) y las $3$ copias de $B$ ($B_1, B_2, B_3$ de izquierda a derecha).

Para $y_1 = A$ y $y_2 = B$, la cantidad de letras $B$ en los intervalos $(A_1, A_2)$ y $(A_2, A_3)$ debe ser la misma. Como solo hay $3$ copias de $B$ en total, esta cantidad común solo puede ser $0$ o $1$:

1. **Caso $(0, 0)$:** No hay ninguna $B$ entre $A_1$ y $A_2$, ni entre $A_2$ y $A_3$. Esto significa que las tres $A$ son contiguas respecto a las $B$ (forman un bloque $AAA$). Para que la condición simétrica ($y_1 = B, y_2 = A$) también se cumpla, la cantidad de letras $A$ en $(B_1, B_2)$ y en $(B_2, B_3)$ debe ser igual. Como las tres $A$ están juntas, no pueden estar entre dos $B$ consecutivas (pues daría $(3, 0)$ o $(0, 3)$). Por lo tanto, el orden relativo de $A$ y $B$ debe ser:
   $$AAABBB \quad \text{o} \quad BBBAAA$$

2. **Caso $(1, 1)$:** Hay exactamente una $B$ en $(A_1, A_2)$ y una $B$ en $(A_2, A_3)$. La tercera $B$ debe situarse antes de $A_1$ o después de $A_3$. Esto produce los órdenes alternados:
   $$ABABAB \quad \text{o} \quad BABABA$$
   En ambos casos se verifica inmediatamente que hay una sola $A$ tanto en $(B_1, B_2)$ como en $(B_2, B_3)$, cumpliendo la condición en ambos sentidos.

Por consiguiente, una disposición de las $24$ letras es válida si y solo si para todo par de letras distintas $X, Y$, su subsucesión restringida a $\{X, Y\}$ es una de las cuatro configuraciones: $XXXYYY$, $YYYXXX$, $XYXYXY$ o $YXYXYX$.

---

### Paso 2: Estructura global de las $n$ letras
Sea $[X_1, X_3]$ el intervalo de posiciones desde la primera hasta la tercera aparición de la letra $X$. Según el Paso 1, para cualquier par de letras distintas $X$ e $Y$:
- O bien sus intervalos $[X_1, X_3]$ y $[Y_1, Y_3]$ son disjuntos ($X_3 < Y_1$ o $Y_3 < X_1$), lo cual denotaremos por $X \prec Y$ o $Y \prec X$.
- O bien $X$ e $Y$ se alternan ($XYXYXY$ o $YXYXYX$), lo cual denotaremos por $X \sim Y$.

Observemos que si $X \sim Y$, entonces se cumple que $X_1 < Y_2 < X_3$ y $Y_1 < X_2 < Y_3$.
Supongamos ahora que $X \sim Y$ e $Y \sim Z$ con $X \neq Z$. Entonces la posición $Y_2$ pertenece tanto a $[X_1, X_3]$ como a $[Z_1, Z_3]$. Al tener el punto $Y_2$ en común, los intervalos $[X_1, X_3]$ y $[Z_1, Z_3]$ no son disjuntos, lo que obliga a que $X \sim Z$.

Esto demuestra que $\sim$ es una **relación de equivalencia** sobre el conjunto de las $n$ letras, y la relación $\prec$ ordena linealmente las clases de equivalencia. Así, toda cadena válida se descompone como una concatenación de bloques disjuntos correspondientes a las clases de equivalencia $C_1 \prec C_2 \prec \dots \prec C_m$.

---

### Paso 3: Estructura dentro de cada bloque y conteo
Consideremos una clase de equivalencia $C$ con $k$ letras. Como todo par de letras distintas $X, Y \in C$ se alterna:
1. $X_1 < Y_2 < X_3$ para todo $X, Y \in C$, lo que implica que todas las primeras apariciones de las letras de $C$ ocurren antes que todas las segundas apariciones, y estas ocurren antes que todas las terceras apariciones.
2. Además, en las configuraciones alternadas $XYXYXY$ y $YXYXYX$ se cumple siempre que:
   $$X_1 < Y_1 \iff X_2 < Y_2 \iff X_3 < Y_3$$
   Por lo tanto, el orden relativo de las $k$ letras en sus primeras, segundas y terceras apariciones debe ser idéntico. Es decir, el bloque asociado a $C$ tiene necesariamente la forma $\pi \pi \pi$, donde $\pi$ es una permutación de las $k$ letras de $C$.

De este modo, cualquier cadena válida de $n$ letras queda determinada de manera única por:
1. Una permutación global $\Pi$ de las $n$ letras (que define el orden de las primeras apariciones de todas las letras de izquierda a derecha), para la cual hay $n!$ opciones.
2. Una partición de $\Pi$ en $m$ bloques contiguos no vacíos $\pi_1, \pi_2, \dots, \pi_m$ para formar la palabra $(\pi_1)^3 (\pi_2)^3 \cdots (\pi_m)^3$. Como hay $n - 1$ espacios entre las $n$ letras de $\Pi$ donde podemos decidir cortar o no cortar entre bloques, existen $2^{n-1}$ formas de particionar $\Pi$.

Multiplicando ambas elecciones, el número total de disposiciones válidas para $n = 24$ es:
$$2^{24-1} \cdot 24! = 2^{23} \cdot 24!$$

\boxed{2^{23} \cdot 24!}