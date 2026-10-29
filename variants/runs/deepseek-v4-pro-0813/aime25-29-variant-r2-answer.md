Voy a razonar el problema paso a paso.

**Planteamiento con coordenadas.**

Coloquemos $P=(0,0)$, $Q=(a,0)$, $R=(0,b)$, con $a,b>0$. Como $\angle P=90^\circ$:

$$
a^2+b^2=QR^2=(4\sqrt{301})^2=4816.
$$

Como $PX=QX=26$, el punto $X$ está en la mediatriz de $PQ$, luego

$$
X=\left(\frac a2,\, h_1\right),\qquad h_1=\sqrt{26^2-\frac{a^2}{4}}.
$$

Como $PY=RY=26$, el punto $Y$ está en la mediatriz de $PR$, luego

$$
Y=\left(k_2,\,\frac b2\right),\qquad k_2=\sqrt{26^2-\frac{b^2}{4}}.
$$

Escribamos

$$
\frac a2=26\cos\theta,\quad h_1=26\sin\theta,
$$

$$
\frac b2=26\sin\phi,\quad k_2=26\cos\phi.
$$

Así

$$
a=52\cos\theta,\qquad b=52\sin\phi.
$$

Dado que $PX=PY=XY=26$, el triángulo $PXY$ es equilátero, de modo que

$$
\phi-\theta=60^\circ.
$$

Sea pues $\phi=\theta+60^\circ$.

**Condición de la hipotenusa.**

$$
a^2+b^2=52^2\left(\cos^2\theta+\sin^2(\theta+60^\circ)\right)=4816.
$$

Como $52^2=2704$ y $4816/2704=301/169$:

$$
\cos^2\theta+\sin^2(\theta+60^\circ)=\frac{301}{169}.
$$

Desarrollamos

$$
\sin(\theta+60^\circ)=\frac12\sin\theta+\frac{\sqrt3}{2}\cos\theta.
$$

Entonces

$$
\cos^2\theta+\left(\frac12\sin\theta+\frac{\sqrt3}{2}\cos\theta\right)^2=\frac{301}{169}.
$$

Operando y usando identidades de ángulo doble se llega a

$$
3\cos 2\theta+\sqrt3\sin 2\theta=\frac{528}{169}.
$$

Observamos que esto es exactamente

$$
\sqrt3\left(\sqrt3\cos 2\theta+\sin 2\theta\right)=\frac{528}{169},
$$

de donde

$$
\sqrt3\cos 2\theta+\sin 2\theta=\frac{528}{169\sqrt3}=\frac{176\sqrt3}{169}.
$$

**Cálculo del área de $QXYR$.**

El cuadrilátero $QXYR$ se obtiene del triángulo $PQR$ quitando los triángulos $PQX$ y $PYR$, y añadiendo de nuevo su solape, que es el triángulo equilátero $PXY$:

$$
[QXYR]=[PQR]-[PQX]-[PYR]+[PXY].
$$

Tenemos

$$
[PQR]=\frac12ab=\frac12(52\cos\theta)(52\sin\phi)=1352\cos\theta\sin\phi,
$$

$$
[PQX]=\frac12 a\cdot h_1=\frac12(52\cos\theta)(26\sin\theta)=676\cos\theta\sin\theta,
$$

$$
[PYR]=\frac12 b\cdot k_2=\frac12(52\sin\phi)(26\cos\phi)=676\sin\phi\cos\phi,
$$

$$
[PXY]=\frac{\sqrt3}{4}\cdot 26^2=169\sqrt3.
$$

Por tanto

$$
[QXYR]=1352\cos\theta\sin\phi-676\cos\theta\sin\theta-676\sin\phi\cos\phi+169\sqrt3.
$$

Simplificamos la parte trigonométrica con $\phi=\theta+60^\circ$.

Primero,

$$
2\cos\theta\sin\phi=2\cos\theta\left(\frac12\sin\theta+\frac{\sqrt3}{2}\cos\theta\right)
=\cos\theta\sin\theta+\sqrt3\cos^2\theta.
$$

Además,

$$
\sin\phi\cos\phi=\left(\frac12\sin\theta+\frac{\sqrt3}{2}\cos\theta\right)\left(\frac12\cos\theta-\frac{\sqrt3}{2}\sin\theta\right)
=-\frac12\sin\theta\cos\theta+\frac{\sqrt3}{4}\cos 2\theta.
$$

Entonces la combinación se reduce a

$$
2\cos\theta\sin\phi-\cos\theta\sin\theta-\sin\phi\cos\phi
=\frac{\sqrt3}{2}+\frac{\sqrt3}{4}\cos 2\theta+\frac14\sin 2\theta.
$$

Como $676=4\cdot 169$:

$$
[QXYR]=169\left(2\sqrt3+\sqrt3\cos 2\theta+\sin 2\theta\right)+169\sqrt3.
$$

Pero ya calculamos

$$
\sqrt3\cos 2\theta+\sin 2\theta=\frac{176\sqrt3}{169}.
$$

Por lo tanto

$$
[QXYR]=169\left(2\sqrt3+\frac{176\sqrt3}{169}\right)+169\sqrt3.
$$

$$
[QXYR]=338\sqrt3+176\sqrt3+169\sqrt3=683\sqrt3.
$$

Así,

$$
n=683.
$$

\[
\boxed{683}
\]Voy a razonar el problema paso a paso.

El triángulo $PQR$ es rectángulo en $P$, con $QR = 4\sqrt{301}$.

Puntos $X$ e $Y$ en el interior con:
- $PX = PY = QX = RY = XY = 26$.

Interpretación: hay un punto $Q$ tal que $PX = QX$, etc. Vamos a plantear geometría.

Como $PX = QX = 26$, los puntos $P$ y $Q$ están ambos a distancia 26 de $X$. Análogamente, $PY = RY = 26$, así que $P$ y $R$ están ambos a distancia 26 de $Y$. Además $XY = 26$.

Esto sugiere una configuración con triángulos equiláteros o rombos.

Sea un sistema de coordenadas con $P$ en el origen. Pongamos $P = (0,0)$.

Como $PX = 26$ y $QX = 26$, el punto $X$ está en la mediatriz de $PQ$. Similar $Y$ en la mediatriz de $PR$.

Además $XY = 26$.

Vamos a pensar en la estructura: Hay triángulos $PQX$ y $PYR$ isósceles. También $PX = PY = XY = 26$, por lo que $PXY$ es un triángulo equilátero de lado 26.

Como $\angle P = 90^\circ$, $Q$ está en una semirrecta desde $P$ y $R$ en la perpendicular. La hipotenusa $QR$ mide $4\sqrt{301}$.

Calculemos: $4\sqrt{301} = 4 \times \sqrt{301} \approx 4 \times 17.349 = 69.4$. Los lados de 26 encajan bien.

Supongamos que $Q$ está en el eje $x$ positivo, $P=(0,0)$, $Q=(a,0)$, $R=(0,b)$ con $a^2+b^2 = (4\sqrt{301})^2 = 16 \times 301 = 4816$.

Punto $X$: satisface $|X-P|=26$ y $|X-Q|=26$. Entonces $X$ está en la mediatriz de $PQ$: $x = a/2$, y además su distancia a $P$ es 26.

Igualmente $Y$: $|Y-P|=26$, $|Y-R|=26$, así que $Y$ está en la mediatriz de $PR$: $y = b/2$.

Además $|XY|=26$.

Como $PXY$ es equilátero, el ángulo entre $PX$ y $PY$ es $60^\circ$. La dirección de $PX$ forma un ángulo con el eje $x$, y la de $PY$ un ángulo con el eje $y$.

Escribamos $X = (a/2, y_X)$ con $|X|^2 = (a/2)^2 + y_X^2 = 26^2 = 676$.

Entonces $y_X^2 = 676 - a^2/4$.

Análogo $Y = (x_Y, b/2)$, con $x_Y^2 = 676 - b^2/4$.

Como $PXY$ equilátero con $X$ e $Y$ en el interior del triángulo (primer cuadrante), ambos $X$, $Y$ tienen coordenadas positivas.

Además $PXY$ equilátero: el ángulo $\angle XPY = 60^\circ$, y los vectores $PX$ y $PY$ tienen longitud 26.

Sean ángulos: $X$ forma ángulo $\theta$ con eje $x$, $Y$ forma ángulo $\phi$ con eje $x$ medido desde $P$. Como $Y$ está cerca del eje $y$, pero en primer cuadrante. La condición $\angle XPY = 60^\circ$ implica $|\phi - \theta| = 60^\circ$.

Además $X = (26\cos\theta, 26\sin\theta)$, y sabemos $x_X = a/2$, así $a/2 = 26\cos\theta$, luego $a = 52\cos\theta$.

$Y = (26\cos\phi, 26\sin\phi)$, y $y_Y = b/2 = 26 \sin\phi$, luego $b = 52\sin\phi$.

Sustituimos en $a^2 + b^2 = (52\cos\theta)^2 + (52\sin\phi)^2 = 4816$.

Dividiendo por $52^2 = 2704$: $\cos^2\theta + \sin^2\phi = 4816/2704 = 4816/2704$.

Calculemos: $2704 \times 1.781 = 4816$? Veamos: $2704 \times 1.78 = 4813.12$. $4816/2704 = (4816 \div 16)/(2704\div 16) = 301/169$. 

¡Interesante! $4816/2704 = 301/169$.

Entonces: $\cos^2\theta + \sin^2\phi = 301/169$.

Esto es notable: $301/169 = (301)/13^2$. Además $301 = 7 \times 43$. 

Tenemos $\theta$ y $\phi$ con $\phi - \theta = 60^\circ$ (asumiendo $\phi > \theta$).

Sustituyamos $\phi = \theta + 60^\circ$.

$\sin\phi = \sin(\theta+60^\circ) = \sin\theta \cos 60^\circ + \cos\theta \sin 60^\circ = \frac{1}{2}\sin\theta + \frac{\sqrt{3}}{2}\cos\theta$.

Elevamos al cuadrado: $\sin^2\phi = \frac{1}{4}\sin^2\theta + \frac{\sqrt{3}}{2}\sin\theta\cos\theta + \frac{3}{4}\cos^2\theta$.

Entonces $\cos^2\theta + \sin^2\phi = \cos^2\theta + \frac{1}{4}\sin^2\theta + \frac{\sqrt3}{2}\sin\theta\cos\theta + \frac{3}{4}\cos^2\theta$.

Agrupemos: $\cos^2\theta + \frac{3}{4}\cos^2\theta = \frac{7}{4}\cos^2\theta$. Más $\frac14 \sin^2\theta$. Más el término cruzado.

Entonces:
$$\frac{7}{4}\cos^2\theta + \frac{1}{4}\sin^2\theta + \frac{\sqrt3}{2}\sin\theta\cos\theta = \frac{301}{169}.$$

Esto se complica. Probemos otra vía más geométrica.

Tal vez la configuración estándar: puntos $X$ e $Y$ tales que forman rombos/equiláteros. Dado que $PX=PY=XY=26$, el triángulo $PXY$ es equilátero.

También $QX = 26$ y $RX$? No, $RY=26$. Tenemos $PX=QX$ con $X$ en mediatriz de $PQ$, y $PY=RY$ con $Y$ en mediatriz de $PR$.

Veamos el cuadrilátero $QXYR$. Queremos su área.

El cuadrilátero $QXYR$ tiene vértices $Q, X, Y, R$. En el triángulo $PQR$, con $X$ cerca de $PQ$ y $Y$ cerca de $PR$.

Área de $QXYR = \text{área}(PQR) - \text{área}(PQX) - \text{área}(PYR) + \text{área}(PXY)$? Cuidado con el solapamiento.

El triángulo $PQR$ se particiona: contiene el triángulo $PQX$ (vértices $P,Q,X$), el triángulo $PYR$ (vértices $P,Y,R$), y el cuadrilátero $QXYR$. Pero el triángulo $PXY$ está en la intersección de $PQX$ y $PYR$? Vamos a ver.

Si $X$ está en la mediatriz de $PQ$, el triángulo $PQX$ está "por encima" del segmento $PQ$? En realidad $X$ está en el lado interior (primer cuadrante). El triángulo $PQX$ usa base $PQ$ sobre eje $x$ y vértice $X$ arriba. El triángulo $PYR$ usa base $PR$ sobre eje $y$ y vértice $Y$ a la derecha.

Estos dos triángulos se solapan en el triángulo $PXY$ (si $X$ e $Y$ están ubicados de modo que el segmento $XY$ corta). El resto del triángulo $PQR$ fuera de estos dos triángulos es exactamente $QXYR$.

Entonces: área $QXYR = [PQR] - [PQX] - [P R Y] + [PXY]$, porque la intersección $PXY$ se restó dos veces.

Sí, esa es la idea. El triángulo $PQR$ está cubierto por $PQX$, $PYR$ y el cuadrilátero central $QXYR$, y $PQX \cap PYR = PXY$ (el triángulo equilátero). Por tanto:
$$[QXYR] = [PQR] - [PQX] - [PYR] + [PXY].$$

Ahora, $[PXY]$ es equilátero de lado 26: $[PXY] = \frac{\sqrt3}{4}\cdot 26^2 = \frac{\sqrt3}{4}\cdot 676 = 169\sqrt3$.

$[PQX]$: triángulo isósceles con $PQ=a$ base y lados $PX=QX=26$. Su altura desde $X$ a $PQ$ es $h_1 = \sqrt{26^2 - (a/2)^2}$. Área = $\frac12 a \cdot h_1$.

Análogamente $[PYR] = \frac12 b \cdot h_2$ con $h_2 = \sqrt{26^2 - (b/2)^2}$.

$[PQR] = \frac12 ab$.

Entonces $[QXYR] = \frac12 ab - \frac12 a h_1 - \frac12 b h_2 + 169\sqrt3$.

Necesitamos $a$, $b$ con $a^2+b^2 = 4816$, y también la condición de que $PXY$ sea equilátero.

La condición equilátera relaciona $X$ e $Y$. Ya vimos que da $\cos^2\theta + \sin^2\phi = 301/169$.

Vamos a resolver algebraicamente de otra forma.

Sea $\theta$ el ángulo de $PX$ con el eje $x$: $X=(26\cos\theta, 26\sin\theta)$, $a/2 = 26\cos\theta$, así $a=52\cos\theta$, $h_1 = 26\sin\theta$.

Sea $\phi$ el ángulo de $PY$ con el eje $y$? Mejor con eje $x$: $Y = (26\cos\phi, 26\sin\phi)$, $b/2 = 26\sin\phi$, $b=52\sin\phi$, $h_2 = 26\cos\phi$.

Condición equilátera: $\phi - \theta = 60^\circ$ (asumiendo $Y$ más "vertical").

Entonces $a = 52\cos\theta$, $b = 52\sin(\theta+60^\circ)$.

Condición $a^2+b^2 = 4816$:
$$52^2[\cos^2\theta + \sin^2(\theta+60^\circ)] = 4816.$$

$2704 [\cos^2\theta + \sin^2(\theta+60^\circ)] = 4816$.

Dividimos: $\cos^2\theta + \sin^2(\theta+60^\circ) = 301/169$.

Ya lo teníamos. Desarrollemos $\sin^2(\theta+60^\circ) = (\frac12\sin\theta + \frac{\sqrt3}{2}\cos\theta)^2 = \frac14\sin^2\theta + \frac{\sqrt3}{2}\sin\theta\cos\theta + \frac34\cos^2\theta$.

Suma con $\cos^2\theta$:
$$\cos^2\theta + \frac14\sin^2\theta + \frac{\sqrt3}{2}\sin\theta\cos\theta + \frac34\cos^2\theta = \frac74\cos^2\theta + \frac14\sin^2\theta + \frac{\sqrt3}{2}\sin\theta\cos\theta.$$

Escribamos $\sin^2\theta = 1 - \cos^2\theta$:
$$\frac74\cos^2\theta + \frac14(1-\cos^2\theta) + \frac{\sqrt3}{2}\sin\theta\cos\theta = \frac64\cos^2\theta + \frac14 + \frac{\sqrt3}{2}\sin\theta\cos\theta = \frac32\cos^2\theta + \frac14 + \frac{\sqrt3}{2}\sin\theta\cos\theta.$$

Igual a $301/169$:
$$\frac32\cos^2\theta + \frac{\sqrt3}{2}\sin\theta\cos\theta + \frac14 = \frac{301}{169}.$$

Multiplicamos por 4:
$$6\cos^2\theta + 2\sqrt3\sin\theta\cos\theta + 1 = \frac{1204}{169}.$$

Entonces:
$$6\cos^2\theta + 2\sqrt3\sin\theta\cos\theta = \frac{1204}{169} - 1 = \frac{1204-169}{169} = \frac{1035}{169}.$$

Usemos identidades: $\cos^2\theta = \frac{1+\cos2\theta}{2}$, $\sin\theta\cos\theta = \frac{\sin 2\theta}{2}$.

$$6\cdot\frac{1+\cos2\theta}{2} + 2\sqrt3 \cdot \frac{\sin2\theta}{2} = 3(1+\cos2\theta) + \sqrt3 \sin2\theta = 3 + 3\cos2\theta + \sqrt3\sin2\theta.$$

Igual a $1035/169$:
$$3 + 3\cos2\theta + \sqrt3\sin2\theta = \frac{1035}{169}.$$

$$3\cos2\theta + \sqrt3\sin2\theta = \frac{1035}{169} - 3 = \frac{1035 - 507}{169} = \frac{528}{169}.$$

Observemos que $3\cos2\theta + \sqrt3\sin2\theta = 2\sqrt3\cos(2\theta - 30^\circ)$? Comprobemos: $2\sqrt3\cos(2\theta-30^\circ) = 2\sqrt3(\cos2\theta\cos30^\circ + \sin2\theta\sin30^\circ) = 2\sqrt3(\frac{\sqrt3}{2}\cos2\theta + \frac12 \sin2\theta) = 3\cos2\theta + \sqrt3\sin2\theta$. Sí.

Entonces:
$$2\sqrt3 \cos(2\theta - 30^\circ) = \frac{528}{169}.$$

$$\cos(2\theta - 30^\circ) = \frac{528}{169 \cdot 2\sqrt3} = \frac{264}{169\sqrt3} = \frac{264\sqrt3}{169\cdot 3} = \frac{88\sqrt3}{169}.$$

Esto no se ve muy "limpio". Revisemos: quizá elegí mal la orientación. Probemos $\phi = \theta - 60^\circ$ o considerar que el ángulo entre $PX$ y $PY$ sea $60^\circ$ pero con $Y$ "por debajo".

Alternativamente, quizá la configuración es: $X$ sobre mediatriz de $PQ$, $Y$ sobre mediatriz de $PR$, pero $PXY$ equilátero puede estar orientado de otra manera. La solución debería dar un $n$ entero bonito. Exploremos.

Tal vez la clave es que el área de $QXYR$ salga $n\sqrt3$ simple, y hay una relación elegante.

Hagamos enfoque vectorial más directo.

Sean $\vec u = \overrightarrow{PX}$, $\vec v = \overrightarrow{PY}$, con $|\vec u|=|\vec v|=26$ y $\vec u \cdot \vec v = 26^2 \cos 60^\circ = 338$ (porque $XY=26$ implica $|\vec v - \vec u|^2 = 26^2$, luego $2\cdot 26^2 - 2\vec u\cdot\vec v = 26^2$, $\vec u \cdot \vec v = 26^2/2 = 338$).

Además $Q = 2X - P$? No, $X$ está en mediatriz de $PQ$, con $P$ en origen. Si $P=(0,0)$ y $PX = QX$, entonces $Q$ es el reflejo de $P$ a través de la perpendicular por $X$... En realidad los puntos a distancia 26 de $X$ incluyen a $P$ y $Q$. $Q$ es el punto a distancia 26 de $X$ en la semirrecta opuesta a la proyección.

Más simplemente, como $P$ y $Q$ equidistan de $X$, el vector $\overrightarrow{PQ}$ es perpendicular a $\overrightarrow{PX}$ y $X$ está en la mediatriz. Concretamente, si $X=(x_1,y_1)$, entonces $Q = 2 \text{proj}_{\perp}$... 

Mejor: $Q$ es la imagen de $P$ por reflexión respecto a la recta por $X$ perpendicular a $PX$. Pero dado $P=0$ y $X$, el punto $Q$ a distancia 26 de $X$ y tal que $PQ$ es un cateto. La relación: $\overrightarrow{PQ} = 2\overrightarrow{PX}_\perp$? 

Sea $X = (x,y)$ con $|X|=26$. La mediatriz de $PQ$ pasa por $X$, y $PQ$ es perpendicular a $PX$. Entonces $Q$ está sobre la recta perpendicular a $PX$ por el punto... Además $P$ y $Q$ son simétricos respecto a la recta perpendicular a $PX$ que pasa por $X$. Así $Q = 2X_\perp$? Hmm.

Si $P=(0,0)$ y la recta $\ell$ (mediatriz) pasa por $X$ y es perpendicular a $PX$, entonces $Q$ es el reflejo de $P$ por $\ell$. Como $P$ está en origen, $Q=2 (X \cdot n) n$? 

La recta $\ell$: pasa por $X$, dirección perpendicular a $X$ (vector $X^\perp=(-y,x)$). El reflejo de $P=0$ por $\ell$: como $\ell$ es perpendicular a $PX$ y pasa por $X$, la recta está a distancia $|X|=26$ del origen a lo largo de la dirección $X/|X|$? En realidad el segmento $PX$ es perpendicular a $\ell$ y va de $P$ a $X$, longitud 26. El reflejo de $P$ por $\ell$ es el punto $Q$ tal que $X$ es punto medio de $PQ$. 

Es decir, $X$ es el punto medio de $PQ$: porque $P$ y $Q$ son simétricos respecto a $\ell$, y $X \in \ell$, además $X$ es el pie de la perpendicular desde $P$ (y desde $Q$) a $\ell$. Entonces $X$ es el punto medio del segmento $PQ$.

¡Claro! $X$ es el punto medio de $PQ$. Comprobemos: si $X$ es punto medio de $PQ$, $PX=QX$, y además la perpendicular a $PQ$ por $X$ es la mediatriz (pasa por $X$). Consistente.

Del mismo modo, $Y$ es el punto medio de $PR$.

Entonces: $Q = 2X$, $R = 2Y$.

¡Excelente! Esto simplifica todo.

Tenemos $P=0$, $Q=2X$, $R=2Y$, con $|X|=|Y|=26$ y $|Y-X|=26$ (triángulo equilátero $PXY$).

Entonces el triángulo $PQR$ tiene catetos $PQ = 2|X| = 52$ y $PR = 2|Y| = 52$, y además el ángulo $QPR$ es el ángulo entre $X$ e $Y$, que es $60^\circ$ (por el triángulo equilátero). Por lo tanto los catetos tienen longitud 52 cada uno y el ángulo entre ellos es $60^\circ$, no $90^\circ$.

¡Contradicción! Se nos dice $\angle P = 90^\circ$. Pero si $Q=2X$, $R=2Y$ y $\angle XPY=60^\circ$, entonces $\angle QPR = 60^\circ$, no $90^\circ$.

Entonces mi suposición de que $X$ es punto medio está mal. Reconsideremos.

Espera: ¿$X$ es punto medio de $PQ$? Si $P$ y $Q$ equidistan de $X$ ($PX=QX$), $X$ está en la mediatriz de $PQ$, no necesariamente es el punto medio. El punto medio de $PQ$ es el pie de la perpendicular mediatriz, pero $X$ puede estar en cualquier parte de la mediatriz. 

Cierto. $X$ está en la mediatriz, pero no tiene por qué ser el pie. Entonces $X$ no es punto medio de $PQ$; $X$ está a distancia 26 de ambos, $P$ y $Q$, por lo que el triángulo $PQX$ es isósceles con base $PQ$ y vértice $X$, pero la base $PQ$ no es necesariamente perpendicular a $PX$... En realidad en un triángulo isósceles, la altura desde $X$ cae en el punto medio de $PQ$, y es perpendicular a $PQ$. Entonces el pie de la perpendicular desde $X$ a $PQ$ es el punto medio de $PQ$, pero $X$ no es ese pie.

Ok, regresemos a la formulación inicial con ángulos.

Retomemos: $Q = (a,0)$, $R=(0,b)$, $X=(a/2, h_1)$ con $h_1 = \sqrt{676 - a^2/4}$, $Y=(k_2, b/2)$ con $k_2 = \sqrt{676-b^2/4}$. Con $h_1, k_2 >0$.

Condición $|Y - X| = 26$.

Esto da una ecuación. También los ángulos.

En realidad nuestra ecuación de ángulos usaba $(a/2) = 26\cos\theta$, $h_1 = 26\sin\theta$, y $(b/2) = 26\sin\phi$, $k_2 = 26\cos\phi$, con $\theta, \phi$ ángulos tal que $\angle XPY = 60^\circ$.

Pero cuidado: $\theta$ era el ángulo de $PX$ con el eje $x$. $X = (a/2, h_1)$. Entonces $\cos\theta = (a/2)/26$, $\sin\theta = h_1/26$.

$Y = (k_2, b/2)$. Ángulo $\phi$ de $PY$ con eje $x$: $\cos\phi = k_2/26$, $\sin\phi = (b/2)/26$.

$\angle XPY = \phi - \theta = 60^\circ$ (con $\phi > \theta$, ya que $Y$ es más cercano al eje $y$).

Eso es lo que usamos, y nos dio una solución con $\cos(2\theta - 30^\circ) = 88\sqrt3/169$. Veamos si es válida. El valor $88\sqrt3/169 \approx 88\times 1.732/169 \approx 152.42/169 \approx 0.902$. Es un coseno válido. Entonces hay solución.

Sigamos. Tenemos $a = 52\cos\theta$, $b = 52\sin(\theta+60^\circ)$.

Ahora calculemos el área deseada $[QXYR] = \frac12 ab - \frac12 a h_1 - \frac12 b h_2 + 169\sqrt3$, con $h_1 = 26\sin\theta$, $h_2 = 26\cos\phi = 26\cos(\theta+60^\circ)$.

Sustituyamos $a = 52\cos\theta$, $b=52\sin\phi$ (con $\phi = \theta + 60^\circ$):

$\frac12 ab = \frac12 \cdot 52\cos\theta \cdot 52\sin\phi = 1352 \cos\theta \sin\phi$.

$\frac12 a h_1 = \frac12 \cdot 52\cos\theta \cdot 26\sin\theta = 676 \cos\theta \sin\theta$.

$\frac12 b h_2 = \frac12 \cdot 52\sin\phi \cdot 26\cos\phi = 676 \sin\phi\cos\phi$.

Entonces:
$$[QXYR] = 1352\cos\theta\sin\phi - 676\cos\theta\sin\theta - 676\sin\phi\cos\phi + 169\sqrt3.$$

Notemos $1352 = 2\times 676$. Entonces:
$$[QXYR] = 676[2\cos\theta\sin\phi - \cos\theta\sin\theta - \sin\phi\cos\phi] + 169\sqrt3.$$

Recordemos identidad: $2\cos\theta\sin\phi = \sin(\phi+\theta) + \sin(\phi-\theta)$.

Con $\phi - \theta = 60^\circ$, $\sin(\phi-\theta) = \sqrt3/2$.

Entonces $2\cos\theta\sin\phi = \sin(\phi+\theta) + \frac{\sqrt3}{2}$.

También $\cos\theta\sin\theta = \frac12 \sin2\theta$, y $\sin\phi\cos\phi = \frac12\sin2\phi$.

Entonces:
$$2\cos\theta\sin\phi - \cos\theta\sin\theta - \sin\phi\cos\phi = \sin(\phi+\theta) + \frac{\sqrt3}{2} - \frac12\sin2\theta - \frac12\sin2\phi.$$

Además $\phi+\theta = 2\theta+60^\circ$. Hmm.

Alternativa, hay identidad para $\cos\theta\sin\phi - \frac12(\sin2\theta+\sin2\phi)$? 

Probemos simplificar usando $\phi = \theta + 60^\circ$ directamente.

$\sin\phi = \frac12\sin\theta + \frac{\sqrt3}{2}\cos\theta$.
$\cos\phi = \frac12\cos\theta - \frac{\sqrt3}{2}\sin\theta$.

Calculemos cada término:

1) $2\cos\theta\sin\phi = 2\cos\theta(\frac12\sin\theta + \frac{\sqrt3}{2}\cos\theta) = \cos\theta\sin\theta + \sqrt3\cos^2\theta$.

2) $\cos\theta\sin\theta$ se queda.

3) $\sin\phi\cos\phi = (\frac12\sin\theta + \frac{\sqrt3}{2}\cos\theta)(\frac12\cos\theta - \frac{\sqrt3}{2}\sin\theta)$.

Desarrollemos el producto: 
$= \frac12\sin\theta \cdot \frac12\cos\theta - \frac12\sin\theta\cdot\frac{\sqrt3}{2}\sin\theta + \frac{\sqrt3}{2}\cos\theta\cdot\frac12\cos\theta - \frac{\sqrt3}{2}\cos\theta\cdot\frac{\sqrt3}{2}\sin\theta$
$= \frac14\sin\theta\cos\theta - \frac{\sqrt3}{4}\sin^2\theta + \frac{\sqrt3}{4}\cos^2\theta - \frac34\sin\theta\cos\theta$
$= (\frac14 - \frac34)\sin\theta\cos\theta + \frac{\sqrt3}{4}(\cos^2\theta - \sin^2\theta)$
$= -\frac12\sin\theta\cos\theta + \frac{\sqrt3}{4}\cos2\theta$.

Entonces:

$E = 2\cos\theta\sin\phi - \cos\theta\sin\theta - \sin\phi\cos\phi$
$= [\cos\theta\sin\theta + \sqrt3\cos^2\theta] - \cos\theta\sin\theta - [-\frac12\sin\theta\cos\theta + \frac{\sqrt3}{4}\cos2\theta]$
$= \sqrt3\cos^2\theta + \frac12\sin\theta\cos\theta - \frac{\sqrt3}{4}\cos2\theta$.

Simplifiquemos. $\cos^2\theta = \frac{1+\cos2\theta}{2}$, $\sin\theta\cos\theta = \frac{\sin2\theta}{2}$, $\cos2\theta = \cos2\theta$.

$E = \sqrt3 \cdot \frac{1+\cos2\theta}{2} + \frac12\cdot\frac{\sin2\theta}{2} - \frac{\sqrt3}{4}\cos2\theta$
$= \frac{\sqrt3}{2} + \frac{\sqrt3}{2}\cos2\theta + \frac14\sin2\theta - \frac{\sqrt3}{4}\cos2\theta$
$= \frac{\sqrt3}{2} + \frac{\sqrt3}{4}\cos2\theta + \frac14\sin2\theta$.

Entonces:
$$[QXYR] = 676\left(\frac{\sqrt3}{2} + \frac{\sqrt3}{4}\cos2\theta + \frac14\sin2\theta\right) + 169\sqrt3.$$

Pero $676 = 4\times 169$. Entonces:
$$[QXYR] = 169\left(4\cdot\frac{\sqrt3}{2} + 4\cdot\frac{\sqrt3}{4}\cos2\theta + 4\cdot\frac14\sin2\theta\right) + 169\sqrt3$$
$$= 169\left(2\sqrt3 + \sqrt3\cos2\theta + \sin2\theta\right) + 169\sqrt3.$$

Tenemos $\sqrt3\cos2\theta + \sin2\theta$ que no conocemos aún, pero tenemos $3\cos2\theta + \sqrt3\sin2\theta = 528/169$.

Podemos calcular $\sqrt3\cos2\theta + \sin2\theta$ a partir de la otra ecuación. Notemos que $3\cos2\theta + \sqrt3\sin2\theta = \sqrt3(\sqrt3\cos2\theta + \sin2\theta)$. 

Sí: $\sqrt3 \cdot \sqrt3 = 3$. Entonces $\sqrt3\cos2\theta + \sin2\theta = \frac{1}{\sqrt3}\cdot\frac{528}{169} = \frac{528}{169\sqrt3} = \frac{528\sqrt3}{169\cdot 3} = \frac{176\sqrt3}{169}$.

Excelente. Entonces:
$$[QXYR] = 169\left(2\sqrt3 + \frac{176\sqrt3}{169}\right) + 169\sqrt3.$$

$= 169\cdot 2\sqrt3 + 169 \cdot \frac{176\sqrt3}{169} + 169\sqrt3$
$= 338\sqrt3 + 176\sqrt3 + 169\sqrt3$
$= (338 + 176 + 169)\sqrt3 = 683\sqrt3$.

Por tanto $n = 683$.

Verifiquemos la consistencia para asegurar que no cometimos error de signo u orientación. También debemos verificar la condición de hipotenusa $QR = 4\sqrt{301}$, que equivale a $a^2 + b^2 = 4816$, lo cual impusimos y de ahí obtuvimos $528/169$. Pero queremos verificar soluciones reales y que correspondan a $\phi - \theta = 60^\circ$ (no $-60^\circ$).

De la ecuación $\cos(2\theta - 30^\circ) = 88\sqrt3/169 \approx 0.9017$. Entonces $2\theta - 30^\circ = \pm \arccos(0.9017) \approx \pm 25.6^\circ$.

Caso 1: $2\theta - 30^\circ = 25.6^\circ$, $2\theta = 55.6^\circ$, $\theta \approx 27.8^\circ$. Entonces $\phi = \theta + 60^\circ \approx 87.8^\circ$. Ambos ángulos en $(0,90^\circ)$, lo cual es consistente con $X$ e $Y$ dentro del primer cuadrante (ángulos agudos).

Caso 2: $2\theta - 30^\circ = -25.6^\circ$, $2\theta = 4.4^\circ$, $\theta \approx 2.2^\circ$. $\phi = \theta + 60^\circ \approx 62.2^\circ$. También válido.

Ambos casos dan configuraciones válidas. En ambos, $b = 52\sin\phi$ y $a=52\cos\theta$.

Calculemos $QR$ para verificar. En el caso 1: $\phi \approx 87.8^\circ$, $\sin\phi \approx 0.9993$, $b \approx 51.96$. $\theta \approx 27.8^\circ$, $\cos\theta \approx 0.884$, $a \approx 45.97$. $a^2+b^2 \approx 2113 + 2699 = 4812 \approx 4816$. Bien.

Revisemos el valor clave $528/169$: De $3\cos2\theta + \sqrt3 \sin2\theta = 528/169$, con $2\theta \approx 55.6^\circ$: $\cos55.6^\circ \approx 0.565$, $\sin55.6^\circ \approx 0.825$. $3(0.565) + 1.732(0.825) = 1.694 + 1.429 = 3.123$. Y $528/169 = 3.124$. ✓.

Entonces el resultado es consistente.

Ahora, revisemos si hay otra configuración donde el ángulo $\angle XPY$ sea $60^\circ$ pero con orientación tal que $\phi - \theta = -60^\circ$ (es decir, $Y$ más cerca del eje x que $X$). Eso correspondería a intercambiar roles, quizá $X$ e $Y$ intercambiados, pero el cuadrilátero $QXYR$ y su área deberían ser los mismos por simetría del problema (aunque el triángulo no es simétrico, las condiciones son simétricas al intercambiar $P \to P$, $Q \leftrightarrow R$, $X \leftrightarrow Y$). El área de $QXYR$ es invariante bajo esa simetría, así que el valor $n$ debe ser el mismo. De todas formas, la formulación del problema sugiere unicidad.

Verifico también el caso $\phi - \theta = -60^\circ$; repetiríamos con $\phi = \theta - 60^\circ$, y obtendríamos análogo resultado, con área igual porque la simetría del setup garantiza la misma área (intercambio de ejes). Confío en que $n=683$.

Hagamos una verificación numérica directa para mayor seguridad.

Construyamos una solución numérica: caso 2 con $\theta \approx 2.2^\circ$, $\phi \approx 62.2^\circ$.

$a = 52\cos\theta \approx 52 \times 0.99926 \approx 51.96$.
$b = 52\sin\phi \approx 52 \times 0.88445 \approx 45.99$.

$h_1 = 26\sin\theta \approx 26 \times 0.0384 = 0.998 \approx 1.0$.
$k_2 = 26\cos\phi \approx 26 \times 0.4668 \approx 12.14$.

$X = (a/2, h_1) \approx (25.98, 1.00)$.
$Y = (k_2, b/2) \approx (12.14, 23.00)$.

$XY = \sqrt{(25.98-12.14)^2 + (1.00-23.00)^2} = \sqrt{(13.84)^2 + (-22.0)^2} = \sqrt{191.5 + 484.0} = \sqrt{675.5} \approx 25.99 \approx 26$. ✓.

$QR$: $Q=(a,0) \approx (51.96,0)$, $R=(0,b) \approx (0,45.99)$. $QR = \sqrt{51.96^2 + 45.99^2} = \sqrt{2699.8 + 2115.1} = \sqrt{4814.9} \approx 69.39$. Y $4\sqrt{301} = 4 \times 17.349 = 69.396$. ✓.

Ahora calculemos área de $QXYR$ numéricamente. Usemos el método de los triángulos:

$[PQR] = \frac12 a b = \frac12 (51.96)(45.99) \approx 1195.4$.

$[PQX] = \frac12 a h_1 = \frac12(51.96)(1.00) \approx 25.98$.

$[PYR] = \frac12 b k_2 = \frac12(45.99)(12.14) \approx 279.2$.

$[PXY] = 169\sqrt3 \approx 169 \times 1.73205 = 292.7$.

$[QXYR] = 1195.4 - 25.98 - 279.2 + 292.7 = 1182.9$.

$683\sqrt3 = 683 \times 1.73205 = 1182.99$. ✓ Excelente coincidencia.

Por lo tanto, la respuesta es $n = 683$.

Redondeando la verificación: todo cuadra perfectamente.

Respuesta final: $\boxed