

Sea \(v_p(x)\) el exponente del primo \(p\) en \(x\). El exponente de \(p\) en \(D\) es

\[
e_p=\min_{n>2024} v_p(Q(n)).
\]

Como cada clase de congruencia módulo cualquier entero contiene infinitos \(n>2024\), podemos trabajar libremente con clases de residuos.

---

### 1. Qué primos pueden dividir a \(D\)

Para que un primo \(p\) divida siempre a

\[
Q(n)=\prod_{k=1}^{45}(n-k^3),
\]

es necesario que, para cada residuo \(r \pmod p\), exista algún \(k\in\{1,\dots,45\}\) tal que

\[
k^3\equiv r \pmod p.
\]

Es decir, los cubos \(k^3\) deben cubrir todos los residuos módulo \(p\).

En \(\mathbb{F}_p^\times\), la función \(x\mapsto x^3\) es biyectiva si y solo si

\[
\gcd(3,p-1)=1,
\]

es decir, si \(p\not\equiv 1 \pmod 3\). Si \(p\equiv 1\pmod 3\), los cubos no cubren todos los residuos, así que ese primo no puede dividir a \(D\).

Además, si \(p>45\), solo hay 45 valores \(k^3\), por lo que tampoco pueden cubrir todos los residuos módulo \(p\).

Por tanto, los únicos primos posibles son los primos \(p\le 45\) con \(p\not\equiv 1\pmod 3\):

\[
2,3,5,11,17,23,29,41.
\]

---

### 2. Exponente de cada uno de esos primos

Para uno de estos primos \(p\), la función \(x\mapsto x^3\) es biyectiva módulo \(p\). Dado cualquier \(n\), existe un único residuo \(c\pmod p\) tal que

\[
c^3\equiv n\pmod p.
\]

Entonces los factores divisibles por \(p\) son exactamente aquellos con

\[
k\equiv c\pmod p.
\]

Entre \(1,2,\dots,45\), cada clase módulo \(p\) aparece al menos

\[
\left\lfloor \frac{45}{p}\right\rfloor
\]

veces. Luego

\[
v_p(Q(n))\ge \left\lfloor \frac{45}{p}\right\rfloor.
\]

Para ver que no hay ninguna potencia superior garantizada, tomemos

\[
n\equiv p\pmod{p^2},
\]

con \(n>2024\). Entonces \(v_p(n)=1\).

- Si \(p\nmid k\), entonces \(k^3\not\equiv 0\pmod p\), así que \(p\nmid (n-k^3)\).
- Si \(p\mid k\), entonces \(k^3\) es divisible por \(p^3\), y como \(v_p(n)=1\), se tiene

\[
v_p(n-k^3)=1.
\]

El número de \(k\le 45\) divisibles por \(p\) es precisamente \(\left\lfloor 45/p\right\rfloor\). Por tanto,

\[
v_p(Q(n))=\left\lfloor \frac{45}{p}\right\rfloor.
\]

Así,

\[
e_p=\left\lfloor \frac{45}{p}\right\rfloor.
\]

---

### 3. Suma de exponentes

\[
\begin{array}{c|c}
p & \left\lfloor 45/p\right\rfloor \\ \hline
2 & 22\\
3 & 15\\
5 & 9\\
11 & 4\\
17 & 2\\
23 & 1\\
29 & 1\\
41 & 1
\end{array}
\]

Por tanto,

\[
m=22+15+9+4+2+1+1+1=55.
\]

\[
\boxed{55}
\]