Para encontrar el valor de $x_{2025}$, expresamos cada término de la sucesión como una fracción irreducible $x_k = \frac{a_k}{b_k}$, donde $a_k$ y $b_k$ son enteros positivos coprimos ($\gcd(a_k, b_k) = 1$).

### Paso 1: Análisis de la relación de recurrencia
Sustituyendo $x_k = \frac{a_k}{b_k}$ en la relación de recurrencia dada:
$$x_{k+1} = \frac{1}{3}\left(\frac{a_k}{b_k} + \frac{b_k}{a_k} - 1\right) = \frac{a_k^2 - a_k b_k + b_k^2}{3 a_k b_k}$$

Analicemos el máximo común divisor entre el numerador $a_k^2 - a_k b_k + b_k^2$ y el producto $a_k b_k$:
- Si un número primo $p$ divide a $a_k$, entonces $a_k^2 - a_k b_k + b_k^2 \equiv b_k^2 \not\equiv 0 \pmod p$, ya que $\gcd(a_k, b_k) = 1$.
- Análogamente, si un primo $p$ divide a $b_k$, entonces $a_k^2 - a_k b_k + b_k^2 \equiv a_k^2 \not\equiv 0 \pmod p$.

Por lo tanto, $\gcd(a_k^2 - a_k b_k + b_k^2, a_k b_k) = 1$. Esto significa que el único factor común posible entre el numerador y el denominador de $\frac{a_k^2 - a_k b_k + b_k^2}{3 a_k b_k}$ es $3$.

Observemos que podemos reescribir el numerador como:
$$a_k^2 - a_k b_k + b_k^2 = (a_k + b_k)^2 - 3 a_k b_k$$
De aquí se deduce que $3$ divide a $a_k^2 - a_k b_k + b_k^2$ si y solo si $3$ divide a $a_k + b_k$.

### Paso 2: Recurrencia para la suma $s_k = a_k + b_k$
Si $3 \mid (a_k + b_k)$, el factor $3$ se cancela en la fracción de $x_{k+1}$, quedando en su forma irreducible $\frac{a_{k+1}}{b_{k+1}}$ con:
$$a_{k+1} = \frac{a_k^2 - a_k b_k + b_k^2}{3}, \qquad b_{k+1} = a_k b_k$$

Sumando ambas expresiones para obtener $s_{k+1} = a_{k+1} + b_{k+1}$:
$$s_{k+1} = \frac{a_k^2 - a_k b_k + b_k^2}{3} + a_k b_k = \frac{a_k^2 + 2a_k b_k + b_k^2}{3} = \frac{(a_k + b_k)^2}{3} = \frac{s_k^2}{3}$$

Para $k = 1$, tenemos $x_1 = \frac{25}{11}$, por lo que $a_1 = 25$, $b_1 = 11$ y:
$$s_1 = 25 + 11 = 36 = 3 \cdot 12$$
Definimos $s_k = 3 t_k$ con $t_1 = 12$. Entonces la relación $s_{k+1} = \frac{s_k^2}{3}$ se transforma en:
$$3 t_{k+1} = \frac{(3 t_k)^2}{3} = 3 t_k^2 \implies t_{k+1} = t_k^2$$

Por inducción, para todo $k \ge 1$, $t_k = 12^{2^{k-1}}$ es un entero positivo, lo que garantiza que $s_k = 3 t_k$ es siempre divisible por $3$ y que la fracción se reduce exactamente por un factor de $3$ en cada paso. Así:
$$s_k = a_k + b_k = 3 \cdot 12^{2^{k-1}}$$

### Paso 3: Cálculo para $k = 2025$ módulo $1000$
Para $k = 2025$, tenemos:
$$m + n = s_{2025} = 3 \cdot 12^{2^{2024}}$$

Queremos hallar $3 \cdot 12^{2^{2024}} \pmod{1000}$. Como $1000 = 8 \times 125$, aplicamos el teorema de Euler módulo $125$, donde $\phi(125) = 100$. Reducimos el exponente $2^{2024} \pmod{100}$:
- Módulo $4$: $2^{2024} \equiv 0 \pmod 4$.
- Módulo $25$: Como $\phi(25) = 20$ y $2024 \equiv 4 \pmod{20}$, tenemos $2^{2024} \equiv 2^4 = 16 \pmod{25}$.

Por el teorema chino del resto, $2^{2024} \equiv 16 \pmod{100}$. Dado que tanto $12^{2^{2024}}$ como $12^{16}$ son múltiplos de $8$, se cumple que:
$$12^{2^{2024}} \equiv 12^{16} \pmod{1000}$$

Calculamos las potencias sucesivas de $12$ módulo $1000$:
$$\begin{aligned}
12^2 &= 144 \\
12^4 &= 144^2 = 20736 \equiv 736 \equiv -264 \pmod{1000} \\
12^8 &\equiv (-264)^2 = 69696 \equiv 696 \equiv -304 \pmod{1000} \\
12^{16} &\equiv (-304)^2 = 92416 \equiv 416 \pmod{1000}
\end{aligned}$$

Finalmente, multiplicamos por $3$:
$$m + n \equiv 3 \times 416 = 1248 \equiv 248 \pmod{1000}$$

\boxed{248}