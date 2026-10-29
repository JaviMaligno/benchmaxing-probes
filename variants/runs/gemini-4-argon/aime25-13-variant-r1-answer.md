Para hallar el número esperado de regiones en las que los $18$ segmentos de recta dividen el disco, podemos utilizar la relación entre el número de regiones, el número de cuerdas y el número de puntos de intersección en el interior del disco.

### 1. Fórmula para el número de regiones
Con probabilidad $1$, ningún par de cuerdas comparte un extremo en la circunferencia y nunca concurren tres o más segmentos en un mismo punto interior (en particular, ninguna de las $16$ cuerdas aleatorias pasa por el centro del disco). 

Comenzando con $1$ región (el disco entero), cada vez que se traza un segmento que interseca a $k$ de los segmentos previos en el interior del disco, dicho segmento queda dividido en $k + 1$ partes, cada una de las cuales divide una región existente en dos, añadiendo así $1 + k$ nuevas regiones. Al sumar sobre los $18$ segmentos (los $2$ diámetros y las $16$ cuerdas aleatorias), el número total de regiones $R$ cumple:
$$R = 1 + 18 + I = 19 + I$$
donde $I$ es el número total de puntos de intersección interiores entre pares de segmentos. Por linealidad de la esperanza:
$$\mathbb{E}[R] = 19 + \mathbb{E}[I]$$

Podemos descomponer $I$ en tres tipos de intersecciones:
1. $I_{dd}$: intersecciones entre los $2$ diámetros.
2. $I_{dc}$: intersecciones entre los $2$ diámetros y las $16$ cuerdas aleatorias.
3. $I_{cc}$: intersecciones entre pares de las $16$ cuerdas aleatorias.

---

### 2. Intersecciones entre los diámetros ($I_{dd}$)
Los dos diámetros perpendiculares se cortan únicamente en el centro del disco, por lo que:
$$I_{dd} = 1$$

---

### 3. Intersecciones entre diámetros y cuerdas aleatorias ($I_{dc}$)
Numeremos los cuatro cuadrantes en sentido antihorario como $Q_1, Q_2, Q_3, Q_4$. Cada cuerda aleatoria se forma eligiendo dos puntos uniformemente al azar en cuadrantes distintos. Como los cuatro cuadrantes tienen igual longitud de arco, los $\binom{4}{2} = 6$ pares posibles de cuadrantes distintos son equiprobables:
- **$4$ pares de cuadrantes adyacentes**: $\{Q_1, Q_2\}, \{Q_2, Q_3\}, \{Q_3, Q_4\}, \{Q_4, Q_1\}$ (probabilidad $\frac{4}{6} = \frac{2}{3}$). Una cuerda con extremos en cuadrantes adyacentes cruza únicamente el diámetro que los separa ($1$ intersección).
- **$2$ pares de cuadrantes opuestos**: $\{Q_1, Q_3\}, \{Q_2, Q_4\}$ (probabilidad $\frac{2}{6} = \frac{1}{3}$). Para ir de un cuadrante al cuadrante opuesto sin pasar por el origen (lo cual ocurre con probabilidad $1$), el segmento de recta debe cambiar el signo de ambas coordenadas cartesianas en puntos distintos, por lo que necesariamente cruza **ambos** diámetros ($2$ intersecciones).

Por tanto, el número esperado de diámetros que corta una cuerda aleatoria es:
$$\frac{2}{3}(1) + \frac{1}{3}(2) = \frac{4}{3}$$
Para las $16$ cuerdas aleatorias, por linealidad de la esperanza:
$$\mathbb{E}[I_{dc}] = 16 \times \frac{4}{3} = \frac{64}{3}$$

---

### 4. Intersecciones entre pares de cuerdas aleatorias ($I_{cc}$)
Consideremos dos cuerdas aleatorias independientes $C_1$ y $C_2$, cuyos extremos caen en los pares de cuadrantes $P_1$ y $P_2$, respectivamente. Hay $6 \times 6 = 36$ pares ordenados $(P_1, P_2)$ igualmente probables. Dos cuerdas se cortan si y solo si sus cuatro extremos se alternan a lo largo de la circunferencia. Dado que la posición de un extremo dentro de su cuadrante es uniforme e independiente, dos extremos que caen en el mismo cuadrante tienen probabilidad $\frac{1}{2}$ de aparecer en cualquiera de los dos órdenes posibles:

- **Si $|P_1 \cap P_2| = 2$** ($P_1 = P_2$, hay $6$ casos): ambas cuerdas tienen extremos en los mismos dos cuadrantes. Se alternan en la circunferencia si el orden relativo de los dos puntos en el primer cuadrante coincide con el orden relativo en el segundo cuadrante, lo cual ocurre con probabilidad $\frac{1}{2}$.
- **Si $|P_1 \cap P_2| = 1$** ($P_1$ y $P_2$ comparten exactamente un cuadrante, hay $6 \times 4 = 24$ casos): de los dos órdenes posibles para los dos extremos dentro del cuadrante compartido, exactamente uno hace que los extremos de $C_1$ y $C_2$ se alternen en la circunferencia. Por tanto, se cortan con probabilidad $\frac{1}{2}$.
- **Si $|P_1 \cap P_2| = 0$** ($P_1$ y $P_2$ son disjuntos, hay $6$ casos):
  - Si $P_1$ es un par de cuadrantes adyacentes y $P_2$ es el par adyacente complementario ($4$ casos, p. ej., $\{Q_1, Q_2\}$ y $\{Q_3, Q_4\}$), los extremos nunca se alternan, por lo que se cortan con probabilidad $0$.
  - Si $P_1$ es un par de cuadrantes opuestos y $P_2$ es el otro par opuesto ($2$ casos, $\{Q_1, Q_3\}$ y $\{Q_2, Q_4\}$), los extremos siempre se alternan, por lo que se cortan con probabilidad $1$.

La probabilidad $p$ de que dos cuerdas aleatorias se corten es entonces:
$$p = \frac{6 \times \frac{1}{2} + 24 \times \frac{1}{2} + 4 \times 0 + 2 \times 1}{36} = \frac{3 + 12 + 0 + 2}{36} = \frac{17}{36}$$

Como hay $\binom{16}{2} = 120$ pares de cuerdas aleatorias:
$$\mathbb{E}[I_{cc}] = 120 \times \frac{17}{36} = \frac{170}{3}$$

---

### 5. Cálculo final
Sumando todas las contribuciones:
$$\mathbb{E}[R] = 19 + 1 + \frac{64}{3} + \frac{170}{3} = 20 + \frac{234}{3} = 20 + 78 = 98$$

\boxed{98}