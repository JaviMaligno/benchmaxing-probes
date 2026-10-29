## Planteamiento

El desarrollo (red) en forma de paralelogramo de un tetraedro regular es una tira de 4 triángulos equiláteros: un paralelogramo de lados $2a$ y $a$ con ángulo de $60°$ entre ellos, donde $a$ es la arista del tetraedro. Hay que inscribir ese paralelogramo, posiblemente girado, dentro del cuadrado de lado $14$, maximizando $a$.

## Optimización del giro

Si giramos el paralelogramo un ángulo $\theta$ (con $0° \le \theta \le 30°$), sus lados son los vectores $\vec u = 2a(\cos\theta, \sin\theta)$ y $\vec v = a(\cos(\theta+60°), \sin(\theta+60°))$. Su caja envolvente mide:

$$W = 2a\cos\theta + a\cos(\theta+60°), \qquad H = 2a\sin\theta + a\sin(\theta+60°).$$

Observación clave: la suma de cuadrados es constante,

$$W^2 + H^2 = a^2\big[4 + 1 + 4(\cos\theta\cos(\theta+60°) + \sin\theta\sin(\theta+60°)\big] = a^2(5 + 4\cos 60°) = 7a^2.$$

Esto equivale a decir que la diagonal larga del paralelogramo mide $a\sqrt{7}$ (por ley del coseno: $4a^2 + a^2 + 2\cdot 2a\cdot a\cos 60° = 7a^2$), y que $W$, $H$ son sus proyecciones.

Como $W$ decrece y $H$ crece con $\theta$, el máximo entre ambos se minimiza cuando $W = H$, y entonces:

$$W = H = a\sqrt{\tfrac{7}{2}}.$$

En esa posición la diagonal larga queda sobre la diagonal del cuadrado.

## Cálculo de la arista

Imponiendo $W = H = 14$:

$$a\sqrt{\tfrac{7}{2}} = 14 \;\Longrightarrow\; a = 14\sqrt{\tfrac{2}{7}} = 2\sqrt{14}, \qquad a^2 = 56.$$

(Comprobación: la diagonal larga mide $a\sqrt7 = 2\sqrt{98} = 14\sqrt2$, exactamente la diagonal del cuadrado.)

## Área superficial

El tetraedro regular tiene 4 caras equiláteras:

$$S = 4\cdot\frac{\sqrt{3}}{4}a^2 = \sqrt{3}\cdot 56 = 56\sqrt{3}.$$

$$\boxed{56\sqrt{3}}$$