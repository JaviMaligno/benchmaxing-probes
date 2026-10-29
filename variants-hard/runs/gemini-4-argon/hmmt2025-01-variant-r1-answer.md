Para encontrar la suma de todos los divisores positivos de $11!$ cuyo dígito de las unidades es $3$, primero hallamos la factorización en números primos de $11!$.

Los números primos menores o iguales a $11$ son $2, 3, 5, 7$ y $11$.
Cualquier divisor positivo cuyo dígito de las unidades sea $3$ no puede ser divisible ni por $2$ (pues sería par) ni por $5$ (pues terminaría en $0$ o $5$). Por lo tanto, solo debemos considerar los factores primos $3, 7$ y $11$.

Calculamos el exponente de cada uno de estos primos en la factorización de $11!$ usando la fórmula de Legendre:
- Exponente de $3$: $\lfloor 11/3 \rfloor + \lfloor 11/9 \rfloor = 3 + 1 = 4$.
- Exponente de $7$: $\lfloor 11/7 \rfloor = 1$.
- Exponente de $11$: $\lfloor 11/11 \rfloor = 1$.

Así, cualquier divisor de $11!$ que termine en $3$ debe ser un divisor de $3^4 \cdot 7^1 \cdot 11^1$, es decir, debe tener la forma:
$$d = 3^a \cdot 7^b \cdot 11^c$$
donde $a \in \{0, 1, 2, 3, 4\}$, $b \in \{0, 1\}$ y $c \in \{0, 1\}$.

Observamos los restos módulo $10$ (el dígito de las unidades):
Como $11 \equiv 1 \pmod{10}$, tenemos que $11^c \equiv 1 \pmod{10}$ tanto para $c = 0$ como para $c = 1$. Esto significa que multiplicar por $11$ no altera el dígito de las unidades. Por lo tanto, buscamos los valores de $a$ y $b$ tales que:
$$3^a \cdot 7^b \equiv 3 \pmod{10}$$

Las potencias de $3$ para $0 \le a \le 4$ y sus respectivos dígitos de las unidades son:
- $3^0 = 1 \equiv 1 \pmod{10}$
- $3^1 = 3 \equiv 3 \pmod{10}$
- $3^2 = 9 \equiv 9 \pmod{10}$
- $3^3 = 27 \equiv 7 \pmod{10}$
- $3^4 = 81 \equiv 1 \pmod{10}$

Analizamos los dos casos posibles para $b$:
1. **Caso $b = 0$:** Necesitamos $3^a \equiv 3 \pmod{10}$. De la lista anterior, esto ocurre únicamente cuando $a = 1$, lo que da $3^1 \cdot 7^0 = 3$.
2. **Caso $b = 1$:** Necesitamos $3^a \cdot 7 \equiv 3 \pmod{10}$. Como $9 \cdot 7 = 63 \equiv 3 \pmod{10}$, necesitamos $3^a \equiv 9 \pmod{10}$. Esto ocurre únicamente cuando $a = 2$, lo que da $3^2 \cdot 7^1 = 63$.

Incorporando el factor $11^c$ con $c \in \{0, 1\}$, obtenemos todos los divisores buscados:
- Para $a = 1, b = 0$: $3 \cdot 1 = 3$ y $3 \cdot 11 = 33$.
- Para $a = 2, b = 1$: $63 \cdot 1 = 63$ y $63 \cdot 11 = 693$.

Finalmente, sumamos estos divisores:
$$3 + 33 + 63 + 693 = (3 + 63)(1 + 11) = 66 \cdot 12 = 792$$

\boxed{792}