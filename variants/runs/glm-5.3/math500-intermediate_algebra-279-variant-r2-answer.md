# Resolución paso a paso

**Paso 1: Sustitución inicial.** Sea $y = x^4$. Entonces:
$$y^2 + 63y - 64 = (y + 64)(y - 1)$$
por lo que el polinomio se convierte en $(x^4 + 64)(x^4 - 1)$.

**Paso 2: Factorizar $x^4 - 1.$**
$$x^4 - 1 = (x-1)(x+1)(x^2+1)$$

**Paso 3: Factorizar $x^4 + 64$ con la identidad de Sophie Germain.** Usamos $a^4 + 4b^4 = (a^2 - 2ab + 2b^2)(a^2 + 2ab + 2b^2)$ con $b = 2$ (pues $4 \cdot 2^4 = 64$):
$$x^4 + 64 = (x^2 - 4x + 8)(x^2 + 4x + 8)$$
Verificación: $(x^2+8)^2 - (4x)^2 = x^4 + 16x^2 + 64 - 16x^2 = x^4 + 64$. ✓

**Paso 4: Confirmar irreducibilidad.** Los cinco factores $x-1$, $x+1$, $x^2+1$, $x^2-4x+8$ y $x^2+4x+8$ son mónicos, de coeficientes enteros, y los cuadráticos tienen discriminantes $-4$ y $-16$ (negativos), así que son irreducibles sobre $\mathbb{Z}$.

**Paso 5: Evaluar en $x = 1$.**
- $q_1(1) = 1 - 1 = 0$
- $q_2(1) = 1 + 1 = 2$
- $q_3(1) = 1 + 1 = 2$
- $q_4(1) = 1 - 4 + 8 = 5$
- $q_5(1) = 1 + 4 + 8 = 13$

Suma: $0 + 2 + 2 + 5 + 13 = 22$.

$$\boxed{22}$$