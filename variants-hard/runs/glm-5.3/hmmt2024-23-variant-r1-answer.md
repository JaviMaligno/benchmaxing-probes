# Planteamiento

Sea $O$ el centro de $\Gamma$ (radio $203$) y $P$ el centro de $\gamma$ (radio $101$). Como $O$ está sobre $\gamma$, se cumple $OP = 101$. Además, $OP + 101 = 202 < 203$, así que $\gamma$ está estrictamente dentro de $\Gamma$.

## Configuración sobre la cuerda

Sea $AB$ la cuerda de $\Gamma$, cortada por $\gamma$ en $C$ y $D$. Pongamos coordenadas a lo largo de la cuerda:
$$AC = k,\quad CD = 2k,\quad DB = 3k \implies AB = 6k,$$
es decir, $A=0$, $C=k$, $D=3k$, $B=6k$ sobre el eje de la cuerda.

**Proyección de $P$:** el centro de $\gamma$ se proyecta en el punto medio de $CD$ (posición $2k$); a distancia perpendicular $s$:
$$P = (2k,\, s), \qquad k^2 + s^2 = 101^2. \tag{1}$$

**Proyección de $O$:** el centro de $\Gamma$ se proyecta en el punto medio de $AB$ (posición $3k$); a distancia perpendicular con signo $h$:
$$O = (3k,\, h), \qquad 9k^2 + h^2 = 203^2. \tag{2}$$

**Condición $OP = 101$:** el vector $O - P = (k,\ h - s)$, de modo que
$$k^2 + (h-s)^2 = 101^2. \tag{3}$$

## Resolución

De (1) y (3): $(h-s)^2 = s^2$, es decir, $h = 0$ o $h = 2s$.

**Caso $h = 0$:** la recta pasa por $O$, así que la cuerda es un **diámetro** de $\Gamma$ ($AB = 406$). El problema lo excluye.

**Caso $h = 2s$:** sustituyendo en (2) y usando (1):
$$9k^2 + 4s^2 = 203^2, \qquad s^2 = 101^2 - k^2.$$
Entonces:
$$9k^2 + 4(101^2 - k^2) = 203^2 \implies 5k^2 = 203^2 - 4\cdot 101^2 = 41209 - 40804 = 405$$
$$k^2 = 81 \implies k = 9.$$

## Verificación

- $s = \sqrt{10201 - 81} = \sqrt{10120} \approx 100{,}6 < 101$ ✓ (la cuerda corta a $\gamma$)
- $h = 2s = \sqrt{40480} \approx 201{,}2 < 203$ ✓ (la recta corta a $\Gamma$)
- Segmentos: $9$, $18$, $27$, que están en razón $1:2:3$ ✓
- Coordenadas explícitas: con $P=(0,0)$, $O=(101,0)$, la recta $sx + 9y + 101s = 0$ con $s=\sqrt{10120}$ reproduce exactamente esta configuración.

La longitud de la cuerda es $AB = 6k = 54$.

$$\boxed{54}$$