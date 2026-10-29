Este es un problema de interpolación de Lagrange. Observa que $q(x)$ es exactamente el polinomio de interpolación de Lagrange en los tres puntos $r$, $s$ y $t$ para los valores $3r-1$, $3s-1$ y $3t-1$:

- $q(r) = 3r - 1$ (los otros dos términos se anulan porque contienen el factor $(x-r)$),
- $q(s) = 3s - 1$,
- $q(t) = 3t - 1$.

Por construcción, $q(x)$ tiene grado a lo sumo 2. Pero el polinomio $p(x) = 3x - 1$, de grado 1, también cumple $p(r) = 3r-1$, $p(s) = 3s-1$, $p(t) = 3t-1$. Como dos polinomios de grado $\le 2$ que coinciden en tres puntos distintos deben ser idénticos, se tiene $q(x) = 3x - 1$ para todo $x$.

(Verificación alternativa: el coeficiente de $x^2$ es $\frac{3r-1}{(r-s)(r-t)} + \frac{3s-1}{(s-r)(s-t)} + \frac{3t-1}{(t-r)(t-s)}$, que al poner denominador común $(r-s)(s-t)(t-r)$ da numerador cero, confirmando que el término cuadrático desaparece.)

Por lo tanto, $q(x) = 3x - 1$ y su grado es

$$\boxed{1}$$