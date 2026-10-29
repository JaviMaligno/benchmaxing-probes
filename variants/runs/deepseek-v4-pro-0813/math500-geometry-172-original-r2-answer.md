Voy a resolver el problema paso a paso.

Sea el triángulo \(ABC\) con área 144. Las medianas \(AD\), \(BE\) y \(CF\) se cortan en el centroide \(G\). La recta por \(G\) paralela a \(BC\) corta a \(AB\) y \(AC\) en \(M\) y \(N\), respectivamente. Nos piden el área del triángulo \(ENG\).

**Paso 1: Ubicación del centroide**

El centroide \(G\) divide cada mediana en razón \(2:1\), de modo que:

\[
AG:GD = 2:1
\]

**Paso 2: La recta por \(G\) paralela a \(BC\)**

Como \(MN \parallel BC\), y \(G\) está sobre la mediana \(AD\), los triángulos \(AMN\) y \(ABC\) son semejantes (tienen lados correspondientes paralelos). Como \(G\) está a \(\frac{2}{3}\) de la altura desde \(A\) hacia \(BC\), la razón de semejanza es:

\[
\frac{AG}{AD} = \frac{2}{3}
\]

Por tanto, el área de \(AMN\) es:

\[
[AMN] = \left(\frac{2}{3}\right)^2 [ABC] = \frac{4}{9} \cdot 144 = 64
\]

**Paso 3: Posición de \(N\)**

\(N\) es el punto donde la recta por \(G\) paralela a \(BC\) corta a \(AC\). Como \(G\) está sobre la mediana \(AD\), que une \(A\) con el punto medio \(D\) de \(BC\), y \(MN \parallel BC\), se tiene:

\[
\frac{AN}{AC} = \frac{AG}{AD} = \frac{2}{3}
\]

Por tanto:

\[
CN = \frac{1}{3} AC
\]

**Paso 4: Triángulo \(ENG\)**

\(E\) es el punto medio de \(AC\), por ser \(BE\) la mediana. Entonces:

\[
AE = EC = \frac{1}{2} AC
\]

Como \(N\) está a \(\frac{2}{3}\) de \(AC\) desde \(A\), tenemos:

\[
AN = \frac{2}{3} AC, \qquad AE = \frac{1}{2} AC
\]

Luego:

\[
NE = AN - AE = \frac{2}{3} AC - \frac{1}{2} AC = \frac{1}{6} AC
\]

**Paso 5: Altura del triángulo \(ENG\)**

Como \(MN \parallel BC\), la recta \(EG\) no es horizontal en general. Necesitamos el área de \(ENG\) con base \(NE\) sobre \(AC\).

Observemos que \(G\) está sobre \(MN\), paralela a \(BC\). La distancia de \(G\) a \(AC\) es la altura del triángulo \(ENG\) respecto a la base \(NE\) (que está sobre \(AC\)).

Como \(MN \parallel BC\) y \(BC\) dista de \(A\) la altura \(h\) del triángulo \(ABC\), la recta \(MN\) está a distancia:

\[
\frac{2}{3} h
\]

de \(A\) y, por tanto, a distancia:

\[
h - \frac{2}{3} h = \frac{1}{3} h
\]

de \(BC\). Sin embargo, la altura del triángulo \(ENG\) respecto a la base \(NE\) no es esta distancia, porque la base \(NE\) está sobre \(AC\), no sobre \(BC\).

Necesitamos la distancia perpendicular de \(G\) a la recta \(AC\).

**Paso 6: Distancia de \(G\) a \(AC\)**

Consideremos la altura \(h_B\) desde \(B\) hasta \(AC\). El área del triángulo \(ABC\) es:

\[
[ABC] = \frac{1}{2} \cdot AC \cdot h_B = 144
\]

Como \(G\) divide la mediana \(BE\) en razón \(BG:GE = 2:1\), la distancia de \(G\) a \(AC\) es \(\frac{1}{3}\) de la distancia de \(B\) a \(AC\), pues \(G\) está a un tercio de \(E\) (que yace sobre \(AC\)) y a dos tercios de \(B\):

\[
d(G, AC) = \frac{1}{3} h_B
\]

**Paso 7: Cálculo del área de \(ENG\)**

La base es:

\[
NE = \frac{1}{6} AC
\]

La altura desde \(G\) hasta \(AC\) es:

\[
d(G, AC) = \frac{1}{3} h_B
\]

Por tanto:

\[
[ENG] = \frac{1}{2} \cdot NE \cdot d(G, AC)
\]

\[
[ENG] = \frac{1}{2} \cdot \frac{1}{6} AC \cdot \frac{1}{3} h_B
\]

\[
[ENG] = \frac{1}{36} \cdot \frac{1}{2} AC \cdot h_B
\]

Pero \(\frac{1}{2} AC \cdot h_B = [ABC] = 144\), luego:

\[
[ENG] = \frac{1}{36} \cdot 144 = 4
\]

**Respuesta final:**

\[
\boxed{4}
\]