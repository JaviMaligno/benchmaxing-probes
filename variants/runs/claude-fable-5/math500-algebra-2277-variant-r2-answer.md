Para calcular cada valor de la inversa, busco qué entradas producen las salidas 0 y 12, verificando ambas ramas.

**Cálculo de $g^{-1}(0)$:**

- Rama $x \leq 4$: $4 - x = 0 \Rightarrow x = 4$. Como $4 \leq 4$, es válido.
- Rama $x > 4$: $-x^3 + 3x^2 + 4x = 0 \Rightarrow x(-x^2 + 3x + 4) = 0$, con raíces $x = 0, 4, -1$. Ninguna cumple $x > 4$.

Por lo tanto, $g^{-1}(0) = 4$.

**Cálculo de $g^{-1}(12)$:**

- Rama $x \leq 4$: $4 - x = 12 \Rightarrow x = -8$. Como $-8 \leq 4$, es válido.
- Rama $x > 4$: $-x^3 + 3x^2 + 4x = 12 \Rightarrow x^3 - 3x^2 - 4x + 12 = 0$, que se factoriza como $(x-3)(x-2)(x+2) = 0$, con raíces $3, 2, -2$. Ninguna cumple $x > 4$.

Por lo tanto, $g^{-1}(12) = -8$.

**Suma:** $g^{-1}(0) + g^{-1}(12) = 4 + (-8) = -4$.

$$\boxed{-4}$$