# Solución paso a paso

## Paso 1: Asignar coordenadas cómodas

Ubiquemos el triángulo en coordenadas: $B = (0,0)$, $C = (2,0)$, $A = (0,2)$.

El área de este triángulo de referencia es:
$$[ABC] = \frac{1}{2}\cdot 2 \cdot 2 = 2$$

## Paso 2: Hallar los puntos clave

**Baricentro** (promedio de vértices):
$$G = \left(\frac{0+2+0}{3}, \frac{2+0+0}{3}\right) = \left(\frac{2}{3}, \frac{2}{3}\right)$$

**Punto $E$** (punto medio de $AC$):
$$E = \left(\frac{0+2}{2}, \frac{2+0}{2}\right) = (1,1)$$

## Paso 3: Hallar $N$

La recta por $G$ paralela a $BC$ (horizontal) es $y = \frac{2}{3}$.

La recta $AC$ va de $(0,2)$ a $(2,0)$, con ecuación $y = 2 - x$. Intersectando:
$$\frac{2}{3} = 2 - x \implies x = \frac{4}{3}$$

Por lo tanto $N = \left(\frac{4}{3}, \frac{2}{3}\right)$.

## Paso 4: Área del triángulo $ENG$

Los puntos son: $E = (1,1)$, $N = \left(\frac{4}{3}, \frac{2}{3}\right)$, $G = \left(\frac{2}{3}, \frac{2}{3}\right)$.

Observemos que $NG$ es horizontal con longitud:
$$NG = \frac{4}{3} - \frac{2}{3} = \frac{2}{3}$$

La altura desde $E$ hasta la recta $y = \frac{2}{3}$ es:
$$h = 1 - \frac{2}{3} = \frac{1}{3}$$

Entonces:
$$[ENG] = \frac{1}{2} \cdot \frac{2}{3} \cdot \frac{1}{3} = \frac{1}{9}$$

## Paso 5: Escalar al área dada

La razón entre las áreas es:
$$\frac{[ENG]}{[ABC]} = \frac{1/9}{2} = \frac{1}{18}$$

Como las áreas escalan con el cuadrado del factor de semejanza, si $[ABC] = 144$:
$$[ENG] = \frac{144}{18} = 8$$

$\boxed{8}$