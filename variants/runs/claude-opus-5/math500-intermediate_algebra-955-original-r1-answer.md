## Razonamiento

Sea $f(x) = ax^2+bx+c$. Evaluando en $x=0, \tfrac12, 1$:

$$f(0)=c,\qquad f\!\left(\tfrac12\right)=\frac{a}{4}+\frac{b}{2}+c,\qquad f(1)=a+b+c.$$

Invirtiendo el sistema:

$$a = 2f(0) - 4f\!\left(\tfrac12\right) + 2f(1),\qquad b = -3f(0) + 4f\!\left(\tfrac12\right) - f(1),\qquad c = f(0).$$

**Cota superior.** Como $|f(0)|, |f(\tfrac12)|, |f(1)| \le 1$:

$$|a|+|b|+|c| \le \big(2+4+2\big) + \big(3+4+1\big) + 1 = 8+8+1 = 17.$$

**Se alcanza.** Para lograr la igualdad hacen falta signos consistentes en las tres expresiones; esto ocurre con $f(0)=1$, $f(\tfrac12)=-1$, $f(1)=1$, que da

$$a=8,\quad b=-8,\quad c=1,\qquad f(x)=8x^2-8x+1.$$

Verificación de la restricción: $f(x) = 8\left(x-\tfrac12\right)^2 - 1$, y para $0\le x\le 1$ se tiene $0 \le \left(x-\tfrac12\right)^2 \le \tfrac14$, luego $-1 \le f(x) \le 1$. Es el polinomio de Chebyshev trasladado al intervalo $[0,1]$.

Entonces $|a|+|b|+|c| = 8+8+1 = 17$.

$$\boxed{17}$$