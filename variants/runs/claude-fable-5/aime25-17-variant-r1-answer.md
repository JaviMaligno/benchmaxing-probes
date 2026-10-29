Trabajando módulo $n+3$: tenemos $n \equiv -3$, así que $n+5 \equiv 2$ y $n^2+7 \equiv 9+7 = 16$. Por tanto:

$$2(n+5)(n^2+7) \equiv 2 \cdot 2 \cdot 16 = 64 \pmod{n+3}$$

Entonces $n+3$ divide al producto si y solo si $n+3 \mid 64$. Los divisores de $64$ mayores que $3$ (ya que $n \geq 1$ implica $n+3 \geq 4$) son $4, 8, 16, 32, 64$, que dan $n = 1, 5, 13, 29, 61$.

Verificación rápida con $n=1$: $n+3=4$ y $2\cdot 6\cdot 8 = 96 = 4\cdot 24$. ✓

Suma: $1+5+13+29+61 = 109$.

$$\boxed{109}$$