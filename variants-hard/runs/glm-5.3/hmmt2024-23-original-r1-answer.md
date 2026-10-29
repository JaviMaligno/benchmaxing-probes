# Solución

**Configuración.** Sea $O$ el centro de $\Omega$ y $P$ el centro de $\omega$. Como $O$ está sobre $\omega$, la distancia entre centros es $OP = 61$.

Sea $AB$ la cuerda de $\Omega$, cortada por $\omega$ en los puntos $X$ y $Y$ (con $X$ más cerca de $A$). Si las longitudes son $k:2k:3k$:

$$AX = k, \quad XY = 2k, \quad YB = 3k, \quad \text{entonces } AB = 6k.$$

**Paso 1: el punto medio de la cuerda coincide con un punto de corte.**

Sea $M$ el punto medio de $AB$; como $AM = 3k$ y $Y$ está a $k + 2k = 3k$ de $A$, se concluye que **$M = Y$**. Es decir, $Y$ es exactamente el punto medio de la cuerda.

**Paso 2: posición del centro de $\omega$.**

Sea $N$ el pie de la perpendicular desde $P$ a la recta $AB$. Como $N$ es el punto medio de la cuerda $XY$ de $\omega$:

$$AN = k + k = 2k \implies MN = AM - AN = 3k - 2k = k.$$

Sea $d = PN$ la distancia de $P$ a la recta de la cuerda, y sea $h = OM$ la distancia de $O$ a la recta de la cuerda.

**Paso 3: ecuaciones.**

- Como $PY = 61$ es radio de $\omega$:
$$k^2 + d^2 = 61^2 = 3721. \tag{1}$$

- Como $OP = 61$, con la horizontal $MN = k$ y vertical $|h \mp d|$ (según el lado en que queden $O$ y $P$):
$$k^2 + (h \mp d)^2 = 3721. \tag{2}$$

De $(1)$ y $(2)$: $(h \mp d)^2 = d^2$, luego $h = 0$ o $h = 2d$ (con signo adecuado). El caso $h = 0$ significa que la cuerda pasa por el centro de $\Omega$, es decir, es un **diámetro**, que el problema excluye. Por lo tanto $h = 2d$.

- Como $A \in \Omega$ con $AM = 3k$:
$$h^2 + 9k^2 = 123^2 = 15129. \tag{3}$$

**Paso 4: resolver el sistema.**

Sustituyendo $h = 2d$ en $(3)$ y usando $(1)$ ($d^2 = 3721 - k^2$):

$$4d^2 + 9k^2 = 15129 \implies 4(3721 - k^2) + 9k^2 = 15129$$
$$14884 + 5k^2 = 15129 \implies 5k^2 = 245 \implies k^2 = 49 \implies k = 7.$$

**Paso 5: longitud y verificación.**

La cuerda mide $AB = 6k = 42$.

*Verificación:* $d^2 = 3721 - 49 = 3672$, así que $h = 2\sqrt{3672} = 12\sqrt{102}$, y en efecto $h^2 + 9k^2 = 14688 + 441 = 15129 = 123^2$ ✓. Además $OP^2 = k^2 + d^2 = 49 + 3672 = 3721 = 61^2$ ✓, y los tres segmentos $7, 14, 21$ están en proporción $1:2:3$ ✓.

$$\boxed{42}$$