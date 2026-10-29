Para encontrar el número de pares ordenados $(x, y)$ de números enteros que satisfacen la desigualdad $|x + yi| \le 6$, primero expresamos el módulo del número complejo en términos de $x$ e $y$:

$$\sqrt{x^2 + y^2} \le 6$$

Elevando ambos lados al cuadrado, obtenemos la condición equivalente:

$$x^2 + y^2 \le 36$$

Como $x$ e $y$ deben ser números enteros, podemos contar las soluciones posibles para $y$ según cada valor entero posible de $x$ (desde $-6$ hasta $6$):

1. **Si $x = 0$:**
   $$0^2 + y^2 \le 36 \implies y^2 \le 36 \implies -6 \le y \le 6$$
   Hay $13$ valores posibles para $y$.

2. **Si $x = \pm 1$:**
   $$(\pm 1)^2 + y^2 \le 36 \implies y^2 \le 35 \implies -5 \le y \le 5$$
   Hay $11$ valores posibles para $y$ por cada valor de $x$ ($2 \times 11 = 22$ pares).

3. **Si $x = \pm 2$:**
   $$(\pm 2)^2 + y^2 \le 36 \implies y^2 \le 32 \implies -5 \le y \le 5$$
   Hay $11$ valores posibles para $y$ por cada valor de $x$ ($2 \times 11 = 22$ pares).

4. **Si $x = \pm 3$:**
   $$(\pm 3)^2 + y^2 \le 36 \implies y^2 \le 27 \implies -5 \le y \le 5$$
   Hay $11$ valores posibles para $y$ por cada valor de $x$ ($2 \times 11 = 22$ pares).

5. **Si $x = \pm 4$:**
   $$(\pm 4)^2 + y^2 \le 36 \implies y^2 \le 20 \implies -4 \le y \le 4$$
   Hay $9$ valores posibles para $y$ por cada valor de $x$ ($2 \times 9 = 18$ pares).

6. **Si $x = \pm 5$:**
   $$(\pm 5)^2 + y^2 \le 36 \implies y^2 \le 11 \implies -3 \le y \le 3$$
   Hay $7$ valores posibles para $y$ por cada valor de $x$ ($2 \times 7 = 14$ pares).

7. **Si $x = \pm 6$:**
   $$(\pm 6)^2 + y^2 \le 36 \implies y^2 \le 0 \implies y = 0$$
   Hay $1$ valor posible para $y$ por cada valor de $x$ ($2 \times 1 = 2$ pares).

Sumando todos los casos obtenemos el total de pares ordenados:

$$13 + 22 + 22 + 22 + 18 + 14 + 2 = 113$$

\boxed{113}