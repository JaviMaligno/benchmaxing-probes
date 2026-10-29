Vamos a resolverlo paso a paso.

**Paso 1: Condición sobre el signo de $x$.**

Como $x^3$ debe ser un factor **positivo** de $10!$, se requiere $x^3 > 0$. Como el cubo conserva el signo, esto implica $x > 0$ (el caso $x=0$ da $x^3=0$, que no es un factor positivo, y $x<0$ daría $x^3<0$). Así que $x$ debe ser un entero positivo.

**Paso 2: Factorización de $10!$.**

$$10! = 1\cdot 2\cdot 3\cdots 10 = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7$$

(Exponentes: los múltiplos de 2 hasta 10 aportan $5+2+1=8$ factors de 2; los de 3 aportan $3+1=4$; los de 5 aportan $2$; el 7 aporta $1$.)

**Paso 3: Condición para que $x^3 \mid 10!$.**

Escribamos $x = 2^a \cdot 3^b \cdot 5^c \cdot 7^d$. Entonces $x^3 = 2^{3a}\cdot 3^{3b}\cdot 5^{3c}\cdot 7^{3d}$, y necesitamos que cada exponente no supere al de $10!$:

- $3a \le 8 \Rightarrow a \in \{0, 1, 2\}$ → **3 opciones**
- $3b \le 4 \Rightarrow b \in \{0, 1\}$ → **2 opciones**
- $3c \le 2 \Rightarrow c = 0$ → **1 opción**
- $3d \le 1 \Rightarrow d = 0$ → **1 opción**

**Paso 4: Conteo.**

$$3 \times 2 \times 1 \times 1 = 6$$

(Verificación: los valores de $x$ son $1, 2, 3, 4, 6, 12$; por ejemplo, $12^3 = 1728$ y $10!/1728 = 2100$, que es entero.)

$$\boxed{6}$$