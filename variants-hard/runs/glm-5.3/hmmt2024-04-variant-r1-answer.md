# Razonamiento

**Paso 1: Plantear la estructura.** Sea $g(x) = \frac{P(x)}{Q(x)}$ con $\deg P \le 2$ y $\deg Q \le 2$. La condición $g(k) = k^3$ para $k \in \{1,2,3,4,6\}$ significa que $P(k) = k^3 Q(k)$, es decir:

$$F(x) := P(x) - x^3 Q(x) = 0 \quad \text{para } x = 1, 2, 3, 4, 6.$$

**Paso 2: Grado de $F$.** Como $\deg P \le 2$ y $\deg(x^3 Q) \le 5$, se tiene $\deg F \le 5$. Si $\deg F \le 4$, entonces $F$ tendría 5 raíces distintas y sería idénticamente cero, lo que forzaría $P = x^3Q$ con grado $\ge 3$: contradicción. Por lo tanto $\deg F = 5$ y:

$$F(x) = A\,(x-1)(x-2)(x-3)(x-4)(x-6), \qquad A \neq 0.$$

**Paso 3: Comparar coeficientes.** Con $\pi(x) = (x-1)(x-2)(x-3)(x-4)(x-6) = x^5 - e_1x^4 + e_2x^3 - \cdots$, donde $\{r_i\} = \{1,2,3,4,6\}$:

- $e_1 = 1+2+3+4+6 = 16$
- $e_2 = \sum_{i<j} r_ir_j = 95$  (suma de $2,3,4,6,6,8,12,12,18,24$)
- $e_5 = 1\cdot2\cdot3\cdot4\cdot6 = 144$

Si $Q(x) = q_2x^2 + q_1x + q_0$, los coeficientes de $x^5, x^4, x^3$ en $F = P - x^3Q$ son $-q_2, -q_1, -q_0$, mientras que en $A\pi$ son $A, -16A, 95A$. Igualando:

$$q_2 = -A, \qquad q_1 = 16A, \qquad q_0 = -95A.$$

En particular $q_2 \neq 0$ (así que $Q$ es genuinamente cuadrática y $Q(0) = -95A \neq 0$).

**Paso 4: Evaluar en $x = 0$.** Como $0^3 = 0$:

$$P(0) = F(0) = A\,(-1)(-2)(-3)(-4)(-6) = -144A.$$

Por lo tanto:

$$g(0) = \frac{P(0)}{Q(0)} = \frac{-144A}{-95A} = \frac{144}{95}.$$

**Verificación.** De hecho $g$ queda unívocamente determinada: con $A = -1$ se obtiene $g(x) = \frac{260x^2 - 324x + 144}{x^2 - 16x + 95}$, y se comprueba $g(1) = \frac{80}{80} = 1$, $g(2) = \frac{536}{67} = 8$, $g(3) = \frac{1512}{56} = 27$, $g(4) = \frac{3008}{47} = 64$, $g(6) = \frac{7560}{35} = 216$. Todo coincide con $k^3$. ✓

$$\boxed{\dfrac{144}{95}}$$