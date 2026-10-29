## Solución

**Clasificación de posiciones en el cubo 3×3×3** según cuántas caras del cubo grande toca cada cubito:

- **Esquinas** (8): muestran 3 caras, una de cada par de caras opuestas.
- **Aristas** (12): muestran 2 caras adyacentes. Cada arista corresponde biunívocamente a un par de caras adyacentes.
- **Centros de cara** (6): muestran 1 cara.
- **Centro** (1): muestra 0 caras.

Si $F_1, F_2$ son los conjuntos de caras grandes donde cada cubito rojo es visible, necesitamos $|F_1 \cup F_2| = 4$. Como $|F_i| \le 3$, los casos posibles son:

**Caso 1: esquina + centro de cara, sin solapamiento** ($3+1-0=4$).
La esquina cubre 3 caras; el centro de cara debe estar en una de las otras 3 caras: $8 \times 3 = 24$.

**Caso 2: esquina + arista, solapamiento exactamente 1** ($3+2-1=4$).
Para una esquina con caras $\{x,y,z\}$ (una por eje), la arista usa 2 ejes: se eligen los 2 ejes ($3$ formas) y cuál de las dos caras coincide con la de la esquina ($2$ formas), es decir, 6 aristas por esquina: $8 \times 6 = 48$.

**Caso 3: esquina + esquina, solapamiento exactamente 2** ($3+3-2=4$).
Dos esquinas comparten exactamente 2 caras si y solo si son adyacentes (unidas por una arista del cubo grande): hay $12$ pares.

**Caso 4: arista + arista, conjuntos de caras disjuntos** ($2+2-0=4$).
Fijada una arista con caras $\{a,b\}$: las aristas que contienen $a$ son 4, las que contienen $b$ son 4, y la que contiene ambas es la propia arista. Por inclusión-exclusión, $4+4-1=7$ aristas comparten alguna cara, dejando $12-7=5$ disjuntas. Pares no ordenados: $\frac{12 \times 5}{2} = 30$.

Cualquier otra combinación (centro, dos centros de cara, arista + centro de cara, etc.) da una unión de tamaño a lo más 3, o bien solapamientos distintos dan uniones de 3 o 5 (imposible, pues el máximo es 3 por cubito... en efecto, la unión nunca excede 6 pero las combinaciones restantes no suman 4).

**Total:** $24 + 48 + 12 + 30 = 114$.

$$\boxed{114}$$