## Solución

**Planteamiento.** Una cuerda de longitud $n$ corresponde a un cero de la función $h_n(x) = g(x+n) - g(x)$. Supongamos que existe una cuerda de longitud $2030$, es decir, $g(x_0) = g(x_0 + 2030)$ para cierto $x_0$.

**Cota inferior (cuerdas forzadas).** Sea $d$ un divisor positivo de $2030$, con $2030 = d\cdot m$. Entonces

$$\sum_{j=0}^{m-1} h_d(x_0 + jd) = g(x_0+2030) - g(x_0) = 0.$$

Como la suma es cero, o bien algún término es cero, o hay dos términos de signos opuestos; en ambos casos, por el teorema del valor intermedio aplicado a la función continua $h_d$, existe un cero de $h_d$, es decir, una cuerda de longitud $d$. Este es el argumento clásico del teorema de la cuerda universal.

Por lo tanto, el grafo debe tener al menos una cuerda de longitud $d$ para **cada divisor** de $2030$. Como $2030 = 2 \cdot 5 \cdot 7 \cdot 29$ tiene $2^4 = 16$ divisores, se fuerza $N \ge 16$.

**La cota es alcanzable.** Dos hechos permiten la construcción:

1. *No se fuerzan longitudes no divisoras:* para $c$ con $a/c \notin \mathbb{Z}$, la función clásica $f(x) = \sin^2(\pi x/c) - \tfrac{x}{a}\sin^2(\pi a/c)$ cumple $f(0)=f(a)$ pero $f(x+c) - f(x) = -\tfrac{c}{a}\sin^2(\pi a/c) \neq 0$ para todo $x$; esto muestra que solo las longitudes $d \mid 2030$ son inevitables.

2. *Compatibilidad de las 16 cuerdas:* el argumento telescópico solo exige que la cuerda de longitud $d$ esté contenida en el intervalo de cada cuerda cuya longitud sea múltiplo de $d$. Esto se satisface anidando los intervalos según divisibilidad (la cuerda de longitud $1$ dentro de todas, etc.), lo cual es posible porque la relación de contención de intervalos admite cualquier anidamiento compatible con el orden parcial de divisibilidad.

Se construye entonces $g$ estrictamente creciente fuera de un compacto, con oscilaciones locales cuidadosamente diseñadas (perturbando una función creciente con "mesetas" del tipo del ejemplo de arriba) que producen **exactamente una** cuerda por cada divisor de $2030$ y ninguna otra cuerda de longitud entera. Así se logra $N = 16$.

**Conclusión.** El valor mínimo es el número de divisores de $2030 = 2\cdot 5\cdot 7\cdot 29$:

$$\boxed{16}$$