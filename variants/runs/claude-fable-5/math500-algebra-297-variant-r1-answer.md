Sustituyendo $y = x^2 - 7$ en la segunda ecuación:

$$(x^2-7)^2 = -9x + 45 \implies x^4 - 14x^2 + 9x + 4 = 0$$

**Factorización:** probando raíces racionales, $x=1$ funciona ($1 - 14 + 9 + 4 = 0$), y luego $x=-4$ ($-64+16+52-4=0$). Dividiendo:

$$x^4 - 14x^2 + 9x + 4 = (x-1)(x+4)(x^2 - 3x - 1)$$

El factor cuadrático da $x = \frac{3 \pm \sqrt{13}}{2}$, así que hay 4 soluciones distintas.

**Coordenadas $y$ (usando $y = x^2 - 7$):**
- $x = 1 \Rightarrow y = -6$
- $x = -4 \Rightarrow y = 9$
- Para las raíces de $x^2 = 3x + 1$: $y = x^2 - 7 = 3x - 6$. El producto de esas dos $y$ es
$$(3x_1 - 6)(3x_2 - 6) = 9x_1x_2 - 18(x_1 + x_2) + 36 = 9(-1) - 18(3) + 36 = -27$$

**Producto total:**
$$(-6)(9)(-27) = 1458$$

Verificación independiente: el producto $\prod(x_i^2 - 7) = P(\sqrt7)\,P(-\sqrt7)$ con $P(x) = x^4 - 14x^2 + 9x + 4$ da $(-45 + 9\sqrt7)(-45 - 9\sqrt7) = 2025 - 567 = 1458$. ✓

$$\boxed{1458}$$