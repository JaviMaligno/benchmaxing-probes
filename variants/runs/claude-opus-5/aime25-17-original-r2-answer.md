## Razonamiento

Sea $m = n+2$. Entonces $n \equiv -2 \pmod{m}$, y reducimos cada factor módulo $m$:

- $n+3 \equiv -2+3 = 1 \pmod m$
- $n^2+9 \equiv (-2)^2+9 = 13 \pmod m$

Por tanto:
$$3(n+3)(n^2+9) \equiv 3 \cdot 1 \cdot 13 = 39 \pmod{m}$$

La condición $m \mid 3(n+3)(n^2+9)$ equivale entonces a $m \mid 39$.

Los divisores positivos de $39$ son $1, 3, 13, 39$. Como $n \geq 1$, se tiene $m = n+2 \geq 3$, lo que descarta $m=1$:

- $m=3 \Rightarrow n=1$
- $m=13 \Rightarrow n=11$
- $m=39 \Rightarrow n=37$

Verificación rápida con $n=1$: $3\cdot 4\cdot 10 = 120$, y $3 \mid 120$. ✓

Suma: $1 + 11 + 37 = 49$.

$\boxed{49}$