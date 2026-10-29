## Razonamiento

Tenemos un triángulo acutángulo $XYZ$. Sea $P$ el pie de la altura desde $X$ a $\overline{YZ}$, $R$ el pie desde $Y$ a $\overline{ZX}$, $S$ el pie desde $Z$ a $\overline{XY}$. El triángulo $PRS$ es el triángulo órtico (orticoide) de $XYZ$.

Sea $T$ el pie de la perpendicular desde $X$ a la línea $RS$. Datos: $XT = 15$, $YZ = 16$, $XP = 20$.

Denotemos:

- $a = YZ = 16$ (lado opuesto a $X$)
- $h_a = XP = 20$ (altura desde $X$)

Entonces el área del triángulo $XYZ$ es:

$$K = \frac{1}{2} \cdot a \cdot h_a = \frac{1}{2} \cdot 16 \cdot 20 = 160.$$

Queremos el perímetro del triángulo órtico $PRS$.

### Propiedades del triángulo órtico

En un triángulo acutángulo, los lados del triángulo órtico son:

- $RS = a\cos X$ (lado opuesto al vértice $X$ en el órtico)
- $SP = b\cos Y$
- $PR = c\cos Z$

donde $a, b, c$ son los lados opuestos a $X, Y, Z$ respectivamente.

Además, el lado $RS$ del órtico es antiparalelo a $YZ$ respecto al ángulo $X$. La distancia desde $X$ a $RS$ es $XT$.

### Relación entre $XT$ y otros elementos

La línea $RS$ en el triángulo órtico es antiparalela a $YZ$. Se puede demostrar que la distancia desde $X$ a la recta $RS$ es:

$$XT = 2R \cos X \cos(Y-Z) \cdot \sin X$$

o más sencillamente, analicemos geométricamente.

Consideremos las coordenadas. Coloquemos $X$ en el origen, con la altura $XP$ a lo largo del eje $y$ (o eje vertical). Sea $YZ$ una recta horizontal a distancia $20$ de $X$, así $P$ es el pie en $YZ$ con $XP = 20$.

Sean $Y$ y $Z$ sobre la línea horizontal con $YZ = 16$. Coloquemos $P$ en $(0,0)$, $X$ en $(0,20)$, y $Y = (-m, 0)$, $Z = (16-m, 0)$ para cierto $m$ con $0 < m < 16$.

El ángulo $X$ es agudo, y como el triángulo es acutángulo, el pie $P$ está entre $Y$ y $Z$, lo cual ya se cumple.

Ahora, calculemos los pies de las alturas $R$ y $S$.

**Pie $R$** desde $Y$ a $\overline{ZX}$.

Recta $ZX$: pasa por $Z = (16-m, 0)$ y $X = (0, 20)$. Vector director $ZX = (-(16-m), 20)$.

**Pie $S$** desde $Z$ a $\overline{XY}$: recta $XY$ pasa por $X=(0,20)$ y $Y=(-m,0)$, vector director $XY = (-m, -20)$.

Vamos a encontrar las coordenadas de $R$ y $S$ y luego la recta $RS$, para hallar la distancia desde $X$ a $RS$.

### Cálculos

**Recta $XY$**: pasa por $(0,20)$ y $(-m, 0)$. Pendiente:

$$k_1 = \frac{0-20}{-m-0} = \frac{-20}{-m} = \frac{20}{m}.$$

Ecuación de $XY$: 
$$y - 20 = \frac{20}{m}(x - 0) \Rightarrow y = \frac{20}{m}x + 20.$$

La altura desde $Z$ es perpendicular a $XY$, pendiente $-\frac{m}{20}$. Pasa por $Z=(16-m,0)$:

$$y = -\frac{m}{20}(x - (16-m)).$$

**Intersección $S$**:

$$\frac{20}{m}x + 20 = -\frac{m}{20}(x - 16 + m)$$

Multiplicamos por $20m$:

$$400x + 400m = -m^2(x - 16 + m) = -m^2 x + 16m^2 - m^3$$

$$400x + m^2 x = 16m^2 - m^3 - 400m$$

$$x_S = \frac{16m^2 - m^3 - 400m}{400 + m^2} = \frac{m(16m - m^2 - 400)}{400+m^2}.$$

**Recta $ZX$**: pasa por $(16-m,0)$ y $(0,20)$. Pendiente:

$$k_2 = \frac{20-0}{0-(16-m)} = \frac{20}{m-16}.$$

Altura desde $Y$ perpendicular a $ZX$: pendiente $-\frac{m-16}{20} = \frac{16-m}{20}$. Pasa por $Y=(-m,0)$:

$$y = \frac{16-m}{20}(x + m).$$

**Intersección $R$**:

Recta $ZX$: 
$$y = \frac{20}{m-16}(x - 16 + m).$$

Igualamos:

$$\frac{20}{m-16}(x - 16 + m) = \frac{16-m}{20}(x+m).$$

Observemos que $16 - m = -(m-16)$. Entonces:

$$\frac{20}{m-16}(x - 16 + m) = -\frac{m-16}{20}(x+m).$$

Multiplicamos por $20(m-16)$:

$$400(x - 16 + m) = -(m-16)^2(x+m).$$

$$400x - 6400 + 400m = -(m-16)^2 x - (m-16)^2 m.$$

$$x_R\big[400 + (m-16)^2\big] = 6400 - 400m - m(m-16)^2.$$

Entonces:

$$x_R = \frac{6400 - 400m - m(m-16)^2}{400 + (m-16)^2}.$$

### Recta $RS$ y distancia desde $X$

Necesitamos encontrar la distancia desde $X=(0,20)$ a la recta que pasa por $R$ y $S$. Sabemos que esta distancia es $15$.

Sin embargo, esta vía algebraica es muy laboriosa. Busquemos una relación más elegante.

### Relación conocida para el triángulo órtico

Recordemos: en el triángulo órtico de un triángulo acutángulo, las alturas del triángulo original son las bisectrices de los ángulos del triángulo órtico. En particular, $X$ es el incentro o excentro de $PRS$... Precisamente, $X, Y, Z$ son los excentros del triángulo órtico $PRS$, y el vértice original es el excentro correspondiente al vértice correspondiente. De hecho, el triángulo órtico $PRS$ tiene como excentros los vértices $X, Y, Z$ del triángulo original, y el vértice $X$ es el excentro opuesto al vértice $P$ del triángulo órtico.

Es decir, el triángulo $XYZ$ es el triángulo excentral del triángulo órtico $PRS$. El triángulo excentral de un triángulo tiene por lados las bisectrices externas.

Entonces, podemos usar las relaciones entre un triángulo y su triángulo excentral.

Sea el triángulo órtico $\triangle PRS$ con lados:

- $p = RS$ (opuesto a $P$)
- $r = SP$ (opuesto a $R$)
- $s = PR$ (opuesto a $S$)

El triángulo excentral $XYZ$ tiene vértices que son excentros. El lado $YZ$ del triángulo excentral es el segmento entre los excentros $Y$ y $Z$ (excentros relativos a los vértices $R$ y $S$ del órtico).

En un triángulo, la distancia entre dos excentros (por ejemplo, los excentros opuestos a los vértices $R$ y $S$, es decir, $I_B$ e $I_C$) es:

$$I_B I_C = 4R_{\triangle PRS}\cos\frac{A}{2}$$

donde $A$ es el ángulo en $P$ del triángulo órtico (o más precisamente, la fórmula). Vamos a recordar las fórmulas del triángulo excentral.

Para un triángulo $ABC$ con circunradio $R_t$, su triángulo excentral tiene lados:

- $I_B I_C = 4R_t \cos(A/2)$
- $I_C I_A = 4R_t \cos(B/2)$
- $I_A I_B = 4R_t \cos(C/2)$

donde $I_A, I_B, I_C$ son los excentros opuestos a $A, B, C$.

En nuestro caso, $XYZ$ es el triángulo excentral de $PRS$. Identifiquemos:

- $X = I_A$ (excentro opuesto al vértice $P$ del órtico, es decir, ángulo en $P$)
- $Y = I_B$ (excentro opuesto al vértice $R$)
- $Z = I_C$ (excentro opuesto al vértice $S$)

Entonces:

- $YZ = I_B I_C = 4R_t \cos(A/2)$ donde $A$ es el ángulo en $P$ del triángulo $PRS$.
- $ZX = I_C I_A = 4R_t \cos(B/2)$
- $XY = I_A I_B = 4R_t \cos(C/2)$

También $R_t$ es el circunradio de $PRS$.

Además, la distancia desde el excentro $I_A$ (que es $X$) al lado $BC$ (que es el lado $RS$ del órtico, opuesto a $P$, es decir, lado $a_t = RS$). La distancia desde $I_A$ a $BC$ es el radio exinscrito $r_a$ del triángulo $PRS$, respecto al lado $a_t = RS$.

Recordemos que el exradio $r_a$ está relacionado con la distancia desde el excentro opuesto al lado $a_t$.

En el triángulo $PRS$, el lado opuesto a $P$ es $RS = a_t$. El excentro opuesto a $P$ es $I_A = X$. La distancia desde $I_A$ a la recta $RS$ (que es la recta $BC$) es el exradio $r_a$.

Pero espera, $T$ es el pie de la perpendicular desde $X$ a la recta $RS$, así que $XT$ es exactamente la distancia desde $X = I_A$ a la recta $RS$, es decir, el exradio $r_a$ del triángulo $PRS$.

Por tanto,

$$r_a = XT = 15.$$

El lado $a_t = RS$ es opuesto al vértice $P$ del órtico. La altura desde $P$ al lado $RS$ es la altura del triángulo $PRS$ al lado $a_t$.

Pero también sabemos que $XP$ es la altura del triángulo original $XYZ$ desde $X$ a $YZ$. ¿Cómo se relaciona esto con el triángulo órtico?

Pensemos nuevamente. En el triángulo original $XYZ$, el punto $P$ es el pie de la altura desde $X$ a $YZ$. Y $P$ es un vértice del triángulo órtico. La distancia $XP$ es la distancia desde el excentro $X = I_A$ al vértice $P$ del triángulo $PRS$.

En el triángulo $PRS$, $P$ es el vértice del ángulo $A$. La distancia desde el excentro $I_A$ al vértice $A$ es:

$$I_A A = r_a \csc\frac{A}{2} = \sqrt{\frac{r_a^2}{...}}$$

Recordemos la fórmula: en un triángulo, la distancia desde el excentro $I_A$ al vértice $A$ es:

$$AI_A = \frac{r_a}{\sin(A/2)} = 4R_t \sin\frac{A}{2} \cdot \frac{...}{}$$

Veamos con más cuidado.

En un triángulo $ABC$ con semiperímetro $s_t$, área $K_t$, exradio $r_a = K_t / (s_t - a_t)$.

La distancia desde el vértice $A$ al excentro $I_A$ es:

$$AI_A = \frac{r_a}{\sin(A/2)}.$$

Demostración: el excentro $I_A$ yace sobre la bisectriz del ángulo $A$ (externa, pero sobre la bisectriz interna en realidad el excentro opuesto a $A$ yace sobre la bisectriz interna de $A$). En efecto, $I_A$ está sobre la bisectriz interna de $\angle A$ y sobre las bisectrices externas de $B$ y $C$.

La distancia desde $I_A$ a los lados $AB$ y $AC$ es $r_a$. En el triángulo rectángulo con hipotenusa $AI_A$ y cateto $r_a$ perpendicular al lado, el ángulo en $A$ es $A/2$, así:

$$r_a = AI_A \sin(A/2) \Rightarrow AI_A = \frac{r_a}{\sin(A/2)}.$$

En nuestro caso, $A$ es el ángulo en $P$ del triángulo $PRS$, así que:

$$XP = AI_A = \frac{r_a}{\sin(A/2)}.$$

Datos: $XP = 20$, $r_a = XT = 15$. Por tanto:

$$20 = \frac{15}{\sin(A/2)} \Rightarrow \sin(A/2) = \frac{15}{20} = \frac{3}{4}.$$

Entonces:

$$\cos(A/2) = \sqrt{1 - \left(\frac{3}{4}\right)^2} = \sqrt{1 - \frac{9}{16}} = \sqrt{\frac{7}{16}} = \frac{\sqrt{7}}{4}.$$

Y además tenemos la relación:

$$YZ = I_B I_C = 4R_t \cos(A/2).$$

Con $YZ = 16$:

$$16 = 4R_t \cdot \frac{\sqrt{7}}{4} = R_t \sqrt{7}.$$

Por tanto:

$$R_t = \frac{16}{\sqrt{7}}.$$

### Perímetro del triángulo $PRS$

Necesitamos el perímetro $a_t + b_t + c_t$ del triángulo $PRS$, donde $a_t = RS$.

Sabemos que en un triángulo, $a_t = 2R_t \sin A$. También conocemos $\sin A$ a partir de $\sin(A/2)$ y $\cos(A/2)$:

$$\sin A = 2\sin(A/2)\cos(A/2) = 2 \cdot \frac{3}{4} \cdot \frac{\sqrt{7}}{4} = \frac{3\sqrt{7}}{8}.$$

Entonces:

$$a_t = RS = 2R_t \sin A = 2 \cdot \frac{16}{\sqrt{7}} \cdot \frac{3\sqrt{7}}{8} = \frac{32}{\sqrt{7}} \cdot \frac{3\sqrt{7}}{8} = \frac{32 \cdot 3}{8} = 12.$$

Así que $RS = 12$.

Ahora necesitamos $SP$ y $PR$, es decir, $b_t$ y $c_t$ del triángulo $PRS$.

Sabemos también el área del triángulo $PRS$, o podemos relacionar las alturas.

Recordemos: en el triángulo original $XYZ$, los lados son proporcionales. Podemos encontrar los lados del triángulo original.

El área del triángulo $XYZ$ es $K = 160$. El circunradio de $XYZ$ es $R_{\triangle XYZ}$, con:

$$K = \frac{abc}{4R} \Rightarrow R = \frac{abc}{4K}.$$

Conocemos $a = YZ = 16$, así que $16 = 2R \sin X$, entonces $\sin X = \frac{16}{2R} = \frac{8}{R}$.

También, el ángulo en $X$ del triángulo original se relaciona con el ángulo en el triángulo órtico. En el triángulo órtico, el ángulo en $P$ es:

$$\angle RPS = 180^\circ - 2\angle X.$$

Espera, verifiquemos. En el triángulo órtico $PRS$, el ángulo en $P$ (el vértice que es el pie de la altura desde $X$) es $\pi - 2X$ o algo así.

Recordemos los ángulos del triángulo órtico: 

$$\angle RPS = 180^\circ - 2X, \quad \angle PSR = 180^\circ - 2Y, \quad \angle PRS = 180^\circ - 2Z.$$

Sí, porque en un triángulo acutángulo, los ángulos del triángulo órtico son $\pi - 2X$, $\pi - 2Y$, $\pi - 2Z$.

Por tanto, $A = \angle RPS = 180^\circ - 2X$, donde $X$ denota el ángulo en el vértice $X$ del triángulo original.

Entonces:

$$\sin(A/2) = \sin\left(\frac{180^\circ - 2X}{2}\right) = \sin(90^\circ - X) = \cos X.$$

Entonces:

$$\cos X = \sin(A/2) = \frac{3}{4}.$$

$$\sin X = \sqrt{1 - \cos^2 X} = \sqrt{1 - \frac{9}{16}} = \frac{\sqrt{7}}{4}.$$

Y $A/2 = 90^\circ - X$, entonces $\cos(A/2) = \sin X = \sqrt{7}/4$, lo cual concuerda con lo anterior.

Ahora, con $\sin X = \sqrt{7}/4$ y $a = 16$, el circunradio del triángulo original es:

$$R = \frac{a}{2\sin X} = \frac{16}{2 \cdot \frac{\sqrt{7}}{4}} = \frac{16}{\frac{\sqrt{7}}{2}} = \frac{32}{\sqrt{7}}.$$

Interesante: $R = \frac{32}{\sqrt{7}}$, igual al doble de $R_t = 16/\sqrt{7}$. Tiene sentido: el circunradio del triángulo original es el doble del circunradio del triángulo órtico. De hecho, en un triángulo acutángulo, el circunradio del triángulo original es $2R_t$ del órtico (o el órtico tiene circunradio $R/2$). Efectivamente, el triángulo órtico tiene circunradio $R_{órtico} = R/2$... comprobemos: $R_t = 16/\sqrt{7}$ y $R = 32/\sqrt{7} = 2R_t$. Sí.

Ahora calculemos los otros lados del triángulo original. Conocemos el área $K=160$, el lado $a=16$, y $R = 32/\sqrt{7}$.

Entonces $K = 160 = \frac{abc}{4R}$, así:

$$160 = \frac{16 \cdot b \cdot c}{4 \cdot \frac{32}{\sqrt{7}}} = \frac{16bc}{\frac{128}{\sqrt{7}}} = \frac{16bc \sqrt{7}}{128} = \frac{bc\sqrt{7}}{8}.$$

Entonces:

$$bc = \frac{160 \cdot 8}{\sqrt{7}} = \frac{1280}{\sqrt{7}}.$$

También, por la ley de senos, $b = 2R \sin Y = \frac{64}{\sqrt{7}}\sin Y$, $c = \frac{64}{\sqrt{7}} \sin Z$.

Y $\sin Y \sin Z = bc / (2R)^2 = \frac{1280/\sqrt{7}}{(64/\sqrt{7})^2} = \frac{1280/\sqrt{7}}{4096/7} = \frac{1280 \cdot 7}{\sqrt{7} \cdot 4096} = \frac{8960}{4096\sqrt{7}} = \frac{35}{16\sqrt{7}}$.

Además, $X + Y + Z = 180^\circ$, así $Y + Z = 180^\circ - X$.

$$\sin Y \sin Z = \frac{\cos(Y-Z) - \cos(Y+Z)}{2} = \frac{\cos(Y-Z) - \cos(180^\circ - X)}{2} = \frac{\cos(Y-Z) + \cos X}{2}.$$

Entonces:

$$\frac{\cos(Y-Z) + \frac{3}{4}}{2} = \frac{35}{16\sqrt{7}}.$$

$$\cos(Y-Z) + \frac{3}{4} = \frac{70}{16\sqrt{7}} = \frac{35}{8\sqrt{7}}.$$

Esto se complica. Mejor enfoquemos el perímetro del órtico directamente.

### Perímetro del triángulo órtico

En el triángulo original, $a = YZ = 16$, y sabemos que $RS = a \cos X$ (lado del órtico opuesto al vértice $P$... verifiquemos qué lado corresponde).

El lado del triángulo órtico $RS$ une los pies $R$ y $S$. $R$ está sobre $ZX$ y $S$ sobre $XY$. El segmento $RS$ es opuesto al vértice $P$. 

En un triángulo acutángulo, $RS = a \cos X$ donde $a = YZ$ es el lado opuesto a $X$. Veamos: los pies de las alturas desde $Y$ y $Z$ definen un segmento $RS$ cuya longitud es $a\cos X$.

Efectivamente, hay una fórmula estándar: en el triángulo órtico, 

$$RS = a \cos X, \quad SP = b \cos Y, \quad PR = c \cos Z.$$

Comprobemos con nuestro resultado anterior: $RS = a_t = 12$ y $a = 16$, $\cos X = 3/4$, entonces $a \cos X = 16 \cdot 3/4 = 12$. ¡Coincide!

Por tanto, el perímetro del triángulo $PRS$ es:

$$\text{Perímetro} = a\cos X + b\cos Y + c\cos Z.$$

Necesitamos $b\cos Y$ y $c\cos Z$.

Sabemos que $b = 2R\sin Y$, $c=2R\sin Z$, con $R = 32/\sqrt{7}$.

Entonces:

$$b\cos Y = 2R \sin Y \cos Y = R \sin 2Y.$$
$$c\cos Z = R \sin 2Z.$$

El perímetro total:

$$\Pi = a\cos X + R(\sin 2Y + \sin 2Z).$$

También sabemos que $Y + Z = 180^\circ - X$, y $X$ está determinado por $\cos X = 3/4$, $\sin X = \sqrt{7}/4$.

$$\sin 2Y + \sin 2Z = 2\sin(Y+Z)\cos(Y-Z) = 2\sin(180^\circ - X)\cos(Y-Z) = 2\sin X \cos(Y-Z).$$

Entonces:

$$\Pi = a\cos X + 2R\sin X \cos(Y-Z).$$

Sustituyendo $a = 16$, $\cos X = 3/4$: $a\cos X = 12$.

$2R \sin X = 2 \cdot \frac{32}{\sqrt{7}} \cdot \frac{\sqrt{7}}{4} = \frac{64}{4} = 16$.

Entonces:

$$\Pi = 12 + 16 \cos(Y-Z).$$

Necesitamos $\cos(Y-Z)$.

### Encontrar $\cos(Y-Z)$

Usemos el área y las relaciones. Sabemos que el área $K$ de $XYZ$ con lados $a=16$, $b$, $c$ y ángulos $Y, Z$:

$$K = \frac{1}{2}ab \sin ... $$

Mejor usemos la ley de cosenos para involucrar $b$ y $c$.

Recordemos la relación de $\cos(Y-Z)$ con los lados. Hay una fórmula para el área o para las diferencias angulares.

También podemos usar que $XP = 20$ ya lo usamos... en realidad $XP$ nos dio $\cos X = 3/4$, y $XT$ nos dio $r_a=15$ que ya usamos para $\sin(A/2)$.

Espera, veamos si falta usar algo más. Tenemos dos datos numéricos: $XT=15$ y $XP=20$ (además de $YZ=16$). Con $XT=15$ y $XP=20$ obtuvimos $\sin(A/2)=3/4$, lo que nos dio $\cos X = 3/4$ y $\sin X = \sqrt{7}/4$. Con $YZ=16$ obtuvimos $RS = a\cos X = 12$.

¿Y la altura $XP = 20$? La usamos para obtener $\sin(A/2)$. ¿Pero también debería darnos otra relación? Veamos: $XP$ es la distancia desde $X$ (excentro $I_A$) al vértice $P$ (vértice $A$ del órtico). Ya usamos $XP = r_a / \sin(A/2)$ para sacar $\sin(A/2)$. Eso determinó $A$, y por tanto $\cos X = \sin(A/2) = 3/4$. Bien.

Sin embargo, necesitamos más información para determinar $\cos(Y-Z)$, es decir, la forma completa del triángulo. Pero quizá el perímetro del triángulo órtico se puede expresar solo en términos del área y los datos dados.

Veamos: el área del triángulo $XYZ$ es $K = 160$, ¿y cómo se relaciona con el perímetro del órtico?

El área del triángulo órtico $PRS$ está relacionada con el área del original: $K_{órtico} = 2K \cos X \cos Y \cos Z$ (fórmula conocida). Hmm, o quizá el semiperímetro.

Hay otra fórmula: el perímetro del triángulo órtico es:

$$\text{Perímetro}_{órtico} = \frac{4K}{R} \cdot \frac{...}{}$$

Busquemos una relación más directa.

Sabemos que $RS = a\cos X$, $SP = b\cos Y$, $PR = c\cos Z$.

El semiperímetro del órtico:

$$s_{órtico} = \frac{a\cos X + b\cos Y + c\cos Z}{2}.$$

Hay una fórmula: en un triángulo acutángulo, el perímetro del triángulo órtico es $4R \sin X \sin Y \sin Z \cdot (\cot X + \cot Y + \cot Z)$... vamos a verificarlo.

$RS = a \cos X = 2R \sin X \cos X$.
$SP = b \cos Y = 2R \sin Y \cos Y$.
$PR = c \cos Z = 2R \sin Z \cos Z$.

Perímetro:

$$\Pi = 2R (\sin X \cos X + \sin Y \cos Y + \sin Z \cos Z).$$

$$= R (\sin 2X + \sin 2Y + \sin 2Z).$$

Para un triángulo con $X+Y+Z = 180^\circ$, hay una identidad:

$$\sin 2X + \sin 2Y + \sin 2Z = 4 \sin X \sin Y \sin Z.$$

Verifiquemos: $\sin 2X + \sin 2Y + \sin 2Z = 4\sin X \sin Y \sin Z$ para $X+Y+Z=\pi$. Sí, es una identidad conocida.

Por tanto:

$$\Pi = R \cdot 4 \sin X \sin Y \sin Z = 4R \sin X \sin Y \sin Z.$$

Como $R = 32/\sqrt{7}$, $\sin X = \sqrt{7}/4$:

$$\Pi = 4 \cdot \frac{32}{\sqrt{7}} \cdot \frac{\sqrt{7}}{4} \cdot \sin Y \sin Z = 32 \sin Y \sin Z.$$

Anteriormente encontramos:

$$\sin Y \sin Z = \frac{35}{16\sqrt{7}}.$$

Entonces:

$$\Pi = 32 \cdot \frac{35}{16\sqrt{7}} = \frac{32 \cdot 35}{16\sqrt{7}} = \frac{1120}{16\sqrt{7}} = \frac{70}{\sqrt{7}} = 10\sqrt{7}.$$

Verifiquemos: $70/\sqrt{7} = 10\sqrt{7}$. Sí.

Por tanto, el perímetro del triángulo $PRS$ es:

$$\Pi = 10\sqrt{7}.$$

### Verificación

Comprobemos la coherencia. 

Tenemos $RS = 12$, y el perímetro total $10\sqrt{7} \approx 26.46$. Entonces $SP + PR = 10\sqrt{7} - 12 \approx 14.46$.

$SP = b\cos Y$, $PR = c\cos Z$.

Verifiquemos que todo es consistente con $bc = 1280/\sqrt{7}$.

Sabemos que $b = 2R\sin Y = \frac{64}{\sqrt{7}}\sin Y$, $c = \frac{64}{\sqrt{7}}\sin Z$.

Entonces $b c = \frac{4096}{7}\sin Y \sin Z = \frac{4096}{7} \cdot \frac{35}{16\sqrt{7}} = \frac{4096 \cdot 35}{7 \cdot 16 \sqrt{7}} = \frac{256 \cdot 35}{7\sqrt{7}} = \frac{8960}{7\sqrt{7}} = \frac{1280}{\sqrt{7}}$. Coincide con lo anterior. Bien.

Ahora, $\sin Y \sin Z = 35/(16\sqrt{7}) \approx 0.827$... espera, $35/(16 \cdot 2.64575) = 35/42.33 \approx 0.827$. Eso está bien, aunque el producto máximo de dos senos se daría si $Y=Z=45^\circ$ con producto $0.5$, pero aquí es $0.827$, lo cual es posible solo si... hmm, espera. $\sin Y \sin Z \le 1$, y $0.827$ está bien, pero recordemos que $Y$ y $Z$ son ángulos de un triángulo con $Y+Z = 180^\circ - X$.

Con $\cos X = 3/4$, $\sin X = \sqrt{7}/4 \approx 0.6614$, entonces $X \approx 41.4^\circ$. $Y + Z \approx 138.6^\circ$.

$\sin Y \sin Z = [\cos(Y-Z) - \cos(Y+Z)]/2 = [\cos(Y-Z) - \cos 138.6^\circ]/2$.

$\cos 138.6^\circ = -\cos 41.4^\circ = -0.75$.

Entonces $\sin Y \sin Z = [\cos(Y-Z) + 0.75]/2$.

Igualando a $35/(16\sqrt{7}) \approx 0.827$:

$$\cos(Y-Z) + 0.75 = 2 \cdot 0.827 = 1.654$$

$$\cos(Y-Z) = 0.904.$$

Eso es posible. Por ejemplo, $Y-Z \approx 25.3^\circ$. Bien.

Ahora verifiquemos $XT$ y $XP$ desde esta configuración para asegurarnos.

Ya usamos $XP$ y $XT$ para derivar $\sin(A/2) = 3/4$ y por tanto $\cos X = 3/4$. Y $YZ = 16$ nos dio $R_t$.

Déjame verificar directamente la distancia $XT$ desde $X$ a $RS$ usando coordenadas o la fórmula del exradio.

En el triángulo $PRS$, el lado $a_t = RS = 12$, y el exradio $r_a = 15$. El semiperímetro $s_t = \Pi/2 = 5\sqrt{7} \approx 13.23$.

El área del triángulo $PRS$ está relacionada con $r_a$:

$$r_a = \frac{K_t}{s_t - a_t}.$$

Por tanto:

$$K_t = r_a(s_t - a_t) = 15 \left(5\sqrt{7} - 12\right).$$

$5\sqrt{7} \approx 13.23$, así $s_t - a_t \approx 1.23$, y $K_t \approx 18.48$.

Por otro lado, el área del triángulo $PRS$ (órtico) está relacionada con el área del original $K=160$ por $K_t = 2K \cos X \cos Y \cos Z$ ... pero también podemos calcular $K_t$ directamente con la fórmula de Herón o con $K_t = 2R_t^2 \sin A \sin B \sin C$ (para el triángulo $PRS$).

Calculemos $K_t$ con $R_t = 16/\sqrt{7}$:

Los ángulos del triángulo $PRS$: $A = 180^\circ - 2X \approx 97.2^\circ$, $B = 180^\circ - 2Y$, $C = 180^\circ - 2Z$.

$\sin A = \sin(180^\circ - 2X) = \sin 2X = 2\sin X \cos X = 2 \cdot \frac{\sqrt{7}}{4} \cdot \frac{3}{4} = \frac{3\sqrt{7}}{8} \approx 0.992$. 

Entonces $K_t = 2R_t^2 \sin A \sin B \sin C = 2 \cdot \frac{256}{7} \cdot \frac{3\sqrt{7}}{8} \cdot \sin B \sin C$.

$\sin B \sin C = \sin(180^\circ-2Y)\sin(180^\circ-2Z) = \sin 2Y \sin 2Z = 4\sin Y \cos Y \sin Z \cos Z = 4 \sin Y \sin Z \cos Y \cos Z$.

Esto se complica, pero confiamos en la coherencia anterior. Usemos Herón directamente con el perímetro y los lados.

Tenemos $a_t = RS = 12$, $\Pi = 10\sqrt{7} \approx 26.4575$, $s_t = 5\sqrt{7} \approx 13.2288$.

Los otros lados: $b_t = SP = ?$ y $c_t = PR = ?$. Sabemos $b_t + c_t = 10\sqrt{7} - 12 \approx 14.4575$.

También, en un triángulo, $a_t + b_t + c_t = 2s_t$.

Con Herón: $K_t^2 = s_t(s_t-a_t)(s_t-b_t)(s_t-c_t)$.

Pero no conocemos $b_t$ y $c_t$ separadamente. Sin embargo, podemos usar que $b_t = b\cos Y$ y $c_t = c\cos Z$ del original, y el producto $b_t c_t$.

$b_t c_t = b c \cos Y \cos Z = \frac{1280}{\sqrt{7}} \cos Y \cos Z$.

Necesitamos $\cos Y \cos Z$. Usando $Y + Z = 180^\circ - X$:

$$\cos Y \cos Z = \frac{\cos(Y+Z) + \cos(Y-Z)}{2} = \frac{\cos(180^\circ - X) + \cos(Y-Z)}{2} = \frac{-\cos X + \cos(Y-Z)}{2}.$$

$\cos X = 3/4$, $\cos(Y-Z) \approx 0.904$.

$$\cos Y \cos Z = \frac{-0.75 + 0.904}{2} \approx 0.077.$$

Entonces $b_t c_t \approx \frac{1280}{2.64575} \cdot 0.077 \approx 483.8 \cdot 0.077 \approx 37.25$.

Y $b_t + c_t \approx 14.4575$. 

Comprobemos Herón: $s_t - a_t = 5\sqrt{7} - 12 \approx 1.2288$.

$s_t - b_t$ y $s_t - c_t$: si $b_t \approx c_t \approx 7.23$ (producto 37.25 implica $b_t \approx 6.1$ y $c_t \approx 6.1$? En realidad $\sqrt{37.25} \approx 6.1$, y $b_t + c_t = 14.46$, así $b_t$ y $c_t$ no son simétricos).

Sea $b_t \approx 4.5$, $c_t \approx 9.96$. Entonces $s_t - b_t \approx 8.73$, $s_t - c_t \approx 3.27$.

$K_t^2 = 13.23 \cdot 1.23 \cdot 8.73 \cdot 3.27 \approx 13.23 \cdot 1.23 = 16.27$, $\cdot 8.73 = 142.1$, $\cdot 3.27 \approx 464.7$. Entonces $K_t \approx 21.56$.

Por otro lado, $K_t$ también se puede obtener del triángulo original: $K_t = 2K\cos X \cos Y \cos Z$ (fórmula estándar para el área del triángulo órtico). Aquí $K = 160$, $\cos X = 0.75$, $\cos Y\cos Z \approx 0.077$, así $K_t \approx 2 \cdot 160 \cdot 0.75 \cdot 0.077 \approx 18.48$. Hay una discrepancia de aproximadamente 21.56 vs 18.48, probablemente por mis aproximaciones groseras de $\cos(Y-Z)$.

Verifiquemos la fórmula exacta. La fórmula del área del triángulo órtico en un triángulo acutángulo es:

$$K_{órtico} = 2K \cos X \cos Y \cos Z.$$

Sí, es una fórmula estándar.

Calculemos $\cos(Y-Z)$ exactamente.

Recordemos que encontramos:

$$\sin Y \sin Z = \frac{35}{16\sqrt{7}}.$$

Y 

$$\cos Y \cos Z = \frac{-\cos X + \cos(Y-Z)}{2} = \frac{-3/4 + \cos(Y-Z)}{2}.$$

También:

$$\sin Y \sin Z = \frac{\cos(Y-Z) - \cos(Y+Z)}{2} = \frac{\cos(Y-Z) + \cos X}{2} = \frac{\cos(Y-Z) + 3/4}{2} = \frac{35}{16\sqrt{7}}.$$

Entonces:

$$\cos(Y-Z) = \frac{70}{16\sqrt{7}} - \frac{3}{4} = \frac{35}{8\sqrt{7}} - \frac{3}{4}.$$

Racionalicemos:

$$\frac{35}{8\sqrt{7}} = \frac{35\sqrt{7}}{56} = \frac{5\sqrt{7}}{8}.$$

Entonces:

$$\cos(Y-Z) = \frac{5\sqrt{7}}{8} - \frac{3}{4} = \frac{5\sqrt{7} - 6}{8}.$$

Entonces:

$$\cos Y \cos Z = \frac{-3/4 + \frac{5\sqrt{7}-6}{8}}{2} = \frac{\frac{-6}{8} + \frac{5\sqrt{7}-6}{8}}{2} = \frac{5\sqrt{7} - 12}{16}.$$

Por tanto:

$$K_t = 2K \cos X \cos Y \cos Z = 2 \cdot 160 \cdot \frac{3}{4} \cdot \frac{5\sqrt{7}-12}{16} = 320 \cdot \frac{3}{4} \cdot \frac{5\sqrt{7}-12}{16} = 240 \cdot \frac{5\sqrt{7}-12}{16} = 15(5\sqrt{7}-12).$$

¡Que es exactamente lo que obtuvimos del exradio!

$$K_t = 15(5\sqrt{7} - 12) \approx 15(13.228 - 12) = 15 \cdot 1.228 \approx 18.43.$$

Bien, mi aproximación anterior de 18.48 era correcta. El problema era la aproximación de Herón, que no es consistente con los lados exactos. Verifiquemos con los lados exactos.

Tenemos $b_t = SP = b \cos Y$ y $c_t = PR = c \cos Z$.

$b = 2R \sin Y = \frac{64}{\sqrt{7}}\sin Y$.
$c = \frac{64}{\sqrt{7}}\sin Z$.

Necesitamos valores exactos de $\sin Y$ y $\cos Y$, etc. Dado que solo conocemos $\sin Y\sin Z$ y $\cos Y\cos Z$, no conocemos los valores individuales, y de hecho el triángulo no está completamente determinado por los datos... pero el perímetro sí está bien definido, como calculamos.

Verifiquemos el perímetro con la fórmula del exradio y el área.

Tenemos $K_t = 15(5\sqrt{7}-12)$, $r_a = 15$, $a_t = 12$, $s_t = \Pi/2$.

Sabemos $r_a = K_t/(s_t - a_t)$, así $s_t - a_t = K_t / r_a = 15(5\sqrt{7}-12)/15 = 5\sqrt{7}-12$.

Entonces $s_t = a_t + 5\sqrt{7} - 12 = 12 + 5\sqrt{7} - 12 = 5\sqrt{7}$.

Por tanto $\Pi = 2s_t = 10\sqrt{7}$.

¡Perfecto, todo consistente!

### Conclusión

El perímetro del triángulo $PRS$ es $10\sqrt{7}$.

Final answer:

$$\boxed{10\sqrt{7}}$$