

Etiquetemos los cuadrantes del círculo como \(Q_1,Q_2,Q_3,Q_4\) en orden cíclico. Los dos diámetros perpendiculares ya dividen el disco en \(4\) regiones.

Salvo eventos de probabilidad cero (tres segmentos concurrentes, un segmento pasando por el centro, etc.), al añadir un segmento nuevo que corta a los segmentos ya dibujados en \(k\) puntos interiores, ese segmento queda dividido en \(k+1\) trozos y aumenta el número de regiones en \(k+1\). Así, si añadimos las \(16\) cuerdas aleatorias,

\[
\mathbb{E}[R]=4+16+\mathbb{E}[I_D]+\mathbb{E}[I_C],
\]

donde \(I_D\) es el número de intersecciones de las cuerdas con los dos diámetros, e \(I_C\) es el número de intersecciones entre las propias cuerdas.

---

### 1. Intersecciones con los diámetros

Para cada cuerda aleatoria, sus dos extremos están en cuadrantes distintos. El par no ordenado de cuadrantes es uniforme entre los

\[
\binom{4}{2}=6
\]

pares posibles.

- Hay \(4\) pares de cuadrantes adyacentes. Una cuerda que une cuadrantes adyacentes cruza exactamente \(1\) de los dos diámetros.
- Hay \(2\) pares de cuadrantes opuestos. Una cuerda que une cuadrantes opuestos cruza los \(2\) diámetros.

Por tanto, el número esperado de intersecciones con diámetros por cada cuerda es

\[
\frac{4}{6}\cdot 1+\frac{2}{6}\cdot 2=\frac{4}{3}.
\]

Para \(16\) cuerdas,

\[
\mathbb{E}[I_D]=16\cdot \frac{4}{3}=\frac{64}{3}.
\]

---

### 2. Intersecciones entre las cuerdas aleatorias

Dos cuerdas se cruzan en el interior del disco si y sólo si sus cuatro extremos aparecen alternados alrededor de la circunferencia.

Calculamos la probabilidad \(p\) de que dos cuerdas aleatorias independientes se crucen.

Una cuerda puede ser de dos tipos:

- adyacente: une dos cuadrantes consecutivos, probabilidad \(\frac{4}{6}=\frac{2}{3}\);
- opuesta: une dos cuadrantes opuestos, probabilidad \(\frac{2}{6}=\frac{1}{3}\).

#### Caso A: la primera cuerda es adyacente

Supongamos que une \(Q_1\) y \(Q_2\). Para la segunda cuerda, entre sus \(6\) pares posibles:

- \(5\) pares tienen al menos un cuadrante en común con \(\{Q_1,Q_2\}\). En estos casos, el orden relativo de los extremos dentro de los cuadrantes comunes hace que las cuerdas se crucen con probabilidad \(\frac12\).
- \(1\) par es disjunto: \(\{Q_3,Q_4\}\). En ese caso los extremos de cada cuerda quedan consecutivos alrededor del círculo, así que no se cruzan.

Por tanto,

\[
\mathbb{P}(\text{cruce}\mid \text{primera adyacente})
=
\frac{5}{6}\cdot \frac12+\frac{1}{6}\cdot 0
=
\frac{5}{12}.
\]

#### Caso B: la primera cuerda es opuesta

Supongamos que une \(Q_1\) y \(Q_3\). Para la segunda cuerda:

- \(5\) de los \(6\) pares posibles dan probabilidad de cruce \(\frac12\).
- El otro par opuesto, \(\{Q_2,Q_4\}\), alterna siempre los extremos, así que da probabilidad \(1\).

Por tanto,

\[
\mathbb{P}(\text{cruce}\mid \text{primera opuesta})
=
\frac{5}{6}\cdot \frac12+\frac{1}{6}\cdot 1
=
\frac{7}{12}.
\]

Luego

\[
p
=
\frac{2}{3}\cdot \frac{5}{12}
+
\frac{1}{3}\cdot \frac{7}{12}
=
\frac{10}{36}+\frac{7}{36}
=
\frac{17}{36}.
\]

Hay \(\binom{16}{2}=120\) pares de cuerdas aleatorias, así que

\[
\mathbb{E}[I_C]
=
120\cdot \frac{17}{36}
=
\frac{170}{3}.
\]

---

### 3. Número esperado de regiones

Finalmente,

\[
\mathbb{E}[R]
=
4+16+\frac{64}{3}+\frac{170}{3}
=
20+\frac{234}{3}
=
20+78
=
98.
\]

\[
\boxed{98}
\]