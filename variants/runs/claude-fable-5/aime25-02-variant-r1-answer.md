## Resolución

**Paso 1: Hallar el área del triángulo PQR.**

Sobre $\overline{PQ}$: $PQ = 3+9+6 = 18$, con $PD = 3$ y $PE = 12$, así que $PD/PQ = 1/6$ y $PE/PQ = 2/3$.
Sobre $\overline{PR}$: $PR = 5+15+10 = 30$, con $PF = 5$ y $PG = 20$, así que $PF/PR = 1/6$ y $PG/PR = 2/3$.

Como las razones coinciden, $DF \parallel EG \parallel QR$, y:

$$[DEGF] = [PEG] - [PDF] = \left(\tfrac{4}{9} - \tfrac{1}{36}\right)[PQR] = \tfrac{15}{36}[PQR] = \tfrac{5}{12}[PQR]$$

Con $[DEGF] = 300$, obtenemos $[PQR] = 720$.

**Paso 2: Coordenadas.**

Tomo $P=(0,0)$, $Q=(18,0)$, $R=(0,80)$ (área $= \tfrac12 \cdot 18 \cdot 80 = 720$ ✓). Entonces:

- $D = (3,0)$, $E = (12,0)$
- $F = \tfrac16 R = (0, \tfrac{40}{3})$, $G = \tfrac23 R = (0, \tfrac{160}{3})$
- $M = 2F - D = (-3, \tfrac{80}{3})$ (reflexión de $D$ en $F$)
- $N = 2E - G = (24, -\tfrac{160}{3})$ (reflexión de $G$ en $E$)

**Paso 3: Shoelace sobre el heptágono $P, F, N, Q, R, E, M$** (se verifica que el polígono es simple):

$$
\begin{aligned}
\sum (x_i y_{i+1} - x_{i+1} y_i) &= 0 + \left(0 - 24\cdot\tfrac{40}{3}\right) + \left(0 + 18\cdot\tfrac{160}{3}\right) + (18\cdot 80) \\
&\quad + (0 - 12\cdot 80) + \left(12\cdot\tfrac{80}{3}\right) + 0 \\
&= -320 + 960 + 1440 - 960 + 320 = 1440
\end{aligned}
$$

Área $= \tfrac{1440}{2} = 720$. Las reflexiones compensan exactamente las regiones añadidas y quitadas, de modo que el heptágono tiene la misma área que el triángulo.

$$\boxed{720}$$