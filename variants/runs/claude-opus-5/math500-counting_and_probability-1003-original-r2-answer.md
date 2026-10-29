## Planteamiento

Sea $x>0$ tal que:
- $P(F) = \tfrac16 + x$
- $P(F') = \tfrac16 - x$ (cara opuesta)
- las otras cuatro caras: $\tfrac16$ cada una

## Probabilidad de suma 7

Como los pares opuestos suman 7, la suma 7 se obtiene exactamente cuando las caras son opuestas entre sí. Hay 6 pares ordenados $(a, 7-a)$:

- dos de ellos involucran $F$ y $F'$: $(F,F')$ y $(F',F)$, con probabilidad $\left(\tfrac16+x\right)\left(\tfrac16-x\right)$ cada uno;
- los cuatro restantes tienen probabilidad $\tfrac16\cdot\tfrac16 = \tfrac1{36}$ cada uno.

$$P(7) = 2\left(\frac1{36} - x^2\right) + \frac{4}{36} = \frac{6}{36} - 2x^2 = \frac16 - 2x^2$$

## Resolución

$$\frac16 - 2x^2 = \frac{47}{288} \implies 2x^2 = \frac{48}{288} - \frac{47}{288} = \frac1{288}$$

$$x^2 = \frac1{576} \implies x = \frac1{24}$$

Por tanto:

$$P(F) = \frac16 + \frac1{24} = \frac{5}{24}$$

Con $m=5$, $n=24$ (coprimos), $m+n = 29$.

\boxed{29}