Para hallar el número esperado de regiones en las que los $18$ segmentos de recta dividen el disco, utilizamos la relación entre el número de regiones $R$, el número de cuerdas (segmentos) $N$ y el número de puntos de intersección interiores $I$ (dado que, con probabilidad $1$, no hay tres segmentos concurrentes en un mismo punto interior):

$$R = 1 + N + I$$

Por linealidad de la esperanza, como hay $N = 2 + 16 = 18$ segmentos en total:
$$\mathbb{E}[R] = 1 + 18 + \mathbb{E}[I] = 19 + \mathbb{E}[I]$$

Desglosamos las intersecciones interiores $I$ en tres categorías:

### 1. Intersección entre los dos diámetros perpendiculares
Los dos diámetros se cortan exactamente en $1$ punto (el centro del disco).

### 2. Intersecciones entre los $16$ segmentos aleatorios y los $2$ diámetros
Como los cuatro cuadrantes tienen la misma longitud de arco, elegir dos puntos al azar en cuadrantes distintos equivale a elegir primero un par de cuadrantes distintos de entre los $\binom{4}{2} = 6$ pares posibles con igual probabilidad, y luego elegir un punto uniformemente al azar en cada uno de los dos cuadrantes seleccionados.
- **$4$ pares de cuadrantes adyacentes:** Un segmento que une puntos en cuadrantes adyacentes cruza exactamente $1$ radio (por tanto, $1$ diámetro).
- **$2$ pares de cuadrantes opuestos:** Un segmento que une el primer y tercer cuadrante (o el segundo y cuarto) cambia de signo en ambas coordenadas, por lo que debe cruzar ambos diámetros (con probabilidad $1$ no pasa por el origen), generando $2$ intersecciones.

El número esperado de intersecciones de uno de estos segmentos con los dos diámetros es:
$$\frac{4}{6}(1) + \frac{2}{6}(2) = \frac{4}{3}$$

Para los $16$ segmentos, el número esperado de intersecciones con los diámetros es:
$$16 \times \frac{4}{3} = \frac{64}{3}$$

### 3. Intersecciones entre pares de los $16$ segmentos aleatorios
Hay $\binom{16}{2} = 120$ pares de segmentos aleatorios. Dos cuerdas se cortan si y solo si sus extremos se alternan a lo largo de la circunferencia. Consideremos los $6 \times 6 = 36$ pares igualmente probables de subconjuntos de $2$ cuadrantes $(S_1, S_2)$ elegidos por dos segmentos $C_1$ y $C_2$:
- **$S_1 = S_2$ ($6$ casos):** Ambos segmentos conectan el mismo par de cuadrantes. En cada uno de los dos cuadrantes hay un extremo de $C_1$ y uno de $C_2$. Los extremos se alternan en la circunferencia con probabilidad $\frac{1}{2}$. Contribución: $6 \times \frac{1}{2} = 3$.
- **$|S_1 \cap S_2| = 1$ ($24$ casos):** Los dos segmentos comparten exactamente un cuadrante. El orden cíclico de los dos extremos fuera del cuadrante compartido es fijo, mientras que los dos extremos dentro del cuadrante compartido tienen la misma probabilidad de aparecer en cualquiera de los dos órdenes posibles; exactamente uno de esos dos órdenes produce alternancia. Por tanto, se cortan con probabilidad $\frac{1}{2}$. Contribución: $24 \times \frac{1}{2} = 12$.
- **$S_1 \cap S_2 = \emptyset$ ($6$ casos):** Los cuatro extremos están en cuadrantes distintos.
  - Si ambos conectan cuadrantes opuestos, es decir, $\{Q_1, Q_3\}$ y $\{Q_2, Q_4\}$ ($2$ casos), sus extremos siempre se alternan, por lo que se cortan con probabilidad $1$. Contribución: $2 \times 1 = 2$.
  - Si ambos conectan cuadrantes adyacentes disjuntos ($4$ casos), nunca se alternan, por lo que se cortan con probabilidad $0$. Contribución: $4 \times 0 = 0$.

Por lo tanto, la probabilidad de que dos segmentos aleatorios se corten es:
$$p = \frac{3 + 12 + 2 + 0}{36} = \frac{17}{36}$$

El número esperado de intersecciones entre los $16$ segmentos aleatorios es:
$$\binom{16}{2} \times \frac{17}{36} = 120 \times \frac{17}{36} = \frac{170}{3}$$

### Total
Sumando todas las intersecciones esperadas:
$$\mathbb{E}[I] = 1 + \frac{64}{3} + \frac{170}{3} = 1 + \frac{234}{3} = 1 + 78 = 79$$

Finalmente, el número esperado de regiones es:
$$\mathbb{E}[R] = 19 + 79 = 98$$

\boxed{98}