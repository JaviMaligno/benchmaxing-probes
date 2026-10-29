Para hallar el área del heptágono $AFNBCEM$, analizamos primero las proporciones de los segmentos dados sobre los lados $\overline{AB}$ y $\overline{AC}$ del triángulo $\triangle ABC$.

### 1. Proporciones y paralelismo
En el lado $\overline{AB}$, los puntos $A, D, E, B$ están en ese orden con longitudes:
$$AD = 4, \quad DE = 16, \quad EB = 8$$
Por lo tanto, las longitudes acumuladas desde $A$ son:
$$AD = 4, \quad AE = 4 + 16 = 20, \quad AB = 20 + 8 = 28$$

En el lado $\overline{AC}$, los puntos $A, F, G, C$ están en ese orden con longitudes:
$$AF = 13, \quad FG = 52, \quad GC = 26$$
Las longitudes acumuladas desde $A$ son:
$$AF = 13, \quad AG = 13 + 52 = 65, \quad AC = 65 + 26 = 91$$

Observamos las razones de los segmentos respecto a los lados completos:
$$\frac{AD}{AB} = \frac{4}{28} = \frac{1}{7} = \frac{13}{91} = \frac{AF}{AC}$$
$$\frac{AE}{AB} = \frac{20}{28} = \frac{5}{7} = \frac{65}{91} = \frac{AG}{AC}$$

Por el recíproco del teorema de Tales, los triángulos $\triangle ADF$, $\triangle AEG$ y $\triangle ABC$ son semejantes, y las rectas $DF$, $EG$ y $BC$ son paralelas entre sí:
$$DF \parallel EG \parallel BC$$

---

### 2. Relación de áreas en $\triangle ABC$
Sea $S = [ABC]$ el área del triángulo $\triangle ABC$. Por semejanza de triángulos, las áreas son proporcionales al cuadrado de la razón de semejanza:
- $[ADF] = \left(\frac{1}{7}\right)^2 S = \frac{1}{49} S$
- $[AEG] = \left(\frac{5}{7}\right)^2 S = \frac{25}{49} S$

El área del trapecio $DEGF$ es la diferencia entre $[AEG]$ y $[ADF]$:
$$[DEGF] = [AEG] - [ADF] = \frac{25}{49} S - \frac{1}{49} S = \frac{24}{49} S$$

Dado que $[DEGF] = 288$, tenemos:
$$\frac{24}{49} S = 288 \implies \frac{1}{49} S = \frac{288}{24} = 12$$
Por consiguiente, el área de $\triangle ABC$ es:
$$S = 49 \times 12 = 588$$

---

### 3. Descomposición del heptágono $AFNBCEM$
Como $M$ es la reflexión de $D$ respecto a $F$, el punto $M$ se encuentra en la recta $DF$ y cumple $FM = DF$. De manera análoga, como $N$ es la reflexión de $G$ respecto a $E$, el punto $N$ se encuentra en la recta $EG$ y cumple $NE = EG$.

Así, las rectas paralelas $DM$ y $GN$ dividen el heptágono $AFNBCEM$ en tres regiones disjuntas:
1. **El triángulo $\triangle AFM$:**
   Tiene base $FM = DF$ sobre la recta $DF$ y comparte la misma altura desde el vértice $A$ que el triángulo $\triangle ADF$. Por lo tanto:
   $$[AFM] = [ADF] = \frac{1}{49} S = 12$$

2. **El trapecio $FNEM$:**
   Sus bases paralelas son $FM = DF$ y $NE = EG$, y la distancia perpendicular entre las rectas $DM$ y $GN$ es la misma altura del trapecio $DEGF$. Como tiene exactamente las mismas bases y la misma altura que $DEGF$, sus áreas son iguales:
   $$[FNEM] = [DEGF] = 288$$

3. **El trapecio $NBCE$:**
   Sus bases paralelas son $NE = EG$ y $BC$, y su altura es la distancia entre las rectas $GN$ y $BC$. Por tener las mismas bases y la misma altura que el trapecio $EBCG$, sus áreas son iguales:
   $$[NBCE] = [EBCG] = [ABC] - [AEG] = \left(1 - \frac{25}{49}\right) S = \frac{24}{49} S = 288$$

---

### 4. Área total
Sumando las áreas de las tres regiones que componen el heptágono $AFNBCEM$:
$$[AFNBCEM] = [AFM] + [FNEM] + [NBCE] = 12 + 288 + 288 = 588$$

\boxed{588}