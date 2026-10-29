Sea $f(x) = \frac{P(x)}{Q(x)}$, donde $P(x)$ y $Q(x)$ son dos polinomios cuadráticos:
$$P(x) = ax^2 + bx + c$$
$$Q(x) = dx^2 + ex + g$$

De acuerdo con el enunciado, tenemos que $f(n) = n^3$ para $n \in \{1, 2, 3, 4, 5\}$, lo cual implica que:
$$n^3 Q(n) - P(n) = 0 \quad \text{para } n = 1, 2, 3, 4, 5.$$

Definamos el polinomio $R(x) = x^3 Q(x) - P(x)$. Sustituyendo las expresiones de $P(x)$ y $Q(x)$, obtenemos:
$$R(x) = x^3(dx^2 + ex + g) - (ax^2 + bx + c) = dx^5 + ex^4 + gx^3 - ax^2 - bx - c$$

Como $R(x)$ es un polinomio de grado 5 cuyas raíces son $1, 2, 3, 4, 5$, podemos factorizarlo como:
$$R(x) = d(x - 1)(x - 2)(x - 3)(x - 4)(x - 5)$$

Queremos calcular $f(0) = \frac{P(0)}{Q(0)} = \frac{c}{g}$. Observando el desarrollo de $R(x)$, notamos que:
- $g$ es el coeficiente de $x^3$ en $R(x)$.
- $-c$ es el término independiente de $R(x)$ (es decir, $R(0)$).

Usando las fórmulas de Vieta para el polinomio mónico $(x - 1)(x - 2)(x - 3)(x - 4)(x - 5) = x^5 - e_1 x^4 + e_2 x^3 - e_3 x^2 + e_4 x - e_5$:

1. El coeficiente de $x^3$ en $R(x)$ es $g = d \cdot e_2$, donde $e_2$ es la suma de los productos de las raíces tomadas de dos en dos:
$$e_2 = \frac{(1+2+3+4+5)^2 - (1^2+2^2+3^2+4^2+5^2)}{2} = \frac{15^2 - 55}{2} = \frac{225 - 55}{2} = 85$$
Por lo tanto, $g = 85d$.

2. Evaluando en $x = 0$, tenemos $R(0) = -c = -d \cdot e_5$, donde $e_5$ es el producto de las raíces:
$$e_5 = 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 = 120$$
Por lo tanto, $c = 120d$.

Finalmente, calculamos $f(0)$:
$$f(0) = \frac{P(0)}{Q(0)} = \frac{c}{g} = \frac{120d}{85d} = \frac{24}{17}$$

\boxed{\frac{24}{17}}