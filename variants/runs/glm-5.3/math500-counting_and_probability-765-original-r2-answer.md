## Razonamiento paso a paso

**Paso 1: Identificar la región ocupada.**

De los 360 estudiantes, 15 no toman ninguna de las tres materias, así que quienes toman al menos una:

$$|C \cup P \cup Q| = 360 - 15 = 345$$

(donde C = cálculo, P = física, Q = química)

**Paso 2: Aplicar inclusión-exclusión.**

$$|C \cup P \cup Q| = |C| + |P| + |Q| - |C \cap P| - |C \cap Q| - |P \cap Q| + |C \cap P \cap Q|$$

Sustituyendo los datos (con |Q| = 2|P|):

$$345 = 180 + |P| + 2|P| - 30 - 75 - 75 + 15$$

**Paso 3: Despejar.**

$$345 = 180 + 3|P| - 165$$
$$345 = 15 + 3|P|$$
$$3|P| = 330 \implies |P| = 110$$

**Paso 4: Verificar.**

Con |P| = 110 y |Q| = 220:
- Suma individual: 180 + 110 + 220 = 510
- Menos intersecciones dobles: 510 − (30 + 75 + 75) = 330
- Más triple: 330 + 15 = 345 ✓

Regiones en diagrama de Venn (todas no negativas): solo física = 110 − 30 − 75 + 15 = 20; solo química = 220 − 75 − 75 + 15 = 85; solo cálculo = 180 − 30 − 75 + 15 = 90. Total: 90 + 15 + 60 + 20 + 60 + 85 + 15 + 15 = 360 ✓

$$\boxed{110}$$