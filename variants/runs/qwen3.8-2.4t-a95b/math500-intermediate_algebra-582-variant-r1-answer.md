

Sea
\[
x^{10}+(11x-1)^{10}=0.
\]
Como \(x=\frac1{11}\) no es raíz, podemos dividir por \((11x-1)^{10}\):
\[
\left(\frac{x}{11x-1}\right)^{10}=-1.
\]
Sea \(\omega\) una raíz décima de \(-1\), es decir \(\omega^{10}=-1\). Entonces
\[
\frac{x}{11x-1}=\omega
\]
y por tanto
\[
x=\frac{\omega}{11\omega-1}.
\]

Las 10 raíces del polinomio corresponden a las 10 raíces \(\omega\) de \(\omega^{10}+1=0\). Como \(|\omega|=1\), para una raíz \(x\) tenemos
\[
x\overline{x}=|x|^2
=\left|\frac{\omega}{11\omega-1}\right|^2
=\frac{1}{|11\omega-1|^2}.
\]
Luego
\[
\frac1{x\overline{x}}=|11\omega-1|^2.
\]
Ahora
\[
|11\omega-1|^2=(11\omega-1)(11\overline{\omega}-1)
=121|\omega|^2-11(\omega+\overline{\omega})+1.
\]
Como \(|\omega|=1\),
\[
\frac1{x\overline{x}}=122-11(\omega+\overline{\omega})
=122-22\operatorname{Re}(\omega).
\]

Las 10 raíces \(\omega\) de \(\omega^{10}+1=0\) tienen suma \(0\), por lo que
\[
\sum_{\omega^{10}=-1}\operatorname{Re}(\omega)=0.
\]
Así, sumando sobre las 10 raíces \(x\),
\[
\sum \frac1{x\overline{x}}
=10\cdot 122-22\cdot 0=1220.
\]
Esta suma cuenta cada par conjugado dos veces, mientras que la suma pedida toma solo un representante de cada par. Por lo tanto,
\[
\frac 1{s_1\overline{s}_1}+\cdots+\frac 1{s_5\overline{s}_5}
=\frac{1220}{2}=610.
\]

\[
\boxed{610}
\]