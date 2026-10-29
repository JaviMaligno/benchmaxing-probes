## Planteamiento

Sea $f(x) = px^2 + qx + r$. Evaluamos en los tres puntos clave $x = 0, 1, 2$ y llamamos
$$u = f(0) = r,\qquad v = f(1) = p+q+r,\qquad w = f(2) = 4p+2q+r.$$

Resolviendo el sistema:
$$p = \frac{u+w}{2} - v,\qquad q = -\frac{3}{2}u + 2v - \frac{1}{2}w,\qquad r = u.$$

La condición $|f(x)|\le 1$ en $[0,2]$ implica $|u|,|v|,|w|\le 1$, así que

$$|p|+|q|+|r| \;\le\; \left|\frac{u+w}{2}-v\right| + \left|{-\tfrac32}u+2v-\tfrac12 w\right| + |u|.$$

## Cota superior

Acotando término a término con $|u|,|v|,|w|\le 1$:
$$|p| \le \tfrac12+\tfrac12+1 = 2,\qquad |q|\le \tfrac32+2+\tfrac12 = 4,\qquad |r|\le 1,$$
de donde $|p|+|q|+|r| \le 7$.

## La cota se alcanza

Tomemos $u=1,\ v=-1,\ w=1$, es decir el polinomio de Chebyshev trasladado al intervalo $[0,2]$:
$$f(x) = 2x^2 - 4x + 1 = 2(x-1)^2 - 1.$$

En $[0,2]$ se tiene $(x-1)^2 \in [0,1]$, luego $f(x) \in [-1,1]$: la restricción se cumple. Y
$$|p|+|q|+|r| = 2+4+1 = 7.$$

(Coincide con el caso conocido en $[0,1]$, donde $8x^2-8x+1$ da $17$, reescalado mediante $x \mapsto x/2$.)

$\boxed{7}$