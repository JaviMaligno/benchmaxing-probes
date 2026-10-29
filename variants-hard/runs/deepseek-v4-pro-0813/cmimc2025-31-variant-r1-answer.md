Para un mes \(m\) y un día \(d\), el número formado es
\[
N=m\cdot 10^k+d,
\]
donde \(k\) es la cantidad de cifras de \(d\).

Como \(N-m\cdot 10^k=d\), la condición de que \(m\mid N\) equivale a que \(m\mid d\). Así, el día debe ser múltiplo del número del mes. Además, como \(d\mid d\), la condición de que \(d\mid N\) equivale a que
\[
d\mid m\cdot 10^k.
\]

**Junio (\(m=6\)):** días múltiplos de \(6\) entre \(1\) y \(30\):
\[
6,12,18,24,30.
\]
- \(d=6\): \(6\mid 60\). Sí.
- \(d=12,18,24,30\): deben dividir a \(600\).
  \[
  12\mid 600,\quad 18\nmid 600,\quad 24\mid 600,\quad 30\mid 600.
  \]
Lucky dates: \(6,12,24,30\). Son \(4\).

**Julio (\(m=7\)):** días múltiplos de \(7\) entre \(1\) y \(31\):
\[
7,14,21,28.
\]
- \(d=7\): \(7\mid 70\). Sí.
- \(d=14,21,28\): deben dividir a \(700\).
  \[
  14\mid 700,\quad 21\nmid 700,\quad 28\mid 700.
  \]
Lucky dates: \(7,14,28\). Son \(3\).

**Agosto (\(m=8\)):** días múltiplos de \(8\) entre \(1\) y \(31\):
\[
8,16,24.
\]
- \(d=8\): \(8\mid 80\). Sí.
- \(d=16,24\): deben dividir a \(800\).
  \[
  16\mid 800,\quad 24\nmid 800.
  \]
Lucky dates: \(8,16\). Son \(2\).

En total:
\[
4+3+2=9.
\]

\[
\boxed{9}
\]