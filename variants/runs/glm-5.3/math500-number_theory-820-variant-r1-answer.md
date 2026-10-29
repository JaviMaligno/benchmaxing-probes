## Planteamiento

Escribo $m = d\cdot a$ y $n = d\cdot b$, donde $d = \gcd(m,n) = 2310$ y $\gcd(a,b)=1$.

Entonces:
$$\mathop{\text{lcm}}[m,n] = d\cdot a\cdot b = 2310^3 \implies a\cdot b = 2310^2$$

Como $2310 = 2\cdot 3\cdot 5\cdot 7\cdot 11$, tenemos:
$$a\cdot b = 2^2 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11^2$$

## Reparto de primos

Como $\gcd(a,b)=1$, cada potencia prima $p^2$ debe ir **completa** a $a$ o a $b$ (no puede repartirse $p$ a cada uno, pues compartirían el factor $p$). Con 5 primos distintos, hay $2^5 = 32$ pares ordenados $(a,b)$.

## Condición $m < n$

Como $m = 2310\,a$ y $n = 2310\,b$, la condición $m<n$ equivale a $a<b$. Ningún par tiene $a=b$ (eso exigiría $a=b=2310$, que comparte todos los primos, violando $\gcd(a,b)=1$). Por simetría, exactamente la mitad de los 32 pares cumple $a<b$:

$$\frac{32}{2} = 16$$

## Verificación

Cada valor de $m$ tiene la forma $m = 2310\cdot a$ donde $a$ es un producto de un subconjunto de los primos elevados al cuadrado. Ejemplo: $a=2^2$, $b=3^2\cdot 5^2\cdot 7^2\cdot 11^2$ da $m=9240$, $n=2310\cdot \text{(resto)}$, con $\gcd=2310$ y $\text{lcm}=2310^3$. ✓

$$\boxed{16}$$