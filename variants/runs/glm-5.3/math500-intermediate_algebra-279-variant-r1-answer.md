**Paso 1: Sustitución.** Sea $y = x^4$. Entonces:
$$y^2 + 63y - 64 = (y - 1)(y + 64)$$
por lo que
$$x^8 + 63x^4 - 64 = (x^4 - 1)(x^4 + 64).$$

**Paso 2: Factorizar $x^4 - 1$.**
$$x^4 - 1 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1).$$
Los tres factores son irreducibles sobre $\mathbb{Z}$.

**Paso 3: Factorizar $x^4 + 64$ (diferencia de cuadrados con un truco).**
$$x^4 + 64 = x^4 + 16x^2 + 64 - 16x^2 = (x^2+8)^2 - (4x)^2 = (x^2 + 4x + 8)(x^2 - 4x + 8).$$
Ambos cuadráticos tienen discriminante $16 - 32 = -12 < 0$, así que son irreducibles sobre $\mathbb{Z}$.

**Paso 4: Evaluar en $x = 1$.**
- $(x-1)\big|_{x=1} = 0$
- $(x+1)\big|_{x=1} = 2$
- $(x^2+1)\big|_{x=1} = 2$
- $(x^2+4x+8)\big|_{x=1} = 13$
- $(x^2-4x+8)\big|_{x=1} = 5$

**Paso 5: Sumar.**
$$0 + 2 + 2 + 13 + 5 = 22.$$

\boxed{22}