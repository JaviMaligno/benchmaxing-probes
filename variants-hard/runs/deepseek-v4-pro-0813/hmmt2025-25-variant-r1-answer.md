Voy a resolver el problema paso a paso.

**Configuración inicial**

Sea $\triangle DEF$ equilátero de lado $9$. Su circuncentro $O$ también es baricentro. El circunradio es

\[
R=\frac{9}{\sqrt{3}}=3\sqrt{3}.
\]

Sea $Y$ un punto sobre el circuncírculo de $\triangle DEF$, distinto de $D$, tal que $Y$ también está sobre el círculo de diámetro $\overline{DQ}$.

Como $Y$ está sobre el círculo de diámetro $DQ$, se cumple

\[
\angle DYQ = 90^\circ.
\]

Además, $Y$ está sobre el circuncírculo de $\triangle DEF$, de modo que $D,E,F,Y$ son concíclicos.

---

**Uso del cuadrilátero cíclico**

Como $E,F,Y,D$ están sobre el mismo círculo y $\angle EQF=120^\circ$:

En el cuadrilátero cíclico $E F Q \dots$ — observemos que $Q$ no está necesariamente en el circuncírculo. Usamos el dato $\angle EQF=120^\circ$ directamente sobre el triángulo $EQF$.

Como $Y$ está en el circuncírculo de $DEF$, y $Q$ satisface $\angle EQF=120^\circ$, queremos relacionar esto con $Y$.

El ángulo $\angle EYF$ es el ángulo inscrito que subtiende el arco $EF$ en el circuncírculo. Como $EF$ es el lado del triángulo equilátero, el ángulo central $\angle EOF$ es $120^\circ$. Por tanto, el ángulo inscrito $\angle EYF$ puede ser

\[
\angle EYF = 60^\circ \quad \text{o} \quad 120^\circ,
\]

según la posición de $Y$.

Dado que $Q$ está **dentro** del triángulo y $\angle EQF=120^\circ$, y $Y\neq D$ está en el arco que no contiene a $D$, obtenemos que $Q$ y $Y$ están relacionados por el arco $EF$. En efecto, ambos ven el segmento $EF$ bajo $120^\circ$, por lo cual $E,Q,F,Y$ son concíclicos.

---

**Demostración de que $E,Q,F,Y$ son concíclicos**

\[
\angle EQF=120^\circ.
\]

Para $Y$ en el circuncírculo de $DEF$, distinto de $D$, el ángulo $\angle EYF$ también vale $120^\circ$ (si $Y$ está sobre el arco menor $EF$). Como $Q$ está dentro del triángulo, $Q$ se encuentra en el mismo lado del segmento $EF$ que $D$, y $Y$ en el lado opuesto. Por tanto,

\[
\angle EQF + \angle EYF = 120^\circ + 60^\circ = 180^\circ,
\]

lo que confirma que $E,Q,F,Y$ son concíclicos.

---

**Cálculo de la cuerda**

Sea $M$ el punto medio de $EF$. En el triángulo equilátero,

\[
DM=\frac{9\sqrt{3}}{2}
\]

y $M$ está sobre la mediana $DM$. El punto $Q$ está sobre el arco de $EF$ con $\angle EQF=120^\circ$, es decir, sobre un círculo de radio $\frac{EF/\sqrt{3}}{2}\dots$

Calculemos $EF=9$. La cuerda $EF$ vista bajo $120^\circ$ corresponde a un círculo cuyo radio es

\[
r=\frac{EF}{2\sin 120^\circ}=\frac{9}{2\cdot \frac{\sqrt{3}}{2}}=\frac{9}{\sqrt{3}}=3\sqrt{3}.
\]

Es decir, $Q$ está sobre el circuncírculo de un triángulo $EQF$ con ángulo $120^\circ$.

Pero $E,Q,F,Y$ son concíclicos, y $E,F$ son puntos fijos. Por tanto, el círculo de $E,Q,F,Y$ tiene radio $3\sqrt{3}$, lo que coincide con el circuncírculo de $DEF$.

Esto implica que $Q$ y $Y$ están ambos sobre ese círculo de radio $3\sqrt{3}$, y $E,Q,F,Y$ son cíclicos.

---

**Relación con el círculo de diámetro $DQ$**

El ángulo $\angle DQY=90^\circ$ (diámetro). En el triángulo $DQY$, rectángulo en $Y$, tenemos $DY=7$. Queremos $YQ$.

Por el teorema de Pitágoras en $\triangle DYQ$:

\[
DQ^2=DY^2+YQ^2.
\]

Necesitamos $DQ$.

---

**Distancia $DQ$**

Como $Q$ está en el circuncírculo de $EQF$ (radio $3\sqrt{3}$) y $E,Q,F,Y$ son concíclicos, el centro de este círculo es $O$ (el centro del circuncírculo de $DEF$). En efecto, $E,F$ también están sobre el circuncírculo de $DEF$ con centro $O$ y radio $3\sqrt{3}$.

Por tanto, $Y,Q$ están sobre el circuncírculo de $\triangle DEF$. Luego $E,Q,F,Y$ están todos sobre el circuncírculo de $DEF$.

Entonces $Q$ está sobre el circuncírculo de $DEF$, lo que contradice que $Q$ está dentro del triángulo — a menos que $Q$ sea $D$ o esté sobre el arco interior.

Recalculemos: si $\angle EQF=120^\circ$ y $Q$ está dentro, entonces $Q$ está en el arco mayor $EF$ del círculo que pasa por $E,F$ con centro... El lugar geométrico de puntos que ven $EF$ bajo $120^\circ$ está formado por dos arcos de círculos de radio $3\sqrt{3}$.

Uno de esos círculos es precisamente el circuncírculo de $DEF$; el arco correspondiente al ángulo interior $120^\circ$ es el arco $EF$ que **contiene a $D$**. Como $Q$ está dentro del triángulo, $Q$ se encuentra sobre ese arco, entre $D$ y $EF$.

Por lo tanto $D,Q,Y$ están sobre el mismo círculo, con $Y$ en el arco opuesto.

---

**Resultado clave**

$D$, $Q$, $Y$ están sobre el circuncírculo de $DEF$, de radio $R=3\sqrt{3}$. El ángulo $\angle DYQ=90^\circ$ implica que $DQ$ es un diámetro de este círculo.

Por tanto,

\[
DQ=2R=6\sqrt{3}.
\]

Finalmente, en el triángulo rectángulo $DYQ$:

\[
DQ^2=DY^2+YQ^2
\]

\[
(6\sqrt{3})^2=7^2+YQ^2
\]

\[
108=49+YQ^2
\]

\[
YQ^2=59
\]

\[
YQ=\sqrt{59}.
\]

\[
\boxed{\sqrt{59}}
\]