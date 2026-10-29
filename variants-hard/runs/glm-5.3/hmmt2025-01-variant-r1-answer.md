# Solución paso a paso

## Paso 1: Factorización de $11!$

$$11! = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7^1 \cdot 11^1$$

## Paso 2: Identificar qué divisores pueden terminar en 3

Un divisor con cifra de unidades $3$ debe ser **impar** (sin factor $2$) y **no divisible por $5$** (sin factor $5$).

Entonces los divisores buscados son de la forma:
$$3^a \cdot 7^b \cdot 11^c, \quad 0 \le a \le 4,\; 0 \le b \le 1,\; 0 \le c \le 1$$

## Paso 3: Analizar los dígitos de las unidades

- $3^a \pmod{10}$: $a=0 \to 1,\; a=1 \to 3,\; a=2 \to 9,\; a=3 \to 7,\; a=4 \to 1$
- $7^b \pmod{10}$: $b=0 \to 1,\; b=1 \to 7$
- $11^c \pmod{10}$: siempre $1$ (no afecta el dígito)

Necesitamos que el producto tenga dígito de unidades $3$:

| $a$ | $3^a$ | $b=0$ | $b=1$ |
|-----|-------|-------|-------|
| 0 | 1 | 1 | 7 |
| 1 | 3 | **3** ✓ | 1 |
| 2 | 9 | 9 | **3** ✓ |
| 3 | 7 | 7 | 9 |
| 4 | 1 | 1 | 7 |

## Paso 4: Listar los divisores con dígito de unidades 3

- $a=1, b=0$: $3^1 = 3$ y $3 \cdot 11 = 33$
- $a=2, b=1$: $3^2 \cdot 7 = 63$ y $3^2 \cdot 7 \cdot 11 = 693$

Todos terminan en $3$: $3, 33, 63, 693$.

## Paso 5: Calcular la suma

$$3 + 33 + 63 + 693 = 792$$

$$\boxed{792}$$