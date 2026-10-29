

Sea
\[
w_k=\frac{2y_k-1}{y_k+1}.
\]
Entonces, como
\[
y_{k+1}=\frac{y_k^2-y_k+1}{3y_k},
\]
tenemos
\[
2y_{k+1}-1=\frac{2y_k^2-5y_k+2}{3y_k}
=\frac{(2y_k-1)(y_k-2)}{3y_k},
\]
y
\[
y_{k+1}+1=\frac{y_k^2+2y_k+1}{3y_k}
=\frac{(y_k+1)^2}{3y_k}.
\]
Por tanto,
\[
w_{k+1}
=\frac{2y_{k+1}-1}{y_{k+1}+1}
=\frac{(2y_k-1)(y_k-2)}{(y_k+1)^2}
=w_k(w_k-1).
\]

Además,
\[
w_1=\frac{2\cdot \frac{19}{14}-1}{\frac{19}{14}+1}
=\frac{8}{11}.
\]

Escribamos \(w_k=\frac{A_k}{B_k}\) en forma reducida, con \(B_k>0\). Entonces
\[
w_{k+1}=\frac{A_k(A_k-B_k)}{B_k^2}.
\]
Como \(\gcd(A_k,B_k)=1\), también \(\gcd(A_k-B_k,B_k)=1\), así que la fracción sigue reducida y
\[
B_{k+1}=B_k^2.
\]
Como \(B_1=11\), se sigue que
\[
B_k=11^{2^{k-1}}.
\]

Ahora despejamos \(y_k\) de \(w_k\):
\[
w_k=\frac{2y_k-1}{y_k+1}
\implies
y_k=\frac{w_k+1}{2-w_k}
=\frac{A_k+B_k}{2B_k-A_k}.
\]
Esta fracción está reducida: si \(d\) divide a \(A_k+B_k\) y a \(2B_k-A_k\), entonces \(d\) divide a
\[
(A_k+B_k)+(2B_k-A_k)=3B_k
\]
y a
\[
2(A_k+B_k)-(2B_k-A_k)=3A_k.
\]
Como \(\gcd(A_k,B_k)=1\), resulta \(d\mid 3\). Pero \(A_1+B_1=19\) no es divisible entre \(3\), y para \(k\ge 2\), \(A_k\equiv 0\pmod 3\) mientras que \(B_k\not\equiv 0\pmod 3\), así que \(3\nmid A_k+B_k\). Por tanto \(d=1\).

Luego
\[
m=A_k+B_k,\qquad n=2B_k-A_k,
\]
y
\[
m+n=3B_k=3\cdot 11^{2^{k-1}}.
\]
Para \(k=2025\),
\[
m+n=3\cdot 11^{2^{2024}}.
\]

Queremos esto módulo \(1000\). Como \(\varphi(1000)=400\) y \(\gcd(11,1000)=1\), reducimos el exponente módulo \(400\):
\[
2^{2024}\equiv 16 \pmod{400}.
\]
Así,
\[
11^{2^{2024}}\equiv 11^{16}\pmod{1000}.
\]
Calculamos:
\[
11^4\equiv 641,\qquad
11^8\equiv 881,\qquad
11^{16}\equiv 161\pmod{1000}.
\]
Por tanto,
\[
3\cdot 11^{2^{2024}}\equiv 3\cdot 161=483\pmod{1000}.
\]

\[
\boxed{483}
\]