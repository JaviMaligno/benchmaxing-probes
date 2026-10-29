Para encontrar el valor de $\wideparen{DE} + 2 \cdot \wideparen{HJ} + 3 \cdot \wideparen{FG}$, analizamos las propiedades del triángulo medial $\triangle DEF$ y su circuncírculo.

### Paso 1: Propiedades de $\triangle DEF$
Dado que $D$, $E$ y $F$ son los puntos medios de los lados $\overline{BC}$, $\overline{AC}$ y $\overline{AB}$, respectivamente, los lados de $\triangle DEF$ son paralelos a los lados de $\triangle ABC$:
$$DE \parallel AB, \quad EF \parallel BC, \quad FD \parallel AC$$

Por semejanza ($\triangle DEF \sim \triangle ABC$), los ángulos interiores de $\triangle DEF$ son:
$$\angle EDF = \angle BAC = 84^\circ$$
$$\angle DEF = \angle ABC = 60^\circ$$
$$\angle DFE = \angle ACB = 36^\circ$$

### Paso 2: Cálculo de $\wideparen{DE}$ y los arcos principales
En el circuncírculo de $\triangle DEF$, la medida de cada arco subtendido por un ángulo inscrito es el doble de la medida de dicho ángulo:
- $\wideparen{DE} = 2 \angle DFE = 2 \cdot 36^\circ = 72^\circ$
- $\wideparen{FGD} = 2 \angle DEF = 2 \cdot 60^\circ = 120^\circ$
- $\wideparen{EHJF} = 2 \angle EDF = 2 \cdot 84^\circ = 168^\circ$

### Paso 3: Cálculo de $\wideparen{FG}$
Como el punto $G$ se encuentra sobre el segmento $\overline{BD}$ (parte del lado $\overline{BC}$) y sabemos que $DF \parallel AC$, los ángulos $\angle FDG$ y $\angle ACB$ son ángulos correspondientes:
$$\angle FDG = \angle FDB = \angle ACB = 36^\circ$$

El ángulo inscrito $\angle FDG$ subtiende el arco menor $\wideparen{FG}$, por lo que:
$$\wideparen{FG} = 2 \angle FDG = 2 \cdot 36^\circ = 72^\circ$$

### Paso 4: Cálculo de $\wideparen{HJ}$
Observamos los puntos $H$ en $\overline{AE}$ (lado $\overline{AC}$) y $J$ en $\overline{AF}$ (lado $\overline{AB}$):
1. Como $EF \parallel BC$, los ángulos $\angle FEH$ y $\angle ACB$ son correspondientes:
   $$\angle FEH = \angle FEA = \angle ACB = 36^\circ$$
   El ángulo inscrito $\angle FEH$ subtiende el arco $\wideparen{FH}$ (compuesto por $\wideparen{FJ} + \wideparen{JH}$), por lo que:
   $$\wideparen{FH} = 2 \angle FEH = 2 \cdot 36^\circ = 72^\circ$$

2. De manera análoga, como $EF \parallel BC$, los ángulos $\angle EFJ$ y $\angle ABC$ son correspondientes:
   $$\angle EFJ = \angle EFA = \angle ABC = 60^\circ$$
   El ángulo inscrito $\angle EFJ$ subtiende el arco $\wideparen{EJ}$ (compuesto por $\wideparen{EH} + \wideparen{HJ}$), por lo que:
   $$\wideparen{EJ} = 2 \angle EFJ = 2 \cdot 60^\circ = 120^\circ$$
   Dado que el arco completo $\wideparen{EHJF}$ mide $168^\circ$, el arco menor $\wideparen{JF}$ mide:
   $$\wideparen{JF} = \wideparen{EHJF} - \wideparen{EJ} = 168^\circ - 120^\circ = 48^\circ$$

3. Por lo tanto, el arco menor $\wideparen{HJ}$ es:
   $$\wideparen{HJ} = \wideparen{FH} - \wideparen{JF} = 72^\circ - 48^\circ = 24^\circ$$

### Paso 5: Cálculo de la expresión final
Sustituimos $\wideparen{DE} = 72^\circ$, $\wideparen{HJ} = 24^\circ$ y $\wideparen{FG} = 72^\circ$ en la expresión solicitada:
$$\wideparen{DE} + 2 \cdot \wideparen{HJ} + 3 \cdot \wideparen{FG} = 72^\circ + 2(24^\circ) + 3(72^\circ) = 72^\circ + 48^\circ + 216^\circ = 336^\circ$$

\boxed{336}