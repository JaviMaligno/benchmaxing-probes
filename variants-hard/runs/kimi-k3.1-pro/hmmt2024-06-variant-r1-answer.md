Sea \(m=2n+3\) y \(d=\operatorname{ord}_m(2)\). Entonces
\[
m\mid 2^{n!}-1\quad\Longleftrightarrow\quad d\mid n!.
\]

1. **Si \(m\) es compuesto**, para \(n\ge 60\) se tiene \(\varphi(m)\mid n!\): cada potencia de primo que divide \(\varphi(m)\) es como mucho \(n\). Como \(d\mid\varphi(m)\), siempre se cumple la divisibilidad.

2. **Si \(m\) es primo**, entonces
   \[
   d\mid m-1=2(n+1).
   \]
   Si \(n+1\) es compuesto, \(2(n+1)\mid n!\), por lo que \(d\mid n!\).

3. Queda el caso en que \(p=n+1\) es primo y \(m=2p+1\) también es primo. Como \(d\mid2p\) y \(d\notin\{1,2\}\), necesariamente \(p\mid d\). Pero \(p=n+1\nmid n!\), así que estos son exactamente los valores buscados.

Por tanto, \(p\) debe ser un primo de Sophie Germain con \(61\le p\le121\). Los únicos son
\[
p=83,\quad89,\quad113,
\]
que dan
\[
n=82,\quad88,\quad112.
\]
Su suma es \(82+88+112=282\).

\[
\boxed{282}
\]