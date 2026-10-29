## Solución

**Suma de Priya:** es la suma de $1$ a $mn$:
$$S_P = \frac{mn(mn+1)}{2}$$

**Suma de Tomás:** es el producto de las sumas de filas y columnas:
$$S_T = \left(\frac{m(m+1)}{2}\right)\left(\frac{n(n+1)}{2}\right) = \frac{m(m+1)n(n+1)}{4}$$

**Diferencia:**
$$S_P - S_T = \frac{mn}{4}\Big(2(mn+1) - (m+1)(n+1)\Big) = \frac{mn}{4}\Big(mn + 1 - m - n\Big) = \frac{mn(m-1)(n-1)}{4}$$

Igualando a $2100$:
$$mn(m-1)(n-1) = 8400$$

**Búsqueda de soluciones:** escribiendo $a = m-1$, $b = n-1$, necesitamos $ab(a+1)(b+1) = 8400$.

Probando $a = 4$, $b = 20$:
$$4 \cdot 20 \cdot 5 \cdot 21 = 80 \cdot 105 = 8400 \checkmark$$

Es decir, $m = 5$, $n = 21$ (y el caso simétrico $m=21$, $n=5$). Verificando que no hay otras factorizaciones: se comprueba que es la única solución con enteros positivos (por ejemplo, $a=5$ requeriría $b(b+1)=280$, $a=7$ daría $b(b+1)=150$, etc., ninguna entera).

**Comprobación:** $mn(m-1)(n-1)/4 = 5\cdot 21\cdot 4\cdot 20/4 = 2100$ ✓

Por lo tanto:
$$m + n = 5 + 21 = \boxed{26}$$