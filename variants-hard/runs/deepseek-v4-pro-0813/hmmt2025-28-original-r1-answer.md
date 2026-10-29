Voy a resolverlo paso a paso.

Sea el trapecio isósceles $ABCD$ con bases $AB \parallel CD$, $AB=4$, $CD>4$. Sea $E$ sobre la recta $CD$ con $DE=2$ y $D$ entre $E$ y $C$.

Primero fijo coordenadas. Como $A,B,C,D,M$ están sobre una circunferencia de radio $5$, conviene usar la circunferencia centrada en el origen.

Por simetría del trapecio isósceles, el eje de simetría pasa por los puntos medios de las bases. Tomemos ese eje como el eje $y$.

Sea el centro de la circunferencia $(0,0)$. Como $AB$ es cuerda de longitud $4$, horizontal, sus extremos están a distancia $\sqrt{25 - x_A^2}$ del eje $x$.

Recordemos que $M$ es punto medio de $AE$, y $E$ está sobre $CD$. Vamos a parametrizar con ángulos sobre el círculo.

Como $AB=4$ y es horizontal, si los extremos $A,B$ están a altura $y_1$ sobre el centro, entonces:

$AB = 2\sqrt{R^2 - y_{AB}^2}$ donde $R=5$ y $y_{AB}$ es la distancia del centro a la cuerda $AB$.

$4 = 2\sqrt{25-y_1^2}$

$\sqrt{25-y_1^2}=2 \Rightarrow 25-y_1^2=4 \Rightarrow y_1^2=21$. Entonces $y_1=\sqrt{21}$.

Tomemos $A=(-2,\sqrt{21})$, $B=(2,\sqrt{21})$. La base menor está arriba y la mayor abajo.

Para la cuerda $CD$, con $CD>4$, su distancia al centro será $y_2$ con $|y_2|<|y_1|$ (más cerca del centro, pues cuerda mayor). Sea $D$ el extremo izquierdo de $CD$: $D=(-x_0, y_2)$, $C=(x_0,y_2)$, con $x_0=\sqrt{25-y_2^2}$. Y $CD=2x_0>4$.

$E$ está en la recta $CD$, es decir $y=y_2$, con $D$ entre $E$ y $C$ y $DE=2$. Como $D$ está a la izquierda de $C$ y $D$ entre $E$ y $C$, $E$ está más a la izquierda que $D$. Entonces:

$E=( -x_0 - 2, \, y_2)$.

Ahora $M$ es punto medio de $AE$:

$M=\left( \frac{-2 + (-x_0-2)}{2}, \frac{\sqrt{21}+y_2}{2} \right)
= \left( \frac{-x_0 -4}{2}, \frac{\sqrt{21}+y_2}{2} \right)$.

Como $M$ está sobre el círculo de radio $5$ centrado en el origen:

$\left(\frac{-x_0 -4}{2}\right)^2 + \left(\frac{\sqrt{21}+y_2}{2}\right)^2 = 25$.

Multiplico por $4$:

$(x_0+4)^2 + (\sqrt{21}+y_2)^2 = 100$.

Con $x_0^2 + y_2^2 = 25$. Expando:

$x_0^2 + 8x_0 + 16 + 21 + 2\sqrt{21}\,y_2 + y_2^2 = 100$.

Sustituyo $x_0^2+y_2^2=25$:

$25 + 8x_0 + 16 + 21 + 2\sqrt{21}\,y_2 = 100$

$8x_0 + 62 + 2\sqrt{21}\,y_2 = 100$

$8x_0 + 2\sqrt{21}\,y_2 = 38$

$4x_0 + \sqrt{21}\,y_2 = 19$.   $(1)$

Además $x_0^2 + y_2^2 = 25$, $x_0>0$.

De $(1)$: $4x_0 = 19 - \sqrt{21}\,y_2$.

Elevamos al cuadrado con la ecuación del círculo. Despejo $x_0$:

$x_0 = \frac{19-\sqrt{21}\,y_2}{4}$.

Sustituyo:

$\left(\frac{19-\sqrt{21}\,y_2}{4}\right)^2 + y_2^2 = 25$.

Multiplico por $16$:

$(19-\sqrt{21}\,y_2)^2 + 16 y_2^2 = 400$.

$361 - 38\sqrt{21}\,y_2 + 21 y_2^2 + 16 y_2^2 = 400$.

$37 y_2^2 - 38\sqrt{21}\,y_2 - 39 = 0$.

Resolvemos la cuadrática en $y_2$:

Discriminante:

$\Delta = ( -38\sqrt{21})^2 - 4 \cdot 37 \cdot (-39)$

$= 1444 \cdot 21 + 5772$

$= 30324 + 5772 = 36096$.

$\sqrt{36096}$. Factorizo: $36096 = 16 \cdot 2256$. Probemos $36096 = 64 \cdot 564 = 64 \cdot 4 \cdot 141 = 256 \cdot 141$. Entonces $\sqrt{36096}=16\sqrt{141}$.

Entonces:

$y_2 = \frac{38\sqrt{21} \pm 16\sqrt{141}}{74}$.

Notemos que $\sqrt{141}$ no es múltiplo racional de $\sqrt{21}$, pero verifiquemos posibles simplificaciones. $\sqrt{141}=\sqrt{21\cdot 6.714...}$ no simplifica con $\sqrt{21}$ salvo factor entero, no es el caso.

Como $CD > AB =4$, la cuerda $CD$ está más cerca del centro que $AB$, así $|y_2| < \sqrt{21} \approx 4.58$. Evaluemos:

Primero con signo más:

$\sqrt{21}\approx 4.5826$, $38\cdot 4.5826 \approx 174.14$; $\sqrt{141}\approx 11.874$, $16\cdot 11.874 \approx 190$. 

Signo más: $174.14+190 \approx 364.14$; dividido 74 $\approx 4.92$, que supera $\sqrt{21}\approx 4.58$. Descartada.

Signo menos: $174.14 - 190 \approx -15.86$; dividido 74 $\approx -0.214$. Entonces $y_2 \approx -0.214$.

Así $y_2 = \frac{38\sqrt{21} - 16\sqrt{141}}{74} = \frac{19\sqrt{21}-8\sqrt{141}}{37}$.

Comprobemos que $CD>4$: $x_0 = \sqrt{25-y_2^2}$ será cercano a $5$, así que sí.

Ahora evaluemos $MD$. $M$ y $D$ tienen la misma coordenada $y$ si $D=(-x_0,y_2)$ y $E=(-x_0-2,y_2)$, y $M$ es punto medio de $A$ y $E$. Su coordenada $y_M=\frac{\sqrt{21}+y_2}{2}$, que no es igual a $y_2$ en general. Entonces la distancia $MD$ se calcula directamente.

Coordenadas:

$D=(-x_0,y_2)$,

$M=\left(\frac{-x_0-4}{2}, \frac{\sqrt{21}+y_2}{2}\right)$.

Entonces:

$\Delta x = \frac{-x_0-4}{2} -(-x_0)
= \frac{-x_0-4+2x_0}{2}
= \frac{x_0-4}{2}$.

$\Delta y = \frac{\sqrt{21}+y_2}{2} - y_2
= \frac{\sqrt{21}-y_2}{2}$.

Por tanto:

$MD^2 = \left(\frac{x_0-4}{2}\right)^2 + \left(\frac{\sqrt{21}-y_2}{2}\right)^2$

$= \frac{(x_0-4)^2 + (\sqrt{21}-y_2)^2}{4}$.

Expando numerador:

$(x_0-4)^2 + (\sqrt{21}-y_2)^2$

$= x_0^2 -8x_0 +16 + 21 -2\sqrt{21}\,y_2 + y_2^2$

$= (x_0^2+y_2^2) -8x_0 -2\sqrt{21}\,y_2 +37$

$= 25 -8x_0 -2\sqrt{21}\,y_2 +37$

$= 62 -8x_0 -2\sqrt{21}\,y_2$.

Usamos $(1)$: $4x_0 + \sqrt{21}\,y_2=19$. Entonces $8x_0+2\sqrt{21}\,y_2=38$.

Por lo tanto el numerador es $62-38=24$.

Así $MD^2 = \frac{24}{4}=6$, luego $MD=\sqrt{6}$.

La respuesta final es:

\boxed{\sqrt{6}}