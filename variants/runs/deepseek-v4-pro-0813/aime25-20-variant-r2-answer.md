## Solución

**1. Identificar el círculo.** Como \(D,E,F\) son los puntos medios de los lados, el circuncírculo de \(\triangle DEF\) es el **círculo de nueve puntos** de \(\triangle PQR\). Sus segundas intersecciones con los lados \(QR, PR, PQ\) son los pies de las alturas:

\[
G=\text{pie desde }P,\qquad H=\text{pie desde }Q,\qquad J=\text{pie desde }R.
\]

**2. Colocar el triángulo.** Tomemos el circuncírculo de \(PQR\) con radio \(1\) y centro \(O\). Convenientemente ponemos

\[
Q=0^\circ,\quad R=160^\circ,\quad P=-84^\circ,
\]

pues los arcos son \(\widehat{QR}=2\cdot 80^\circ=160^\circ\), \(\widehat{RP}=2\cdot 58^\circ=116^\circ\), \(\widehat{PQ}=2\cdot 42^\circ=84^\circ\).

**3. Posiciones de los puntos medios.** Si \(X\) es el ortocentro y el centro del círculo de nueve puntos es \(N=\frac{O+X}{2}=\frac{P+Q+R}{2}\), entonces

\[
D-N=\frac{Q+R}{2}-\frac{P+Q+R}{2}=-\frac{P}{2},\quad
E-N=-\frac{Q}{2},\quad
F-N=-\frac{R}{2}.
\]

Luego sus ángulos en el círculo de nueve puntos son:

\[
D: 96^\circ,\qquad E: 180^\circ,\qquad F: 340^\circ.
\]

**4. Posiciones de los pies de las alturas.** El pie de la altura desde \(P\) es el punto medio entre \(X\) y \(P_{\text{alt}}\), la segunda intersección de la altura con el circuncírculo; por tanto \(G-N=\frac{P_{\text{alt}}}{2}\), y el ángulo de \(G\) es el de \(P_{\text{alt}}\).

La cuerda \(QR\) tiene dirección \(170^\circ\), así que la altura desde \(P\) tiene dirección \(80^\circ\). La cuerda \(P P_{\text{alt}}\) tiene entonces punto medio en \(170^\circ\); como \(P=-84^\circ\),

\[
P_{\text{alt}}=2\cdot 170^\circ-(-84^\circ)=424^\circ\equiv 64^\circ
\quad\Rightarrow\quad G=64^\circ.
\]

Análogamente:

\[
Q_{\text{alt}}=256^\circ\Rightarrow H=256^\circ,\qquad
R_{\text{alt}}=296^\circ\Rightarrow J=296^\circ.
\]

**5. Orden y arcos menores.** En el círculo de nueve puntos, en orden creciente:

\[
G(64^\circ),\ D(96^\circ),\ E(180^\circ),\ H(256^\circ),\ J(296^\circ),\ F(340^\circ).
\]

Los seis arcos menores consecutivos son

\[
\widehat{GD}=32^\circ,\quad \widehat{DE}=84^\circ,\quad \widehat{EH}=76^\circ,\quad
\widehat{HJ}=40^\circ,\quad \widehat{JF}=44^\circ,\quad \widehat{FG}=84^\circ.
\]

**6. Cálculo final.**

\[
\widehat{DE}+2\widehat{HJ}+3\widehat{FG}
=84^\circ+2(40^\circ)+3(84^\circ)
=84^\circ+80^\circ+252^\circ
=416^\circ.
\]

\[
\boxed{416}
\]

<thinking>
El problema es de geometría. Triángulo PQR con ángulos en P=80°, Q=58°, R=42°. D, E, F son puntos medios de QR, PR, PQ respectivamente. El triángulo DEF es el triángulo medial, similar a PQR. Circuncírculo de DEF (círculo de los nueve puntos de PQR). Se intersecta con QD, PE, PF nuevamente en G, H, J respectivamente.

Necesito encontrar la suma de arcos en el circuncírculo de DEF: arco DE + 2·arco HJ + 3·arco FG.

Primero, entiendo la configuración. D es punto medio de QR, E de PR, F de PQ.

Como D, E, F son puntos medios, DE es paralelo a PQ (segmento medio), EF paralelo a QR, DF paralelo a PR. Así el triángulo DEF tiene ángulos: en D igual al ángulo en P = 80°, en E igual al ángulo en Q = 58°, en F igual al ángulo en R = 42°. Espera, verifiquemos:

- DE es paralelo a PQ, DF paralelo a PR. Entonces el ángulo en D (entre DE y DF) es el ángulo entre PQ y PR = ángulo en P = 80°. Correcto.
- En E: entre DE (paralelo PQ) y EF (paralelo QR) = ángulo entre PQ y QR = ángulo en Q = 58°.
- En F: entre DF (paralelo PR) y EF (paralelo QR) = ángulo entre PR y QR = ángulo en R = 42°.

Entonces el circuncírculo de DEF tiene arcos correspondientes.

Los puntos G, H, J están sobre las cevianas QD, PE, PF (medianas del triángulo original) y vuelven a intersecar el circuncírculo de DEF.

Necesito calcular los arcos. Hay que determinar las posiciones relativas de estos puntos en el círculo.

Primero, ubiquemos coordenadas o usemos teoría de ángulos.

El circuncírculo de DEF. Los arcos menores entre los puntos consecutivos. Los seis puntos dividen el círculo en seis arcos menores. Necesitamos arco DE (el arco menor entre D y E), arco HJ, arco FG. Pero cuidado: estos arcos ¿son consecutivos? Los puntos en orden en el círculo serían... necesitamos determinar el orden.

Los seis puntos: D, E, F y G, H, J donde G está en QD, H en PE, J en PF. G está sobre el rayo de D hacia Q (o el segmento QD - "meets QD again" significa la recta QD interseca el círculo en D y G). Entonces G está en la línea QD pasando por D. Similar H en PE (línea PE), J en PF.

Necesitamos el orden circular de estos puntos. Probablemente el orden sea D, H, E, ..., etc. Vamos a calcular.

Puedo usar la propiedad del círculo de nueve puntos. El círculo de DEF es el círculo de nueve puntos del triángulo PQR. Contiene los puntos medios de los lados (D, E, F), los pies de las alturas, y los puntos medios de los segmentos desde vértices al ortocentro.

Los puntos G, H, J son las segundas intersecciones de las medianas con el círculo de nueve puntos.

Espera: las medianas van de Q a D, de P a E, de P a F. Pero D es punto medio de QR, E de PR, F de PQ. Las medianas: QD conecta Q con el punto medio D de PR... espera D es punto medio de QR. La mediana desde Q es Q a punto medio de PR, que es E, no D. Hmm.

D es punto medio de QR, E de PR, F de PQ.
- Mediana desde Q: conecta Q con punto medio de PR = E. Entonces QE es mediana. Pero el problema dice "meets QD" - QD es la recta Q a D. D es el punto medio de QR, así que QD está sobre el lado QR (ya que D está en QR). Entonces QD es el segmento desde Q al punto medio de QR, que está en el lado QR. Esa no es una mediana; es parte del lado QR. Hmm pero el lado QR contiene a Q y R.

Espera: D es punto medio de QR. Entonces QD es la mitad del lado QR, sobre el lado QR. Entonces la recta QD es la recta QR (el lado). La segunda intersección del circuncírculo de DEF con la recta QR (lado) sería... D está en QR y en el círculo. La recta QR intersecta el círculo en D y otro punto G. Entonces G es el otro punto de intersección del lado QR con el círculo de nueve puntos.

Similar: PE - E es punto medio de PR, entonces PE está sobre el lado PR, la segunda intersección H está sobre PR. PF está sobre el lado PQ, J sobre PQ.

Así G está en QR, H en PR, J en PQ. Vamos a ver: el círculo de nueve puntos interseca los lados en los puntos medios y en los pies de las alturas (porque el círculo de nueve puntos pasa por los pies de las alturas). En efecto, la segunda intersección del lado QR con el círculo de nueve puntos es el pie de la altura desde P sobre QR. Por lo tanto:

- G es el pie de la altura desde P sobre QR.
- H es el pie de la altura desde Q sobre PR.
- J es el pie de la altura desde R sobre PQ.

Espera, H está en PE (lado PR) y es el pie de la altura desde Q sobre PR. J está en PQ y es el pie de la altura desde R sobre PQ.

Esto es clave: G, H, J son los pies de las alturas del triángulo PQR.

Entonces el círculo de DEF (círculo de nueve puntos) contiene a D, E, F (puntos medios) y a los pies de las alturas G, H, J.

Ahora necesitamos los arcos entre estos seis puntos y calcular la suma.

El círculo de nueve puntos es la imagen del circuncírculo de PQR por homotecia de centro el ortocentro O (llamémoslo X) con factor 1/2. El triángulo DEF es homotético al triángulo PQR con centro el baricentro y factor -1/2. Pero para el círculo de nueve puntos la relación es con el ortocentro.

Mejor calcular los ángulos directamente.

La posición de un punto en el círculo de nueve puntos: los pies de alturas y puntos medios tienen posiciones conocidas en términos de ángulos.

El circuncírculo de DEF (círculo de nueve puntos) tiene los seis puntos en secuencia. Tradicionalmente, en el triángulo, el círculo de nueve puntos contiene:
- puntos medios de los lados
- pies de las alturas
- puntos medios entre ortocentro y vértices.

Existe un orden. Vamos a determinar los ángulos de los arcos.

Sea el triángulo PQR. Usemos la notación: P es el vértice con ángulo 80° (en P), Q con 58°, R con 42°.

Los pies de alturas: G = pie desde P sobre QR, H = pie desde Q sobre PR, J = pie desde R sobre PQ.

Necesito las posiciones en el círculo de nueve puntos.

Alternativa: calculamos explícitamente con coordenadas.

Tomemos un sistema de coordenadas. Podemos colocar el triángulo con P en el origen quizá, o usar el circuncírculo.

Mejor usar el círculo unitario y los ángulos.

Vamos a elegir coordenadas convenientes.

Coloquemos el triángulo PQR de forma que P esté en la parte superior, etc. Usemos el circuncírculo de PQR. Pero ya que el círculo de nueve puntos es homotético con centro en el ortocentro, las posiciones angulares podrían heredarse.

Enfoque con el circuncírculo de PQR de radio R = 1 (o 2), centrado en el origen. Los vértices P, Q, R en ángulos θ_P, θ_Q, θ_R. Los arcos del circuncírculo: arco QR = 2·ángulo P = 160°, arco RP = 2·ángulo Q = 116°, arco PQ = 2·ángulo R = 84°.

Entonces si colocamos P, Q, R en el círculo unitario, los arcos entre ellos son 84°, 116°, 160°. Podemos asignar posiciones:
- Coloquemos Q en ángulo 0°, R en ángulo 160° (arco QR = 160°). Espera, el arco menor QR correspondiente al ángulo P=80° es 160°. Entonces Q y R separados por 160°.
- P está en algún ángulo tal que arco RP = 116° y arco PQ = 84°. Si Q=0°, R=160°. El arco de R a P: 116°, entonces P puede estar en 160°+116° = 276° (o -84°). Arco de P a Q: de 276° a 360°/0° = 84°. Correcto.

Entonces:
- Q: 0°
- R: 160°
- P: 276° = -84°

Arcos: PQ = 84° (de P=-84° a Q=0°), QR=160° (Q=0° a R=160°), RP=116° (R=160° a P=276°).

Total 360°, correcto.

Ahora, ¿el círculo de nueve puntos? Es el círculo que pasa por los puntos medios D, E, F. Podemos calcular el centro y radio.

O usemos el hecho: el círculo de nueve puntos tiene centro en el punto medio del segmento entre el circuncentro y el ortocentro. Su radio es R/2.

Calculemos las coordenadas de los seis puntos y luego los arcos.

Tomemos circuncírculo unitario (R=1). Vértices:
P = (cos(-84°), sin(-84°)) = (cos 84°, -sin 84°).
Q = (1, 0).
R = (cos 160°, sin 160°) = (-cos 20°, sin 20°) ya que cos160=-cos20, sin160=sin20. cos20≈0.9397, sin20≈0.3420. Entonces R ≈ (-0.9397, 0.3420).

P = (cos 84°, -sin 84°) ≈ (0.1045, -0.9945).

Puntos medios:
D = punto medio de QR = (Q+R)/2 = ((1 + cos160)/2, (0 + sin160)/2) = ((1 - cos20)/2, sin20/2).
E = punto medio de PR = (P+R)/2 = ((cos84 + cos160)/2, (-sin84 + sin160)/2).
F = punto medio de PQ = (P+Q)/2 = ((cos84+1)/2, (-sin84)/2).

Pies de alturas:
G = pie de la altura desde P sobre QR.
H = pie desde Q sobre PR.
J = pie desde R sobre PQ.

Podemos calcular las coordenadas de los pies de alturas.

Mejor usar fórmulas con ángulos en el circuncírculo. Hay una técnica.

Alternativamente, podemos usar que el círculo de nueve puntos está centrado en el punto medio entre O (circuncentro) y X (ortocentro). Con R=1, radio = 1/2.

En un triángulo, las coordenadas de los pies de alturas en el círculo de nueve puntos... Hay una forma elegante usando el circuncírculo: el pie de altura desde P está a mitad de camino entre P y un punto relacionado con la reflexión de X sobre QR.

Quizá mejor hacerlo vía trigonometría esférica / ángulos.

Vamos a parametrizar el círculo de nueve puntos. El círculo de nueve puntos es homotético al circuncírculo con centro X (ortocentro) y razón 1/2. En esta homotecia, cada punto A del circuncírculo va a (A + X)/2. En particular, los vértices P, Q, R van a los puntos medios entre X y P, Q, R. Los puntos D, E, F son las imágenes de... Espera, bajo la homotecia de centro X y factor 1/2, la imagen del vértice P es (X+P)/2 = punto medio de XP. No es D (punto medio de QR). Entonces no directamente.

Pero la propiedad clave: el círculo de nueve puntos es la imagen del circuncírculo por homotecia de centro X (ortocentro), razón 1/2. Entonces la imagen de P es el punto medio de XP (que está en el círculo de nueve puntos), y este es un punto que llamaré P'. Similar Q' y R'. Los puntos medios D, E, F también están en este círculo.

Entonces el círculo de nueve puntos contiene: D, E, F, G, H, J, P', Q', R'.

Los ángulos en el círculo de nueve puntos: la homotecia preserva los ángulos centrales, es decir, la posición angular de la imagen es la misma que la del punto original (el centro de homotecia no cambia los ángulos respecto al centro original; la imagen del circuncírculo es el círculo de nueve puntos con centro N = (O+X)/2; los ángulos desde N son iguales a los ángulos desde O del punto original, porque la homotecia es central con centro X: si A está a ángulo α desde O, su imagen A'=(A+X)/2 está a ángulo α desde N=(O+X)/2, ya que A - O = 2(A'-N). Entonces los ángulos se preservan).

Por lo tanto, en el círculo de nueve puntos:
- P' está en el mismo ángulo que P (desde el centro del círculo de nueve puntos).
- Q' en ángulo de Q.
- R' en ángulo de R.

Los arcos entre P', Q', R' en el círculo de nueve puntos son los mismos ángulos centrales: arco P'Q' = 84° (menor), Q'R' = 160°, R'P' = 116°.

Ahora, ¿dónde están D, E, F y G, H, J en este círculo de nueve puntos, en relación con los ángulos?

D es el punto medio de QR. Su posición: en el circuncírculo original, el punto medio del arco QR (no confundir con punto medio del segmento). La imagen por homotecia de centro X del punto del circuncírculo que es... Hmm, D no es imagen de un punto del circuncírculo bajo homotecia X,1/2 necesariamente. D es el punto medio del segmento QR.

Existe una relación: en el círculo de nueve puntos, el punto D está en el ángulo de... Vamos a ver.

Usemos la propiedad: el centro del círculo de nueve puntos es N. Los ángulos desde N de los puntos medios.

Calculemos directamente con coordenadas, eligiendo el centro de nueve puntos como origen. Eso simplifica: el centro del círculo de nueve puntos N = (O + X)/2. Si tomamos N como origen, los puntos P', Q', R' están en ángulos iguales a los de P, Q, R respecto a O.

Pero D, E, F son puntos medios de lados. ¿Sus ángulos desde N?

Podemos usar el hecho de que en el triángulo, los ángulos en D, E, F son conocidos, y el radio del círculo de nueve puntos es 1/2.

Mejor aún: calculemos las posiciones angulares usando el teorema: la distancia desde el centro hasta cada punto es igual (radio 1/2) y las cuerdas entre ellos determinan los arcos.

Vamos a calcular los ángulos centrales (desde N) entre los seis puntos.

Primero, notemos que el triángulo DEF es similar a PQR (medial). En el círculo de nueve puntos, las cuerdas DE, EF, FD corresponden a lados paralelos a PQ, QR, RP. El arco menor DE (en el círculo de nueve puntos) corresponde al ángulo central subtendido por la cuerda DE.

El ángulo inscrito que subtiende el arco DE es el ángulo en F (o en cualquier punto del arco mayor). El ángulo en F del triángulo DEF es 42° (ángulo entre DF y EF, que es igual al ángulo R = 42°). Entonces el arco DE (el arco que no contiene a F) = 2·42° = 84°. Espera, el ángulo inscrito ∠DFE = 42° subtiende el arco DE que no contiene a F. Entonces el arco DE menor = 84°. Eso es consistente con arco PQ en el circuncírculo = 84°. De hecho el círculo de nueve puntos es homotético al circuncírculo por razón 1/2, pero los ángulos centrales son iguales. El arco DE en el círculo de nueve puntos = arco P'Q' = 84°? Hmm, D y E no son P' y Q'.

Espera, ¿D y E corresponden a qué? D es punto medio de QR, E de PR, F de PQ.

En el círculo de nueve puntos, los puntos medios D, E, F. El ángulo en F (∠DFE) = 42° = ángulo en R. Entonces el arco DE (que no contiene a F) = 84°. El arco DE = 84°, coincide con arco PQ del circuncírculo (el arco correspondiente al vértice opuesto). En general, el arco DE en el círculo de nueve puntos corresponde al arco entre los puntos medios de QR y PR. Dado que D, E están en los lados QR y PR, y E-D es paralelo a PQ, la cuerda DE es paralela a PQ. En el circuncírculo, el arco PQ = 84°. Por homotecia, el arco DE en el círculo de nueve puntos también es 84° (ya que DE es la imagen homotética de PQ bajo homotecia de centro R, factor 1/2, pero el ángulo central depende del centro N...).

Verifiquemos con la homotecia: La imagen del circuncírculo por homotecia X,1/2 es el círculo de nueve puntos. Bajo esta homotecia, la cuerda PQ (del circuncírculo) va a la cuerda P'Q' (que une puntos medios de XP y XQ). P'Q' no es DE. Entonces no.

Sin embargo, los ángulos centrales del círculo de nueve puntos entre D y E: podemos derivarlos.

Consideremos la homotecia con centro R y factor 1/2: envía Q→D (punto medio de RQ), P→F? No: envía Q a punto medio de RQ = D, envía P a punto medio de RP = E. Entonces esta homotecia envía la cuerda PQ a la cuerda DE. La homotecia de centro R, factor 1/2 mapea el circuncírculo de PQR a un círculo que pasa por D, E, F (centro a mitad entre R y O). Ese círculo es el círculo de nueve puntos. Sí, porque D, E, F son imágenes de Q, P, R? Espera: bajo homotecia centro R factor 1/2: R→R (no, R queda fijo, así que imagen de R es R mismo, no F). Los vértices: Q→D, P→E, R→R. Entonces el círculo por D, E, R. Pero el círculo de nueve puntos pasa por D, E, F, no R. Hmm.

Pensemos de nuevo: la homotecia centro R factor 1/2 mapea el circuncírculo (que pasa por P, Q, R) a un círculo que pasa por E (img P), D (img Q), y R (img R). Ese círculo tiene centro (O+R)/2 y radio R/2. ¿Es este el círculo de nueve puntos? El círculo de nueve puntos tiene centro (O+X)/2, no (O+R)/2. Entonces no.

Pero observemos que el círculo centrado en (O+R)/2 con radio 1/2 pasa por D, E y R. Y el círculo de nueve puntos pasa por D, E y F. Son círculos distintos.

Sin embargo, la cuerda DE es la misma en ambos y es paralela a PQ. El ángulo central entre D y E en el círculo de nueve puntos: podemos usar trigonometría.

Vamos a calcular mediante coordenadas explícitas. Es lo más seguro.

Elijo el sistema con N (centro del círculo de nueve puntos) como origen, radio 1/2. Entonces los puntos están en ángulos φ. Los seis puntos D, E, F, G, H, J.

Para calcular los ángulos φ, uso coordenadas en el circuncírculo unitario y la transformación al círculo de nueve puntos.

Sea O = origen (0,0), circunradio 1. Sea X = ortocentro. N = X/2 (porque O=0). El círculo de nueve puntos centrado en N = X/2 con radio 1/2.

Cualquier punto A en el circuncírculo unitario mapea a A' = (A + X)/2 en el círculo de nueve puntos (esto para los puntos P', Q', R'). Pero D, E, F son puntos medios de lados; no son imágenes de vértices bajo homotecia X.

Para los pies de alturas G, H, J, estos son puntos del circuncírculo? No, están en los lados.

Calculemos directamente las coordenadas de todos los puntos en el sistema del circuncírculo y luego restamos N y normalizamos para hallar ángulos respecto a N.

Primero calculemos el ortocentro X para nuestro triángulo en el circuncírculo unitario.

Para un triángulo en el circuncírculo unitario con vectores p, q, r, el ortocentro es x = p + q + r (convención: si el centro es O, ortocentro = p+q+r). Para triángulo acutángulo, sí.

Calculemos:
p = (cos 84°, -sin 84°) = (c4, -s4) donde c4 = cos 84° ≈ 0.104528, s4 = sin 84° ≈ 0.994522.
q = (1, 0).
r = (cos 160°, sin 160°) = (-cos 20°, sin 20°) = (-c2, s2) con c2 = cos 20° ≈ 0.939693, s2 = sin 20° ≈ 0.342020.

x = p + q + r = (c4 + 1 - c2, -s4 + s2).

c4 = 0.104528, 1 - c2 = 1 - 0.939693 = 0.060307. Suma x-coord = 0.104528 + 0.060307 = 0.164835.
y = -0.994522 + 0.342020 = -0.652502.

Entonces X ≈ (0.164835, -0.652502). N = X/2 ≈ (0.0824175, -0.326251).

Puntos medios:
D = (q + r)/2 = (1 - c2, s2)/2 = (0.060307/2, 0.342020/2) = (0.0301535, 0.171010).
E = (p + r)/2 = (c4 - c2, -s4 + s2)/2 = (0.104528 - 0.939693, -0.994522+0.342020)/2 = (-0.835165, -0.652502)/2 = (-0.4175825, -0.326251).
F = (p + q)/2 = (c4 + 1, -s4)/2 = (1.104528, -0.994522)/2 = (0.552264, -0.497261).

Fíjate: E = (-0.4175825, -0.326251). N = (0.0824175, -0.326251). Vector E - N = (-0.5, 0). Entonces E está exactamente a la izquierda de N, distancia 0.5, ángulo 180°. ¡Interesante! E - N = (-0.5, 0). Exacto en teoría: E debería estar en ángulo 180°.

Verifiquemos: E = (p+r)/2. N = (p+q+r)/4. E - N = (p+r)/2 - (p+q+r)/4 = (2p + 2r - p - q - r)/4 = (p - q + r)/4. Hmm, con nuestros números salió (-0.5, 0) — depende.

Calculemos exactamente los vectores desde N con los valores:
E - N = (-0.4175825 - 0.0824175, -0.326251 - (-0.326251)) = (-0.5, 0). Correcto.

D - N = (0.0301535 - 0.0824175, 0.171010 - (-0.326251)) = (-0.052264, 0.497261). Distancia: sqrt(0.052264² + 0.497261²). 0.497261² ≈ 0.247268, 0.052264² ≈ 0.002732. Suma ≈ 0.25. Exacto, radio 0.5.

F - N = (0.552264 - 0.0824175, -0.497261 - (-0.326251)) = (0.4698465, -0.171010). Distancia 0.5.

Entonces los ángulos de D, E, F desde N:

E: ángulo 180°.

D: vector (-0.052264, 0.497261). Ángulo: atan2(0.497261, -0.052264) = 180° - arctan(0.497261/0.052264). 0.497261/0.052264 ≈ 9.515. arctan(9.515) ≈ 84°. Entonces ángulo ≈ 180° - 84° = 96°.

F: vector (0.4698465, -0.171010). Ángulo: atan2(-0.171010, 0.4698465) = -20° (o 340°). 0.171010/0.4698465 ≈ 0.36397 = tan 20°. Entonces ángulo ≈ -20° = 340°.

Entonces:
- E: 180°
- D: 96°
- F: 340° (=-20°)

Ahora calculemos G, H, J (pies de alturas).

G es el pie de la altura desde P sobre QR. La altura desde P es perpendicular a QR.

Podemos calcular la proyección de p sobre la recta QR.

La recta QR pasa por q=(1,0) y r=(-c2, s2). Vector director u = r - q = (-c2 - 1, s2) = (-(1+c2), s2).

El pie de la altura G es la proyección ortogonal de p sobre la recta q + t u.

Alternativamente, existe fórmula: el pie de altura desde P en el circuncírculo unitario: G = (q + r + p - ...). Mejor use proyección.

También en el círculo de nueve puntos, los pies de alturas G, H, J son las imágenes bajo homotecia X,1/2 de los puntos del circuncírculo? No. Pero existe una relación: el pie de altura desde P es el punto medio entre X y el punto A del circuncírculo donde la recta XP vuelve a encontrar... Hmm.

Recordemos: el pie de la altura desde P sobre QR es la reflexión de X sobre QR. Más precisamente, la reflexión de X sobre QR está en el circuncírculo (es el punto del circuncírculo opuesto donde la altura desde P reencuentra el circuncírculo). Entonces si reflejamos X sobre QR obtenemos un punto P_alt del circuncírculo, y G es el punto medio entre X y P_alt. Por tanto G es imagen por homotecia X,1/2 de P_alt (un punto del circuncírculo). Entonces G está en el círculo de nueve puntos y su ángulo desde N es el ángulo de P_alt.

Entonces los pies de alturas G, H, J tienen ángulos desde N iguales a los de los puntos "anti-podales" en el circuncírculo.

Calculemos P_alt: reflexión de X sobre QR. En el circuncírculo, el punto P_alt es el punto donde la altura desde P (recta PX) corta de nuevo el circuncírculo. La recta PX es la altura desde P (perpendicular a QR). Entonces P_alt está en el circuncírculo y ∠P_alt ... Podemos encontrar su ángulo.

El ángulo de P_alt: es el punto del circuncírculo tal que el arco... La recta PX es la altura desde P, perpendicular a QR. La dirección de la perpendicular a QR. En el circuncírculo, el punto P_alt está diametralmente relacionado con el arco.

Usemos la propiedad: el ángulo ∠(P_alt, Q, R) etc. Alternativamente, la recta P P_alt es perpendicular a QR, por lo tanto P_alt está en el punto del circuncírculo tal que el arco QP_alt ... mejor con simetría.

En el circuncírculo, la recta perpendicular a QR desde P interseca de nuevo en P_alt. Como P_alt está en la recta perpendicular a QR, y P también, la cuerda P P_alt es perpendicular a QR. Entonces la cuerda P P_alt es perpendicular a la cuerda QR; en un círculo, cuerdas perpendiculares implican que los arcos entre sus extremos se relacionan.

Podemos usar que la dirección angular de P_alt: si P está a ángulo θ_P = -84°, y Q=0°, R=160°. La recta perpendicular a QR. Calculemos directamente la ecuación de la altura y su intersección con el circuncírculo.

Recta QR: vector director u = r - q = (-(1+c2), s2). Pendiente = s2 / (-(1+c2)) = - s2/(1+c2).

La perpendicular tiene pendiente = (1+c2)/s2.

La recta por p = (c4, -s4) con pendiente m_perp = (1+c2)/s2.

Intersección con el círculo unitario: resolver.

Pero quizá es más fácil calcular G directamente por proyección y luego el ángulo desde N.

Calculemos G = proyección de p sobre la recta QR.

Recta QR parametrizada: q + t(r-q), t ∈ ℝ.

Vector u = r - q = (-(1+c2), s2). |u|² = (1+c2)² + s2² = 1 + 2c2 + c2² + s2² = 1 + 2c2 + 1 = 2 + 2c2 = 2(1+c2).

Proyección de p en q + t u:
p - q = (c4 - 1, -s4).
t = (p - q)·u / |u|².

(p-q)·u = (c4 - 1)·(-(1+c2)) + (-s4)·s2 = -(c4-1)(1+c2) - s4 s2 = (1 - c4)(1+c2) - s4 s2.

Calculemos valores numéricos: c4=0.104528, s4=0.994522, c2=0.939693, s2=0.342020.

(1-c4) = 0.895472. (1+c2) = 1.939693. Producto = 0.895472 * 1.939693 ≈ 1.7370? Calculemos: 0.895472*1.939693 = 0.895472*1.9 = 1.7014, más 0.895472*0.039693 ≈ 0.03554, total ≈ 1.73694.
s4 s2 = 0.994522 * 0.342020 ≈ 0.34015.
t = (1.73694 - 0.34015) / (2*1.939693) = 1.39679 / 3.879386 ≈ 0.36006.

Entonces G = q + t u = (1,0) + 0.36006 * (-1.939693, 0.342020) = (1 - 0.69837, 0.12314) = (0.30163, 0.12314).

Verifiquemos: G debería estar sobre QR entre Q y R. Q=(1,0), R=(-0.9397,0.3420). Con t≈0.36, punto cerca de Q. Parece razonable (proyección de P cerca de Q porque el ángulo Q es grande 58, R pequeño 42, el pie de la altura desde P está más cerca de R? Hmm, P está en -84° cerca de Q (0°), así que la altura cae cerca de Q).

Bien. Ahora vector G - N:
G = (0.30163, 0.12314), N = (0.0824175, -0.326251).
G - N = (0.2192125, 0.449391). Distancia: sqrt(0.2192² + 0.4494²) = sqrt(0.04805 + 0.20195) = sqrt(0.25) = 0.5. Correcto.

Ángulo de G: atan2(0.449391, 0.2192125) ≈ 64°. Calculemos: tan = 0.449391/0.219213 ≈ 2.050. arctan(2.050) ≈ 64.0°. Bien, digamos 64°.

Entonces G está a 64°.

Ahora H: pie de altura desde Q sobre PR.

Recta PR: por p=(c4,-s4) y r=(-c2,s2). Vector v = r - p = (-c2 - c4, s2 + s4) = (-(c2+c4), s2+s4).

Proyección de q sobre recta p + t v.

q - p = (1 - c4, s4).
v·(q-p) = (-(c2+c4))(1-c4) + (s2+s4) s4 = -(c2+c4)(1-c4) + s4 s2 + s4².

|v|² = (c2+c4)² + (s2+s4)² = c2²+2c2c4+c4² + s2²+2s2s4+s4² = 2 + 2(c2c4 + s2s4) = 2 + 2 cos(160° - 84°)? c2c4+s2s4 = cos(20° - 84°)? cos(20-84)=cos(-64)=cos64. Entonces |v|² = 2 + 2 cos64°.

cos64° ≈ 0.438371. |v|² ≈ 2 + 0.876742 = 2.876742.

Calculemos numéricamente:
c2+c4 = 0.939693 + 0.104528 = 1.044221.
s2+s4 = 0.342020 + 0.994522 = 1.336542.
-(c2+c4)(1-c4) = -1.044221 * 0.895472 ≈ -0.93507.
s4 s2 = 0.34015.
s4² = 0.994522² ≈ 0.989074.
Suma = -0.93507 + 0.34015 + 0.989074 = 0.394154.
t = 0.394154 / 2.876742 ≈ 0.137025.

H = p + t v = (c4, -s4) + 0.137025 * (-1.044221, 1.336542) = (0.104528 - 0.14307, -0.994522 + 0.18314) = (-0.038542, -0.811382).

Vector H - N = (-0.038542 - 0.0824175, -0.811382 - (-0.326251)) = (-0.1209595, -0.485131).

Distancia: sqrt(0.014631 + 0.235352) = sqrt(0.249983) ≈ 0.5. Correcto.

Ángulo de H: atan2(-0.485131, -0.1209595). Ambos negativos, tercer cuadrante. Ángulo = 180° + arctan(0.485131/0.1209595) = 180° + arctan(4.0107). arctan(4.0107) ≈ 76°. Entonces H ≈ 256°.

Ahora J: pie de altura desde R sobre PQ.

Recta PQ: por p=(c4,-s4) y q=(1,0). Vector w = q - p = (1-c4, s4).

Proyección de r sobre recta p + t w.

r - p = (-c2 - c4, s2 + s4).
w·(r-p) = (1-c4)(-c2-c4) + s4(s2+s4) = -(1-c4)(c2+c4) + s4 s2 + s4².

Ya calculamos: -(1-c4)(c2+c4) = -0.895472*1.044221 ≈ -0.93507. s4 s2 ≈ 0.34015, s4² ≈ 0.989074. Suma ≈ 0.394154.

|w|² = (1-c4)² + s4² = 1 - 2c4 + c4² + s4² = 2 - 2c4 = 2(1-c4) = 2*0.895472 = 1.790944.

t = 0.394154 / 1.790944 ≈ 0.22008.

J = p + t w = (c4, -s4) + 0.22008 * (0.895472, 0.994522) = (0.104528 + 0.19708, -0.994522 + 0.21888) = (0.301608, -0.775642).

Vector J - N = (0.301608 - 0.0824175, -0.775642 - (-0.326251)) = (0.2191905, -0.449391).

Distancia = 0.5. Correcto.

Ángulo de J: atan2(-0.449391, 0.2191905) ≈ -64° = 296°.

Entonces los ángulos de los seis puntos desde N:
- F: 340° (o -20°)
- G: 64°
- D: 96°
- E: 180°
- H: 256°
- J: 296°

Orden en el círculo (creciente): G (64°), D (96°), E (180°), H (256°), J (296°), F (340°), y de vuelta a G (64°+360°=424°).

Orden circular: G, D, E, H, J, F, (G).

Los arcos menores:
- arco GD = 96 - 64 = 32°
- arco DE = 180 - 96 = 84°
- arco EH = 256 - 180 = 76°
- arco HJ = 296 - 256 = 40°
- arco JF = 340 - 296 = 44°
- arco FG = (424 - 340) = 84°

Suma: 32+84+76+40+44+84 = 360. Correcto.

El problema pide: arco DE + 2·arco HJ + 3·arco FG.

arco DE = 84°, arco HJ = 40°, arco FG = 84°.

Entonces: 84 + 2·40 + 3·84 = 84 + 80 + 252 = 416.

Entonces la respuesta es 416.

Espera, verifiquemos los arcos con las fórmulas angulares para estar seguros, especialmente que el "arco DE" pedido sea el arco menor DE (84°) y el arco FG sea el arco menor FG (84°, el que va de F a G pasando por el punto de corte 360/0). Como se menciona "six minor arcs", los arcos son los menores entre puntos consecutivos. El orden que encontramos es el correcto.

Ahora, déjame verificar los valores angulares de G, H, J con más precisión analítica para confirmar que son 64°, 256°, 296° exactos o aproximados.

- G: ángulo 64°. ¿Por qué sería exacto 64°? Ángulo entre ciertos elementos. En el triángulo, 64° no es un ángulo del triángulo. Podría ser derivado de relaciones.

Notemos: 64° = 180° - 116°? 116° es el arco RP (2·ángulo Q = 116°). O 64° = ... El ángulo de G = 64°. El ángulo en P es 80°, Q=58°, R=42°.

Los arcos que salieron: GD = 32°, DE = 84°, EH = 76°, HJ = 40°, JF = 44°, FG = 84°.

Verifico: 32 = 2·16? 76 = 2·38? Hmm.

En el circuncírculo original los arcos eran PQ=84°, QR=160°, RP=116°.

En el círculo de nueve puntos: DE = 84° (corresponde a PQ). FG = 84° (corresponde a... también PQ? D es punto medio QR, E punto medio PR; F punto medio PQ. F está en PQ, y G es pie de altura desde P en QR).

Existe una simetría: el círculo de nueve puntos contiene los puntos medios y pies de alturas en un orden específico. Los arcos del círculo de nueve puntos pueden calcularse con los ángulos del triángulo.

Verifiquemos con fórmulas exactas.

Para el triángulo con ángulos P=80°, Q=58°, R=42°, el círculo de nueve puntos tiene los seis puntos. Los ángulos de los arcos:

Del circuncírculo con la secuencia de "los puntos notables": Recordemos que el triángulo DEF (medial) tiene arcos correspondientes a los ángulos centrales 2·(ángulos). El arco DE = 2·∠F = 2·42° = 84°. El arco EF = 2·∠D = 2·80° = 160°, el arco FD = 2·∠E = 2·58° = 116°.

Pero entre D y E en el círculo hay dos arcos: el arco DE que pasa por G (arco menor = 84°) y el arco mayor. Encontramos que alrededor, el orden es G, D, E, H, J, F, así que D y E están separados 84° (arco DE = 84°, no contiene a F ni a otros). Bien.

Arco EF: en el orden, E → F pasando por H, J: EH + HJ + JF = 76+40+44 = 160°. Correcto, arco EF = 160° (el arco que no contiene a D = 160°, igual a 2·∠D = 160°). El otro arco E→F pasando por D, G = ED + DG? Espera el arco E→F pasando por D sería E→D (84°)... no, E→D→G→F = 84+32+84 = 200°, no es menor. Hmm el arco menor EF = 160° pasando por H, J. Correcto.

Arco FD: en el orden, F→D pasando por G: FG + GD = 84+32 = 116°. Correcto, = 2·∠E = 116°.

Entonces los arcos entre los puntos medios:
- DE = 84° (=2R)
- EF = 160° (=2P), el arco que pasa por H,J
- FD = 116° (=2Q), el arco que pasa por G (FG=84, GD=32).

Ahora los pies de alturas G, H, J subdividen estos arcos:
- El arco EF (160°) está subdividido por H (en 76° + ...) y J: EH=76°, HJ=40°, JF=44°. Suma 160.
- El arco FD (116°) subdividido por G: FG=84°, GD=32°. Suma 116.
- El arco DE (84°) no tiene ningún pie de altura, es 84°.

Ahora, ¿cómo se subdividen exactamente? Necesitamos las posiciones de los pies de alturas relativas a los puntos medios.

En el círculo de nueve puntos, el orden de los seis puntos (para un triángulo acutángulo) es bien conocido. Dado nuestro orden: G, D, E, H, J, F.

Los arcos involucrados: FG = 84°, GD = 32°, EH = 76°, HJ = 40°, JF = 44°.

Verifiquemos estas subdivisiones con identidades trigonométricas. En teoría:

En el triángulo, la posición de los pies de alturas en el círculo de nueve puntos: el pie de altura desde P (G) está a mitad de camino entre... La propiedad de la homotecia X,1/2: G es imagen del punto P_alt en el circuncírculo (la segunda intersección de la altura desde P). El ángulo de G en el círculo de nueve puntos es igual al ángulo de P_alt en el circuncírculo.

Calculemos P_alt. La altura desde P encuentra el circuncírculo de nuevo en P_alt. Las coordenadas de P_alt en el circuncírculo unitario: P_alt es la reflexión de X sobre QR. En el circuncírculo, podemos hallar su ángulo.

El punto P_alt está en la línea a través de P y X. También P_alt es el punto tal que el arco... Mejor relación: para el circuncírculo, el ángulo de P_alt respecto a Q y R. Sabemos que P_alt es el "punto de la altura". El arco QP_alt = 2·∠Q P_alt? Hmm.

Relación: ∠X P Q... alternativamente, el punto P_alt es el punto del circuncírculo tal que P_alt es la reflexión del ortocentro X sobre el lado QR. La reflexión de X sobre QR está en el circuncírculo. Entonces P_alt está en el circuncírculo, y P_alt es simétrico a X respecto a QR.

Ángulo de P_alt: En el circuncírculo, los ángulos de los puntos "anti-ortocentro". Existe fórmula: si los ángulos del triángulo son A=P=80°, B=Q=58°, C=R=42°, y el circuncírculo parametrizado de forma que Q esté en 0°, R en 2A=160°, P en 2A+... mejor.

Podemos relacionar: P_alt está en el circuncírculo en el ángulo de P desplazado. La altura desde P es perpendicular a QR. En el circuncírculo, el punto P_alt tiene la propiedad de que ∠P_alt Q R = ∠P_alt Q? Ya que P_alt está en la recta PX, perpendicular a QR, ∠(P_alt, y QR)...

Usemos que la cuerda P P_alt es perpendicular a QR. En el círculo, si dos cuerdas son perpendiculares, el ángulo entre las direcciones en el punto de intersección... pero aquí no se intersecan dentro del círculo necesariamente (P y su altura, QR son lados).

Mejor: dirección de la altura desde P es perpendicular a QR. En el circuncírculo, la recta PP_alt es perpendicular a QR. Sabemos que la recta PQ es una cuerda, PR otra.

Existe la identidad: el ángulo de P_alt = ángulo de P + 2(90° - ...). Hmm.

Quizá más simple: Calculemos P_alt numéricamente y obtengamos su ángulo exacto simbólico.

P_alt es la intersección de la recta por P perpendicular a QR con el círculo unitario. La recta por p=(c4,-s4) con dirección perpendicular a QR.

La perpendicular a QR tiene dirección (dirección normal a QR). Vector normal a QR: n = (perpendicular a u). u = r - q = (-(1+c2), s2). La perpendicular es (s2? ...). Un vector perpendicular a u es (s2, 1+c2) o su negativo. La dirección de la altura desde P hacia QR es tal que va hacia el lado QR (hacia abajo/arriba). P está en (0.1045, -0.9945). La altura desciende hasta G=(0.3016, 0.1231), que está más arriba. Entonces la dirección desde P hacia G es (0.3016-0.1045, 0.1231-(-0.9945)) = (0.1971, 1.1176). Esa es la dirección de la altura.

La perpendicular viaja desde P hasta QR y luego más allá hasta P_alt (al otro lado del círculo). La dirección de la altura es perpendicular a QR, y normalizamos es el vector (s2, 1+c2) quizá: (0.3420, 1.9397). Normalizado tiene longitud sqrt(0.342²+1.9397²)=sqrt(0.117+3.762)=sqrt(3.879)=1.9696. Dirección unitaria = (0.1736, 0.9848) = (cos80°, sin80°)? cos80=0.173648, sin80=0.984808. ¡Sí! La dirección de la altura desde P es ángulo 80°.

Interesante: la altura desde P tiene dirección 80° (desde el eje x). ¿Por qué? Porque QR tiene dirección... u = (-(1+c2), s2) ángulo. Ángulo de u: atan2(s2, -(1+c2)) = 180° - atan(s2/(1+c2)). s2/(1+c2) = 0.342/1.9397 = 0.176327 = tan10°. Entonces ángulo de u = 180° - 10° = 170°. Perpendicular = 170° - 90° = 80° o 260°. La altura desde P hacia G tiene dirección 80° (hacia arriba). Entonces la línea de la altura desde P tiene dirección 80°.

P está en ángulo -84°. La recta por P con dirección 80° intersecta el círculo unitario en P y P_alt.

El punto P_alt es la otra intersección. Si P está a ángulo -84° y la recta tiene dirección 80°, entonces la cuerda P-P_alt es una recta con dirección 80°. Para una cuerda en el círculo con dirección φ, los ángulos de sus extremos satisfacen: la dirección de la cuerda es perpendicular al radio hacia el punto medio de la cuerda. Si la cuerda tiene dirección 80°, el vector perpendicular a la cuerda es 80°+90°=170°, o sea el punto medio de la cuerda está en dirección 170° (o 350°). Los extremos son simétricos respecto a 170°.

Entonces si un extremo es P en ángulo -84°=276°, el otro extremo P_alt en ángulo α tal que (α + 276°)/2 ≡ 170° (módulo 180°, ya que el punto medio de la cuerda está en dirección 170° o 170°+180°=350°).

El ángulo central del punto medio: (α+276)/2 = 170° o 350°.

Caso 1: (α+276)/2 = 170° → α+276=340 → α=64°.
Caso 2: (α+276)/2 = 350° → α+276=700 → α=424° ≡ 64°.

¡Ambos dan α=64°! Entonces P_alt está a 64°.

Por lo tanto G (imagen bajo homotecia X,1/2 de P_alt) está en el círculo de nueve puntos a ángulo 64° desde N. ¡Exactamente! Nuestro cálculo numérico dio 64°. Perfecto.

Así que G está a 64°.

Similarmente, H: H es la imagen del punto Q_alt (segunda intersección de la altura desde Q con el circuncírculo). La altura desde Q es perpendicular a PR. La dirección de la altura desde Q... Calculemos la dirección perpendicular a PR.

PR: v = r - p = (-(c2+c4), s2+s4). Ángulo de v: atan2(s2+s4, -(c2+c4)) = 180° - atan((s2+s4)/(c2+c4)). (s2+s4)/(c2+c4) = 1.336542/1.044221 ≈ 1.27995. atan(1.27995) ≈ 52°? tan52° = 1.27994. ¡Sí, exactamente 52°! Entonces ángulo de v = 180° - 52° = 128°. La perpendicular es 128° + 90° = 218° o 38°. La altura desde Q (en ángulo 0°, (1,0)) hacia PR: Q=(1,0), el pie H está en (-0.0385, -0.8114), dirección desde Q a H: (-0.0385-1, -0.8114-0) = (-1.0385, -0.8114), ángulo atan2(-0.8114, -1.0385) ≈ 218°. Entonces la dirección de la altura desde Q es 218° (o 38° en sentido opuesto).

La cuerda Q-Q_alt tiene dirección 218°. Punto medio de la cuerda en dirección 218°-90°=128° (o 128°+180°=308°). Q está a 0°. El otro extremo Q_alt en ángulo β con (β+0)/2 ≡ 128° o 308°.

Caso 1: β/2 = 128° → β = 256°.
Caso 2: β/2 = 308° → β = 616° ≡ 256°.

Entonces Q_alt está a 256°, y H está a 256° en el círculo de nueve puntos. ¡Correcto, nuestro cálculo dio 256°!

J: altura desde R perpendicular a PQ. PQ: w = q - p = (1-c4, s4). Ángulo de w: atan2(s4, 1-c4) = 90° - atan((1-c4)/s4)? (1-c4)/s4 = 0.895472/0.994522 ≈ 0.900404 = tan42°. Entonces atan = 42°, ángulo de w = 90° - 42° = 48°. Perpendicular = 48° + 90° = 138° o 318°. La altura desde R (ángulo 160°, (-0.9397, 0.3420)) hacia J=(0.3016, -0.7756): dirección = (0.3016+0.9397, -0.7756-0.3420) = (1.2413, -1.1176), ángulo atan2(-1.1176, 1.2413) ≈ -42° = 318°. Entonces la dirección de la altura desde R es 318° (no 138°; 138° sería hacia el otro lado).

Cuerda R-R_alt dirección 318°. Punto medio en 318°-90°=228° (o 48°). R está a 160°. Otro extremo γ con (γ+160)/2 ≡ 228° o 48°.

Caso 1: (γ+160)/2 = 228° → γ+160=456 → γ=296°.
Caso 2: (γ+160)/2 = 48° → γ+160=96 → γ=-64° ≡ 296°.

Entonces γ=296°, J a 296°. ¡Correcto!

Perfecto. Entonces la configuración es consistente. Los ángulos de los seis puntos en el círculo de nueve puntos son:

- E: 180° (punto medio de PR)
- D: 96° (punto medio de QR)
- F: -20° = 340° (punto medio de PQ)
- G: 64° (pie de altura desde P)
- H: 256° (pie de altura desde Q)
- J: 296° (pie de altura desde R)

Orden: G(64°), D(96°), E(180°), H(256°), J(296°), F(340°).

Arcos menores:
GD = 32°
DE = 84°
EH = 76°
HJ = 40°
JF = 44°
FG = 84° (340°→424°)

Respuesta: DE + 2 HJ + 3 FG = 84 + 80 + 252 = 416.

Ahora debo verificar si hay ambigüedad en "arco FG": hay dos arcos entre F y G (uno pasando por D,E,H,J... ¿hay otro?). Los puntos F (340°) y G (64°) están separados por el arco menor 84° (de 340° a 424° = 64°+360°), que no contiene otros puntos. Correcto.

Los arcos son "minor arcs" así que 84° para FG.

Por lo tanto, la respuesta final es 416.

Déjame verificar una vez más que el "circumcircle of triangle DEF" se refiere al círculo de DEF y los puntos G, H, J son las segundas intersecciones con QD, PE, PF. D es punto medio de QR, así que QD es el segmento dentro del lado QR, y PE es dentro del lado PR (E punto medio de PR), PF dentro del lado PQ. Las segundas intersecciones son los pies de alturas. Sí, porque el círculo de nueve puntos pasa por los pies de alturas.

Espera: ¿QD se refiere al segmento desde Q hasta D (punto medio de QR), que está sobre QR. La recta QD es la recta QR. La segunda intersección es G = pie de altura desde P. Correcto.

PE: P a E (punto medio de PR), recta PR, segunda intersección H = pie de altura desde Q. Correcto.

PF: P a F (punto medio de PQ), recta PQ, segunda intersección J = pie de altura desde R. Correcto.

Sí.

Por lo tanto la suma es 416.

Déjame también verificar la derivación de los arcos con base en los ángulos del triángulo de manera general, como comprobación.

En general para triángulo con ángulos P=A, Q=B, R=C:
Los puntos medios en el círculo de nueve puntos forman el triángulo medial con arcos: DE=2C, EF=2A, FD=2B.

Los pies de alturas subdividen:
- El pie de altura desde P (G) cae en el arco FD (entre F y D). FG = ? y GD = ?.
- El pie desde Q (H) cae en el arco DE, y el de R (J) en el arco EF? Espera, en nuestro caso G cayó en el arco FD (entre F y D), H y J cayeron en el arco EF (entre E y F). D y E no tienen pies entre ellos en el arco DE.

Revisemos la subdivisión encontrada:
- Arco FD = 116° = 2B (B=58). Subdividido: FG=84°, GD=32°.
- Arco EF = 160° = 2A (A=80). Subdividido: EH=76°, HJ=40°, JF=44°.

Entonces G divide FD, y H, J dividen EF.

Los valores de subdivisión:
En el arco EF (2A=160°): EH=76°, HJ=40°, JF=44°.
En el arco FD (2B=116°): FG=84°, GD=32°.

Verifico si hay fórmulas estándar: En el triángulo, el pie de altura desde R (J) sobre PQ cae más cerca de P o Q dependiendo. JF es el arco entre J y F (F es punto medio de PQ). JF=44°.

Podemos derivar JF: En el círculo de nueve puntos, el ángulo ∠JEF? Hmm.

Otra forma: considerar el ángulo en F entre FJ y FE, etc. El ángulo entre la recta FP (= PQ, ya que F está en PQ y P,F,Q son colineales) y el pie de altura J (que está en PQ). Espera, J está en PQ y F está en PQ, así que F y J están en la misma recta PQ. La recta FJ es PQ. Entonces en el círculo, los puntos F y J están sobre la recta PQ, y el círculo de nueve puntos interseca PQ en F (punto medio de PQ) y J (pie de altura desde R).

El ángulo central ∠FNJ (arco JF) se relaciona con... En el círculo de nueve puntos, el ángulo entre FJ (= dirección PQ) y otros elementos.

Podemos calcular directamente: la distancia entre F y J a lo largo de PQ: F es punto medio de PQ, J es pie de altura desde R. La distancia FJ en la recta PQ. En el círculo de nueve puntos, la cuerda FJ tiene longitud |FJ|, y la relación con el ángulo central: |FJ| = 2·(1/2)·sin(∠FNJ/2) = sin(∠FNJ/2). Entonces ∠FNJ = 2 arcsin(|FJ|). Con radio 1/2.

En el triángulo, F = punto medio de PQ, J = pie de altura desde R sobre PQ. La distancia |FJ| = |(posición F - posición J)| a lo largo de PQ.

Calculemos en función de los ángulos. En el circuncírculo unitario, la distancia |FJ| en la recta PQ. Usamos coordenadas del circuncírculo, multipliquemos por factor... la distancia real en el circuncírculo unitario: F = (p+q)/2, J = proyección de r sobre PQ.

Ya calculamos J = (0.301608, -0.775642), F = (0.552264, -0.497261). Distancia FJ = sqrt((0.552264-0.301608)² + (-0.497261+0.775642)²) = sqrt(0.250656² + 0.278381²) = sqrt(0.062828 + 0.077496) = sqrt(0.140324) = 0.3746.

En el círculo de nueve puntos, radio 1/2. La cuerda FJ en el círculo de nueve puntos es la misma distancia real (los puntos son los mismos en el plano). Entonces sin(arco JF / 2) = |FJ| / (2·r) = 0.3746 / 1 = 0.3746. arco JF/2 = arcsin(0.3746) ≈ 22°. arco JF ≈ 44°. ¡Correcto! Nuestro 44°.

Generalizando: arco JF = 44° para nuestro triángulo. ¿Y en términos de ángulos? 44° = 2·22°, y sin22° = 0.3746 = |FJ|. Esto es consistente.

Bien, la configuración es correcta.

Ahora, la respuesta al problema:

arco DE = 84°, arco HJ = 40°, arco FG = 84°.

84 + 2·40 + 3·84 = 84 + 80 + 252 = 416.

La respuesta es 416.

Déjame redactar la solución paso a paso en español. Debo explicar con claridad.

Voy a presentar:

1. Reconocer que el circuncírculo de DEF es el círculo de nueve puntos de PQR.
2. G, H, J son los pies de las alturas.
3. Determinar los ángulos del triángulo medial: DE corresponde a arco 84°, EF = 160°, FD = 116°.
4. Localizar los pies de alturas en el círculo mediante las segundas intersecciones de las alturas con el circuncírculo (homotecia), encontrando las posiciones angulares.
5. Encontrar el orden y los arcos: GD=32°, DE=84°, EH=76°, HJ=40°, JF=44°, FG=84°.
6. Sumar: 84 + 80 + 252 = 416.

Debo ser conciso pero suficiente. La respuesta final debe ser solo el \boxed{416}.

También verificar: ¿el problema dice "Give only the final answer inside \boxed{}" — la instrucción es razonar paso a paso y dar la respuesta final en \boxed{}. Debo incluir explicación y al final \boxed{416}.

Escribiré en español.

Los detalles de la solución:

Para encontrar las posiciones de los pies de alturas, usaré un argumento elegante: en el circuncírculo de PQR, sean Q=0°, R=160°, P=-84°. La altura desde P es perpendicular a la cuerda QR. La dirección de QR es 170° (ya que el ángulo entre QR y ...). Hmm, ¿cómo presentar sin demasiada trigonometría pesada?

Voy a presentar el razonamiento con el circuncírculo:

Después de poner Q en 0°, R en 2·80°=160° y P en -84° (porque arco PQ=2·42°=84°), usamos que la recta QR tiene dirección 170° (pues QR subtiende un arco de 160°, y el radio medio está en 80°; la recta QR perpendicular al radio en 80° da dirección 80°+90°=170°). Entonces la perpendicular a QR por P tiene dirección 80°. La otra intersección con el circuncírculo es el punto P_alt; la simetría de la cuerda con dirección 80° da que si un extremo es -84°, el otro es 64°. Bajo la homotecia de centro el ortocentro y razón 1/2, este punto se mapea a G, y los ángulos centrales se preservan, por lo que G queda a 64° en el círculo de nueve puntos.

Similar: la cuerda PR tiene dirección 128° (verifico), la altura desde Q dirección 218°, Q=0°, el otro extremo Q_alt = 256°, luego H a 256°. La cuerda PQ dirección 48°, altura desde R dirección 318°, R=160°, otro extremo 296°, luego J a 296°.

Para los puntos medios: E está a 180°, D a 96°, F a 340° (o -20°).

¿Cómo obtuve E a 180°? E = punto medio de PR = imagen de... hmm, bajo la homotecia X,1/2 no es imagen de una cuerda. Necesito justificar las posiciones de D, E, F.

En el círculo de nueve puntos, los puntos medios D, E, F son puntos medios de los lados, y forman el triángulo medial semejante a PQR. Los arcos entre ellos: DE=84°, EF=160°, FD=116°.

Para fijar la posición angular absoluta de E=180°, D=96°, F=340°, usemos que el triángulo medial DEF es homotético al triángulo PQR respecto al baricentro (factor -1/2), no respecto al ortocentro. Para el círculo de nueve puntos, los ángulos de D, E, F desde N no son directamente los ángulos de los vértices.

Alternativa elegante: usar que los vectores desde N de los puntos medios.

Sabemos que E = (p+r)/2 y N = (p+q+r)/4 en coordenadas del circuncírculo. Entonces vector N→E = E - N = (p+r)/2 - (p+q+r)/4 = (p - q + r)/4.

Para nuestros ángulos: p = (cos84°, -sin84°), q = (1,0), r = (cos160°, sin160°) = (-cos20°, sin20°).

E - N = ((cos84 - 1 - cos20)/4, (-sin84 + sin20)/4). ¿Este vector tiene ángulo 180°? Necesitamos verificar que el vector apunta a 180°, es decir, tiene coordenada y = 0 y x < 0. ¿Es -sin84 + sin20 = 0? No exactamente. -0.994522 + 0.342020 = -0.652502 ≠ 0. Espera, eso no da y=0.

Espera, E - N = ((cos84 - 1 + cos160)/4, ...). Cos160 = -cos20. Entonces x-coord = (cos84 - 1 - cos20)/4. Con cos84 = 0.104528, 1 = 1, -cos20 = -0.939693: x = (0.104528 - 1 - 0.939693)/4 = (-1.835165)/4 = -0.458791. y-coord = (-sin84 + sin20)/4 = (-0.994522 + 0.342020)/4 = -0.652502/4 = -0.163126. Entonces E - N = (-0.458791, -0.163126). Eso no es ángulo 180°. ¡Oops! Antes calculé E=(p+r)/2 = (-0.4175825, -0.326251) y N=(0.0824175, -0.326251), así que E-N=(-0.5, 0). ¿Qué pasó con el cálculo actual?

Espera, calculemos de nuevo: p+r = (cos84 + cos160, -sin84 + sin160) = (0.104528 + (-0.939693), -0.994522 + 0.342020) = (-0.835165, -0.652502). E = (p+r)/2 = (-0.4175825, -0.326251).

N = (p+q+r)/4 = ((0.104528+1-0.939693)/4, (-0.994522+0+0.342020)/4) = (0.164835/4, -0.652502/4) = (0.041209, -0.163126).

Espera, antes dije N = X/2 donde X = p+q+r = (0.164835, -0.652502), así que N = (0.082418, -0.326251). ¡Debo ser consistente! N está en el círculo de nueve puntos con centro a la mitad del ortocentro (O=(0,0), X=(0.164835,-0.652502)), entonces N = X/2 = (0.082418, -0.326251).

Pero en mi cálculo de N como (p+q+r)/4 salió (0.041209, -0.163126). ¿Cuál es correcto? ¡Depende del centro del circuncírculo! Si O=(0,0), entonces N = X/2 = (p+q+r)/2, no /4. Corregí: X = p+q+r, N = X/2 = (p+q+r)/2. Entonces N = (0.164835/2, -0.652502/2) = (0.082418, -0.326251). ¡Sí! Había un error: N = (p+q+r)/2, no /4. Porque X = p+q+r (suma de vectores), N = X/2.

Entonces E - N = (p+r)/2 - (p+q+r)/2 = -(q)/2 = -q/2 = (-0.5, 0). ¡Exacto! Esa es la razón: E - N = -q/2, porque E=(p+r)/2 y N=(p+q+r)/2, por lo tanto E-N = (p+r - p - q - r)/2 = -q/2 = (-1/2, 0). Entonces E está a ángulo 180° (pues q=(1,0), -q/2 = (-0.5,0)).

¡Muy bien! Entonces E está a 180° exactamente.

Similarmente:
D = (q+r)/2. D - N = (q+r)/2 - (p+q+r)/2 = -p/2. P en ángulo -84°, entonces -p/2 está en ángulo -84°+180° = 96°. ¡Exacto! D a 96°.

F = (p+q)/2. F - N = (p+q)/2 - (p+q+r)/2 = -r/2. R en ángulo 160°, -r/2 en ángulo 160°+180° = 340°. ¡Exacto! F a 340°.

Excelente, esto es muy elegante. Entonces:
- D - N = -p/2 → ángulo 96° (ya que P está a -84°)
- E - N = -q/2 → ángulo 180° (Q a 0°)
- F - N = -r/2 → ángulo 340° (R a 160°)

Hermoso.

Y los pies de alturas:
G es la imagen de P_alt por homotecia X,1/2: G = (P_alt + X)/2. N = X/2. Entonces G - N = P_alt/2. Por lo tanto el ángulo de G es el ángulo de P_alt. P_alt está a 64°. Entonces G a 64°.

Similar H - N = Q_alt/2, Q_alt a 256°, H a 256°. J - N = R_alt/2, R_alt a 296°, J a 296°.

Muy limpio.

Ahora calculamos P_alt: la segunda intersección de la altura desde P con el circuncírculo. P está a -84°, Q a 0°, R a 160°.

Determinación de P_alt: la altura desde P es perpendicular a la cuerda QR. El punto medio de la cuerda QR está en la dirección (0°+160°)/2 = 80° (el radio que biseca la cuerda QR). La cuerda QR es perpendicular al radio en 80°, por lo tanto la dirección de la cuerda QR es 80°+90° = 170°. La altura desde P es perpendicular a QR, luego tiene dirección 170°-90° = 80° (o 260°). La cuerda P P_alt tiene dirección 80°, así que su punto medio está en dirección 80°+90° = 170° (o 80°-90° = -10°... debemos ser cuidadosos).

Para una cuerda con dirección φ, el radio al punto medio de la cuerda es perpendicular a la cuerda, es decir, está en dirección φ+90° o φ-90°. Los extremos son simétricos respecto al punto medio.

Tomemos la cuerda P P_alt con dirección 80°. Su punto medio está en la dirección 80°+90° = 170° (o 80°-90° = -10° ≡ 350°). Los ángulos de los extremos P (-84°) y P_alt (α) satisfacen (α + (-84°))/2 ≡ 170° (mod 180°), es decir, α - 84° ≡ 340° (mod 360°) → α ≡ 424° ≡ 64°. O bien usando 350°: (α-84)/2 ≡ 350° → α-84 ≡ 700° → α ≡ 784° ≡ 64°. Coincide.

Entonces P_alt = 64°, G = 64°.

Para Q_alt: altura desde Q perpendicular a PR. PR: P=-84°, R=160°. Punto medio de PR en dirección (160° + (-84°))/2 = (160-84)/2 = 76/2 = 38°. Cuerda PR perpendicular al radio en 38°, dirección de PR = 38°+90° = 128°. Debo verificar: ¿el punto medio del arco PR es 38°? El arco desde P(-84°) hasta R(160°) en sentido antihorario: 160 - (-84) = 244°, el punto medio en -84+122 = 38°. Sí. Entonces la cuerda PR tiene dirección 38°+90° = 128° (verificado antes: 128°).

La altura desde Q es perpendicular a PR, dirección 128°+90° = 218° (o 38°). La altura desde Q hacia H tiene dirección 218° (verificado). Cuerda Q Q_alt dirección 218°, punto medio en 218°+90° = 308° (o 128°). Q en 0°. Otro extremo β: (β+0)/2 ≡ 308° → β = 616° ≡ 256°. Entonces Q_alt = 256°, H = 256°.

Para R_alt: altura desde R perpendicular a PQ. PQ: P=-84°, Q=0°. Punto medio de PQ en dirección (-84+0)/2 = -42° (≡ 318°). Cuerda PQ dirección = -42°+90° = 48° (verificado: 48°). Altura desde R dirección 48°+90° = 138° o 318°. La altura desde R hacia J tiene dirección 318° (verificado). Cuerda R R_alt dirección 318°, punto medio en 318°+90° = 408° ≡ 48° (o 228°). R en 160°. Otro extremo γ: (γ+160)/2 ≡ 48° → γ+160 = 96° → γ = -64° ≡ 296°. Entonces R_alt = 296°, J = 296°.

Perfecto.

Ahora los ángulos de los seis puntos:
G=64°, D=96°, E=180°, H=256°, J=296°, F=340°.

Orden creciente: G(64), D(96), E(180), H(256), J(296), F(340).

Diferencias consecutivas (arcos menores):
GD = 32°, DE = 84°, EH = 76°, HJ = 40°, JF = 44°, FG = 84° (de 340 a 424=64+360).

Estas suman 360°. Los seis arcos menores.

El problema pide:
\wideparen{DE} + 2·\wideparen{HJ} + 3·\wideparen{FG} = 84 + 2·40 + 3·84 = 84 + 80 + 252 = 416.

Respuesta: 416.

Debo redactar en español, explicando los pasos. Seré claro pero no excesivamente largo.

Un detalle: al decir "punto medio de la cuerda QR en dirección 80°", debo explicar que el radio que biseca una cuerda es perpendicular a ella, por lo tanto la cuerda QR tiene dirección 80°+90° = 170°. La altura desde P, perpendicular a QR, tiene dirección 80°. La cuerda PP_alt tiene dirección 80°, etc.

Debo también justificar por qué G es la imagen de P_alt bajo la homotecia con centro el ortocentro: porque el pie de altura G es el punto medio entre el ortocentro X y P_alt (la segunda intersección de la altura con el circuncírculo). Hecho conocido: la reflexión del ortocentro sobre un lado cae en el circuncírculo, y el pie de la altura es el punto medio entre el ortocentro y esa reflexión. Entonces G = (X + P_alt)/2.

También N = X/2 (centro del círculo de nueve puntos es el punto medio entre circuncentro O y ortocentro X; con O en el origen, N = X/2). Entonces G - N = P_alt/2, por lo que la posición angular de G respecto a N es la misma que la de P_alt respecto a O. Similar para H, J.

Para D, E, F: D=(Q+R)/2, N=(P+Q+R)/2 (con O=0, X=P+Q+R, N=X/2). Entonces D - N = (Q+R - P - Q - R)/2 = -P/2; su ángulo es el de P más 180°.

Perfecto.

Escribo la solución.

Quiero asegurarme de la notación de los vértices: P ángulo 80°, Q 58°, R 42°. Entonces:
- P: -84° (o 276°)
- Q: 0°
- R: 160°

Arcos del circuncírculo: PQ = 84° (ángulo central menor entre P y Q: de -84 a 0 es 84°). QR = 160° (de 0 a 160). RP = 116° (de 160 a 276).

Estos corresponden: arco QR = 2∠P = 160°, arco RP = 2∠Q = 116°, arco PQ = 2∠R = 84°. Correcto.

Ahora, al derivar los ángulos de los pies de las alturas:

Para P_alt: altura desde P perpendicular a QR. QR es cuerda con extremos Q(0°) y R(160°). El punto medio del arco menor QR está en 80°. El radio en 80° es perpendicular a la cuerda QR, así que la cuerda QR tiene dirección 80°+90°=170°. (Alternativamente 80°-90° = -10°, la misma recta). La altura desde P es perpendicular a QR, dirección 80° (o 260°). La cuerda P P_alt tiene dirección 80°. El punto medio de esta cuerda está en la dirección perpendicular a la cuerda: 80°+90°=170°. Entonces los extremos son simétricos respecto a 170°: si un extremo es P=-84°, el otro es 2·170° - (-84°) = 340°+84° = 424° ≡ 64°. Entonces P_alt = 64°.

De forma similar para los otros.

Para Q_alt: altura desde Q perpendicular a PR. PR: extremos P(-84°) y R(160°). Punto medio del arco PR: el arco menor desde P(-84°) a R(160°) mide 244° (en sentido antihorario), punto medio en -84 + 122 = 38°. El radio en 38° es perpendicular a PR, entonces PR tiene dirección 128°. La altura desde Q es perpendicular a PR, dirección 218° (o 38°). La cuerda Q Q_alt dirección 218°, punto medio en 218°-90° = 128°. Espera, el punto medio de la cuerda está en la dirección perpendicular a la cuerda: 218°+90° = 308° o 218°-90° = 128°. Ambos son la misma recta (difieren 180°). Usemos 308°: extremos simétricos respecto a 308°. Q=0°, otro extremo β: 2·308° - 0° = 616° ≡ 256°. Entonces Q_alt=256°.

Para R_alt: altura desde R perpendicular a PQ. PQ: extremos P(-84°) y Q(0°). Punto medio del arco PQ: arco menor desde -84° a 0° es 84°, punto medio en -42° (≡ 318°). Radio en 318° perpendicular a PQ, entonces PQ dirección 318°+90° = 408° ≡ 48°. Altura desde R perpendicular a PQ, dirección 48°+90° = 138° o 318°. La cuerda R R_alt dirección 318° (es la dirección de la altura desde R hacia el pie J, verificada). Punto medio en 318°+90° = 408° ≡ 48° (o 228°). Extremos simétricos respecto a 48°: R=160°, otro γ: 2·48° - 160° = 96° - 160° = -64° ≡ 296°. Entonces R_alt=296°.

Bien.

Entonces todos los valores son consistentes.

Voy a escribir la solución final en español con estas ideas, y la respuesta en \boxed{416}.

Debo mantenerlo razonablemente conciso. Usaré aproximaciones de grados y mostraré las posiciones.

Al redactar, también debo mencionar que el orden de los seis puntos en el círculo de nueve puntos es G, D, E, H, J, F, y los arcos menores consecutivos.

Voy a incluir las figuras verbales.

Final:

Los arcos menores: \wideparen{GD}=32°, \wideparen{DE}=84°, \wideparen{EH}=76°, \wideparen{HJ}=40°, \wideparen{JF}=44°, \wideparen{FG}=84°.

Entonces \wideparen{DE} + 2\wideparen{HJ} + 3\wideparen{FG} = 84 + 80 + 252 = 416.

Respuesta: \boxed{416}.

Voy a red