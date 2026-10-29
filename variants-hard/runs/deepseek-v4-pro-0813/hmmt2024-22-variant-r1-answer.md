¡Vamos a resolver el problema paso a paso.

## Paso 1: Entender la configuración

En el triángulo rectángulo $PQR$ con $\angle QPR = 90^\circ$:

- $X$: pie de la **altura** desde $P$ sobre $QR$.
- $Y$: punto donde la **bisectriz** de $\angle QPR$ corta a $QR$.
- $Z$: punto medio de $QR$ (**mediana** desde $P$).

Sabemos que $XY = 5$ y $YZ = 13$. Queremos hallar $QR$.

## Paso 2: Notar la relación entre $X$, $Y$ y $Z$

Un hecho clave en triángulos rectángulos es que la bisectriz del ángulo recto siempre queda entre la altura y la mediana (sobre la hipotenusa). Además, el punto medio $Z$ de la hipotenusa es el circuncentro, y el pie de la altura $X$ puede estar a un lado u otro de $Z$ según si el triángulo es "sesgado" (no isósceles).

Dado $XY = 5$ y $YZ = 13$, hay dos posibilidades de orden:

1. $X$ — $Y$ — $Z$ sobre la hipotenusa, lo que daría $XZ = XY + YZ = 18$.  
2. $Y$ — $Z$ — $X$, lo que daría $XZ = YZ - XY = 8$.

Para un triángulo rectángulo, la bisectriz del ángulo recto *siempre* cae entre la altura y la mediana, es decir, $Y$ queda entre $X$ y $Z$ cuando el triángulo no es isósceles. Por tanto, el orden correcto es $X$ — $Y$ — $Z$, y así

$$
XZ = 18.
$$

## Paso 3: Relacionar $XZ$ con los catetos

Sea $c = QR$ la hipotenusa. Sean $a = PR$ y $b = QP$ los catetos.

Sabemos que $Z$ es el punto medio de la hipotenusa, así que $QZ = ZR = \frac{c}{2}$.

El pie de la altura $X$ divide a la hipotenusa en segmentos proporcionales a los catetos. Una fórmula útil es:

$$
QX = \frac{b^2}{c}, \qquad XR = \frac{a^2}{c}.
$$

Por tanto,

$$
XZ = \left| QZ - QX \right| = \left| \frac{c}{2} - \frac{b^2}{c} \right| = \left| \frac{c^2 - 2b^2}{2c} \right|.
$$

Usando $a^2 + b^2 = c^2$, tenemos $c^2 - 2b^2 = a^2 - b^2$, así que

$$
XZ = \frac{|a^2 - b^2|}{2c}.
$$

Igualando con $XZ = 18$:

$$
\frac{|a^2 - b^2|}{2c} = 18.
$$

## Paso 4: Relacionar la bisectriz con la altura y la mediana

Hay una fórmula que da la distancia entre la altura y la bisectriz desde el vértice del ángulo recto. Alternativamente, usamos la razón en que la bisectriz divide la hipotenusa.

La bisectriz del ángulo recto divide a la hipotenusa $QR$ en segmentos proporcionales a los catetos $a$ y $b$:

$$
QY = \frac{bc}{a+b}, \qquad YR = \frac{ac}{a+b}.
$$

Entonces,

$$
XY = |QX - QY| = \left| \frac{b^2}{c} - \frac{bc}{a+b} \right|.
$$

Factorizando $\frac{b}{c(a+b)}$:

$$
XY = \frac{b}{c(a+b)} \left| b(a+b) - c^2 \right|.
$$

Usando $c^2 = a^2 + b^2$:

$$
b(a+b) - (a^2+b^2) = ab + b^2 - a^2 - b^2 = ab - a^2 = a(b-a).
$$

Luego,

$$
XY = \frac{ab\,|b-a|}{c(a+b)}.
$$

Sabemos $XY = 5$, así que

$$
\frac{ab\,|b-a|}{c(a+b)} = 5.
$$

## Paso 5: Resolver el sistema

Tenemos dos ecuaciones:

$$
\frac{|a^2 - b^2|}{2c} = 18, \tag{1}
$$

$$
\frac{ab\,|a-b|}{c(a+b)} = 5. \tag{2}
$$

Como $|a^2 - b^2| = |a-b|(a+b)$, la ecuación (1) se convierte en:

$$
\frac{|a-b|(a+b)}{2c} = 18.
$$

Ahora dividimos (1) entre (2):

$$
\frac{\frac{|a-b|(a+b)}{2c}}{\frac{ab\,|a-b|}{c(a+b)}} = \frac{18}{5}.
$$

Simplificando:

$$
\frac{|a-b|(a+b)}{2c} \cdot \frac{c(a+b)}{ab\,|a-b|} = \frac{18}{5}.
$$

Los términos $|a-b|$ y $c$ se cancelan:

$$
\frac{(a+b)^2}{2ab} = \frac{18}{5}.
$$

Por tanto,

$$
(a+b)^2 = \frac{36}{5}ab.
$$

## Paso 6: Hallar la hipotenusa $c$

Recordemos que $c^2 = a^2 + b^2 = (a+b)^2 - 2ab$. Usando $(a+b)^2 = \frac{36}{5}ab$:

$$
c^2 = \frac{36}{5}ab - 2ab = \frac{36 - 10}{5}ab = \frac{26}{5}ab.
$$

Ahora necesitamos $ab$. De la ecuación (2) tenemos:

$$
\frac{ab\,|a-b|}{c(a+b)} = 5.
$$

También de (1):

$$
\frac{|a-b|(a+b)}{2c} = 18 \implies \frac{|a-b|}{c} = \frac{36}{a+b}.
$$

Sustituyendo en (2):

$$
\frac{ab}{a+b} \cdot \frac{36}{a+b} = 5,
$$

$$
\frac{36ab}{(a+b)^2} = 5.
$$

Pero ya sabíamos que $(a+b)^2 = \frac{36}{5}ab$, lo cual es consistente. Necesitamos una expresión numérica para $ab$ en términos de $c$.

De $(a+b)^2 = \frac{36}{5}ab$ y $c^2 = a^2 + b^2 = (a+b)^2 - 2ab$:

$$
c^2 = \frac{36}{5}ab - 2ab = \frac{26}{5}ab.
$$

Despejamos $ab$:

$$
ab = \frac{5}{26}c^2.
$$

## Paso 7: Usar la ecuación de $XY$ para hallar $c$

Sustituimos $ab = \frac{5}{26}c^2$ en (2). Primero, de la ecuación (2):

$$
\frac{ab\,|a-b|}{c(a+b)} = 5.
$$

También tenemos $|a-b|(a+b) = |a^2 - b^2| = 2c \cdot 18 = 36c$. Además, $|a-b| = \frac{36c}{a+b}$.

Sustituyendo en (2):

$$
\frac{ab}{c(a+b)} \cdot \frac{36c}{a+b} = 5.
$$

Los $c$ se cancelan:

$$
\frac{36ab}{(a+b)^2} = 5.
$$

Esto es una identidad que ya teníamos. Para obtener una ecuación con $c$, usamos la relación entre $a+b$ y $c$ y $ab$.

Sabemos que:

$$
(a+b)^2 = a^2 + 2ab + b^2 = c^2 + 2ab.
$$

Con $ab = \frac{5}{26}c^2$:

$$
(a+b)^2 = c^2 + 2\cdot \frac{5}{26}c^2 = c^2 + \frac{5}{13}c^2 = \frac{18}{13}c^2.
$$

Por otra parte, $(a+b)^2 = \frac{36}{5}ab = \frac{36}{5}\cdot \frac{5}{26}c^2 = \frac{36}{26}c^2 = \frac{18}{13}c^2$. ¡Consistente!

Ahora usamos $|a^2-b^2| = 36c$:

$$
(a-b)^2(a+b)^2 = (a^2 - b^2)^2.
$$

Recordando que $(a-b)^2 = a^2 - 2ab + b^2 = c^2 - 2ab$:

$$
(a-b)^2 = c^2 - 2\cdot \frac{5}{26}c^2 = c^2 - \frac{5}{13}c^2 = \frac{8}{13}c^2.
$$

Además, $(a+b)^2 = \frac{18}{13}c^2$. Entonces:

$$
(a-b)^2(a+b)^2 = \frac{8}{13}c^2 \cdot \frac{18}{13}c^2 = \frac{144}{169}c^4.
$$

Pero $(a^2 - b^2)^2 = (36c)^2 = 1296c^2$. Igualando:

$$
\frac{144}{169}c^4 = 1296c^2.
$$

Dividiendo entre $c^2$ (con $c > 0$):

$$
\frac{144}{169}c^2 = 1296,
$$

$$
c^2 = 1296 \cdot \frac{169}{144} = 9 \cdot 169 = 1521,
$$

$$
c = \sqrt{1521} = 39.
$$

## Resultado final

$$
\boxed{39}
$$