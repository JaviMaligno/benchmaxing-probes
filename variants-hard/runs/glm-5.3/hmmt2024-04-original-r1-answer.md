Sea $f(x)=\dfrac{p(x)}{q(x)}$ con $p,q$ cuadráticos. La condición $f(n)=n^3$ equivale a

$$p(n)-n^3 q(n)=0\quad\text{para } n=1,\dots,5.$$

Entonces $g(x)=p(x)-x^3q(x)$ es un polinomio de grado $\le 5$ con raíces $1,2,3,4,5$, así que

$$g(x)=c\,(x-1)(x-2)(x-3)(x-4)(x-5)=c\left(x^5-15x^4+85x^3-225x^2+274x-120\right).$$

Escribamos $q(x)=ax^2+bx+d$. Los términos de grado $5,4,3$ de $g$ provienen de $-x^3q(x)$, pues $p$ es cuadrático:

$$-a=c,\qquad -b=-15c,\qquad -d=85c \;\Longrightarrow\; a=-c,\; b=15c,\; d=-85c.$$

Entonces $q(x)=c(-x^2+15x-85)$ y

$$p(x)=g(x)+x^3q(x)=c\left(-225x^2+274x-120\right).$$

Por tanto

$$f(0)=\frac{p(0)}{q(0)}=\frac{-120c}{-85c}=\frac{24}{17}.$$

**Verificación:** con $c$ absorbido, $q(n)=-n^2+15n-85$ da $-71,-59,-49,-41,-35$ para $n=1,\dots,5$, y $p(n)=-225n^2+274n-120$ da $-71,-472,-1323,-2624,-4375$, que coinciden exactamente con $n^3q(n)$ ($1\cdot(-71),\ 8\cdot(-59),\ 27\cdot(-49),\ 64\cdot(-41),\ 125\cdot(-35)$). ✓

$\boxed{\dfrac{24}{17}}$