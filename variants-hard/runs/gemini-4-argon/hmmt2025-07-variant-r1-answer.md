Para resolver el problema paso a paso, podemos aprovechar una sustitución trigonométrica o un enfoque algebraico directo. A continuación, presentamos ambos métodos para mayor claridad.

### Paso 1: Planteamiento algebraico
Sea $k$ el valor común de las tres expresiones dadas:
$$3(x^2+1) = 4(y^2+1) = 5(z^2+1) = k$$

De aquí podemos despejar $x^2+1$, $y^2+1$ y $z^2+1$:
$$x^2 + 1 = \frac{k}{3}, \quad y^2 + 1 = \frac{k}{4}, \quad z^2 + 1 = \frac{k}{5}$$

### Paso 2: Uso de la condición $xy + yz + zx = 1$
Observamos que si $xy + yz + zx = 1$, podemos factorizar $x^2 + 1$ de la siguiente manera:
$$x^2 + 1 = x^2 + xy + yz + zx = x(x+y) + z(x+y) = (x+y)(x+z)$$

De forma análoga, para $y^2+1$ y $z^2+1$ obtenemos:
$$y^2 + 1 = (y+x)(y+z)$$
$$z^2 + 1 = (z+x)(z+y)$$

Sustituyendo estas factorizaciones en las ecuaciones del Paso 1, tenemos el sistema:
1. $(x+y)(x+z) = \frac{k}{3}$
2. $(x+y)(y+z) = \frac{k}{4}$
3. $(x+z)(y+z) = \frac{k}{5}$

### Paso 3: Proporciones entre las sumas por pares
Multiplicando las tres ecuaciones anteriores miembro a miembro:
$$[(x+y)(y+z)(x+z)]^2 = \frac{k^3}{60}$$
Como $x, y, z > 0$, tomamos la raíz cuadrada positiva:
$$(x+y)(y+z)(x+z) = \frac{k\sqrt{k}}{\sqrt{60}}$$

Dividiendo esta expresión por cada una de las ecuaciones (1), (2) y (3), hallamos las razones entre $y+z$, $x+z$ y $x+y$:
- Al dividir (1) entre (2): $\frac{x+z}{y+z} = \frac{4}{3}$
- Al dividir (2) entre (3): $\frac{x+y}{x+z} = \frac{5}{4}$

Por lo tanto, existe una constante positiva $t$ tal que:
$$y + z = 3t$$
$$x + z = 4t$$
$$x + y = 5t$$

### Paso 4: Cálculo de $x, y, z$ en función de $t$
Sumando las tres ecuaciones anteriores:
$$2(x + y + z) = 12t \implies x + y + z = 6t$$

Restando cada suma por pares de $x + y + z = 6t$, obtenemos:
- $x = (x+y+z) - (y+z) = 6t - 3t = 3t$
- $y = (x+y+z) - (x+z) = 6t - 4t = 2t$
- $z = (x+y+z) - (x+y) = 6t - 5t = t$

### Paso 5: Determinación de $t$ y resultado final
Sustituimos $x = 3t$, $y = 2t$ y $z = t$ en la condición $xy + yz + zx = 1$:
$$(3t)(2t) + (2t)(t) + (t)(3t) = 1$$
$$6t^2 + 2t^2 + 3t^2 = 1$$
$$11t^2 = 1 \implies t = \frac{1}{\sqrt{11}} = \frac{\sqrt{11}}{11} \quad (\text{ya que } t > 0)$$

Finalmente, calculamos la suma pedida:
$$x + y + z = 6t = \frac{6}{\sqrt{11}} = \frac{6\sqrt{11}}{11}$$

\boxed{\frac{6\sqrt{11}}{11}}