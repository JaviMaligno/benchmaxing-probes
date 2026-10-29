Para resolver este problema paso a paso, analizamos las propiedades geométricas del triángulo $\triangle PQR$ y la circunferencia circunscrita a su triángulo medial $\triangle DEF$.

### Paso 1: Identificación de la circunferencia de los nueve puntos y el orden de los puntos
En $\triangle PQR$, tenemos $\angle P = 80^\circ$, $\angle Q = 58^\circ$ y $\angle R = 42^\circ$. Como todos sus ángulos son agudos, $\triangle PQR$ es un triángulo acutángulo.

Dado que $D$, $E$ y $F$ son los puntos medios de los lados $\overline{QR}$, $\overline{PR}$ y $\overline{PQ}$ respectivamente, la circunferencia circunscrita a $\triangle DEF$ es la **circunferencia de los nueve puntos** de $\triangle PQR$. Esta circunferencia interseca a las rectas que contienen los lados del triángulo ($QR$, $PR$ y $PQ$) por segunda vez precisamente en los pies de las alturas trazadas desde $P$, $Q$ y $R$:
- Como $\angle Q > \angle R$, se cumple que $PR > PQ$, por lo que el pie de la altura desde $P$ hacia $\overline{QR}$ está más cerca de $Q$ que de $R$, cayendo en el segmento $\overline{QD}$. Por tanto, $G$ es el pie de la altura desde $P$.
- Como $\angle P > \angle R$, el pie de la altura desde $Q$ hacia $\overline{PR}$ cae en $\overline{PE}$, siendo este el punto $H$.
- Como $\angle P > \angle Q$, el pie de la altura desde $R$ hacia $\overline{PQ}$ cae en $\overline{PF}$, siendo este el punto $J$.

Recorriendo el perímetro de $\triangle PQR$ en el sentido $Q \to R \to P \to Q$, encontramos los seis puntos sobre la circunferencia en el orden cíclico $G, D, E, H, J, F$, los cuales dividen la circunferencia en los seis arcos menores $\wideparen{GD}$, $\wideparen{DE}$, $\wideparen{EH}$, $\wideparen{HJ}$, $\wideparen{JF}$ y $\wideparen{FG}$.

---

### Paso 2: Cálculo de $\wideparen{DE}$
Como $D$, $E$ y $F$ son los puntos medios de los lados de $\triangle PQR$, por el teorema de los puntos medios se tiene que $\overline{DF} \parallel \overline{PR}$ y $\overline{EF} \parallel \overline{QR}$. Por lo tanto, el cuadrilátero $DFER$ es un paralelogramo y:
$$\angle DFE = \angle PRQ = 42^\circ$$

Dado que $\angle DFE$ es un ángulo inscrito en la circunferencia que subtiende el arco menor $\wideparen{DE}$, la medida en grados de dicho arco es:
$$\wideparen{DE} = 2 \cdot \angle DFE = 2 \cdot 42^\circ = 84^\circ$$

---

### Paso 3: Cálculo de $\wideparen{HJ}$
Consideremos el triángulo $\triangle PEF$. Como $\overline{EF} \parallel \overline{QR}$, tenemos que $\triangle PEF \sim \triangle PRQ$, de donde:
- $\angle PEF = \angle PRQ = 42^\circ$
- $\angle PFE = \angle PQR = 58^\circ$

Además, $PEDF$ es un paralelogramo, por lo que $\angle EDF = \angle QPR = 80^\circ$. El ángulo inscrito $\angle EDF$ subtiende el arco $\wideparen{EHF} = \wideparen{EH} + \wideparen{HJ} + \wideparen{JF}$, cuya medida es:
$$\wideparen{EHF} = 2 \cdot \angle EDF = 2 \cdot 80^\circ = 160^\circ$$
Por lo tanto, el arco restante $\wideparen{EDF}$ (que contiene a $D$ y $G$) mide $360^\circ - 160^\circ = 200^\circ$.

Por propiedad del ángulo exterior formado por dos secantes trazadas desde $P$ (las rectas $PE$ y $PF$, que cortan a la circunferencia en $H, E$ y $J, F$ respectivamente):
$$\angle EPF = \frac{\wideparen{EDF} - \wideparen{HJ}}{2}$$
Sustituyendo $\angle EPF = 80^\circ$ y $\wideparen{EDF} = 200^\circ$:
$$80^\circ = \frac{200^\circ - \wideparen{HJ}}{2} \implies 160^\circ = 200^\circ - \wideparen{HJ} \implies \wideparen{HJ} = 40^\circ$$

---

### Paso 4: Cálculo de $\wideparen{FG}$
En el triángulo $\triangle QFD$, dado que $\overline{DF} \parallel \overline{PR}$, los ángulos $\angle QDF$ y $\angle QRP$ son correspondientes entre paralelas, por lo que:
$$\angle QDF = \angle PRQ = 42^\circ$$

Como $G$ se encuentra sobre el segmento $\overline{QD}$, la cuerda $\overline{DG}$ está contenida en el rayo $DQ$, de modo que el ángulo inscrito $\angle GDF = \angle QDF = 42^\circ$. Este ángulo inscrito subtiende el arco menor $\wideparen{FG}$, por lo que:
$$\wideparen{FG} = 2 \cdot \angle GDF = 2 \cdot 42^\circ = 84^\circ$$

---

### Paso 5: Resultado final
Sustituimos los valores obtenidos en la expresión pedida:
$$\wideparen{DE} + 2 \cdot \wideparen{HJ} + 3 \cdot \wideparen{FG} = 84^\circ + 2(40^\circ) + 3(84^\circ) = 84^\circ + 80^\circ + 252^\circ = 416^\circ$$

\boxed{416}