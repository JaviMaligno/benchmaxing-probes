Como la asignación de etiquetas es arbitraria, basta considerar todas las ordenaciones posibles de los seis puntos.

Sea
\[
C_1=(0,0),\quad C_2=(10,0),\quad C_3=(10,10),\quad C_4=(0,10),
\]
y sean los puntos interiores
\[
P=(3,4),\quad Q=(6,2).
\]
En un polígono simple, los vértices de la envolvente convexa deben aparecer en su orden cíclico; sin pérdida de generalidad, tomamos
\[
C_1,C_2,C_3,C_4
\]
en sentido antihorario. Así, \(P\) y \(Q\) solo pueden insertarse en las cuatro cadenas entre esquinas consecutivas.

El área del cuadrado es \(100\). Si un punto \(Z=(x,y)\) se inserta solo, la pérdida de área respecto al cuadrado es:

\[
\begin{array}{c|c}
\text{cadena} & \text{pérdida}\\ \hline
C_1ZC_2 & 5y\\
C_2ZC_3 & 5(10-x)\\
C_3ZC_4 & 5(10-y)\\
C_4ZC_1 & 5x
\end{array}
\]

Entonces, para \(P\) y \(Q\):

\[
\begin{array}{c|cccc}
 & C_1C_2 & C_2C_3 & C_3C_4 & C_4C_1\\ \hline
P & 20 & 35 & 30 & 15\\
Q & 10 & 20 & 40 & 30
\end{array}
\]

Si ambos puntos están en la misma cadena, usando la fórmula del área por determinantes se obtienen las pérdidas:

\[
\begin{array}{c|cc}
\text{cadena} & \text{orden }P,Q & \text{orden }Q,P\\ \hline
C_1C_2 & 19 & 11\\
C_2C_3 & 19 & 36\\
C_3C_4 & 24 & 46\\
C_4C_1 & 24 & 21
\end{array}
\]

Para el máximo, la menor pérdida posible es \(11\), lograda con
\[
C_1,Q,P,C_2,C_3,C_4.
\]
Este hexágono es simple, así que
\[
a_{\max}=100-11=89.
\]

Para el mínimo, buscamos la mayor pérdida que dé un hexágono simple. Si \(P,Q\) están en la misma cadena, la pérdida es a lo más \(46\). Si están en cadenas distintas, los únicos casos con pérdida mayor que \(55\) son:

\[
\begin{array}{c|c}
\text{caso} & \text{pérdida}\\ \hline
P\text{ en }C_2C_3,\ Q\text{ en }C_3C_4 & 75\\
P\text{ en }C_2C_3,\ Q\text{ en }C_4C_1 & 65\\
P\text{ en }C_1C_2,\ Q\text{ en }C_3C_4 & 60
\end{array}
\]

Pero esos tres casos se autointersecan: por ejemplo, \(PC_3\) corta a \(QC_4\) en \(\left(\frac{90}{23},\frac{110}{23}\right)\), y en el tercer caso \(PC_2\) corta a \(QC_4\) en \(\left(\frac{45}{8},\frac52\right)\).

La mayor pérdida viable es entonces \(55\), lograda con
\[
C_1,C_2,C_3,Q,C_4,P.
\]
Su área es
\[
a_{\min}=100-55=45.
\]

Por lo tanto,
\[
a_{\max}-a_{\min}=89-45=44.
\]

\boxed{44}