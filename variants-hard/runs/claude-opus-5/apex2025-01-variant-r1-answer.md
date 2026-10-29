## Planteamiento

**Teorema de la cuerda horizontal.** Si una función continua $g$ tiene una cuerda horizontal de longitud $\ell$, entonces tiene cuerdas horizontales de longitud $\ell/n$ para todo entero $n\ge 1$.

*Idea de la demostración:* si $g(a)=g(a+\ell)$, se define $h(x)=g(x+\ell/n)-g(x)$. Entonces
$$\sum_{k=0}^{n-1} h\!\left(a+\tfrac{k\ell}{n}\right)=g(a+\ell)-g(a)=0,$$
así que los $n$ valores no pueden ser todos del mismo signo: o alguno es cero, o hay dos de signos opuestos y el teorema del valor intermedio da un punto con $h(x_0)=0$, es decir, una cuerda de longitud $\ell/n$.

Además, este resultado es óptimo: para cualquier $\ell'$ que **no** sea de la forma $\ell/n$ existe una función continua con cuerda de longitud $\ell$ y sin ninguna cuerda de longitud $\ell'$ (el ejemplo clásico es $g(x)=\sin^2\!\big(\pi x/\ell\big)-x\,\sin^2(\pi \ell'/\ell)\cdot\frac{1}{\ell'}$, tipo "seno inclinado").

## Aplicación

Como existe una cuerda de longitud $2030$, están forzadas las cuerdas de longitud $2030/n$. De ellas, las de **longitud entera** son exactamente aquellas con $n \mid 2030$:
$$2030 = 2\cdot 5\cdot 7\cdot 29 .$$

El número de divisores es
$$d(2030)=2\cdot2\cdot2\cdot2=16.$$

Por tanto hay al menos $16$ longitudes enteras obligatorias: $1,2,5,7,10,14,29,35,58,70,145,203,290,406,1015,2030$.

Ninguna otra longitud entera está forzada (por la parte de optimalidad del teorema), y el ejemplo del seno inclinado con $\ell=2030$ puede ajustarse para que cada una de esas longitudes se realice por una única cuerda. Así el mínimo se alcanza.

$$\boxed{16}$$