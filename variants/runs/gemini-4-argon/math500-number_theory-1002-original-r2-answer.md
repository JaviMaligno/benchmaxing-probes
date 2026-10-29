Buscamos el mayor número entero $n < 2010$ que cumpla con el siguiente sistema de congruencias:
$$\begin{aligned}
n &\equiv 5 \pmod{7} \\
n &\equiv 10 \pmod{11} \\
n &\equiv 10 \pmod{13}
\end{aligned}$$

**Paso 1: Combinar las dos últimas congruencias.**
Dado que $n$ deja el mismo residuo ($10$) al dividirse entre $11$ y entre $13$, y como $\text{mcd}(11, 13) = 1$, podemos combinar ambas condiciones en una sola módulo $11 \times 13 = 143$:
$$n \equiv 10 \pmod{143}$$

Por lo tanto, podemos expresar $n$ de la forma:
$$n = 143k + 10$$
para algún número entero $k$.

**Paso 2: Sustituir en la primera congruencia.**
Sustituimos esta expresión en la condición $n \equiv 5 \pmod{7}$:
$$143k + 10 \equiv 5 \pmod{7}$$

Sabemos que $143 = 7 \times 20 + 3$, por lo que $143 \equiv 3 \pmod{7}$, y además $10 \equiv 3 \pmod{7}$. Reduciendo módulo $7$, obtenemos:
$$3k + 3 \equiv 5 \pmod{7}$$
$$3k \equiv 2 \pmod{7}$$

Multiplicamos ambos lados por $5$ (el inverso multiplicativo de $3$ módulo $7$, ya que $3 \times 5 = 15 \equiv 1 \pmod{7}$):
$$k \equiv 10 \equiv 3 \pmod{7}$$

**Paso 3: Encontrar la solución general y el mayor valor menor que $2010$.**
Como $k = 7m + 3$ para algún entero $m$, sustituimos de vuelta en la ecuación de $n$:
$$n = 143(7m + 3) + 10 = 1001m + 429 + 10 = 1001m + 439$$

Probamos valores enteros para $m$ buscando el mayor $n < 2010$:
- Para $m = 0$: $n = 439$
- Para $m = 1$: $n = 1001(1) + 439 = 1440$
- Para $m = 2$: $n = 1001(2) + 439 = 2441$ (mayor que $2010$)

\boxed{1440}