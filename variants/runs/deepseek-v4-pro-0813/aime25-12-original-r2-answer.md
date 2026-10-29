Voy a resolver el problema paso a paso.

El conjunto de puntos en el plano $x+y+z=75$ con $x-yz<y-zx<z-xy$. Esto forma tres regiones convexas disjuntas, exactamente una con área finita. Necesito calcularla.

**Paso 1: Reescribir las desigualdades**

Las desigualdades son:
$$x-yz<y-zx$$

Sumando $x+y+z$ a ambos lados:
$$2x+y+z-yz < x+2y+z-zx$$

Usando $x+y+z=75$, podemos simplificar. Notemos que:
$$x-yz = x - y(75-x-y)$$

Pero quizás sea más útil reescribir como sigue. La condición $x-yz<y-zx$ equivale a:
$$x-yz-y+zx<0$$
$$x-y+zx-yz<0$$
$$(x-y)+z(x-y)<0$$
$$(x-y)(1+z)<0$$

Como $1+z$ puede ser positivo o negativo, esto depende del signo de $z+1$.

Similarmente, $y-zx<z-xy$:
$$y-zx-z+xy<0$$
$$y-z+xy-zx<0$$
$$(y-z)+x(y-z)<0$$
$$(y-z)(1+x)<0$$

**Paso 2: Analizar los casos según los signos**

Necesitamos $x-yz<y-zx<z-xy$, es decir dos desigualdades:
1. $(x-y)(1+z)<0$
2. $(y-z)(1+x)<0$

Caso A: $1+z>0$ y $1+x>0$ (es decir, $z>-1$, $x>-1$).
  Entonces $x-y<0$ y $y-z<0$, o sea $x<y<z$.

Caso B: $1+z>0$ y $1+x<0$ ($z>-1$, $x<-1$).
  Entonces $x-y<0$ y $y-z>0$, o sea $x<y$ y $y>z$. Así que $z<y$ y $x<y$.

Caso C: $1+z<0$ y $1+x>0$ ($z<-1$, $x>-1$).
  Entonces $x-y>0$ y $y-z<0$, o sea $x>y$ y $y<z$. Así que $y<x$ y $y<z$.

Caso D: $1+z<0$ y $1+x<0$ ($z<-1$, $x<-1$).
  Entonces $x-y>0$ y $y-z>0$, o sea $x>y>z$.

**Paso 3: Determinar las regiones y su área**

Con $x+y+z=75$, el plano es simplemente un plano 2D. Las desigualdades $x>-1$, $z>-1$ son semiespacios en este plano, dando líneas. Las ordenaciones $x<y<z$ etc. también dan líneas.

Las cuatro regiones:
- Región 1: $x<y<z$, $x>-1$, $z>-1$.
- Región 2: $x<y$, $z<y$, $x>-1$, $z<-1$.
- Región 3: $y<x$, $y<z$, $x<-1$, $z>-1$.
- Región 4: $x>y>z$, $x<-1$, $z<-1$.

El problema dice que hay tres regiones, una con área finita. Veamos: las regiones limitadas por semiespacios en un plano pueden ser infinitas o finitas dependiendo de si las líneas de frontera forman un triángulo o no.

La región de área finita debe ser la determinada por un triángulo. Consideremos la región 1: $x<y<z$ en el plano $x+y+z=75$ con $x>-1$, $z>-1$.

Parametricemos el plano $x+y+z=75$. Pongamos $y = 75 - x - z$. Las condiciones:
- $x<y$: $x < 75-x-z$, o sea $2x + z < 75$.
- $y<z$: $75-x-z < z$, o sea $75 - x < 2z$, o sea $x + 2z > 75$.
- $x>-1$, $z>-1$.

En el plano $(x,z)$, las rectas son $2x+z=75$ y $x+2z=75$. Se intersecan en $x=z=25$. La región con $2x+z<75$ y $x+2z>75$, $x>-1$, $z>-1$.

La región 1 es un triángulo no acotado: con $x>-1$ y las rectas $2x+z=75$ y $x+2z=75$. Veamos el triángulo: las rectas se cruzan en $(25,25)$, y con $x=-1$: la recta $2(-1)+z=75$ da $z=77$; la recta $-1+2z=75$ da $z=38$. La región entre estas dos líneas para $x\in[-1,25]$ es acotada por $x=-1$ a la izquierda. Pero para $z>-1$, y $x>25$... no, las ordenaciones $x<y<z$ imponen que no podemos ir más allá del cruce. Así que la región 1 es un triángulo finito: vértices $(25,25)$ en coordenadas $(x,z)$, correspondiente a $(x,y,z)=(25,25,25)$; y $(x,z)=(-1,77)$ correspondiente a $(-1,-1,77)$; y $(x,z)=(-1,38)$ correspondiente a $(-1,38,38)$.

Espera, revisemos $(-1,77)$: $x=-1$, $z=77$, $y=75-(-1)-77=-1$. Entonces $x=y=-1<z=77$, así que $x<y$ falla (es igualdad). Hmm, necesitamos $x<y$ estricta, así que $x>-1$ estrictamente, y el punto límite $(-1,-1,77)$ está en la frontera. Similarmente $(-1,38,38)$ con $y=z=38$, en la frontera $y<z$ (igualdad). La región es un triángulo abierto (fronteras excluidas) pero su área es la del triángulo cerrado, finita.

**Paso 4: Calcular el área**

Vértices en coordenadas $(x,z)$:
- $A = (25,25)$
- $B = (-1,77)$
- $C = (-1,38)$

Área en coordenadas $(x,z)$: base vertical en $x=-1$ desde $z=38$ a $z=77$, longitud $77-38=39$. La distancia horizontal desde $x=-1$ hasta $x=25$ es $26$. Pero como las rectas no son perpendiculares, necesitamos el área real en el plano 3D. Sin embargo, podemos usar la fórmula del área en el plano paramétrico $(x,z)$ multiplicada por el factor de escala.

El plano $x+y+z=75$ con coordenadas $(x,z)$: la parametrización es $r(x,z)=(x, 75-x-z, z)$. El factor de escala (Jacobiano) es la norma del producto cruz de las derivadas parciales: $\partial r/\partial x = (1,-1,0)$, $\partial r/\partial z = (0,-1,1)$. Producto cruz: $(1,-1,0)\times(0,-1,1) = (-1\cdot1 - 0\cdot(-1), 0\cdot0 - 1\cdot1, 1\cdot(-1) - (-1)\cdot0) = (-1, -1, -1)$. Norma: $\sqrt{3}$.

Entonces el área 3D = área en $(x,z)$-plano × $\sqrt{3}$.

El triángulo en $(x,z)$ tiene base $39$ (vertical) y altura $26$ (horizontal, distancia de $(25,25)$ a la línea $x=-1$). Área = $\frac12 \cdot 39 \cdot 26 = 507$.

Área 3D = $507\sqrt{3}$.

**Paso 5: Verificar $a$ y $b$**

$a=507$, $b=3$. $b=3$ no es divisible por un cuadrado de primo. $a+b=510$.

Espera, pero debo verificar que las otras dos regiones son infinitas y que esta es la única finita. Rápidamente:

- Región 2: $x<y$, $z<y$, $x>-1$, $z<-1$. En plano $(x,z)$: $y=75-x-z$. Condiciones: $x<75-x-z \Rightarrow 2x+z<75$; $z<75-x-z \Rightarrow x+2z<75$; $x>-1$, $z<-1$. Esta región está en $z<-1$ (semiplano inferior), $x>-1$ (semiplano derecho), limitada por dos rectas. La recta $2x+z=75$ y $x+2z=75$ se cruzan en $(25,25)$, que está muy arriba a la derecha. Para $z<-1$, las rectas están lejos. La región $2x+z<75$ y $x+2z<75$ con $x>-1$, $z<-1$: para $x$ grande y $z<-1$, ambas desigualdades se satisfacen (ya que $2x+z<75$ requiere $x$ moderado... hmm, para $x$ grande, $2x+z>75$ viola). En realidad, las dos rectas juntas acotan la región en dirección $x\to\infty$. Veamos: si $z<-1$ y $x$ crece, $2x+z$ crece, eventualmente supera 75. Entonces la región 2 está acotada en $x$ por la recta $2x+z=75$. Pero en dirección $z\to-\infty$, ambas desigualdades se satisfacen (para $x$ moderado, $2x+z<75$ y $x+2z<75$ son ciertas). Por tanto la región 2 es infinita (se extiende a $z\to-\infty$).

Similarmente, las regiones 3 y 4 son infinitas, pero solo tres de las cuatro regiones existen (la región 4 quizás vacía, o una de las cuatro es vacía). De hecho, el problema dice tres regiones, una finita. La región 1 es la finita.

**Paso 6: Doble chequeo del área**

Área del triángulo en el plano 3D: los vértices son
$$P_1=(25,25,25), \quad P_2=(-1,-1,77), \quad P_3=(-1,38,38).$$

Calculemos directamente. Vectores: $P_2-P_1=(-26,-26,52)$, $P_3-P_1=(-26,13,13)$.

Producto cruz: $(-26,-26,52)\times(-26,13,13)$:
- componente $x$: $(-26)(13)-(52)(13) = -338 - 676 = -1014$
- componente $y$: $52(-26) - (-26)(13) = -1352 + 338 = -1014$
- componente $z$: $(-26)(13) - (-26)(-26) = -338 - 676 = -1014$

Norma: $\sqrt{3\cdot 1014^2} = 1014\sqrt{3}$.

Área = $\frac12 \cdot 1014\sqrt{3} = 507\sqrt{3}$.

Confirmado.

$a=507$, $b=3$, $a+b=507+3=510$.

**Respuesta final:**

$$\boxed{510}$$