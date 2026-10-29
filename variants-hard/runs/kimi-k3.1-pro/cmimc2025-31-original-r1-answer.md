Sea \(m\) el mes y \(d\) el día. La concatenación es
\[
N=\begin{cases}
10m+d,&d<10,\\
100m+d,&d\ge 10.
\end{cases}
\]
Como \(m\) divide a \(10m\) y a \(100m\), la condición \(m\mid N\) equivale a \(m\mid d\). Además, \(d\mid N\) equivale a \(d\mid 10m\) cuando \(d<10\), y a \(d\mid 100m\) cuando \(d\ge10\).

- **Marzo (\(m=3\)):** los días válidos son \(3,6,12,15,30\): **5 días**.
- **Abril (\(m=4\)):** los días válidos son \(4,8,16,20\): **4 días**.
- **Mayo (\(m=5\)):** los días válidos son \(5,10,20,25\): **4 días**.

En total, hay \(5+4+4\) días buenos:

\[
\boxed{13}
\]