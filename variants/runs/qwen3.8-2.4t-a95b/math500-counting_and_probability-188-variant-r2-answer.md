

Elegimos \(a,b\) de forma independiente y uniforme en \((0,4)\). El espacio muestral es el cuadrado

\[
0<a<4,\qquad 0<b<4,
\]

de área \(16\).

Para que exista un triángulo con lados \(2,a,b\), se deben cumplir las tres desigualdades triangulares:

\[
a+b>2,
\]
\[
a+2>b \iff b-a<2,
\]
\[
b+2>a \iff a-b<2.
\]

Las dos últimas equivalen a

\[
|a-b|<2.
\]

Por tanto, la región favorable dentro del cuadrado es:

\[
a+b>2 \quad \text{y} \quad |a-b|<2.
\]

Calculamos el área favorable restando del cuadrado total las regiones que no cumplen las condiciones.

1. La condición \(a+b>2\) excluye el triángulo cerca del origen con vértices \((0,0),(2,0),(0,2)\), cuya área es

\[
\frac{1}{2}\cdot 2\cdot 2=2.
\]

2. La condición \(|a-b|<2\) excluye dos triángulos:
   - donde \(b-a\ge 2\), con área \(2\);
   - donde \(a-b\ge 2\), con área \(2\).

Estas regiones excluidas no se solapan en área con \(a+b\le 2\), salvo fronteras de área cero.

Así, el área favorable es

\[
16-2-2-2=10.
\]

La probabilidad pedida es

\[
\frac{10}{16}=\frac{5}{8}.
\]

\[
\boxed{\frac{5}{8}}
\]