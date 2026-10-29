Para hallar el coeficiente de $x^{2027}$ en el polinomio $g(x)$, utilizamos la fórmula de interpolación de Lagrange.

Sea $P = 2029$, que es un número primo. Los cuadrados perfectos en el conjunto $\{1, 2, \ldots, 2029\}$ son $1^2, 2^2, \ldots, 45^2$, ya que $45^2 = 2025 \le 2029 < 2116 = 46^2$.

Por la fórmula de interpolación de Lagrange, el polinomio único $g(x)$ de grado a lo sumo $2028$ viene dado por:
$$g(x) = \sum_{m=1}^{2029} g(m) \prod_{\substack{j=1 \\ j \neq m}}^{2029} \frac{x - j}{m - j} = \sum_{k=1}^{45} \frac{L_{k^2}(x)}{D_{k^2}}$$
donde, para cada $m \in \{1, 2, \ldots, 2028\}$:
$$L_m(x) = \prod_{\substack{j=1 \\ j \neq m}}^{2029} (x - j) \quad \text{y} \quad D_m = \prod_{\substack{j=1 \\ j \neq m}}^{2029} (m - j).$$

**Paso 1: Analizar el denominador $D_m$ módulo $P = 2029$.**

Para cualquier $m \in \{1, 2, \ldots, P-1\}$, podemos escribir:
$$D_m = (m-1)(m-2)\cdots(1)\cdot(-1)(-2)\cdots(m-P) = (-1)^{P-m}(m-1)!(P-m)!$$
Como $1 \le m \le P-1$ y $P$ es primo, ni $(m-1)!$ ni $(P-m)!$ son divisibles por $P$, por lo que $\gcd(D_m, P) = 1$. Además, módulo $P$:
$$D_m = (-1)^{P-m}(m-1)!(P-m)! \equiv (m-1)! \cdot m(m+1)\cdots(P-1) = (P-1)! \pmod{P}.$$
Por el teorema de Wilson, $(P-1)! \equiv -1 \pmod{P}$, de modo que:
$$D_m \equiv -1 \pmod{2029}.$$

**Paso 2: Analizar el coeficiente de $x^{2027}$ en $L_m(x)$ módulo $P = 2029$.**

El polinomio $L_m(x)$ es mónico de grado $P-1 = 2028$. Por las fórmulas de Vieta, el coeficiente $c_m$ de $x^{2027}$ en $L_m(x)$ es el opuesto de la suma de sus raíces:
$$c_m = -\sum_{\substack{j=1 \\ j \neq m}}^{2029} j = -\left(\frac{2029 \times 2030}{2} - m\right) = m - 2029 \times 1015.$$
Reduciendo módulo $2029$, obtenemos:
$$c_m \equiv m \pmod{2029}.$$

**Paso 3: Calcular $s$ módulo $2029$.**

El coeficiente de $x^{2027}$ en $g(x)$ es:
$$\frac{p}{q} = \sum_{k=1}^{45} \frac{c_{k^2}}{D_{k^2}}.$$
Como $\gcd(D_{k^2}, 2029) = 1$ para todo $k \in \{1, \ldots, 45\}$, se tiene que $\gcd(q, 2029) = 1$. La condición $p - sq \equiv 0 \pmod{2029}$ equivale a:
$$s \equiv p q^{-1} \equiv \sum_{k=1}^{45} c_{k^2} D_{k^2}^{-1} \equiv \sum_{k=1}^{45} \frac{k^2}{-1} = -\sum_{k=1}^{45} k^2 \pmod{2029}.$$

Calculamos la suma de los cuadrados:
$$\sum_{k=1}^{45} k^2 = \frac{45 \times 46 \times 91}{6} = 15 \times 23 \times 91 = 345 \times 91 = 31395.$$

Finalmente, reducimos $-31395$ módulo $2029$:
$$31395 = 15 \times 2029 + 960 \equiv 960 \pmod{2029},$$
por lo que:
$$s \equiv -960 \equiv 2029 - 960 = 1069 \pmod{2029}.$$

\boxed{1069}