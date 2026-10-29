Voy a razonar el problema y, de paso, verificar mi conteo con una comprobación rápida por fuerza bruta.

**Razonamiento:**

La cuadrícula tiene 3 filas de puntos ($y = 0, 1, 2$) y $n$ columnas ($x = 0, \dots, n-1$). Un cuadrado con vértices en puntos de la red y vector lateral $(a,b)$ tiene caja envolvente de lado $|a|+|b|$. Como la altura disponible es 2, se necesita $|a|+|b| \le 2$, lo que da exactamente **tres tamaños** (coincidiendo con el enunciado):

1. **Lado 1** (vector $(1,0)$): caja $1\times 1$ → posiciones: $(n-1)$ horizontales × $2$ verticales = $2(n-1)$.
2. **Lado 2** (vector $(2,0)$): caja $2\times 2$ → $(n-2)$ horizontales × $1$ vertical = $n-2$.
3. **Lado $\sqrt{2}$** (vector $(1,1)$, girado 45°): caja $2\times 2$ → $(n-2) \times 1 = n-2$.

Total: $2(n-1) + (n-2) + (n-2) = 4n - 6$.

Verifiquemos esto computacionalmente para estar seguros: