Paso 1: interpretar la condición. Para cada primo \(p\), se pide que \(f\pmod p\) se pueda escribir como \(g_p h_p\) con \(\deg g_p,\deg h_p<4\). Como \(f\) es mónico de grado \(4\), esto equivale a que \(f\) sea reducible módulo \(p\).

Paso 2: si \(f\) ya es reducible en \(\mathbb Z[x]\), entonces es splitty automáticamente. Factorizando
\[
x^4+16x^2+n=(x^2+ax+b)(x^2+cx+d),
\]
comparando coeficientes se obtiene \(c=-a\) y:
- si \(a=0\), entonces \(b+d=16\) y \(bd=n\), lo que da
\[
n=15,28,39,48,55,60,63,64;
\]
- si \(b=d\), entonces \(n=b^2\) y \(2b-a^2=16\), lo que con \(n\le100\) da \(n=64\) o \(n=100\).

Así, los valores reducibles son
\[
\{15,28,39,48,55,60,63,64,100\}.
\]

Paso 3: si \(f\) es irreducible en \(\mathbb Q[x]\), su grupo de Galois es un subgrupo transitivo de \(D_4\). Por Chebotarev, existen infinitos primos para los que \(f\) es irreducible módulo \(p\) si \(f\) tiene un \(4\)-ciclo en su grupo de Galois. Los subgrupos transitivos de \(D_4\) son \(V_4,C_4,D_4\), y solo \(V_4\) no contiene \(4\)-ciclos. Por tanto, en el caso irreducible, \(f\) es splitty si y solo si su grupo de Galois es \(V_4\).

El grupo es \(V_4\) exactamente cuando el discriminante de \(f\) es un cuadrado. Para \(x^4+Ax^2+B\),
\[
\Delta=16B(A^2-4B)^2.
\]
Con \(A=16,B=n\):
\[
\Delta=16n(256-4n)^2=256n(64-n)^2.
\]
Esto es un cuadrado perfecto si y solo si \(n\) es un cuadrado perfecto.

Por lo tanto, además de los reducibles, sirven todos los cuadrados perfectos \(n\le100\):
\[
1,4,9,16,25,36,49,64,81,100.
\]

Los valores splitty son la unión de los cuadrados perfectos y la lista reducible no cuadrada:
\[
\{1,4,9,16,25,36,49,64,81,100\}\cup\{15,28,39,48,55,60,63\}.
\]
La suma de los cuadrados es
\[
1^2+\cdots+10^2=385,
\]
y la suma de los reducibles no cuadrados es
\[
15+28+39+48+55+60+63=308.
\]
Total:
\[
385+308=693.
\]

\[
\boxed{693}
\]