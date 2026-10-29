## Planteamiento

Sustituyo $y = x-1$, de modo que $y \in [-1,1]$:
$$g(y) = p(y+1)^2 + q(y+1) + r = ay^2 + by + c,$$
con $a=p$, $b=2p+q$, $c=p+q+r$, y $|g(y)|\le 1$ en $[-1,1]$.

## Expresar los coeficientes por valores puntuales

Sean $u=g(-1)$, $v=g(0)$, $w=g(1)$, todos en $[-1,1]$. Entonces
$$a=\frac{u+w}{2}-v,\qquad b=\frac{w-u}{2},\qquad c=v.$$

Despejando los coeficientes originales:
$$p=a=\frac{u+w}{2}-v,\qquad q=b-2a=-\frac{3u}{2}-\frac{w}{2}+2v,\qquad r=a-b+c=u.$$

## Cota superior

Aplicando desigualdad triangular con $|u|,|v|,|w|\le 1$:
$$|p|\le \tfrac12+\tfrac12+1=2,\qquad |q|\le \tfrac32+\tfrac12+2=4,\qquad |r|\le 1,$$
luego $|p|+|q|+|r|\le 7$.

## La cota se alcanza

Tomando $u=1$, $v=-1$, $w=1$ se cumple la igualdad en las tres desigualdades a la vez: $g(y)=2y^2-1$, que efectivamente satisface $|g(y)|\le 1$ en $[-1,1]$ (es el polinomio de Chebyshev $T_2$). Deshaciendo el cambio:
$$f(x)=2(x-1)^2-1=2x^2-4x+1,$$
con $|f(x)|\le 1$ en $[0,2]$, y
$$|p|+|q|+|r|=2+4+1=7.$$

\boxed{7}