Representamos las sillas como una cadena binaria de longitud 16, donde 1 significa silla ocupada y 0 silla vacía. Como hay 8 personas, hay exactamente 8 unos. La condición “ninguna persona se sienta junto a otras dos personas” equivale a que no haya tres unos consecutivos, es decir, no puede aparecer el bloque `111`.

Agrupamos los 8 unos en \(r\) bloques consecutivos. Como no puede haber tres unos seguidos, cada bloque tiene longitud 1 o 2. Si \(t\) bloques tienen longitud 2, entonces
\[
t + (r-t)+t = r+t = 8,
\]
por lo que \(t=8-r\). Así, \(r\) puede ser \(4,5,6,7,8\).

Para cada \(r\):
- Elegimos cuáles \(t=8-r\) bloques tienen longitud 2: \(\binom{r}{8-r}\) formas.
- Colocamos los \(r\) bloques entre los 8 ceros, dejando al menos un cero entre bloques consecutivos. Tras reservar \(r-1\) ceros separadores, quedan \(8-(r-1)=9-r\) ceros libres para repartir entre \(r+1\) huecos: \(\binom{9}{r}\) formas.

Entonces:
\[
N=\sum_{r=4}^{8} \binom{r}{8-r}\binom{9}{r}.
\]

Calculamos:
\[
\begin{aligned}
r=4 &: \binom{4}{4}\binom{9}{4}=1\cdot 126=126,\\
r=5 &: \binom{5}{3}\binom{9}{5}=10\cdot 126=1260,\\
r=6 &: \binom{6}{2}\binom{9}{6}=15\cdot 84=1260,\\
r=7 &: \binom{7}{1}\binom{9}{7}=7\cdot 36=252,\\
r=8 &: \binom{8}{0}\binom{9}{8}=1\cdot 9=9.
\end{aligned}
\]

Sumando:
\[
N=126+1260+1260+252+9=2907.
\]

Por tanto, el residuo al dividir entre \(1000\) es:
\[
2907 \equiv 907 \pmod{1000}.
\]

\[
\boxed{907}
\]