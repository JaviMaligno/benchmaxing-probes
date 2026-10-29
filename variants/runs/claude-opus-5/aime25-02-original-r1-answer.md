## Planteamiento

Sobre $\overline{AB}$: $AB = 4+16+8 = 28$, con $AD=4$, $AE=20$.
Sobre $\overline{AC}$: $AC = 13+52+26 = 91$, con $AF=13$, $AG=65$.

### Paso 1: Área total del triángulo

Sea $T = [ABC]$. Usando la razón de áreas para triángulos que comparten el vértice $A$:

- $[ADG] = \dfrac{AD}{AB}\cdot\dfrac{AG}{AC}\,T = \dfrac{4}{28}\cdot\dfrac{65}{91}T = \dfrac{1}{7}\cdot\dfrac{5}{7}T = \dfrac{5T}{49}$
- $[ADF] = \dfrac{1}{7}\cdot\dfrac{13}{91}T = \dfrac{T}{49}$
- $[AEG] = \dfrac{20}{28}\cdot\dfrac{65}{91}T = \dfrac{5}{7}\cdot\dfrac{5}{7}T = \dfrac{25T}{49}$

Entonces
$$[DEGF] = [DFG] + [DEG] = \left(\tfrac{5T}{49}-\tfrac{T}{49}\right) + \left(\tfrac{25T}{49}-\tfrac{5T}{49}\right) = \frac{24T}{49} = 288$$

De aquí $T = 588$.

### Paso 2: Coordenadas y heptágono

Tomo $A=(0,0)$, $B=(28,0)$, $D=(4,0)$, $E=(20,0)$, y $C=(7k,42)$ (la altura $42$ da área $\tfrac12\cdot28\cdot42=588$). Así:

$$F=\tfrac17 C=(k,6),\qquad G=\tfrac57 C=(5k,30)$$
$$M = 2F-D = (2k-4,\,12),\qquad N = 2E-G = (40-5k,\,-30)$$

Shoelace sobre $A, F, N, B, C, E, M$:

| tramo | $x_iy_{i+1}-x_{i+1}y_i$ |
|---|---|
| $A\to F$ | $0$ |
| $F\to N$ | $-30k-(40-5k)6 = -240$ |
| $N\to B$ | $+840$ |
| $B\to C$ | $+1176$ |
| $C\to E$ | $-840$ |
| $E\to M$ | $+240$ |
| $M\to A$ | $0$ |

Suma $=1176$, luego el área es $\tfrac{1176}{2}=588$ (nótese que el parámetro $k$ se cancela, como debía ocurrir).

El heptágono tiene exactamente la misma área que $\triangle ABC$: las reflexiones intercambian las piezas $\triangle AFM \leftrightarrow$ zonas sobrantes de forma equivalente.

\boxed{588}