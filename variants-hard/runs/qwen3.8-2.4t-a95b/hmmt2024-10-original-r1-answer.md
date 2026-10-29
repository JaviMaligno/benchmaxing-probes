

Sea  
\[
f_n(x)=x^4+16x^2+n.
\]
La condición “splitty” equivale a que, para cada primo \(p\), \(f_n\) se factorice en \(\mathbb{F}_p[x]\) como producto de dos polinomios de grado \(<4\); como \(f_n\) es mónico de grado \(4\), esto es simplemente que \(f_n\) es reducible módulo \(p\).

### 1. El primo \(p=2\)

Módulo \(2\),
\[
f_n(x)\equiv x^4+n \pmod 2.
\]
Si \(n\) es par, \(f_n(x)\equiv x^4\), reducible. Si \(n\) es impar,
\[
x^4+1=(x+1)(x^3+x^2+x+1)\quad\text{en }\mathbb{F}_2,
\]
también reducible. Así, \(p=2\) no impone ninguna restricción.

### 2. Criterio para primos impares

Para \(p\) impar, si \(f_n\) es reducible, por ser un polinomio par termina factorizando en dos cuadráticos mónicos. Escribamos
\[
x^4+16x^2+n=(x^2+ax+b)(x^2+cx+d).
\]
Comparando coeficientes:
\[
a+c=0,\qquad a(d-b)=0.
\]
Por tanto \(c=-a\), y hay dos casos.

- Si \(a=0\), entonces
  \[
  b+d=16,\qquad bd=n.
  \]
  Eso ocurre si y solo si el discriminante de \(T^2-16T+n\) es cuadrado en \(\mathbb{F}_p\), es decir, si
  \[
  256-4n=4(64-n)
  \]
  es cuadrado, equivalentemente \(64-n\) es cuadrado módulo \(p\).

- Si \(a\neq 0\), entonces \(d=b\), y
  \[
  b^2=n,\qquad 2b-a^2=16.
  \]
  En particular \(n\) es cuadrado módulo \(p\).

Recíprocamente:

- Si \(64-n=s^2\) en \(\mathbb{F}_p\), entonces
  \[
  f_n(x)=(x^2+8-s)(x^2+8+s).
  \]

- Si \(n=m^2\) en \(\mathbb{F}_p\), entonces o bien \(64-n\) es cuadrado, o bien
  \[
  (2m-16)(-2m-16)=4(64-n)
  \]
  no es cuadrado. En ese segundo caso, exactamente uno de \(2m-16\) y \(-2m-16\) es cuadrado, digamos \(r^2=2\varepsilon m-16\) con \(\varepsilon=\pm1\), y
  \[
  f_n(x)=(x^2+rx+\varepsilon m)(x^2-rx+\varepsilon m).
  \]

Por tanto, para todo primo impar \(p\),
\[
f_n \text{ es reducible módulo } p
\iff
n \text{ es cuadrado en } \mathbb{F}_p \text{ o } 64-n \text{ lo es}.
\]

### 3. Condición global

Para que \(f_n\) sea reducible módulo todo primo impar, necesitamos que para todo \(p\) impar al menos uno de \(n\) o \(64-n\) sea cuadrado módulo \(p\).

Usamos el hecho estándar: si dos enteros \(a,b\) no son cuadrados perfectos, existe algún primo impar \(p\) tal que ambos son no residuos cuadráticos módulo \(p\). Esto se sigue, por ejemplo, del teorema de Dirichlet sobre progresiones aritméticas.

Así, para que \(f_n\) sea splitty, al menos uno de
\[
n,\qquad 64-n
\]
debe ser un cuadrado perfecto en \(\mathbb{Z}\). Recíprocamente, si uno de ellos es cuadrado perfecto, entonces es cuadrado módulo todo \(p\), y \(f_n\) es reducible módulo todo primo.

### 4. Contar \(n\le 100\)

Los cuadrados positivos \(\le 100\) son
\[
1,4,9,16,25,36,49,64,81,100.
\]

Los \(n\) tales que \(64-n\) es cuadrado no negativo son
\[
64-d^2,\quad d=0,1,\dots,8.
\]
Los positivos son
\[
64,63,60,55,48,39,28,15.
\]

La unión es
\[
\{1,4,9,15,16,25,28,36,39,48,49,55,60,63,64,81,100\}.
\]

Su suma es
\[
(1+4+9+16+25+36+49+64+81+100)+(15+28+39+48+55+60+63).
\]
La primera parte es la suma de los primeros diez cuadrados:
\[
385.
\]
La segunda parte es
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