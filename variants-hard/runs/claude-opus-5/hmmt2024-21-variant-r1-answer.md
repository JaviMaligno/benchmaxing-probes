## Configuración

Tomo el centro común $O$ (por la simetría de orden 3, el centro del triángulo grande, el del hueco central y el centro de rotación del molinete coinciden). En la disposición en molinete los tres triángulos pequeños están invertidos respecto del grande, y el hueco central queda con la misma orientación que el grande.

Coordenadas: el hueco central $D$ (lado 2, apuntando hacia abajo en mi marco) con centro en el origen tiene vértices
$$L=(-1,\tfrac1{\sqrt3}),\quad R=(1,\tfrac1{\sqrt3}),\quad B=(0,-\tfrac2{\sqrt3}),$$
es decir, inradio $\dfrac{2}{2\sqrt3}=\dfrac{1}{\sqrt3}$.

El triángulo $T_1$ (lado $x$) apoya su lado inferior sobre la recta $y=\tfrac1{\sqrt3}$, y para que el hueco sea exactamente $D$ sin solapamientos, su vértice inferior izquierdo debe caer en $L$:
$$T_1:\;(-1,\tfrac1{\sqrt3}),\;(x-1,\tfrac1{\sqrt3}),\;(\tfrac x2-1,\tfrac1{\sqrt3}+\tfrac{x\sqrt3}{2}).$$
Los otros dos son $R_{120^\circ}(T_1)$ y $R_{240^\circ}(T_1)$. Se comprueba que $L$ pertenece al lado derecho de $T_2$ (recta $y=-\sqrt3x-\tfrac2{\sqrt3}$): ahí está el contacto vértice‑sobre‑triángulo del molinete.

## Contacto con el triángulo grande

Un vértice solo puede tocar un lado del triángulo grande **en un único punto** si ese lado es paralelo al lado opuesto del triangulito (si fuera paralelo a un lado adyacente, toda una arista quedaría apoyada, con dos vértices sobre el lado). Eso obliga a que el vértice de contacto sea el ápice $(\tfrac x2-1,\tfrac1{\sqrt3}+\tfrac{x\sqrt3}{2})$, apoyado en el lado paralelo a la base del triangulito.

Midiendo sobre la perpendicular desde $O$ a ese lado:
$$\underbrace{\frac{1}{\sqrt3}}_{\text{inradio del hueco}}+\underbrace{\frac{x\sqrt3}{2}}_{\text{altura del triangulito}}=\underbrace{\frac{9}{2\sqrt3}}_{\text{inradio del grande}}$$

Multiplicando por $2\sqrt3$:
$$2+3x=9\quad\Longrightarrow\quad x=\frac73.$$

**Verificación** ($x=7/3\approx2.333$): $T_1=\{(-1,0.577),(1.333,0.577),(0.167,2.598)\}$ toca el lado superior en $(0.167,2.598)$; $T_2$ toca el lado izquierdo en $(-2.333,-1.155)$ y $T_3$ el derecho (tres lados distintos). El vértice $(-1,0.577)$ de $T_1$ está sobre la arista de $T_2$, los triángulos no se solapan (solo se tocan en $L$, $R$, $B$) y encierran exactamente el triángulo central de lado 2.

$$\boxed{\dfrac{7}{3}}$$