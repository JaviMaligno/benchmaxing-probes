## Planteamiento

Sea el cuadrado $ABCD$ de lado $s$. La suma de las cuatro áreas es el área total:
$$s^2 = 1+2+3+4 = 10$$

**Observación clave:** los triángulos opuestos cumplen
$$[PAB]+[PCD] = [PBC]+[PDA] = \tfrac{s^2}{2} = 5$$

Por tanto las parejas opuestas deben ser $\{1,4\}$ y $\{2,3\}$.

## Coordenadas

Tomo $A=(0,0)$, $B=(s,0)$, $C=(s,s)$, $D=(0,s)$, con $P=(x,y)$ y $s=\sqrt{10}$:

- $[PAB] = \tfrac{sy}{2} = 1 \Rightarrow y = \tfrac{2}{\sqrt{10}}$
- $[PDA] = \tfrac{sx}{2} = 2 \Rightarrow x = \tfrac{4}{\sqrt{10}}$

(automáticamente $[PCD]=4$ y $[PBC]=3$).

## Distancias

$$x^2=\tfrac{16}{10},\quad y^2=\tfrac{4}{10},\quad (x-s)^2=\tfrac{36}{10},\quad (y-s)^2=\tfrac{64}{10}$$

$$PA^2 = \tfrac{16+4}{10}=2,\qquad PB^2=\tfrac{36+4}{10}=4,$$
$$PC^2=\tfrac{36+64}{10}=10,\qquad PD^2=\tfrac{16+64}{10}=8$$

## Producto

$$(PA\cdot PB\cdot PC\cdot PD)^2 = 2\cdot 4\cdot 10\cdot 8 = 640$$

$$PA\cdot PB\cdot PC\cdot PD = \sqrt{640} = 8\sqrt{10}$$

Las demás asignaciones compatibles dan el mismo producto (solo permutan los valores $2,4,8,10$).

\boxed{8\sqrt{10}}