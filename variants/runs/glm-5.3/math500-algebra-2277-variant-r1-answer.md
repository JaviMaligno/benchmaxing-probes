# Solución paso a paso

**Paso 1: Interpretar $g^{-1}(y)$**

Como $g$ está definida a trozos, $g^{-1}(y)$ es el valor de $x$ tal que $g(x)=y$. Debemos buscar en ambas ramas.

**Paso 2: Calcular $g^{-1}(0)$**

*Rama 1 ($x \leq 4$):*
$$4 - x = 0 \implies x = 4$$
Es válida, pues $4 \leq 4$. ✔️

*Rama 2 ($x > 4$):*
$$-x^3 + 3x^2 + 4x = 0 \implies -x(x^2 - 3x - 4) = 0 \implies -x(x-4)(x+1) = 0$$
Las raíces son $x = 0,\ 4,\ -1$, y ninguna cumple $x > 4$. ✖️

Por lo tanto, $g^{-1}(0) = 4$.

**Paso 3: Calcular $g^{-1}(12)$**

*Rama 1 ($x \leq 4$):*
$$4 - x = 12 \implies x = -8$$
Es válida, pues $-8 \leq 4$. ✔️

*Rama 2 ($x > 4$):*
$$-x^3 + 3x^2 + 4x = 12 \implies x^3 - 3x^2 - 4x + 12 = 0$$
Factorizando (probando $x=2$: $8 - 12 - 8 + 12 = 0$ ✔️):
$$(x-2)(x^2 - x - 6) = (x-2)(x-3)(x+2) = 0$$
Las raíces son $x = 2,\ 3,\ -2$, y ninguna cumple $x > 4$. ✖️

Por lo tanto, $g^{-1}(12) = -8$.

**Paso 4: Sumar**

$$g^{-1}(0) + g^{-1}(12) = 4 + (-8) = -4$$

$$\boxed{-4}$$