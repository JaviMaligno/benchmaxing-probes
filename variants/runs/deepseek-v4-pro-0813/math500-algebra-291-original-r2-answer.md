Vamos a definir dos probabilidades:

- $a$: probabilidad de que Alice gane cuando es el turno de Alice.
- $b$: probabilidad de que Alice gane cuando es el turno de Bob.

**Turno de Alice.** Con probabilidad $1/2$ saca cara y gana; con probabilidad $1/2$ saca cruz y pasa el turno a Bob. Por tanto:

$$a = \frac{1}{2}\cdot 1 + \frac{1}{2}\cdot b = \frac{1}{2} + \frac{b}{2}.$$

**Turno de Bob.** Con probabilidad $1/2$ saca cruz y gana Bob (Alice pierde); con probabilidad $1/2$ saca cara y devuelve el turno a Alice. Así:

$$b = \frac{1}{2}\cdot 0 + \frac{1}{2}\cdot a = \frac{a}{2}.$$

Sustituimos $b = a/2$ en la primera ecuación:

$$a = \frac{1}{2} + \frac{1}{2}\cdot \frac{a}{2} = \frac{1}{2} + \frac{a}{4}.$$

Multiplicando por $4$:

$$4a = 2 + a \implies 3a = 2 \implies a = \frac{2}{3}.$$

\boxed{\frac{2}{3}}