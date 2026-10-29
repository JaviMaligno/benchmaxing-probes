## Planteamiento

Coloco el cuadrado en coordenadas: $A=(0,0)$, $B=(s,0)$, $C=(s,s)$, con lado $s$. Sea $M=\left(\tfrac{s}{2},0\right)$ el punto medio de $AB$.

**Observación clave:** como $M$ es punto medio de $AB$, los puntos $A$ y $B$ equidistan de $\ell$:
$$d(A,\ell) = d(B,\ell) = 4.$$

## Cálculo con la pendiente

Sea $\ell$ la recta por $M$ con pendiente $m$ (con $0\le m\le 2$ para que corte al segmento $BC$):
$$\ell:\; mx - y - \tfrac{ms}{2} = 0.$$

**Distancia de $A=(0,0)$:**
$$\frac{\tfrac{ms}{2}}{\sqrt{m^2+1}} = 4. \tag{1}$$

**Distancia de $C=(s,s)$:** el valor absoluto del numerador es $\left|\tfrac{ms}{2} - s\right| = s\left(1-\tfrac{m}{2}\right)$ (pues $m<2$):
$$\frac{s\left(1-\tfrac{m}{2}\right)}{\sqrt{m^2+1}} = \frac{s(2-m)}{2\sqrt{m^2+1}} = 7. \tag{2}$$

Dividiendo $(2)$ entre $(1)$:
$$\frac{2-m}{m} = \frac{7}{4} \quad\Longrightarrow\quad 8-4m = 7m \quad\Longrightarrow\quad m = \frac{8}{11}.$$

Sustituyendo en $(1)$, con $\sqrt{m^2+1} = \sqrt{\tfrac{185}{121}} = \tfrac{\sqrt{185}}{11}$:
$$\frac{\tfrac{8}{11}\cdot s}{2\cdot \tfrac{\sqrt{185}}{11}} = 4 \quad\Longrightarrow\quad \frac{4s}{\sqrt{185}} = 4 \quad\Longrightarrow\quad s = \sqrt{185}.$$

## Comprobación con áreas

Como $B$ y $C$ están en lados opuestos de $\ell$, si $E = \ell \cap BC$, por semejanza:
$$\frac{BE}{EC} = \frac{d(B,\ell)}{d(C,\ell)} = \frac{4}{7} \quad\Longrightarrow\quad BE = \tfrac{4s}{11},\; MB = \tfrac{s}{2}.$$

El área del triángulo rectángulo $MBE$ es $\tfrac{1}{2}\cdot \tfrac{s}{2}\cdot \tfrac{4s}{11} = \tfrac{s^2}{11}$, y también $\tfrac{1}{2}\cdot ME \cdot 4 = 2ME = \tfrac{s\sqrt{185}}{11}$. De ahí $s^2 = s\sqrt{185}$, o sea $s = \sqrt{185}$ ✓.

Por lo tanto, el área del cuadrado es $s^2 = 185$.

$$\boxed{185}$$