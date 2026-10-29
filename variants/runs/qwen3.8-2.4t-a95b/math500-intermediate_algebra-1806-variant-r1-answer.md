

Sea \(w=e^{i\theta}\), con \(\theta\in\mathbb{R}\), y sea \(x=\cos\theta\), de modo que \(x\in[-1,1]\).

Primero,
\[
|1+w|=|1+e^{i\theta}|=\sqrt{2+2\cos\theta}=\sqrt{2+2x}.
\]

Luego,
\[
2-2w+2w^2=2w(w+w^{-1}-1)=2w(2\cos\theta-1)=2w(2x-1).
\]
Como \(|w|=1\),
\[
|2-2w+2w^2|=2|2x-1|.
\]

Por tanto, queremos maximizar
\[
f(x)=\sqrt{2+2x}+2|2x-1|,\qquad x\in[-1,1].
\]

Dividimos en dos casos.

**Caso 1:** \(x\le \frac12\). Entonces
\[
f(x)=\sqrt{2+2x}+2-4x.
\]
Derivando:
\[
f'(x)=\frac{1}{\sqrt{2+2x}}-4.
\]
El punto crítico satisface
\[
\frac{1}{\sqrt{2+2x}}=4
\]
\[
\sqrt{2+2x}=\frac14
\]
\[
2+2x=\frac1{16}
\]
\[
x=-\frac{31}{32}.
\]
Este punto está en \([-1,\frac12]\) y da un máximo local. Su valor es
\[
f\!\left(-\frac{31}{32}\right)
=\frac14+2-4\left(-\frac{31}{32}\right)
=\frac14+2+\frac{31}{8}
=\frac{49}{8}.
\]

**Caso 2:** \(x\ge \frac12\). Entonces
\[
f(x)=\sqrt{2+2x}+4x-2,
\]
cuya derivada es
\[
f'(x)=\frac{1}{\sqrt{2+2x}}+4>0.
\]
Así que \(f\) crece en este intervalo, y el máximo ocurre en \(x=1\):
\[
f(1)=2+2=4.
\]

Comparando con los extremos, \(f(-1)=6\) y \(f(1)=4\), el máximo global es

\[
\boxed{\frac{49}{8}}
\]