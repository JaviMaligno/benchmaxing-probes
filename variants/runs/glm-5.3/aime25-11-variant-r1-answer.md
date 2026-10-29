## Planteamiento

Como $|g(x)|\le 1$, todo punto de intersección cumple $x = 66y^2 \le 66$, así que basta analizar $x\in[0,66]$.

**Parametrización del zigzag.** Por periodo, con $k$ entero:
- Segmento creciente: $y = x - 4k$ sobre $x\in[4k-1,\,4k+1)$, es decir $x = 4k + y$ con $y\in[-1,1)$.
- Segmento decreciente: $y = 4k+2-x$ sobre $x\in[4k+1,\,4k+3)$, es decir $x = 4k+2-y$ con $y\in(-1,1]$.

## Intersecciones

**Segmentos crecientes:** $66y^2 = 4k + y$, es decir $66y^2 - y - 4k = 0$, con raíces
$$y=\frac{1\pm\sqrt{1+1056k}}{132}.$$
Debe cumplirse $y\in[-1,1)$:
- $y_+<1 \iff \sqrt{1+1056k}<131 \iff k<16.25 \Rightarrow k\le 16$,
- $y_-\ge -1 \iff \sqrt{1+1056k}\le 133 \iff k\le 16$ (y $k\ge 0$ por el discriminante y por $x\ge 0$).

Para $k=17$ ambas raíces caen fuera de $[-1,1)$. Entonces los segmentos crecientes con $k=0,1,\dots,16$ (17 segmentos) aportan **dos raíces válidas cada uno**. Por Vieta, la suma de las dos raíces de $66y^2-y-4k=0$ es $\frac{1}{66}$.

**Segmentos decrecientes:** $66y^2 = 4k+2-y$, es decir $66y^2+y-(4k+2)=0$, con raíces
$$y=\frac{-1\pm\sqrt{1056k+529}}{132}.$$
Debe cumplirse $y\in(-1,1]$:
- $y_+\le 1 \iff \sqrt{1056k+529}\le 133 \iff k\le 16$,
- $y_-> -1 \iff \sqrt{1056k+529}<131 \iff k\le 15$.

Así, para $k=0,\dots,15$ (16 segmentos) ambas raíces son válidas (suma $=-\frac{1}{66}$ por Vieta), y para $k=16$ solo sobrevive
$$y_+ = \frac{-1+\sqrt{17425}}{132} = \frac{-1+5\sqrt{697}}{132}\approx 0.9924<1,$$
mientras que $y_-\approx -1.008<-1$ se descarta. (Ningún punto cae exactamente en $y=\pm 1$, pues eso exigiría $k$ no entero.)

**Total de puntos:** $17\cdot 2 + 16\cdot 2 + 1 = 67$.

## Suma de las ordenadas

$$S \;=\; 17\cdot\frac{1}{66} \;+\; 16\cdot\left(-\frac{1}{66}\right) \;+\; \frac{-1+5\sqrt{697}}{132} \;=\; \frac{1}{66} + \frac{-1+5\sqrt{697}}{132} \;=\; \frac{1+5\sqrt{697}}{132},$$

donde usé $\sqrt{17425}=\sqrt{25\cdot 697}=5\sqrt{697}$, con $697 = 17\cdot 41$ libre de cuadrados.

Esto da $a=1$, $b=5$, $c=697$, $d=132$, que cumplen $\gcd(a,b,d)=1$. Por lo tanto,
$$a+b+c+d = 1+5+697+132 = 835.$$

\boxed{835}