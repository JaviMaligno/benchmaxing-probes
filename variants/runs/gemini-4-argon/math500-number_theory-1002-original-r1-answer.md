Sea $n$ el número entero que buscamos. Según el enunciado, $n$ debe cumplir el siguiente sistema de congruencias:
$$\begin{aligned}
n &\equiv 5 \pmod{7} \\
n &\equiv 10 \pmod{11} \\
n &\equiv 10 \pmod{13}
\end{aligned}$$

**Paso 1: Combinar las dos últimas congruencias.**
Dado que $n$ deja el mismo residuo ($10$) al dividirse tanto por $11$ como por $13$, significa que $n - 10$ es múltiplo de $11$ y de $13$. Como $11$ y $13$ son primos entre sí, $n - 10$ es múltiplo de $\text{mcm}(11, 13) = 11 \times 13 = 143$. Por lo tanto:
$$n \equiv 10 \pmod{143}$$
Esto nos permite escribir $n$ en la forma:
$$n = 143k + 10$$
para algún número entero $k$.

**Paso 2: Sustituir en la primera congruencia.**
Sustituimos la expresión de $n$ en la condición módulo $7$:
$$143k + 10 \equiv 5 \pmod{7}$$

Reducimos los coeficientes módulo $7$ (sabiendo que $143 = 7 \times 20 + 3$ y $10 = 7 \times 1 + 3$):
$$3k + 3 \equiv 5 \pmod{7}$$
$$3k \equiv 2 \pmod{7}$$

Multiplicamos ambos lados por $5$, que es el inverso multiplicativo de $3$ módulo $7$ (ya que $3 \times 5 = 15 \equiv 1 \pmod{7}$):
$$k \equiv 10 \equiv 3 \pmod{7}$$

Por lo tanto, $k$ se puede escribir como $k = 7m + 3$ para algún entero $m$.

**Paso 3: Hallar la forma general de $n$ y el mayor valor menor que $2010$.**
Sustituimos $k$ de vuelta en la ecuación para $n$:
$$n = 143(7m + 3) + 10 = 1001m + 429 + 10 = 1001m + 439$$

Probamos valores enteros para $m$ buscando el mayor $n < 2010$:
- Para $m = 0$: $n = 439$
- Para $m = 1$: $n = 1001(1) + 439 = 1440$
- Para $m = 2$: $n = 1001(2) + 439 = 2441$ (que supera $2010$)

\boxed{1440}