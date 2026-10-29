Para determinar qué enteros positivos $n \leq 100$ hacen que el polinomio $f(x) = x^4 + 20x^2 + n$ sea *breakable* (reducible módulo $p$ para todo número primo $p$), analizamos la factorización de $f(x)$ en $\mathbb{F}_p[x]$.

### Paso 1: Condición de reducibilidad módulo $p$
Como $f(x)$ es mónico de grado $4$, existen polinomios $g_p, h_p \in \mathbb{Z}[x]$ con $\deg g_p, \deg h_p < 4$ tales que $f \equiv g_p h_p \pmod p$ si y solo si $f(x)$ es reducible en $\mathbb{F}_p[x]$.

Notemos que $f(-x) = f(x)$. Si $f(x)$ tiene una raíz $r \in \mathbb{F}_p$, entonces $-r$ también es raíz. Por tanto, siempre que $f(x)$ sea reducible en $\mathbb{F}_p[x]$, debe factorizar como el producto de dos polinomios cuadráticos mónicos en $\mathbb{F}_p[x]$:
$$x^4 + 20x^2 + n \equiv (x^2 + cx + d)(x^2 - cx + e) \pmod p$$
Igualando coeficientes módulo $p$, obtenemos el sistema:
1. $d + e - c^2 \equiv 20 \pmod p$
2. $c(e - d) \equiv 0 \pmod p$
3. $de \equiv n \pmod p$

Para un primo impar $p$, la ecuación $c(e - d) \equiv 0 \pmod p$ nos da dos casos posibles:

- **Caso A ($c \equiv 0 \pmod p$):** Entonces $d + e \equiv 20 \pmod p$ y $de \equiv n \pmod p$. Esto ocurre si y solo si el discriminante de $t^2 - 20t + n$ es un cuadrado en $\mathbb{F}_p$, es decir, si $20^2 - 4n = 4(100 - n)$ es un residuo cuadrático módulo $p$ (o congruente con $0$). Equivalentemente, $100 - n$ es un cuadrado en $\mathbb{F}_p$.

- **Caso B ($c \not\equiv 0 \pmod p$):** Entonces $d \equiv e \pmod p$, por lo que $d^2 \equiv n \pmod p$ y $c^2 \equiv 2d - 20 \pmod p$. Para que existan tales $c, d \in \mathbb{F}_p$, es necesario que $n$ sea un cuadrado módulo $p$ ($d \equiv \pm\sqrt{n} \pmod p$) y que al menos uno de los valores $2d - 20$ o $-2d - 20$ sea un cuadrado módulo $p$.

Observemos que el producto de estos dos valores es:
$$(2d - 20)(-2d - 20) = 400 - 4d^2 \equiv 4(100 - n) \pmod p$$
Por la multiplicatividad del símbolo de Legendre, si $100 - n$ **no** es un residuo cuadrático módulo $p$, entonces el producto $(2d - 20)(-2d - 20)$ tampoco lo es, lo que garantiza que exactamente uno de los dos factores ($2d - 20$ o $-2d - 20$) es un residuo cuadrático módulo $p$.

### Paso 2: Caracterización para todo primo $p$
De lo anterior se deduce que:
- Para $p = 2$, $f(x) \equiv x^4 + n \equiv (x^2 + n)^2 \pmod 2$, que siempre es reducible.
- Para cualquier primo impar $p$, $f(x)$ es reducible módulo $p$ si y solo si **al menos uno** de los enteros $100 - n$ o $n$ es un cuadrado módulo $p$.

Por la ley de reciprocidad cuadrática y el teorema de Dirichlet (o el teorema de densidad de Chebotarev), la condición de que para *todo* primo impar $p$ al menos uno de los números $n$ o $100 - n$ sea un residuo cuadrático módulo $p$ se cumple si y solo si al menos uno de los números $n$ o $100 - n$ es un cuadrado perfecto en $\mathbb{Z}$:
- Si ni $n$ ni $100 - n$ son cuadrados perfectos, siempre existen infinitos primos $p$ tales que $\left(\frac{n}{p}\right) = -1$ y $\left(\frac{100 - n}{p}\right) = -1$ (tanto si $n(100 - n)$ es un cuadrado perfecto como si no lo es), para los cuales $f(x)$ es irreducible módulo $p$.

### Paso 3: Cálculo de la suma de los valores de $n$
Buscamos todos los enteros $1 \leq n \leq 100$ tales que $n = m^2$ o $100 - n = k^2$ para algunos enteros $m, k$:

1. **Cuando $n = m^2$ ($1 \leq m \leq 10$):**
   $$n \in \{1, 4, 9, 16, 25, 36, 49, 64, 81, 100\}$$
2. **Cuando $n = 100 - k^2$ ($0 \leq k \leq 9$):**
   $$n \in \{100, 99, 96, 91, 84, 75, 64, 51, 36, 19\}$$

Las intersecciones entre ambos conjuntos corresponden a las soluciones enteras de $m^2 + k^2 = 100$, que dan $n \in \{36, 64, 100\}$.

Agrupando los elementos de la unión en pares que suman $100$:
- Para $m \in \{1, 2, 3, 4, 5, 7, 9\}$, cada par $\{m^2, 100 - m^2\}$ contiene dos elementos distintos cuya suma es $100$. Esto aporta $7 \times 100 = 700$.
- Los elementos restantes de la unión son $36$, $64$ y $100$, cuya suma es $36 + 64 + 100 = 200$.

Por lo tanto, la suma total es:
$$700 + 200 = 900$$

\boxed{900}