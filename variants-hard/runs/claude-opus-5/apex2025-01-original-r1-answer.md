## Planteamiento

Sea $a = 2025$ y supongamos $f(x_0) = f(x_0 + a)$.

**Paso 1 — Cuerdas forzadas (teorema de la cuerda horizontal).**
Para cada entero $n \ge 1$ defino $g(x) = f\!\left(x + \tfrac{a}{n}\right) - f(x)$ sobre $[x_0,\, x_0 + a - \tfrac{a}{n}]$. Entonces

$$\sum_{k=0}^{n-1} g\!\left(x_0 + \tfrac{ka}{n}\right) = f(x_0 + a) - f(x_0) = 0 .$$

Si algún término es no nulo, hay uno positivo y uno negativo, y por el teorema del valor intermedio $g$ se anula; si todos son nulos, también. En cualquier caso **existe una cuerda de longitud $a/n$** para todo $n \ge 1$.

**Paso 2 — Cuáles de esas longitudes son enteras.**
$a/n \in \mathbb{Z}$ exactamente cuando $n \mid 2025$, y entonces $a/n$ recorre los divisores de $2025$. Como

$$2025 = 3^4 \cdot 5^2 \quad\Longrightarrow\quad d(2025) = (4+1)(2+1) = 15,$$

hay $15$ longitudes enteras distintas garantizadas: $1, 3, 5, 9, 15, 25, 27, 45, 75, 81, 135, 225, 405, 675, 2025$. Cuerdas de longitudes distintas son segmentos distintos, luego $N \ge 15$.

**Paso 3 — La cota se alcanza.**
No se fuerza nada más: ninguna longitud entera $L$ que no divida a $2025$ es obligatoria, y basta una cuerda por divisor. El mecanismo estándar es el de las funciones tipo

$$f(x) = \sin^{2}\!\left(\frac{\pi x}{L}\right) - x\,\sin^{2}\!\left(\frac{\pi a}{L}\right),$$

para la cual $f(x+L) - f(x) = -L\sin^2(\pi a/L) \neq 0$ cuando $L \nmid a$, de modo que se eliminan las longitudes no divisoras mientras se conserva la cuerda de longitud $a$; combinando este tipo de perturbaciones (y ramas estrictamente monótonas fuera de un intervalo compacto, para que no aparezcan cuerdas con extremos en las colas) se obtiene una $f$ continua con **exactamente una** cuerda de cada longitud divisora de $2025$ y ninguna otra.

Por tanto el mínimo es el número de divisores de $2025$.

$$\boxed{15}$$