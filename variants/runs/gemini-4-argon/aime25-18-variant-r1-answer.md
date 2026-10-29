Para encontrar el número de coloraciones válidas, podemos dividir los $12$ segmentos unitarios de la cuadrícula de $2 \times 2$ en dos grupos:
- **$4$ segmentos interiores**, cada uno compartido por dos cuadrados unitarios adyacentes.
- **$8$ segmentos exteriores**, de los cuales corresponden exactamente $2$ a cada uno de los cuatro cuadrados unitarios.

Observemos que si un segmento interior se pinta de rojo, este aporta un lado rojo a los dos cuadrados que lo comparten. Como cada cuadrado unitario debe tener **exactamente $1$ lado rojo**, un cuadrado no puede tener dos segmentos interiores rojos a la vez. Si numeramos los cuadrados cíclicamente como $S_1, S_2, S_3, S_4$, los $4$ segmentos interiores forman un ciclo de longitud $4$ en el cual no puede haber dos segmentos rojos que compartan un mismo cuadrado.

Analicemos los casos según la cantidad $k$ de segmentos interiores pintados de rojo:

1. **Caso $k = 0$ (ningún segmento interior es rojo):**
   Los $4$ segmentos interiores son azules. Por lo tanto, cada uno de los $4$ cuadrados unitarios debe tener su único lado rojo en uno de sus $2$ segmentos exteriores. Como los segmentos exteriores de distintos cuadrados son independientes, hay $2$ opciones para cada cuadrado:
   $$2 \times 2 \times 2 \times 2 = 16 \text{ formas.}$$

2. **Caso $k = 1$ (exactamente $1$ segmento interior es rojo):**
   Hay $4$ maneras de elegir cuál de los $4$ segmentos interiores es rojo. Ese segmento ya le proporciona su único lado rojo a los $2$ cuadrados que lo comparten, por lo que los segmentos exteriores de esos $2$ cuadrados deben ser todos azules ($1$ sola opción para cada uno). Los otros $2$ cuadrados no tienen lados interiores rojos, así que cada uno tiene $2$ opciones para elegir cuál de sus $2$ segmentos exteriores será rojo:
   $$4 \times (1 \times 1 \times 2 \times 2) = 16 \text{ formas.}$$

3. **Caso $k = 2$ (exactamente $2$ segmentos interiores son rojos):**
   Para que ningún cuadrado tenga dos lados interiores rojos, los $2$ segmentos interiores rojos deben ser opuestos entre sí (por ejemplo, los dos horizontales interiores o los dos verticales interiores). Hay $2$ maneras de elegir este par de segmentos. En ambos casos, cada uno de los $4$ cuadrados ya cuenta con $1$ lado interior rojo, lo que obliga a que los $8$ segmentos exteriores sean todos azules ($1$ sola opción):
   $$2 \times 1 = 2 \text{ formas.}$$

4. **Caso $k \ge 3$:**
   Es imposible pintar $3$ o $4$ segmentos interiores de rojo sin que al menos un cuadrado tenga dos lados interiores rojos.

Sumando las posibilidades de todos los casos válidos, obtenemos el total de coloraciones:
$$16 + 16 + 2 = 34$$

\boxed{34}