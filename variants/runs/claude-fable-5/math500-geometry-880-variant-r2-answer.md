## Planteamiento

Coloco coordenadas en la habitación: largo $x\in[0,15]$, ancho $y\in[0,12]$, altura $z\in[0,9]$.

- **Araña**: en la pared lateral $x=0$, a 1 pie del techo y 1 pie de la pared trasera ($y=0$): punto $(0,\,1,\,8)$.
- **Polilla**: en la pared lateral opuesta $x=15$, a 1 pie del suelo y 1 pie de la pared frontal ($y=12$): punto $(15,\,11,\,1)$.

El camino más corto sobre superficies se encuentra desplegando las caras en un plano y midiendo la recta. Como el suelo está prohibido, pruebo los desdoblamientos posibles:

**1) Pared lateral → techo → pared opuesta:**
Recorrido horizontal desplegado: $1 + 15 + 8 = 24$; desplazamiento lateral: $11-1 = 10$.
$$\sqrt{24^2+10^2}=\sqrt{676}=26$$

**2) Pared lateral → pared trasera (o frontal) → pared opuesta:**
Tramo desplegado: $1+15+11=27$; vertical: $8-1=7$.
$$\sqrt{27^2+7^2}=\sqrt{778}\approx 27.9$$

**3) Pared lateral → pared trasera → techo → pared opuesta:**
$$\sqrt{24^2+12^2}=\sqrt{720}=12\sqrt5\approx 26.83$$

**4) Pared lateral → techo → pared frontal → pared opuesta** (tipo Dudeney):
Despliego la pared de la araña con coordenadas $(u,v)=(y,z)$, araña en $(1,8)$. El techo gira sobre $v=9$: puntos $(u,v)=(y,\,9+x)$. La pared frontal gira sobre $u=12$: $(u,v)=(21-z,\,9+x)$. La pared opuesta gira sobre $v=24$: $(u,v)=(21-z,\,24+(12-y))$.

La polilla $(y=11,\,z=1)$ queda en $(20,\,25)$. La distancia a la araña $(1,8)$:
$$\sqrt{(20-1)^2+(25-8)^2}=\sqrt{19^2+17^2}=\sqrt{361+289}=\sqrt{650}=5\sqrt{26}\approx 25.50$$

**Verificación de validez**: la recta de $(1,8)$ a $(20,25)$ cruza $v=9$ en $u\approx 2.1$ (entra al techo ✓), cruza $u=12$ en $v\approx 17.8$ (entra a la pared frontal ✓) y cruza $v=24$ en $u\approx 18.9$ (entra a la pared opuesta ✓). El camino es realizable y no toca el suelo.

Como $5\sqrt{26}\approx 25.50 < 26 < 12\sqrt5 < \sqrt{778}$, este es el mínimo.

$$\boxed{5\sqrt{26}}$$