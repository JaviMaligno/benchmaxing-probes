Vamos a resolver el problema paso a paso.

Consideremos la ecuación
\[
x^{10}+(11x-1)^{10}=0.
\]
Queremos calcular
\[
\sum_{i=1}^5 \frac{1}{s_i\overline{s}_i},
\]
donde \(s_1,\dots,s_5\) son 5 de las 10 raíces (las otras 5 son sus conjugadas).

**Paso 1: Relación entre las raíces.**

Si \(s\) es una raíz, su conjugada \(\overline{s}\) también lo es, pues la ecuación tiene coeficientes reales. Por lo tanto, las 10 raíces son \(s_1,\overline{s}_1,\dots,s_5,\overline{s}_5\).

Queremos la suma de los inversos de los cuadrados de los módulos de las raíces.

**Paso 2: Reescribir la ecuación.**

Observemos que
\[
x^{10}+(11x-1)^{10}=0 \iff (11x-1)^{10} = -x^{10}.
\]
Si \(x\neq 0\), dividimos por \(x^{10}\):
\[
\left(11-\frac{1}{x}\right)^{10} = -1.
\]
Sea \(y = 11-\frac{1}{x}\). Entonces
\[
\frac{1}{x} = 11-y, \qquad x = \frac{1}{11-y}.
\]
La ecuación se reduce a
\[
y^{10} = -1.
\]

**Paso 3: Soluciones de \(y^{10}=-1\).**

Las soluciones son
\[
y_k = e^{i(2k+1)\pi/10}, \qquad k=0,1,\dots,9.
\]
Cada una da una raíz
\[
x_k = \frac{1}{11-y_k}.
\]

**Paso 4: Calcular \(\frac{1}{x_k\overline{x_k}}\).**

Como \(x_k = \frac{1}{11-y_k}\), tenemos
\[
\frac{1}{x_k\overline{x_k}} = (11-y_k)(11-\overline{y_k}).
\]
Además, \(|y_k|=1\), así que
\[
(11-y_k)(11-\overline{y_k}) = 121 - 11(y_k+\overline{y_k}) + |y_k|^2
= 122 - 11(y_k+\overline{y_k})
= 122 - 22\cos\theta_k,
\]
donde \(\theta_k = \frac{(2k+1)\pi}{10}\).

**Paso 5: Sumar sobre las raíces.**

Las 10 raíces corresponden a \(\theta_k = \frac{(2k+1)\pi}{10}\), \(k=0,\dots,9\). Para nuestra suma sobre \(i=1,\dots,5\), usamos (por ejemplo) \(k=0,1,2,3,4\). Entonces:
\[
\sum_{i=1}^5 \frac{1}{s_i\overline{s}_i}
= \sum_{k=0}^4 \left(122 - 22\cos\frac{(2k+1)\pi}{10}\right).
\]

**Paso 6: Evaluar la suma de cosenos.**

\[
\sum_{k=0}^4 \cos\frac{(2k+1)\pi}{10}
= \cos\frac{\pi}{10} + \cos\frac{3\pi}{10} + \cos\frac{5\pi}{10} + \cos\frac{7\pi}{10} + \cos\frac{9\pi}{10}.
\]
Usando \(\cos\frac{9\pi}{10} = -\cos\frac{\pi}{10}\) y \(\cos\frac{7\pi}{10} = -\cos\frac{3\pi}{10}\), y \(\cos\frac{5\pi}{10}=0\), la suma es \(0\).

Por lo tanto,
\[
\sum_{i=1}^5 \frac{1}{s_i\overline{s}_i}
= 5\cdot 122 - 22\cdot 0 = 610.
\]

La respuesta es
\[
\boxed{610}
\]