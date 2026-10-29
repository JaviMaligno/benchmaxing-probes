Primero observamos la ecuación:

\[
z^8 - z^7 + z^6 - z^5 + z^4 - z^3 + z^2 - z + 1 = 0.
\]

Los términos alternan signo. Esto sugiere multiplicar por \(z+1\). Recordemos que

\[
(z+1)(z^8 - z^7 + z^6 - z^5 + z^4 - z^3 + z^2 - z + 1) = z^9 + 1.
\]

Verifiquemos: al multiplicar, los términos intermedios se cancelan en pares, y efectivamente queda \(z^9+1\).

Por tanto, las raíces de la ecuación original son las raíces de

\[
z^9 + 1 = 0
\]

excepto \(z=-1\), ya que \(z=-1\) es la raíz que corresponde al factor \(z+1\) que añadimos.

Las raíces de \(z^9=-1\) son

\[
z = e^{i\theta_k}, \qquad \theta_k = \frac{\pi + 2\pi k}{9}, \quad k=0,1,\dots,8.
\]

Todas tienen módulo \(1\), así que \(r=1\), consistente con \(r>0\).

La raíz \(z=-1\) corresponde a \(\theta=\pi\), es decir, cuando \(\pi+2\pi k = 9\pi\), lo cual da \(k=4\). Esa debe excluirse.

Entonces los valores posibles de \(\theta\) son

\[
\theta_k = \frac{\pi + 2\pi k}{9}, \quad k=0,1,2,3,5,6,7,8.
\]

Sumémoslos. La suma de los nueve valores con \(k=0,\dots,8\) es

\[
\sum_{k=0}^{8} \frac{\pi+2\pi k}{9}
= \frac{9\pi}{9} + \frac{2\pi}{9}\cdot \frac{8\cdot 9}{2}
= \pi + 8\pi
= 9\pi.
\]

Restamos el valor excluido \(\pi\):

\[
9\pi - \pi = 8\pi.
\]

Por lo tanto, la suma de todos los valores posibles de \(\theta\) es

\[
\boxed{8\pi}.
\]