## Resolución

**Configuración.** El grid de 2×2 tiene 12 aristas: 4 aristas interiores (que forman una cruz "+" alrededor del centro, llamémoslas N, E, S, O) y 8 aristas de borde. Cada cuadrado tiene 2 aristas interiores (dos brazos adyacentes de la cruz) y 2 aristas de borde (propias, no compartidas).

**Observación clave.** Una arista interior roja cuenta como el lado rojo de **los dos** cuadrados que la comparten. Como cada cuadrado debe tener exactamente 1 lado rojo, dos brazos adyacentes de la cruz (por ejemplo N y E, que comparten el cuadrado noreste) no pueden ser rojos a la vez. Es decir, el conjunto de aristas interiores rojas debe ser un conjunto independiente en el ciclo N–E–S–O. Las posibilidades son:

- ∅ (ninguna interior roja)
- {N}, {E}, {S}, {O}
- {N,S}, {E,O}

**Conteo por casos.**

- **Caso ∅:** las 4 aristas interiores son azules. Cada cuadrado debe tomar su único lado rojo entre sus 2 aristas de borde: $2^4 = 16$ coloraciones.

- **Caso un brazo rojo (p. ej. {N}):** el brazo N cubre a los cuadrados NE y NO, cuyos demás lados deben ser azules (sin elecciones). Los cuadrados SE y SO eligen cada uno su lado rojo entre sus 2 aristas de borde: $2 \times 2 = 4$. Con 4 brazos posibles: $4 \times 4 = 16$.

- **Caso dos brazos opuestos ({N,S} o {E,O}):** los dos brazos cubren a los 4 cuadrados, así que todas las demás aristas son azules: 1 coloración cada uno, total $2$.

**Total:** $16 + 16 + 2 = 34$.

$$\boxed{34}$$