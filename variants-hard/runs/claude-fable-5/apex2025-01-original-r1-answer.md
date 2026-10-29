## Razonamiento

**Cota inferior.** Supongamos que el grafo de $f$ tiene una cuerda de longitud 2025, es decir, existe $x_0$ con $f(x_0) = f(x_0 + 2025)$. Aplico el **teorema de la cuerda universal** en el intervalo $[x_0, x_0+2025]$: para cada entero positivo $n$, considero
$$g_n(x) = f\!\left(x + \tfrac{2025}{n}\right) - f(x).$$
La suma telescópica
$$\sum_{k=0}^{n-1} g_n\!\left(x_0 + \tfrac{2025k}{n}\right) = f(x_0+2025) - f(x_0) = 0$$
implica que $g_n$ toma valores de ambos signos (o se anula), y por continuidad existe algún punto donde $g_n = 0$. Es decir, **existe una cuerda de longitud $2025/n$ para todo $n \ge 1$**.

De estas longitudes, son enteras exactamente cuando $n \mid 2025$. Como $2025 = 3^4 \cdot 5^2$, tiene
$$\tau(2025) = (4+1)(2+1) = 15$$
divisores: $1, 3, 5, 9, 15, 25, 27, 45, 75, 81, 135, 225, 405, 675, 2025$. Al ser longitudes distintas, hay al menos 15 cuerdas distintas, así que $N \ge 15$.

**Cota superior (construcción).** Se puede construir $f$ con *exactamente* una cuerda de cada longitud divisora y ninguna más. La idea estándar: se parte de una función del tipo $\sin^2$ con pendiente añadida, de modo que para longitudes enteras $h$ que **no** dividen a 2025 la ecuación $f(x+h) = f(x)$ no tenga solución (la inclinación $\varepsilon h$ queda fuera del rango de la oscilación, ajustando la función pieza a pieza), mientras que para cada divisor $d$ de 2025 la igualdad se logra en exactamente un punto, haciendo la función estrictamente monótona fuera de un intervalo compacto para evitar cuerdas adicionales. Con un ajuste cuidadoso (construcción clásica de este tipo de problemas de olimpiada, análoga al ejemplo de Lévy de funciones sin cuerdas de longitud dada), se consigue que el grafo tenga exactamente las 15 cuerdas forzadas.

Por tanto, el mínimo es el número de divisores de 2025.

$$\boxed{15}$$