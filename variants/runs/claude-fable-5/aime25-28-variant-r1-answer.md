## Planteamiento

La recurrencia es $y_{k+1} = \dfrac{y_k^2 - y_k + 1}{3y_k}$. Escribo $y_k = \dfrac{a_k}{b_k}$ en forma reducida, de modo que

$$a_{k+1}' = a_k^2 - a_k b_k + b_k^2, \qquad b_{k+1}' = 3a_k b_k.$$

## El factor común es exactamente 3

Con $a_1 = 19,\ b_1 = 14$: son coprimos, $3 \nmid a_1$, $3 \nmid b_1$, pero $3 \mid a_1 + b_1 = 33$.

Si $b \equiv -a \pmod 3$, escribiendo $b = -a + 3t$:

$$a^2 - ab + b^2 = 3(a^2 - 3at + 3t^2),$$

donde $a^2 - 3at + 3t^2 \equiv a^2 \not\equiv 0 \pmod 3$. Como $3 \nmid a,b$, tanto el numerador como el denominador tienen **exactamente** un factor 3. La fracción reducida es

$$a_{k+1} = \frac{a_k^2 - a_k b_k + b_k^2}{3}, \qquad b_{k+1} = a_k b_k,$$

que son coprimos (un primo común dividiría a $a_k$ o $b_k$ y luego al otro, contradicción). Además las condiciones ($3\nmid a$, $3\nmid b$, $3 \mid a+b$) se preservan, así que esto vale para todo $k$.

## La suma satisface una recurrencia limpia

$$S_{k+1} = a_{k+1} + b_{k+1} = \frac{a_k^2 - a_k b_k + b_k^2 + 3a_k b_k}{3} = \frac{(a_k + b_k)^2}{3} = \frac{S_k^2}{3}.$$

Con $S_1 = 33 = 3 \cdot 11$, por inducción:

$$S_k = 3 \cdot 11^{2^{k-1}} \quad\Longrightarrow\quad m + n = S_{2025} = 3 \cdot 11^{2^{2024}}.$$

(Verificación: $y_2 = \frac{291}{798} = \frac{97}{266}$, y $97 + 266 = 363 = 3 \cdot 11^2$ ✓.)

## Cálculo módulo 1000

Primero el orden de 11: $11^{10} \equiv 601$, $11^{25} \equiv 251$, $11^{50} \equiv 251^2 = 63001 \equiv 1 \pmod{1000}$. Así que reduzco el exponente módulo 50.

**Exponente:** $2^{2024} \bmod 50$. Módulo 25, el orden de 2 es 20 y $2024 \equiv 4 \pmod{20}$, luego $2^{2024} \equiv 2^4 = 16 \pmod{25}$; como es par, $2^{2024} \equiv 16 \pmod{50}$.

**Potencia:** $11^{16} \bmod 1000$:
$$11^2 = 121,\quad 11^4 \equiv 641,\quad 11^8 \equiv 641^2 = 410881 \equiv 881,\quad 11^{16} \equiv 881^2 = 776161 \equiv 161.$$

Por tanto:

$$m + n \equiv 3 \cdot 161 = 483 \pmod{1000}.$$

$$\boxed{483}$$