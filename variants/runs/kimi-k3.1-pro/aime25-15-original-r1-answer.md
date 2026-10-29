Como \((a+3^6)^3\equiv a^3\pmod{3^7}\), podemos considerar \(a,b,c\) como residuos módulo \(729\). Cada residuo corresponde a exactamente un entero del intervalo \(1,\dots,729\).

### 1. Distribución de los cubos

Clasificamos \(a\) según \(v_3(a)\). Usando que los cubos de unidades módulo \(3^k\) son precisamente los residuos \(\equiv\pm1\pmod9\), obtenemos:

\[
\begin{array}{c|c|c}
v_3(a)&\text{posibles valores de }a^3\pmod{2187}&\text{multiplicidad}\\ \hline
0&\varepsilon+9t,\quad \varepsilon=\pm1,\ t\in\mathbb Z/243\mathbb Z&1\\
1&27(\varepsilon+9t),\quad \varepsilon=\pm1,\ t\in\mathbb Z/9\mathbb Z&9\\
2&729\varepsilon,\quad \varepsilon=\pm1&27\\
\ge3&0&27
\end{array}
\]

La última columna indica cuántos valores de \(a\) producen cada cubo.

### 2. Soluciones con exactamente dos unidades

Todo cubo de una unidad es \(\equiv\pm1\pmod9\), mientras que los demás cubos son \(\equiv0\pmod9\). Por tanto:

- con una sola unidad no hay soluciones;
- con tres unidades tampoco, pues una suma de tres signos \(\pm1\) nunca es \(0\pmod9\);
- con dos unidades, sus signos deben ser opuestos.

Fijemos las posiciones y los signos; hay \(3\cdot2=6\) elecciones. Los dos cubos son
\[
1+9t,\qquad -1+9u,\qquad t,u\in\mathbb Z/243\mathbb Z.
\]
El tercer cubo, proveniente de un no unitario, se escribe como \(27v\), con \(v\in\mathbb Z/81\mathbb Z\). La condición es
\[
9(t+u)+27v\equiv0\pmod{2187}
\iff t+u+3v\equiv0\pmod{243}.
\]
Para cada \(v\), hay \(243\) pares \((t,u)\). Si \(W(v)\) es el número de no unitarios cuyo cubo es \(27v\), entonces
\[
\sum_{v\bmod81}W(v)=243.
\]
Así, para posiciones y signos fijos, hay \(243\cdot243=59049\) soluciones. En total:
\[
N_{\mathrm{2\ unidades}}=6\cdot59049=354294.
\]

### 3. Soluciones sin unidades

Ahora todos los valores son divisibles por \(3\).

**Exactamente dos valores con valuación \(1\).**  
Después de factorizar \(27\), sus cubos tienen la forma \(\varepsilon+9t\pmod{81}\). Deben tener signos opuestos. El tercer término reducido es \(0,27\) o \(-27\), cada uno con multiplicidad \(27\).

Para posiciones y signos fijos, el número de soluciones es
\[
3\cdot9\cdot9^2\cdot27=59049.
\]
Por tanto, este caso aporta
\[
6\cdot59049=354294.
\]
Con uno o tres valores de valuación \(1\), la obstrucción módulo \(9\) impide soluciones.

**Ningún valor con valuación \(1\).**  
Cada término es \(0\) o \(\pm729\), con \(27\) elecciones para cada posibilidad. Las combinaciones válidas son:

- todas nulas: \(1\) patrón;
- exactamente dos términos no nulos, con signos opuestos: \(6\) patrones;
- tres términos no nulos del mismo signo: \(2\) patrones.

Aportan
\[
27^3(1+6+2)=177147.
\]

### 4. Total

\[
N=354294+354294+177147=885735.
\]
Por consiguiente, el residuo solicitado es

\[
\boxed{735}
\]