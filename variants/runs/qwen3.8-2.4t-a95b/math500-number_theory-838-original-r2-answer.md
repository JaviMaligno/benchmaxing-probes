

Primero factorizamos \(10!\):

\[
10! = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7^1
\]

Si \(x^3\) es un factor positivo de \(10!\), entonces cada exponente en la factorización prima de \(x^3\) debe ser menor o igual que el exponente correspondiente en \(10!\).

Sea

\[
x = 2^a 3^b 5^c 7^d \cdots
\]

Entonces

\[
x^3 = 2^{3a} 3^{3b} 5^{3c} 7^{3d} \cdots
\]

Necesitamos:

\[
3a \le 8 \Rightarrow a \le 2
\]

\[
3b \le 4 \Rightarrow b \le 1
\]

\[
3c \le 2 \Rightarrow c = 0
\]

\[
3d \le 1 \Rightarrow d = 0
\]

Por lo tanto, \(x\) solo puede tener factores primos \(2\) y \(3\), con

\[
x = 2^a 3^b
\]

donde \(a \in \{0,1,2\}\) y \(b \in \{0,1\}\).

El número de posibilidades es

\[
3 \cdot 2 = 6
\]

\[
\boxed{6}
\]