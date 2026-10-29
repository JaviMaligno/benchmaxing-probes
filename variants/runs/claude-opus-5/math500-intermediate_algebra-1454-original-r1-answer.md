## Reescritura del tercer radical

Completando cuadrados:

$$x^2+y^2-80x-100y+4100=(x-40)^2+(y-50)^2$$

ya que $(x-40)^2+(y-50)^2 = x^2+y^2-80x-100y+1600+2500$, y $4100=1600+2500$.

La expresión es entonces:

$$\sqrt{x^2+20^2}+\sqrt{y^2+30^2}+\sqrt{(40-x)^2+(50-y)^2}$$

## Interpretación vectorial

Tomamos los vectores

$$\mathbf{u}=(20,\;x),\qquad \mathbf{v}=(y,\;30),\qquad \mathbf{w}=(40-x,\;50-y)$$

cuyas normas son exactamente los tres sumandos. Su suma es

$$\mathbf{u}+\mathbf{v}+\mathbf{w}=(60+y-x,\;80+x-y)$$

Con $t=x-y$, por la desigualdad triangular:

$$\|\mathbf{u}\|+\|\mathbf{v}\|+\|\mathbf{w}\|\ \ge\ \sqrt{(60-t)^2+(80+t)^2}$$

Minimizando el lado derecho en $t$: $-(60-t)+(80+t)=0\Rightarrow t=-10$, lo que da $\sqrt{70^2+70^2}=70\sqrt{2}$.

## Verificación de la igualdad

La igualdad requiere que los tres vectores sean paralelos (misma dirección, pendiente $1$ según la suma $(70,70)$). Eso se cumple con $x=20$, $y=30$:

$$\mathbf{u}=(20,20),\quad \mathbf{v}=(30,30),\quad \mathbf{w}=(20,20)$$

y ambos valores están en los rangos permitidos ($0\le 20\le 40$, $0\le 30\le 50$). Evaluando:

$$\sqrt{800}+\sqrt{1800}+\sqrt{800}=20\sqrt2+30\sqrt2+20\sqrt2=70\sqrt2\approx 98.995$$

El mínimo se alcanza y vale:

\boxed{70\sqrt{2}}