

Para que la ecuación

\[
\log(kx)=2\log(x+2)
\]

tenga sentido real, necesitamos

\[
x+2>0 \quad\Longrightarrow\quad x>-2
\]

y además \(kx>0\).

Usando la propiedad \(2\log(x+2)=\log((x+2)^2)\), válida porque \(x+2>0\), la ecuación equivale a

\[
\log(kx)=\log((x+2)^2).
\]

Como el logaritmo es inyectivo,

\[
kx=(x+2)^2.
\]

Si \(k=0\), entonces \(\log(kx)=\log(0)\) no está definido, así que \(k=0\) no da soluciones.

Para \(k\neq 0\), podemos escribir

\[
k=\frac{(x+2)^2}{x}=x+4+\frac4x.
\]

Analicemos esta función según el signo de \(x\).

---

### 1. Caso \(x>0\)

\[
f(x)=x+4+\frac4x.
\]

Por AM-GM o derivando,

\[
f'(x)=1-\frac4{x^2}=0 \quad\Longrightarrow\quad x=2.
\]

El mínimo es

\[
f(2)=2+4+2=8.
\]

Además, \(f(x)\to\infty\) cuando \(x\to0^+\) y cuando \(x\to\infty\). Por tanto:

- si \(k<8\), no hay soluciones positivas;
- si \(k=8\), hay exactamente una solución positiva;
- si \(k>8\), hay dos soluciones positivas.

---

### 2. Caso \(-2<x<0\)

En este intervalo,

\[
f'(x)=1-\frac4{x^2}<0,
\]

así que \(f\) es estrictamente decreciente. Además,

\[
\lim_{x\to -2^+} f(x)=0
\]

y

\[
\lim_{x\to 0^-} f(x)=-\infty.
\]

Por lo tanto, para cada \(k<0\) hay exactamente una solución en \((-2,0)\), y para \(k\ge 0\) no hay soluciones en este intervalo.

---

### Conteo final

La ecuación tiene exactamente una solución real para:

- todos los enteros negativos \(k\in[-500,-1]\), que son \(500\) valores;
- \(k=8\), que aporta \(1\) valor más.

En total:

\[
500+1=501.
\]

\[
\boxed{501}
\]