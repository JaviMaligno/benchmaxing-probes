## Razonamiento

**Método 1: AM-GM ponderado**

Escribimos la suma $p+q+r+s=16$ como suma de 8 términos (los pesos $1,2,2,3$ suman $8$):

$$p + \frac{q}{2} + \frac{q}{2} + \frac{r}{2} + \frac{r}{2} + \frac{s}{3} + \frac{s}{3} + \frac{s}{3} = 16.$$

Por AM-GM sobre estos 8 términos:

$$\frac{16}{8} = 2 \geq \left( p \cdot \frac{q^2}{4} \cdot \frac{r^2}{4} \cdot \frac{s^3}{27} \right)^{1/8}.$$

Elevando a la octava potencia:

$$\frac{p\, q^2 r^2 s^3}{4 \cdot 4 \cdot 27} \leq 2^8 = 256 \quad\Longrightarrow\quad p\, q^2 r^2 s^3 \leq 256 \cdot 432 = 110592.$$

La igualdad se alcanza cuando los 8 términos valen $2$:

$$p = 2,\qquad \frac{q}{2}=2 \Rightarrow q=4,\qquad \frac{r}{2}=2 \Rightarrow r=4,\qquad \frac{s}{3}=2 \Rightarrow s=6.$$

Verificación de la restricción: $2+4+4+6 = 16$. ✓

**Método 2: Multiplicadores de Lagrange (verificación)**

Maximizamos $f = \ln p + 2\ln q + 2\ln r + 3\ln s$ con $p+q+r+s=16$. Las condiciones dan:

$$\frac{1}{p} = \frac{2}{q} = \frac{2}{r} = \frac{3}{s} = \lambda \;\Longrightarrow\; p=\frac{1}{\lambda},\; q=r=\frac{2}{\lambda},\; s=\frac{3}{\lambda}.$$

Sumando: $\frac{8}{\lambda} = 16 \Rightarrow \lambda = \frac{1}{2}$, es decir, $p=2$, $q=r=4$, $s=6$, que coincide con el método anterior.

**Evaluación:**
$$p\, q^2 r^2 s^3 = 2 \cdot 4^2 \cdot 4^2 \cdot 6^3 = 2 \cdot 16 \cdot 16 \cdot 216 = 110592.$$

$$\boxed{110592}$$