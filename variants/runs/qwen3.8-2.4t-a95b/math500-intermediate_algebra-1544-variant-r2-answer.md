

Sea \(f(t)=t^2-4t+6\). Si las raíces de \(x^2+px+q=0\) forman el conjunto \(S\) (con \(|S|\le 2\)), la condición es

\[
f(S)\subseteq S.
\]

Hacemos el cambio \(z=x-2\). Entonces

\[
f(x)-2=(x-2)^2,
\]

por lo que en la variable \(z\) la dinámica es simplemente \(z\mapsto z^2\).

Buscamos conjuntos invariantes de tamaño \(1\) o \(2\).

1. **Raíz doble**: se necesita \(z^2=z\), así que \(z=0\) o \(z=1\), es decir \(x=2\) o \(x=3\). Esto da
   \[
   (x-2)^2=0,\qquad (x-3)^2=0.
   \]

2. **Dos raíces distintas**:
   - Ambas fijas: \(z=0,1\), es decir raíces \(2,3\). Da
     \[
     (x-2)(x-3)=0.
     \]
   - Una fija y la otra cae en ella: la única preimagen nueva de \(z=1\) es \(z=-1\). Así obtenemos raíces \(x=1,3\), y la ecuación
     \[
     (x-1)(x-3)=0.
     \]
   - Un ciclo de longitud \(2\): necesitamos \(z^4=z\) con \(z^2\ne z\). Las soluciones no fijas son las raíces cúbicas primitivas de la unidad \(\omega,\omega^2\). Las raíces en \(x\) son \(2+\omega\) y \(2+\omega^2\), cuya suma es \(3\) y producto es \(3\). Esto da
     \[
     x^2-3x+3=0.
     \]

En total hay \(2+1+1+1=5\) ecuaciones:

\[
(x-2)^2,\quad (x-3)^2,\quad (x-2)(x-3),\quad (x-1)(x-3),\quad x^2-3x+3.
\]

\[
\boxed{5}
\]