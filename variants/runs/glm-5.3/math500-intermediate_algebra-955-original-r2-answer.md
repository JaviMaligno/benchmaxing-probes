## Planteamiento

Denotamos $p(x) = ax^2 + bx + c$, con $|p(x)| \le 1$ para todo $x \in [0,1]$. La clave es expresar los coeficientes en términos de los valores de $p$ en tres puntos del intervalo: $0$, $\tfrac12$ y $1$.

**Paso 1: Despejar los coeficientes.**

Tenemos:
$$p(0) = c, \qquad p(1) = a+b+c, \qquad p\left(\tfrac12\right) = \tfrac14 a + \tfrac12 b + c.$$

De las dos últimas ecuaciones, restando $c = p(0)$:
$$p(1) - p(0) = a + b, \qquad 4\left[p\left(\tfrac12\right) - p(0)\right] = a + 2b.$$

Restando la primera de la segunda:
$$b = 4p\left(\tfrac12\right) - p(1) - 3p(0),$$
y entonces
$$a = \big(p(1) - p(0)\big) - b = 2p(1) - 4p\left(\tfrac12\right) + 2p(0).$$

**Paso 2: Acotar cada coeficiente.**

Como $|p(x)| \le 1$ en el intervalo, cada uno de estos valores está en $[-1, 1]$, así que por la desigualdad triangular:
$$|a| \le 2|p(1)| + 4\left|p\left(\tfrac12\right)\right| + 2|p(0)| \le 2 + 4 + 2 = 8,$$
$$|b| \le 4\left|p\left(\tfrac12\right)\right| + |p(1)| + 3|p(0)| \le 4 + 1 + 3 = 8,$$
$$|c| = |p(0)| \le 1.$$

Por lo tanto:
$$|a| + |b| + |c| \le 8 + 8 + 1 = 17.$$

**Paso 3: Verificar que 17 es alcanzable.**

La desigualdad triangular parece estricta, pero los tres máximos se pueden lograr a la vez. Consideramos:
$$p(x) = 1 - 8\left(x - \tfrac12\right)^2 = -8x^2 + 8x - 1,$$
es decir, $a = -8$, $b = 8$, $c = -1$.

- Es una parábola cóncava con vértice en $x = \tfrac12$, donde $p\left(\tfrac12\right) = 1$.
- En los extremos: $p(0) = p(1) = -1$.

Como $p$ es monótona a cada lado del vértice, su rango en $[0,1]$ es exactamente $[-1, 1]$, de modo que $|p(x)| \le 1$ en todo el intervalo. ✓

Para este polinomio:
$$|a| + |b| + |c| = 8 + 8 + 1 = 17.$$

## Conclusión

La cota superior 17 se alcanza, así que es el valor máximo buscado.

$$\boxed{17}$$