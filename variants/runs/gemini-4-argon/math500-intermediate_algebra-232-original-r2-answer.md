Para encontrar el número de pares ordenados $(a,b)$ de números enteros tales que $|a + bi| \le 5$, primero expresamos el módulo del número complejo en función de $a$ y $b$:

$$|a + bi| = \sqrt{a^2 + b^2} \le 5$$

Elevando ambos lados al cuadrado (dado que ambos lados son no negativos), obtenemos la desigualdad equivalente:

$$a^2 + b^2 \le 25$$

Dado que $a$ y $b$ son números enteros, $a^2 \le 25$, lo que significa que $a$ puede tomar valores enteros desde $-5$ hasta $5$. Analizamos el número de valores enteros posibles para $b$ según cada valor de $|a|$:

1. **Si $a = 0$:**
   $$0^2 + b^2 \le 25 \implies b^2 \le 25 \implies -5 \le b \le 5$$
   Hay $5 - (-5) + 1 = 11$ valores posibles para $b$.

2. **Si $a = \pm 1$:**
   $$(\pm 1)^2 + b^2 \le 25 \implies b^2 \le 24 \implies -4 \le b \le 4$$
   Hay $4 - (-4) + 1 = 9$ valores posibles para $b$ por cada valor de $a$. En total: $2 \times 9 = 18$ pares.

3. **Si $a = \pm 2$:**
   $$(\pm 2)^2 + b^2 \le 25 \implies b^2 \le 21 \implies -4 \le b \le 4$$
   Hay $9$ valores posibles para $b$ por cada valor de $a$. En total: $2 \times 9 = 18$ pares.

4. **Si $a = \pm 3$:**
   $$(\pm 3)^2 + b^2 \le 25 \implies b^2 \le 16 \implies -4 \le b \le 4$$
   Hay $9$ valores posibles para $b$ por cada valor de $a$. En total: $2 \times 9 = 18$ pares.

5. **Si $a = \pm 4$:**
   $$(\pm 4)^2 + b^2 \le 25 \implies b^2 \le 9 \implies -3 \le b \le 3$$
   Hay $3 - (-3) + 1 = 7$ valores posibles para $b$ por cada valor de $a$. En total: $2 \times 7 = 14$ pares.

6. **Si $a = \pm 5$:**
   $$(\pm 5)^2 + b^2 \le 25 \implies b^2 \le 0 \implies b = 0$$
   Hay $1$ valor posible para $b$ por cada valor de $a$. En total: $2 \times 1 = 2$ pares.

Sumando todos los casos obtenemos el total de pares ordenados $(a,b)$:

$$11 + 18 + 18 + 18 + 14 + 2 = 81$$

\boxed{81}