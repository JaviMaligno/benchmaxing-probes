Sea \(N=1000a+b\), con \(0\le a,b\le 999\). Como  
\[
1000\equiv -1 \pmod{91},
\]
se tiene
\[
N\equiv b-a \pmod{91}.
\]
Luego \(91\mid N\) si y solo si \(a\equiv b\pmod{91}\).

Para cada \(x\in[0,999]\), sea \(f(x)\) la suma de sus dígitos impares, representándolo con tres cifras. La contribución de cada par \((a,b)\) con \(a\equiv b\pmod{91}\) es \(f(a)+f(b)\).

En \([0,999]\), hay
- \(11\) números por cada residuo \(0,1,\dots,89\pmod{91}\),
- \(10\) números en el residuo \(90\).

Si \(x=100h+10t+u\), entonces
\[
x\equiv 9h+10t+u \pmod{91}.
\]
Sea \(v=9h+10t+u\). Salvo cuando \(v=90\), el residuo correspondiente tiene \(11\) números; solo \(v=90\) tiene \(10\).

Primero,
\[
\sum_{x=0}^{999} f(x)=3\cdot 100(1+3+5+7+9)=7500.
\]

Los casos con \(v=90\) son
\[
9h+10t+u=90 \implies (h,t,u)=(h,9-h,h),\quad h=0,\dots,9.
\]
En esos \(10\) casos, cada posición recorre una vez los dígitos \(0,\dots,9\), así que su suma de dígitos impares es
\[
3(1+3+5+7+9)=75.
\]

Por tanto,
\[
\sum_{a\equiv b} f(a)=11\cdot 7500-75=82425.
\]
Como el total es \(f(a)+f(b)\), el resultado es
\[
2\cdot 82425=164850.
\]

\[
\boxed{164850}
\]