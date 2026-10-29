Vamos a resolver el problema paso a paso.

Sea \(z\) un número complejo con \(|z|=1\). Escribimos \(z=e^{i\theta}\) con \(\theta\in[0,2\pi)\).

Queremos maximizar
\[
|1+z|+|1-z+z^2|.
\]

## Primer término

Como \(|z|=1\),
\[
|1+z|=|1+e^{i\theta}|
=\left|e^{i\theta/2}\left(e^{-i\theta/2}+e^{i\theta/2}\right)\right|
=2\left|\cos\frac{\theta}{2}\right|.
\]

## Segundo término

Observamos que
\[
1-z+z^2=\frac{1+z^3}{1+z}
\]
siempre que \(z\neq -1\); de hecho la factorización vale para todo \(z\neq -1\), y para \(z=-1\) el valor es \(1-(-1)+1=3\), que podemos tratar aparte o por continuidad.

Otra forma útil: multiplicamos por \(z^{-1}\) (ya que \(|z|=1\)):
\[
|1-z+z^2|
=\left|z^{-1}(1-z+z^2)\right|
=|z^{-1}-1+z|
=|z+z^{-1}-1|.
\]
Pero \(z+z^{-1}=e^{i\theta}+e^{-i\theta}=2\cos\theta\). Por tanto,
\[
|1-z+z^2|=|2\cos\theta-1|.
\]

Así, la expresión a maximizar es
\[
f(\theta)=2\left|\cos\frac{\theta}{2}\right|+|2\cos\theta-1|.
\]

## Simplificación

Sea \(c=\cos\frac{\theta}{2}\). Como \(\theta\in[0,2\pi)\), \(c\in[-1,1]\), y
\[
\cos\theta=2c^2-1.
\]
Entonces
\[
2\cos\theta-1=4c^2-3.
\]
Por lo tanto,
\[
f=2|c|+|4c^2-3|.
\]

Ahora notamos que \(4c^2-3\ge 0\) cuando \(c^2\ge 3/4\), es decir \(|c|\ge \sqrt3/2\). Para \(|c|<\sqrt3/2\), tenemos \(|4c^2-3|=3-4c^2\).

Sea \(t=|c|\in[0,1]\). Entonces
\[
f(t)=
\begin{cases}
2t+3-4t^2, & 0\le t<\sqrt3/2,\\[4pt]
2t+4t^2-3, & \sqrt3/2\le t\le 1.
\end{cases}
\]

## Maximización

### Caso 1: \(0\le t<\sqrt3/2\)

Aquí
\[
f(t)=3+2t-4t^2.
\]
Derivamos:
\[
f'(t)=2-8t.
\]
El máximo se da en \(t=1/4\), que está en el intervalo. Entonces
\[
f(1/4)=3+\frac12-4\cdot\frac1{16}
=3+\frac12-\frac14
=\frac{13}{4}.
\]

### Caso 2: \(\sqrt3/2\le t\le 1\)

Aquí
\[
f(t)=4t^2+2t-3.
\]
Derivada:
\[
f'(t)=8t+2>0,
\]
así que \(f\) es creciente. El máximo ocurre en \(t=1\):
\[
f(1)=4+2-3=3.
\]

Por tanto, el máximo global es
\[
\frac{13}{4}.
\]

## Verificación

Con \(t=1/4\), elegimos \(\theta\) tal que \(\cos(\theta/2)=\pm 1/4\). Por ejemplo, \(\cos(\theta/2)=1/4\). Entonces
\[
2|1/4|=1/2,\qquad |4(1/16)-3|=\left|\frac14-3\right|=\frac{11}{4},
\]
y la suma es
\[
\frac12+\frac{11}{4}=\frac{13}{4}.
\]

\[
\boxed{\frac{13}{4}}
\]