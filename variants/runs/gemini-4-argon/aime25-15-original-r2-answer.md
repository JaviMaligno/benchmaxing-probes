Para hallar el número $N$ de ternas ordenadas de enteros positivos $(a, b, c)$ tales que $1 \le a, b, c \le 3^6$ y $a^3 + b^3 + c^3 \equiv 0 \pmod{3^7}$, analizaremos la ecuación según la divisibilidad de $a, b, c$ por $3$.

### Paso 1: Análisis módulo 9 y la aplicación cubo
Para cualquier entero $x$:
- Si $3 \nmid x$, entonces $x \equiv \pm 1, \pm 2, \pm 4 \pmod 9$, por lo que $x^3 \equiv \pm 1 \pmod 9$.
- Si $3 \mid x$, entonces $x^3 \equiv 0 \pmod{27}$, y en particular $x^3 \equiv 0 \pmod 9$.

Para que se cumpla $a^3 + b^3 + c^3 \equiv 0 \pmod{3^7}$, es necesario que $a^3 + b^3 + c^3 \equiv 0 \pmod 9$. Evaluando las posibles combinaciones de residuos en $\{0, 1, -1\}$ módulo $9$:
- Si ninguno de $a, b, c$ es múltiplo de $3$, la suma es de la forma $(\pm 1) + (\pm 1) + (\pm 1) \equiv \pm 1 \text{ o } \pm 3 \not\equiv 0 \pmod 9$.
- Si exactamente dos de ellos son múltiplos de $3$, la suma es congruente con $0 + 0 + (\pm 1) \equiv \pm 1 \not\equiv 0 \pmod 9$.

Por lo tanto, solo existen dos casos posibles:
1. **Caso 1:** Exactamente uno de los números $a, b, c$ es múltiplo de $3$, y los otros dos no lo son.
2. **Caso 2:** Los tres números $a, b, c$ son múltiplos de $3$.

Además, recordemos una propiedad clave de los cubos módulo potencias de $3$: para cualquier $k \ge 1$, como $(x + m \cdot 3^k)^3 = x^3 + 3^{k+1}mx^2 + 3^{2k+1}m^2x + 3^{3k}m^3 \equiv x^3 \pmod{3^{k+1}}$, el valor de $x^3 \pmod{3^{k+1}}$ depende únicamente de $x \pmod{3^k}$. Más aún, a medida que $x$ recorre los $2 \cdot 3^{k-1}$ residuos coprimos con $3$ en $\{1, \dots, 3^k\}$, el valor de $x^3 \pmod{3^{k+1}}$ recorre de manera biyectiva los $2 \cdot 3^{k-1}$ residuos módulo $3^{k+1}$ que son congruentes con $\pm 1 \pmod 9$.

---

### Paso 2: Conteo del Caso 1 (exactamente un múltiplo de 3)
Supongamos que exactamente uno de $a, b, c$ es divisible por $3$:
- Hay $3$ maneras de elegir cuál de las tres variables (digamos $c$) es múltiplo de $3$.
- En el conjunto $\{1, \dots, 3^6\}$, hay $3^5$ múltiplos de $3$ posibles para $c$. Para cualquiera de ellos, se cumple que $c^3 \equiv 0 \pmod 9$.
- Para la primera variable coprima con $3$ (digamos $a$), hay $3^6 - 3^5 = 2 \cdot 3^5$ elecciones posibles. Su cubo cumple $a^3 \equiv \pm 1 \pmod 9$.
- Necesitamos que $b^3 \equiv -c^3 - a^3 \pmod{3^7}$. Como $-c^3 - a^3 \equiv 0 - (\pm 1) \equiv \mp 1 \pmod 9$, por la biyección mencionada en el Paso 1 (con $k = 6$), existe un **único** $b \in \{1, \dots, 3^6\}$ coprimo con $3$ que satisface esta congruencia.

Por lo tanto, el número de ternas en el Caso 1 es:
$$N_1 = 3 \times 3^5 \times (2 \cdot 3^5) \times 1 = 2 \cdot 3^{11}$$

---

### Paso 3: Conteo del Caso 2 (los tres son múltiplos de 3)
Si $3 \mid a, b, c$, podemos escribir $a = 3a'$, $b = 3b'$ y $c = 3c'$, donde $a', b', c' \in \{1, \dots, 3^5\}$. Sustituyendo en la condición original:
$$27\left((a')^3 + (b')^3 + (c')^3\right) \equiv 0 \pmod{3^7} \iff (a')^3 + (b')^3 + (c')^3 \equiv 0 \pmod{3^4}$$

Nuevamente, analizando módulo $9$, nos dividimos en dos subcasos para $(a', b', c')$:

#### Subcaso 2a: Exactamente uno de $a', b', c'$ es múltiplo de $3$
- Hay $3$ maneras de elegir cuál de las tres variables es múltiplo de $3$.
- En $\{1, \dots, 3^5\}$, hay $3^4$ opciones para dicha variable.
- Para la primera variable no divisible por $3$, hay $2 \cdot 3^4$ opciones en $\{1, \dots, 3^5\}$.
- Para la segunda variable no divisible por $3$, su cubo módulo $3^4$ queda fijado en un residuo congruente con $\pm 1 \pmod 9$. Por la biyección del Paso 1 (con $k = 3$), esto determina un único residuo módulo $3^3$, lo que corresponde a $\frac{3^5}{3^3} = 3^2$ valores posibles en $\{1, \dots, 3^5\}$.

El número de ternas en este subcaso es:
$$N_{2a} = 3 \times 3^4 \times (2 \cdot 3^4) \times 3^2 = 2 \cdot 3^{11}$$

#### Subcaso 2b: Los tres números $a', b', c'$ son múltiplos de $3$
Escribimos $a' = 3a''$, $b' = 3b''$ y $c' = 3c''$ con $a'', b'', c'' \in \{1, \dots, 3^4\}$. La condición se reduce a:
$$27\left((a'')^3 + (b'')^3 + (c'')^3\right) \equiv 0 \pmod{3^4} \iff (a'')^3 + (b'')^3 + (c'')^3 \equiv 0 \pmod 3$$

Por el pequeño teorema de Fermat, $x^3 \equiv x \pmod 3$, por lo que la condición equivale a $a'' + b'' + c'' \equiv 0 \pmod 3$:
- Hay $3^4$ elecciones para $a''$ y $3^4$ elecciones para $b''$.
- Para cualesquiera $a''$ y $b''$, el residuo de $c'' \pmod 3$ queda únicamente determinado, por lo que hay $\frac{3^4}{3} = 3^3$ elecciones para $c''$.

El número de ternas en este subcaso es:
$$N_{2b} = 3^4 \times 3^4 \times 3^3 = 3^{11}$$

---

### Paso 4: Cálculo total y reducción módulo 1000
Sumando todos los casos obtenemos $N$:
$$N = N_1 + N_{2a} + N_{2b} = 2 \cdot 3^{11} + 2 \cdot 3^{11} + 3^{11} = 5 \cdot 3^{11}$$

Calculamos $3^{11}$:
$$3^{11} = 177\,147$$

Multiplicando por $5$:
$$N = 5 \times 177\,147 = 885\,735$$

Al dividir $N$ entre $1000$, el residuo es $735$.

\boxed{735}