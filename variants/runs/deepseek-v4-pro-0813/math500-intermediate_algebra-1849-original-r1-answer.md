Vamos a resolver el problema paso a paso.

Queremos que la ecuación
\[
\log(kx)=2\log(x+2)
\]
tenga exactamente una solución real.

**Paso 1: Restricciones de dominio**

Para que los logaritmos estén definidos:
- \(kx > 0\).
- \(x+2 > 0\), es decir \(x > -2\).

**Paso 2: Reescribir la ecuación**

Usando propiedades de logaritmos:
\[
\log(kx)=\log\bigl((x+2)^2\bigr).
\]
Por tanto (al ser el logaritmo inyectivo en su dominio):
\[
kx = (x+2)^2,
\]
es decir
\[
x^2 + 4x + 4 - kx = 0,
\]
\[
x^2 + (4-k)x + 4 = 0.
\]

**Paso 3: Resolver la cuadrática**

El discriminante es
\[
\Delta = (4-k)^2 - 16 = k^2 - 8k = k(k-8).
\]

- Si \(\Delta < 0\), no hay soluciones reales.
- Si \(\Delta = 0\), hay una solución doble:
  \[
  k=0 \quad\text{o}\quad k=8.
  \]
- Si \(\Delta > 0\), hay dos soluciones reales:
  \[
  k<0 \quad\text{o}\quad k>8.
  \]

**Paso 4: Aplicar las restricciones de dominio**

Caso \(k=0\): la ecuación original sería \(\log(0\cdot x)\), lo cual no está definido. Descartamos \(k=0\).

Caso \(k=8\):
\[
x^2 - 4x + 4 = 0 \implies (x-2)^2=0 \implies x=2.
\]
Comprobamos: \(kx = 8\cdot 2 = 16 > 0\) y \(x+2=4>0\). Válido.

Ahora, cuando hay dos soluciones de la cuadrática, necesitamos comprobar cuántas satisfacen las restricciones \(x>-2\) y \(kx>0\).

**Paso 5: Análisis para \(k>8\)**

Las raíces son:
\[
x = \frac{k-4 \pm \sqrt{k(k-8)}}{2}.
\]
Ambas son positivas (producto \(4>0\), suma \(k-4>0\)), así que ambas cumplen \(x>0>-2\) y además \(kx>0\). Por tanto hay dos soluciones. No nos sirve.

**Paso 6: Análisis para \(k<0\)**

Las raíces son:
\[
x = \frac{k-4 \pm \sqrt{k(k-8)}}{2}.
\]
Como \(k-4<0\) y el producto es \(4>0\), ambas raíces son negativas.

Comprobemos la condición \(x>-2\).

Sea \(k=-m\) con \(m>0\). Las raíces:
\[
x = \frac{-m-4 \pm \sqrt{m(m+8)}}{2}.
\]
Nos interesa la mayor:
\[
x_+ = \frac{-m-4 + \sqrt{m(m+8)}}{2}.
\]
Necesitamos \(x > -2\):
\[
\frac{-m-4 + \sqrt{m(m+8)}}{2} > -2,
\]
\[
-m-4 + \sqrt{m(m+8)} > -4,
\]
\[
\sqrt{m(m+8)} > m,
\]
siempre cierto para \(m>0\). Por tanto \(x_+ > -2\).

Para la menor:
\[
x_- = \frac{-m-4 - \sqrt{m(m+8)}}{2}.
\]
Claramente \(x_- < x_+ < 0\). ¿Es \(x_- > -2\)?
\[
\frac{-m-4 - \sqrt{m(m+8)}}{2} > -2,
\]
\[
-m-4 - \sqrt{m(m+8)} > -4,
\]
\[
-m - \sqrt{m(m+8)} > 0,
\]
lo cual es falso. Por tanto \(x_- < -2\) y se descarta. Queda exactamente una solución.

Además, como \(x> -2\) y \(x<0\), se tiene \(kx = (-m)x >0\), así que el logaritmo está definido.

**Paso 7: Conclusión**

- \(k=8\) da una solución.
- \(k<0\) da exactamente una solución.
- \(k>8\) da dos soluciones.
- \(k=0\) no es válido (logaritmo no definido).
- \(0<k<8\) no da soluciones reales.

Contamos valores enteros de \(k\) en \([-500,500]\):

- \(k=8\): un valor.
- \(k<0\): desde \(-500\) hasta \(-1\), es decir \(500\) valores.

Total: \(500+1=501\).

\[
\boxed{501}
\]