Para resolver el problema paso a paso, analizamos las propiedades geométricas de la circunferencia circunscrita al $\triangle DEF$:

1. **Identificación de la circunferencia de los nueve puntos:**
   Dado que $D$, $E$ y $F$ son los puntos medios de los lados $\overline{QR}$, $\overline{PR}$ y $\overline{PQ}$ respectivamente, la circunferencia circunscrita al $\triangle DEF$ es la **circunferencia de los nueve puntos** (o circunferencia de Euler) del $\triangle PQR$. Esta circunferencia interseca por segunda vez a cada uno de los lados del triángulo precisamente en los pies de las alturas. Por lo tanto:
   - $G$ es el pie de la altura desde $P$ hacia $\overline{QR}$ (como $\angle PQR = 58^\circ > 42^\circ = \angle PRQ$, $G$ se encuentra en el segmento $\overline{QD}$, dando el orden $Q - G - D - R$).
   - $H$ es el pie de la altura desde $Q$ hacia $\overline{PR}$ (como $\angle QPR = 80^\circ > 42^\circ = \angle PRQ$, $H$ se encuentra en el segmento $\overline{PE}$, dando el orden $P - H - E - R$).
   - $J$ es el pie de la altura desde $R$ hacia $\overline{PQ}$ (como $\angle QPR = 80^\circ > 58^\circ = \angle PQR$, $J$ se encuentra en el segmento $\overline{PF}$, dando el orden $P - J - F - Q$).

   Recorriendo el perímetro del triángulo, los seis puntos aparecen en la circunferencia en el orden cíclico $G, D, E, H, J, F$.

2. **Cálculo de $\wideparen{DE}$:**
   Por ser $D, E, F$ los puntos medios de los lados, los segmentos medios son paralelos a los lados del $\triangle PQR$ ($DE \parallel PQ$, $DF \parallel PR$, $EF \parallel QR$) y $\triangle DEF \sim \triangle PQR$. En consecuencia:
   $$\angle EDF = \angle QPR = 80^\circ, \quad \angle DEF = \angle PQR = 58^\circ, \quad \angle DFE = \angle PRQ = 42^\circ$$
   El ángulo inscrito $\angle DFE$ subtiende el arco menor $\wideparen{DE}$, por lo que:
   $$\wideparen{DE} = 2 \angle DFE = 2 \cdot 42^\circ = 84^\circ$$

3. **Cálculo de $\wideparen{FG}$:**
   Como $DF \parallel PR$ y los puntos $Q, G, D, R$ son colineales en ese orden sobre $\overline{QR}$, por ángulos correspondientes se cumple que:
   $$\angle FDG = \angle PRQ = 42^\circ$$
   Dado que $\angle FDG$ es un ángulo inscrito en la circunferencia que subtiende el arco menor $\wideparen{FG}$, obtenemos:
   $$\wideparen{FG} = 2 \angle FDG = 2 \cdot 42^\circ = 84^\circ$$

4. **Cálculo de $\wideparen{HJ}$:**
   El ángulo inscrito $\angle EDF = 80^\circ$ subtiende el arco $\wideparen{EF}$ que contiene a los puntos $H$ y $J$:
   $$\wideparen{EH} + \wideparen{HJ} + \wideparen{JF} = 2 \angle EDF = 2 \cdot 80^\circ = 160^\circ$$
   - Como $EF \parallel QR$ y el orden en $\overline{PR}$ es $P - H - E - R$, el ángulo inscrito $\angle FEH = \angle FEP$ es correspondiente con $\angle PRQ = 42^\circ$. Este ángulo subtiende el arco $\wideparen{FH} = \wideparen{HJ} + \wideparen{JF}$, de modo que:
     $$\wideparen{HJ} + \wideparen{JF} = 2 \angle FEH = 2 \cdot 42^\circ = 84^\circ$$
     Restando de $160^\circ$, hallamos $\wideparen{EH} = 160^\circ - 84^\circ = 76^\circ$.
   - De forma análoga, como $EF \parallel QR$ y el orden en $\overline{PQ}$ es $P - J - F - Q$, el ángulo inscrito $\angle EFJ = \angle EFP$ es correspondiente con $\angle PQR = 58^\circ$. Este ángulo subtiende el arco $\wideparen{EJ} = \wideparen{EH} + \wideparen{HJ}$, por lo que:
     $$\wideparen{EH} + \wideparen{HJ} = 2 \angle EFJ = 2 \cdot 58^\circ = 116^\circ$$
   - Sustituyendo $\wideparen{EH} = 76^\circ$, obtenemos:
     $$\wideparen{HJ} = 116^\circ - 76^\circ = 40^\circ$$

5. **Cálculo final:**
   Sustituimos las medidas de los tres arcos en la expresión pedida:
   $$\wideparen{DE} + 2 \cdot \wideparen{HJ} + 3 \cdot \wideparen{FG} = 84^\circ + 2(40^\circ) + 3(84^\circ) = 84^\circ + 80^\circ + 252^\circ = 416^\circ$$

\boxed{416}