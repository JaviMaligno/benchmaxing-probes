Para hallar el valor de $\sum_{k=1}^{1080} \nu_3(b_k)$, expresemos primero los términos de la sucesión $b_k$ de forma explícita.

### Paso 1: Fórmula cerrada para $b_k$
El bloque de los primeros $10$ dígitos es $B = b_{10} = 1234567890$. Podemos escribir $b_r$ para $0 \le r \le 9$ (con $b_0 = 0$) como:
$$b_r = \sum_{j=1}^r j \cdot 10^{r-j} = \frac{10^{r+1} - 10 - 9r}{81}.$$
En particular, $b_9 = 123456789 = 9C$, donde $C = 13717421$ (cuya suma de dígitos es $26 \equiv 2 \pmod 3$, por lo que $\gcd(C, 3) = 1$), y $B = 10b_9 = 90C$.

Para cualquier entero $k = 10q + r$ con $q \ge 0$ y $0 \le r \le 9$, el número $b_{10q+r}$ está formado por $q$ bloques iguales a $B$ seguidos de los $r$ dígitos de $b_r$:
$$b_{10q+r} = b_r + B \cdot 10^r \sum_{i=0}^{q-1} 10^{10i} = b_r + 90C \cdot 10^r \frac{10^{10q} - 1}{10^{10} - 1}.$$
Sea $M = \frac{10^{10} - 1}{9} = 1111111111$. Como la suma de los dígitos de $M$ es $10$, se tiene $M \equiv 1 \pmod 3$ y $\gcd(M, 3) = 1$. Multiplicando por $M$ obtenemos:
$$M b_{10q+r} = M b_r + C \cdot 10^{r+1} (10^{10q} - 1),$$
y dado que $\gcd(M, 3) = 1$, se cumple que $\nu_3(b_{10q+r}) = \nu_3(M b_{10q+r})$.

---

### Paso 2: Análisis según el residuo $r = k \bmod 10$
La suma de los dígitos de $B$ es $45 \equiv 0 \pmod 9$, por lo que la suma de los dígitos de $b_{10q+r}$ es congruente con $\frac{r(r+1)}{2} \pmod 9$.

1. **Casos $r \in \{1, 4, 7\}$:**
   La suma de dígitos es $\frac{r(r+1)}{2} \equiv 1 \pmod 3$. Por tanto, $3 \nmid b_{10q+r}$ y:
   $$\nu_3(b_{10q+r}) = 0.$$

2. **Casos $r \in \{2, 3, 5, 6\}$:**
   La suma de dígitos es $\frac{r(r+1)}{2} \in \{3, 6, 15, 21\} \equiv 3 \text{ o } 6 \pmod 9$. Así, $b_{10q+r}$ es múltiplo de $3$ pero no de $9$, luego:
   $$\nu_3(b_{10q+r}) = 1.$$

3. **Caso $r = 0$ ($k = 10q$, con $1 \le q \le 108$):**
   Como $b_0 = 0$, tenemos $M b_{10q} = C \cdot 10 (10^{10q} - 1)$. Aplicando el lema de *Lifting the Exponent* (LTE):
   $$\nu_3(b_{10q}) = \nu_3(10^{10q} - 1) = \nu_3(10 - 1) + \nu_3(10q) = 2 + \nu_3(q).$$

4. **Caso $r = 9$ ($k = 10q + 9$, con $0 \le q \le 107$):**
   Al añadir el dígito de las unidades de $10(q+1)$ (que es $0$) a la derecha de $b_{10q+9}$, se obtiene exactamente $b_{10(q+1)} = 10 b_{10q+9}$. Por tanto:
   $$\nu_3(b_{10q+9}) = \nu_3(b_{10(q+1)}) = 2 + \nu_3(q + 1).$$

5. **Caso $r = 8$ ($k = 10q + 8$, con $0 \le q \le 107$):**
   Observamos que $b_{10q+9} = 10 b_{10q+8} + 9$. Multiplicando por $M$ y usando que $M b_{10q+9} = C(10^{10(q+1)} - 1)$ y $9M = 10^{10} - 1$, resulta:
   $$10 M b_{10q+8} = C(10^{10(q+1)} - 1) - (10^{10} - 1) = (10^{10} - 1)(C S_m - 1),$$
   donde $m = q + 1 \in \{1, 2, \dots, 108\}$ y $S_m = \frac{10^{10m} - 1}{10^{10} - 1}$. Como $\nu_3(10^{10} - 1) = 2$, tenemos:
   $$\nu_3(b_{10q+8}) = 2 + \nu_3(C S_m - 1).$$
   Desarrollando $10^{10m} = (1 + 9M)^m$ mediante el teorema del binomio:
   $$S_m = \frac{(1 + 9M)^m - 1}{9M} = m + 9M \binom{m}{2} + 81M^2 \binom{m}{3} + 729M^3 \binom{m}{4} + \cdots$$
   Como $81C = M - 10 = \frac{10^{10} - 91}{9}$, usando el desarrollo binomial de $(1 + 9)^{10}$ se obtiene $C \equiv 71 \equiv -10 \pmod{81}$ y $C \equiv 71 \pmod{243}$, mientras que $M \equiv 10 \pmod{81}$.
   - Módulo $3$: $C S_m - 1 \equiv 2m - 1 \pmod 3$, que es divisible por $3$ si y solo si $m \equiv 2 \pmod 3$, es decir, $3 \mid (m + 1)$.
   - Si $m \equiv 2 \pmod 3$, entonces $3 \mid (m - 2)$, por lo que $\binom{m}{3}$ es un entero y $81M^2 \binom{m}{3} \equiv 0 \pmod{81}$ (y los términos de orden $k \ge 4$ son múltiplos de $243$).
   - Módulo $9$: $C S_m - 1 \equiv -m - 1 \pmod 9$, que es divisible por $9$ si y solo si $m \equiv 8 \pmod 9$.
   - Si $m \equiv 8 \pmod 9$, entonces $\binom{m}{2} \equiv 1 \pmod 9$ y $9M\binom{m}{2} \equiv 9 \pmod{81}$. Así, $S_m \equiv m + 9 \pmod{81}$ y:
     $$C S_m - 1 \equiv -10(m + 9) - 1 = -10m - 91 \equiv -10(m + 1) \pmod{81}.$$
   - Para el único valor en el rango con $m \equiv 80 \pmod{81}$, que es $m = 80$, calculamos módulo $243$:
     $$S_{80} \equiv 80 + 9(10)\binom{80}{2} + 81(1^2)\binom{80}{3} \equiv 80 + 90 + 81 = 251 \equiv 8 \pmod{243},$$
     de donde $C S_{80} - 1 \equiv 71 \times 8 - 1 = 567 \equiv 81 \pmod{243}$, luego $\nu_3(C S_{80} - 1) = 4 = \nu_3(80 + 1)$.

   En consecuencia, para todo $m \in \{1, \dots, 108\}$ se cumple $\nu_3(C S_m - 1) = \nu_3(m + 1)$, lo que implica:
   $$\nu_3(b_{10q+8}) = 2 + \nu_3(q + 2).$$

---

### Paso 3: Cálculo de la suma total
Para $1 \le k \le 1080$, hay exactamente $108$ valores de $q$ para cada residuo $r \in \{0, 1, \dots, 9\}$:
- Para $r \in \{1, 4, 7\}$, la suma aporta $0$.
- Para $r \in \{2, 3, 5, 6\}$, la suma aporta $4 \times 108 \times 1 = 432$.
- Para $r = 0$ ($1 \le q \le 108$):
  $$\sum_{q=1}^{108} (2 + \nu_3(q)) = 216 + \nu_3(108!).$$
- Para $r = 9$ ($0 \le q \le 107$, haciendo $m = q + 1 \in \{1, \dots, 108\}$):
  $$\sum_{m=1}^{108} (2 + \nu_3(m)) = 216 + \nu_3(108!).$$
- Para $r = 8$ ($0 \le q \le 107$, haciendo $n = q + 2 \in \{2, \dots, 109\}$ y notando que $\nu_3(1) = \nu_3(109) = 0$):
  $$\sum_{n=2}^{109} (2 + \nu_3(n)) = 216 + \nu_3(108!).$$

Por la fórmula de Legendre:
$$\nu_3(108!) = \left\lfloor \frac{108}{3} \right\rfloor + \left\lfloor \frac{108}{9} \right\rfloor + \left\lfloor \frac{108}{27} \right\rfloor + \left\lfloor \frac{108}{81} \right\rfloor = 36 + 12 + 4 + 1 = 53.$$

Sumando todas las contribuciones:
$$\sum_{k=1}^{1080} \nu_3(b_k) = 432 + 3 \times (216 + 53) = 432 + 807 = 1239.$$

\boxed{1239}