## Resolución

**Paso 1: Factorización inicial.** Tratando el polinomio como una cuadrática en $x^4$:
$$x^8 + 63x^4 - 64 = (x^4 - 1)(x^4 + 64).$$

**Paso 2: Factorizar $x^4 - 1$.**
$$x^4 - 1 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1).$$
Aquí $x^2+1$ es irreducible sobre los enteros (no tiene raíces reales).

**Paso 3: Factorizar $x^4 + 64$.** Usando la identidad de Sophie Germain, $a^4 + 4b^4 = (a^2+2ab+2b^2)(a^2-2ab+2b^2)$, con $a = x$ y $b = 2$ (ya que $4\cdot 2^4 = 64$):
$$x^4 + 64 = (x^2 + 4x + 8)(x^2 - 4x + 8).$$
Ambos factores cuadráticos tienen discriminante $16 - 32 = -16 < 0$, así que son irreducibles sobre los enteros.

**Paso 4: Factorización completa.**
$$x^8 + 63x^4 - 64 = (x-1)(x+1)(x^2+1)(x^2+4x+8)(x^2-4x+8).$$

**Paso 5: Evaluar en $x = 1$ y sumar.**
- $(1-1) = 0$
- $(1+1) = 2$
- $(1+1) = 2$
- $(1+4+8) = 13$
- $(1-4+8) = 5$

Suma: $0 + 2 + 2 + 13 + 5 = 22$.

$$\boxed{22}$$