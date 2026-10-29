Para calcular $f^{-1}(0)$ y $f^{-1}(6)$, busco los valores de $x$ tales que $f(x)=0$ y $f(x)=6$.

**Cálculo de $f^{-1}(0)$:**

- Rama $x \leq 3$: $3 - x = 0 \Rightarrow x = 3$. Como $3 \leq 3$, es válido.
- Rama $x > 3$: $-x^3 + 2x^2 + 3x = 0 \Rightarrow -x(x^2 - 2x - 3) = 0 \Rightarrow -x(x-3)(x+1) = 0$, con soluciones $x = 0, 3, -1$. Ninguna cumple $x > 3$.

Por lo tanto, $f^{-1}(0) = 3$.

**Cálculo de $f^{-1}(6)$:**

- Rama $x \leq 3$: $3 - x = 6 \Rightarrow x = -3$. Como $-3 \leq 3$, es válido.
- Rama $x > 3$: $-x^3 + 2x^2 + 3x = 6$. En $x = 3$ la expresión vale $-27 + 18 + 9 = 0$, y para $x > 3$ la función cúbica es decreciente (su derivada $-3x^2 + 4x + 3 < 0$ para $x > 3$), así que toma valores negativos y nunca alcanza $6$.

Por lo tanto, $f^{-1}(6) = -3$.

**Suma:**
$$f^{-1}(0) + f^{-1}(6) = 3 + (-3) = 0$$

$$\boxed{0}$$