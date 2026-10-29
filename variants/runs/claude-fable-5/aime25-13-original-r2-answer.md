## Planteamiento

Uso la fórmula clásica para regiones en un disco: cada segmento nuevo añade **1 + (número de intersecciones con segmentos previos)** regiones. Así,

$$E[\text{regiones}] = 4 + \sum_{\text{cuerdas}} \left(1 + E[\text{cruces}]\right)$$

donde 4 son las regiones iniciales creadas por los dos diámetros.

## Paso 1: Cruces de cada cuerda con los diámetros

Una cuerda une dos cuadrantes distintos. Fijado el primer punto, el segundo cae con igual probabilidad en cada uno de los otros tres cuadrantes:
- Cuadrantes **adyacentes** (prob. 2/3): cruza 1 diámetro.
- Cuadrantes **opuestos** (prob. 1/3): cruza 2 diámetros.

$$E[\text{cruces con diámetros}] = \tfrac{2}{3}(1) + \tfrac{1}{3}(2) = \tfrac{4}{3}$$

## Paso 2: Probabilidad de cruce entre dos cuerdas aleatorias

Dos cuerdas se cruzan si y solo si sus extremos se alternan en el círculo. Analizo por casos según los pares de cuadrantes (condicionando, los puntos son uniformes dentro de cada cuadrante):

**Ambas opuestas** (prob. $\tfrac{1}{3}\cdot\tfrac{1}{3} = \tfrac19$): si usan el mismo par de cuadrantes (prob. 1/2) se cruzan con prob. 1/2; si usan pares distintos ({1,3} y {2,4}) siempre se alternan y se cruzan. Prob. de cruce: $\tfrac12\cdot\tfrac12 + \tfrac12\cdot 1 = \tfrac34$.

**Una opuesta, una adyacente** (prob. $2\cdot\tfrac13\cdot\tfrac23 = \tfrac49$): la cuerda adyacente comparte exactamente un cuadrante con la opuesta, y el cruce depende de la posición relativa de dos puntos uniformes en ese cuadrante: prob. $\tfrac12$.

**Ambas adyacentes** (prob. $\tfrac23\cdot\tfrac23 = \tfrac49$): dado el par de A, el par de B es uniforme entre los 4 pares adyacentes:
- Mismo par (1/4): se cruzan iff el orden en ambos cuadrantes coincide → prob. 1/2.
- Comparten un cuadrante (1/2): prob. 1/2 (decidido por dos puntos uniformes en el cuadrante común).
- Pares disjuntos (1/4): los extremos quedan en bloque XXYY, nunca se cruzan → prob. 0.

Prob. de cruce: $\tfrac14\cdot\tfrac12 + \tfrac12\cdot\tfrac12 + \tfrac14\cdot 0 = \tfrac38$.

Total:
$$p = \tfrac19\cdot\tfrac34 + \tfrac49\cdot\tfrac12 + \tfrac49\cdot\tfrac38 = \tfrac{3}{36} + \tfrac{8}{36} + \tfrac{6}{36} = \tfrac{17}{36}$$

## Paso 3: Esperanza total

$$E = 4 + 25\left(1 + \tfrac43\right) + \binom{25}{2}\cdot\tfrac{17}{36} = 4 + 25\cdot\tfrac73 + 300\cdot\tfrac{17}{36} = 4 + \tfrac{175}{3} + \tfrac{425}{3} = 4 + 200$$

$$\boxed{204}$$