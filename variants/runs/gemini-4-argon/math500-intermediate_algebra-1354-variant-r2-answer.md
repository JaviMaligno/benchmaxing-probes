Para calcular la suma
\[S = \frac{1}{1 + z} + \frac{1}{1 + z^2} + \frac{1}{1 + z^3} + \dots + \frac{1}{1 + z^{2027}},\]
utilizamos la condición dada $z^{2027} = 1$.

**Paso 1: Verificar que los denominadores no se anulan**
Si existiera algún entero $k$ tal que $1 + z^k = 0$, entonces $z^k = -1$. Elevando ambos lados a la potencia $2027$ (que es un número impar), obtendríamos:
\[-1 = (-1)^{2027} = (z^k)^{2027} = (z^{2027})^k = 1^k = 1,\]
lo cual es una contradicción. Por lo tanto, todos los términos de la suma están bien definidos.

**Paso 2: Emparejar los términos simétricos**
Para cualquier $k \in \{1, 2, \dots, 2026\}$, como $z^{2027} = 1$, se cumple que $z^{2027 - k} = z^{-k}$. Sumando el término $k$-ésimo con el término $(2027 - k)$-ésimo, tenemos:
\[\frac{1}{1 + z^k} + \frac{1}{1 + z^{2027 - k}} = \frac{1}{1 + z^k} + \frac{1}{1 + z^{-k}} = \frac{1}{1 + z^k} + \frac{z^k}{z^k + 1} = \frac{1 + z^k}{1 + z^k} = 1.\]

**Paso 3: Sumar todos los términos**
Podemos agrupar los primeros $2026$ términos en $\frac{2026}{2} = 1013$ parejas de la forma $(k, 2027 - k)$ para $k = 1, 2, \dots, 1013$. Cada una de estas $1013$ parejas suma $1$.

Por último, evaluamos el término correspondiente a $k = 2027$:
\[\frac{1}{1 + z^{2027}} = \frac{1}{1 + 1} = \frac{1}{2}.\]

Sumando las $1013$ parejas y el último término, obtenemos:
\[S = 1013 \cdot 1 + \frac{1}{2} = \frac{2027}{2}.\]

\boxed{\frac{2027}{2}}