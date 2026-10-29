# Resolución paso a paso

**Planteamiento.** Como $a_n = 2$ y las $n$ raíces $r_1, \dots, r_n$ son enteros distintos, podemos escribir
$$f(x) = 2\prod_{i=1}^{n}(x - r_i).$$

**Condición 1 (término independiente).** Evaluando en $x=0$:
$$a_0 = 2(-1)^n \prod_{i=1}^n r_i = 66 \quad\Longrightarrow\quad \prod_{i=1}^n r_i = (-1)^n \cdot 33.$$
Por tanto $|r_1 r_2 \cdots r_n| = 33 = 3\cdot 11$, así que cada $|r_i|$ divide a 33: $|r_i| \in \{1, 3, 11, 33\}$.

**Condición 2 (coeficiente buscado).** El coeficiente de $x^{n-1}$ es
$$a_{n-1} = -2\sum_{i=1}^n r_i \quad\Longrightarrow\quad |a_{n-1}| = 2\left|\sum r_i\right|.$$

**Enumerar configuraciones posibles.** Como los enteros son distintos, el valor absoluto 1 puede aparecer a lo sumo dos veces (como $1$ y $-1$), y los valores $3, 11, 33$ a lo sumo una vez cada uno. Las multifilas de valores absolutos con producto 33 son:

- $n=1$: $\{33\}$ — solo $r=-33$; $|a_{n-1}| = 66$.
- $n=2$: $\{3,11\}$ o $\{1,33\}$, con producto $+33$: mejores sumas $\pm 14$ o $\pm 34$, mínimo $|a_1| = 28$.
- $n=3$ (producto $-33$): 
  - $\{1,3,11\}$ con un número impar de negativos: sumas $13, 9, -7, -15$ → mínimo $|\text{suma}| = 7$.
  - $\{1,-1,33\}$: suma $33$ → $66$.
- $n=4$ (producto $+33$): $\{1,-1,\pm 3,\pm 11\}$ con signos de producto $+33$: sumas $\pm 8$ → $|a_3| = 16$.

Para $n \ge 5$ haría falta repetir el valor absoluto 1 tres veces, lo cual es imposible.

**Verificación del mejor caso ($n=3$).** Con raíces $1, 3, -11$:
$$f(x) = 2(x-1)(x-3)(x+11) = 2x^3 + 14x^2 - 82x + 66,$$
donde $a_3 = 2$, $a_0 = 66$ y $a_2 = 14$. La suma de raíces es $1+3-11 = -7$, así que $|a_{n-1}| = 2\cdot 7 = 14$.

Comparando todos los casos: $66, 28, 14, 16, \dots$, el mínimo es $14$.

$$\boxed{14}$$