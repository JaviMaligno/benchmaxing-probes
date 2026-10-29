Sea \(m\) el mes y \(d\) el día. La concatenación es \(N=m\cdot 10^k+d\), donde \(k\) es el número de dígitos de \(d\). Como

\[
N\equiv d \pmod m,
\]

la condición \(m\mid N\) equivale a \(m\mid d\). Además, \(d\mid N\) equivale a \(d\mid m\cdot 10^k\).

- **Marzo** (\(m=3\), \(d\le 31\)): necesitamos \(3\mid d\). Los candidatos son \(3,6,9,12,15,18,21,24,27,30\).  
  De un dígito: \(d\mid 30\), sirven \(3,6\).  
  De dos dígitos: \(d\mid 300\), sirven \(12,15,30\).  
  Total: \(5\).

- **Abril** (\(m=4\), \(d\le 30\)): necesitamos \(4\mid d\). Candidatos: \(4,8,12,16,20,24,28\).  
  Sirven \(4,8,16,20\).  
  Total: \(4\).

- **Mayo** (\(m=5\), \(d\le 31\)): necesitamos \(5\mid d\). Candidatos: \(5,10,15,20,25,30\).  
  Sirven \(5,10,20,25\).  
  Total: \(4\).

Sumando: \(5+4+4=13\).

\[
\boxed{13}
\]