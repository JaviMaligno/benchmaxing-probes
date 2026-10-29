Para calcular la suma
$$S = \sum_{k=-1200}^{1200}\left\lfloor\frac{3150}{k+0.5}\right\rfloor$$
primero reescribimos el argumento de la función piso multiplicando el numerador y el denominador por $2$:
$$\frac{3150}{k+0.5} = \frac{6300}{2k+1}$$

Observemos el comportamiento del denominador $m = 2k+1$ a medida que $k$ varía desde $-1200$ hasta $1200$:
- Para $k = -1200$, $2k+1 = -2399$.
- Para $k = -1$, $2k+1 = -1$.
- Para $k = 0$, $2k+1 = 1$.
- Para $k = 1199$, $2k+1 = 2399$.
- Para $k = 1200$, $2k+1 = 2401$.

Por lo tanto, podemos agrupar los términos para $k \in \{0, 1, \dots, 1199\}$ con sus respectivos términos simétricos $k' = -k-1 \in \{-1, -2, \dots, -1200\}$, dejando aparte el término correspondiente a $k = 1200$:
$$S = \left\lfloor\frac{6300}{2401}\right\rfloor + \sum_{k=0}^{1199} \left( \left\lfloor\frac{6300}{2k+1}\right\rfloor + \left\lfloor-\frac{6300}{2k+1}\right\rfloor \right)$$

Recordemos la propiedad fundamental de la función piso para cualquier número real $x$:
$$\lfloor x \rfloor + \lfloor -x \rfloor = \begin{cases} 0 & \text{si } x \in \mathbb{Z}, \\ -1 & \text{si } x \notin \mathbb{Z}. \end{cases}$$

Analicemos para cuántos valores de $k \in \{0, 1, \dots, 1199\}$ la fracción $\frac{6300}{2k+1}$ es un número entero:
1. Como $m = 2k+1$ es impar, $m$ divide a $6300$ si y solo si $m$ divide a la parte impar de $6300$.
2. Factorizando $6300$ en primos:
   $$6300 = 2^2 \times 3^2 \times 5^2 \times 7^1$$
   La parte impar es $3^2 \times 5^2 \times 7^1 = 1575$.
3. El número total de divisores positivos de $1575$ es:
   $$(2+1)(2+1)(1+1) = 3 \times 3 \times 2 = 18$$
4. Como el mayor divisor impar de $6300$ es $1575$ y $1575 \le 2399$, los $18$ divisores impares positivos están incluidos dentro del rango $1 \le 2k+1 \le 2399$.

De los $1200$ pares de términos en la sumatoria:
- $18$ pares corresponden a valores enteros y aportan $0$ a la suma.
- Los restantes $1200 - 18 = 1182$ pares corresponden a valores no enteros y aportan $-1$ cada uno.

Finalmente, evaluamos el término restante para $k = 1200$:
$$\left\lfloor\frac{6300}{2401}\right\rfloor = 2 \quad (\text{ya que } 2 \times 2401 = 4802 \le 6300 < 7203 = 3 \times 2401)$$

Sumando todas las contribuciones obtenemos:
$$S = 2 + 18(0) + 1182(-1) = 2 - 1182 = -1180$$

\boxed{-1180}