## Planteamiento

Coloco el centro $O$ en el origen, con circunradio 1. Los vértices son:
- $P = (0, 1)$
- $Q = (-\tfrac{\sqrt3}{2}, -\tfrac12)$
- $R = (\tfrac{\sqrt3}{2}, -\tfrac12)$

El lado del triángulo es $s = \sqrt3$, así que su área es $\frac{\sqrt3}{4}s^2 = \frac{3\sqrt3}{4}$. Los lados del triángulo son las rectas $y = -\tfrac12$, $\sqrt3 x + y = 1$ y $-\sqrt3 x + y = 1$ (el inradio es $\tfrac12$).

## Región más cercana a $O$

Un punto está más cerca de $O$ que de un vértice $V$ si queda del lado de $O$ respecto de la mediatriz del segmento $OV$. Las tres mediatrices son:

- Mediatriz de $OP$: $\quad y \le \tfrac12$
- Mediatriz de $OR$: $\quad \sqrt3 x - y \le 1$
- Mediatriz de $OQ$: $\quad -\sqrt3 x - y \le 1$

Intersecando estas tres condiciones con el triángulo se obtiene un hexágono con vértices (donde cada mediatriz corta a los lados del triángulo):

$$\left(\pm\tfrac{\sqrt3}{6}, \tfrac12\right),\quad \left(\pm\tfrac{\sqrt3}{3}, 0\right),\quad \left(\pm\tfrac{\sqrt3}{6}, -\tfrac12\right)$$

Por ejemplo, la mediatriz de $OR$ corta el lado $PR$ en $(\tfrac{\sqrt3}{3}, 0)$ y el lado $QR$ en $(\tfrac{\sqrt3}{6}, -\tfrac12)$; se verifica que las mediatrices no se cortan entre sí dentro del triángulo.

## Área del hexágono

Por simetría, la mitad superior ($0 \le y \le \tfrac12$) es un trapecio con base inferior $\tfrac{2\sqrt3}{3}$, base superior $\tfrac{\sqrt3}{3}$ y altura $\tfrac12$:

$$A_{\text{mitad}} = \frac{1}{2}\left(\frac{2\sqrt3}{3} + \frac{\sqrt3}{3}\right)\cdot\frac12 = \frac{\sqrt3}{4} \implies A_{\text{hex}} = \frac{\sqrt3}{2}$$

**Verificación:** el complemento son tres triángulos de esquina (por ejemplo, el de $R$ tiene vértices $R$, $(\tfrac{\sqrt3}{3},0)$, $(\tfrac{\sqrt3}{6},-\tfrac12)$, con área $\tfrac{\sqrt3}{12}$ cada uno). Entonces $\frac{3\sqrt3}{4} - 3\cdot\frac{\sqrt3}{12} = \frac{\sqrt3}{2}$ ✓.

## Probabilidad

$$P = \frac{A_{\text{hex}}}{A_{\triangle}} = \frac{\sqrt3/2}{3\sqrt3/4} = \frac{2}{3}$$

$$\boxed{\dfrac{2}{3}}$$