**Configuración.** Sea $f(x) = ax^2 + bx + c$, con $|f(x)| \le 1$ en $[0,1]$. Evaluamos en tres puntos:
$$u = f(0) = c, \qquad v = f\!\left(\tfrac12\right) = \tfrac{a}{4} + \tfrac{b}{2} + c, \qquad w = f(1) = a+b+c,$$
con $|u|,|v|,|w| \le 1$.

**Cota superior.** Despejando de ese sistema:
$$a = 2u - 4v + 2w, \qquad b = -3u + 4v - w, \qquad c = u.$$
Entonces, por la desigualdad triangular:
$$|a| \le 2|u| + 4|v| + 2|w| \le 8, \qquad |b| \le 3|u| + 4|v| + |w| \le 8, \qquad |c| \le 1.$$
Sumando: $|a| + |b| + |c| \le 6|u| + 8|v| + 3|w| \le 17$.

**Se alcanza 17.** Tomemos $u = 1$, $v = -1$, $w = 1$:
$$f(x) = 8x^2 - 8x + 1 = 8\left(x - \tfrac12\right)^2 - 1.$$
En $[0,1]$ esto varía entre $-1$ (en $x = \frac12$) y $1$ (en los extremos), así que $|f(x)| \le 1$ se cumple, y
$$|a| + |b| + |c| = 8 + 8 + 1 = 17.$$

$$\boxed{17}$$