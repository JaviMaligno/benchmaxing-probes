Como \(x=0\) no es raíz, podemos dividir entre \(x^{10}\):
\[
\left(\frac{11x-1}{x}\right)^{10}=-1.
\]
Así, para cada raíz \(x\),
\[
11-\frac1x=\omega,\qquad \omega^{10}=-1,
\]
de donde \(x=(11-\omega)^{-1}\). Los diez valores de \(\omega\) son
\[
\omega_k=e^{(2k+1)\pi i/10},\qquad k=0,\dots,9,
\]
y las raíces conjugadas corresponden a valores conjugados de \(\omega\).

Por tanto,
\[
\frac1{x\overline x}
=|11-\omega|^2
=122-22\operatorname{Re}\omega.
\]
Tomando un representante de cada par conjugado, correspondiente a \(\omega_0,\dots,\omega_4\), la suma buscada es
\[
5\cdot122-22\sum_{k=0}^4\cos\frac{(2k+1)\pi}{10}.
\]
Los cosenos se cancelan por parejas:
\[
\cos18^\circ+\cos162^\circ=0,\qquad
\cos54^\circ+\cos126^\circ=0,\qquad
\cos90^\circ=0.
\]
Hence, el resultado es
\[
\boxed{610}
\]