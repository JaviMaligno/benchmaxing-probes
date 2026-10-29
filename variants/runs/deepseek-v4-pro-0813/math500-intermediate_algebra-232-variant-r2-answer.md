Queremos contar pares ordenados de enteros \((x,y)\) tales que

\[
|x+yi|=\sqrt{x^2+y^2}\le 6,
\]

es decir,

\[
x^2+y^2\le 36.
\]

Para cada entero \(x\) entre \(-6\) y \(6\), los posibles valores de \(y\) son los enteros que cumplen

\[
y^2\le 36-x^2.
\]

Entonces la cantidad de valores de \(y\) para cada \(x\) es

\[
2\left\lfloor \sqrt{36-x^2}\right\rfloor+1.
\]

Calculamos por simetría:

- \(x=0\): \(\sqrt{36}=6\), da \(13\) valores.
- \(x=\pm 1\): \(\sqrt{35}\), parte entera \(5\), da \(11\).
- \(x=\pm 2\): \(\sqrt{32}\), parte entera \(5\), da \(11\).
- \(x=\pm 3\): \(\sqrt{27}\), parte entera \(5\), da \(11\).
- \(x=\pm 4\): \(\sqrt{20}\), parte entera \(4\), da \(9\).
- \(x=\pm 5\): \(\sqrt{11}\), parte entera \(3\), da \(7\).
- \(x=\pm 6\): \(\sqrt{0}=0\), da \(1\).

Sumamos:

\[
13+2(11+11+11+9+7+1)=13+2(50)=113.
\]

\[
\boxed{113}
\]