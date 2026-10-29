Para determinar cuántos "días buenos" hay en marzo, abril y mayo combinados, representemos el mes como $m$ y el día como $d$.

Según los ejemplos del enunciado:
1. Si el día tiene un solo dígito ($1 \le d \le 9$), la concatenación del mes y el día es $10m + d$ (por ejemplo, el 9 de marzo es $39$).
   - Para que $m$ divida a $10m + d$, es necesario y suficiente que $m$ divida a $d$ ($m \mid d$).
   - Para que $d$ divida a $10m + d$, es necesario y suficiente que $d$ divida a $10m$ ($d \mid 10m$).

2. Si el día tiene dos dígitos ($10 \le d \le 31$), la concatenación del mes y el día es $100m + d$ (por ejemplo, el 15 de marzo es $315$).
   - Para que $m$ divida a $100m + d$, se requiere que $m$ divida a $d$ ($m \mid d$).
   - Para que $d$ divida a $100m + d$, se requiere que $d$ divida a $100m$ ($d \mid 100m$).

En ambos casos, como $m \mid d$, podemos escribir $d = m \cdot k$ para algún entero positivo $k$. Sustituyendo esto en la segunda condición:
- Para $1 \le d \le 9$: $mk \mid 10m \iff k \mid 10$.
- Para $d \ge 10$: $mk \mid 100m \iff k \mid 100$.

Ahora analizamos cada mes por separado:

### 1. Marzo ($m = 3$, tiene $31$ días)
Como $d = 3k$:
- **Días de un dígito ($1 \le 3k \le 9 \implies 1 \le k \le 3$):**
  Buscamos divisores de $10$ en el rango $1 \le k \le 3$, que son $k = 1, 2$.
  Esto nos da $d = 3(1) = 3$ y $d = 3(2) = 6$ (las concatenaciones son $33$ y $36$).
- **Días de dos dígitos ($10 \le 3k \le 31 \implies 4 \le k \le 10$):**
  Buscamos divisores de $100$ en el rango $4 \le k \le 10$, que son $k = 4, 5, 10$.
  Esto nos da $d = 12, 15, 30$ (las concatenaciones son $312$, $315$ y $330$).
- **Total en marzo:** $2 + 3 = 5$ días buenos.

### 2. Abril ($m = 4$, tiene $30$ días)
Como $d = 4k$:
- **Días de un dígito ($1 \le 4k \le 9 \implies 1 \le k \le 2$):**
  Los divisores de $10$ en $1 \le k \le 2$ son $k = 1, 2$.
  Esto nos da $d = 4, 8$ (las concatenaciones son $44$ y $48$).
- **Días de dos dígitos ($10 \le 4k \le 30 \implies 3 \le k \le 7$):**
  Los divisores de $100$ en $3 \le k \le 7$ son $k = 4, 5$.
  Esto nos da $d = 16, 20$ (las concatenaciones son $416$ y $420$).
- **Total en abril:** $2 + 2 = 4$ días buenos.

### 3. Mayo ($m = 5$, tiene $31$ días)
Como $d = 5k$:
- **Días de un dígito ($1 \le 5k \le 9 \implies k = 1$):**
  El divisor de $10$ en este rango es $k = 1$.
  Esto nos da $d = 5$ (la concatenación es $55$).
- **Días de dos dígitos ($10 \le 5k \le 31 \implies 2 \le k \le 6$):**
  Los divisores de $100$ en $2 \le k \le 6$ son $k = 2, 4, 5$.
  Esto nos da $d = 10, 20, 25$ (las concatenaciones son $510$, $520$ y $525$).
- **Total en mayo:** $1 + 3 = 4$ días buenos.

### Total combinado
Sumando los días buenos de los tres meses obtenemos $5 + 4 + 4 = 13$.

\boxed{13}