## Planteamiento

Los puntos de intersección cumplen simultáneamente $y=g(x)$ y $x=66y^2$. Como el rango de $g$ es $[-1,1]$, toda intersección tiene $y\in[-1,1]$ y por tanto $x=66y^2\in[0,66]$.

**Estructura de $g$ en $[0,66]$.** Por periodicidad, para cada entero $k\ge 0$:

- tramo *ascendente*: $x\in[4k-1,\,4k+1)$ (para $k=0$ solo la parte $[0,1)$), donde $g(x)=x-4k$;
- tramo *descendente*: $x\in[4k+1,\,4k+3)$, donde $g(x)=4k+2-x$.

(con $g(4k-1)=-1$, $g(4k+1)=1$).

## Tramos ascendentes

De $y=x-4k=66y^2-4k$ sale $66y^2-y-4k=0$, con raíces $y=\dfrac{1\pm\sqrt{1+1056k}}{132}$. La solución es válida si $y\in[-1,1)$ (y $y\in[0,1)$ si $k=0$):

- $k=0$: raíces $0$ y $\tfrac1{66}$, ambas válidas;
- $1\le k\le 16$: $y_+<1\iff\sqrt{1+1056k}<131\iff k\le 16$, y $y_-\ge-1\iff\sqrt{1+1056k}\le 133\iff k\le 16$: **ambas válidas**;
- $k\ge 17$: $y_+>1$ y $y_-<-1$: ninguna válida.

Cada uno de los $17$ tramos da $2$ puntos (34 en total), y cada pareja de raíces suma $\tfrac{1}{66}$ (vieta), luego aportan $\tfrac{17}{66}$.

## Tramos descendentes

De $y=4k+2-x=4k+2-66y^2$ sale $66y^2+y-(4k+2)=0$, con raíces $y=\dfrac{-1\pm\sqrt{1056k+529}}{132}$, válidas si $y\in(-1,1]$:

- $y_+\le 1\iff\sqrt{1056k+529}\le 133\iff k\le 16$: válida para $k=0,\dots,16$ (17 raíces);
- $y_->-1\iff\sqrt{1056k+529}<131\iff k\le 15$: válida para $k=0,\dots,15$ (16 raíces).

Las $16$ parejas completas ($k\le 15$) suman $-\tfrac{16}{66}$; queda suelta la raíz del tramo $k=16$:
$$y_+=\frac{-1+\sqrt{1056\cdot16+529}}{132}=\frac{-1+\sqrt{17425}}{132}=\frac{-1+5\sqrt{697}}{132},\qquad 17425=25\cdot 697.$$

## Suma total

Hay $34+33=67$ puntos, y los radicales se cancelan por telescopio (solo sobreviven $\sqrt{1+1056\cdot0}=1$ y $\sqrt{17425}$):
$$S=\frac{17}{66}-\frac{16}{66}+\frac{-1+5\sqrt{697}}{132}=\frac{2}{132}+\frac{-1+5\sqrt{697}}{132}=\frac{1+5\sqrt{697}}{132}\approx 1{.}0076.$$

Así $a=1$, $b=5$, $c=697=17\cdot 41$ (libre de cuadrados), $d=132$, con $\gcd(1,5,132)=1$.

$$a+b+c+d=1+5+697+132=\boxed{835}$$