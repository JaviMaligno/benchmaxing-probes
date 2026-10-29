## Planteamiento

Factorizo: $2025 = 3^4 \cdot 5^2$, así que los divisores son $3^a 5^b$ con $0\le a\le 4$, $0\le b\le 2$. En total hay $(4+1)(2+1)=15$ divisores, y $B$ se elige uniformemente entre los $2^{15}$ subconjuntos.

## Condición sobre el lcm

Para que $\mathrm{lcm}(B)=2025$ necesito:
- algún elemento con exponente $a=4$ (potencia de 3 máxima), y
- algún elemento con exponente $b=2$ (potencia de 5 máxima).

Notar que esto ya fuerza $B\neq\varnothing$.

## Conteo por inclusión-exclusión

- Divisores con $a=4$: hay $3$ (uno por cada $b\in\{0,1,2\}$).
- Divisores con $b=2$: hay $5$ (uno por cada $a\in\{0,\dots,4\}$).
- Divisores con $a=4$ **y** $b=2$: solo $1$ (el propio $2025$).

Diviso­res "neutros" (sin $a=4$ ni $b=2$): $4\cdot 2 = 8$.

Subconjuntos que **violan** alguna condición (no tienen ningún elemento con $a=4$, o ninguno con $b=2$):

$$N_{\text{malos}} = 2^{12} + 2^{10} - 2^{8}$$

- sin ningún $a=4$: quedan $15-3=12$ divisores libres $\Rightarrow 2^{12}$;
- sin ningún $b=2$: quedan $15-5=10$ $\Rightarrow 2^{10}$;
- sin $a=4$ **ni** $b=2$: quedan $15-(3+5-1)=8$ $\Rightarrow 2^{8}$ (caso contado dos veces).

Entonces los subconjuntos válidos son:

$$N = 2^{15} - 2^{12} - 2^{10} + 2^{8} = 32768 - 4096 - 1024 + 256 = 27904$$

## Probabilidad

$$P = \frac{27904}{32768} = \frac{109}{128}$$

con $\gcd(109,128)=1$ (109 es primo y 128 es potencia de 2).

Por lo tanto $m=109$, $n=128$:

$$m+n = 237$$

\boxed{237}