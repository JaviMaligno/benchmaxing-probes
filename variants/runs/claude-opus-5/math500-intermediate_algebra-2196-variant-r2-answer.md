## Planteamiento

**Paso 1: minimizar el denominador para una diferencia fija.**

Sea $s = a - b$ fijo. Hay que minimizar $a^4 + b^4$ con $b = a - s$:
$$f(a) = a^4 + (a-s)^4, \qquad f'(a) = 4a^3 + 4(a-s)^3 = 0 \implies a^3 = -(a-s)^3 \implies a = \frac{s}{2}.$$

Entonces $b = -\frac{s}{2}$ y el mínimo es $2\left(\frac{s}{2}\right)^4 = \frac{s^4}{8}$.

**Paso 2: optimizar en $s$.**

La expresión queda (conviene $s > 0$):
$$g(s) = \frac{s}{\frac{s^4}{8} + 96} = \frac{8s}{s^4 + 768}.$$

Derivando el cociente, el numerador de $g'$ es
$$8(s^4 + 768) - 8s\cdot 4s^3 = 8(768 - 3s^4) = 0 \implies s^4 = 256 \implies s = 4.$$

**Paso 3: valor máximo.**
$$g(4) = \frac{32}{256 + 768} = \frac{32}{1024} = \frac{1}{32},$$

alcanzado en $a = 2$, $b = -2$: $\dfrac{4}{16 + 16 + 96} = \dfrac{4}{128} = \dfrac{1}{32}$.

\boxed{\dfrac{1}{32}}