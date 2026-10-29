Para determinar el mayor valor posible de la expresión
\[\frac{a - b}{a^4 + b^4 + 96}\]
donde $a$ y $b$ son números reales, podemos aplicar la desigualdad entre la media aritmética y la media geométrica (MA-MG).

**Paso 1: Descomponer la constante y aplicar MA-MG**

Observamos que podemos reescribir el denominador agrupando los términos de manera conveniente:
\[a^4 + b^4 + 96 = (a^4 + 48) + (b^4 + 48) = (a^4 + 16 + 16 + 16) + (b^4 + 16 + 16 + 16)\]

Aplicando la desigualdad MA-MG a los cuatro términos positivos $(a^4, 16, 16, 16)$:
\[a^4 + 16 + 16 + 16 \ge 4\sqrt[4]{a^4 \cdot 16 \cdot 16 \cdot 16} = 4 \cdot |a| \cdot 8 = 32|a| \ge 32a\]
Por lo tanto:
\[a^4 + 48 \ge 32a\]

De manera análoga, aplicando la desigualdad MA-MG a $(b^4, 16, 16, 16)$:
\[b^4 + 16 + 16 + 16 \ge 4\sqrt[4]{b^4 \cdot 16 \cdot 16 \cdot 16} = 32|b| \ge -32b\]
Por lo tanto:
\[b^4 + 48 \ge -32b\]

**Paso 2: Sumar las desigualdades**

Sumando ambas desigualdades obtenemos:
\[a^4 + b^4 + 96 \ge 32(a - b)\]

Dado que $a^4 + b^4 + 96 > 0$ para cualesquiera $a, b \in \mathbb{R}$, podemos dividir ambos lados entre $32(a^4 + b^4 + 96)$:
\[\frac{a - b}{a^4 + b^4 + 96} \le \frac{1}{32}\]

**Paso 3: Verificar la condición de igualdad**

La igualdad en la desigualdad MA-MG se alcanza cuando todos los términos son iguales y tienen el signo adecuado:
- $a^4 = 16$ con $a > 0 \implies a = 2$
- $b^4 = 16$ con $b < 0 \implies b = -2$

Sustituyendo $a = 2$ y $b = -2$ en la expresión original:
\[\frac{2 - (-2)}{2^4 + (-2)^4 + 96} = \frac{4}{16 + 16 + 96} = \frac{4}{128} = \frac{1}{32}\]

\boxed{\frac{1}{32}}