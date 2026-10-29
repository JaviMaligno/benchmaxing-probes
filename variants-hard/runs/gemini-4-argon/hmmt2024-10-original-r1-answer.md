Para determinar qué enteros positivos $n \leq 100$ hacen que el polinomio $f(x) = x^4 + 16x^2 + n$ sea *splitty*, analizamos primero la condición dada módulo cada número primo $p$.

### Paso 1: Traducción a reducibilidad en $\mathbb{F}_p[x]$
Sea $f(x) = x^4 + 16x^2 + n$. Como $f$ es mónico de grado $4$, su reducción $\bar{f} = f \pmod p$ en $\mathbb{F}_p[x]$ también tiene grado $4$ para todo primo $p$.

- Si existen $g_p, h_p \in \mathbb{Z}[x]$ con $\deg g_p, \deg h_p \leq 3$ tales que $f - g_p h_p$ tiene todos sus coeficientes divisibles por $p$, entonces en $\mathbb{F}_p[x]$ se cumple $\bar{f} = \bar{g}_p \bar{h}_p$, donde $\deg \bar{g}_p \leq \deg g_p \leq 3$ y $\deg \bar{h}_p \leq \deg h_p \leq 3$. Como $\deg \bar{g}_p + \deg \bar{h}_p = \deg \bar{f} = 4$, ambos polinomios $\bar{g}_p$ y $\bar{h}_p$ tienen grado al menos $1$, por lo que $\bar{f}$ es reducible en $\mathbb{F}_p[x]$.
- Recíprocamente, si $\bar{f}$ es reducible en $\mathbb{F}_p[x]$, podemos levantar sus factores a polinomios en $\mathbb{Z}[x]$ del mismo grado ($< 4$), cumpliendo la definición.

Por lo tanto, $f(x)$ es *splitty* si y solo si $f(x)$ es reducible en $\mathbb{F}_p[x]$ para todo primo $p$.

---

### Paso 2: Criterio de reducibilidad de un polinomio bicuadrático en $\mathbb{F}_p[x]$
Para $p = 2$, $x^4 + 16x^2 + n \equiv x^4 + n \equiv (x^2 + n)^2 \pmod 2$, que siempre es reducible.

Sea $p > 2$ un primo impar. Afirmamos que un polinomio bicuadrático $x^4 + ax^2 + b \in \mathbb{F}_p[x]$ es reducible en $\mathbb{F}_p[x]$ si y solo si al menos uno de los elementos $b$ o $a^2 - 4b$ es un cuadrado en $\mathbb{F}_p$:

1. **($\Rightarrow$)** Si $x^4 + ax^2 + b$ tiene un factor lineal $x - r$ en $\mathbb{F}_p[x]$, entonces $y = r^2 \in \mathbb{F}_p$ es raíz de $y^2 + ay + b = 0$, luego su discriminante $a^2 - 4b$ es un cuadrado en $\mathbb{F}_p$. Si no tiene factores lineales pero se factoriza en dos polinomios cuadráticos mónicos:
   $$x^4 + ax^2 + b = (x^2 + cx + d)(x^2 - cx + k),$$
   al igualar el coeficiente de $x$ obtenemos $c(k - d) = 0$.
   - Si $c = 0$, entonces $d + k = a$ y $dk = b$, por lo que el discriminante $(d - k)^2 = a^2 - 4b$ es un cuadrado en $\mathbb{F}_p$.
   - Si $c \neq 0$, entonces $k = d$, lo que implica que $b = d^2$ es un cuadrado en $\mathbb{F}_p$.

2. **($\Leftarrow$)** Recíprocamente:
   - Si $a^2 - 4b = s^2$ en $\mathbb{F}_p$, entonces $x^4 + ax^2 + b = \left(x^2 + \frac{a-s}{2}\right)\left(x^2 + \frac{a+s}{2}\right)$ es reducible en $\mathbb{F}_p[x]$.
   - Si $b = d^2$ en $\mathbb{F}_p$, consideramos $u = 2d - a$ y $v = -2d - a$ en $\mathbb{F}_p$. Si $u = c^2$ es un cuadrado en $\mathbb{F}_p$, entonces $x^4 + ax^2 + d^2 = (x^2 + d)^2 - c^2 x^2 = (x^2 - cx + d)(x^2 + cx + d)$. Si $v = c^2$ es un cuadrado en $\mathbb{F}_p$, entonces $x^4 + ax^2 + d^2 = (x^2 - d)^2 - c^2 x^2 = (x^2 - cx - d)(x^2 + cx - d)$. Si ni $u$ ni $v$ son cuadrados en $\mathbb{F}_p$, como el producto de dos no-cuadrados en $\mathbb{F}_p^\times$ es un cuadrado, su producto $uv = a^2 - 4d^2 = a^2 - 4b$ es un cuadrado en $\mathbb{F}_p$, reduciéndose al caso anterior.

Aplicado a $f(x) = x^4 + 16x^2 + n$ (donde $a = 16$ y $a^2 - 4b = 4(64 - n)$), concluimos que $f(x)$ es reducible módulo $p$ para todo primo $p > 2$ si y solo si para todo primo impar $p$, al menos uno de $n$ o $64 - n$ es un residuo cuadrático módulo $p$.

---

### Paso 3: Condición sobre el entero $n$
Por la ley de reciprocidad cuadrática y el teorema de Dirichlet sobre primos en progresiones aritméticas (o equivalentemente por el teorema de densidad de Chebotarev aplicado al grupo de Galois de $f$), si ni $n$ ni $64 - n$ son cuadrados perfectos en $\mathbb{Z}$, existen infinitos primos $p$ para los cuales $\left(\frac{n}{p}\right) = -1$ y $\left(\frac{64 - n}{p}\right) = -1$ (incluso si $n(64 - n)$ es un cuadrado perfecto, en cuyo caso ambos símbolos de Legendre coinciden y valen $-1$ simultáneamente para la mitad de los primos).

Por consiguiente, $x^4 + 16x^2 + n$ es *splitty* si y solo si:
$$\text{o bien } n \text{ es un cuadrado perfecto en } \mathbb{Z}, \text{ o bien } 64 - n \text{ es un cuadrado perfecto en } \mathbb{Z}.$$

---

### Paso 4: Conteo y suma para $1 \leq n \leq 100$
1. **Caso 1: $n = m^2$ es un cuadrado perfecto.**
   Para $1 \leq n \leq 100$, tenemos $m \in \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$, lo que da los valores:
   $$n \in \{1, 4, 9, 16, 25, 36, 49, 64, 81, 100\}.$$
   Su suma es:
   $$\sum_{m=1}^{10} m^2 = \frac{10 \cdot 11 \cdot 21}{6} = 385.$$

2. **Caso 2: $64 - n = k^2$ es un cuadrado perfecto ($k \geq 0$).**
   Como $n = 64 - k^2 \geq 1$, los posibles valores enteros no negativos de $k$ son $k \in \{0, 1, 2, 3, 4, 5, 6, 7\}$, que producen:
   $$n \in \{64, 63, 60, 55, 48, 39, 28, 15\}.$$
   El único valor que coincide con el Caso 1 es $n = 64$ (para $k = 0$). Excluyendo $n = 64$, la suma de los valores restantes ($k = 1, \dots, 7$) es:
   $$\sum_{k=1}^{7} (64 - k^2) = 7 \cdot 64 - \frac{7 \cdot 8 \cdot 15}{6} = 448 - 140 = 308.$$

Sumando ambos conjuntos disjuntos obtenemos el total:
$$385 + 308 = 693.$$

\boxed{693}