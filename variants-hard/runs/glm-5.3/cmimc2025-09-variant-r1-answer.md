## Solución

**Paso 1: Factorización algebraica.**

Usamos la fórmula de diferencia de quintas potencias:

$$80^5 - 1 = (80-1)\left(80^4+80^3+80^2+80+1\right) = 79 \times 41\,478\,481$$

donde $80^4+80^3+80^2+80+1 = 40\,960\,000 + 512\,000 + 6\,400 + 80 + 1 = 41\,478\,481$.

**Paso 2: El factor 79.**

$79$ es primo (no es divisible por $2, 3, 5, 7$).

**Paso 3: Factorizar $41\,478\,481$.**

La suma alternada de dígitos es $4-1+4-7+8-4+8-1 = 11$, múltiplo de $11$:

$$41\,478\,481 = 11 \times 3\,770\,771$$

**Paso 4: Factorizar $3\,770\,771$.**

Buscando divisores, se encuentra:

$$3\,770\,771 = 751 \times 5\,021$$

(Verificación: $751 \times 5000 = 3\,755\,000$ y $751 \times 21 = 15\,771$; la suma da $3\,770\,771$.)

- $751$ es primo (no tiene divisores primos hasta $\sqrt{751}\approx 27{,}4$).
- $5\,021$ es primo (ninguno de los primos hasta $\sqrt{5021}\approx 70{,}9$ lo divide: $3\,7\,11\,13\,17\,19\,23\,29\,31\,37\,41\,43\,47\,53\,59\,61\,67$ fallan todos).

**Paso 5: Verificación global.**

$$79 \times 11 \times 751 \times 5\,021 = 3\,276\,799\,999 = 80^5 - 1 \checkmark$$

Por lo tanto:

$$80^5-1 = 79 \times 11 \times 751 \times 5\,021$$

El mayor factor primo es $5\,021$.

$$\boxed{5021}$$