Para factorizar, trato el polinomio como cuadrática en $x^4$:

$$x^8 + 63x^4 - 64 = (x^4 - 1)(x^4 + 64).$$

**Primer factor:**
$$x^4 - 1 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1).$$

**Segundo factor** (identidad de Sophie Germain, $a^4 + 4b^4$ con $b=2$):
$$x^4 + 64 = (x^2 + 4x + 8)(x^2 - 4x + 8).$$

Ambos factores cuadráticos tienen discriminante $16 - 32 = -16 < 0$, así que son irreducibles sobre los enteros, igual que $x^2+1$.

La factorización completa es:
$$(x-1)(x+1)(x^2+1)(x^2+4x+8)(x^2-4x+8).$$

Evaluando cada factor en $x=1$:
- $x-1 \to 0$
- $x+1 \to 2$
- $x^2+1 \to 2$
- $x^2+4x+8 \to 13$
- $x^2-4x+8 \to 5$

Suma: $0 + 2 + 2 + 13 + 5 = 22$.

$$\boxed{22}$$