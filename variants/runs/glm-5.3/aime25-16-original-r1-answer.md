## Planteamiento

Coloco los puntos en una recta (el eje $x$), con $A$ en $0$.

**Posiciones en la recta:**

- $AF = 73 \Rightarrow F = 73$
- $AC = 26 \Rightarrow C = 26$
- $DF = 33 \Rightarrow D = 73 - 33 = 40$
- $CE = 31 \Rightarrow E = 26 + 31 = 57$
- $BD = 22 \Rightarrow B = 40 - 22 = 18$

Compruebo el orden: $0 < 18 < 26 < 40 < 57 < 73$. ✓

**Altura de $G$ sobre la recta:**

En el triángulo $\triangle CGD$: $CG = 40$, $DG = 30$, $CD = 40 - 26 = 14$.

Por la fórmula de Herón, con semiperímetro $s = \frac{40+30+14}{2} = 42$:

$$[\triangle CGD] = \sqrt{42 \cdot 2 \cdot 12 \cdot 28} = \sqrt{28224} = 168$$

La altura $h$ de $G$ sobre la recta satisface $\frac{1}{2}\cdot 14 \cdot h = 168$, así que $h = 24$.

**Verificación de consistencia:** si $G = (x_G, 24)$, entonces $(x_G-26)^2 = 1600-576 = 1024$ y $(x_G-40)^2 = 900-576 = 324$, lo que da $x_G = 58$ en ambos casos. ✓

**Área de $\triangle BGE$:**

Los puntos $B$ y $E$ están en la recta, con $BE = 57 - 18 = 39$, y la altura desde $G$ es $h = 24$:

$$[\triangle BGE] = \frac{1}{2} \cdot 39 \cdot 24 = 468$$

$$\boxed{468}$$