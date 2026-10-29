Analicemos el problema.

**Planteamiento:** Como $f(x) = px^2 + qx + r$ está acotada por 1 en valor absoluto en $[0,2]$, evaluamos en tres puntos convenientes: $x = 0, 1, 2$:

- $f(0) = r$
- $f(1) = p + q + r$
- $f(2) = 4p + 2q + r$

Resolviendo para los coeficientes en términos de estos valores:

$$p = \frac{f(0) - 2f(1) + f(2)}{2}, \qquad q = \frac{-3f(0) + 4f(1) - f(2)}{2}, \qquad r = f(0).$$

**Cotas:** Como $|f(0)|, |f(1)|, |f(2)| \le 1$:

$$|p| \le \frac{1 + 2 + 1}{2} = 2, \qquad |q| \le \frac{3 + 4 + 1}{2} = 4, \qquad |r| \le 1.$$

Por lo tanto $|p| + |q| + |r| \le 7$.

**Alcanzabilidad:** Hay que verificar que las tres cotas se logran simultáneamente. El candidato natural es el polinomio de Chebyshev trasladado al intervalo $[0,2]$: con $t = x - 1$,

$$f(x) = 2(x-1)^2 - 1 = 2x^2 - 4x + 1.$$

Verificación: en $[0,2]$, $(x-1)^2 \in [0,1]$, así que $f(x) \in [-1,1]$; en efecto $f(0) = 1$, $f(1) = -1$, $f(2) = 1$. La condición se cumple y

$$|p| + |q| + |r| = 2 + 4 + 1 = 7.$$

Las cotas de $p$, $q$ y $r$ se saturan todas con el patrón de signos $f(0)=1, f(1)=-1, f(2)=1$, que es exactamente el que da este polinomio, de modo que el máximo es alcanzable.

$$\boxed{7}$$