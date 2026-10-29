La probabilidad es sobre los enteros impares positivos menores que 4000.

**Paso 1: ¿Cuándo tiene expansión decimal finita el recíproco?**

Para un entero positivo $N$ con factorización prima $N = 2^a 3^b 5^c \cdots$, el recíproco $\frac{1}{N}$ tiene expansión decimal finita si y solo si $N$ tiene la forma:

$$N = 2^a \cdot 5^b$$

Es decir, sus únicos factores primos son 2 y 5.

**Paso 2: Condición sobre el entero impar**

Como el entero elegido es **impar**, no puede tener factor 2. Entonces, para que su recíproco sea finito, debe cumplirse:

$$N = 5^b$$

es decir, $N$ es una potencia de 5.

**Paso 3: Contar los enteros impares positivos menores que 4000**

Los enteros impares positivos menores que 4000 son:
$$1, 3, 5, 7, \dots, 3999$$
En total: $2000$ enteros.

**Paso 4: Contar las potencias de 5 menores que 4000**

Las potencias de 5 (todas impares):
- $5^0 = 1$ ✓
- $5^1 = 5$ ✓
- $5^2 = 25$ ✓
- $5^3 = 125$ ✓
- $5^4 = 625$ ✓
- $5^5 = 3125$ ✓
- $5^6 = 15625 > 4000$ ✗

Hay **6** potencias de 5 menores que 4000.

**Paso 5: Probabilidad**

$$P = \frac{6}{2000} = \frac{3}{1000}$$

**Paso 6: Suma $m + n$**

$$m + n = 3 + 1000 = 1003$$

$$\boxed{1003}$$