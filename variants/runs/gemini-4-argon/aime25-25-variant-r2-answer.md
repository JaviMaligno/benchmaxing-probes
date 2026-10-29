Para encontrar el número $N$ de subconjuntos de los 17 asientos que pueden ser ocupados por los 9 invitados, podemos representar la fila de asientos como una cadena binaria de longitud 17, donde un $1$ representa un asiento ocupado (hay nueve $1$s) y un $0$ representa un asiento vacío (hay ocho $0$s).

### Paso 1: Traducir la condición del problema
La condición de que "ningún invitado esté sentado junto a otros dos invitados" significa que ningún invitado puede tener tanto el asiento a su izquierda como el asiento a su derecha ocupados. En términos de la cadena binaria, esto equivale a que no haya tres asientos ocupados consecutivos, es decir, no puede aparecer el bloque $111$. Por lo tanto, los asientos ocupados solo pueden formar bloques de longitud $1$ o $2$ separados por al menos un asiento vacío ($0$).

### Paso 2: Plantear el modelo combinatorio
Los ocho asientos vacíos ($0$s) determinan $8 + 1 = 9$ espacios (incluyendo los extremos antes del primer $0$ y después del último $0$) donde se pueden colocar los bloques de $1$s:
$$\_ \ 0 \ \_ \ 0 \ \_ \ 0 \ \_ \ 0 \ \_ \ 0 \ \_ \ 0 \ \_ \ 0 \ \_ \ 0 \ \_$$

Sea $x_i$ la cantidad de $1$s colocados en el $i$-ésimo espacio para $i = 1, 2, \dots, 9$. Como no puede haber bloques de tres o más $1$s consecutivos, cada $x_i$ debe cumplir $x_i \in \{0, 1, 2\}$. Además, como hay 9 invitados en total, debemos tener:
$$x_1 + x_2 + \dots + x_9 = 9$$

### Paso 3: Contar el número de soluciones
Sea $k$ la cantidad de variables $x_i$ que toman el valor $2$.
- Como estas $k$ variables suman $2k$, el resto de la suma ($9 - 2k$) debe obtenerse con variables que toman el valor $1$. Así, hay $9 - 2k$ variables iguales a $1$.
- El número restante de variables, que toman el valor $0$, es $9 - k - (9 - 2k) = k$.

Como la cantidad de variables iguales a $1$ no puede ser negativa ($9 - 2k \ge 0$), los valores posibles para $k$ son $0, 1, 2, 3, 4$. Para cada valor de $k$, el número de formas de elegir cuáles de las 9 variables valen $2$, cuáles valen $0$ y cuáles valen $1$ está dado por el coeficiente multinomial:
$$\frac{9!}{k! \, k! \, (9 - 2k)!} = \binom{9}{2k}\binom{2k}{k}$$

Calculamos este valor para cada $k$:
- Para $k = 0$: $\binom{9}{0}\binom{0}{0} = 1 \times 1 = 1$
- Para $k = 1$: $\binom{9}{2}\binom{2}{1} = 36 \times 2 = 72$
- Para $k = 2$: $\binom{9}{4}\binom{4}{2} = 126 \times 6 = 756$
- Para $k = 3$: $\binom{9}{6}\binom{6}{3} = 84 \times 20 = 1680$
- Para $k = 4$: $\binom{9}{8}\binom{8}{4} = 9 \times 70 = 630$

### Paso 4: Sumar los casos y hallar el residuo
Sumando todos los casos posibles obtenemos $N$:
$$N = 1 + 72 + 756 + 1680 + 630 = 3139$$

Finalmente, calculamos el residuo de dividir $N$ entre $1000$:
$$3139 \equiv 139 \pmod{1000}$$

\boxed{139}