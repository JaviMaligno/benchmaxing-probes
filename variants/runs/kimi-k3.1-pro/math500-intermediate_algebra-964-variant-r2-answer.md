Sea \(f_i(j)=g(i,j)\). Para cada \(i\ge1\),
\[
f_i(0)=f_{i-1}(2),\qquad f_i(j)=f_{i-1}(f_i(j-1)).
\]
Calculamos sucesivamente las filas \((f_i(0),\dots,f_i(4))\):
\[
\begin{aligned}
f_0&=(1,2,3,4,0),\\
f_1&=(3,4,0,1,2),\\
f_2&=(0,3,1,4,2),\\
f_3&=(1,3,4,2,1),\\
f_4&=(4,1,3,2,4),\\
f_5&=(3,2,3,2,3).
\end{aligned}
\]
Al aplicar la misma recurrencia a \(f_5\), obtenemos \(f_6=f_5\). Por inducción, \(f_i=f_5\) para todo \(i\ge5\). En particular,
\[
g(2024,3)=f_{2024}(3)=f_5(3)=\boxed{2}.
\]