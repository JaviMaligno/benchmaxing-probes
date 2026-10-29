Para encontrar el residuo cuando $117^{36} + 194^{38}$ se divide entre $11$, podemos trabajar con aritmética modular (módulo $11$).

**Paso 1: Reducir las bases módulo $11$**
* Para $117$: como $117 = 11 \times 10 + 7$, tenemos que $117 \equiv 7 \pmod{11}$.
* Para $194$: como $194 = 11 \times 17 + 7$, tenemos que $194 \equiv 7 \pmod{11}$.

Por lo tanto, la expresión se simplifica a:
$$117^{36} + 194^{38} \equiv 7^{36} + 7^{38} \pmod{11}$$

**Paso 2: Reducir los exponentes usando el pequeño teorema de Fermat**
Como $11$ es un número primo y $\text{mcd}(7, 11) = 1$, el pequeño teorema de Fermat establece que $7^{10} \equiv 1 \pmod{11}$.

* $7^{36} = (7^{10})^3 \cdot 7^6 \equiv 1^3 \cdot 7^6 \equiv 7^6 \pmod{11}$
* $7^{38} = (7^{10})^3 \cdot 7^8 \equiv 1^3 \cdot 7^8 \equiv 7^8 \pmod{11}$

**Paso 3: Calcular las potencias restantes módulo $11$**
Sabemos que:
$$7^2 = 49 = 11 \times 4 + 5 \equiv 5 \pmod{11}$$

A partir de esto:
* $7^6 = (7^2)^3 \equiv 5^3 = 125 \pmod{11}$. Como $125 = 11 \times 11 + 4$, obtenemos $7^6 \equiv 4 \pmod{11}$.
* $7^8 = 7^6 \cdot 7^2 \equiv 4 \cdot 5 = 20 \pmod{11}$. Como $20 = 11 \times 1 + 9$, obtenemos $7^8 \equiv 9 \pmod{11}$.

**Paso 4: Sumar los resultados**
$$7^6 + 7^8 \equiv 4 + 9 = 13 \equiv 2 \pmod{11}$$

\boxed{2}