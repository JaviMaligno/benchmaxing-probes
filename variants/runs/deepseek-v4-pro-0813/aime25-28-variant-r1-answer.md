Escribimos \(y_k=\frac{p_k}{q_k}\) en forma irreducible. Entonces

\[
y_{k+1}=\frac{p_k^2+q_k^2-p_kq_k}{3p_kq_k}.
\]

Se comprueba por inducción que \(p_k\equiv 1\pmod 3\) y \(q_k\equiv 2\pmod 3\). Por tanto,

\[
p_k^2+q_k^2-p_kq_k\equiv 0\pmod 3,
\]

y la fracción queda reducida como

\[
p_{k+1}=\frac{p_k^2+q_k^2-p_kq_k}{3},\qquad q_{k+1}=p_kq_k.
\]

Trabajando módulo \(1000\), como \(3^{-1}\equiv 667\pmod{1000}\),

\[
p_{k+1}\equiv 667(p_k^2-p_kq_k+q_k^2)\pmod{1000},
\]
\[
q_{k+1}\equiv p_kq_k\pmod{1000}.
\]

Iterando obtenemos, módulo \(1000\):

\[
\begin{array}{c|ccccccccccc}
k&1&2&3&4&5&6&7&8&9&10&11&12\\
(p_k,q_k)&(19,14)&(97,266)&(121,802)&(601,42)&(241,242)&(441,322)&(721,2)&(801,442)&(641,42)&(241,922)&(321,202)&(1,842)
\end{array}
\]

\[
\begin{array}{c|ccccccccccc}
k&13&14&15&16&17&18&19&20&21&22&23\\
(p_k,q_k)&(41,842)&(41,522)&(921,402)&(201,242)&(441,642)&(841,122)&(521,602)&(401,642)&(841,442)&(641,722)&(121,802)
\end{array}
\]

Como \((p_{23},q_{23})=(121,802)=(p_3,q_3)\), a partir de \(k=3\) la sucesión tiene periodo \(20\).

Ahora,

\[
2025-3=2022\equiv 2\pmod{20}.
\]

Por tanto,

\[
(p_{2025},q_{2025})\equiv (p_5,q_5)\equiv (241,242)\pmod{1000}.
\]

Así,

\[
m+n\equiv p_{2025}+q_{2025}\equiv 241+242=483\pmod{1000}.
\]

\[
\boxed{483}
\]