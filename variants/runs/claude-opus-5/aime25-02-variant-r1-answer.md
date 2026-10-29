## Planteamiento

Coloco $P$ en el origen y uso que $D,E$ dividen $\overline{PQ}$ y $F,G$ dividen $\overline{PR}$ en razones iguales:

$$PQ = 3+9+6 = 18,\qquad PR = 5+15+10 = 30$$

$$\frac{PD}{PQ}=\frac{3}{18}=\frac16=\frac{5}{30}=\frac{PF}{PR},\qquad \frac{PE}{PQ}=\frac{12}{18}=\frac23=\frac{20}{30}=\frac{PG}{PR}$$

Por tanto $\triangle PDF \sim \triangle PQR$ con razón $1/6$, y $\triangle PEG \sim \triangle PQR$ con razón $2/3$:

$$[DEGF] = [PEG]-[PDF] = \left(\frac49-\frac1{36}\right)[PQR] = \frac{15}{36}[PQR] = \frac{5}{12}[PQR]$$

Como $[DEGF]=300$, resulta $[PQR] = 720$.

## Coordenadas

Tomo $P=(0,0)$, $Q=(18,0)$, $R=(0,80)$ (así $\tfrac12\cdot 18\cdot 80 = 720$). Entonces:

- $D=(3,0)$, $E=(12,0)$
- $F=\tfrac16 R=(0,\tfrac{40}{3})$, $G=\tfrac23 R=(0,\tfrac{160}{3})$
- $M = 2F-D = (-3,\tfrac{80}{3})$
- $N = 2E-G = (24,-\tfrac{160}{3})$

Verificación: con $D,E,G,F$ el área por shoelace es $\tfrac12|640-40|=300$ ✓

## Área del heptágono $PFNQREM$

Shoelace con $P(0,0)$, $F(0,\tfrac{40}3)$, $N(24,-\tfrac{160}3)$, $Q(18,0)$, $R(0,80)$, $E(12,0)$, $M(-3,\tfrac{80}3)$:

$$0 + \left(-320\right) + 960 + 1440 + \left(-960\right) + 320 + 0 = 1440$$

$$[PFNQREM] = \frac{1440}{2} = 720$$

(El heptágono resulta tener exactamente el área del triángulo: las reflexiones compensan las piezas quitadas y añadidas.)

\boxed{720}