Para encontrar el número de pares ordenados $(x, y)$ de números enteros que satisfacen la desigualdad $|x + yi| \le 6$, primero utilizamos la definición del módulo de un número complejo:

$$|x + yi| = \sqrt{x^2 + y^2} \le 6$$

Elevando ambos lados al cuadrado (dado que ambos lados son no negativos), obtenemos una condición equivalente:

$$x^2 + y^2 \le 36$$

Dado que $x$ e $y$ son números enteros, los posibles valores para $x$ están en el rango $-6 \le x \le 6$. Podemos contar el número de valores enteros posibles para $y$ para cada valor de $x$:

1. **Si $x = 0$:**
   $$0^2 + y^2 \le 36 \implies y^2 \le 36 \implies -6 \le y \le 6$$
   Esto nos da $6 - (-6) + 1 = 13$ valores para $y$.

2. **Si $x = \pm 1$:**
   $$(\pm 1)^2 + y^2 \le 36 \implies y^2 \le 35 \implies -5 \le y \le 5$$
   Esto nos da $11$ valores para $y$ por cada uno de los dos valores de $x$, sumando $2 \times 11 = 22$ pares.

3. **Si $x = \pm 2$:**
   $$(\pm 2)^2 + y^2 \le 36 \implies y^2 \le 32 \implies -5 \le y \le 5$$
   Esto nos da $11$ valores para $y$ por cada valor de $x$, sumando $2 \times 11 = 22$ pares.

4. **Si $x = \pm 3$:**
   $$(\pm 3)^2 + y^2 \le 36 \implies y^2 \le 27 \implies -5 \le y \le 5$$
   Esto nos da $11$ valores para $y$ por cada valor de $x$, sumando $2 \times 11 = 22$ pares.

5. **Si $x = \pm 4$:**
   $$(\pm 4)^2 + y^2 \le 36 \implies y^2 \le 20 \implies -4 \le y \le 4$$
   Esto nos da $9$ valores para $y$ por cada valor de $x$, sumando $2 \times 9 = 18$ pares.

6. **Si $x = \pm 5$:**
   $$(\pm 5)^2 + y^2 \le 36 \implies y^2 \le 11 \implies -3 \le y \le 3$$
   Esto nos da $7$ valores para $y$ por cada valor de $x$, sumando $2 \times 7 = 14$ pares.

7. **Si $x = \pm 6$:**
   $$(\pm 6)^2 + y^2 \le 36 \implies y^2 \le 0 \implies y = 0$$
   Esto nos da $1$ valor para $y$ por cada valor de $x$, sumando $2 \times 1 = 2$ pares.

Finalmente, sumamos todos los casos posibles:

$$13 + 22 + 22 + 22 + 18 + 14 + 2 = 113$$

\boxed{113}