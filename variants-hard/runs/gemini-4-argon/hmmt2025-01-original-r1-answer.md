Para hallar la suma de los divisores positivos de $9!$ cuyo dígito de las unidades es $1$, primero descomponemos $9!$ en sus factores primos:

$$9! = 1 \times 2 \times 3 \times 4 \times 5 \times 6 \times 7 \times 8 \times 9 = 2^7 \times 3^4 \times 5^1 \times 7^1$$

Cualquier número cuyo dígito de las unidades sea $1$ no puede ser divisible por $2$ (ya que sería par) ni por $5$ (ya que terminaría en $0$ o en $5$). Por lo tanto, los divisores que buscamos deben ser divisores únicamente de la parte formada por los factores $3$ y $7$, es decir, de $3^4 \times 7^1$.

Listamos todos los divisores positivos de $3^4 \times 7^1$ y observamos su último dígito:

1. **Sin el factor $7$ ($3^a$ con $0 \le a \le 4$):**
   - $3^0 = 1$ (termina en $1$)
   - $3^1 = 3$ (termina en $3$)
   - $3^2 = 9$ (termina en $9$)
   - $3^3 = 27$ (termina en $7$)
   - $3^4 = 81$ (termina en $1$)

2. **Con el factor $7$ ($3^a \times 7$ con $0 \le a \le 4$):**
   - $3^0 \times 7 = 7$ (termina en $7$)
   - $3^1 \times 7 = 21$ (termina en $1$)
   - $3^2 \times 7 = 63$ (termina en $3$)
   - $3^3 \times 7 = 189$ (termina en $9$)
   - $3^4 \times 7 = 567$ (termina en $7$)

Los únicos divisores que tienen $1$ en el dígito de las unidades son $1$, $81$ y $21$.

Finalmente, calculamos su suma:
$$1 + 81 + 21 = 103$$

\boxed{103}