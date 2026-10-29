Esta expresión es exactamente el polinomio de interpolación de Lagrange que pasa por los tres puntos $(r, 3r-1)$, $(s, 3s-1)$ y $(t, 3t-1)$.

**Paso 1: Reconocer la estructura.** El polinomio de Lagrange para los valores $y_r = 3r-1$, $y_s = 3s-1$, $y_t = 3t-1$ en los nodos $r, s, t$ es precisamente $q(x)$, y es el único polinomio de grado $\le 2$ que satisface $q(r) = 3r-1$, $q(s) = 3s-1$, $q(t) = 3t-1$.

**Paso 2: Identificar el polinomio.** El polinomio lineal $p(x) = 3x - 1$ también cumple esas tres condiciones. Por la unicidad de la interpolación (dos polinomios de grado $\le 2$ que coinciden en tres puntos distintos son idénticos), se concluye que
$$q(x) = 3x - 1.$$

**Verificación del coeficiente cuadrático:** el coeficiente de $x^2$ en $q(x)$ es
$$\frac{3r-1}{(r-s)(r-t)} + \frac{3s-1}{(s-r)(s-t)} + \frac{3t-1}{(t-r)(t-s)},$$
que al poner denominador común $(r-s)(s-t)(t-r)$ da numerador
$$-(3r-1)(s-t) - (3s-1)(t-r) - (3t-1)(r-s) = -3(rs - rt + st - rs + rt - st) + (s-t+t-r+r-s) = 0,$$
confirmando que el término cuadrático se cancela, mientras que el coeficiente de $x$ es $3 \neq 0$.

Por lo tanto, $q(x) = 3x - 1$ y su grado es

$$\boxed{1}$$