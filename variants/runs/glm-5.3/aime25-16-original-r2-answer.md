# Resolución

## Paso 1: Coordenadas en la recta

Coloco los puntos en el eje $x$ con $A = 0$. De $AF = 73$ y $DF = 33$:

$$AB = AF - DF = 73 - 33 = 40$$

Espera — mejor derivo cada tramo con las ecuaciones dadas:
- $c - a = 26$, $d - b = 22$, $e - c = 31$, $d - f = -33$, $a - f = -73$.

De $f - a = 73$: $b - a = 73 - 33 - 22 = 18$, y $d - c = 14$, $c - b = 8$.

Entonces:
$$A=0,\quad B=18,\quad C=26,\quad D=40,\quad E=57,\quad F=73$$

**Verificación:** $AC=26$✓, $BD=22$✓, $CE=31$✓, $DF=33$✓, $AF=73$✓.

## Paso 2: Coordenadas de $G$

Sea $G=(x,y)$, $y \neq 0$. Con $CG=40$ y $DG=30$:

$$(x-26)^2 + y^2 = 1600, \qquad (x-40)^2 + y^2 = 900$$

Restando la segunda de la primera:

$$(x-26)^2 - (x-40)^2 = 700$$
$$28x - 924 = 700 \implies x = 58$$

Entonces:
$$y^2 = 1600 - (58-26)^2 = 1600 - 1024 = 576 \implies y = \pm 24$$

Tomo $G = (58, 24)$.

## Paso 3: Área de $\triangle BGE$

Con $B = (18,0)$, $G = (58,24)$, $E = (57,0)$:

$$\text{Área} = \frac{1}{2}\left|\det\begin{pmatrix} 58-18 & 24 \\ 57-18 & 0 \end{pmatrix}\right| = \frac{1}{2}\left| 40\cdot 0 - 24 \cdot 39 \right| = \frac{936}{2}$$

**Verificación:** base $BE = 39$ sobre el eje $x$, altura $= 24$; área $= \frac{39 \cdot 24}{2} = 468$. ✓

\boxed{468}