## Planteamiento

Sea $f(x)=\dfrac{p(x)}{q(x)}$ con $p,q$ cuadráticos. De $f(n)=n^3$ para $n=1,\dots,5$:

$$p(n)-n^3q(n)=0,\qquad n=1,2,3,4,5.$$

El polinomio $p(x)-x^3q(x)$ tiene grado $\le 5$ y cinco raíces conocidas, así que

$$p(x)-x^3q(x)=k(x-1)(x-2)(x-3)(x-4)(x-5).$$

## Determinación de los coeficientes

Con $q(x)=ax^2+bx+c$ y la expansión
$$(x-1)\cdots(x-5)=x^5-15x^4+85x^3-225x^2+274x-120,$$

se tiene
$$p(x)=ax^5+bx^4+cx^3+k\left(x^5-15x^4+85x^3-225x^2+274x-120\right).$$

Como $p$ es cuadrático, los coeficientes de $x^5,x^4,x^3$ deben anularse:

- $x^5:\ a+k=0\Rightarrow a=-k$
- $x^4:\ b-15k=0\Rightarrow b=15k$
- $x^3:\ c+85k=0\Rightarrow c=-85k$

Queda $p(x)=k(-225x^2+274x-120)$ y $q(x)=k(-x^2+15x-85)$.

## Evaluación

$$f(0)=\frac{p(0)}{q(0)}=\frac{-120k}{-85k}=\frac{120}{85}=\frac{24}{17}.$$

$$\boxed{\dfrac{24}{17}}$$