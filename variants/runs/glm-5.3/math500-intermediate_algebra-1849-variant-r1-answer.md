Dominio de la ecuación:

- \(\log(kx)\) exige \(kx>0\).
- \(\log(x+3)\) exige \(x+3>0\), es decir \(x>-3\).

Como el logaritmo es inyectivo,

\[
\log(kx)=2\log(x+3)=\log((x+3)^2)
\]

implica, dentro del dominio,

\[
kx=(x+3)^2.
\]

Entonces

\[
x^2+(6-k)x+9=0.
\]

Su discriminante es

\[
\Delta=(6-k)^2-36=k(k-12).
\]

Analizamos por casos:

1. **\(k<0\):** \(\Delta>0\), hay dos raíces reales. Además,

   \[
   q(-3)=(-3)^2+(6-k)(-3)+9=3k<0.
   \]

   Como \(q(x)\to+\infty\) cuando \(x\to+\infty\), exactamente una raíz queda en \(x>-3\). También esa raíz es negativa, y con \(k<0\) se cumple \(kx>0\).  
   Por tanto, cada entero negativo funciona.

2. **\(k=0\):** \(\log(kx)=\log(0)\) no está definido, así que no hay soluciones.

3. **\(0<k<12\):** \(\Delta<0\), no hay soluciones reales.

4. **\(k=12\):** la ecuación es

   \[
   x^2-6x+9=0 \implies (x-3)^2=0,
   \]

   con la única solución \(x=3\), válida en el dominio.

5. **\(k>12\):** \(\Delta>0\), y ambas raíces son positivas, luego hay dos soluciones reales válidas.

Los enteros negativos en \([-250,400]\) son \(250\) valores: \(-250,-249,\dots,-1\). A ellos se suma \(k=12\).

Por lo tanto, el número total es

\[
250+1=251.
\]

\[
\boxed{251}
\]