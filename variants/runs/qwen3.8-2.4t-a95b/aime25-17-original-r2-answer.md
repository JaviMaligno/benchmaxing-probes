Sea $m = n+2$. Entonces $n = m-2$, y como $n$ es un entero positivo, tenemos $m \geq 3$.

Reescribimos los factores del producto en términos de $m$:

$$n+3 = (m-2)+3 = m+1$$

$$n^2+9 = (m-2)^2+9 = m^2-4m+4+9 = m^2-4m+13$$

Por lo tanto, el producto es:

$$3(n+3)(n^2+9) = 3(m+1)(m^2-4m+13)$$

Queremos que $m = n+2$ divida este producto. Analizamos cada factor módulo $m$:

$$m+1 \equiv 1 \pmod{m}$$

$$m^2-4m+13 \equiv 13 \pmod{m}$$

Así que el producto completo es congruente a:

$$3 \cdot 1 \cdot 13 = 39 \pmod{m}$$

Para que $m$ divida el producto, necesitamos que $m \mid 39$.

Los divisores positivos de $39$ son: $1, 3, 13, 39$.

Como $m \geq 3$, descartamos $m=1$. Los valores válidos son:

- $m=3 \Rightarrow n=1$
- $m=13 \Rightarrow n=11$
- $m=39 \Rightarrow n=37$

Verificación rápida:
- $n=1$: $3 \cdot 4 \cdot 10 = 120$, y $3 \mid 120$. ✓
- $n=11$: $3 \cdot 14 \cdot 130 = 5460$, y $13 \mid 5460$. ✓
- $n=37$: $3 \cdot 40 \cdot 1378 = 165360$, y $39 \mid 165360$. ✓

La suma buscada es:

$$1 + 11 + 37 = 49$$

$$\boxed{49}$$