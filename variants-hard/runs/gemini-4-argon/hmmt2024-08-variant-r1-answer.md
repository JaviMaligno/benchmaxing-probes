Para resolver el problema paso a paso, definamos la suma dentro del módulo como:
$$S = \omega^a + \omega^b + \omega^c + \omega^d$$

Dado que $\omega = \cos \frac{2\pi}{13} + i\sin \frac{2\pi}{13}$ es una raíz primitiva $13$-ésima de la unidad, cumple que $|\omega| = 1$, $\overline{\omega^k} = \omega^{-k}$ y su polinomio mínimo sobre $\mathbb{Q}$ es el polinomio ciclotómico:
$$\Phi_{13}(x) = 1 + x + x^2 + \dots + x^{12} = 0$$

### Paso 1: Caracterización de los exponentes módulo 13
Elevando al cuadrado la condición $|S| = \sqrt{3}$, obtenemos:
$$|S|^2 = S \overline{S} = \left(\omega^a + \omega^b + \omega^c + \omega^d\right)\left(\omega^{-a} + \omega^{-b} + \omega^{-c} + \omega^{-d}\right) = 3$$

Al expandir el producto, hay $4$ términos de la forma $\omega^{x_i - x_i} = \omega^0 = 1$ y $12$ términos cruzados de la forma $\omega^{x_i - x_j}$ con $i \neq j$, donde $\{x_1, x_2, x_3, x_4\} = \{a, b, c, d\}$:
$$4 + \sum_{i \neq j} \omega^{x_i - x_j} = 3 \implies \sum_{i \neq j} \omega^{x_i - x_j} = -1$$

Como sabemos que $\omega + \omega^2 + \dots + \omega^{12} = -1$ y $\Phi_{13}(x)$ es irreducible sobre $\mathbb{Q}$, la única manera de que la suma de $12$ potencias de $\omega$ sea igual a $-1$ es que los $12$ exponentes $x_i - x_j \pmod{13}$ (para $i \neq j$) tomen exactamente una vez cada uno de los valores $\{1, 2, \dots, 12\}$.

En otras palabras, los residuos de $\{a, b, c, d\}$ módulo $13$ deben formar un **conjunto de diferencias perfecto** $(13, 4, 1)$.

### Paso 2: Estructura de los residuos y paridad
Si colocamos los $4$ residuos en un círculo de longitud $13$, estos dividen el círculo en $4$ arcos cuyas longitudes enteras positivas suman $13$. Para que las diferencias entre los elementos generen todos los valores del $1$ al $12$ módulo $13$, las $4$ longitudes de arco adyacentes deben ser una rotación de $(1, 2, 6, 4)$ o de su reflejo $(1, 4, 6, 2)$.

Para minimizar $1000a + 100b + 10c + d$ con $a > b > c > d \ge 1$ impares, buscamos minimizar primero $a$. Supongamos que $1 \le d < c < b < a$ están contenidos en un rango menor o igual a $13$, de modo que su orden como enteros coincide con su orden cíclico módulo $13$. Las longitudes de los $4$ arcos consecutivos son:
$$c - d, \quad b - c, \quad a - b, \quad \text{y} \quad (d + 13) - a$$

Como $a, b, c, d$ son todos números **impares**:
- Las tres diferencias $c - d$, $b - c$ y $a - b$ son **pares**.
- La diferencia restante $(d + 13) - a$ es **impar** (ya que $a - d$ es par y $13$ es impar).

Observando las longitudes de arco $\{1, 2, 6, 4\}$, notamos que hay exactamente un número impar ($1$) y tres números pares ($2, 6, 4$). Por lo tanto, obligatoriamente debe cumplirse que el arco impar sea $1$:
$$(d + 13) - a = 1 \implies a - d = 12$$

### Paso 3: Minimización de $a, b, c, d$
Como $d \ge 1$ es un entero positivo impar y $a = d + 12$, el menor valor posible para $a$ se obtiene cuando $d = 1$, lo cual nos da:
$$d = 1, \quad a = 13$$

Las tres diferencias $(c - d, b - c, a - b)$ deben corresponder a las longitudes pares en orden cíclico, es decir, $(2, 6, 4)$ o $(4, 6, 2)$:
1. Si $(c - d, b - c, a - b) = (2, 6, 4)$:
   - $d = 1$
   - $c = 1 + 2 = 3$
   - $b = 3 + 6 = 9$
   - $a = 9 + 4 = 13$
2. Si $(c - d, b - c, a - b) = (4, 6, 2)$:
   - $d = 1$
   - $c = 1 + 4 = 5$
   - $b = 5 + 6 = 11$
   - $a = 11 + 2 = 13$

La primera cuádrupla $(a, b, c, d) = (13, 9, 3, 1)$ minimiza simultáneamente $a, b, c$ y $d$. Sustituyendo estos valores en la expresión pedida:
$$1000a + 100b + 10c + d = 1000(13) + 100(9) + 10(3) + 1 = 13931$$

\boxed{13931}