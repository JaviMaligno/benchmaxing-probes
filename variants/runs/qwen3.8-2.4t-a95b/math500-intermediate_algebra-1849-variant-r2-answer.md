

Para que la ecuación

\[
\log(kx)=2\log(x+3)
\]

tenga sentido en los reales, necesitamos

\[
kx>0 \quad \text{y} \quad x+3>0.
\]

Dentro del dominio, podemos igualar argumentos:

\[
\log(kx)=\log\bigl((x+3)^2\bigr)
\]

por lo que

\[
kx=(x+3)^2.
\]

Esto equivale a la cuadrática

\[
x^2+(6-k)x+9=0.
\]

Además, si una raíz de esta ecuación cumple \(x>-3\), entonces automáticamente

\[
kx=(x+3)^2>0,
\]

así que basta contar cuántas raíces cumplen \(x>-3\).

El discriminante es

\[
\Delta=(6-k)^2-36=k(k-12).
\]

Analicemos por casos:

1. **\(0<k<12\):**  
   \(\Delta<0\), no hay raíces reales. No hay soluciones.

2. **\(k=12\):**  
   \[
   x^2-6x+9=(x-3)^2=0,
   \]
   hay una única raíz \(x=3\), que cumple \(x>-3\). Por tanto, hay exactamente una solución.

3. **\(k>12\):**  
   \(\Delta>0\). El producto de raíces es \(9>0\) y la suma es \(k-6>0\), así que ambas raíces son positivas. Ambas cumplen \(x>-3\), luego hay dos soluciones.

4. **\(k=0\):**  
   La ecuación original tiene \(\log(0)\), que no está definido. No hay soluciones.

5. **\(k<0\):**  
   \(\Delta>0\). El producto de raíces es positivo y la suma \(k-6\) es negativa, así que ambas raíces son negativas. Además,
   \[
   q(-3)=(-3)^2+(6-k)(-3)+9=3k<0.
   \]
   Como la parábola abre hacia arriba, \(q(-3)<0\) implica que \(-3\) está entre las dos raíces. Por tanto, una raíz es menor que \(-3\) y la otra está en \((-3,0)\). Solo esta última es válida, dando exactamente una solución.

Entonces, los enteros \(k\) que funcionan son todos los negativos en el intervalo más \(k=12\):

\[
k=-250,-249,\dots,-1
\]

hay \(250\) valores, y además \(k=12\) aporta \(1\) valor.

\[
250+1=251
\]

\[
\boxed{251}
\]