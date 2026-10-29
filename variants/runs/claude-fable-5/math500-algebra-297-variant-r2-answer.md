Sustituyendo $y = x^2 - 7$ en $y^2 = -9x + 45$:

$$(x^2-7)^2 = -9x + 45 \implies x^4 - 14x^2 + 9x + 4 = 0$$

Las raíces de este polinomio son los valores de $x$ de las soluciones. Probando raíces racionales: $x=1$ funciona, y tras factorizar queda $x^3 + x^2 - 13x - 4$, que tiene raíz $x=-4$, dejando $x^2 - 3x - 1 = 0$ con raíces reales $\frac{3\pm\sqrt{13}}{2}$. Las cuatro raíces son distintas, así que hay cuatro soluciones distintas.

El producto buscado es $\prod_i (x_i^2 - 7)$. Como $P(x) = x^4 - 14x^2 + 9x + 4 = \prod_i (x - x_i)$, se tiene:

$$\prod_i (x_i^2 - 7) = \prod_i (x_i - \sqrt{7})(x_i + \sqrt{7}) = P(\sqrt{7}) \cdot P(-\sqrt{7})$$

Calculando:
- $P(\sqrt{7}) = 49 - 98 + 9\sqrt{7} + 4 = -45 + 9\sqrt{7}$
- $P(-\sqrt{7}) = 49 - 98 - 9\sqrt{7} + 4 = -45 - 9\sqrt{7}$

$$P(\sqrt{7}) \cdot P(-\sqrt{7}) = (-45)^2 - 81 \cdot 7 = 2025 - 567 = 1458$$

Verificación directa: los valores de $y$ son $-6$ (de $x=1$), $9$ (de $x=-4$) y $\frac{-3\pm 3\sqrt{13}}{2}$, cuyo producto es $(-6)(9)\cdot\frac{9 - 117}{4} = (-54)(-27) = 1458$. ✓

$$\boxed{1458}$$