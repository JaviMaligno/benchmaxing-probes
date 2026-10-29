## Razonamiento paso a paso

**Paso 1: Sustitución inicial.** Sea $y = x^4$. Entonces:
$$x^8 + 3x^4 - 4 = y^2 + 3y - 4 = (y+4)(y-1)$$

**Paso 2: Volver a $x$.** Esto nos da:
$$(x^4+4)(x^4-1)$$

**Paso 3: Factorizar $x^4 - 1$:**
$$x^4 - 1 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1)$$

**Paso 4: Factorizar $x^4 + 4$ (identidad de Sophie Germain):**
$$x^4 + 4 = (x^2+2x+2)(x^2-2x+2)$$

**Paso 5: Verificar irreducibilidad.** Los factores son:
- $x - 1$ y $x + 1$: lineales, irreducibles.
- $x^2 + 1$: discriminante $-4 < 0$, irreducible.
- $x^2 - 2x + 2$: discriminante $4 - 8 = -4 < 0$, irreducible.
- $x^2 + 2x + 2$: discriminante $-4 < 0$, irreducible.

**Paso 6: Evaluar en $x = 1$:**
- $p_1(1) = 1 - 1 = 0$
- $p_2(1) = 1 + 1 = 2$
- $p_3(1) = 1 + 1 = 2$
- $p_4(1) = 1 - 2 + 2 = 1$
- $p_5(1) = 1 + 2 + 2 = 5$... 

Espera, corrijamos: $x^2+2x+2$ en $x=1$ da $1+2+2=5$? No: $1+2+2=5$. Pero verifiquemos el producto total en $x=1$: $p_1(1)\cdots p_5(1) = 0 \cdot 2 \cdot 2 \cdot 1 \cdot 5 = 0$, y efectivamente $1 + 3 - 4 = 0$. ✓

Entonces la suma es: $0 + 2 + 2 + 1 + 5$... revisemos: los factores son $(x-1)$, $(x+1)$, $(x^2+1)$, $(x^2-2x+2)$, $(x^2+2x+2)$:
$$0 + 2 + 2 + 1 + 5 = 10$$

Pero $x^2+2x+2$ en $x=1$: $1 + 2 + 2 = 5$. Hmm, verificación: $(x^2-2x+2)(x^2+2x+2) = (x^2+2)^2 - (2x)^2 = x^4+4x^2+4-4x^2 = x^4+4$. ✓ Y en $x=1$: $x^4+4 = 5 = 1 \cdot 5$. ✓

Suma total: $0 + 2 + 2 + 1 + 5 = 10$.

Espera — revisemos $x^2+2x+2$ en $x=1$ una vez más: $1^2 + 2(1) + 2 = 5$. Correcto. Y $x^2-2x+2 = 1-2+2 = 1$. Correcto.

$$\boxed{10}$$