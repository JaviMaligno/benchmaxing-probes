## Planteamiento

Una cuadrícula de 3 filas × n columnas de puntos tiene una altura disponible de 2 unidades (entre la primera y la última fila). Todo cuadrado con vértices en puntos de una retícula tiene vectores laterales $(a, b)$ y $(-b, a)$, y su rectángulo envolvente mide $(a+b) \times (a+b)$. Como la altura solo permite $a + b \le 2$, las únicas posibilidades son:

**Tamaño 1 (lado 1, alineado):** $(a,b) = (1,0)$.
- Hay $(3-1)(n-1) = 2(n-1)$ cuadrados unitarios.

**Tamaño 2 (lado 2, alineado):** $(a,b) = (2,0)$.
- Ocupa exactamente las 3 filas, con $n-2$ posiciones horizontales.

**Tamaño √2 (inclinado 45°):** $(a,b) = (1,1)$.
- Cada uno ocupa una caja de $2\times 2$ unidades (3 filas × 3 columnas de puntos); la posición vertical es única y hay $n-2$ posiciones horizontales, con exactamente 1 rombo por caja: son $n-2$.

## Verificación con casos pequeños

Para $n=3$ (retícula 3×3): $2\cdot2 + 1 + 1 = 6$ cuadrados. Comprobación manual: 4 unitarios, 1 de lado 2 (el borde), y el rombo central — total 6. ✓

Para $n=4$: $6 + 2 + 2 = 10$. ✓

## Ecuación

$$2(n-1) + (n-2) + (n-2) = 86$$
$$2n - 2 + 2n - 4 = 86 \implies 4n - 6 = 86 \implies 4n = 92$$

Comprobación con $n = 23$: $44 + 21 + 21 = 86$, y los tamaños son exactamente tres ($1$, $2$, $\sqrt{2}$). ✓

$$\boxed{23}$$