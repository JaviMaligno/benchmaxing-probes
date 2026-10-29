Voy a razonar el problema paso a paso.

## Planteamiento

Sea $\Omega$ la circunferencia grande de radio $R = 123$ y $\omega$ la pequeña de radio $r = 61$.

Dato clave 1: **el centro $O$ de $\Omega$ está sobre $\omega$**. Es decir, $O$ es un punto de la circunferencia $\omega$.

Sea $C$ el centro de $\omega$. Entonces $CO = 61$.

Consideramos una cuerda $AB$ de $\Omega$ que es cortada por $\omega$ en tres segmentos con razones $1:2:3$ en ese orden. Como la cuerda atraviesa $\omega$ y el centro de $\Omega$ (que está sobre $\omega$) se encuentra en algún lugar, conviene parametrizar la situación mediante la distancia del centro $O$ de $\Omega$ a la cuerda.

---

## Parametrización

Sea $d$ la distancia del centro $O$ de $\Omega$ a la cuerda. Entonces la semilongitud de la cuerda de $\Omega$ es

$$
\ell = \sqrt{R^2 - d^2} = \sqrt{123^2 - d^2}.
$$

La longitud total de la cuerda de $\Omega$ es $2\ell$.

Necesitamos que $\omega$ corte esta cuerda de manera que los tres segmentos sobre la cuerda (delimitados por los dos puntos de intersección de la cuerda con $\omega$) tengan longitudes en proporción $1:2:3$.

Esto significa que, si los puntos de intersección de la cuerda con $\omega$ son $P$ y $Q$, y los extremos de la cuerda de $\Omega$ son $A$ y $B$ (en ese orden $A, P, Q, B$), entonces

$$
AP : PQ : QB = 1 : 2 : 3.
$$

Sea $k$ la unidad de proporción. Entonces:

- $AP = k$
- $PQ = 2k$
- $QB = 3k$

y la longitud de la cuerda de $\Omega$ es $AB = AP + PQ + QB = k + 2k + 3k = 6k$.

Por tanto $2\ell = 6k$, de donde $k = \ell/3$. Además:

$$
AP = \frac{\ell}{3}, \qquad PQ = \frac{2\ell}{3}, \qquad QB = \ell.
$$

En particular, la cuerda de $\omega$ (el segmento $PQ$) tiene longitud $PQ = \dfrac{2\ell}{3}$.

---

## Relación entre $\omega$ y el centro de $\Omega$

Como $O$ está sobre $\omega$, la distancia del centro $C$ de $\omega$ al punto $O$ es $CO = 61 = r$.

Consideremos la cuerda $PQ$ de $\omega$. Su semilongitud es

$$
\ell_\omega = \frac{PQ}{2} = \frac{2\ell/3}{2} = \frac{\ell}{3}.
$$

Si $M$ es el punto medio de la cuerda, la distancia del centro $C$ de $\omega$ a la cuerda es $CM$, y para la circunferencia $\omega$ se cumple

$$
CM^2 + \ell_\omega^2 = r^2,
$$

es decir,

$$
CM^2 + \left(\frac{\ell}{3}\right)^2 = 61^2.
$$

Por otro lado, para $\Omega$, el punto medio de su cuerda $AB$ es el pie de la perpendicular desde $O$. ¿Es este punto medio el mismo que $M$?

Veamos: la cuerda es un segmento común de una recta. Para $\Omega$, el punto medio de $AB$ es el pie de la perpendicular desde $O$, y para $\omega$, el punto medio de $PQ$ es el pie de la perpendicular desde $C$. No son en general el mismo punto.

Necesitamos por tanto ubicar $M$ (punto medio de $PQ$) respecto de $O$, es decir, la distancia $OM$ a lo largo de la recta.

---

## Posición relativa de los segmentos

Sobre la recta que contiene la cuerda, elegimos una coordenada con origen en $M$ (punto medio de $PQ$). Entonces:

- $P$ y $Q$ están en $x = -\ell_\omega$ y $x = +\ell_\omega$ donde $\ell_\omega = \ell/3$.
- La cuerda de $\Omega$ tiene longitud $6k = 2\ell$, con $PQ = 2\ell/3$ en el centro de la proporción $2$.

Los extremos $A$ y $B$ de la cuerda de $\Omega$ están separados $2\ell$ en total. El segmento $PQ$ ocupa $\dfrac{2\ell}{3}$ centrales. Entonces queda $\dfrac{2\ell - 2\ell/3}{2} = \dfrac{4\ell/3}{2} = \dfrac{2\ell}{3}$ a cada lado... 

Espera, calculemos con las proporciones dadas $k:\ 2k : 3k$.

- $A$ está a distancia $k = \ell/3$ a la izquierda de $P$.
- $Q$ está a distancia $3k = \ell$ a la derecha... No, $Q$ a la derecha de $P$ está a $2k = 2\ell/3$, y $B$ a la derecha de $Q$ está a $3k = \ell$.

Entonces, tomando $P$ como referencia:

- $A$ en $x = -k = -\ell/3$
- $P$ en $x = 0$
- $Q$ en $x = 2k = 2\ell/3$
- $B$ en $x = 2k + 3k = 5k = 5\ell/3$

Por tanto el punto medio $M$ de $PQ$ está en $x = k = \ell/3$ (promedio de $0$ y $2\ell/3$).

El punto medio de $AB$ está en $x = \dfrac{-k + 5k}{2} = \dfrac{4k}{2} = 2k = \dfrac{2\ell}{3}$.

Así que, respecto a $M$, el punto medio $N$ de $AB$ está en

$$
N - M = \frac{2\ell}{3} - \frac{\ell}{3} = \frac{\ell}{3}.
$$

Es decir, el pie de la perpendicular desde $O$ (que es $N$) está desplazado $\ell/3$ a la derecha de $M$ sobre la recta.

---

## Relaciones con las distancias a los centros

La recta de la cuerda está a distancia $d = ON$ del centro de $\Omega$.

La distancia de $C$ a la recta es $CM$, y ya teníamos

$$
CM^2 + \left(\frac{\ell}{3}\right)^2 = 61^2.
$$

Necesitamos relacionar $CM$ con $d$ y con la posición relativa de $M$ y $N$. Para ello usamos la posición de $O$ y $C$.

Recordemos que $O$ está sobre $\omega$, así que $CO = 61$.

Proyectemos sobre la recta perpendicular a la cuerda los puntos $O$, $C$, $N$ y $M$. Sean sus proyecciones $O'$, $C'$, $N'$ y $M'$. Entonces:

- La distancia de $O$ a la recta es $ON = d = O'N'$.
- La distancia de $C$ a la recta es $CM = C'M'$.
- Sobre la dirección de la recta (paralela), la separación entre los pies es $NM = \ell/3$.

La distancia $OC = 61$ se descompone en dos componentes perpendiculares:

$$
OC^2 = (\text{diferencia de alturas})^2 + (\text{separación paralela})^2.
$$

La diferencia de alturas entre $O$ y $C$ es $ON - CM = d - CM$ (tomando signo según orientación). La separación paralela es $NM = \ell/3$.

Por tanto:

$$
61^2 = (d - CM)^2 + \left(\frac{\ell}{3}\right)^2.
$$

---

## Sistema de ecuaciones

Tenemos:

1. Para $\Omega$: $\ell^2 + d^2 = 123^2$.

2. Para $\omega$: $CM^2 + \left(\dfrac{\ell}{3}\right)^2 = 61^2$.

3. Para $OC$: $(d - CM)^2 + \left(\dfrac{\ell}{3}\right)^2 = 61^2$.

De 2:

$$
CM^2 = 61^2 - \frac{\ell^2}{9}.
$$

De 3:

$$
(d - CM)^2 = 61^2 - \frac{\ell^2}{9} = CM^2.
$$

Entonces:

$$
(d - CM)^2 = CM^2.
$$

Esto da dos posibilidades:

- $d - CM = CM$, es decir, $d = 2CM$.
- $d - CM = -CM$, es decir, $d = 0$.

Si $d = 0$, la cuerda sería un diámetro, pero el problema aclara que **no es un diámetro**. Por tanto:

$$
d = 2CM.
$$

---

## Resolución

Sustituimos $d = 2CM$ en la ecuación de $\Omega$:

$$
\ell^2 + (2CM)^2 = 123^2.
$$

Además, de la ecuación de $\omega$:

$$
CM^2 + \frac{\ell^2}{9} = 61^2.
$$

Despejamos $\ell^2$ de esta última:

$$
\ell^2 = 9(61^2 - CM^2).
$$

Sustituimos en la primera:

$$
9(61^2 - CM^2) + 4CM^2 = 123^2.
$$

$$
9 \cdot 61^2 - 5CM^2 = 123^2.
$$

Calculamos:

$$
61^2 = 3721, \qquad 123^2 = 15129.
$$

$$
9 \cdot 3721 = 33489.
$$

Entonces:

$$
33489 - 5CM^2 = 15129.
$$

$$
5CM^2 = 33489 - 15129 = 18360.
$$

$$
CM^2 = \frac{18360}{5} = 3672.
$$

Ahora:

$$
\ell^2 = 9(3721 - 3672) = 9 \cdot 49 = 441.
$$

$$
\ell = 21.
$$

La longitud de la cuerda es $2\ell = 42$.

---

## Verificación

- $\ell = 21$, cuerda de $\Omega$ de longitud $42$.
- $d = 2CM$, con $CM = \sqrt{3672} = 6\sqrt{102} \approx 60{,}6$... 

Espera, verifiquemos que esto es consistente: $CM^2 = 3672$, en efecto $CM \approx 60{,}6 < 61$, correcto para una cuerda de $\omega$.

Entonces $d = 2CM \approx 121{,}2$. Para $\Omega$, con $R = 123$, esto da semilongitud $\ell = \sqrt{123^2 - d^2} = \sqrt{15129 - 14688} = \sqrt{441} = 21$, consistente.

Los radios son distintos, la cuerda no es diámetro, y las proporciones $1:2:3$ se cumplen con $k = 7$: segmentos $7$, $14$ y $21$, que suman $42$, coincidiendo con $2\ell = 42$.

La respuesta es:

$$
\boxed{42}
$$