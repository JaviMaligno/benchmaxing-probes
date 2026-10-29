## Razonamiento

Sea $f(x) = px^2 + qx + r$, con $|f(x)| \le 1$ para todo $x \in [0,2]$.

**Paso 1: Evaluaciones útiles.**
$$f(0) = r, \qquad f(1) = p+q+r, \qquad f(2) = 4p+2q+r,$$
y las tres satisfacen $|f(\cdot)| \le 1$.

**Paso 2: Acotar cada combinación de signos.**
Como $|p|+|q|+|r| = \max_{\varepsilon_i = \pm 1}(\varepsilon_1 p + \varepsilon_2 q + \varepsilon_3 r)$, basta acotar los ocho funcionales $\pm p \pm q \pm r$. Escribiéndolos como combinaciones de $f(0), f(1), f(2)$:

$$p - q + r = 3f(0) - 3f(1) + f(2) \implies |p-q+r| \le 3+3+1 = 7,$$
$$-p+q-r = -3f(0) + 3f(1) - f(2) \implies \le 7,$$
$$p-q-r = f(0) - 3f(1) + f(2) \implies \le 5, \qquad -p+q+r = -f(0)+3f(1)-f(2) \implies \le 5,$$
$$p+q+r = f(1) \implies \le 1, \quad p+q-r = f(1)-2f(0) \implies \le 3, \quad -p-q+r = 2f(0)-f(1) \implies \le 3, \quad -p-q-r = -f(1) \implies \le 1.$$

Las ocho cotas son $\le 7$, luego
$$|p|+|q|+|r| \le 7.$$

(Alternativamente: como $|p|+|q|+|r|$ es convexa, su máximo sobre el conjunto convexo y compacto de los polinomios admisibles se alcanza en un punto extremo; una clasificación de estos muestra el mismo límite.)

**Paso 3: Comprobar que 7 se alcanza.**
Tomemos el polinomio de Chebyshev trasladado:
$$f(x) = 2(x-1)^2 - 1 = 2x^2 - 4x + 1.$$
Para $x \in [0,2]$ tenemos $(x-1)^2 \in [0,1]$, así que $f(x) \in [-1,1]$: es admisible. Sus coeficientes son $p = 2$, $q = -4$, $r = 1$, con lo cual
$$|p|+|q|+|r| = 2 + 4 + 1 = 7,$$
y en este caso $p - q + r = 7$, que satura exactamente la cota del Paso 2.

Por lo tanto, el mayor valor posible es $7$.

$\boxed{7}$