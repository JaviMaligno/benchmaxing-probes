## Planteamiento

$777 = 3 \cdot 7 \cdot 37$. Aplico el TCR. La altura de la torre, $7^{7^7}$, es enormemente grande, así que todos los niveles necesarios existen.

**Módulo 7:** la torre es $7^{(\text{algo} \ge 1)} \equiv 0 \pmod 7$.

**Módulo 3:** $7 \equiv 1$, luego $7^{\text{cualquiera}} \equiv 1 \pmod 3$.

**Módulo 37:** calculo el orden de 7. Como $7^3 = 343 = 9\cdot 37 + 10 \equiv 10$ y $7^9 \equiv 10^3 = 1000 = 27\cdot 37 + 1 \equiv 1$, el orden es 9 (pues $7^3 \equiv 10 \neq 1$).

Necesito el exponente (la torre de altura una unidad menor) módulo 9:
- Orden de 7 módulo 9: $7^3 = 343 = 38\cdot 9 + 1 \equiv 1$, orden 3.
- Necesito la torre siguiente módulo 3, que vale $1$.
- Por tanto el exponente $\equiv 7^1 = 7 \pmod 9$.

Entonces, módulo 37: $7^7 = 7^6 \cdot 7 \equiv 26 \cdot 7 = 182 \equiv 34 \pmod{37}$.

## Reconstrucción por TCR

Busco $x$ con $x \equiv 0 \pmod 7$, $x \equiv 1 \pmod 3$, $x \equiv 34 \pmod{37}$.

Escribo $x = 7k$:
- $7k \equiv k \equiv 1 \pmod 3$
- $7k \equiv 34 \pmod{37}$, y como $7^{-1} \equiv 16$ (porque $7\cdot 16 = 112 \equiv 1$), resulta $k \equiv 34\cdot 16 = 544 \equiv 26 \pmod{37}$.

De $k = 26 + 37m$ con $k \equiv 1 \pmod 3$: $2 + m \equiv 1$, luego $m \equiv 2 \pmod 3$, y con $m = 2$ queda $k = 100$.

Así $x = 700$. Verificación: $700 = 7\cdot 100$ ✓, $700 \equiv 1 \pmod 3$ ✓, $700 - 666 = 34 \pmod{37}$ ✓.

\boxed{700}