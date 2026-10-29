Vamos a analizar el problema paso a paso.

## 1. Entender el algoritmo voraz

Con monedas de 1, 10 y 25 centavos, el algoritmo voraz para una cantidad $N$:

- Toma tantas monedas de 25 como sea posible: $q = \lfloor N/25 \rfloor$
- Luego, con el residuo, tantas monedas de 10 como sea posible: $d = \lfloor r/10 \rfloor$
- Finalmente, el resto en monedas de 1: $p = r \bmod 10$

El número total de monedas voraz es:
$$g(N) = \lfloor N/25 \rfloor + \lfloor (N \bmod 25)/10 \rfloor + (N \bmod 10)$$

## 2. Cuándo falla el voraz

El sistema de monedas $1, 10, 25$ no es canónico. El voraz falla cuando podemos reducir $g(N)$ usando una combinación diferente.

Observemos el caso $N = 40$:

- Voraz: $25 + 10 + 5 \times 1 = 7$ monedas
- Mejor: $4 \times 10 = 4$ monedas

Aquí el voraz usa un 25 y luego completa con 10 y unos, pero usar cuatro monedas de 10 es mejor.

## 3. Identificar el patrón de fallo

El voraz falla cuando el residuo $r = N \bmod 25$ se puede cubrir con monedas de 10 y 1 de forma más eficiente usando menos monedas de las que el voraz usa.

Para $r$ (con $0 \le r \le 24$), el voraz usa:
$$g(r) = \lfloor r/10 \rfloor + (r \bmod 10)$$

La forma óptima para cubrir $r$ con monedas de 10 y 1 es exactamente esta, así que para el residuo el voraz es óptimo.

El problema real es que el voraz ya comprometió una moneda de 25, y a veces conviene **no** usar el 25, usando $q-1$ monedas de 25 (o menos) y más monedas de 10.

## 4. Análisis con base en $N \bmod 25$

Escribamos $N = 25q + r$, con $0 \le r \le 24$.

El voraz usa $q$ monedas de 25 y cubre $r$ con $g(r)$ monedas:
$$g(N) = q + g(r)$$

**Alternativa:** usar $q-1$ monedas de 25 y cubrir $25+r$ con monedas de 10 y 1. El total de monedas sería:
$$(q-1) + h(25+r)$$
donde $h(m)$ es el mínimo de monedas con denominaciones 1 y 10:
$$h(m) = \lfloor m/10 \rfloor + (m \bmod 10)$$

El voraz falla si:
$$(q-1) + h(25+r) < q + g(r)$$
es decir:
$$h(25+r) < 1 + g(r)$$

## 5. Evaluar para cada residuo $r$

Calculemos $g(r)$ y $h(25+r)$ para $r = 0, \ldots, 24$:

| $r$ | $g(r)$ | $25+r$ | $h(25+r)$ | ¿Falla? ($h < 1+g$) |
|-----|--------|--------|-----------|---------------------|
| 0 | 0 | 25 | 3 (2×10+5×1) | 3 < 1? No |
| 1 | 1 | 26 | 8 (2×10+6×1) | 8 < 2? No |
| 2 | 2 | 27 | 9 | 9 < 3? No |
| 3 | 3 | 28 | 10 | 10 < 4? No |
| 4 | 4 | 29 | 11 | 11 < 5? No |
| 5 | 5 | 30 | 3 | 3 < 6? **Sí** |
| 6 | 6 | 31 | 4 | 4 < 7? **Sí** |
| 7 | 7 | 32 | 5 | 5 < 8? **Sí** |
| 8 | 8 | 33 | 6 | 6 < 9? **Sí** |
| 9 | 9 | 34 | 7 | 7 < 10? **Sí** |
| 10 | 1 | 35 | 8 (3×10+5×1) | 8 < 2? No |
| 11 | 2 | 36 | 9 | 9 < 3? No |
| 12 | 3 | 37 | 10 | 10 < 4? No |
| 13 | 4 | 38 | 11 | 11 < 5? No |
| 14 | 5 | 39 | 12 | 12 < 6? No |
| 15 | 6 | 40 | 4 | 4 < 7? **Sí** |
| 16 | 7 | 41 | 5 | 5 < 8? **Sí** |
| 17 | 8 | 42 | 6 | 6 < 9? **Sí** |
| 18 | 9 | 43 | 7 | 7 < 10? **Sí** |
| 19 | 10 | 44 | 8 | 8 < 11? **Sí** |
| 20 | 2 | 45 | 9 (4×10+5×1) | 9 < 3? No |
| 21 | 3 | 46 | 10 | 10 < 4? No |
| 22 | 4 | 47 | 11 | 11 < 5? No |
| 23 | 5 | 48 | 12 | 12 < 6? No |
| 24 | 6 | 49 | 13 | 13 < 7? No |

Los residuos que fallan: $r \in \{5, 6, 7, 8, 9, 15, 16, 17, 18, 19\}$.

Pero hay que tener cuidado: para $N < 25$, no hay moneda de 25 disponible (la alternativa de $q-1$ no aplica). Debemos verificar si para $N < 25$ el voraz acierta siempre.

## 6. Casos pequeños ($1 \le N \le 24$)

Para $N < 25$, el voraz usa solo monedas de 10 y 1, que es óptimo. Por tanto, todos los $N$ de 1 a 24 tienen voraz exitoso, aun si su residuo aparece en la lista de fallo (pues no hay 25 para intercambiar).

De hecho, para que el fallo ocurra, necesitamos $q \ge 1$, es decir, $N \ge 25$.

## 7. Contar los casos

Para $N \ge 25$, escribimos $N = 25q + r$ con $q \ge 1$.

Los valores de $N$ entre 1 y 1000:

- De 1 a 24: todos exitosos → 24
- De 25 a 1000: hay $1000 - 25 + 1 = 976$ valores. De estos, fallan los que tengan $r \in F = \{5,6,7,8,9,15,16,17,18,19\}$, un total de 10 residuos de cada 25.

  Número de fallos entre 25 y 1000:
  - Cada bloque de 25 números tiene 10 fallos.
  - De 25 a 999 hay $975$ números → $975/25 = 39$ bloques → $39 \times 10 = 390$ fallos.
  - El 1000: $1000 = 25 \times 40 + 0$, residuo 0, no falla.

  Total fallos: $390$.

  Éxitos entre 25 y 1000: $976 - 390 = 586$.

## 8. Total final

$$\text{Éxitos totales} = 24 + 586 = 610$$

## Verificación rápida

Alternativamente, de 1 a 1000 hay 1000 números. De 25 a 999 (975 números) fallan 390. Los restantes exitosos son:
$$1000 - 390 = 610$$

Esto confirma el resultado.

$$\boxed{610}$$