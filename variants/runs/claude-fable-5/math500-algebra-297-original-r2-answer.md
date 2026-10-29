Voy a resolver el sistema paso a paso.

**Paso 1: Sustituir.** De la primera ecuación, $y = x^2 - 8$. Sustituyendo en $y^2 = -5x + 44$:

$$(x^2-8)^2 = -5x + 44 \implies x^4 - 16x^2 + 64 + 5x - 44 = 0 \implies x^4 - 16x^2 + 5x + 20 = 0$$

**Paso 2: Factorizar la cuártica.** Busco una factorización $(x^2+ax+b)(x^2-ax+c)$, lo que exige $b+c-a^2=-16$, $a(c-b)=5$, $bc=20$. Con $a=5$: $b+c=9$ y $c-b=1$, es decir $c=5$, $b=4$, y $bc=20$ ✓. Entonces:

$$x^4 - 16x^2 + 5x + 20 = (x^2+5x+4)(x^2-5x+5) = 0$$

**Paso 3: Hallar las soluciones.**
- $x^2+5x+4=0 \implies x=-1$ o $x=-4$
- $x^2-5x+5=0 \implies x=\dfrac{5\pm\sqrt{5}}{2}$

Las cuatro raíces son distintas y reales. Sus coordenadas $y = x^2-8$:
- $x=-1 \implies y=-7$
- $x=-4 \implies y=8$
- $x=\dfrac{5\pm\sqrt{5}}{2} \implies x^2 = \dfrac{15\pm5\sqrt{5}}{2} \implies y = \dfrac{-1\pm5\sqrt{5}}{2}$

**Paso 4: Producto de las $y$.** El producto de las dos últimas es $\dfrac{(-1)^2-(5\sqrt5)^2}{4} = \dfrac{1-125}{4} = -31$. Entonces:

$$(-7)(8)(-31) = 1736$$

(Verificación: eliminando $x$ se obtiene $y^4 - 88y^2 - 25y + 1736 = 0$, cuyo producto de raíces es el término constante $1736$ ✓.)

$$\boxed{1736}$$