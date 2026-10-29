# Solución paso a paso

**Paso 1: Suma de la cuadrícula de Isabella.**
Isabella escribe los números $1, 2, \ldots, ab$, así que su suma es:
$$S_I = \frac{ab(ab+1)}{2}$$

**Paso 2: Suma de la cuadrícula de Vidur.**
Vidur pone $ij$ en la celda $(i,j)$, así que su suma es:
$$S_V = \left(\sum_{i=1}^{a} i\right)\left(\sum_{j=1}^{b} j\right) = \frac{a(a+1)}{2} \cdot \frac{b(b+1)}{2} = \frac{ab(a+1)(b+1)}{4}$$

**Paso 3: Diferencia.**
$$S_I - S_V = \frac{ab}{4}\Big(2(ab+1) - (a+1)(b+1)\Big) = \frac{ab}{4}\Big(2ab + 2 - ab - a - b - 1\Big) = \frac{ab(ab - a - b + 1)}{4}$$

Factorizando $ab - a - b + 1 = (a-1)(b-1)$:
$$S_I - S_V = \frac{ab(a-1)(b-1)}{4}$$

**Verificación con el ejemplo** ($a=3$, $b=4$): $\frac{12 \cdot 2 \cdot 3}{4} = 18$, y en efecto $78 - 60 = 18$. ✓

**Paso 4: Resolver la ecuación.**
$$\frac{ab(a-1)(b-1)}{4} = 1200 \quad\Longrightarrow\quad ab(a-1)(b-1) = 4800$$

Probando valores: con $a = 5$:
$$5b \cdot 4(b-1) = 4800 \quad\Longrightarrow\quad b(b-1) = 240 \quad\Longrightarrow\quad b = 16$$

(Verificamos que $16 \cdot 15 = 240$. ✓ Se puede comprobar que no hay otras soluciones enteras positivas; por ejemplo $a=6$ exige $b(b-1)=160$, $a=4$ exige $b(b-1)=400$, $a=3$ exige $b(b-1)=800$, ninguna con solución entera, y el caso simétrico $a=16, b=5$ da lo mismo.)

**Comprobación final:** $a=5$, $b=16$: $\frac{5 \cdot 16 \cdot 4 \cdot 15}{4} = \frac{4800}{4} = 1200$. ✓

Por lo tanto:
$$a + b = 5 + 16 = \boxed{21}$$