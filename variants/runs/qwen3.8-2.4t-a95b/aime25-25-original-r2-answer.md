

Representamos los asientos como una cadena binaria de longitud 16, donde 1 indica silla ocupada y 0 indica silla vacía.

Hay 8 sillas ocupadas y 8 vacías. La condición “ninguna persona se sienta junto a otras dos personas” equivale a prohibir tres sillas ocupadas consecutivas, es decir, no puede aparecer el patrón \(111\).

Las 8 sillas vacías crean 9 espacios donde pueden ir sillas ocupadas:

\[
\_ 0 \_ 0 \_ 0 \_ 0 \_ 0 \_ 0 \_ 0 \_ 0 \_
\]

En cada espacio puede haber 0, 1 o 2 sillas ocupadas, pero no 3. Necesitamos colocar en total 8 sillas ocupadas.

Sea \(j\) el número de espacios con exactamente 2 sillas ocupadas. Entonces debemos tener \(8-2j\) espacios con exactamente 1 silla ocupada. Como máximo \(j=4\).

Contamos para cada \(j\):

\[
\sum_{j=0}^{4} \binom{9}{j}\binom{9-j}{8-2j}
\]

Calculamos:

\[
j=0:\ \binom{9}{0}\binom{9}{8}=9
\]

\[
j=1:\ \binom{9}{1}\binom{8}{6}=9\cdot 28=252
\]

\[
j=2:\ \binom{9}{2}\binom{7}{4}=36\cdot 35=1260
\]

\[
j=3:\ \binom{9}{3}\binom{6}{2}=84\cdot 15=1260
\]

\[
j=4:\ \binom{9}{4}\binom{5}{0}=126\cdot 1=126
\]

Sumando:

\[
N=9+252+1260+1260+126=2907
\]

Finalmente,

\[
2907 \equiv 907 \pmod{1000}
\]

\[
\boxed{907}
\]