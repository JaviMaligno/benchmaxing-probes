## Planteamiento

Para cuerdas en un disco en posición general, cada cuerda nueva añade $1 + (\text{número de intersecciones con cuerdas anteriores})$ regiones. Por lo tanto:

$$\text{Regiones} = 1 + L + P,$$

donde $L = 18$ es el número de segmentos y $P$ es el número de puntos de intersección interiores. Por linealidad de la esperanza, basta calcular $E[P]$.

## Intersecciones esperadas

**1. Diámetro con diámetro:** los dos diámetros se cruzan en el centro: $1$ intersección.

**2. Segmento aleatorio con los diámetros:** los dos extremos caen en cuadrantes distintos. De los 6 pares de cuadrantes posibles (todos equiprobables), 4 son adyacentes (el segmento cruza 1 diámetro) y 2 son opuestos (cruza 2 diámetros). Esperanza por segmento:

$$\tfrac{2}{3}\cdot 1 + \tfrac{1}{3}\cdot 2 = \tfrac{4}{3} \quad\Rightarrow\quad 16\cdot\tfrac{4}{3} = \tfrac{64}{3}.$$

**3. Segmento aleatorio con segmento aleatorio:** condicionando en los pares de cuadrantes de cada cuerda (36 combinaciones equiprobables) y usando que los extremos dentro de cada cuadrante son uniformes:

- Ambas con el mismo par opuesto (2 combos): se cruzan con probabilidad $\tfrac12$.
- Pares opuestos distintos, p. ej. $Q_1Q_3$ y $Q_2Q_4$ (2 combos): se cruzan siempre, probabilidad $1$.
- Una opuesta y una adyacente (16 combos): probabilidad $\tfrac12$.
- Ambas con el mismo par adyacente (4 combos): probabilidad $\tfrac12$.
- Pares adyacentes que comparten un cuadrante (8 combos): probabilidad $\tfrac12$.
- Pares adyacentes disjuntos, p. ej. $Q_1Q_2$ y $Q_3Q_4$ (4 combos): nunca se cruzan, probabilidad $0$.

$$P(\text{cruce}) = \frac{2\cdot\frac12 + 2\cdot 1 + 16\cdot\frac12 + 4\cdot\frac12 + 8\cdot\frac12 + 0}{36} = \frac{17}{36}.$$

Con $\binom{16}{2} = 120$ pares:

$$120\cdot\frac{17}{36} = \frac{170}{3}.$$

## Total

$$E[P] = 1 + \frac{64}{3} + \frac{170}{3} = 1 + \frac{234}{3} = 1 + 78 = 79.$$

$$E[\text{Regiones}] = 1 + 18 + 79 = 98.$$

$$\boxed{98}$$