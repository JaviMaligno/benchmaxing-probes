## Factorización

**Paso 1.** Uso la diferencia de potencias:

$$45^5-1=(45-1)\left(45^4+45^3+45^2+45+1\right)$$

**Paso 2.** Primer factor: $44=2^2\cdot 11$.

**Paso 3.** Segundo factor (quinto polinomio ciclotómico en 45):

$$4100625+91125+2025+45+1=4193821$$

**Paso 4.** Todo primo $p$ que divide a $\Phi_5(45)$ cumple $p\equiv 1 \pmod 5$ (o $p=5$, imposible aquí porque $45^5-1\equiv -1 \bmod 5$). Basta probar primos $\equiv 1 \pmod 5$ hasta $\sqrt{4193821}\approx 2048$: $11, 31, 41, 61, \dots$ Todos fallan hasta llegar a

$$4193821 = 1471 \cdot 2851$$

(verificación: $1471\cdot 2851 = 4\,118\,800 + 75\,021 = 4\,193\,821$).

**Paso 5.** Ambos son primos:
- $1471$: no divisible por $2,3,5,7,11,13,17,19,23,29,31,37$, y $\sqrt{1471}\approx 38{,}4$.
- $2851$: no divisible por primos hasta $53$, y $\sqrt{2851}\approx 53{,}4$.

**Factorización completa:**

$$45^5-1 = 184\,528\,124 = 2^2\cdot 11\cdot 1471\cdot 2851$$

El mayor factor primo es $2851$.

$$\boxed{2851}$$