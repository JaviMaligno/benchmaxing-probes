## Solución

Escribimos $f_i(j) = g(i,j)$ y calculamos la "fila" $f_i$ completa a partir de la fila anterior, usando:
- $f_i(0) = f_{i-1}(2)$
- $f_i(j) = f_{i-1}(f_i(j-1))$ para $j = 1,2,3,4$

**Fila 0:** $f_0(j) = (j+1) \bmod 5$, es decir $[1,2,3,4,0]$.

**Fila 1** (con $f_0(j)=(j+1)\bmod 5$):
- $f_1(0)=f_0(2)=3$
- $f_1(1)=f_0(3)=4$
- $f_1(2)=f_0(4)=0$
- $f_1(3)=f_0(0)=1$
- $f_1(4)=f_0(1)=2$

Fila 1: $[3,4,0,1,2]$.

**Fila 2** (usando fila 1: $[3,4,0,1,2]$):
- $f_2(0)=f_1(2)=0$
- $f_2(1)=f_1(0)=3$
- $f_2(2)=f_1(3)=1$
- $f_2(3)=f_1(1)=4$
- $f_2(4)=f_1(4)=2$

Fila 2: $[0,3,1,4,2]$.

**Fila 3** (usando fila 2):
- $f_3(0)=f_2(2)=1$
- $f_3(1)=f_2(1)=3$
- $f_3(2)=f_2(3)=4$
- $f_3(3)=f_2(4)=2$
- $f_3(4)=f_2(2)=1$

Fila 3: $[1,3,4,2,1]$.

**Fila 4** (usando fila 3):
- $f_4(0)=f_3(2)=4$
- $f_4(1)=f_3(4)=1$
- $f_4(2)=f_3(1)=3$
- $f_4(3)=f_3(3)=2$
- $f_4(4)=f_3(2)=4$

Fila 4: $[4,1,3,2,4]$.

**Fila 5** (usando fila 4):
- $f_5(0)=f_4(2)=3$
- $f_5(1)=f_4(3)=2$
- $f_5(2)=f_4(2)=3$
- $f_5(3)=f_4(3)=2$
- $f_5(4)=f_4(2)=3$

Fila 5: $[3,2,3,2,3]$.

**Fila 6** (usando fila 5):
- $f_6(0)=f_5(2)=3$
- $f_6(1)=f_5(3)=2$
- $f_6(2)=f_5(2)=3$
- $f_6(3)=f_5(3)=2$
- $f_6(4)=f_5(2)=3$

Fila 6: $[3,2,3,2,3]$, igual a la fila 5.

Como cada fila depende **solo** de la fila anterior, y la fila 6 coincide con la fila 5, por inducción $f_i = [3,2,3,2,3]$ para todo $i \ge 5$. En particular, para $i = 2024$:

$$g(2024,3) = f_{2024}(3) = 2$$

\boxed{2}