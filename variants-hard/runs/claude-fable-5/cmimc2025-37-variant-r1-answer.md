## Planteamiento

Módulo 3 se tiene $1+x+x^2 \equiv (1-x)^2 \pmod 3$, ya que $(1-x)^2 = 1-2x+x^2 \equiv 1+x+x^2$.

Por lo tanto:
$$(1+x+x^2)^{2019} \equiv (1-x)^{4038} \pmod 3,$$
y entonces
$$\binom{2019}{k}_3 \equiv (-1)^k \binom{4038}{k} \pmod 3.$$

## Aplicando Lucas

Escribimos $4038$ en base 3:
$$4038 = (1,2,1,1,2,1,2,0)_3 \quad (\text{de } 3^7 \text{ a } 3^0).$$

Por el teorema de Lucas, $\binom{4038}{k} \equiv \prod_i \binom{n_i}{k_i} \pmod 3$, que es no nulo solo si cada dígito $k_i \le n_i$. Los factores posibles:

- Posiciones con dígito $1$ (hay 4: $3^7, 3^5, 3^4, 3^2$): $k_i \in \{0,1\}$, factor siempre $1$.
- Posiciones con dígito $2$ (hay 3: $3^6, 3^3, 3^1$): $k_i \in \{0,1,2\}$, factor $2$ si $k_i=1$, y $1$ si $k_i\in\{0,2\}$.
- Posición con dígito $0$ ($3^0$): forzosamente $k_0 = 0$.

Si $m$ es el número de posiciones de dígito $2$ con $k_i = 1$, entonces $\binom{4038}{k} \equiv 2^m \equiv (-1)^m \pmod 3$.

## La condición

Queremos $(-1)^k \cdot (-1)^m \equiv 1 \pmod 3$, es decir $k \equiv m \pmod 2$.

Como las potencias de 3 son impares, $k \equiv \sum_i k_i \pmod 2$. Separando:
- En posiciones de dígito $2$: $k_i \bmod 2 = 1$ exactamente cuando $k_i = 1$, así que su aporte a la paridad es exactamente $m$.
- En posiciones de dígito $1$: aportan $\sum k_i$ con $k_i \in \{0,1\}$.

Entonces $k \equiv m + (\text{número de unos en las posiciones de dígito } 1) \pmod 2$, y la condición $k \equiv m$ se reduce a:

**el número de unos entre las 4 posiciones de dígito $1$ debe ser par.**

## Conteo

- Posiciones de dígito $1$: elecciones de $\{0,1\}^4$ con cantidad par de unos: $2^4/2 = 8$.
- Posiciones de dígito $2$: libres, $3^3 = 27$ opciones.
- Posición de dígito $0$: $1$ opción.

Total: $8 \cdot 27 = 216$.

$$\boxed{216}$$