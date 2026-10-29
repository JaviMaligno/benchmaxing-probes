## Planteamiento

Sea $h$ la altura de la caverna. Colocando el suelo en $y=0$, las puntas de las formaciones están a las alturas:

- Estalactitas: $h-18$ y $h-34$
- Estalagmitas: $25$ y $47$

**Emparejar las diagonales del cuadrado.** Las diagonales de un cuadrado se bisecan, así que los puntos medios de los dos pares de vértices opuestos coinciden (en particular, en la coordenada $y$). Probando los emparejamientos:

- Estalactita con estalagmita: $\frac{(h-18)+25}{2} = \frac{(h-34)+47}{2}$ da $h+7 = h+13$, imposible; el otro cruce da $h+29 = h-9$, también imposible.
- Las dos estalactitas opuestas entre sí (y las dos estalagmitas opuestas entre sí):
$$\frac{(h-18)+(h-34)}{2} = \frac{25+47}{2} \implies h - 26 = 36 \implies h = 62.$$

**Verificación de que existe tal cuadrado.** Con $h = 62$, las alturas de las puntas son $44, 28$ (estalactitas) y $25, 47$ (estalagmitas). Una diagonal une puntos con diferencia vertical $44-28 = 16$ y componente horizontal $a$; la otra tiene diferencia vertical $47-25 = 22$ y componente horizontal $b$. Para un cuadrado, las diagonales deben ser perpendiculares y de igual longitud:

$$ab + 16\cdot 22 = 0, \qquad a^2 + 256 = b^2 + 484.$$

De ahí $ab = -352$ y $a^2 - b^2 = 228$. Resolviendo: $a^2 = 484$, $b^2 = 256$, es decir $a = 22$, $b = -16$, que satisface $ab = -352$. 

Con centro en $(0, 36)$, los vértices son $A=(11,44)$, $B=(8,25)$, $C=(-11,28)$, $D=(-8,47)$. Comprobando los lados: $\vec{AB}=(-3,-19)$, $\vec{BC}=(-19,3)$, $\vec{CD}=(3,19)$, $\vec{DA}=(19,-3)$ — todos de longitud $\sqrt{370}$ y consecutivamente perpendiculares. Es un cuadrado válido, con todas las puntas entre el suelo y el techo.

$$\boxed{62}$$