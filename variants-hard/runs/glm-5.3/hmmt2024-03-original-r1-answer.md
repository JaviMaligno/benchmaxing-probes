Sean
\[
N=\overline{abc}=100a+10b+c,\qquad M=\overline{bca}=100b+10c+a.
\]
Entonces
\[
10N=1000a+100b+10c=(100b+10c+a)+999a=M+999a,
\]
de modo que
\[
M=10N-999a.
\]

Supongamos que \(x\) cumple la propiedad. Si \(N\) es múltiplo de \(x\), entonces \(M\) también lo es, y por lo tanto
\[
x\mid (10N-M)=999a.
\]

Tomando \(a=1\): todo \(x\) de dos cifras tiene algún múltiplo entre \(110\) y \(199\) con \(b\neq 0\). Para ese múltiplo, la condición obliga a que
\[
x\mid 999.
\]

Recíprocamente, si \(x\mid 999\), entonces \(x\mid 999a\) para cada dígito \(a\). Así, para cualquier múltiplo \(N\) de \(x\),
\[
M=10N-999a
\]
es diferencia de dos múltiplos de \(x\), luego también es múltiplo de \(x\). Por lo tanto, exactamente los divisores de dos cifras de \(999\) funcionan.

Ahora,
\[
999=3^3\cdot 37,
\]
cuyos divisores de dos cifras son \(27\) y \(37\). Su suma es \(27+37=64\).

\[
\boxed{64}
\]