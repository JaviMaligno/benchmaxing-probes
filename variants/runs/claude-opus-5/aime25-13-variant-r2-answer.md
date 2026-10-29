## Planteamiento

Para cuerdas en posición general dentro de un disco, el número de regiones es

$$R = 1 + L + I,$$

donde $L=18$ es el número de segmentos e $I$ el número de puntos de intersección interiores. Por linealidad, basta calcular $E[I]$.

## Pares de diámetros

Los dos diámetros se cortan en el centro: aporta $1$.

## Diámetro × segmento aleatorio

Un diámetro separa el disco en dos mitades formadas por dos cuadrantes adyacentes (p. ej. $\{Q_1,Q_2\}$ vs $\{Q_3,Q_4\}$). Un segmento aleatorio elige un par no ordenado de cuadrantes distintos, cada uno con probabilidad $1/6$. De los $6$ pares, los que tienen sus extremos en mitades opuestas son $\{1,3\},\{1,4\},\{2,3\},\{2,4\}$: son $4$, luego la probabilidad de cruce es $\tfrac{4}{6}=\tfrac{2}{3}$.

Hay $2\cdot 16=32$ pares:
$$32\cdot\frac23=\frac{64}{3}.$$

## Segmento aleatorio × segmento aleatorio

Dos cuerdas se cortan si sus extremos se alternan en el círculo. Clasifico los $36$ casos igualmente probables de pares de cuadrantes $(A,B)$:

- **Mismo par** ($6$ casos): ambos extremos recorren los mismos dos arcos disjuntos; se cortan si el orden relativo coincide en ambos arcos → probabilidad $\tfrac12$.
- **Pares disjuntos complementarios adyacentes** ($\{1,2\}$ vs $\{3,4\}$ y $\{2,3\}$ vs $\{4,1\}$, $4$ casos ordenados): los extremos ocupan arcos contiguos separados, nunca se alternan → probabilidad $0$.
- **Pares opuestos** ($\{1,3\}$ vs $\{2,4\}$, $2$ casos ordenados): el orden es siempre $Q_1,Q_2,Q_3,Q_4$ alternando → probabilidad $1$.
- **Comparten exactamente un cuadrante** ($24$ casos): tomando el cuadrante común como $[0,1)$, el extremo ajeno a la otra cuerda está fijo dentro o fuera del arco $(p,q)$, y la condición se reduce a comparar los dos puntos uniformes del cuadrante común → probabilidad $\tfrac12$.

$$P(\text{corte})=\frac{1}{36}\left[6\cdot\tfrac12+4\cdot 0+2\cdot 1+24\cdot\tfrac12\right]=\frac{3+0+2+12}{36}=\frac{17}{36}.$$

Con $\binom{16}{2}=120$ pares:
$$120\cdot\frac{17}{36}=\frac{170}{3}.$$

## Total

$$E[I]=1+\frac{64}{3}+\frac{170}{3}=1+78=79,$$

$$E[R]=1+18+79=98.$$

\boxed{98}