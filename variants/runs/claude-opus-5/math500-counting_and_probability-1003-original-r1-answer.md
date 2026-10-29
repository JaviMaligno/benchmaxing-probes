## Planteamiento

Sea $x>0$ tal que:
- $P(F) = \tfrac16 + x$
- $P(7-F) = \tfrac16 - x$
- Las otras cuatro caras: $\tfrac16$ cada una

## Probabilidad de suma 7

Las parejas que suman 7 son las de caras opuestas. Separando:

- Pareja $\{F, 7-F\}$: contribuye $2\left(\tfrac16+x\right)\left(\tfrac16-x\right) = 2\left(\tfrac1{36}-x^2\right)$
- Las otras dos parejas opuestas (4 ordenamientos): $4\cdot\tfrac1{36} = \tfrac19$

Total:
$$P(\text{suma }7) = \frac{2}{36} - 2x^2 + \frac{4}{36} = \frac16 - 2x^2$$

## Resolviendo

$$\frac16 - 2x^2 = \frac{47}{288} \implies \frac{48}{288}-\frac{47}{288} = 2x^2 \implies 2x^2 = \frac{1}{288}$$

$$x^2 = \frac{1}{576} \implies x = \frac{1}{24}$$

Por lo tanto:
$$P(F) = \frac16 + \frac1{24} = \frac{5}{24}$$

Con $m=5$, $n=24$ (coprimos), se obtiene $m+n = 29$.

\boxed{29}