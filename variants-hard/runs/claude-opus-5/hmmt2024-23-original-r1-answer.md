## Planteamiento

Sea $O$ el centro de $\Omega$ (radio $123$) y $C$ el centro de $\omega$ (radio $61$), con $|OC| = 61$ ya que $O \in \omega$.

Si los tres segmentos miden $x, 2x, 3x$, la cuerda total mide $6x$ y el segmento central $2x$ es precisamente la cuerda que $\omega$ determina sobre la recta.

**Coordenadas:** tomo $O = (0,0)$ y la recta $y = d$, con $C = (a,b)$, $a^2 + b^2 = 61^2$.

- El pie de la perpendicular desde $O$ es $M = (0,d)$, punto medio de la cuerda de $\Omega$, así que las puntas están en $t = \pm 3x$.
- Los cortes con $\omega$ están entonces en $t = -2x$ y $t = 0$, cuyo punto medio es $t = -x$. Ese punto medio es el pie de la perpendicular desde $C$, es decir $N = (a,d)$, luego $|a| = x$.

## Ecuaciones

Distancia de $C$ a la recta: $e = |d-b|$. De la semicuerda de $\omega$:
$$x^2 = 61^2 - (d-b)^2, \qquad x^2 = a^2 = 61^2 - b^2$$

Restando: $(d-b)^2 = b^2$, de donde $d = 0$ (la cuerda sería diámetro, excluido) o
$$d = 2b.$$

De la semicuerda de $\Omega$: $9x^2 = 123^2 - d^2$, y de la otra relación $x^2 = 61^2 - \tfrac{d^2}{4}$. Sustituyendo:
$$9\left(3721 - \frac{d^2}{4}\right) = 15129 - d^2 \;\Longrightarrow\; 33489 - 15129 = \frac{5}{4}d^2 \;\Longrightarrow\; d^2 = 14688.$$

Entonces $x^2 = 3721 - 3672 = 49$, es decir $x = 7$.

**Verificación:** $9x^2 = 441 = 15129 - 14688$ ✓ y $d^2 = 14688 < 15129$, con $b = d/2$ válido.

La cuerda mide $6x = 42$.

\boxed{42}