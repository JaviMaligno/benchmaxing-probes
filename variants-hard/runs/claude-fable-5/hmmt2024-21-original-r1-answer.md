## Solución

**Configuración con coordenadas.** Coloco el triángulo grande con centro en el origen: vértices $A=(-3,-\sqrt3)$, $B=(3,-\sqrt3)$, $C=(0,2\sqrt3)$ (lado 6, inradio $\sqrt3$). Toda la figura tiene simetría rotacional de $120^\circ$ alrededor del centro $O$; llamo $\omega$ a esa rotación, de modo que $T_2=\omega T_1$ y $T_3=\omega^2 T_1$.

Los tres triángulos pequeños están invertidos (apuntando hacia abajo), lo cual mantiene sus lados paralelos al triángulo grande. Sea $T_1$ con vértices $a$ (superior izquierdo), $b=a+x$ (superior derecho) y $d=a+xe^{-i\pi/3}$ (vértice inferior, apoyado en el lado $AB$).

**Condición del triángulo central.** Los puntos de contacto son: el vértice $b$ de $T_1$ apoyado sobre un lado de $T_2$, y sus imágenes rotadas. El triángulo central tiene vértices $b$, $\omega b$, $\omega^2 b$, que forman un triángulo equilátero centrado en $O$ con lado $\sqrt3\,|b|$. Además, el segmento de $\omega b$ a $b$ debe estar contenido en el lado de $T_2$ que sale de $\omega b$; ese lado tiene dirección $\omega(a-b)\propto e^{-i\pi/3}$. Entonces:

$$b-\omega b = 1\cdot e^{-i\pi/3} \quad\Longrightarrow\quad b=\frac{e^{-i\pi/3}}{1-\omega}=\frac{e^{-i\pi/3}}{\sqrt3\,e^{-i\pi/6}}=\frac{1}{\sqrt3}e^{-i\pi/6}=\left(\tfrac12,\,-\tfrac{\sqrt3}{6}\right).$$

En efecto $\sqrt3\,|b| = \sqrt3\cdot\frac{1}{\sqrt3} = 1$, el lado del triángulo central. ✓

**Condición del vértice sobre el lado grande.** El vértice inferior de $T_1$ es
$$d = b + x\left(e^{-i\pi/3}-1\right) = b + x\,e^{-2\pi i/3} = \left(\tfrac12-\tfrac{x}{2},\; -\tfrac{\sqrt3}{6}-\tfrac{x\sqrt3}{2}\right).$$

Para que $d$ esté sobre el lado inferior $y=-\sqrt3$:
$$\frac{\sqrt3}{6}+\frac{x\sqrt3}{2}=\sqrt3 \quad\Longrightarrow\quad \frac16+\frac{x}{2}=1 \quad\Longrightarrow\quad x=\frac53.$$

**Verificación.** Con $x=\tfrac53$: $T_1$ tiene vértices $(-\tfrac76,-\tfrac{\sqrt3}{6})$, $(\tfrac12,-\tfrac{\sqrt3}{6})$, $(-\tfrac13,-\sqrt3)$. El punto $b$ cae sobre el lado de $T_2$ a distancia $1\le \tfrac53$ de su extremo; los tres triángulos no se superponen y encierran exactamente el hueco central equilátero de vértices $(\pm\tfrac12,-\tfrac{\sqrt3}{6})$ y $(0,\tfrac{\sqrt3}{3})$, de lado $1$. ✓

$$\boxed{\dfrac{5}{3}}$$