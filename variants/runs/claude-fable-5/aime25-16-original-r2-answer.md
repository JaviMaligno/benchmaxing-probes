## Solución

**Ubicar los puntos en la recta.** Pongo $A = 0$. Entonces:
- $AC = 26 \Rightarrow C = 26$
- $AF = 73 \Rightarrow F = 73$
- $DF = 33 \Rightarrow D = 40$
- $BD = 22 \Rightarrow B = 18$
- $CE = 31 \Rightarrow E = 57$

Las posiciones $0, 18, 26, 40, 57, 73$ respetan el orden $A, B, C, D, E, F$. ✓

**Encontrar la posición de $G$.** Con coordenadas, sea $G = (x, y)$:
- $CG = 40$: $(x-26)^2 + y^2 = 1600$
- $DG = 30$: $(x-40)^2 + y^2 = 900$

Restando: $(x-26)^2 - (x-40)^2 = 700$, es decir $14(2x - 66) = 700$, de donde $2x - 66 = 50$ y $x = 58$.

Entonces $y^2 = 1600 - (58-26)^2 = 1600 - 1024 = 576$, así que $|y| = 24$. Esta es la altura de $G$ respecto a la recta.

**Área de $\triangle BGE$.** La base es $BE = 57 - 18 = 39$ y la altura es $24$:

$$\text{Área} = \frac{1}{2} \cdot 39 \cdot 24 = 468$$

$$\boxed{468}$$