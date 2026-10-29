## Planteamiento

**Ubicación de las ocho esferas.**
Cada esfera de radio $1$ dentro del cubo de lado $4$ debe tener su centro a distancia $\ge 1$ de cada cara, es decir, los centros viven en un cubo concéntrico de lado $4-2=2$.

Para que cada esfera sea tangente exteriormente a exactamente tres otras, la configuración natural es poner los centros en los vértices de un cubo de lado $s$, donde cada centro tiene tres vecinos por arista. La tangencia exige $s = 1+1 = 2$, que es justamente el máximo permitido: los centros son los vértices del cubo de lado $2$ concéntrico con el original.

Tomando el centro del cubo como origen, los centros son
$$(\pm 1, \pm 1, \pm 1).$$

**Esfera interior.**
La distancia del origen a cada centro es
$$d = \sqrt{1^2+1^2+1^2} = \sqrt{3}.$$

Una esfera centrada en el origen de radio $r$ es tangente exteriormente a cada una de las ocho si
$$r + 1 = \sqrt{3} \quad\Longrightarrow\quad r = \sqrt{3}-1 \approx 0{,}732.$$

**Verificación de que cabe en el cubo.**
La distancia del origen a cada cara es $2$, y $\sqrt{3}-1 < 2$, así que la esfera está contenida en el cubo. Además no puede ser mayor: cualquier esfera tangente exteriormente a las ocho simultáneamente queda atrapada en el hueco central, y el radio está determinado por $r=\sqrt3-1$.

$$\boxed{\sqrt{3}-1}$$