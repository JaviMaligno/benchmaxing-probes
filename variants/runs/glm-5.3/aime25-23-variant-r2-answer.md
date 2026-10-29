## Planteamiento

Escribamos $N = 24q + r$ con $0 \le r \le 23$. El algoritmo voraz usa $q$ monedas de 24, luego $\lfloor r/10 \rfloor$ monedas de 10 y $r \bmod 10$ monedas de 1, es decir:

$$G = q + \underbrace{\lfloor r/10\rfloor + (r \bmod 10)}_{g(r)}.$$

**Cualquier otra colección** tiene $q - k$ monedas de 24 (con $0 \le k \le q$; no puede tener más que $q$), y el mínimo de monedas de 10 y 1 para el resto $r + 24k$ es $\lfloor (r+24k)/10 \rfloor + ((r+24k)\bmod 10)$. Usando $24k = 20k + 4k$, esa cantidad es $2k + \lfloor (r+4k)/10\rfloor + ((r+4k)\bmod 10)$.

## Condición de fallo

El voraz falla si existe $k \ge 1$ (con $k \le q$) tal que:

$$q - k + 2k + \left\lfloor \tfrac{r+4k}{10}\right\rfloor + \big((r+4k)\bmod 10\big) < q + g(r).$$

Usando la identidad $\lfloor x/10\rfloor + (x \bmod 10) = x - 9\lfloor x/10\rfloor$, esto se simplifica a:

$$5k < 9\left(\left\lfloor \tfrac{r+4k}{10}\right\rfloor - \left\lfloor \tfrac{r}{10}\right\rfloor\right).$$

## Análisis por residuo

**Caso $k=1$:** la condición es $5 < 9\left(\lfloor (r+4)/10\rfloor - \lfloor r/10\rfloor\right)$, que se cumple exactamente cuando ese salto de piso vale 1, es decir para $r \in \{6,7,8,9,16,17,18,19\}$.

**Ejemplo:** $r=6$: $N=30$ da voraz $24+6\cdot 1 = 7$ monedas, pero $3\cdot 10 = 3$ monedas. $r=16$: $N=40$ (el ejemplo del enunciado).

**Para los demás residuos** hay que verificar que ningún $k$ mayor funciona. Como $\lfloor (r+4k)/10\rfloor - \lfloor r/10\rfloor \lesssim 0{.}4k + 1$, el lado derecho crece como $3{.}6k < 5k$, así que solo hace falta revisar $k$ pequeños:

- $r \in \{0,\dots,5\}$: para $k=1,\dots,7$ el lado derecho da a lo sumo $0, 9, 9, 18, 18, 18, 27$ frente a $5,10,15,20,25,30,35$. Nunca falla.
- $r \in \{10,\dots,15\}$: los valores máximos son $0,9,9,18,18,18,27$ frente a $5,10,15,20,25,30,35$. Nunca falla. (Ej.: $N=44$: voraz $= 24+10+10+4 = 4$ monedas, óptimo.)
- $r \in \{20,\dots,23\}$: máximos $0,0,9,9,18,18,27$ frente a $5,10,15,20,25,30,35$. Nunca falla.

## Conteo

El voraz falla exactamente cuando $N \ge 24$ y $N \bmod 24 \in \{6,7,8,9,16,17,18,19\}$ (para $N < 24$ no hay alternativa posible, pues $q=0$).

De $1$ a $1000$: con $q = 1,\dots,40$ cada bloque aporta 8 valores de fallo ($24q + r \le 983 \le 1000$). Para $q = 41$ ($N = 984 + r$), solo $r \in \{6,7,8,9,16\}$ da $N \le 1000$ (pues $984 + 17 > 1000$), o sea 5 valores.

Valores que fallan: $40 \times 8 + 5 = 325$.

Valores donde el voraz tiene éxito:

$$1000 - 325 = 675.$$

$$\boxed{675}$$