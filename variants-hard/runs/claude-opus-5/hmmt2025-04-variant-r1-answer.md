## Planteamiento

Como $k+0.5=\frac{2k+1}{2}$, tenemos
$$\left\lfloor\frac{3150}{k+0.5}\right\rfloor=\left\lfloor\frac{6300}{2k+1}\right\rfloor.$$

Con $n=2k+1$, al recorrer $k=-1200,\dots,1200$ el índice $n$ recorre los **impares** desde $-2399$ hasta $2401$:
$$S=\sum_{\substack{n=-2399\\ n\ \text{impar}}}^{2401}\left\lfloor\frac{6300}{n}\right\rfloor.$$

## Emparejamiento $n$ con $-n$

Los impares negativos $-2399,\dots,-1$ se emparejan exactamente con los positivos $1,\dots,2399$, y sobra únicamente $n=2401$.

Para cada par se usa la identidad $\lfloor x\rfloor+\lfloor -x\rfloor=\begin{cases}0,& x\in\mathbb{Z}\\ -1,&\text{si no}\end{cases}$

Hay $\frac{2399+1}{2}=1200$ impares en $1,\dots,2399$. De ellos, los que dan cociente entero son los divisores impares de $6300=2^2\cdot3^2\cdot5^2\cdot7$, es decir los divisores de $3^2\cdot5^2\cdot7=1575$:
$$1,3,5,7,9,15,21,25,35,45,63,75,105,175,225,315,525,1575$$
que son $3\cdot3\cdot2=18$, y todos cumplen $\le 2399$.

Por tanto la contribución de los pares es
$$-(1200-18)=-1182.$$

## Término sobrante

$$\left\lfloor\frac{6300}{2401}\right\rfloor=2\qquad (2\cdot2401=4802\le 6300<7203).$$

## Resultado

$$S=-1182+2=-1180.$$

\boxed{-1180}