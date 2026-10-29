Para hallar el área del heptágono $PFNQREM$, primero determinamos el área de $\triangle PQR$ y luego establecemos un sistema de coordenadas afines adecuado.

### Paso 1: Área de $\triangle PQR$
En el lado $\overline{PQ}$, tenemos las longitudes:
$$PD = 3, \quad PE = PD + DE = 3 + 9 = 12, \quad PQ = PE + EQ = 12 + 6 = 18$$

En el lado $\overline{PR}$, tenemos las longitudes:
$$PF = 5, \quad PG = PF + FG = 5 + 15 = 20, \quad PR = PG + GR = 20 + 10 = 30$$

Observamos que los puntos dividen ambos lados en la misma proporción:
$$\frac{PD}{PQ} = \frac{3}{18} = \frac{1}{6} = \frac{5}{30} = \frac{PF}{PR}$$
$$\frac{PE}{PQ} = \frac{12}{18} = \frac{2}{3} = \frac{20}{30} = \frac{PG}{PR}$$

Por lo tanto, $\triangle PDF \sim \triangle PEG \sim \triangle PQR$ con razón de semejanza $1 : 4 : 6$. Como las áreas están en razón de los cuadrados de sus lados correspondientes ($1^2 : 4^2 : 6^2 = 1 : 16 : 36$), si llamamos $A = [PDF]$, entonces:
$$[PEG] = 16A \quad \text{y} \quad [PQR] = 36A$$

El área del cuadrilátero $DEGF$ es:
$$[DEGF] = [PEG] - [PDF] = 16A - A = 15A$$

Dado que $[DEGF] = 300$, obtenemos $A = \frac{300}{15} = 20$. Así, el área total del triángulo $\triangle PQR$ es:
$$[PQR] = 36A = 36 \times 20 = 720$$

---

### Paso 2: Coordenadas afines y vértices del heptágono
Dado que las razones de áreas y los puntos medios se conservan bajo transformaciones afines, tomamos a $P$ como el origen $(0,0)$ y usamos la base dada por los vectores $\vec{e}_1 = \overrightarrow{PD}$ y $\vec{e}_2 = \overrightarrow{PF}$. En este sistema de coordenadas, un triángulo unitario de base $1$ y altura $1$ (como $\triangle PDF$) tiene área $A = 20$.

Las coordenadas de los puntos sobre $\overline{PQ}$ y $\overline{PR}$ son:
- $P = (0, 0)$
- $D = (1, 0)$, $E = (4, 0)$, $Q = (6, 0)$
- $F = (0, 1)$, $G = (0, 4)$, $R = (0, 6)$

Calculamos las coordenadas de las reflexiones $M$ y $N$:
- Como $M$ es la reflexión de $D$ respecto a $F$, $F$ es el punto medio de $\overline{DM}$:
  $$M = 2F - D = 2(0, 1) - (1, 0) = (-1, 2)$$
- Como $N$ es la reflexión de $G$ respecto a $E$, $E$ es el punto medio de $\overline{GN}$:
  $$N = 2E - G = 2(4, 0) - (0, 4) = (8, -4)$$

---

### Paso 3: Área del heptágono $PFNQREM$
Aplicamos la fórmula de Gauss (fórmula de la lazada) a los vértices ordenados del heptágono simple $P(0,0) \to F(0,1) \to N(8,-4) \to Q(6,0) \to R(0,6) \to E(4,0) \to M(-1,2) \to P(0,0)$.

Calculamos los determinantes $x_i y_{i+1} - x_{i+1} y_i$ para cada arista:
1. $P(0,0) \to F(0,1)$: $0(1) - 0(0) = 0$
2. $F(0,1) \to N(8,-4)$: $0(-4) - 8(1) = -8$
3. $N(8,-4) \to Q(6,0)$: $8(0) - 6(-4) = 24$
4. $Q(6,0) \to R(0,6)$: $6(6) - 0(0) = 36$
5. $R(0,6) \to E(4,0)$: $0(0) - 4(6) = -24$
6. $E(4,0) \to M(-1,2)$: $4(2) - (-1)(0) = 8$
7. $M(-1,2) \to P(0,0)$: $(-1)(0) - 0(2) = 0$

Sumando estas contribuciones:
$$\sum (x_i y_{i+1} - x_{i+1} y_i) = 0 - 8 + 24 + 36 - 24 + 8 + 0 = 36$$

Como el triángulo $\triangle PDF$ con vértices $(0,0), (1,0), (0,1)$ tiene determinante $1$ y área $A = 20$, el área del heptágono es:
$$[PFNQREM] = 36 \times A = 36 \times 20 = 720$$

\boxed{720}