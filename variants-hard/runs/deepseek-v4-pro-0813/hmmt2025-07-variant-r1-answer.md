

Vamos a resolver el problema paso a paso.

**Paso 1: Plantear las igualdades.**

Nos dan:

\[
3(x^2+1)=4(y^2+1)=5(z^2+1).
\]

Llamemos \(k\) a este valor común:

\[
3(x^2+1)=4(y^2+1)=5(z^2+1)=k.
\]

Entonces:

\[
x^2+1=\frac{k}{3},\qquad y^2+1=\frac{k}{4},\qquad z^2+1=\frac{k}{5}.
\]

De aquí:

\[
x^2=\frac{k}{3}-1,\qquad y^2=\frac{k}{4}-1,\qquad z^2=\frac{k}{5}-1.
\]

Puesto que \(x,y,z>0\), podemos despejar:

\[
x=\sqrt{\frac{k}{3}-1},\qquad y=\sqrt{\frac{k}{4}-1},\qquad z=\sqrt{\frac{k}{5}-1}.
\]

Para que estas raíces sean reales y positivas necesitamos:

\[
\frac{k}{3}>1,\quad \frac{k}{4}>1,\quad \frac{k}{5}>1,
\]

o sea:

\[
k>3,\quad k>4,\quad k>5.
\]

Por tanto, la condición más restrictiva es:

\[
k>5.
\]

**Paso 2: Usar la segunda condición.**

Nos dicen:

\[
xy+yz+zx=1.
\]

Sustituimos:

\[
\sqrt{\frac{k}{3}-1}\sqrt{\frac{k}{4}-1}
+\sqrt{\frac{k}{4}-1}\sqrt{\frac{k}{5}-1}
+\sqrt{\frac{k}{5}-1}\sqrt{\frac{k}{3}-1}=1.
\]

No resulta cómodo de resolver directamente. Vamos a hacer un cambio de variable para simplificar.

**Paso 3: Cambio de variable.**

Observemos que:

\[
\frac{k}{3}-1=\frac{k-3}{3},\qquad
\frac{k}{4}-1=\frac{k-4}{4},\qquad
\frac{k}{5}-1=\frac{k-5}{5}.
\]

Entonces:

\[
x=\sqrt{\frac{k-3}{3}},\qquad
y=\sqrt{\frac{k-4}{4}},\qquad
z=\sqrt{\frac{k-5}{5}}.
\]

Definamos:

\[
a=\sqrt{k-3},\qquad b=\sqrt{k-4},\qquad c=\sqrt{k-5}.
\]

Entonces:

\[
x=\frac{a}{\sqrt{3}},\qquad y=\frac{b}{\sqrt{4}}=\frac{b}{2},\qquad z=\frac{c}{\sqrt{5}}.
\]

Además, como \(a^2=k-3\), \(b^2=k-4\), \(c^2=k-5\), se cumple:

\[
a^2-b^2=1,\qquad b^2-c^2=1,\qquad a^2-c^2=2.
\]

La condición \(xy+yz+zx=1\) queda:

\[
\frac{a}{\sqrt{3}}\cdot \frac{b}{2}
+\frac{b}{2}\cdot \frac{c}{\sqrt{5}}
+\frac{c}{\sqrt{5}}\cdot \frac{a}{\sqrt{3}}
=1.
\]

Multiplicando por \(2\sqrt{3}\sqrt{5}\):

\[
\sqrt{5}\,ab+\sqrt{3}\,bc+2\,ca=2\sqrt{15}.
\]

**Paso 4: Relaciones entre \(a,b,c\).**

Ya vimos que:

\[
a^2=b^2+1,\qquad c^2=b^2-1.
\]

Entonces:

\[
a=\sqrt{b^2+1},\qquad c=\sqrt{b^2-1}.
\]

Estas dos restricciones dependen solo de \(b\), así que sustituimos en la ecuación anterior:

\[
\sqrt{5}\,b\,a+\sqrt{3}\,b\,c+2\,c\,a=2\sqrt{15},
\]

es decir:

\[
\sqrt{5}\,b\sqrt{b^2+1}
+\sqrt{3}\,b\sqrt{b^2-1}
+2\sqrt{b^2+1}\sqrt{b^2-1}
=2\sqrt{15}.
\]

Esta ecuación parece complicada, pero se puede resolver haciendo otro cambio de variable.

**Paso 5: Cambio trigonométrico/hiperbólico.**

Observemos que \(b^2-1>0\) porque \(b=\sqrt{k-4}\) y \(k>5\), por lo que \(b>1\).

Usemos relaciones de tipo hiperbólico: como

\[
a^2-b^2=1,
\]

podemos escribir:

\[
a=\cosh u,\qquad b=\sinh u.
\]

De hecho, \(a^2-b^2=\cosh^2 u-\sinh^2 u=1\).

Además, como \(b^2-c^2=1\), podemos escribir:

\[
b=\cosh v,\qquad c=\sinh v.
\]

Igualamos las dos expresiones para \(b\):

\[
\sinh u=\cosh v.
\]

Esta relación no es inmediata, pero podemos usar que \(\cosh v=\sinh u\) implica \(v\) y \(u\) relacionados. En efecto:

\[
\cosh v=\sinh u
\]

equivale a:

\[
\sinh^2 u-\cosh^2 v=0.
\]

Como \(\cosh^2 v-\sinh^2 v=1\), no sé si es la vía más limpia. Probemos otro enfoque.

**Paso 6: Otro enfoque: resolver directamente en \(k\).**

Tenemos:

\[
x=\sqrt{\frac{k-3}{3}},\qquad
y=\sqrt{\frac{k-4}{4}},\qquad
z=\sqrt{\frac{k-5}{5}}.
\]

La condición \(xy+yz+zx=1\) da:

\[
\sqrt{\frac{k-3}{3}}\sqrt{\frac{k-4}{4}}
+\sqrt{\frac{k-4}{4}}\sqrt{\frac{k-5}{5}}
+\sqrt{\frac{k-5}{5}}\sqrt{\frac{k-3}{3}}
=1.
\]

Elevar al cuadrado no es inmediato. Podemos intentar adivinar un valor razonable de \(k\).

**Paso 7: Buscar una solución razonable.**

Si la solución es única y el problema pide \(x+y+z\), probablemente \(k\) sea un valor agradable. Probemos con valores enteros de \(k>5\).

- Si \(k=6\):

  \[
  x=\sqrt{\frac{3}{3}}=1,\qquad
  y=\sqrt{\frac{2}{4}}=\frac{\sqrt{2}}{2},\qquad
  z=\sqrt{\frac{1}{5}}=\frac{1}{\sqrt{5}}.
  \]

  Entonces:

  \[
  xy+yz+zx
  =1\cdot \frac{\sqrt{2}}{2}
  +\frac{\sqrt{2}}{2}\cdot \frac{1}{\sqrt{5}}
  +\frac{1}{\sqrt{5}}\cdot 1.
  \]

  Esto no vale \(1\) en general. Calculemos numéricamente:

  \[
  xy\approx 0{,}7071,\quad yz\approx 0{,}3162,\quad zx\approx 0{,}4472,
  \]

  así que:

  \[
  xy+yz+zx\approx 1{,}4705\neq 1.
  \]

  Demasiado grande.

- Si \(k=6{,}5\):

  \[
  x=\sqrt{\frac{3{,}5}{3}}\approx\sqrt{1{,}1667}\approx 1{,}0801,
  \]
  \[
  y=\sqrt{\frac{2{,}5}{4}}=\sqrt{0{,}625}\approx 0{,}7906,
  \]
  \[
  z=\sqrt{\frac{1{,}5}{5}}=\sqrt{0{,}3}\approx 0{,}5477.
  \]

  Entonces:

  \[
  xy\approx 0{,}8539,\quad yz\approx 0{,}4330,\quad zx\approx 0{,}5916.
  \]

  Suma:

  \[
  xy+yz+zx\approx 1{,}8785.
  \]

  ¡Ha aumentado! Eso es raro. Esperaríamos que para \(k\) mayor, \(x,y,z\) crecieran y por tanto la suma creciera. En \(k=6\) dio \(1{,}4705\) y en \(k=6{,}5\) dio \(1{,}8785\). Si la tendencia es creciente, nunca llegaremos a \(1\) para \(k>5\). Eso sugiere que quizá la elección del valor común \(k\) no debe ser mayor que \(5\) para todos, o que hay algo mal.

Pero espera: para \(k=6\), \(z=\sqrt{1/5}\approx 0{,}447\), positiva, y todo bien. La suma \(xy+yz+zx\) en \(k=6\) es \(1{,}47\), no \(1\). Para \(k=6{,}5\) es \(1{,}88\), mayor. Entonces no parece que haya un \(k>5\) con la suma igual a \(1\). Esto indica que el problema quizá tiene solución con otro signo o hay que considerar \(k\) tal que alguna raíz sea imaginaria y luego se recombinen.

Pero el enunciado dice que existe exactamente una terna de reales positivos. Entonces debe haber una solución con \(k>5\). ¿Quizá mi numeración está mal?

Revisemos \(k=6\):

\[
x^2+1=2,\quad y^2+1=1{,}5,\quad z^2+1=1{,}2.
\]

Entonces:

\[
x^2=1,\quad y^2=0{,}5,\quad z^2=0{,}2.
\]

Así:

\[
x=1,\quad y=\sqrt{0{,}5}\approx 0{,}7071,\quad z=\sqrt{0{,}2}\approx 0{,}4472.
\]

Entonces:

\[
xy\approx 0{,}7071,\quad yz\approx 0{,}3162,\quad zx\approx 0{,}4472.
\]

Suma:

\[
\approx 1{,}4705.
\]

Eso es correcto.

Parece que para \(k=6\) la suma es \(1{,}47\), y para \(k\) grande tenderá a grande. Quizá la suma no es monótona; pero en los dos valores probados creció. Tal vez hay un mínimo y después crece. De hecho, \(x,y,z\) crecen con \(k\), así que \(xy+yz+zx\) también crece y es creciente, al menos en cada término. Veamos: ¿es realmente creciente?

\[
x=\sqrt{\frac{k-3}{3}}.
\]

Sí, creciente en \(k\). Lo mismo \(y,z\). Entonces \(xy,yz,zx\) son crecientes por ser producto de funciones positivas crecientes. Por tanto la suma es estrictamente creciente para \(k>5\). En \(k\to 5^+\), veamos los límites:

\[
x\to\sqrt{\frac{2}{3}}\approx 0{,}8165,\quad
y\to\sqrt{\frac{1}{4}}=0{,}5,\quad
z\to 0.
\]

Entonces:

\[
xy\to 0{,}4082,\quad yz\to 0,\quad zx\to 0.
\]

Suma límite: \(0{,}4082\). En \(k=6\) es \(1{,}47\) y crece. Entonces la suma varía desde \(0{,}4082\) hasta \(\infty\) de forma continua y estrictamente creciente. Entonces habrá un único \(k>5\) con suma \(1\). ¡Perfecto! Mi valor en \(k=6\) era \(1{,}47>1\), así que la solución está con \(5<k<6\).

**Paso 8: Buscar la solución numérica.**

Sabemos que en \(k=5\) la suma tiende a \(0{,}4082\) y en \(k=6\) es \(1{,}4705\). Queremos suma \(1\). Por continuidad, hay un \(k\in(5,6)\). Probemos \(k=5{,}5\):

\[
x=\sqrt{\frac{2{,}5}{3}}=\sqrt{0{,}8333}\approx 0{,}9129,
\]
\[
y=\sqrt{\frac{1{,}5}{4}}=\sqrt{0{,}375}\approx 0{,}6124,
\]
\[
z=\sqrt{\frac{0{,}5}{5}}=\sqrt{0{,}1}\approx 0{,}3162.
\]

Entonces:

\[
xy\approx 0{,}5590,\quad yz\approx 0{,}1936,\quad zx\approx 0{,}2887.
\]

Suma:

\[
\approx 1{,}0413.
\]

Todavía un poco mayor que \(1\).

Probemos \(k=5{,}4\):

\[
x=\sqrt{\frac{2{,}4}{3}}=\sqrt{0{,}8}\approx 0{,}8944,
\]
\[
y=\sqrt{\frac{1{,}4}{4}}=\sqrt{0{,}35}\approx 0{,}5916,
\]
\[
z=\sqrt{\frac{0{,}4}{5}}=\sqrt{0{,}08}\approx 0{,}2828.
\]

Entonces:

\[
xy\approx 0{,}5292,\quad yz\approx 0{,}1673,\quad zx\approx 0{,}2530.
\]

Suma:

\[
\approx 0{,}9495.
\]

Ahora está por debajo de \(1\). Entonces la solución está entre \(5{,}4\) y \(5{,}5\).

Probemos \(k=5{,}44\):

\[
x=\sqrt{\frac{2{,}44}{3}}=\sqrt{0{,}81333}\approx 0{,}9019,
\]
\[
y=\sqrt{\frac{1{,}44}{4}}=\sqrt{0{,}36}=0{,}6,
\]
\[
z=\sqrt{\frac{0{,}44}{5}}=\sqrt{0{,}088}\approx 0{,}2966.
\]

Entonces:

\[
xy\approx 0{,}5411,\quad yz\approx 0{,}1780,\quad zx\approx 0{,}2675.
\]

Suma:

\[
\approx 0{,}9866.
\]

Todavía menos que \(1\).

Probemos \(k=5{,}45\):

\[
x=\sqrt{\frac{2{,}45}{3}}=\sqrt{0{,}81667}\approx 0{,}9037,
\]
\[
y=\sqrt{\frac{1{,}45}{4}}=\sqrt{0{,}3625}\approx 0{,}6021,
\]
\[
z=\sqrt{\frac{0{,}45}{5}}=\sqrt{0{,}09}=0{,}3.
\]

Entonces:

\[
xy\approx 0{,}5441,\quad yz\approx 0{,}1806,\quad zx\approx 0{,}2711.
\]

Suma:

\[
\approx 0{,}9958.
\]

Muy cerca de \(1\), un poco menos.

Probemos \(k=5{,}455\):

\[
x=\sqrt{\frac{2{,}455}{3}}=\sqrt{0{,}81833}\approx 0{,}9046,
\]
\[
y=\sqrt{\frac{1{,}455}{4}}=\sqrt{0{,}36375}\approx 0{,}6031,
\]
\[
z=\sqrt{\frac{0{,}455}{5}}=\sqrt{0{,}091}\approx 0{,}3017.
\]

Entonces:

\[
xy\approx 0{,}5456,\quad yz\approx 0{,}1820,\quad zx\approx 0{,}2729.
\]

Suma:

\[
\approx 1{,}0005.
\]

Muy cerca de \(1\). Parece que \(k\approx 5{,}454\).

**Paso 9: Hallar \(x+y+z\).**

Con \(k\approx 5{,}454\):

\[
x\approx 0{,}904,\quad y\approx 0{,}603,\quad z\approx 0{,}301.
\]

Entonces:

\[
x+y+z\approx 0{,}904+0{,}603+0{,}301=1{,}808.
\]

Pero esto es aproximado. El problema pide un valor exacto. Probemos a buscar una solución racional o algebraica agradable.

**Paso 10: Buscar una solución exacta.**

Quizá la solución tiene \(k\) racional y \(x,y,z\) agradables. Observemos que si \(z=1/3\), entonces:

\[
z^2=\frac{1}{9}.
\]

De:

\[
z^2+1=\frac{k}{5},
\]

tendríamos:

\[
\frac{10}{9}=\frac{k}{5}\implies k=\frac{50}{9}\approx 5{,}5556.
\]

Luego:

\[
x^2+1=\frac{k}{3}=\frac{50}{27},
\]

\[
x^2=\frac{50}{27}-1=\frac{23}{27},
\]

\[
y^2+1=\frac{k}{4}=\frac{50}{36}=\frac{25}{18},
\]

\[
y^2=\frac{25}{18}-1=\frac{7}{18}.
\]

Comprobemos \(xy+yz+zx\):

\[
x=\sqrt{\frac{23}{27}},\quad y=\sqrt{\frac{7}{18}},\quad z=\frac{1}{3}.
\]

No parece que dé \(1\) exactamente.

Probemos \(z=1/4\). Entonces \(z^2=\frac{1}{16}\),

\[
z^2+1=\frac{17}{16}=\frac{k}{5}\implies k=\frac{85}{16}=5{,}3125.
\]

Luego:

\[
x=\sqrt{\frac{k-3}{3}}=\sqrt{\frac{85/16-3}{3}}
=\sqrt{\frac{85/16-48/16}{3}}
=\sqrt{\frac{37/16}{3}}
=\sqrt{\frac{37}{48}},
\]

\[
y=\sqrt{\frac{k-4}{4}}=\sqrt{\frac{85/16-4}{4}}
=\sqrt{\frac{85/16-64/16}{4}}
=\sqrt{\frac{21/16}{4}}
=\sqrt{\frac{21}{64}}
=\frac{\sqrt{21}}{8}.
\]

No parece agradable.

Probemos \(k=\frac{23}{4}=5{,}75\). Entonces:

\[
x^2+1=\frac{23/4}{3}=\frac{23}{12},
\]

\[
x^2=\frac{23}{12}-1=\frac{11}{12},
\]

\[
y^2+1=\frac{23/4}{4}=\frac{23}{16},
\]

\[
y^2=\frac{23}{16}-1=\frac{7}{16},
\]

\[
z^2+1=\frac{23/4}{5}=\frac{23}{20},
\]

\[
z^2=\frac{23}{20}-1=\frac{3}{20}.
\]

Esto da:

\[
x=\sqrt{\frac{11}{12}},\quad y=\frac{\sqrt{7}}{4},\quad z=\sqrt{\frac{3}{20}}.
\]

Probemos la suma de productos:

\[
xy=\sqrt{\frac{11}{12}}\cdot \frac{\sqrt{7}}{4}
=\frac{\sqrt{77}}{4\sqrt{12}}
=\frac{\sqrt{77}}{8\sqrt{3}},
\]

\[
yz=\frac{\sqrt{7}}{4}\cdot \sqrt{\frac{3}{20}}
=\frac{\sqrt{21}}{4\sqrt{20}}
=\frac{\sqrt{21}}{8\sqrt{5}},
\]

\[
zx=\sqrt{\frac{3}{20}}\cdot \sqrt{\frac{11}{12}}
=\frac{\sqrt{33}}{\sqrt{240}}
=\frac{\sqrt{33}}{4\sqrt{15}}.
\]

No parece que sume \(1\).

Probemos \(z=\frac{1}{\sqrt{5}}=\frac{\sqrt{5}}{5}\approx 0{,}4472\). Este es el caso \(k=6\), que ya vimos da \(1{,}47\), no sirve.

**Paso 11: Buscar una solución con radicales agradables.**

Quizá \(k=5{,}45\ldots\) no tiene forma cerrada simple, y el problema espera una respuesta numérica. Pero el enunciado sugiere que hay una única terna y pide \(x+y+z\). Tal vez la solución sea \(x+y+z=\frac{3\sqrt{3}}{2}\) o algo así.

En \(k\approx 5{,}454\), tenemos \(x+y+z\approx 1{,}808\). Veamos si \(\sqrt{3}\approx 1{,}732\), \(\frac{3\sqrt{3}}{2}\approx 2{,}598\), \(1+\frac{\sqrt{3}}{2}\approx 1{,}866\). Nada obvio.

Probemos encontrar una solución exacta probando con \(x,y,z\) racionales.

**Paso 12: Suponer que \(x,y,z\) son racionales.**

Si \(x,y,z\) son racionales positivos, entonces de:

\[
3(x^2+1)=4(y^2+1)=5(z^2+1)=k,
\]

tenemos que \(k\) es racional y:

\[
x^2=\frac{k}{3}-1,\quad y^2=\frac{k}{4}-1,\quad z^2=\frac{k}{5}-1.
\]

Para que \(x,y,z\) sean racionales, necesitamos que \(\frac{k}{3}-1\), \(\frac{k}{4}-1\), \(\frac{k}{5}-1\) sean cuadrados racionales. Probemos \(x=1\). Ya vimos \(k=6\), no sirve.

Probemos \(x=\frac{1}{2}\). Entonces:

\[
x^2=\frac{1}{4}.
\]

\[
\frac{k}{3}-1=\frac{1}{4}\implies \frac{k}{3}=\frac{5}{4}\implies k=\frac{15}{4}=3{,}75.
\]

Pero \(k<5\), lo cual no permite \(z\) real positivo. Descartado.

Probemos \(x=2\). Entonces:

\[
x^2=4,\quad \frac{k}{3}-1=4\implies \frac{k}{3}=5\implies k=15.
\]

Entonces:

\[
y^2+1=\frac{15}{4}\implies y^2=\frac{11}{4},
\]

\[
z^2+1=\frac{15}{5}=3\implies z^2=2.
\]

Así \(y=\frac{\sqrt{11}}{2}\), \(z=\sqrt{2}\). La suma \(xy+yz+zx\) no da \(1\) seguramente.

Probemos \(y=\frac{1}{2}\). Entonces:

\[
y^2=\frac{1}{4},\quad \frac{k}{4}-1=\frac{1}{4}\implies \frac{k}{4}=\frac{5}{4}\implies k=5.
\]

Pero \(k=5\) da \(z=0\), no positiva. Descartado.

Probemos \(y=1\). Entonces:

\[
y^2=1,\quad \frac{k}{4}-1=1\implies \frac{k}{4}=2\implies k=8.
\]

Entonces:

\[
x^2+1=\frac{8}{3}\implies x^2=\frac{5}{3},
\]

\[
z^2+1=\frac{8}{5}\implies z^2=\frac{3}{5}.
\]

Así:

\[
x=\sqrt{\frac{5}{3}},\quad y=1,\quad z=\sqrt{\frac{3}{5}}.
\]

Calculemos \(xy+yz+zx\):

\[
xy=\sqrt{\frac{5}{3}},\quad
yz=\sqrt{\frac{3}{5}},\quad
zx=\sqrt{\frac{3}{5}}\cdot \sqrt{\frac{5}{3}}=1.
\]

Entonces:

\[
xy+yz+zx=\sqrt{\frac{5}{3}}+\sqrt{\frac{3}{5}}+1
=\frac{\sqrt{15}}{3}+\frac{\sqrt{15}}{5}+1
=\sqrt{15}\left(\frac{1}{3}+\frac{1}{5}\right)+1
=\sqrt{15}\cdot \frac{8}{15}+1
=\frac{8\sqrt{15}}{15}+1.
\]

Esto no es \(1\). Descartado.

**Paso 13: Probar \(z=\frac{1}{3}\).**

Ya lo probamos y no dio.

**Paso 14: Tal vez \(x,y,z\) no son racionales, pero la suma sí tiene forma cerrada.**

Volvamos a la ecuación:

\[
\sqrt{5}\,b\sqrt{b^2+1}
+\sqrt{3}\,b\sqrt{b^2-1}
+2\sqrt{b^2+1}\sqrt{b^2-1}
=2\sqrt{15}.
\]

Quizá convenga elevar al cuadrado de forma inteligente o usar otra sustitución. Recordemos que:

\[
a=\sqrt{b^2+1},\qquad c=\sqrt{b^2-1}.
\]

Entonces la condición es:

\[
\sqrt{5}\,ab+\sqrt{3}\,bc+2\,ca=2\sqrt{15}.
\]

Además:

\[
a^2-b^2=1,\qquad b^2-c^2=1.
\]

De estas dos, obtenemos:

\[
a^2-c^2=2.
\]

También:

\[
a^2=b^2+1,\qquad c^2=b^2-1.
\]

Multiplicando:

\[
a^2c^2=(b^2+1)(b^2-1)=b^4-1.
\]

No parece simplificar mucho.

**Paso 15: Probar la sustitución \(u=b^2\).**

Sea \(u=b^2>1\). Entonces:

\[
a=\sqrt{u+1},\qquad c=\sqrt{u-1}.
\]

La condición queda:

\[
\sqrt{5}\,\sqrt{u+1}\,\sqrt{u}
+\sqrt{3}\,\sqrt{u}\,\sqrt{u-1}
+2\sqrt{u+1}\sqrt{u-1}
=2\sqrt{15}.
\]

Es decir:

\[
\sqrt{5u(u+1)}+\sqrt{3u(u-1)}+2\sqrt{u^2-1}
=2\sqrt{15}.
\]

Esta ecuación podría resolverse numéricamente, pero no veo una forma cerrada simple.

**Paso 16: ¿Quizá hay un error en el planteamiento?**

Releamos el enunciado:

\[
3(x^2+1)=4(y^2+1)=5(z^2+1)
\]

y

\[
xy+yz+zx=1.
\]

Tal vez el valor común no es \(k\) sino que hay un factor. Pero mi planteamiento es correcto.

**Paso 17: Resolver numéricamente con precisión.**

Ya sabemos \(k\approx 5{,}454\). Calculemos con más precisión.

Sea \(F(k)=xy+yz+zx-1\).

Para \(k=5{,}45\), \(F\approx 0{,}99584-1=-0{,}00416\).

Para \(k=5{,}455\), \(F\approx 1{,}0005-1=0{,}0005\).

Interpolando, la raíz está cerca de \(5{,}4545\).

Calculemos \(k=5{,}4545\):

\[
x=\sqrt{\frac{2{,}4545}{3}}=\sqrt{0{,}8181667}.
\]

Calculemos con más precisión usando aproximaciones:

\[
x^2=0{,}8181667,\quad x\approx 0{,}90453.
\]

\[
y^2=\frac{1{,}4545}{4}=0{,}363625,\quad y\approx 0{,}60301.
\]

\[
z^2=\frac{0{,}4545}{5}=0{,}0909,\quad z\approx 0{,}30150.
\]

Entonces:

\[
xy\approx 0{,}90453\cdot 0{,}60301\approx 0{,}54544,
\]
\[
yz\approx 0{,}60301\cdot 0{,}30150\approx 0{,}18181,
\]
\[
zx\approx 0{,}30150\cdot 0{,}90453\approx 0{,}27273.
\]

Suma:

\[
\approx 0{,}54544+0{,}18181+0{,}27273=1{,}0000.
\]

¡Muy bien! Entonces \(k\approx 5{,}4545\).

Ahora:

\[
x+y+z\approx 0{,}90453+0{,}60301+0{,}30150=1{,}80904.
\]

**Paso 18: Buscar una expresión exacta.**

Observemos que los valores aproximados son:

\[
x\approx 0{,}9045,\quad y\approx 0{,}6030,\quad z\approx 0{,}3015.
\]

Notemos que:

\[
0{,}9045^2\approx 0{,}8182,\quad
0{,}6030^2\approx 0{,}3636,\quad
0{,}3015^2\approx 0{,}0909.
\]

Parece que \(z\approx \frac{3}{10}\)? No exactamente, \(z\approx 0{,}3015\), \(\frac{3}{10}=0{,}3\).

Veamos si \(z=\frac{3}{10}=0{,}3\). Entonces \(z^2=0{,}09\),

\[
z^2+1=1{,}09=\frac{109}{100}.
\]

Entonces:

\[
\frac{k}{5}=\frac{109}{100}\implies k=\frac{109}{20}=5{,}45.
\]

¡Ajá! \(k=5{,}45\) es un valor racional agradable.

Entonces:

\[
x^2+1=\frac{k}{3}=\frac{109/20}{3}=\frac{109}{60},
\]

\[
x^2=\frac{109}{60}-1=\frac{49}{60},
\]

\[
y^2+1=\frac{k}{4}=\frac{109/20}{4}=\frac{109}{80},
\]

\[
y^2=\frac{109}{80}-1=\frac{29}{80}.
\]

Y como \(z=\frac{3}{10}\), \(z^2=\frac{9}{100}\).

Comprobemos \(xy+yz+zx\):

\[
x=\sqrt{\frac{49}{60}}=\frac{7}{\sqrt{60}}=\frac{7}{2\sqrt{15}},
\]

\[
y=\sqrt{\frac{29}{80}}=\frac{\sqrt{29}}{4\sqrt{5}}.
\]

Entonces:

\[
xy=\frac{7}{2\sqrt{15}}\cdot \frac{\sqrt{29}}{4\sqrt{5}}
=\frac{7\sqrt{29}}{8\sqrt{75}}
=\frac{7\sqrt{29}}{8\cdot 5\sqrt{3}}
=\frac{7\sqrt{29}}{40\sqrt{3}},
\]

\[
yz=\frac{\sqrt{29}}{4\sqrt{5}}\cdot \frac{3}{10}
=\frac{3\sqrt{29}}{40\sqrt{5}},
\]

\[
zx=\frac{3}{10}\cdot \frac{7}{2\sqrt{15}}
=\frac{21}{20\sqrt{15}}.
\]

Esto no parece simplificar a \(1\). Entonces \(z=\frac{3}{10}\) no es la solución exacta, aunque \(k=5{,}45\) es cercano.

**Paso 19: ¿Quizá la solución exacta tiene \(z=\frac{1}{\sqrt{11}}\) o algo así?**

Probemos \(z=\frac{1}{\sqrt{11}}\). Entonces \(z^2=\frac{1}{11}\),

\[
z^2+1=\frac{12}{11}=\frac{k}{5}\implies k=\frac{60}{11}\approx 5{,}4545.
\]

¡Este \(k\) se parece mucho a nuestro valor numérico! \(60/11=5{,}454545\ldots\)

Entonces con \(z=\frac{1}{\sqrt{11}}\):

\[
x^2+1=\frac{k}{3}=\frac{60/11}{3}=\frac{20}{11},
\]

\[
x^2=\frac{20}{11}-1=\frac{9}{11},
\]

\[
y^2+1=\frac{k}{4}=\frac{60/11}{4}=\frac{15}{11},
\]

\[
y^2=\frac{15}{11}-1=\frac{4}{11}.
\]

¡Excelente! Entonces:

\[
x=\sqrt{\frac{9}{11}}=\frac{3}{\sqrt{11}},
\]

\[
y=\sqrt{\frac{4}{11}}=\frac{2}{\sqrt{11}},
\]

\[
z=\frac{1}{\sqrt{11}}.
\]

¡Perfecto! Ahora comprobemos \(xy+yz+zx\):

\[
xy=\frac{3}{\sqrt{11}}\cdot \frac{2}{\sqrt{11}}=\frac{6}{11},
\]

\[
yz=\frac{2}{\sqrt{11}}\cdot \frac{1}{\sqrt{11}}=\frac{2}{11},
\]

\[
zx=\frac{1}{\sqrt{11}}\cdot \frac{3}{\sqrt{11}}=\frac{3}{11}.
\]

Suma:

\[
xy+yz+zx=\frac{6+2+3}{11}=\frac{11}{11}=1.
\]

¡Funciona!

Verifiquemos también las igualdades originales:

\[
x^2+1=\frac{9}{11}+1=\frac{20}{11},
\]

\[
y^2+1=\frac{4}{11}+1=\frac{15}{11},
\]

\[
z^2+1=\frac{1}{11}+1=\frac{12}{11}.
\]

Entonces:

\[
3(x^2+1)=3\cdot \frac{20}{11}=\frac{60}{11},
\]

\[
4(y^2+1)=4\cdot \frac{15}{11}=\frac{60}{11},
\]

\[
5(z^2+1)=5\cdot \frac{12}{11}=\frac{60}{11}.
\]

Todos iguales. ¡La terna es:

\[
x=\frac{3}{\sqrt{11}},\qquad y=\frac{2}{\sqrt{11}},\qquad z=\frac{1}{\sqrt{11}}.
\]

**Paso 20: Calcular \(x+y+z\).**

\[
x+y+z=\frac{3}{\sqrt{11}}+\frac{2}{\sqrt{11}}+\frac{1}{\sqrt{11}}
=\frac{6}{\sqrt{11}}
=\frac{6\sqrt{11}}{11}.
\]

Por tanto:

\[
\boxed{\frac{6\sqrt{11}}{11}}
\]

Esa es la respuesta final.