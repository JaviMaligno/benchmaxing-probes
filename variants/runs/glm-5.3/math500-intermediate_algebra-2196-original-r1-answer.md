# Resolución

## Planteamiento

Queremos maximizar
$$f(x,y) = \frac{x - y}{x^4 + y^4 + 6}.$$

Observamos que el denominador siempre es positivo ($x^4 + y^4 + 6 \ge 6 > 0$), así que $f$ está bien definida en todo $\mathbb{R}^2$. Además, $f \to 0$ cuando $|x| + |y| \to \infty$, así que el máximo se alcanza en algún punto.

## Conjetura a partir de un punto de prueba

Probemos $x = 1$, $y = -1$:
$$f(1,-1) = \frac{1 - (-1)}{1 + 1 + 6} = \frac{2}{8} = \frac{1}{4}.$$

Conjeturamos que el máximo es $\frac{1}{4}$, es decir, que para **todos** $(x,y)$ se cumple
$$\frac{x - y}{x^4 + y^4 + 6} \le \frac{1}{4}.$$

## Demostración de la cota

Como el denominador es positivo, la desigualdad equivale a demostrar:
$$4(x - y) \le x^4 + y^4 + 6,$$
es decir:
$$x^4 + y^4 + 6 - 4x + 4y \ge 0.$$

Reorganizamos separando las variables:
$$(x^4 - 4x + 3) + (y^4 + 4y + 3) \ge 0.$$

**Factorizamos cada bloque.** Para $x$:
$$x^4 - 4x + 3 = (x - 1)^2(x^2 + 2x + 3).$$
Verificación: $(x^2 - 2x + 1)(x^2 + 2x + 3) = x^4 + 2x^3 + 3x^2 - 2x^3 - 4x^2 - 6x + x^2 + 2x + 3 = x^4 - 4x + 3$. ✓

Para $y$, de forma análoga:
$$y^4 + 4y + 3 = (y + 1)^2(y^2 - 2y + 3).$$

**Ambos factores son no negativos**, ya que:
- $(x-1)^2 \ge 0$ y $x^2 + 2x + 3 = (x+1)^2 + 2 > 0$;
- $(y+1)^2 \ge 0$ y $y^2 - 2y + 3 = (y-1)^2 + 2 > 0$.

Por lo tanto:
$$(x - 1)^2(x^2 + 2x + 3) + (y + 1)^2(y^2 - 2y + 3) \ge 0,$$
lo que confirma que
$$\frac{x - y}{x^4 + y^4 + 6} \le \frac{1}{4} \quad \text{para todo } (x, y) \in \mathbb{R}^2.$$

## Verificación de que la cota se alcanza

La igualdad se logra cuando ambos cuadrados se anulan simultáneamente:
$$x - 1 = 0 \quad \text{y} \quad y + 1 = 0 \implies x = 1,\ y = -1.$$

En efecto:
$$f(1, -1) = \frac{2}{8} = \frac{1}{4}.$$

## Conclusión

La cota superior $\frac{1}{4}$ se cumple para todos los reales $x, y$, y se alcanza exactamente en $(x, y) = (1, -1)$.

$$\boxed{\dfrac{1}{4}}$$