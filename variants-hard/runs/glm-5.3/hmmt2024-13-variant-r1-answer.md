## Planteamiento

Un cubo de 3×3×3 tiene 27 posiciones, clasificadas según cuántas caras exteriores tocan:

- **8 esquinas**: tocan 3 caras
- **12 centros de arista**: tocan 2 caras
- **6 centros de cara**: tocan 1 cara
- **1 interior**: toca 0 caras

Como las rotaciones y reflexiones se consideran distintas, basta contar conjuntos de 2 posiciones (las 2 cubetas azules) tales que la **unión** de las caras exteriores que tocan tenga exactamente 3 caras.

## Casos por par de posiciones

**Esquina + esquina:** Dos esquinas distintas comparten a lo sumo 2 caras, así que la unión tiene al menos 4 caras. → **0**

**Esquina + centro de arista:** Vale solo si las 2 caras de la arista están entre las 3 caras de la esquina (las 3 aristas que inciden en la esquina):
$$8 \times 3 = 24$$

**Esquina + centro de cara:** El centro de cara debe estar en una de las 3 caras de la esquina:
$$8 \times 3 = 24$$

**Esquina + interior:** La esquina aporta exactamente 3 caras:
$$8 \times 1 = 8$$

**Arista + arista:** La unión de $\{2\text{ caras}\} \cup \{2\text{ caras}\}$ tiene tamaño 3 solo si comparten exactamente 1 cara. Cada cara contiene $\binom{4}{2}=6$ pares de aristas, y $6$ caras dan $36$ pares (dos aristas distintas nunca comparten dos caras, ya que dos caras se cortan en una sola arista):
$$36$$

**Arista + centro de cara:** El centro de cara no debe estar en las 2 caras de la arista:
$$12 \times 4 = 48$$

**Resto de casos** (arista+interior, cara+cara, cara+interior, interior+interior): la unión tiene menos de 3 caras. → **0**

## Total

$$24 + 24 + 8 + 36 + 48 = 140$$

$$\boxed{140}$$