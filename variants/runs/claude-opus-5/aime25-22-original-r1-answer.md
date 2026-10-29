## Planteamiento

$2025 = 3^4 \cdot 5^2$, así que $A$ tiene $5 \cdot 3 = 15$ divisores de la forma $3^a 5^b$ con $0\le a\le 4$, $0\le b\le 2$. El total de subconjuntos es $2^{15} = 32768$.

## Condición sobre el mcm

El mcm de $B$ es $2025$ si y solo si algún elemento aporta $3^4$ y algún elemento aporta $5^2$ (esto fuerza además que $B$ sea no vacío).

Por inclusión–exclusión, contando los subconjuntos "malos":

- Sin ningún elemento con $a=4$: quedan $4\cdot 3 = 12$ divisores → $2^{12}$ subconjuntos.
- Sin ningún elemento con $b=2$: quedan $5\cdot 2 = 10$ divisores → $2^{10}$ subconjuntos.
- Sin ambos: quedan $4\cdot 2 = 8$ divisores → $2^{8}$ subconjuntos.

$$N = 2^{15} - 2^{12} - 2^{10} + 2^{8} = 32768 - 4096 - 1024 + 256 = 27904$$

## Probabilidad

$$\frac{27904}{32768} = \frac{2^8 \cdot 109}{2^{15}} = \frac{109}{128}$$

Con $m = 109$, $n = 128$ (coprimos), se obtiene $m+n = 237$.

\boxed{237}