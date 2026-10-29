## Planteamiento

Completando cuadrados en el tercer radical:

$$x^2+y^2-80x-100y+4100=(x-40)^2+(y-50)^2$$

Así, la expresión es

$$\sqrt{x^2+20^2}+\sqrt{y^2+30^2}+\sqrt{(40-x)^2+(50-y)^2}.$$

## Interpretación vectorial

Cada término es la norma de un vector:

$$\vec{u}=(20,\;x),\qquad \vec{v}=(y,\;30),\qquad \vec{w}=(40-x,\;50-y).$$

Su suma es

$$\vec{u}+\vec{v}+\vec{w}=(60+y-x,\;80+x-y).$$

Con $t=x-y$, por la desigualdad triangular:

$$\|\vec u\|+\|\vec v\|+\|\vec w\|\;\ge\;\|\vec u+\vec v+\vec w\|=\sqrt{(60-t)^2+(80+t)^2}.$$

Minimizando el lado derecho: $-(60-t)+(80+t)=0\Rightarrow t=-10$, lo que da $\sqrt{70^2+70^2}=70\sqrt{2}$.

Por tanto la expresión es siempre $\ge 70\sqrt{2}$.

## Igualdad

La igualdad requiere que los tres vectores sean paralelos y, con $t=-10$, paralelos a $(1,1)$:

- $(20,x)\parallel(1,1)\Rightarrow x=20$
- $(y,30)\parallel(1,1)\Rightarrow y=30$
- $(40-20,\,50-30)=(20,20)\parallel(1,1)$ ✓

Además $x-y=-10=t$ ✓, y ambos valores están en el rango permitido ($0\le 20\le 40$, $0\le 30\le 50$).

Verificación: $20\sqrt2+30\sqrt2+20\sqrt2=70\sqrt2\approx 98.995$.

\boxed{70\sqrt{2}}