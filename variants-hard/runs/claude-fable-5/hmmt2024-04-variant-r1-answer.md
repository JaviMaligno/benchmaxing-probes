## Planteamiento

Sea $g(x) = \dfrac{p(x)}{q(x)}$ con $p, q$ cuadráticos. Definimos

$$h(x) = p(x) - x^3\, q(x).$$

Como $g(k) = k^3$ para $k \in \{1,2,3,4,6\}$, se cumple $p(k) = k^3 q(k)$, es decir, $h(k)=0$ en esos cinco puntos. Como $h$ tiene grado a lo sumo 5, debe ser

$$p(x) - x^3 q(x) = c\,(x-1)(x-2)(x-3)(x-4)(x-6).$$

## Expansión del producto

$$(x-1)(x-2)(x-3)(x-4)(x-6) = x^5 - 16x^4 + 95x^3 - 260x^2 + 324x - 144.$$

## Igualar coeficientes

Escribiendo $q(x) = ax^2 + bx + d$, entonces $x^3 q(x) = ax^5 + bx^4 + dx^3$, y

$$p(x) = x^3 q(x) + c(x^5 - 16x^4 + 95x^3 - 260x^2 + 324x - 144).$$

Como $p$ es cuadrático, los coeficientes de $x^5, x^4, x^3$ deben anularse:

- $x^5$: $a + c = 0$
- $x^4$: $b - 16c = 0$
- $x^3$: $d + 95c = 0$

Tomando $c=1$: $a = -1$, $b = 16$, $d = -95$, y

$$p(x) = -260x^2 + 324x - 144, \qquad q(x) = -x^2 + 16x - 95.$$

## Evaluar en cero

$$g(0) = \frac{p(0)}{q(0)} = \frac{-144}{-95} = \frac{144}{95}.$$

$$\boxed{\dfrac{144}{95}}$$