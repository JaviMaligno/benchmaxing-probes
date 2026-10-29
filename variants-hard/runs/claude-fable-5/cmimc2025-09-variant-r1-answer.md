## Resolución

**Paso 1: Factorización algebraica.** Usando $x^5 - 1 = (x-1)(x^4 + x^3 + x^2 + x + 1)$ con $x = 80$:

$$80^5 - 1 = 79 \cdot (80^4 + 80^3 + 80^2 + 80 + 1)$$

El primer factor, $79$, es primo. El segundo factor vale:

$$40\,960\,000 + 512\,000 + 6400 + 80 + 1 = 41\,478\,481$$

**Paso 2: Factorizar $41\,478\,481$.** Este número es $\Phi_5(80)$ (el quinto polinomio ciclotómico evaluado en 80), así que todo primo que lo divida debe ser $\equiv 1 \pmod 5$ (o ser 5, que aquí no divide). Eso restringe la búsqueda a primos terminados en 1.

- **Prueba con 11:** $80 \equiv 3 \pmod{11}$ y $3^5 = 243 \equiv 1 \pmod{11}$, así que 11 divide. En efecto, $41\,478\,481 = 11 \cdot 3\,770\,771$.
- **Factorizar $3\,770\,771$:** probando primos $\equiv 1 \pmod{10}$ se encuentra $751 \cdot 5021 = 3\,755\,000 + 15\,771 = 3\,770\,771$. ✓

**Paso 3: Verificar primalidad.**
- $751$: no es divisible por ningún primo hasta $\sqrt{751} \approx 27{,}4$ (2, 3, 5, 7, 11, 13, 17, 19, 23). Es primo.
- $5021$: no es divisible por ningún primo hasta $\sqrt{5021} \approx 70{,}9$ (se comprueban todos: 7 da resto 2, 31 da resto 30, 67 da resto 63, etc.). Es primo.

**Verificación final:** $79 \cdot 11 \cdot 751 \cdot 5021 = 79 \cdot 41\,478\,481 = 3\,276\,799\,999 = 80^5 - 1$. ✓

Por lo tanto, $80^5 - 1 = 11 \cdot 79 \cdot 751 \cdot 5021$, y el mayor factor primo es:

$$\boxed{5021}$$