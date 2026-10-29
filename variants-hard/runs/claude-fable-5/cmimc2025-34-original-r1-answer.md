## Planteamiento

Los puntos $(0,0),(10,0),(10,10),(0,10)$ son los vértices del casco convexo (un cuadrado de área 100), y $P=(3,4)$, $Q=(6,2)$ son interiores. En cualquier polígono simple, los vértices del casco convexo deben aparecer en el mismo orden cíclico que en el casco. Por lo tanto, el hexágono es el cuadrado con "muescas": los puntos interiores se insertan en los huecos entre esquinas consecutivas, y cada muesca **resta** área al cuadrado.

**Áreas de triángulo** (muesca de un solo punto): con base 10 y distancia $d$ al lado, el área es $5d$:

- $P=(3,4)$: abajo 20, derecha 35, arriba 30, izquierda 15.
- $Q=(6,2)$: abajo 10, derecha 20, arriba 40, izquierda 30.

## Área máxima (minimizar lo recortado)

Si ambos puntos van en el mismo hueco inferior con orden $(0,0),(6,2),(3,4),(10,0)$, el cuadrilátero recortado tiene área (shoelace) igual a **11**. Verifico que el hexágono
$$(0,0),(6,2),(3,4),(10,0),(10,10),(0,10)$$
es simple: la única intersección candidata entre $(0,0)\text{–}(6,2)$ y $(3,4)\text{–}(10,0)$ ocurre en $x=\tfrac{120}{19}\approx 6.32$, fuera del primer segmento. El shoelace directo confirma área $89$. Ninguna otra configuración recorta menos de 11, así que $a_{\max}=89$.

## Área mínima (maximizar lo recortado)

Las combinaciones con recorte grande fallan por autointersección:
- $P$ derecha $+$ $Q$ arriba (recorte 75): los segmentos $(10,0)\text{–}(3,4)$ y $(6,2)\text{–}(0,10)$ se cruzan en $(5.625, 2.5)$.
- $P$ derecha $+$ $Q$ izquierda (65), $P$ abajo $+$ $Q$ arriba (60), $P$ arriba $+$ $Q$ izquierda (60): todas tienen cruces análogos (se comprueba resolviendo las intersecciones de rectas; cada una cae dentro de ambos segmentos).

La mejor configuración válida es $P$ en el lado izquierdo (15) y $Q$ en el lado superior (40), recorte total **55**. El hexágono
$$(0,0),(10,0),(10,10),(6,2),(0,10),(3,4)$$
es simple (el único cruce candidato, entre $(6,2)\text{–}(0,10)$ y $(3,4)\text{–}(0,0)$, ocurre en $x=3.75$, fuera del segundo segmento), y el shoelace confirma área $45$. Los recortes de dos puntos en un mismo hueco llegan a lo sumo a 46 (lado superior), que da área 54, peor que 45. Así $a_{\min}=45$.

## Resultado

$$a_{\max}-a_{\min}=89-45=44$$

$$\boxed{44}$$