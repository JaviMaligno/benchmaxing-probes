# Solución paso a paso

**Planteamiento.** La cuadrícula $2\times 2$ tiene $12$ segmentos unitarios: $8$ en el borde exterior (cada uno pertenece a **un solo** cuadrado) y $4$ interiores (cada uno compartido por **dos** cuadrados: los que forman la "cruz" central).

**Conteo por incidencias.** Cada uno de los $4$ cuadrados debe tener exactamente $1$ lado rojo, así que hay exactamente $4$ incidencias (cuadrado, lado rojo). Un segmento interior rojo aporta $2$ incidencias; uno de borde, $1$. Si $k$ = segmentos interiores rojos y $m$ = segmentos de borde rojos:
$$2k + m = 4 \implies (k,m) \in \{(0,4),\ (1,2),\ (2,0)\}.$$

**Caso $k=0$:** los 4 lados rojos están en el borde. Cada cuadrado tiene $2$ lados exteriores y elige exactamente uno para ser rojo: $2^4 = 16$ coloraciones.

**Caso $k=1$:** sea, por ejemplo, rojo el segmento interior vertical $v_1$ (entre los cuadrados superiores $A$ y $B$). Entonces $A$ y $B$ ya cumplen, y todos sus demás lados son azules. Los cuadrados inferiores $C$ y $D$ necesitan su lado rojo en su borde exterior (izquierdo o inferior para $C$; derecho o inferior para $D$): $2\cdot 2 = 4$ coloraciones. Hay $4$ segmentos interiores posibles, cada uno con $4$ coloraciones: $4 \cdot 4 = 16$.

**Caso $k=2$:** los dos lados rojos son interiores, y cada cuadrado debe tocar **exactamente uno**. De las parejas de segmentos interiores, solo funcionan el par vertical $\{v_1,v_2\}$ y el par horizontal $\{h_1,h_2\}$ (cualquier pareja "adyacente" daría un cuadrado con dos lados rojos). Esto da $2$ coloraciones.

**Total:**
$$16 + 16 + 2 = 34.$$

\boxed{34}