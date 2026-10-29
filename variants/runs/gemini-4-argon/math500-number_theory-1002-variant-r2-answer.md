Sea $x$ el número entero que buscamos. Según el enunciado, $x$ debe cumplir el siguiente sistema de congruencias:
$$\begin{aligned}
x &\equiv 2 \pmod{7} \\
x &\equiv 8 \pmod{11} \\
x &\equiv 8 \pmod{13}
\end{aligned}$$

**Paso 1: Combinar las dos últimas congruencias.**
Dado que $x$ deja el mismo residuo ($8$) al dividirse por $11$ y por $13$, y como $\text{mcd}(11, 13) = 1$, podemos combinar ambas condiciones en una sola:
$$x \equiv 8 \pmod{11 \times 13}$$
$$x \equiv 8 \pmod{143}$$

Esto significa que podemos escribir $x$ de la forma:
$$x = 143k + 8$$
para algún número entero $k$.

**Paso 2: Sustituir en la primera congruencia.**
Sustituimos la expresión de $x$ en la condición módulo $7$:
$$143k + 8 \equiv 2 \pmod{7}$$

Reducimos los coeficientes módulo $7$ sabiendo que $143 = 7 \times 20 + 3 \equiv 3 \pmod{7}$ y $8 \equiv 1 \pmod{7}$:
$$3k + 1 \equiv 2 \pmod{7}$$
$$3k \equiv 1 \pmod{7}$$

Multiplicamos ambos lados por $5$ (el inverso multiplicativo de $3$ módulo $7$, ya que $3 \times 5 = 15 \equiv 1 \pmod{7}$):
$$k \equiv 5 \pmod{7}$$

Por lo tanto, $k$ se puede expresar como $k = 7m + 5$ para algún entero $m$.

**Paso 3: Encontrar la solución general.**
Sustituimos $k$ en nuestra ecuación para $x$:
$$x = 143(7m + 5) + 8$$
$$x = 1001m + 715 + 8$$
$$x = 1001m + 723$$

**Paso 4: Hallar el mayor entero menor que $3000$.**
Buscamos el valor más grande de $m$ tal que $x < 3000$:
$$1001m + 723 < 3000$$
$$1001m < 2277$$

El mayor entero $m$ que cumple esta desigualdad es $m = 2$. Sustituyendo $m = 2$:
$$x = 1001(2) + 723 = 2002 + 723 = 2725$$

\boxed{2725}