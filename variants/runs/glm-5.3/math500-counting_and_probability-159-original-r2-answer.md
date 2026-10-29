## Razonamiento paso a paso

**Planteamiento:** Hay 11 personas en total: 5 Demócratas (D), 5 Republicanos (R) y 1 Independiente (I). La condición es que los miembros de cada partido formen un bloque contiguo alrededor de la mesa.

**Paso 1: Tratar cada partido como un bloque.**
Como los miembros de cada partido deben sentarse juntos, podemos pensar en 3 bloques:
- Bloque D (5 personas)
- Bloque R (5 personas)
- Bloque I (1 persona)

**Paso 2: Contar los arreglos de los bloques.**
Los arreglos circulares de 3 objetos, donde las rotaciones son equivalentes, son:
$$(3-1)! = 2$$
(Los dos órdenes cíclicos son D-R-I y D-I-R; las reflexiones cuentan como diferentes porque el problema solo identifica rotaciones.)

**Paso 3: Contar los arreglos internos.**
Dentro de cada bloque, las personas se ordenan linealmente a lo largo del arco que ocupa:
- Demócratas: $5! = 120$
- Republicanos: $5! = 120$
- Independiente: $1! = 1$

**Paso 4: Multiplicar.**
$$2 \times 5! \times 5! \times 1 = 2 \times 120 \times 120 = 28\,800$$

**Verificación (método alternativo):** Fijamos al Independiente en un asiento para eliminar la simetría rotacional. Los otros 10 asientos forman un camino lineal. Los 5 Demócratas deben ocupar 5 posiciones consecutivas y los 5 Republicanos las otras 5 consecutivas: solo hay 2 divisiones posibles (D en los primeros 5 y R en los últimos 5, o viceversa). Esto da $2 \times 5! \times 5! = 28\,800$, confirmando el resultado. ✓

$\boxed{28800}$