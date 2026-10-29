## Resolución

**Paso 1: Escribir Q como suma de dos cuadrados.**

Intento la forma $Q(x) = (x^2+12x+t)^2 + (\text{lineal})^2$. Expandiendo con $t=-40$:

$$(x^2+12x-40)^2 = x^4 + 24x^3 + 64x^2 - 960x + 1600$$

y sumando $(x+30)^2 = x^2 + 60x + 900$ se obtiene exactamente:

$$Q(x) = (x^2+12x-40)^2 + (x+30)^2$$

Esto además confirma que $Q(x)>0$ para todo $x$ real (los dos cuadrados no se anulan simultáneamente).

**Paso 2: Resolver $Q(z)=0$.**

$$(z^2+12z-40)^2 = -(z+30)^2 \quad\Longrightarrow\quad z^2+12z-40 = \pm i(z+30)$$

Tomando el signo $+$:

$$z^2 + (12-i)z - (40+30i) = 0$$

Por la fórmula cuadrática:

$$z = \frac{-(12-i) \pm \sqrt{(12-i)^2 + 4(40+30i)}}{2} = \frac{-12+i \pm \sqrt{144 - 24i - 1 + 160 + 120i}}{2} = \frac{-12 + i \pm \sqrt{303+96i}}{2}$$

**Paso 3: Elegir la raíz del primer cuadrante.**

Como $|303+96i| = \sqrt{303^2+96^2} = \sqrt{101025} \approx 317.8$, la raíz cuadrada principal es aproximadamente $17.6 + 2.73i$. Con el signo $+$:

$$z \approx \frac{-12 + 17.6}{2} + \frac{1+2.73}{2}i \approx 2.8 + 1.87i$$

que efectivamente está en el primer cuadrante (las otras ramas dan raíces en el tercer y cuarto cuadrante).

Por lo tanto:

$$z = \frac{1}{2}\left(-12 + i + \sqrt{303 + 96i}\right)$$

con $a = -12$, $b = 1$, $c = 303$, $d = 96$, y:

$$a+b+c+d = -12 + 1 + 303 + 96 = 388$$

$$\boxed{388}$$