# Solución

**Paso 1: Plantear la condición de máximo.**

Sea $M$ el valor máximo de $\frac{a-b}{a^4+b^4+96}$. En el punto donde se alcanza, la razón entre el numerador y el denominador debe ser estacionaria. Igualando las derivadas parciales de $\frac{a-b}{a^4+b^4+96}$ a cero:

- Con respecto a $a$: $\frac{a^4+b^4+96 - (a-b)\cdot 4a^3}{(a^4+b^4+96)^2} = 0$
- Con respecto a $b$: $\frac{-(a^4+b^4+96) - (a-b)\cdot 4b^3}{(a^4+b^4+96)^2} = 0$

**Paso 2: Simplificar las condiciones.**

Si $M = \frac{a-b}{a^4+b^4+96}$, las condiciones se vuelven $1 = 4Ma^3$ y $-1 = 4Mb^3$. Por lo tanto:

$$a^3 = \frac{1}{4M}, \qquad b^3 = -\frac{1}{4M}$$

Esto implica $b = -a$, y $a > 0$ (pues $M > 0$).

**Paso 3: Sustituir $b = -a$.**

Con $b=-a$ tenemos $a - b = 2a$ y $a^4 + b^4 = 2a^4$, así que:

$$M = \frac{2a}{2a^4 + 96} = \frac{a}{a^4 + 48}$$

Combinando con $M = \frac{1}{4a^3}$:

$$\frac{a}{a^4+48} = \frac{1}{4a^3} \implies 4a^4 = a^4 + 48 \implies 3a^4 = 48 \implies a^4 = 16 \implies a = 2$$

Entonces $M = \frac{1}{4\cdot 8} = \frac{1}{32}$, alcanzado en $(a,b) = (2,-2)$: efectivamente $\frac{2-(-2)}{16+16+96} = \frac{4}{128} = \frac{1}{32}$. ✓

**Paso 4: Verificar que es el máximo global.**

Debemos comprobar que $a - b \le \frac{a^4+b^4+96}{32}$ para todo $(a,b)$, es decir:

$$\underbrace{(a^4 - 32a + 48)}_{g(a)} + \underbrace{(b^4 + 32b + 48)}_{h(b)} \ge 0$$

Ahora bien, $g'(a) = 4a^3 - 32 = 0$ solo en $a = 2$, y $g(2) = 16 - 64 + 48 = 0$ es el mínimo de $g$ (pues $g \to \infty$ cuando $|a| \to \infty$). Análogamente, $h'(b) = 4b^3 + 32 = 0$ solo en $b = -2$, y $h(-2) = 0$ es el mínimo de $h$. Por lo tanto $g(a) \ge 0$ y $h(b) \ge 0$ siempre, con igualdad exactamente en $(2,-2)$.

Por lo tanto, el valor máximo es

$$\boxed{\dfrac{1}{32}}$$