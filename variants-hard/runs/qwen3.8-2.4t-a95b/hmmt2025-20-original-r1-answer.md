

Sean los huecos entre serpientes consecutivas alrededor del círculo. Inicialmente hay \(45-15=30\) arcos vacíos, y como las serpientes ocupan cada tercer arco, cada hueco tiene \(2\) arcos vacíos.

Como cada serpiente se mueve un arco por segundo, un hueco cambia en \(0\) o \(\pm 2\) arcos vacíos. Por tanto los huecos siempre son pares. Definamos

\[
x_i=\frac{\text{número de arcos vacíos en el hueco }i}{2}.
\]

Entonces inicialmente

\[
x_1=x_2=\cdots=x_{15}=1,
\qquad \sum_i x_i=15.
\]

Cuando un hueco llega a \(0\), las dos serpientes se tocan y se fusionan; el hueco desaparece, pero la suma total sigue siendo \(15\). Al final queda una sola serpiente y un solo hueco de tamaño \(15\).

Para un hueco de tamaño \(x\), en un segundo:

- disminuye a \(x-1\) con probabilidad \(1/4\),
- aumenta a \(x+1\) con probabilidad \(1/4\),
- queda igual con probabilidad \(1/2\).

Definamos

\[
f(x)=\frac{2}{45}x(225-x^2),
\]

con \(f(0)=f(15)=0\), y sea

\[
\Phi=\sum_i f(x_i).
\]

Calculamos el cambio esperado de \(f(x)\). Como

\[
f(x+1)-2f(x)+f(x-1)=-\frac{4x}{15},
\]

se tiene

\[
\mathbb{E}[f(x')-f(x)]
=
\frac14\bigl(f(x+1)+f(x-1)-2f(x)\bigr)
=
-\frac{x}{15}.
\]

Sumando sobre todos los huecos,

\[
\mathbb{E}[\Phi'-\Phi]
=
-\sum_i \frac{x_i}{15}
=
-1,
\]

porque \(\sum_i x_i=15\). Así, \(\Phi\) disminuye exactamente en \(1\) por segundo en esperanza, y vale \(0\) cuando queda una sola serpiente. Por tanto, el tiempo esperado restante desde una configuración es precisamente \(\Phi\).

Inicialmente,

\[
\Phi_0=15 f(1)
=
15\cdot \frac{2}{45}(225-1)
=
15\cdot \frac{448}{45}
=
\frac{448}{3}.
\]

\[
\boxed{\frac{448}{3}}
\]