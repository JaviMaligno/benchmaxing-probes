## Factorización

**Paso 1.** Usamos la identidad $x^5-1=(x-1)(x^4+x^3+x^2+x+1)$ con $x=80$:

$$80^5-1 = 79 \cdot (80^4+80^3+80^2+80+1) = 79 \cdot 41{,}478{,}481$$

**Paso 2.** $79$ es primo.

**Paso 3.** Todo factor primo de $\Phi_5(80)=41{,}478{,}481$ debe ser $\equiv 1 \pmod 5$ (y, al ser impar, $\equiv 1 \pmod{10}$), salvo el propio $5$, que no divide porque $80\not\equiv 1\pmod 5$.

- Por el criterio de divisibilidad alternado: $1-8+4-8+7-4+1-4=-11$, así que $11 \mid 41{,}478{,}481$:
$$41{,}478{,}481 = 11 \cdot 3{,}770{,}771$$

- Probando los candidatos $\equiv 1 \pmod{10}$ hasta $\sqrt{3{,}770{,}771}\approx 1942$:
$$3{,}770{,}771 = 751 \cdot 5021$$

**Paso 4.** $751$ es primo. Para $5021$ basta probar los candidatos $\equiv 1\pmod{10}$ hasta $\sqrt{5021}\approx 70.9$: $11, 31, 41, 61$ — ninguno divide, luego $5021$ es primo.

**Verificación:** $11 \cdot 751 = 8261$ y $8261 \cdot 5021 = 41{,}478{,}481$ ✓

$$80^5-1 = 11 \cdot 79 \cdot 751 \cdot 5021$$

El mayor factor primo es $5021 > 751 > 79 > 11$.

$$\boxed{5021}$$