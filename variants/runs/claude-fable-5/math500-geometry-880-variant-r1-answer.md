## Planteamiento

Coloco coordenadas: la habitación mide 15 (largo, eje $x$), 12 (ancho, eje $y$) y 9 (alto, eje $z$).

- **Araña**: en la pared lateral $x=0$, a 1 pie del techo y 1 pie de la pared trasera ($y=0$): punto $(0,\,1,\,8)$.
- **Polilla**: en la pared lateral $x=15$, a 1 pie del piso y 1 pie de la pared frontal ($y=12$): punto $(15,\,11,\,1)$.

El camino más corto sobre superficies se encuentra **desplegando** las caras en un plano y midiendo la línea recta. Hay que probar varias secuencias de caras (sin usar el piso).

## Candidatos principales

**1) Pared lateral → techo → pared lateral opuesta:**
Desplegando sobre el plano del techo: araña en $(-1,\,1)$, polilla en $(23,\,11)$.
$$\sqrt{24^2+10^2}=\sqrt{676}=26$$

**2) Pared lateral → pared trasera (o frontal) → pared lateral opuesta:**
$$\sqrt{27^2+7^2}=\sqrt{778}\approx 27.9$$

**3) Pared lateral → techo → pared frontal → pared lateral opuesta:**
Despliego el techo ($x\in[0,15],\ y\in[0,12]$), la pared de la araña sobre el borde $x=0$, la pared frontal sobre el borde $y=12$, y la pared de la polilla sobre el borde $x=15$ de la pared frontal:

- Araña: $(-1,\,1)$
- Polilla: $x = 15 + (12-11) = 16$, $\ y = 12 + (9-1) = 20$, es decir $(16,\,20)$

$$\sqrt{17^2+19^2}=\sqrt{289+361}=\sqrt{650}=5\sqrt{26}\approx 25.5$$

**Verificación de validez**: la recta de $(-1,1)$ a $(16,20)$ cruza $x=0$ en $y\approx 2.1$ (entra al techo ✓), cruza $y=12$ en $x\approx 8.8$ (entra a la pared frontal ✓) y cruza $x=15$ en $y\approx 18.9$ (entra a la pared de la polilla ✓). El camino es geométricamente válido.

Otras secuencias (pasando por la pared trasera y el techo, o rodeando por atrás) dan $\sqrt{720}=12\sqrt5\approx26.8$, $\sqrt{810}=9\sqrt{10}\approx28.5$, etc., todas mayores.

## Conclusión

El camino más corto cruza cuatro caras (pared lateral, techo, pared frontal y pared lateral opuesta) y mide

$$\boxed{5\sqrt{26}}$$