Para encontrar el número $M$ de ternas ordenadas de enteros positivos $(x, y, z)$ con $x, y, z \le 3^7$ tales que $x^3 + y^3 + z^3$ es divisible por $3^8$, planteamos el problema de forma general.

Sea $M_n$ el número de ternas $(x, y, z) \in \{1, 2, \dots, 3^n\}^3$ tales que:
$$x^3 + y^3 + z^3 \equiv 0 \pmod{3^{n+1}}$$
Buscamos calcular $M_7 \pmod{1000}$.

### Paso 1: Propiedades de los cubos módulo $3^{n+1}$
Para cualquier entero $x$ y $n \ge 1$, al sumar un múltiplo de $3^n$ tenemos:
$$(x + k \cdot 3^n)^3 = x^3 + 3k x^2 \cdot 3^n + 3k^2 x \cdot 3^{2n} + k^3 \cdot 3^{3n} \equiv x^3 \pmod{3^{n+1}}$$
Por lo tanto, el valor de $x^3 \pmod{3^{n+1}}$ depende únicamente de la clase de resto de $x \pmod{3^n}$. Podemos entonces considerar $x, y, z \in \mathbb{Z}/3^n\mathbb{Z}$.

Consideremos la aplicación $f: (\mathbb{Z}/3^n\mathbb{Z})^\times \to (\mathbb{Z}/3^{n+1}\mathbb{Z})^\times$ dada por $f(x) = x^3 \pmod{3^{n+1}}$.
- Si $x^3 \equiv y^3 \pmod{3^{n+1}}$ con $\gcd(x, 3) = \gcd(y, 3) = 1$, entonces $(x y^{-1})^3 \equiv 1 \pmod{3^{n+1}}$, lo que implica (por el lema de Hensel / LTE) que $x y^{-1} \equiv 1 \pmod{3^n}$, es decir, $x \equiv y \pmod{3^n}$. Así, $f$ es inyectiva.
- Para todo $x$ coprimo con $3$, se cumple que $x^3 \equiv \pm 1 \pmod 9$. El conjunto de restos módulo $3^{n+1}$ que son congruentes con $\pm 1 \pmod 9$ tiene tamaño $2 \cdot 3^{(n+1)-2} = 2 \cdot 3^{n-1}$, que coincide exactamente con el tamaño de $(\mathbb{Z}/3^n\mathbb{Z})^\times$.

En consecuencia, cuando $x$ recorre los $2 \cdot 3^{n-1}$ elementos de $(\mathbb{Z}/3^n\mathbb{Z})^\times$, $x^3 \pmod{3^{n+1}}$ toma cada uno de los valores congruentes con $\pm 1 \pmod 9$ **exactamente una vez**.

---

### Paso 2: Clasificación según la divisibilidad por $3$
Para $n \ge 1$, clasificamos las ternas $(x, y, z) \in (\mathbb{Z}/3^n\mathbb{Z})^3$ según cuántas de sus componentes son divisibles por $3$:

1. **Ninguna variable es divisible por $3$:**
   Entonces $x^3, y^3, z^3 \equiv \pm 1 \pmod 9$. La suma de tres elementos en $\{1, -1\}$ solo puede ser $\pm 1$ o $\pm 3$, por lo que $x^3 + y^3 + z^3 \not\equiv 0 \pmod 9$ y no puede ser divisible por $3^{n+1}$ (ya que $n+1 \ge 2$). Hay **$0$ soluciones**.

2. **Exactamente una variable es divisible por $3$:**
   Hay $3$ formas de elegir cuál de las variables es múltiplo de $3$ (supongamos que es $z$, mientras que $3 \nmid x, y$).
   - Hay $3^{n-1}$ elecciones para $z \in \mathbb{Z}/3^n\mathbb{Z}$ con $3 \mid z$. En todas ellas se cumple $z^3 \equiv 0 \pmod 9$.
   - Hay $2 \cdot 3^{n-1}$ elecciones para $x \in (\mathbb{Z}/3^n\mathbb{Z})^\times$.
   - Para que $y^3 \equiv -x^3 - z^3 \pmod{3^{n+1}}$, notamos que $-x^3 - z^3 \equiv -x^3 \equiv \mp 1 \pmod 9$. Por la biyección del Paso 1, para cada elección de $x$ y $z$ existe un **único** $y \in (\mathbb{Z}/3^n\mathbb{Z})^\times$ que satisface la congruencia.
   
   Por tanto, este caso aporta:
   $$3 \times 3^{n-1} \times (2 \cdot 3^{n-1}) \times 1 = 2 \cdot 3^{2n-1} \text{ soluciones.}$$

3. **Exactamente dos variables son divisibles por $3$:**
   Dos de los cubos son $\equiv 0 \pmod 9$ y el tercero es $\equiv \pm 1 \pmod 9$, por lo que su suma es $\equiv \pm 1 \not\equiv 0 \pmod 9$. Hay **$0$ soluciones**.

4. **Las tres variables son divisibles por $3$:**
   Escribimos $x = 3x'$, $y = 3y'$, $z = 3z'$ con $x', y', z' \in \{1, 2, \dots, 3^{n-1}\}$. La condición se convierte en:
   $$27(x'^3 + y'^3 + z'^3) \equiv 0 \pmod{3^{n+1}} \iff x'^3 + y'^3 + z'^3 \equiv 0 \pmod{3^{n-2}}$$
   Para $n \ge 4$, dado que $n-2 = (n-3) + 1$ y $n-3 \ge 1$, el valor de $x'^3 \pmod{3^{n-2}}$ depende únicamente de $x' \pmod{3^{n-3}}$. Como cada clase módulo $3^{n-3}$ se repite $3^2 = 9$ veces en $\{1, \dots, 3^{n-1}\}$, para las tres variables cada terna en $(\mathbb{Z}/3^{n-3}\mathbb{Z})^3$ se repite $(3^2)^3 = 3^6$ veces.
   Por lo tanto, para $n \ge 4$, este caso aporta $3^6 M_{n-3}$ soluciones.

---

### Paso 3: Recurrencia y cálculo de $M_7$
De los casos anteriores obtenemos, para $n \ge 4$:
$$M_n = 2 \cdot 3^{2n-1} + 3^6 M_{n-3}$$

Calculamos primero el caso base $M_1$:
- Para $n = 1$, el Caso 2 aporta $2 \cdot 3^{2(1)-1} = 6$ soluciones.
- El Caso 4 corresponde a $x \equiv y \equiv z \equiv 0 \pmod 3$, donde $x^3 + y^3 + z^3$ es múltiplo de $27$ (y por tanto de $9$), aportando $1$ solución: $(3, 3, 3)$.
Así, $M_1 = 6 + 1 = 7$.

Aplicamos ahora la recurrencia para llegar a $M_7$:
$$M_4 = 2 \cdot 3^7 + 3^6 M_1$$
$$M_7 = 2 \cdot 3^{13} + 3^6 M_4 = 2 \cdot 3^{13} + 3^6(2 \cdot 3^7 + 3^6 M_1) = 2 \cdot 3^{13} + 2 \cdot 3^{13} + 3^{12} M_1$$

Sustituyendo $M_1 = 7$ y factorizando $3^{12}$:
$$M_7 = 6 \cdot 3^{12} + 6 \cdot 3^{12} + 7 \cdot 3^{12} = 19 \cdot 3^{12}$$

---

### Paso 4: Cálculo módulo $1000$
Calculamos $3^{12} \pmod{1000}$:
$$3^6 = 729$$
$$3^{12} = 729^2 = 531441 \equiv 441 \pmod{1000}$$

Finalmente, multiplicamos por $19$:
$$M_7 \equiv 19 \times 441 = 8379 \equiv 379 \pmod{1000}$$

\boxed{379}