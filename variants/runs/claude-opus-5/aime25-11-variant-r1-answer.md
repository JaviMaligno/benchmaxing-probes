## Planteamiento

Como $|g(x)|\le 1$, toda intersección tiene $y\in[-1,1]$ y $x=66y^2\in[0,66]$. Hay que resolver $y=g(66y^2)$.

Escribiendo $x=4k+t$:

- **Rama A** ($t\in[-1,1)$): $g=t=y$, luego $66y^2=4k+y$, es decir $66y^2-y-4k=0$, con la única condición $y\in[-1,1)$.
- **Rama B** ($t\in[1,3)$): $g=2-t=y$ con $y\in(-1,1]$, luego $66y^2=4k+2-y$, es decir $66y^2+y-(4k+2)=0$.

## Rama A

Raíces: $y=\dfrac{1\pm\sqrt{1+1056k}}{132}$, y $k\ge 0$ porque $x\ge 0$.

- $y<1 \iff 1+1056k<17161 \iff k\le 16$.
- $y\ge -1 \iff 1+1056k\le 17689 \iff k\le 16$.

Así que para $k=0,1,\dots,16$ ambas raíces son válidas (en $k=0$ son $0$ y $1/66$). Cada par suma $\tfrac{1}{66}$, de modo que la suma de la rama A es
$$17\cdot\frac{1}{66}=\frac{17}{66}.$$

## Rama B

Raíces: $y=\dfrac{-1\pm\sqrt{1056k+529}}{132}$, con $k\ge0$.

- Raíz positiva: $y\le 1\iff 1056k+529\le 17689\iff k\le 16$.
- Raíz negativa: $y>-1\iff 1056k+529<17161\iff k\le 15$.

Para $k=0,\dots,15$ ambas raíces valen y cada par suma $-\tfrac1{66}$; para $k=16$ solo sobrevive la raíz positiva:
$$y=\frac{-1+\sqrt{17425}}{132}=\frac{-1+5\sqrt{697}}{132},$$
ya que $17425=25\cdot 697$ y $697=17\cdot 41$ es libre de cuadrados.

Suma de la rama B: $-\dfrac{16}{66}+\dfrac{-1+5\sqrt{697}}{132}$.

## Total

$$\frac{17}{66}-\frac{16}{66}+\frac{-1+5\sqrt{697}}{132}=\frac{2}{132}+\frac{-1+5\sqrt{697}}{132}=\frac{1+5\sqrt{697}}{132}.$$

Con $a=1$, $b=5$, $c=697$, $d=132$ (y $\gcd(1,5,132)=1$):
$$a+b+c+d=1+5+697+132=835.$$

\boxed{835}