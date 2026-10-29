## Razonamiento

**Cálculo de $g^{-1}(0)$**

- Rama $x \leq 4$: $4 - x = 0 \Rightarrow x = 4$. Cumple $x \leq 4$. ✓
- Rama $x > 4$: $-x^3 + 3x^2 + 4x = -x(x-4)(x+1) = 0 \Rightarrow x \in \{0, 4, -1\}$. Ninguna satisface $x > 4$. ✗

Por tanto $g^{-1}(0) = 4$.

**Cálculo de $g^{-1}(12)$**

- Rama $x \leq 4$: $4 - x = 12 \Rightarrow x = -8$. Cumple $x \leq 4$. ✓
- Rama $x > 4$: en $x = 4$ la expresión vale $-64 + 48 + 16 = 0$, y su derivada $-3x^2 + 6x + 4$ es negativa para $x > 4$, así que la función decrece desde $0$ y nunca alcanza $12$. ✗

Por tanto $g^{-1}(12) = -8$.

**Suma**

$$g^{-1}(0) + g^{-1}(12) = 4 + (-8) = -4$$

\boxed{-4}