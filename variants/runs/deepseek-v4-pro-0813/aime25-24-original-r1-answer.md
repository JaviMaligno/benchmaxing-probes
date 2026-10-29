Vamos a resolver el problema paso a paso.

## 1. Entender la condición \( f(x) = 0 \)

Tenemos

\[
f(x) = \sin\!\left(7\pi \cdot \sin(5x)\right).
\]

La condición \( f(x) = 0 \) equivale a que

\[
\sin\!\left(7\pi \sin(5x)\right) = 0.
\]

El seno de un ángulo es cero cuando el ángulo es un múltiplo entero de \(\pi\). Por tanto,

\[
7\pi \sin(5x) = k\pi,
\]

es decir,

\[
7\sin(5x) = k,
\]

donde \(k \in \mathbb{Z}\).

Como \(\sin(5x) \in [-1,1]\), los posibles valores de \(k\) son los enteros entre \(-7\) y \(7\), inclusive. Es decir,

\[
k = -7, -6, \dots, 6, 7.
\]

Así,

\[
\sin(5x) = \frac{k}{7}.
\]

---

## 2. Contar las soluciones para cada \(k\)

En el intervalo \(0 < x < 2\pi\), tenemos que \(5x\) recorre el intervalo

\[
0 < 5x < 10\pi.
\]

### Caso \(k = \pm 7\)

Aquí \(\sin(5x) = \pm 1\). La ecuación \(\sin u = 1\) tiene soluciones

\[
u = \frac{\pi}{2} + 2m\pi,
\]

y \(\sin u = -1\) tiene soluciones

\[
u = \frac{3\pi}{2} + 2m\pi.
\]

En el intervalo \(0 < u < 10\pi\):

- Para \(\sin u = 1\), las soluciones son \(u = \frac{\pi}{2}, \frac{5\pi}{2}, \frac{9\pi}{2}, \frac{13\pi}{2}, \frac{17\pi}{2}\). Son **5 soluciones**.
- Para \(\sin u = -1\), las soluciones son \(u = \frac{3\pi}{2}, \frac{7\pi}{2}, \frac{11\pi}{2}, \frac{15\pi}{2}, \frac{19\pi}{2}\). Son **5 soluciones**.

---

### Caso \(-6 \le k \le 6\)

Para cada valor de \(k\) en este rango, \(\frac{k}{7} \in (-1,1)\). La ecuación

\[
\sin u = c,
\]

con \(c \in (-1,1)\), tiene **dos soluciones** en cada intervalo de longitud \(2\pi\).

Como \(u = 5x\) recorre un intervalo de longitud \(10\pi\), que equivale a \(5\) períodos completos del seno, hay

\[
2 \cdot 5 = 10
\]

soluciones para cada \(c \in (-1,1)\).

---

## 3. Total de soluciones \(n\)

- Para los valores extremos \(k = \pm 7\): \(5 + 5 = 10\) soluciones.
- Para los valores intermedios \(k = -6, -5, \dots, 5, 6\), hay \(13\) valores de \(k\), y cada uno produce \(10\) soluciones:

\[
13 \cdot 10 = 130.
\]

Por tanto,

\[
n = 10 + 130 = 140.
\]

---

## 4. Valores donde la gráfica es tangente al eje \(x\)

La gráfica de \(y = f(x)\) es tangente al eje \(x\) cuando

\[
f(x) = 0 \quad \text{y} \quad f'(x) = 0.
\]

Calculemos la derivada:

\[
f(x) = \sin(g(x)), \qquad g(x) = 7\pi \sin(5x).
\]

Entonces,

\[
f'(x) = \cos(g(x)) \cdot g'(x).
\]

Además,

\[
g'(x) = 7\pi \cdot 5\cos(5x) = 35\pi \cos(5x).
\]

Por tanto,

\[
f'(x) = 35\pi \cos(5x) \cdot \cos\!\left(7\pi \sin(5x)\right).
\]

Cuando \(f(x) = 0\), tenemos \(\sin(7\pi \sin(5x)) = 0\). Para que además \(f'(x) = 0\), se necesita

\[
\cos(5x) \cdot \cos\!\left(7\pi \sin(5x)\right) = 0.
\]

Como \(\sin(7\pi \sin(5x)) = 0\), su coseno es \(\pm 1\). Así, el único modo de que el producto sea cero es que

\[
\cos(5x) = 0.
\]

Por tanto, los puntos de tangencia corresponden a los ceros de \(f\) en los que además

\[
\cos(5x) = 0.
\]

---

## 5. Relación con los valores de \(k\)

Tenemos

\[
\sin(5x) = \frac{k}{7}.
\]

Si además \(\cos(5x) = 0\), entonces

\[
\sin(5x) = \pm 1.
\]

Por eso,

\[
\frac{k}{7} = \pm 1,
\]

lo que da \(k = \pm 7\). Esto significa que los únicos ceros de \(f\) para los cuales la gráfica es tangente al eje \(x\) son aquellos con \(\sin(5x) = \pm 1\).

Del paso 2, para \(\sin(5x) = 1\) hay \(5\) soluciones, y para \(\sin(5x) = -1\) hay \(5\) soluciones. Por tanto,

\[
t = 5 + 5 = 10.
\]

---

## 6. Resultado final

\[
n = 140, \qquad t = 10.
\]

Por tanto,

\[
n + t = 140 + 10 = 150.
\]

\[
\boxed{150}
\]