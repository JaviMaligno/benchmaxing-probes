## Planteamiento

El tercer término se puede completar cuadrados:

$$x^2 + y^2 - 80x - 100y + 4100 = (x-40)^2 + (y-50)^2,$$

ya que $(x-40)^2 + (y-50)^2 = x^2 - 80x + 1600 + y^2 - 100y + 2500$, y $1600 + 2500 = 4100$. ✓

Entonces la expresión es

$$\sqrt{x^2 + 20^2} + \sqrt{30^2 + y^2} + \sqrt{(40-x)^2 + (50-y)^2}.$$

## Desigualdad de Minkowski (triangular con vectores)

Interpretamos cada término como la norma de un vector, eligiendo las componentes convenientemente:

- $\vec{u} = (x,\, 20)$
- $\vec{v} = (30,\, y)$  (nótese que $\sqrt{30^2 + y^2} = \sqrt{y^2 + 900}$)
- $\vec{w} = (40-x,\, 50-y)$

La suma de los tres vectores es constante:

$$\vec{u} + \vec{v} + \vec{w} = (x + 30 + 40 - x,\; 20 + y + 50 - y) = (70,\, 70).$$

Por la desigualdad triangular,

$$|\vec{u}| + |\vec{v}| + |\vec{w}| \ge |\vec{u}+\vec{v}+\vec{w}| = \sqrt{70^2 + 70^2} = 70\sqrt{2}.$$

## Verificación de la igualdad

La igualdad requiere que los tres vectores sean paralelos a $(1,1)$:

- $(x, 20) \parallel (1,1) \Rightarrow x = 20$ (dentro de $[0,40]$ ✓)
- $(30, y) \parallel (1,1) \Rightarrow y = 30$ (dentro de $[0,50]$ ✓)
- $(40-20,\, 50-30) = (20, 20) \parallel (1,1)$ ✓

Comprobación directa en $(x,y) = (20,30)$:

$$\sqrt{400+400} + \sqrt{900+900} + \sqrt{400+400} = 20\sqrt{2} + 30\sqrt{2} + 20\sqrt{2} = 70\sqrt{2}.$$

$$\boxed{70\sqrt{2}}$$