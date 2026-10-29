## Planteamiento

Ubico la habitación con coordenadas: la dirección de 15′ en $x$, la de 12′ en $y$, y la altura en $z$. Según el enunciado, las paredes laterales son de $12\times 9$, así que la araña está en $x=0$ y la polilla en $x=15$:

- **Araña:** $(0,\,1,\,8)$ — a 1′ del techo y 1′ de la trasera.
- **Polilla:** $(15,\,11,\,1)$ — a 1′ del suelo y 1′ de la frontal.

El suelo no se puede usar, así que comparo los despliegues de las rutas viables (techo + paredes).

**Ruta por el techo (S→C→R):** Despliego la pared de la araña, el techo y la pared de la polilla como tira continua. La araña queda a 8 sobre el borde inferior; la polilla queda a $8$ (subida a la arista) $+15$ (techo) $+8$ (bajada) en la otra dirección, con desfase horizontal $11-1=10$:

$$\sqrt{10^2+24^2}=\sqrt{676}=26$$

**Otras rutas de verificación:**

| Ruta | Longitud |
|---|---|
| S→C→R (techo) | $\mathbf{26}$ |
| S→L₁→C→R | $\sqrt{720}\approx 26.8$ |
| S→C→L₁→R | $\sqrt{810}\approx 28.5$ |
| S→L₁→R / S→L₂→R (solo paredes) | $\sqrt{778}\approx 27.9$ |
| S→C→L₂→R | $\sqrt{1090}\approx 33.0$ |

La ruta por el techo es la más corta: sube 1′, cruza el techo en diagonal y baja 8′ por la pared opuesta.

## Respuesta

$$\boxed{26}$$