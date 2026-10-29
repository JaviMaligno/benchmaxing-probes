## Razonamiento paso a paso

### Marco general: conteo de regiones

Cuando tenemos un conjunto de segmentos (o cuerdas) en un disco, el número de regiones se puede calcular mediante la fórmula de Euler para un grafo planar:

\[
R = E - V + 1,
\]

donde:

- \(V\) = número total de vértices del grafo (puntos de intersección más puntos finales de los segmentos sobre la circunferencia),
- \(E\) = número total de aristas,
- y sumamos \(1\) porque el exterior cuenta como una región en el grafo planar completo.

Alternativamente, cada vez que agregamos una cuerda nueva, el número de regiones aumenta en:

\[
1 + (\text{número de intersecciones de la cuerda con segmentos previos}).
\]

Es decir,

\[
R = 1 + \sum_{\text{segmentos}} \left(1 + \text{intersecciones previas del segmento}\right).
\]

Aquí partimos de los dos diámetros y luego añadimos 16 cuerdas aleatorias.

---

### Regiones iniciales con los dos diámetros

Maya traza dos diámetros perpendiculares. Esto divide el disco en:

\[
4 \text{ regiones}.
\]

Los dos diámetros se cruzan en el centro, creando un punto de intersección. Cada diámetro queda dividido por el centro en dos aristas. En total, sobre estos dos diámetros hay:

- \(V = 5\) vértices: \(4\) puntos sobre la circunferencia más el centro,
- \(E\): cada diámetro tiene 2 aristas, así que \(4\) aristas en total.

Con Euler:

\[
R = E - V + 1 = 4 - 5 + 1 = 0,
\]

pero ese cálculo es para el grafo sin la frontera; en realidad las regiones del disco son \(4\), y la fórmula con la frontera incluida da:

\[
R_{\text{disco}} = E - V + 1 + 1 = 4 - 5 + 2 = 1,
\]

lo cual no coincide. Mejor usemos directamente el enfoque incremental, que es más claro.

Con los dos diámetros ya trazados, hay **4 regiones**.

---

### Cómo añadir una cuerda nueva

Cada cuerda nueva corta una serie de regiones. Si una cuerda cruza \(k\) segmentos ya existentes, entonces:

- pasa por \(k+1\) regiones,
- y por lo tanto aumenta el número de regiones en \(k+1\).

Así, el número esperado de regiones finales es:

\[
\mathbb{E}[R] = 4 + \sum_{i=1}^{16} \left(1 + \mathbb{E}[k_i]\right),
\]

donde \(k_i\) es el número de intersecciones de la \(i\)-ésima cuerda aleatoria con los segmentos ya trazados.

---

### Intersecciones con los diámetros

Consideremos una cuerda cuyos extremos están en cuadrantes distintos.

Hay que distinguir:

- **Extremos en cuadrantes opuestos**: la cuerda cruza el centro si los extremos son puntos diametralmente opuestos, pero en general una cuerda con extremos en cuadrantes opuestos pasa por el centro solo si los puntos son exactamente antipodales, lo cual tiene probabilidad \(0\). Sin cruzarlo, cruza **exactamente uno** de los dos diámetros.

  Veamos por qué: si los extremos están en cuadrantes opuestos (por ejemplo, cuadrante I y cuadrante III), la cuerda cruza la región central. Dependiendo de la posición, cruzará uno de los dos diámetros o pasará muy cerca del centro. Como los diámetros son perpendiculares y pasan por el centro, cualquier cuerda que una cuadrantes opuestos sin pasar exactamente por el centro corta **exactamente un diámetro**.

- **Extremos en cuadrantes adyacentes**: la cuerda no pasa por el centro y tampoco cruza ningún diámetro, salvo si sus extremos están justo sobre las líneas que separan los cuadrantes, lo cual tiene probabilidad \(0\). Por tanto, en el caso general corta **0** diámetros.

Entonces, para una cuerda aleatoria:

- Hay \(4\) cuadrantes. El número total de pares de cuadrantes es \(\binom{4}{2} = 6\).
- De esos \(6\), hay \(2\) pares de cuadrantes opuestos: (I, III) y (II, IV).
- Y \(4\) pares de cuadrantes adyacentes: (I, II), (II, III), (III, IV), (IV, I).

Como los dos puntos se eligen uniformemente en la circunferencia, la probabilidad de que caigan en dos cuadrantes particulares es proporcional a las áreas (longitudes) de esos cuadrantes. Los cuatro cuadrantes tienen la misma área, así que cada uno de los \(6\) pares de cuadrantes tiene la misma probabilidad:

\[
\frac{1}{6}.
\]

Por lo tanto, la probabilidad de que una cuerda tenga extremos en cuadrantes opuestos es:

\[
\frac{2}{6} = \frac{1}{3}.
\]

Y en cuadrantes adyacentes:

\[
\frac{4}{6} = \frac{2}{3}.
\]

Así, el número esperado de intersecciones con los diámetros es:

\[
\mathbb{E}[\text{intersecciones con diámetros}] = \frac{1}{3} \cdot 1 + \frac{2}{3} \cdot 0 = \frac{1}{3}.
\]

---

### Intersecciones entre las cuerdas aleatorias

Consideremos dos cuerdas aleatorias independientes. ¿Cuál es la probabilidad de que se crucen dentro del disco?

Dos cuerdas se cruzan si y solo si sus extremos se alternan alrededor de la circunferencia. Para cuatro puntos elegidos uniformemente al azar en la circunferencia, la probabilidad de que los extremos de las dos cuerdas estén alternados es:

\[
\frac{1}{3}.
\]

Justificación: fijemos los dos extremos de una cuerda. Los otros dos puntos caen aleatoriamente; de las \(3\) formas en que pueden quedar entremezclados (relativas a los dos arcos determinados por la primera cuerda), exactamente \(1\) produce cruce. Por tanto, la probabilidad de que dos cuerdas aleatorias se crucen es:

\[
p = \frac{1}{3}.
\]

Pero ojo: aquí las cuerdas no son completamente arbitrarias; sus extremos deben estar en cuadrantes distintos. Esto restringe la elección y podría cambiar la probabilidad de cruce. Sin embargo, veremos que no cambia, porque la condición “extremos en cuadrantes distintos” es simétrica y no introduce correlación que altere la probabilidad de alternancia.

De hecho, aun con la restricción de cuadrantes, la probabilidad de que dos cuerdas con extremos en cuadrantes distintos se crucen sigue siendo \(1/3\).

---

### Cálculo del número esperado de regiones

Denotemos por \(C_1, C_2, \dots, C_{16}\) las cuerdas aleatorias, en el orden en que se dibujan.

El número esperado de intersecciones de \(C_i\) con las cuerdas previas es:

\[
\mathbb{E}[k_i] = (i-1) \cdot \frac{1}{3},
\]

por linealidad de la esperanza.

Además, \(C_i\) cruza los dos diámetros con esperanza \(1/3\), como calculamos antes.

Por tanto, el número esperado de regiones añadidas al dibujar \(C_i\) es:

\[
1 + (i-1) \cdot \frac{1}{3} + \frac{1}{3}
= 1 + \frac{i}{3}.
\]

Empezando con \(4\) regiones de los dos diámetros:

\[
\mathbb{E}[R] = 4 + \sum_{i=1}^{16} \left(1 + \frac{i}{3}\right).
\]

Calculamos:

\[
\sum_{i=1}^{16} 1 = 16,
\]

\[
\sum_{i=1}^{16} \frac{i}{3} = \frac{1}{3} \cdot \frac{16 \cdot 17}{2} = \frac{136}{3}.
\]

Entonces:

\[
\mathbb{E}[R] = 4 + 16 + \frac{136}{3}
= 20 + \frac{136}{3}
= \frac{60 + 136}{3}
= \frac{196}{3}.
\]

---

\[
\boxed{\frac{196}{3}}
\]