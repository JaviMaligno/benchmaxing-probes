

Tenemos \(|x+yi|=\sqrt{x^2+y^2}\), así que la condición es

\[
x^2+y^2 \le 36.
\]

Contamos los pares enteros \((x,y)\) fijando \(x\) y contando los valores posibles de \(y\).

Para cada \(x\), se necesita

\[
y^2 \le 36-x^2,
\]

por lo que el número de enteros \(y\) es

\[
2\left\lfloor \sqrt{36-x^2}\right\rfloor+1.
\]

Como \(x^2\le 36\), tenemos \(x=-6,-5,\dots,6\).

- \(x=0\): \(\lfloor\sqrt{36}\rfloor=6\), hay \(2\cdot 6+1=13\).
- \(x=\pm1\): \(\lfloor\sqrt{35}\rfloor=5\), hay \(11\) para cada uno, total \(22\).
- \(x=\pm2\): \(\lfloor\sqrt{32}\rfloor=5\), total \(22\).
- \(x=\pm3\): \(\lfloor\sqrt{27}\rfloor=5\), total \(22\).
- \(x=\pm4\): \(\lfloor\sqrt{20}\rfloor=4\), hay \(9\) para cada uno, total \(18\).
- \(x=\pm5\): \(\lfloor\sqrt{11}\rfloor=3\), hay \(7\) para cada uno, total \(14\).
- \(x=\pm6\): \(\lfloor\sqrt{0}\rfloor=0\), hay \(1\) para cada uno, total \(2\).

Sumando:

\[
13+22+22+22+18+14+2=113.
\]

\[
\boxed{113}
\]