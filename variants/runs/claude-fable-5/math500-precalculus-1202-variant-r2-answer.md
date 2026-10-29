Trabajemos el problema.

**Planteamiento.** Sean α = arccos x, β = arccos 2x, γ = arccos 4x, con α + β + γ = π. Entonces α + β = π − γ, y tomando coseno:

$$\cos(\alpha+\beta) = \cos(\pi - \gamma) = -\cos\gamma = -4x.$$

**Expandiendo el lado izquierdo:**

$$\cos\alpha\cos\beta - \sin\alpha\sin\beta = (x)(2x) - \sqrt{1-x^2}\sqrt{1-4x^2} = -4x.$$

Reordenando:

$$2x^2 + 4x = \sqrt{(1-x^2)(1-4x^2)}.$$

**Elevando al cuadrado:**

$$4x^4 + 16x^3 + 16x^2 = (1-x^2)(1-4x^2) = 4x^4 - 5x^2 + 1.$$

Los términos $4x^4$ se cancelan:

$$16x^3 + 21x^2 - 1 = 0.$$

**Minimalidad.** Verificamos que este cúbico es irreducible sobre ℚ probando todas las raíces racionales posibles $\pm 1, \pm\tfrac12, \pm\tfrac14, \pm\tfrac18, \pm\tfrac1{16}$: ninguna anula el polinomio. Por tanto es el polinomio minimal (salvo escala) y los coeficientes $16, 21, 0, -1$ ya son coprimos, así que no se puede reducir la suma.

$$|a| + |b| + |c| + |d| = 16 + 21 + 0 + 1 = 38.$$

$$\boxed{38}$$