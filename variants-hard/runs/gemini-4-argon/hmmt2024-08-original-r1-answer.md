Para hallar el menor valor posible de $1000a + 100b + 10c + d$, analicemos primero la condición dada elevando ambos lados de la ecuación al cuadrado.

Sabemos que para cualquier número complejo $z$, se cumple $|z|^2 = z\overline{z}$. Dado que $|\zeta| = 1$, el conjugado de $\zeta^k$ es $\overline{\zeta^k} = \zeta^{-k}$. Por lo tanto:
$$
\left|\zeta^{a}+\zeta^{b}+\zeta^{c}+\zeta^{d}\right|^2 = (\zeta^{a}+\zeta^{b}+\zeta^{c}+\zeta^{d})(\zeta^{-a}+\zeta^{-b}+\zeta^{-c}+\zeta^{-d}) = 3
$$

Al expandir el producto de la izquierda, obtenemos 4 términos iguales a $\zeta^0 = 1$ y 12 términos cruzados:
$$
4 + \sum_{x \neq y \in \{a,b,c,d\}} \zeta^{x-y} = 3 \implies \sum_{x \neq y \in \{a,b,c,d\}} \zeta^{x-y} = -1
$$

Como $\zeta = e^{2\pi i / 13}$ es una raíz primitiva decimotercera de la unidad, su polinomio mínimo sobre $\mathbb{Q}$ es el polinomio ciclotómico:
$$
1 + \zeta + \zeta^2 + \dots + \zeta^{12} = 0 \implies \sum_{k=1}^{12} \zeta^k = -1
$$

Dado que la suma $\sum_{x \neq y} \zeta^{x-y}$ consta exactamente de 12 términos y el polinomio ciclotómico es irreducible, la única forma de que esta suma sea igual a $-1$ es que las 12 diferencias $x - y \pmod{13}$ para $x \neq y$ recorran todos los residuos no nulos $1, 2, \dots, 12$ módulo $13$, exactamente una vez cada uno.

Consideremos las 6 diferencias positivas entre los cuatro enteros $a > b > c > d \ge 1$:
$$
a-b, \quad a-c, \quad a-d, \quad b-c, \quad b-d, \quad c-d
$$

Para minimizar $1000a + 100b + 10c + d$, debemos minimizar primero $a$, luego $b$, luego $c$ y finalmente $d$:
1. Como las 6 diferencias positivas deben ser todas distintas entre sí (pues son incongruentes módulo 13), la mayor de ellas, que es $a - d$, debe ser al menos $6$.
2. Como $d$ es un entero positivo, $d \ge 1$, lo que implica que:
   $$a = d + (a - d) \ge 1 + 6 = 7$$
3. Para alcanzar el valor mínimo $a = 7$, necesitamos que $d = 1$ y que las 6 diferencias positivas sean exactamente el conjunto $\{1, 2, 3, 4, 5, 6\}$. Notemos que con estas diferencias, sus opuestos $-1, -2, -3, -4, -5, -6$ son congruentes a $12, 11, 10, 9, 8, 7 \pmod{13}$, cubriendo así todos los residuos no nulos módulo 13.

Ahora buscamos $b$ y $c$ tales que $7 > b > c > 1$ y las diferencias entre $\{7, b, c, 1\}$ sean $\{1, 2, 3, 4, 5, 6\}$:
- La diferencia $6$ ya se obtiene con $7 - 1 = 6$.
- Para obtener la diferencia $5$, debemos tener $c = 2$ (pues $7 - 2 = 5$) o $b = 6$ (pues $6 - 1 = 5$).
- Como queremos minimizar $b$, probamos el caso $c = 2$. Los elementos son $\{7, b, 2, 1\}$, cuyas diferencias conocidas son $7 - 1 = 6$, $7 - 2 = 5$ y $2 - 1 = 1$.
- Necesitamos que las diferencias restantes ($7 - b$, $b - 2$ y $b - 1$) sean $\{2, 3, 4\}$. Eligiendo $b = 5$, obtenemos:
  $$7 - 5 = 2, \quad 5 - 2 = 3, \quad 5 - 1 = 4$$
  lo cual cumple todas las condiciones.

Así, la cuádrupla que minimiza la expresión es $(a, b, c, d) = (7, 5, 2, 1)$, dando como resultado:
$$
1000(7) + 100(5) + 10(2) + 1 = 7521
$$

\boxed{7521}