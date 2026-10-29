## Planteamiento

$2025 = 3^4 \cdot 5^2$, así que $A$ tiene $(4+1)(2+1) = 15$ divisores, y hay $2^{15}$ subconjuntos posibles.

## Condición sobre el mcm

El mcm de $B$ es $2025$ si y solo si:
- algún elemento aporta $3^4$, y
- algún elemento aporta $5^2$.

## Inclusión–exclusión

Contamos los subconjuntos que **fallan**:

- Todos los elementos con exponente de 3 menor o igual a 3: son los divisores de $3^3\cdot 5^2$, es decir $4\cdot 3 = 12$ divisores → $2^{12}$ subconjuntos.
- Todos los elementos con exponente de 5 menor o igual a 1: divisores de $3^4\cdot 5$, es decir $5\cdot 2 = 10$ → $2^{10}$.
- Ambas condiciones: divisores de $3^3\cdot 5$, es decir $4\cdot 2 = 8$ → $2^{8}$.

Subconjuntos válidos:
$$2^{15} - 2^{12} - 2^{10} + 2^{8} = 32768 - 4096 - 1024 + 256 = 27904$$

(Estos subconjuntos son automáticamente no vacíos.)

## Probabilidad

$$\frac{27904}{32768} = \frac{256 \cdot 109}{256 \cdot 128} = \frac{109}{128}$$

Con $\gcd(109,128)=1$, se tiene $m+n = 109 + 128 = 237$.

\boxed{237}