Para hallar la suma $\sum_{m=1}^{3^{2030}} r_m$, utilizaremos funciones generatrices trabajando módulo $3$.

### Paso 1: Función generatriz de $c_m$
Por definición, $c_m$ es el número de composiciones (sumas ordenadas) de $m$ cuyas partes son potencias de $3$. Si definimos $c_0 = 1$, cualquier composición de $m \ge 1$ termina en alguna potencia $3^k$, por lo que se cumple la recurrencia:
$$c_m = \sum_{k \ge 0,\, 3^k \le m} c_{m - 3^k}.$$

Sea $C(x) = \sum_{m=0}^{\infty} c_m x^m$ la función generatriz de la sucesión $c_m$, y sea
$$P(x) = \sum_{k=0}^{\infty} x^{3^k} = x + x^3 + x^9 + x^{27} + \cdots.$$
Entonces:
$$C(x) = 1 + C(x)P(x) \implies C(x) = \frac{1}{1 - P(x)}.$$

### Paso 2: Reducción módulo $3$
Consideremos las series de potencias formales en $\mathbb{F}_3[[x]]$. En característica $3$, se cumple que $(A(x))^3 = A(x^3)$ para cualquier serie $A(x) \in \mathbb{F}_3[[x]]$. Observamos que $P(x)$ satisface:
$$P(x) = x + P(x^3) = x + P(x)^3 \pmod 3.$$
Despejando $x$ y factorizando en $\mathbb{F}_3[[x]]$:
$$x = P(x) - P(x)^3 = P(x)(1 - P(x)^2) = P(x)(1 - P(x))(1 + P(x)) \pmod 3.$$
Dividiendo ambos lados por $x(1 - P(x))$, obtenemos una expresión explícita para $C(x)$ en $\mathbb{F}_3[[x]]$:
$$C(x) = \frac{1}{1 - P(x)} \equiv \frac{P(x) + P(x)^2}{x} \pmod 3.$$

### Paso 3: Expansión de los coeficientes $r_m$
Expandimos ambos términos del numerador dividido por $x$:
1. Para el término lineal:
$$\frac{P(x)}{x} = \sum_{k=0}^{\infty} x^{3^k - 1} = 1 + \sum_{k=1}^{\infty} x^{3^k - 1}.$$
2. Para el término cuadrático:
$$\frac{P(x)^2}{x} = \frac{1}{x} \left(\sum_{k=0}^{\infty} x^{3^k}\right)^2 = \sum_{k=0}^{\infty} x^{2 \cdot 3^k - 1} + 2 \sum_{0 \le j < k} x^{3^k + 3^j - 1}.$$

Por la unicidad de la representación en base $3$, los enteros de las formas $3^k$ ($k \ge 1$), $2 \cdot 3^k$ ($k \ge 0$) y $3^k + 3^j$ ($0 \le j < k$) son todos distintos entre sí. Por lo tanto, al restar $1$ a cada exponente, los tres conjuntos de exponentes para $m \ge 1$ son disjuntos dos a dos.

De este modo, para cada $m \ge 1$, el resto $r_m \in \{0, 1, 2\}$ viene dado exactamente por:
- $r_m = 1$, si $m = 3^k - 1$ con $k \ge 1$.
- $r_m = 1$, si $m = 2 \cdot 3^k - 1$ con $k \ge 0$.
- $r_m = 2$, si $m = 3^k + 3^j - 1$ con $0 \le j < k$.
- $r_m = 0$, en cualquier otro caso.

### Paso 4: Cálculo de la suma hasta $m = 3^{2030}$
Sea $N = 2030$. Contamos cuántos índices $m \in \{1, 2, \dots, 3^N\}$ pertenecen a cada una de las tres familias:

1. **Familia $m = 3^k - 1$ ($k \ge 1$):**
   La condición $1 \le 3^k - 1 \le 3^N$ equivale a $1 \le k \le N$. Hay $N$ términos, cada uno con $r_m = 1$.
   $$\text{Aporte}_1 = N.$$

2. **Familia $m = 2 \cdot 3^k - 1$ ($k \ge 0$):**
   La condición $1 \le 2 \cdot 3^k - 1 \le 3^N$ equivale a $0 \le k \le N - 1$. Hay $N$ términos, cada uno con $r_m = 1$.
   $$\text{Aporte}_2 = N.$$

3. **Familia $m = 3^k + 3^j - 1$ ($0 \le j < k$):**
   - Si $1 \le k \le N - 1$, cualquier $0 \le j < k$ cumple $3^k + 3^j - 1 < 3^N$, lo que da $\binom{N}{2}$ parejas $(j, k)$.
   - Si $k = N$, la condición $3^N + 3^j - 1 \le 3^N$ implica $3^j \le 1$, cuya única solución es $j = 0$ (correspondiente a $m = 3^N$). Esto añade $1$ pareja más.
   - Si $k > N$, no hay soluciones.
   
   En total hay $\binom{N}{2} + 1$ términos en esta familia, cada uno con $r_m = 2$.
   $$\text{Aporte}_3 = 2\left(\binom{N}{2} + 1\right) = N(N - 1) + 2.$$

Sumando los tres aportes para $N = 2030$:
$$\sum_{m=1}^{3^N} r_m = N + N + N(N - 1) + 2 = N^2 + N + 2.$$

Sustituyendo $N = 2030$:
$$2030^2 + 2030 + 2 = 4120900 + 2030 + 2 = 4122932.$$

\boxed{4122932}