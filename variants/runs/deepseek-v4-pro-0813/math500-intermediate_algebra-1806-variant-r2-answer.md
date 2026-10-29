Sea \(w=e^{i\theta}\) con \(\theta\in\mathbb R\).

Para el primer término:
\[
|1+w|=|1+e^{i\theta}|=2\left|\cos\frac{\theta}{2}\right|.
\]

Para el segundo:
\[
1-w+w^2=e^{i\theta}(e^{-i\theta}-1+e^{i\theta})
=e^{i\theta}(2\cos\theta-1),
\]
así que
\[
|2-2w+2w^2|=2|1-w+w^2|=2|2\cos\theta-1|.
\]

Tomando \(c=\cos\frac{\theta}{2}\in[-1,1]\), tenemos
\[
2\cos\theta-1=4c^2-3.
\]
Por tanto, hay que maximizar
\[
2\left(|c|+|4c^2-3|\right).
\]

Sea \(x=|c|\in[0,1]\). Debemos maximizar
\[
H(x)=x+|4x^2-3|.
\]

Si \(0\le x\le \frac{\sqrt3}{2}\), entonces
\[
H(x)=x+3-4x^2,
\]
cuyo máximo en ese intervalo se da en \(x=\frac18\), y vale
\[
H\left(\frac18\right)=\frac{49}{16}.
\]

Si \(\frac{\sqrt3}{2}\le x\le 1\), entonces
\[
H(x)=x+4x^2-3,
\]
que es creciente en ese intervalo y vale como máximo \(2<\frac{49}{16}\).

Por lo tanto, el valor máximo buscado es
\[
2\cdot\frac{49}{16}=\frac{49}{8}.
\]

\[
\boxed{\frac{49}{8}}
\]