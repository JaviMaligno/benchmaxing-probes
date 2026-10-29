Voy a resolver el problema paso a paso.

**Planteamiento.** Queremos que $n+3 \mid 2(n+5)(n^2+7)$. Escribamos $d = n+3$, de modo que $n \equiv -3 \pmod{d}$.

**Reducimos cada factor módulo $d$.**
- $n+5 \equiv -3+5 \equiv 2 \pmod{d}$
- $n^2+7 \equiv (-3)^2+7 = 9+7 \equiv 16 \pmod{d}$

Entonces:
$$2(n+5)(n^2+7) \equiv 2 \cdot 2 \cdot 16 = 64 \pmod{n+3}$$

Por lo tanto, la condición equivale a que $n+3$ divida a $64$.

**Enumeramos los casos.** Los divisores positivos de $64$ son $1, 2, 4, 8, 16, 32, 64$, que dan $n = d - 3 \in \{-2, -1, 1, 5, 13, 29, 61\}$. Los enteros **positivos** son:
$$n \in \{1, 5, 13, 29, 61\}$$

**Suma.**
$$1 + 5 + 13 + 29 + 61 = 109$$

**Verificación.** Para $n=1$: $n+3=4$ y $2\cdot 6 \cdot 8 = 96$, divisible entre $4$. Para $n=61$: $n+3=64$ y el producto es $\equiv 64 \pmod{64}$, o sea divisible. Para $d=128$ (que daría $n=125$): el producto es $\equiv 64 \pmod{128}$, que **no** es divisible, así que no faltan casos.

$$\boxed{109}$$