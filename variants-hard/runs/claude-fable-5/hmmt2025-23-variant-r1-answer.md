## Solución

**Planteamiento.** Sea $s$ el lado del cuadrado. Cada uno de los cuatro triángulos tiene como base un lado del cuadrado, así que su área es $\frac{1}{2}s \cdot d$, donde $d$ es la distancia de $Q$ a ese lado. Las cuatro áreas suman el área del cuadrado:
$$3+4+6+7 = 20 = s^2 \implies s = 2\sqrt{5}.$$

Las distancias de $Q$ a dos lados opuestos suman $s$, así que las áreas de triángulos opuestos suman $\frac{1}{2}s^2 = 10$. Los pares opuestos deben ser $\{3,7\}$ y $\{4,6\}$.

**Coordenadas.** Pongo $W=(0,0)$, $X=(s,0)$, $Y=(s,s)$, $Z=(0,s)$ y $Q=(x,y)$. Las distancias a los lados $WX, XY, YZ, ZW$ son $a=y$, $b=s-x$, $c=s-y$, $d=x$. Tomando el caso $(a,c) \propto (3,7)$, $(b,d) \propto (4,6)$, con factor de escala $\frac{2}{s} = \frac{1}{\sqrt5}$:
$$a=\tfrac{3}{\sqrt5},\quad b=\tfrac{4}{\sqrt5},\quad c=\tfrac{7}{\sqrt5},\quad d=\tfrac{6}{\sqrt5}.$$

**Cálculo de las distancias a los vértices.**
$$QW^2 = d^2+a^2 = \tfrac{36+9}{5}=9,\qquad QX^2 = a^2+b^2 = \tfrac{9+16}{5}=5,$$
$$QY^2 = b^2+c^2 = \tfrac{16+49}{5}=13,\qquad QZ^2 = c^2+d^2 = \tfrac{49+36}{5}=17.$$

Entonces:
$$(QW\cdot QX\cdot QY\cdot QZ)^2 = 9\cdot 5\cdot 13\cdot 17 = 9945.$$

**Invariancia del orden.** El producto es $(a^2+b^2)(b^2+c^2)(c^2+d^2)(d^2+a^2)$, que es simétrico ante intercambiar $a\leftrightarrow c$, $b\leftrightarrow d$, o los pares entre sí; cualquier asignación válida de las áreas da el mismo valor.

$$QW\cdot QX\cdot QY\cdot QZ = \sqrt{9945} = \boxed{3\sqrt{1105}}$$