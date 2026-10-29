Sea \(S_n\) el total de camarones acumulados tras el día \(n\).

El día en que la piel se vuelve rosa es el primer día en que \(S_n\ge 10\). Como ese día Pinky come \(1\) o \(2\) camarones, y antes de ese día tenía a lo sumo \(9\), ese día termina con \(10\) o con \(11\) camarones.

No se enferma ese día si y solo si termina con exactamente \(10\).

Definimos \(p_k\) como la probabilidad de alcanzar \(10\) antes que \(11\), partiendo de \(k\) camarones acumulados (\(0\le k\le 9\)). Tenemos:

\[
p_{10}=1,\qquad p_{11}=0
\]

Y la recurrencia:

\[
p_k=\frac12 p_{k+1}+\frac12 p_{k+2}
\]

Calculando hacia atrás:

\[
p_9=\frac12
\]

\[
p_8=\frac12\cdot\frac12+\frac12\cdot1=\frac34
\]

\[
p_7=\frac12\cdot\frac34+\frac12\cdot\frac12=\frac58
\]

\[
p_6=\frac{11}{16},\quad
p_5=\frac{21}{32},\quad
p_4=\frac{43}{64},\quad
p_3=\frac{85}{128},\quad
p_2=\frac{171}{256},\quad
p_1=\frac{341}{512}
\]

Finalmente:

\[
p_0=\frac12\cdot\frac{341}{512}+\frac12\cdot\frac{171}{256}
=\frac{683}{1024}
\]

\[
\boxed{\frac{683}{1024}}
\]