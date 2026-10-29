## Solución paso a paso

**Paso 1: Factorización de $12!$.**

Contamos los factores primos de $12! = 1\cdot 2 \cdots 12$:

- Potencias de $2$: $\left\lfloor \tfrac{12}{2} \right\rfloor + \left\lfloor \tfrac{12}{4} \right\rfloor + \left\lfloor \tfrac{12}{8} \right\rfloor = 6+3+1 = 10$
- Potencias de $3$: $\left\lfloor \tfrac{12}{3} \right\rfloor + \left\lfloor \tfrac{12}{9} \right\rfloor = 4+1 = 5$
- Potencias de $5$: $\left\lfloor \tfrac{12}{5} \right\rfloor = 2$
- Potencias de $7$: $\left\lfloor \tfrac{12}{7} \right\rfloor = 1$
- Potencias de $11$: $\left\lfloor \tfrac{12}{11} \right\rfloor = 1$

Entonces:
$$12! = 2^{10} \cdot 3^{5} \cdot 5^{2} \cdot 7^{1} \cdot 11^{1}$$

**Paso 2: Condición sobre $y$.**

Si $y = 2^{a} \cdot 3^{b} \cdot 5^{c} \cdot 7^{d} \cdot 11^{e}$, entonces $y^3$ divide a $12!$ si y solo si cada exponente de $y^3$ no excede al de $12!$, es decir, $3a \le 10$, $3b \le 5$, $3c \le 2$, $3d \le 1$, $3e \le 1$.

**Paso 3: Contar los valores posibles de cada exponente.**

- $a \in \{0,1,2,3\}$: **4 opciones** (pues $3\cdot 3 = 9 \le 10$)
- $b \in \{0,1\}$: **2 opciones** (pues $3 \cdot 1 = 3 \le 5$)
- $c \in \{0\}$: **1 opción** (pues $3 \cdot 1 = 3 > 2$)
- $d \in \{0\}$: **1 opción**
- $e \in \{0\}$: **1 opción**

**Paso 4: Total.**

Por el principio multiplicativo:
$$4 \cdot 2 \cdot 1 \cdot 1 \cdot 1 = 8$$

$\boxed{8}$