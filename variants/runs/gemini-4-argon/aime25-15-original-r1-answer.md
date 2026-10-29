Para hallar el número $N$ de ternas ordenadas de enteros positivos $(a, b, c)$ tales que $1 \le a, b, c \le 3^6$ y $3^7 \mid a^3 + b^3 + c^3$, analizamos el comportamiento de los cubos módulo potencias de $3$.

### Paso 1: Reducción módulo $9$ y clasificación por casos
Para cualquier entero $x$:
- Si $x \equiv 0 \pmod 3$, entonces $27 \mid x^3$, por lo que $x^3 \equiv 0 \pmod 9$.
- Si $x \equiv 1 \pmod 3$, escribiendo $x = 3k + 1$ tenemos $x^3 = 27k^3 + 27k^2 + 9k + 1 \equiv 1 \pmod 9$.
- Si $x \equiv -1 \pmod 3$, escribiendo $x = 3k - 1$ tenemos $x^3 = 27k^3 - 27k^2 + 9k - 1 \equiv -1 \pmod 9$.

Como $3^7 \mid a^3 + b^3 + c^3$, en particular debe cumplirse que $a^3 + b^3 + c^3 \equiv 0 \pmod 9$. Dado que cada cubo es congruente con $0$, $1$ o $-1$ módulo $9$, existen únicamente dos casos disjuntos para que la suma de los tres sea congruente con $0$ módulo $9$:
1. **Caso 1:** Uno de los números es congruente con $0$, otro con $1$ y otro con $-1$ módulo $3$ (en algún orden).
2. **Caso 2:** Los tres números $a, b, c$ son múltiplos de $3$.

---

### Paso 2: Conteo del Caso 1
Hay $3! = 6$ permutaciones para asignar qué variable es congruente con $0, 1$ y $-1 \pmod 3$. Fijemos, sin pérdida de generalidad, $a \equiv 1 \pmod 3$, $b \equiv -1 \pmod 3$ y $c \equiv 0 \pmod 3$.

- En el conjunto $\{1, 2, \dots, 3^6\}$, hay $3^5$ elecciones posibles para $b \equiv -1 \pmod 3$ y $3^5$ elecciones posibles para $c \equiv 0 \pmod 3$.
- Una vez fijados $b$ y $c$, necesitamos que $a^3 \equiv -b^3 - c^3 \pmod{3^7}$. Notemos que $-b^3 - c^3 \equiv -(-1) - 0 \equiv 1 \pmod 9$.
- Consideremos la función $x \mapsto x^3 \pmod{3^7}$ restringida a los $3^5$ elementos $x \in \{1, \dots, 3^6\}$ tales que $x \equiv 1 \pmod 3$. Si $x_1 \equiv x_2 \equiv 1 \pmod 3$, por el lema de elevación del exponente (LTE) se tiene:
  $$v_3(x_1^3 - x_2^3) = v_3(x_1 - x_2) + 1$$
  Por tanto, $x_1^3 \equiv x_2^3 \pmod{3^7} \iff x_1 \equiv x_2 \pmod{3^6}$. Esto demuestra que la función es una biyección sobre los $3^5$ residuos módulo $3^7$ que son congruentes con $1 \pmod 9$.

Así, para cada elección de $(b, c)$ existe un único $a \in \{1, \dots, 3^6\}$ con $a \equiv 1 \pmod 3$ que cumple la congruencia. Multiplicando por las $6$ permutaciones, el Caso 1 aporta:
$$N_1 = 6 \cdot 3^5 \cdot 3^5 \cdot 1 = 6 \cdot 3^{10} = 2 \cdot 3^{11}$$

---

### Paso 3: Conteo del Caso 2
Si $3 \mid a, b, c$, podemos escribir $a = 3a_1, b = 3b_1, c = 3c_1$ con $1 \le a_1, b_1, c_1 \le 3^5$. La condición $3^7 \mid a^3 + b^3 + c^3$ equivale a:
$$3^7 \mid 27(a_1^3 + b_1^3 + c_1^3) \iff 3^4 \mid a_1^3 + b_1^3 + c_1^3$$

Observemos que $(x + 3^3 k)^3 = x^3 + 3^4 k x^2 + 3^7 k^2 x + 3^9 k^3 \equiv x^3 \pmod{3^4}$, por lo que el valor de $x^3 \pmod{3^4}$ depende únicamente de $x \pmod{3^3}$. Como cada clase de equivalencia módulo $3^3$ aparece $3^5 / 3^3 = 3^2$ veces en $\{1, \dots, 3^5\}$, el número de soluciones $(a_1, b_1, c_1) \in \{1, \dots, 3^5\}^3$ es $(3^2)^3 = 3^6$ veces el número de soluciones $(a_1, b_1, c_1) \in \{1, \dots, 3^3\}^3$ tales que $3^4 \mid a_1^3 + b_1^3 + c_1^3$.

Para contar las soluciones $(a_1, b_1, c_1) \in \{1, \dots, 3^3\}^3$ con $3^4 \mid a_1^3 + b_1^3 + c_1^3$, aplicamos la misma división en subcasos módulo $3$:
- **Subcaso 2a:** $(a_1, b_1, c_1) \pmod 3$ es una permutación de $(0, 1, -1) \pmod 3$. Por el mismo argumento biyectivo que en el Paso 2, hay $3^2$ opciones para la variable $\equiv -1 \pmod 3$, $3^2$ opciones para la variable $\equiv 0 \pmod 3$, y una única opción para la variable $\equiv 1 \pmod 3$. Con las $6$ permutaciones, esto da:
  $$6 \cdot 3^2 \cdot 3^2 \cdot 1 = 6 \cdot 3^4 = 2 \cdot 3^5$$
- **Subcaso 2b:** $3 \mid a_1, b_1, c_1$. Escribimos $a_1 = 3a_2, b_1 = 3b_2, c_1 = 3c_2$ con $1 \le a_2, b_2, c_2 \le 3^2$. La condición $3^4 \mid 27(a_2^3 + b_2^3 + c_2^3)$ se reduce a:
  $$3 \mid a_2^3 + b_2^3 + c_2^3 \iff a_2 + b_2 + c_2 \equiv 0 \pmod 3$$
  Para cualesquiera $a_2, b_2 \in \{1, \dots, 9\}$ ($9$ opciones cada uno), existen exactamente $3$ valores de $c_2 \in \{1, \dots, 9\}$ tales que $c_2 \equiv -a_2 - b_2 \pmod 3$. Esto aporta:
  $$9 \cdot 9 \cdot 3 = 3^5$$

Sumando ambos subcasos y multiplicando por el factor $3^6$, obtenemos el total del Caso 2:
$$N_2 = 3^6 (2 \cdot 3^5 + 3^5) = 3^6 \cdot 3^6 = 3^{12}$$

---

### Paso 4: Cálculo final módulo $1000$
Sumando los resultados de ambos casos:
$$N = N_1 + N_2 = 2 \cdot 3^{11} + 3^{12} = 5 \cdot 3^{11}$$

Calculamos $5 \cdot 3^{11}$:
$$3^{11} = 177147 \implies N = 5 \cdot 177147 = 885735$$

Tomando el residuo al dividir entre $1000$:
$$N \equiv 735 \pmod{1000}$$

\boxed{735}