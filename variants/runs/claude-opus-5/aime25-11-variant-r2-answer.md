## Planteamiento

Buscamos los $y$ con $|y|\le 1$ tales que $g(66y^2)=y$, pues $x=66y^2\in[0,66]$.

**Tramos ascendentes** ($x\in[4k-1,4k+1)$, $g(x)=x-4k$):
$$66y^2-y-4k=0,\qquad 66y^2=y+4k$$
La condición $4k-1\le y+4k<4k+1$ equivale a $-1\le y<1$.

Para la raíz positiva: $\frac{1+\sqrt{1+1056k}}{132}<1\iff 1056k<17160\iff k\le 16$.
Para la negativa: $\frac{1-\sqrt{1+1056k}}{132}\ge -1\iff 1056k\le 17688\iff k\le 16$.

Así que para $k=0,1,\dots,16$ ambas raíces sirven (en $k=0$ son $y=0$ y $y=1/66$). Cada cuadrática aporta suma $\tfrac{1}{66}$:
$$S_A=17\cdot\frac{1}{66}=\frac{17}{66}.$$

**Tramos descendentes** ($x\in[4k+1,4k+3)$, $g(x)=4k+2-x$):
$$66y^2+y-(4k+2)=0,\qquad 66y^2=4k+2-y$$
La condición da $-1<y\le 1$, y las raíces son $y=\frac{-1\pm\sqrt{1056k+529}}{132}$.

Raíz positiva: $\sqrt{1056k+529}\le 133\iff 1056k\le 17160\iff k\le 16$.
Raíz negativa: $\sqrt{1056k+529}<131\iff 1056k<16632\iff k\le 15$.

Entonces para $k=0,\dots,15$ hay dos raíces (suma $-\tfrac{1}{66}$ cada par) y para $k=16$ solo la positiva:
$$\frac{-1+\sqrt{1056\cdot16+529}}{132}=\frac{-1+\sqrt{17425}}{132}=\frac{-1+5\sqrt{697}}{132}.$$
(Se verifica: $\approx 0{,}99245\le 1$, con $x\approx 65{,}007\in[65,67)$.)

$$S_B=-\frac{16}{66}+\frac{-1+5\sqrt{697}}{132}=\frac{-33+5\sqrt{697}}{132}.$$

## Suma total

$$S=\frac{17}{66}+\frac{-33+5\sqrt{697}}{132}=\frac{34-33+5\sqrt{697}}{132}=\frac{1+5\sqrt{697}}{132}$$

Con $697=17\cdot 41$ libre de cuadrados y $\gcd(1,5,132)=1$: $a=1$, $b=5$, $c=697$, $d=132$.

$$a+b+c+d=1+5+697+132=835$$

\boxed{835}