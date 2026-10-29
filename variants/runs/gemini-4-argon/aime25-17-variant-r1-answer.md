Para encontrar todos los enteros positivos $n$ tales que $n+3$ divide al producto $2(n+5)(n^2+7)$, podemos utilizar aritmética modular (o el teorema del resto).

Queremos que:
$$2(n+5)(n^2+7) \equiv 0 \pmod{n+3}$$

Dado que $n \equiv -3 \pmod{n+3}$, sustituimos $n$ por $-3$ en la expresión:
$$2(-3+5)((-3)^2+7) \equiv 2(2)(9+7) \equiv 4(16) \equiv 64 \pmod{n+3}$$

Por lo tanto, $n+3$ divide a $2(n+5)(n^2+7)$ si y solo si $n+3$ divide a $64$.

Como $n$ es un entero positivo ($n \ge 1$), tenemos que $n+3 \ge 4$.
Los divisores positivos de $64 = 2^6$ son $1, 2, 4, 8, 16, 32, 64$. Filtrando aquellos que son mayores o iguales a $4$, obtenemos los posibles valores para $n+3$:
- $n+3 = 4 \implies n = 1$
- $n+3 = 8 \implies n = 5$
- $n+3 = 16 \implies n = 13$
- $n+3 = 32 \implies n = 29$
- $n+3 = 64 \implies n = 61$

Finalmente, sumamos todos los valores posibles de $n$:
$$1 + 5 + 13 + 29 + 61 = 109$$

\boxed{109}