Representemos las sillas seleccionadas con \(1\) y las vacías con \(0\). La condición equivale a que ninguna persona tenga a ambas vecinas ocupadas, es decir, no puede aparecer \(111\).

Contemos cadenas de longitud \(16\) con ocho \(1\) y ocho \(0\) sin tres \(1\) consecutivos. Agrupemos los \(1\) en \(r\) bloques, cada uno de longitud \(1\) o \(2\). Como hay \(8\) personas, \(r\) puede ser de \(4\) a \(8\).

Para cada \(r\):

- Hay \(8-r\) bloques de longitud \(2\), elegibles entre los \(r\) bloques:
  \[
  \binom{r}{8-r}.
  \]
- Las \(8\) sillas vacías se distribuyen en \(r+1\) huecos, con los \(r-1\) huecos internos teniendo al menos una vacía. Esto deja \(8-(r-1)=9-r\) vacías libres, repartidas entre \(r+1\) huecos:
  \[
  \binom{9}{r}.
  \]

Así,
\[
N=\sum_{r=4}^{8}\binom{r}{8-r}\binom{9}{r}
=126+1260+1260+252+9=2907.
\]

Por lo tanto,
\[
N\bmod 1000=907.
\]

\[
\boxed{907}
\]