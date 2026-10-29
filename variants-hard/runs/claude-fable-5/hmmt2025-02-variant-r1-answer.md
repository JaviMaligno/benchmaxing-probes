Sea $N = \underline{abcde} = 10000a + m$, donde $m = \underline{bcde}$ (con $0 \le m \le 9999$).

La condición $\sqrt{10000a + m} = a\sqrt{m}$ al elevar al cuadrado da:

$$10000a + m = a^2 m \quad\Longrightarrow\quad m = \frac{10000a}{a^2 - 1}$$

Como $\gcd(a, a^2-1) = 1$, necesitamos que $a^2 - 1$ divida a $10000$. Probando $a = 2, \dots, 9$:

- $a=2$: $3 \nmid 20000$
- $a=3$: $m = 30000/8 = 3750$ ✓ → $N = 33750$ (verificación: $9 \cdot 3750 = 33750$)
- $a=4$: $15 \nmid 40000$
- $a=5$: $24 \nmid 50000$
- $a=6$: $35 \nmid 60000$
- $a=7$: $48 \nmid 70000$
- $a=8$: $63 \nmid 80000$
- $a=9$: $m = 90000/80 = 1125$ ✓ → $N = 91125$ (verificación: $81 \cdot 1125 = 91125$)

Las únicas soluciones son $33750$ y $91125$, y su suma es:

$$33750 + 91125 = 124875$$

$$\boxed{124875}$$