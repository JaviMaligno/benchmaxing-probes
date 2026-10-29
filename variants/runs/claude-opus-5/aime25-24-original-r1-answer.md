## Planteamiento

Buscamos los ceros de $f(x)=\sin(7\pi\sin(5x))$ en $0<x<2\pi$.

$$\sin(7\pi\sin(5x))=0 \iff 7\pi\sin(5x)=k\pi \iff \sin(5x)=\frac{k}{7},\quad k\in\mathbb{Z}$$

Como $|\sin(5x)|\le 1$, se tiene $k=-7,-6,\dots,7$.

## Conteo de $n$

Sea $u=5x$. Si $x\in(0,2\pi)$, entonces $u\in(0,10\pi)$: exactamente 5 periodos completos de la función seno.

- **$k=0$**: $\sin u=0$ da $u=m\pi$ con $m=1,\dots,9$ (se excluyen $u=0$ y $u=10\pi$) → **9 soluciones**.
- **$k=\pm1,\dots,\pm6$** (12 valores): $\sin u=c$ con $0<|c|<1$ tiene 2 soluciones por periodo → $2\cdot 5=10$ cada uno → $12\cdot 10=$ **120 soluciones**.
- **$k=\pm7$**: $\sin u=\pm1$ tiene 1 solución por periodo → $5+5=$ **10 soluciones**.

$$n=9+120+10=139$$

## Conteo de $t$ (tangencias)

La tangencia al eje $x$ requiere $f(x)=0$ y $f'(x)=0$:

$$f'(x)=35\pi\cos(7\pi\sin(5x))\cdot\cos(5x)$$

En un cero, $7\pi\sin(5x)=k\pi$, luego $\cos(7\pi\sin(5x))=\cos(k\pi)=\pm1\neq 0$. Por tanto hace falta $\cos(5x)=0$, es decir $\sin(5x)=\pm1$, lo que corresponde precisamente a $k=\pm7$.

Esos son los 10 puntos contados arriba (y en ellos efectivamente el cero es de orden par, pues $\sin(5x)$ alcanza un extremo):

$$t=10$$

## Resultado

$$n+t=139+10=149$$

\boxed{149}