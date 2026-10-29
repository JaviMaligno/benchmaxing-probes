## Planteamiento

Como $3^7 = 2187$ y $3^6 = 729$, observo primero que si $a \equiv b \pmod{3^6}$ entonces
$$a^3 = b^3 + 3b^2\cdot 3^6k + \dots \equiv b^3 \pmod{3^7}.$$
Luego $a^3 \bmod 3^7$ solo depende de $a \bmod 729$, y $a$ recorre un sistema completo de restos módulo $729$.

## Distribución de los cubos

Sea $f(v) = \#\{a \le 729 : a^3 \equiv v \pmod{2187}\}$. Según $v_3(a)$:

- $3 \nmid a$ (486 valores): el cubo es inyectivo sobre las unidades mód $729$, y su imagen es el subgrupo de índice 3 de cubos, que es exactamente $U=\{u \equiv \pm 1 \pmod 9\}$ (486 elementos). Así $f(u)=1$ para $u\in U$.
- $v_3(a)=1$: $a^3 = 27a'^3$, y $a'^3 \bmod 81$ recorre $H'=\{h \bmod 81 : h\equiv \pm1 \pmod 9\}$ (18 valores), cada uno 9 veces: $f(27h)=9$.
- $v_3(a)=2$: $a^3 = 729a''^3$ con $a''^3\equiv a'' \pmod 3$: $f(729)=f(1458)=27$.
- $v_3(a)\ge 3$: $f(0)=27$.

Comprobación: $486+162+54+27=729$. ✔

## Casos según cuántos términos son unidades

**Tres unidades:** cada $u_i \equiv \pm1 \pmod 9$, así que la suma es $\pm1$ o $\pm3$ mód 9, nunca $0$. → **0**

**Una unidad:** la suma es unidad mód 3. → **0**

**Dos unidades:** se necesita mezcla ($u_1\equiv 1$, $u_2\equiv -1$ mód 9). Escribiendo $u_2=-u_2'$ con $u_1,u_2'$ recorriendo los $243$ restos $\equiv 1 \pmod 9$, la suma es $9m$ con cada $m \in \mathbb{Z}/243$ alcanzado $243$ veces. Entonces
$$\sum_m f(-9m) = 27 + 18\cdot 9 + 2\cdot 27 = 243,$$
de donde $243\cdot 243 = 59049$, por $2$ (orden) y por $3$ (posición del tercer término): $\;3\cdot 118098 = 354294$.

**Ninguna unidad** (términos de valuación $3$, $6$ o $\infty$):
- Tres de tipo $27h$: requeriría $h_1+h_2+h_3\equiv 0 \pmod 9$, imposible. → 0
- Uno de tipo $27h$: la valuación sería exactamente 3. → 0
- Dos de tipo $27h$: hay $18$ pares con $h_1+h_2 \equiv -t/27 \pmod{81}$ para cada $t\in\{0,729,1458\}$, luego $3\cdot 81\cdot 18\cdot 81 = 354294$.
- Ninguno: $729(s_1+s_2+s_3)\equiv 0$ con $s_i\in\{0,1,2\}$ de peso 27: $9\cdot 27^3 = 177147$.

## Total

$$N = 354294 + 354294 + 177147 = 885735$$

$885735 \equiv 735 \pmod{1000}$.

\boxed{735}