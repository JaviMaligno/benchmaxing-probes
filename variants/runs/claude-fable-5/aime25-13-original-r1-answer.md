## Planteamiento

Uso el hecho de que, en un disco, cada segmento nuevo añade **1 + (número de intersecciones con los segmentos ya dibujados)** regiones. Así:

$$E[\text{regiones}] = 4 + \sum_{i=1}^{25}\Big(1 + E[\text{cruces con diámetros}] + E[\text{cruces con cuerdas previas}]\Big)$$

(los dos diámetros ya dividen el disco en 4 regiones).

## Cruces de una cuerda con los diámetros

Los extremos de cada cuerda caen en dos cuadrantes distintos, y los 6 pares de cuadrantes son equiprobables:
- **Cuadrantes adyacentes** (4 de 6 casos): la cuerda cruza exactamente 1 diámetro.
- **Cuadrantes opuestos** (2 de 6 casos): cruza ambos diámetros.

$$E = \frac{4\cdot 1 + 2\cdot 2}{6} = \frac{4}{3}$$

## Probabilidad de que dos cuerdas se crucen

Dos cuerdas se cruzan si y solo si sus extremos se alternan sobre la circunferencia. Analizando los $6\times 6 = 36$ combos equiprobables de pares de cuadrantes (dentro de un mismo cuadrante, el orden de dos puntos es uniforme):

| Configuración | Casos | P(cruce) |
|---|---|---|
| Ambas opuestas, mismo par | 2 | 1/2 |
| Ambas opuestas, pares distintos | 2 | 1 |
| Una opuesta, otra adyacente | 16 | 1/2 |
| Adyacentes, mismo par | 4 | 1/2 |
| Adyacentes, comparten un cuadrante | 8 | 1/2 |
| Adyacentes, disjuntas | 4 | 0 |

$$p = \frac{2\cdot\frac12 + 2\cdot 1 + 16\cdot\frac12 + 4\cdot\frac12 + 8\cdot\frac12}{36} = \frac{17}{36}$$

## Suma total

- Regiones iniciales: $4$
- Las 25 cuerdas en sí: $+25$
- Cruces con diámetros: $25 \cdot \frac{4}{3} = \frac{100}{3}$
- Cruces entre cuerdas: $\binom{25}{2}\cdot\frac{17}{36} = 300\cdot\frac{17}{36} = \frac{425}{3}$

$$4 + 25 + \frac{100}{3} + \frac{425}{3} = 29 + \frac{525}{3} = 29 + 175 = 204$$

$$\boxed{204}$$