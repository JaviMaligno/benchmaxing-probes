Para hallar el área del cuadrado $ABCD$, establezcamos un sistema de coordenadas cartesianas.

Sea $s$ la longitud del lado del cuadrado $ABCD$, de modo que su área es $s^2$. Ubicamos los vértices del cuadrado en:
$$A = (0, 0), \quad B = (s, 0), \quad C = (s, s), \quad D = (0, s)$$

El punto medio $M$ del segmento $\overline{AB}$ tiene coordenadas:
$$M = \left(\frac{s}{2}, 0\right)$$

Sea $\theta$ el ángulo de inclinación de la recta $\ell$. Como $\ell$ pasa por $M\left(\frac{s}{2}, 0\right)$, su ecuación normal se puede escribir como:
$$\left(x - \frac{s}{2}\right)\sin\theta - y\cos\theta = 0$$

Dado que $\ell$ interseca al segmento $\overline{BC}$ (donde $x = s$ y $0 \le y \le s$), al sustituir $x = s$ obtenemos la ordenada del punto de intersección:
$$y = \frac{s}{2}\tan\theta$$
Para que este punto pertenezca al segmento $\overline{BC}$, se debe cumplir que $0 \le \tan\theta \le 2$, por lo que podemos tomar $\theta \in [0, \arctan 2]$, lo cual implica que $\sin\theta \ge 0$ y $\cos\theta > 0$.

La distancia de un punto $(x_0, y_0)$ a la recta $\ell$ está dada por:
$$d((x_0, y_0), \ell) = \left|\left(x_0 - \frac{s}{2}\right)\sin\theta - y_0\cos\theta\right|$$

1. **Distancia desde $A(0,0)$ hasta $\ell$:**
   $$d(A, \ell) = \left|-\frac{s}{2}\sin\theta\right| = \frac{s}{2}\sin\theta = 4 \implies s\sin\theta = 8$$

2. **Distancia desde $C(s,s)$ hasta $\ell$:**
   $$d(C, \ell) = \left|\frac{s}{2}\sin\theta - s\cos\theta\right| = |4 - s\cos\theta| = 7$$
   Como $s > 0$ y $\cos\theta > 0$, el término $s\cos\theta$ es positivo. Si $4 - s\cos\theta = 7$, tendríamos $s\cos\theta = -3$, lo cual es imposible. Por lo tanto:
   $$4 - s\cos\theta = -7 \implies s\cos\theta = 11$$
   (Notemos además que $\tan\theta = \frac{8}{11} \in [0, 2]$, lo que confirma que $\ell$ efectivamente corta al segmento $\overline{BC}$).

Finalmente, usando la identidad pitagórica $\sin^2\theta + \cos^2\theta = 1$, calculamos el área $s^2$ del cuadrado $ABCD$:
$$s^2 = (s\sin\theta)^2 + (s\cos\theta)^2 = 8^2 + 11^2 = 64 + 121 = 185$$

\boxed{185}