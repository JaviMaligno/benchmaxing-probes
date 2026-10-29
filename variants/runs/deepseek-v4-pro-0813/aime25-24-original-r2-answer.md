Vamos a analizar el problema paso a paso.

Tenemos:
\[
f(x) = \sin\bigl(7\pi \sin(5x)\bigr)
\]

Buscamos los ceros en \(0 < x < 2\pi\), es decir, los \(x\) tales que
\[
\sin\bigl(7\pi \sin(5x)\bigr) = 0.
\]

## Paso 1: ceros del seno exterior

El seno exterior se anula cuando su argumento es un múltiplo entero de \(\pi\):
\[
7\pi \sin(5x) = k\pi, \qquad k \in \mathbb{Z}.
\]
Dividiendo entre \(\pi\):
\[
7\sin(5x) = k.
\]

Como \(\sin(5x) \in [-1,1]\), tenemos
\[
k \in \{-7,-6,\dots,6,7\}.
\]

Por tanto, los ceros de \(f\) están dados por:
\[
\sin(5x) = \frac{k}{7}, \qquad k=-7,-6,\dots,6,7.
\]

## Paso 2: contar ceros

Para cada \(k \in \{-7,\dots,7\}\), hay que contar cuántas soluciones tiene \(\sin(5x) = \frac{k}{7}\) en \(0 < x < 2\pi\).

Los casos especiales son \(k = \pm 7\), que corresponden a
\[
\sin(5x) = \pm 1.
\]
Para cada uno de estos dos casos hay exactamente \(2\) soluciones en \((0, 2\pi)\) (los máximos/mínimos de \(\sin(5x)\)), pues en el intervalo \(5x \in (0, 10\pi)\) la función \(\sin(5x)\) alcanza el valor \(1\) en
\[
5x = \frac{\pi}{2} + 2m\pi, \qquad m = 0,1,2,3,4
\]
es decir, \(5\) puntos, y análogamente para \(-1\). Espera: hay que comprobar con cuidado.

Para \(5x \in (0, 10\pi)\):

- \(\sin(5x)=1\) cuando \(5x = \frac{\pi}{2} + 2m\pi\). Con \(m=0,1,2,3,4\) obtenemos \(5x = \frac{\pi}{2}, \frac{5\pi}{2}, \frac{9\pi}{2}, \frac{13\pi}{2}, \frac{17\pi}{2}\), todos dentro de \((0, 10\pi)\). Son \(5\) soluciones.

- \(\sin(5x)=-1\) cuando \(5x = \frac{3\pi}{2} + 2m\pi\). Con \(m=0,1,2,3,4\) obtenemos \(5x = \frac{3\pi}{2}, \frac{7\pi}{2}, \frac{11\pi}{2}, \frac{15\pi}{2}, \frac{19\pi}{2}\), también \(5\) soluciones.

Entonces para \(k=-7\) hay \(5\) y para \(k=7\) hay \(5\): en total \(10\).

Para los valores \(k=-6,\dots,6\) (es decir, \(13\) valores), tenemos
\[
\sin(5x) = \frac{k}{7},
\]
con \(\left|\frac{k}{7}\right| < 1\) para \(k=-6,\dots,6\).

En un período de longitud \(2\pi\) de la variable \(5x\), la ecuación \(\sin u = c\) con \(|c|<1\) tiene exactamente \(2\) soluciones. Dado que el intervalo \(5x \in (0, 10\pi)\) contiene \(5\) períodos completos de longitud \(2\pi\), hay
\[
5 \cdot 2 = 10
\]
soluciones por cada \(k \in \{-6,\dots,6\}\).

Hay \(13\) valores de \(k\) en \(\{-6,\dots,6\}\), así que:
\[
13 \cdot 10 = 130.
\]

Total de ceros:
\[
n = 130 + 10 = 140.
\]

## Paso 3: contar tangencias

Una tangencia ocurre cuando, además de \(f(x)=0\), la derivada se anula:
\[
f'(x) = \cos\bigl(7\pi \sin(5x)\bigr) \cdot 7\pi \cos(5x) \cdot 5 = 0.
\]

En un cero de \(f\), tenemos \(\sin(5x) = \frac{k}{7}\) con \(k \in \{-7,\dots,7\}\). Se presentan dos posibilidades:

1. \(\cos(7\pi \sin(5x)) = 0\): ocurre cuando
\[
7\pi \sin(5x) = \frac{\pi}{2} + m\pi,
\]
es decir,
\[
7\sin(5x) = m + \tfrac12.
\]
Pero \(\sin(5x)=\frac{k}{7}\), luego
\[
k = m + \tfrac12,
\]
que es imposible para \(k\) entero. Así que este caso no contribuye.

2. \(\cos(5x) = 0\): ocurre cuando
\[
5x = \frac{\pi}{2} + m\pi.
\]

Debemos imponer que estos puntos sean ceros de \(f\). En ese caso,
\[
\sin(5x) = \pm 1,
\]
luego los ceros correspondientes son los de \(k = \pm 7\).

En \(5x \in (0, 10\pi)\), \(\cos(5x)=0\) cuando
\[
5x = \frac{\pi}{2} + m\pi, \qquad m = 0,1,\dots,9.
\]
Esto da \(10\) puntos.

De esos \(10\) puntos, los de \(\sin(5x)=1\) son \(5\) y los de \(\sin(5x)=-1\) son \(5\). Todos ellos están dentro de \((0, 10\pi)\), por lo que producen tangencias.

Por tanto,
\[
t = 10.
\]

## Paso 4: resultado final

\[
n + t = 140 + 10 = 150.
\]

\[
\boxed{150}
\]