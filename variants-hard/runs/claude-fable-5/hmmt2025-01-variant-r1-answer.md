**La suma es 792.**

Razonamiento:

1. **Factorización:** $11! = 39\,916\,800 = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7 \cdot 11$.

2. **Restricción:** un divisor que termina en 3 es impar y no múltiplo de 5, así que debe ser de la forma $3^a \cdot 7^b \cdot 11^c$ con $0 \le a \le 4$, $b, c \in \{0,1\}$.

3. **Dígito de unidades:** las unidades de $3^a$ para $a=0,\dots,4$ son $1,3,9,7,1$. Las unidades de $7^b \cdot 11^c$ son $1$ (si $b=0$) o $7$ (si $b=1$), ya que el 11 no cambia el dígito final.
   - Si el factor $7^b 11^c$ termina en **1**: necesito $3^a$ terminando en 3, es decir $a=1$. Divisores: $3 \cdot 1 = 3$ y $3 \cdot 11 = 33$.
   - Si termina en **7**: necesito $3^a$ terminando en 9 (pues $9 \cdot 7 = 63$), es decir $a=2$. Divisores: $9 \cdot 7 = 63$ y $9 \cdot 77 = 693$.

4. **Suma:** $3 + 33 + 63 + 693 = 792$.

$$\boxed{792}$$