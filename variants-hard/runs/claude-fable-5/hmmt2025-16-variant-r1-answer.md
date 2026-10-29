## Planteamiento

En una cuadrícula de $6 \times 6$ hay 7 líneas verticales y 7 horizontales (coordenadas $0$ a $6$). Un rectángulo queda determinado por un intervalo en $x$ y otro en $y$, cada uno elegido entre $\binom{7}{2} = 21$ posibles, dando $21^2 = 441$ rectángulos.

## Condición de disyunción

Dos rectángulos (como conjuntos cerrados, incluyendo bordes y vértices) no comparten ningún punto si y solo si **sus intervalos en $x$ son disjuntos o sus intervalos en $y$ son disjuntos**.

**Pares ordenados de intervalos disjuntos en un eje:** dos intervalos cerrados disjuntos requieren 4 extremos distintos $a < b < c < d$; se eligen de $\binom{7}{4} = 35$ formas, y hay 2 maneras de asignar cuál intervalo va primero:
$$D = 2 \cdot 35 = 70.$$

## Conteo por inclusión-exclusión (pares ordenados)

- **Disjuntos en $x$** (los intervalos en $y$ son libres): $70 \cdot 21 \cdot 21 = 30870$.
- **Disjuntos en $y$:** por simetría, $30870$.
- **Disjuntos en ambos ejes:** $70 \cdot 70 = 4900$.

$$30870 + 30870 - 4900 = 56840 \text{ pares ordenados}.$$

## Pares no ordenados

Como dos rectángulos disjuntos nunca son iguales, divido entre 2:
$$\frac{56840}{2} = 28420.$$

(Verificación: el mismo método en una cuadrícula $5\times 5$ da $6300$, el resultado conocido de ese problema clásico.)

$$\boxed{28420}$$