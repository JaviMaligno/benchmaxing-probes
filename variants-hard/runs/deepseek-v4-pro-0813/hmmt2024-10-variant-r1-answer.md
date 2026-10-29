Let \(f_n(x)=x^4+20x^2+n\).

La condición equivale a que, para todo primo \(p\), la reducción de \(f_n\) módulo \(p\) sea reducible en \(\mathbb F_p[x]\).

**1. Reducibilidad sobre \(\mathbb Z\).**
Como \(f_n\) no tiene raíces reales para \(n>0\), si es reducible debe factorizar como
\[
f_n=(x^2+ax+b)(x^2+cx+d).
\]
Comparando coeficientes:
\[
a+c=0,\qquad ac+b+d=20,\qquad ad+bc=0,\qquad bd=n.
\]
De \(c=-a\) y \(a(d-b)=0\):
- Si \(a=0\), entonces \(b+d=20\) y \(bd=n\), luego \(n=b(20-b)\) para \(1\le b\le 19\).
- Si \(a\neq 0\), entonces \(b=d\) y \(a^2=2b-20\). Además \(b^2=n\le 100\), lo que fuerza \(b=10\) y \(a=0\), contradicción.

Así, los \(n\leq 100\) para los que \(f_n\) es reducible sobre \(\mathbb Z\) son
\[
S=\{19,36,51,64,75,84,91,96,99,100\}.
\]

**2. Caso irreducible.**
Si \(n\notin S\), \(f_n\) es irreducible. Para una cuártica irreducible, \(f_n\) es reducible módulo todo primo si y solo si su discriminante es un cuadrado perfecto: esto equivale a que su grupo de Galois esté contenido en \(A_4\), es decir, que no contenga ningún \(4\)-ciclo.

El discriminante de \(x^4+20x^2+n\) es
\[
\Delta=16n(400-4n)^2=256n(100-n)^2.
\]
Como \(256\) y \((100-n)^2\) son cuadrados, \(\Delta\) es cuadrado perfecto si y solo si \(n\) lo es.

Por tanto, los \(n\) breakables son exactamente
\[
S\cup\{k^2:1\le k\le 10\}.
\]

Los cuadrados suman
\[
1+4+\cdots+100=385.
\]
Los elementos no cuadrados de \(S\) suman
\[
19+51+75+84+91+96+99=515.
\]
Por lo tanto, la suma pedida es
\[
385+515=900.
\]

\[
\boxed{900}
\]