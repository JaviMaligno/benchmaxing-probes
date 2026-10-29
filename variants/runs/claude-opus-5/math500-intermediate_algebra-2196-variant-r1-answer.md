## Planteamiento

Sea $s = a - b$. Para maximizar la expresión conviene, fijado $s$, **minimizar** el denominador, es decir minimizar $a^4 + b^4$ sujeto a $a - b = s$.

**Paso 1: minimizar $a^4+b^4$ con $a-b=s$ fijo.**

Escribimos $a = x + \tfrac{s}{2}$, $b = x - \tfrac{s}{2}$. Entonces
$$f(x) = \left(x+\tfrac{s}{2}\right)^4 + \left(x-\tfrac{s}{2}\right)^4 = 2x^4 + 3s^2x^2 + \tfrac{s^4}{8}.$$
Todos los términos en $x$ son no negativos, así que el mínimo se alcanza en $x = 0$, o sea $a = -b = \tfrac{s}{2}$, con valor
$$a^4+b^4 = \frac{s^4}{8}.$$

**Paso 2: optimizar en $s$.**

El problema se reduce a maximizar
$$g(s) = \frac{s}{\frac{s^4}{8} + 96} = \frac{8s}{s^4 + 768}, \qquad s > 0.$$
Derivando (numerador de $g'$):
$$8\left(s^4 + 768\right) - 8s\cdot 4s^3 = 8\left(768 - 3s^4\right) = 0 \implies s^4 = 256 \implies s = 4.$$

Como $g'>0$ para $s<4$ y $g'<0$ para $s>4$, es el máximo global (y para $s\le 0$ la expresión no es positiva).

**Paso 3: valor máximo.**

Con $s=4$: $a = 2$, $b = -2$, y
$$\frac{a-b}{a^4+b^4+96} = \frac{4}{16+16+96} = \frac{4}{128} = \frac{1}{32}.$$

Verificación alternativa por AM–GM: $a^4 + b^4 + 96 = a^4+b^4+16+16+32+32 \ge 6\sqrt[6]{a^4b^4\cdot 16^2\cdot 32^2}$... más directo es notar que $\frac{s^4}{8}+96 \ge 32 s$ para todo $s>0$, pues $s^4 - 256s + 768 = (s-4)^2(s^2+8s+48) \ge 0$.

\boxed{\dfrac{1}{32}}