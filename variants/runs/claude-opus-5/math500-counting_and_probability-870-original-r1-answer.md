## Razonamiento

**Paso 1.** Los cuatro puntos son, con probabilidad 1, distintos. Fijémonos en el conjunto de las cuatro posiciones sobre la circunferencia y recorrámoslas en sentido horario: llamemos $P_1, P_2, P_3, P_4$ a los puntos en ese orden cíclico.

**Paso 2.** Dados esos cuatro puntos, hay exactamente $3$ maneras de emparejarlos en dos cuerdas:

- $\{P_1P_2\}$ y $\{P_3P_4\}$ → no se cruzan
- $\{P_1P_4\}$ y $\{P_2P_3\}$ → no se cruzan
- $\{P_1P_3\}$ y $\{P_2P_4\}$ → **sí se cruzan** (son las dos "diagonales" del cuadrilátero)

Dos cuerdas se cortan si y solo si sus extremos se alternan en el orden cíclico, lo que ocurre únicamente en el tercer emparejamiento.

**Paso 3.** Como las etiquetas $A, B, C, D$ se asignan independientemente y de forma intercambiable, cada uno de los $3$ emparejamientos posibles (es decir, que el par $\{A,B\}$ corresponda a una u otra de las tres divisiones) es igualmente probable.

**Paso 4.** Por tanto la probabilidad de que $AB$ y $CD$ se corten es $\dfrac{1}{3}$.

$$\boxed{\dfrac{1}{3}}$$