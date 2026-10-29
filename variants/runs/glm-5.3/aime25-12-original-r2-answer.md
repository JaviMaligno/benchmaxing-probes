## Desarrollo

**Paso 1: Factorizar las desigualdades.**

De $x-yz<y-zx$:
$$x-yz-y+zx=(x-y)(z+1)<0.$$

De $y-zx<z-xy$:
$$y-zx-z+xy=(y-z)(x+1)<0.$$

**Paso 2: Análisis por casos según los signos de $(x+1)$ y $(z+1)$.**

- **Caso $x>-1,\ z>-1$:** obliga a $x<y<z$ (con $z>y>x>-1$). Región: $-1<x<y<z$, $x+y+z=75$: es un triángulo **acotado**.
- **Caso $x<-1,\ z<-1$:** obliga a $z<y<x<-1$, así que $x+y+z<-3\neq 75$: región **vacía**.
- **Caso $x>-1,\ z<-1$:** obliga a $y<x$ e $y<z$: región convexa **no acotada** (p. ej. $z=-2$, $y\to-\infty$).
- **Caso $x<-1,\ z>-1$:** obliga a $y>x$ e $y>z$: región convexa **no acotada**.

En total son **tres regiones convexas disjuntas** y solo la primera tiene área finita, como afirma el problema.

**Paso 3: Vértices del triángulo finito.**

La región es el triángulo abierto en el plano $x+y+z=75$ delimitado por $x=-1$, $y=x$, $y=z$:

$$A=(-1,-1,77),\qquad B=(25,25,25),\qquad C=(-1,38,38).$$

(Verificación: las sumas dan $75$ en los tres casos.)

**Paso 4: Calcular el área.**

Con $\vec{u}=B-A=(26,26,-52)$ y $\vec{v}=C-A=(0,39,-39)$:
$$\vec{u}\times\vec{v}=(1014,\,1014,\,1014),\qquad |\vec{u}\times\vec{v}|=1014\sqrt3.$$
$$\text{Área}=\tfrac12\cdot 1014\sqrt3=507\sqrt3.$$

**Comprobación (proyección):** proyectando sobre el plano $xy$, el triángulo $(-1,-1),(25,25),(-1,38)$ tiene área $507$ por la fórmula del cordón; como el plano $x+y+z=75$ forma con el plano $xy$ un ángulo con $\cos\theta=1/\sqrt3$, el área se multiplica por $\sqrt3$: de nuevo $507\sqrt3$. (También coincide vía Heron: es un triángulo rectángulo en $C$ con catetos $39\sqrt2$ y $\sqrt{1014}=13\sqrt{6}$... de hecho $\sqrt{1014}$, dando $\frac12\cdot 39\sqrt2\cdot\sqrt{1014}=507\sqrt3$.)

**Paso 5: Conclusión.**

El área es $507\sqrt3$, es decir, $a=507$, $b=3$ (libre de cuadrados), y por lo tanto
$$a+b=507+3=510.$$

$$\boxed{510}$$