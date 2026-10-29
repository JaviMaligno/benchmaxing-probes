Para determinar cuántas "fechas afortunadas" (*lucky dates*) hay en junio, julio y agosto combinados, analizamos la condición de divisibilidad según la cantidad de dígitos del día $D$, siendo $M$ el número del mes ($M \in \{6, 7, 8\}$).

### Caso 1: Días de un solo dígito ($1 \le D \le 9$)
El número formado al escribir el mes seguido del día es $10M + D$.
Para que esta fecha sea afortunada, se deben cumplir dos condiciones:
1. $M$ divide a $10M + D$, lo cual equivale a que $M$ divida a $D$.
2. $D$ divide a $10M + D$, lo cual equivale a que $D$ divida a $10M$.

Como $M \in \{6, 7, 8\}$ y $1 \le D \le 9$, el único múltiplo de $M$ en ese rango es $D = M$. Si $D = M$, entonces $D$ también divide a $10M$ automáticamente. Esto nos da una fecha por cada mes:
- **Junio ($M = 6$):** 6 de junio ($66$ es divisible por $6$).
- **Julio ($M = 7$):** 7 de julio ($77$ es divisible por $7$).
- **Agosto ($M = 8$):** 8 de agosto ($88$ es divisible por $8$).

Esto aporta **$3$** fechas afortunadas.

---

### Caso 2: Días de dos dígitos ($10 \le D \le 30$ o $31$)
El número formado al escribir el mes seguido del día es $100M + D$.
Las condiciones de divisibilidad son:
1. $M$ divide a $100M + D \iff M \mid D$. Por lo tanto, $D = kM$ para algún entero positivo $k \ge 2$.
2. $D$ divide a $100M + D \iff D \mid 100M$. Sustituyendo $D = kM$, obtenemos $kM \mid 100M \iff k \mid 100$.

Los divisores de $100$ mayores o iguales a $2$ son $k \in \{2, 4, 5, 10, \dots\}$. Evaluamos para cada mes según su límite de días:

- **Junio ($M = 6$, $10 \le D \le 30$):**
  Como $D = 6k \le 30$, tenemos $k \in \{2, 3, 4, 5\}$. De estos, los que dividen a $100$ son $k = 2, 4, 5$:
  - $k = 2 \implies D = 12$ ($612$ es divisible por $6$ y $12$).
  - $k = 4 \implies D = 24$ ($624$ es divisible por $6$ y $24$).
  - $k = 5 \implies D = 30$ ($630$ es divisible por $6$ y $30$).
  (Total en este caso para junio: **$3$** fechas).

- **Julio ($M = 7$, $10 \le D \le 31$):**
  Como $D = 7k \le 31$, tenemos $k \in \{2, 3, 4\}$. De estos, los que dividen a $100$ son $k = 2, 4$:
  - $k = 2 \implies D = 14$ ($714$ es divisible por $7$ y $14$).
  - $k = 4 \implies D = 28$ ($728$ es divisible por $7$ y $28$).
  (Total en este caso para julio: **$2$** fechas).

- **Agosto ($M = 8$, $10 \le D \le 31$):**
  Como $D = 8k \le 31$, tenemos $k \in \{2, 3\}$. De estos, el único que divide a $100$ es $k = 2$:
  - $k = 2 \implies D = 16$ ($816$ es divisible por $8$ y $16$).
  (Total en este caso para agosto: **$1$** fecha).

---

### Total combinado
Sumando todas las fechas afortunadas encontradas:
$$3 + 3 + 2 + 1 = 9$$

\boxed{9}