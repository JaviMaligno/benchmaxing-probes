Trabajemos con los valores del polinomio en puntos clave. Sea $f(x) = px^2 + qx + r$, y definamos $a = f(0)$, $b = f(1)$, $c = f(2)$, cada uno con $|a|, |b|, |c| \le 1$.

**Expresar $p, q, r$ en términos de $a, b, c$:**

$$a = r, \qquad b = p + q + r, \qquad c = 4p + 2q + r.$$

Resolviendo:

$$p = \frac{a - 2b + c}{2}, \qquad q = \frac{-3a + 4b - c}{2}, \qquad r = a.$$

**Cota superior:** Por desigualdad triangular,

$$|p| \le \frac{|a| + 2|b| + |c|}{2} \le 2, \qquad |q| \le \frac{3|a| + 4|b| + |c|}{2} \le 4, \qquad |r| \le 1,$$

de modo que $|p| + |q| + |r| \le 7$. Hay que verificar que las tres cotas pueden alcanzarse simultáneamente: para que $|p| = 2$ y $|q| = 4$ a la vez, los signos deben alinearse. Tomando $a = c = 1$, $b = -1$ (o los opuestos), obtenemos $p = 2$, $q = -4$, $r = 1$, y las tres desigualdades se vuelven igualdades de forma coherente.

**Construcción que alcanza la cota:** Consideremos

$$f(x) = 2x^2 - 4x + 1 = 2(x-1)^2 - 1,$$

que es el polinomio de Chebyshev $T_2$ trasladado al intervalo $[0,2]$. Para $0 \le x \le 2$ tenemos $(x-1)^2 \in [0,1]$, así que $f(x) \in [-1, 1]$, cumpliendo la condición. Entonces

$$|p| + |q| + |r| = 2 + 4 + 1 = 7.$$

$$\boxed{7}$$