## Planteamiento

Aplicamos Cauchy–Schwarz escribiendo $b_i^2 = b_i^{1/2}\cdot b_i^{3/2}$:

$$\left(\sum b_i^2\right)^2 \le \left(\sum b_i\right)\left(\sum b_i^3\right)$$

Con los datos:

- Lado izquierdo: $144^2 = 20736$
- Lado derecho: $108 \cdot 192 = 20736$

Se cumple la **igualdad**, lo que obliga a que los vectores $(b_i^{1/2})$ y $(b_i^{3/2})$ sean proporcionales: $b_i^{3/2} = \lambda\, b_i^{1/2}$, es decir $b_i = \lambda$ para todo $i$.

## Determinación de $n$

De $n\lambda = 108$ y $n\lambda^2 = 144$ se obtiene $\lambda = \tfrac{144}{108} = \tfrac43$, y por tanto

$$n = \frac{108}{4/3} = 81.$$

Verificación con los cubos: $81\cdot\left(\tfrac43\right)^3 = 81\cdot\tfrac{64}{27} = 192$. ✓

Como la solución es única, la suma de todos los valores posibles de $n$ es $81$.

\boxed{81}