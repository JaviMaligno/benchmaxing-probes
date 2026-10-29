

Sea \(m\) el mes y \(d\) el día. El número formado es

\[
N = m\cdot 10^k + d,
\]

donde \(k=1\) si el día tiene 1 dígito y \(k=2\) si tiene 2 dígitos.

Para que \(m\mid N\), como \(m\mid m\cdot 10^k\), necesitamos \(m\mid d\). Escribamos \(d=mq\).

Además, para que \(d\mid N\):

\[
d\mid m\cdot 10^k+d \iff d\mid m\cdot 10^k \iff mq\mid m\cdot 10^k \iff q\mid 10^k.
\]

Ahora contamos por mes.

**Días de 1 dígito:** \(k=1\), así que \(q\mid 10\). Como \(m=6,7,8\), el único múltiplo de un dígito posible es \(d=m\), es decir:

- 6 de junio
- 7 de julio
- 8 de agosto

Esto da \(3\) fechas.

**Días de 2 dígitos:** \(k=2\), así que \(q\mid 100\).

- Junio, \(m=6\), días hasta 30: \(q=2,3,4,5\). Divisores de \(100\): \(2,4,5\). Fechas: 12, 24, 30. Total: \(3\).
- Julio, \(m=7\), días hasta 31: \(q=2,3,4\). Divisores de \(100\): \(2,4\). Fechas: 14, 28. Total: \(2\).
- Agosto, \(m=8\), días hasta 31: \(q=2,3\). Divisor de \(100\): \(2\). Fecha: 16. Total: \(1\).

Total combinado:

\[
3+3+2+1=9.
\]

\[
\boxed{9}
\]