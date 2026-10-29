Para encontrar el número de pares ordenados $(a,b)$ de números enteros tales que $|a + bi| \le 5$, primero expresamos el módulo del número complejo en términos de $a$ y $b$:

$$|a + bi| = \sqrt{a^2 + b^2} \le 5$$

Elevando ambos lados al cuadrado (dado que ambos lados son no negativos), obtenemos la desigualdad equivalente:

$$a^2 + b^2 \le 25$$

Como $a$ y $b$ son números enteros, $a^2 \le 25$ implica que $a$ puede tomar valores enteros desde $-5$ hasta $5$. Podemos contar el número de soluciones enteras para $b$ analizando cada caso posible para $|a|$:

1. **Si $a = 0$:**
   $$0^2 + b^2 \le 25 \implies b^2 \le 25 \implies -5 \le b \le 5$$
   Esto nos da $11$ valores posibles para $b$ ($-5, -4, \dots, 4, 5$).
   Total para $a = 0$: **$11$ pares**.

2. **Si $a = \pm 1$:**
   $$1^2 + b^2 \le 25 \implies b^2 \le 24 \implies -4 \le b \le 4$$
   Esto nos da $9$ valores posibles para $b$ por cada valor de $a$.
   Total para $a = \pm 1$: $2 \times 9 =$ **$18$ pares**.

3. **Si $a = \pm 2$:**
   $$2^2 + b^2 \le 25 \implies b^2 \le 21 \implies -4 \le b \le 4$$
   Esto nos da $9$ valores posibles para $b$ por cada valor de $a$.
   Total para $a = \pm 2$: $2 \times 9 =$ **$18$ pares**.

4. **Si $a = \pm 3$:**
   $$3^2 + b^2 \le 25 \implies b^2 \le 16 \implies -4 \le b \le 4$$
   Esto nos da $9$ valores posibles para $b$ por cada valor de $a$.
   Total para $a = \pm 3$: $2 \times 9 =$ **$18$ pares**.

5. **Si $a = \pm 4$:**
   $$4^2 + b^2 \le 25 \implies b^2 \le 9 \implies -3 \le b \le 3$$
   Esto nos da $7$ valores posibles para $b$ por cada valor de $a$.
   Total para $a = \pm 4$: $2 \times 7 =$ **$14$ pares**.

6. **Si $a = \pm 5$:**
   $$5^2 + b^2 \le 25 \implies b^2 \le 0 \implies b = 0$$
   Esto nos da $1$ valor posible para $b$ por cada valor de $a$.
   Total para $a = \pm 5$: $2 \times 1 =$ **$2$ pares**.

Finalmente, sumamos la cantidad de pares de todos los casos:

$$11 + 18 + 18 + 18 + 14 + 2 = 81$$

\boxed{81}