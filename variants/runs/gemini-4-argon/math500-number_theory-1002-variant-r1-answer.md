Sea $x$ el número entero que buscamos. Según el enunciado, $x$ debe cumplir el siguiente sistema de congruencias:
$$\begin{aligned}
x &\equiv 2 \pmod{7} \\
x &\equiv 8 \pmod{11} \\
x &\equiv 8 \pmod{13}
\end{aligned}$$

1. **Combinamos las dos últimas congruencias:**
   Como $x$ deja el mismo residuo ($8$) al dividirse entre $11$ y entre $13$, y dado que $\text{mcd}(11, 13) = 1$, podemos combinarlas en una sola congruencia módulo $11 \times 13 = 143$:
   $$x \equiv 8 \pmod{143}$$
   Esto significa que podemos expresar $x$ de la forma:
   $$x = 143k + 8$$
   para algún número entero $k$.

2. **Sustituimos en la primera congruencia:**
   Reemplazamos la expresión de $x$ en $x \equiv 2 \pmod{7}$:
   $$143k + 8 \equiv 2 \pmod{7}$$
   Reducimos los coeficientes módulo $7$ sabiendo que $143 = 7 \times 20 + 3 \equiv 3 \pmod{7}$ y $8 \equiv 1 \pmod{7}$:
   $$3k + 1 \equiv 2 \pmod{7}$$
   $$3k \equiv 1 \pmod{7}$$
   Como $3 \times 5 = 15 \equiv 1 \pmod{7}$, multiplicamos ambos lados por $5$:
   $$k \equiv 5 \pmod{7}$$

3. **Hallamos la solución general:**
   Expresamos $k$ como $k = 7m + 5$ para algún entero $m$, y sustituimos de vuelta en la ecuación de $x$:
   $$x = 143(7m + 5) + 8 = 1001m + 715 + 8 = 1001m + 723$$

4. **Buscamos el mayor entero menor que $3000$:**
   Queremos que $1001m + 723 < 3000$:
   $$1001m < 2277$$
   El mayor valor entero que puede tomar $m$ es $m = 2$. Sustituyendo $m = 2$:
   $$x = 1001(2) + 723 = 2002 + 723 = 2725$$

\boxed{2725}