## Planteamiento

Clasifico las 27 posiciones del cubo 3×3×3 según cuántas caras del cubo grande tocan:

- **Esquinas (8):** visibles en 3 caras (un trío de caras mutuamente adyacentes).
- **Aristas (12):** visibles en 2 caras adyacentes.
- **Centros de cara (6):** visibles en 1 cara.
- **Centro (1):** visible en 0 caras.

Coloco 2 cubos azules en posiciones distintas; necesito que la **unión** de los conjuntos de caras visibles de ambos tenga tamaño exactamente 3. Analizo por tipos de posición (a, b) según el número de caras que aporta cada cubo:

**Caso (3, 0): esquina + centro.** La unión son las 3 caras de la esquina. Hay 8 esquinas × 1 centro = **8**.

**Caso (3, 1): esquina + centro de cara.** La cara del centro de cara debe estar entre las 3 caras de la esquina (si no, la unión sería 4). Por esquina hay 3 opciones: 8 × 3 = **24**.

**Caso (3, 2): esquina + arista.** Las 2 caras de la arista deben estar dentro del trío de la esquina. Cada par de caras adyacentes del cubo grande contiene exactamente 1 cubo de arista (el del medio de esa arista grande), y el trío de la esquina da 3 pares: 8 × 3 = **24**.

**Caso (3, 3): dos esquinas.** Dos esquinas distintas nunca tienen el mismo trío de caras; esquinas adyacentes dan unión 4, diagonales de cara dan 5, opuestas dan 6. Aporta **0**.

**Caso (2, 2): dos aristas.** Necesito que sus pares de caras compartan exactamente una cara (2 + 2 − 1 = 3). Para una arista fija con caras {A, B}: cada cara del cubo grande contiene 4 cubos de arista, y el único cubo de arista en A ∩ B es ella misma, así que hay 3 + 3 = 6 aristas compatibles. Pares no ordenados: 12 × 6 / 2 = **36**.

**Caso (2, 1): arista + centro de cara.** La cara del centro de cara debe ser *distinta* de las 2 caras de la arista (si coincide, la unión es 2). Quedan 4 caras posibles: 12 × 4 = **48**.

**Casos restantes** ((2,0), (1,1), (1,0)): la unión tiene a lo sumo 2 caras, aportan **0**.

## Total

$$8 + 24 + 24 + 36 + 48 = 140$$

$$\boxed{140}$$