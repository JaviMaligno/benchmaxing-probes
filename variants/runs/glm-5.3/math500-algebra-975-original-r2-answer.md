## Solución paso a paso

**Paso 1: Identificar la condición del dominio.**

La función es $f(x)=\dfrac{1}{|x^2+3x-4|+|x^2+9x+20|}$, así que $x$ no pertenece al dominio exactamente cuando el denominador es cero:

$$|x^2+3x-4|+|x^2+9x+20|=0$$

**Paso 2: Analizar cuándo una suma de valores absolutos es cero.**

Como cada valor absoluto es $\geq 0$, la suma es cero solo si **ambos** términos son cero a la vez:

- $x^2+3x-4 = 0$
- $x^2+9x+20 = 0$

**Paso 3: Factorizar cada polinomio.**

$$x^2+3x-4 = (x+4)(x-1) \quad\Rightarrow\quad \text{raíces: } x=-4,\ x=1$$

$$x^2+9x+20 = (x+4)(x+5) \quad\Rightarrow\quad \text{raíces: } x=-4,\ x=-5$$

**Paso 4: Buscar raíces comunes.**

Necesitamos un valor que anule ambos polinomios simultáneamente:

- Conjunto 1: $\{-4, 1\}$
- Conjunto 2: $\{-5, -4\}$

La única intersección es $x=-4$.

**Verificación en $x=-4$:**
- $(-4)^2+3(-4)-4 = 16-12-4 = 0$ ✓
- $(-4)^2+9(-4)+20 = 16-36+20 = 0$ ✓

Denominador $= 0+0 = 0$, así que $f(-4)$ no está definida. Para cualquier otro $x$, al menos un término del denominador es positivo, así que el denominador no es cero.

## Respuesta final

$$\boxed{-4}$$