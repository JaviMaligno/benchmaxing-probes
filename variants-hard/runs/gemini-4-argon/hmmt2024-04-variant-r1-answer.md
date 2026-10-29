Sea $g(x) = \frac{P(x)}{Q(x)}$, donde $P(x) = a_2 x^2 + a_1 x + a_0$ y $Q(x) = b_2 x^2 + b_1 x + b_0$ son dos polinomios cuadráticos. 

La condición $g(k) = k^3$ para $k \in \{1, 2, 3, 4, 6\}$ implica que:
$$k^3 Q(k) - P(k) = 0 \quad \text{para } k \in \{1, 2, 3, 4, 6\}.$$

Definamos el polinomio $R(x) = x^3 Q(x) - P(x)$. Sustituyendo las expresiones de $P(x)$ y $Q(x)$, obtenemos:
$$R(x) = b_2 x^5 + b_1 x^4 + b_0 x^3 - a_2 x^2 - a_1 x - a_0.$$

Observamos que $R(x)$ es un polinomio de grado a lo sumo $5$ que tiene $5$ raíces distintas: $1, 2, 3, 4$ y $6$. Por lo tanto, podemos factorizar $R(x)$ como:
$$R(x) = b_2 (x - 1)(x - 2)(x - 3)(x - 4)(x - 6).$$

Sin pérdida de generalidad, podemos fijar $b_2 = 1$ (ya que multiplicar $P(x)$ y $Q(x)$ por una misma constante no altera $g(x)$). Queremos calcular:
$$g(0) = \frac{P(0)}{Q(0)} = \frac{a_0}{b_0}.$$

A partir de las relaciones de Vieta para el polinomio $R(x) = (x - 1)(x - 2)(x - 3)(x - 4)(x - 6)$:

1. El término independiente de $R(x)$ es $-a_0$:
   $$-a_0 = (-1)(-2)(-3)(-4)(-6) = -144 \implies a_0 = 144.$$

2. El coeficiente de $x^3$ en $R(x)$ es $b_0$, el cual corresponde a la suma de los productos de las raíces tomadas de dos en dos ($\sum_{i < j} r_i r_j$). Usando la identidad $2\sum_{i < j} r_i r_j = \left(\sum r_i\right)^2 - \sum r_i^2$:
   $$\sum r_i = 1 + 2 + 3 + 4 + 6 = 16,$$
   $$\sum r_i^2 = 1^2 + 2^2 + 3^2 + 4^2 + 6^2 = 1 + 4 + 9 + 16 + 36 = 66.$$
   Por consiguiente:
   $$b_0 = \frac{16^2 - 66}{2} = \frac{256 - 66}{2} = \frac{190}{2} = 95.$$

Finalmente, evaluamos $g(0)$:
$$g(0) = \frac{a_0}{b_0} = \frac{144}{95}.$$

\boxed{\frac{144}{95}}