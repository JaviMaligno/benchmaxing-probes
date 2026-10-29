Voy a resolverlo paso a paso.

**1. Coordenadas del triángulo equilátero**

Coloquemos el triángulo equilátero \(ABC\) de lado \(6\) en el plano:

- \(A=(0,0)\)
- \(B=(6,0)\)
- \(C=(3,3\sqrt{3})\)

El circuncentro (que coincide con el baricentro) es:

\[
O=\left(3,\sqrt{3}\right)
\]

y el circunradio es:

\[
R=\frac{6}{\sqrt{3}}=2\sqrt{3}.
\]

La circunferencia circunscrita tiene ecuación:

\[
(x-3)^2+(y-\sqrt{3})^2=12.
\]

---

**2. Condición sobre \(P\)**

Sabemos que \(P\) está dentro del triángulo y

\[
\angle BPC=120^\circ.
\]

Para puntos \(P\) que ven al segmento \(BC\) bajo un ángulo de \(120^\circ\), el lugar geométrico es un arco de circunferencia.

El segmento \(BC\) mide \(6\). Para un ángulo de \(120^\circ\), el centro del arco correspondiente forma un ángulo central de \(2\cdot 120^\circ=240^\circ\), es decir el arco mayor. El centro está en el lado de \(A\) respecto a \(BC\).

Calculemos ese centro. La recta \(BC\) tiene pendiente:

\[
\frac{3\sqrt{3}-0}{3-6}=-\sqrt{3}.
\]

La mediatriz de \(BC\) pasa por el punto medio \(M_{BC}=\left(\frac{9}{2},\frac{3\sqrt{3}}{2}\right)\) y por \(A=(0,0)\), ya que \(A\) equidista de \(B\) y \(C\).

---

El punto \(P\) con \(\angle BPC=120^\circ\) dentro del triángulo está sobre el arco menor de la circunferencia cuyo centro \(O_P\) está en la mediatriz de \(BC\), del lado de \(A\), y para el cual el ángulo central subtendido por \(BC\) es \(240^\circ\).

La distancia de \(O_P\) a \(B\) y \(C\) debe cumplir:

\[
BC=2r\sin 120^\circ = 2r\cdot \frac{\sqrt{3}}{2}=r\sqrt{3}.
\]

Como \(BC=6\):

\[
r=2\sqrt{3}.
\]

Curiosamente este es el mismo radio que la circunferencia circunscrita. Eso significa que \(O_P\) es justamente el otro punto que forma un triángulo equilátero con \(B\) y \(C\), es decir \(O_P\) es el punto \(A\) si \(A\) viera a \(BC\) bajo \(60^\circ\), pero aquí necesitamos \(120^\circ\) para el ángulo *inscrito*, lo que corresponde a \(P\) sobre la circunferencia circunscrita viendo el arco mayor.

De hecho, **en un triángulo equilátero**, cualquier punto \(P\) del arco \(BC\) menor de la circunferencia circunscrita cumple:

\[
\angle BPC = 120^\circ.
\]

Por lo tanto, \(P\) está sobre el arco menor \(BC\) de la circunferencia circunscrita. Como \(P\) está dentro del triángulo, el arco menor \(BC\) (el que no contiene a \(A\)) queda dentro del triángulo.

Así, \(P\) está sobre la circunferencia circunscrita, en el arco menor \(BC\).

---

**3. Circunferencia con diámetro \(AP\)**

La circunferencia con diámetro \(AP\) tiene por ecuación: todo punto \(Y=(x,y)\) sobre ella cumple

\[
\overrightarrow{AY}\cdot \overrightarrow{PY}=0.
\]

Para la intersección con la circunferencia circunscrita, sea \(X\) el segundo punto de corte.

Sabemos que el ángulo \(\angle AXP=90^\circ\), por ser \(AP\) diámetro. Como \(X\) y \(P\) están sobre la circunferencia circunscrita, el cuadrilátero \(AXPC\) es cíclico (con \(A,X,P,C\) sobre la circunferencia circunscrita).

---

**4. Geometría clave**

Dado que \(A,X,P\) están sobre la circunferencia circunscrita y \(\angle AXP=90^\circ\), por el teorema del ángulo inscrito, el arco \(AP\) (el que no contiene a \(X\)) mide \(180^\circ\). Por lo tanto, \(AP\) es un diámetro de la circunferencia circunscrita.

Así, \(A\) y \(P\) son puntos antipodales en la circunferencia circunscrita. Luego:

\[
AP=2R=4\sqrt{3}.
\]

---

**5. Posición de \(P\)**

Como \(P\) es antipodal de \(A=(0,0)\), y el centro es \(O=(3,\sqrt{3})\), entonces:

\[
P = 2O - A = (6, 2\sqrt{3}).
\]

Verifiquemos que \(P\) está en el arco menor \(BC\). El punto \(B=(6,0)\) y \(C=(3,3\sqrt{3})\). El arco menor va de \(B\) a \(C\) pasando por el lado derecho. El punto \((6,2\sqrt{3})\) está justo sobre la recta vertical \(x=6\), entre \(B\) y la altura. Efectivamente está en el arco menor \(BC\), es decir dentro del triángulo (en la frontera, sobre la recta \(BC\)? Veamos).

La recta \(BC\) tiene ecuación:

\[
y=-\sqrt{3}x+6\sqrt{3}.
\]

Para \(x=6\): \(y=0\), no \(2\sqrt{3}\). Así que \(P=(6,2\sqrt{3})\) está dentro del triángulo.

Comprobemos \(\angle BPC\): \(B=(6,0)\), \(C=(3,3\sqrt{3})\), \(P=(6,2\sqrt{3})\).

Vectores \(\overrightarrow{PB}=(0,-2\sqrt{3})\) y \(\overrightarrow{PC}=(-3,\sqrt{3})\).

Producto punto:

\[
(0)(-3)+(-2\sqrt{3})(\sqrt{3})=-6.
\]

Normas: \(|PB|=2\sqrt{3}\), \(|PC|=\sqrt{9+3}=2\sqrt{3}\).

Así:

\[
\cos\angle BPC=\frac{-6}{(2\sqrt{3})^2}=-\frac{6}{12}=-\frac12,
\]

luego \(\angle BPC=120^\circ\). ¡Correcto!

---

**6. Hallar \(X\)**

El círculo con diámetro \(AP\), donde \(A=(0,0)\) y \(P=(6,2\sqrt{3})\), tiene centro

\[
M=\left(3,\sqrt{3}\right)=O.
\]

¡El círculo con diámetro \(AP\) tiene el mismo centro que la circunferencia circunscrita! Su radio es:

\[
\frac{AP}{2}=2\sqrt{3},
\]

es decir **es la misma circunferencia circunscrita**. En ese caso coinciden completamente y \(X\) no está bien definido como intersección "de nuevo".

Hmm, pero el enunciado dice que se cortan de nuevo en \(X\neq A\) y que \(AX=5\). Entonces \(P\) no puede ser antipodal, porque si lo fuera, las circunferencias coincidirían.

Esto sugiere que mi deducción de \(\angle AXP=90^\circ\) implicando que \(AP\) es diámetro de la circunferencia circunscrita es correcta, pero quizá hay más de una posibilidad para \(P\): el punto \(P\) no tiene por qué estar en la circunferencia circunscrita.

Revisemos: \(\angle BPC=120^\circ\). Para que un punto interior vea \(BC\) bajo \(120^\circ\), el lugar geométrico es un arco de una circunferencia distinta (no necesariamente la circunscrita). El centro de esa circunferencia estaría en la mediatriz de \(BC\).

La circunferencia que pasa por \(B,C\) y cuyo arco menor produce ángulo inscrito \(120^\circ\) es: el ángulo inscrito \(120^\circ\) corresponde a un arco mayor de \(240^\circ\), luego el ángulo central menor es \(360^\circ-240^\circ=120^\circ\). Entonces \(O_P\) debe ver a \(BC\) bajo un ángulo central de \(120^\circ\), no \(240^\circ\).

Así, el radio \(r\) cumple:

\[
BC=2r\sin 60^\circ = r\sqrt{3} \implies r=2\sqrt{3}.
\]

Otra vez \(r=2\sqrt{3}\). El centro está en la mediatriz de \(BC\), del lado de \(A\) o del lado opuesto. Para que \(P\) esté dentro del triángulo, el centro \(O_P\) debe estar del lado opuesto a \(A\) respecto de \(BC\), y el arco menor que contiene a \(P\) queda cerca de \(BC\), es decir dentro del triángulo.

La mediatriz de \(BC\) es la recta que pasa por \(A=(0,0)\) y \(M_{BC}=(4.5,\frac{3\sqrt{3}}2)\), de ecuación \(y=\frac{x}{\sqrt{3}}\).

El centro \(O_P\) está sobre esta mediatriz, a distancia \(r\cos 60^\circ = r/2=\sqrt{3}\) de la recta \(BC\), del lado opuesto a \(A\).

La recta \(BC\) a distancia \(\sqrt{3}\) del lado opuesto a \(A\): la recta paralela a \(BC\) a esa distancia. El punto de la mediatriz \(y=x/\sqrt{3}\) que cumple esto nos da \(O_P\).

Distancia de un punto \((x,y)\) a la recta \(BC: y+\sqrt{3}x-6\sqrt{3}=0\):

\[
d=\frac{|y+\sqrt{3}x-6\sqrt{3}|}{\sqrt{1+3}}=\frac{|y+\sqrt{3}x-6\sqrt{3}|}{2}.
\]

Para \(A=(0,0)\): \(d_A=\frac{6\sqrt{3}}{2}=3\sqrt{3}\), que es la altura del triángulo, correcto.

Para \(O_P\) del lado opuesto a \(A\), la distancia a \(BC\) es \(\sqrt{3}\), así:

\[
\frac{|y+\sqrt{3}x-6\sqrt{3}|}{2}=\sqrt{3}.
\]

Sustituyendo \(y=x/\sqrt{3}=\frac{x}{\sqrt{3}}\):

\[
\frac{|x/\sqrt{3}+\sqrt{3}x-6\sqrt{3}|}{2}=\sqrt{3}.
\]

\[
x/\sqrt{3}+\sqrt{3}x=x\left(\frac{1}{\sqrt{3}}+\sqrt{3}\right)=x\cdot\frac{4}{\sqrt{3}}.
\]

Entonces:

\[
\frac{|4x/\sqrt{3}-6\sqrt{3}|}{2}=\sqrt{3}.
\]

\[
|4x/\sqrt{3}-6\sqrt{3}|=2\sqrt{3}.
\]

Dividimos por \(2\sqrt{3}/\sqrt{3}\)... Mejor resolvamos directamente.

Multiplicando todo por \(\sqrt{3}\):

\[
|4x-18|=6.
\]

Dos casos:

- \(4x-18=6 \implies x=6\), \(y=2\sqrt{3}\). Ese es el punto antipodal de \(A\) que ya vimos, correspondiente al centro que ve \(BC\) bajo \(120^\circ\).

- \(4x-18=-6 \implies x=3\), \(y=\sqrt{3}\), que es el centro \(O\) de la circunferencia circunscrita, que ve \(BC\) bajo \(120^\circ\) (central). Pero ese daría una circunferencia de radio \(2\sqrt{3}\) idéntica a la circunscrita, y en ese caso \(P\) estaría en el arco menor, y de nuevo tendríamos coincidencia si \(AP\) es diámetro.

Espera, necesito replantear. El centro correcto para que \(P\) interior vea \(BC\) bajo \(120^\circ\) debe estar del lado opuesto a \(A\) (para que el arco curvo quede dentro del triángulo). El punto \(x=6,y=2\sqrt{3}\) está del lado de \(A\) o opuesto a \(A\)?

Evaluemos la recta \(BC\): \(y+\sqrt{3}x-6\sqrt{3}\). Para \(O_P=(6,2\sqrt{3})\):

\[
2\sqrt{3}+6\sqrt{3}-6\sqrt{3}=2\sqrt{3}>0.
\]

Para \(A=(0,0)\): valor \(=-6\sqrt{3}<0\). Entonces \(O_P\) está en el lado opuesto a \(A\). ¡Correcto!

Para \(O_P=O=(3,\sqrt{3})\):

\[
\sqrt{3}+3\sqrt{3}-6\sqrt{3}=-2\sqrt{3}<0,
\]

mismo lado que \(A\). Descartado.

Así, el lugar geométrico de \(P\) (dentro del triángulo, con \(\angle BPC=120^\circ\)) es el arco menor de la circunferencia centrada en \(O_P=(6,2\sqrt{3})\) de radio \(2\sqrt{3}\), que pasa por \(B\) y \(C\), y va por dentro del triángulo.

**Importante:** \(O_P=(6,2\sqrt{3})\) es justamente el punto antipodal de \(A\) en la circunferencia circunscrita. Y el radio \(2\sqrt{3}\) es igual al circunradio.

---

**7. Relación entre ambas circunferencias**

Tenemos dos circunferencias de radio \(2\sqrt{3}\):

- Circunferencia circunscrita \(\Gamma\), centro \(O=(3,\sqrt{3})\).
- Circunferencia del lugar de \(P\), centro \(O_P=(6,2\sqrt{3})\).

La distancia entre centros:

\[
OO_P=\sqrt{(6-3)^2+(2\sqrt{3}-\sqrt{3})^2}=\sqrt{9+3}=2\sqrt{3}.
\]

Como la distancia entre centros es igual al radio común, son circunferencias tangentes exteriormente. Se cortan en un único punto: el punto de tangencia. ¿Cuál es? Está en la recta que une los centros.

Recta que une \(O=(3,\sqrt{3})\) y \(O_P=(6,2\sqrt{3})\): vector \((3,\sqrt{3})\), pendiente \(1/\sqrt{3}\). Tangente a ambas en el punto medio entre centros extendido.

El punto de tangencia está a distancia \(2\sqrt{3}\) de \(O\) en dirección a \(O_P\), o sea:

\[
T=O+\frac{O_P-O}{2}=(4.5, 1.5\sqrt{3}).
\]

Pero \(T\) debe ser \(B\) o \(C\)? Verifiquemos: \(B=(6,0)\) no. \(C=(3,3\sqrt{3})\) no. \(T=(4.5, 1.5\sqrt{3})\) es el punto medio de \(B\) y \(C\)... De hecho \(M_{BC}=(4.5,1.5\sqrt{3})\). Sí, \(T=M_{BC}\), el punto medio del lado \(BC\).

Entonces \(\Gamma\) y la circunferencia de \(P\) son tangentes en el punto medio de \(BC\), y se cortan solo ahí. Por lo tanto el arco de \(P\) interior no vuelve a tocar \(\Gamma\); \(P\) está en el interior sobre un arco que va desde \(B\) hasta \(C\) pasando cerca de \(BC\), sin tocar \(\Gamma\) salvo en \(B\) y \(C\).

---

**8. Vuelta al problema de \(X\)**

Ahora, \(X\) es el segundo punto de intersección del círculo con diámetro \(AP\) y la circunferencia circunscrita \(\Gamma\).

El círculo con diámetro \(AP\) tiene centro \(M\), punto medio de \(A\) y \(P\), y radio \(AP/2\).

Sea \(A=(0,0)\). Parametricemos \(P\) en el arco interior.

Sabemos que \(X\) está en \(\Gamma\) y cumple \(\angle AXP=90^\circ\) y \(AX=5\).

Por el teorema del ángulo inscrito en \(\Gamma\), como \(\angle AXP=90^\circ\), el segmento \(AP\) debe ser un diámetro de \(\Gamma\). Pero ya vimos que si \(AP\) es diámetro, las dos circunferencias coinciden y no hay segundo punto de corte. Salvo que \(P\) no esté en \(\Gamma\).

**Espera, reformulemos.** El ángulo \(\angle AXP=90^\circ\) es un ángulo con vértice \(X\) en \(\Gamma\). No implica directamente que \(AP\) sea diámetro de \(\Gamma\), a menos que \(P\) también esté en \(\Gamma\). ¡Y \(P\) NO está en \(\Gamma\)!

Entonces ese razonamiento falla. \(P\) no está en \(\Gamma\), salvo en \(B\) o \(C\).

---

Por tanto, \(A,X,P\) están sobre el círculo de diámetro \(AP\), con \(\angle AXP=90^\circ\). Los puntos \(A\) y \(X\) están en \(\Gamma\). \(P\) está en otro lugar.

Necesitamos relacionar esto con \(AX=5\) y \(AP\) desconocido.

En el triángulo rectángulo \(AXP\), con ángulo recto en \(X\), se cumple:

\[
AP^2=AX^2+XP^2=25+XP^2.
\]

Necesitamos otra relación para \(XP\).

---

**9. Usar que \(X\in\Gamma\) y \(P\) está en el arco interior**

Como \(A\) y \(X\) están en \(\Gamma\), conocemos la cuerda \(AX=5\) en \(\Gamma\) de radio \(2\sqrt{3}\).

El ángulo central asociado a la cuerda \(AX\):

\[
\sin\frac{\angle AOX}{2}=\frac{AX/2}{R}=\frac{5/2}{2\sqrt{3}}=\frac{5}{4\sqrt{3}}.
\]

Además, \(\angle AXO\) y demás. Pero también podemos ubicar \(X\) en \(\Gamma\).

Más útil: en el círculo de diámetro \(AP\), el ángulo \(\angle AXP=90^\circ\) significa que \(XP\perp XA\).

Además \(\angle BPC=120^\circ\).

Quizá tenga que ver con el teorema de la potencia o con el punto de Miquel. Consideremos la condición sobre \(P\): está sobre el arco centrado en \(O_P\) de radio \(2\sqrt{3}\). La circunferencia \(\Gamma\) pasa por \(A\), \(B\), \(C\) y es tangente a la de \(P\) en \(M_{BC}\).

El punto \(X\) está sobre \(\Gamma\) con \(AX=5\). El círculo de diámetro \(AP\) corta a \(\Gamma\) en \(A\) y \(X\).

Por potencia de \(P\) respecto a \(\Gamma\):

La potencia de \(P\) respecto a \(\Gamma\) es:

\[
\mathrm{Pot}_\Gamma(P) = PO^2 - R^2.
\]

También, como la recta \(PX\) interseca \(\Gamma\) en \(X\) y otro punto \(Y\) (que es la otra intersección de la recta \(PX\) con \(\Gamma\)), tenemos:

\[
PX\cdot PY = \mathrm{Pot}_\Gamma(P).
\]

Pero \(P\) no está necesariamente alineado con \(X\) y otro punto especial.

Por otra parte, el círculo con diámetro \(AP\) corta a \(\Gamma\) en \(A\) y \(X\). La recta \(PX\) es tangente al círculo de diámetro \(AP\) en \(X\) (porque \(PX\perp AX\), y \(AX\) es radio de este círculo en \(X\)? No, el radio en \(X\) es \(MX\), no \(AX\)).

De hecho, en el círculo con diámetro \(AP\), la tangente en \(X\) es perpendicular al radio \(MX\). Como \(\angle AXP=90^\circ\), \(PX\perp AX\). No es la tangente.

---

**10. Potencia del punto \(X\)**

Tomemos potencia de \(X\) respecto a la circunferencia de \(P\) (la centrada en \(O_P\), radio \(2\sqrt{3}\), que pasa por \(B\) y \(C\)).

Como \(P\) está en esa circunferencia y \(X\) está en \(\Gamma\), la potencia de \(X\) respecto a esa circunferencia:

\[
\mathrm{Pot}_{(O_P)}(X)=XO_P^2-(2\sqrt{3})^2.
\]

La recta \(XP\) corta esa circunferencia en \(P\) y en otro punto \(Q\):

\[
XP\cdot XQ = \mathrm{Pot}_{(O_P)}(X).
\]

Pero no conocemos \(XQ\).

Mejor: como \(X\) está en \(\Gamma\) y \(\Gamma\) es tangente a la circunferencia de \(P\) en \(M_{BC}\), la potencia de \(X\) respecto a \(\Gamma\) es cero (por estar en \(\Gamma\)). No ayuda directamente.

---

**11. Enfoque con coordenadas parametrizando \(X\)**

Parametricemos \(X\) en \(\Gamma\):

\[
X=(3+2\sqrt{3}\cos\theta,\ \sqrt{3}+2\sqrt{3}\sin\theta).
\]

La condición \(AX=5\):

\[
AX^2=(3+2\sqrt{3}\cos\theta)^2+(\sqrt{3}+2\sqrt{3}\sin\theta)^2=25.
\]

Desarrollemos:

\[
=9+12\sqrt{3}\cos\theta+12\cos^2\theta +3+12\sin\theta+12\sin^2\theta.
\]

\[
=12+12+12\sqrt{3}\cos\theta+12\sin\theta = 24+12(\sqrt{3}\cos\theta+\sin\theta)=25.
\]

Por tanto:

\[
\sqrt{3}\cos\theta+\sin\theta=\frac{1}{12}.
\]

Esto da dos posibles \(\theta\), correspondientes a las dos posiciones de \(X\) con \(AX=5\) (simétricas respecto a \(OA\)).

Ahora, \(P\) está en la circunferencia centrada en \(O_P=(6,2\sqrt{3})\) de radio \(2\sqrt{3}\):

\[
P=(6+2\sqrt{3}\cos\phi,\ 2\sqrt{3}+2\sqrt{3}\sin\phi).
\]

Además \(P\) debe cumplir \(\angle BPC=120^\circ\), que ya está garantizado por estar en esa circunferencia (arco interior). Y \(P\) dentro del triángulo acota \(\phi\).

La condición crucial: \(X\) está en el círculo con diámetro \(AP\). Es decir, \(\overrightarrow{AX}\cdot \overrightarrow{XP}=0\).

Equivalentemente, \((X-A)\cdot (P-X)=0\):

\[
X\cdot (P-X)=0 \iff X\cdot P - |X|^2=0.
\]

Como \(|X|^2=AX^2=25\):

\[
X\cdot P = 25.
\]

¡Esta es una relación clave!

---

**12. Usar \(X\cdot P=25\)**

Calculemos \(X\cdot P\) en coordenadas.

\[
X\cdot P = (3+2\sqrt{3}c)(6+2\sqrt{3}p) + (\sqrt{3}+2\sqrt{3}s)(2\sqrt{3}+2\sqrt{3}q),
\]

donde \(c=\cos\theta\), \(s=\sin\theta\), \(p=\cos\phi\), \(q=\sin\phi\).

Desarrollemos:

Primer término:

\[
18+6\sqrt{3}c+6\sqrt{3}p+12cp.
\]

Segundo término:

\[
(\sqrt{3}+2\sqrt{3}s)(2\sqrt{3}+2\sqrt{3}q)
= \sqrt{3}\cdot 2\sqrt{3}(1+q) + 2\sqrt{3}s\cdot 2\sqrt{3}(1+q)
= 6(1+q)+12s(1+q).
\]

\[
=6+6q+12s+12sq.
\]

Sumando:

\[
X\cdot P=24+6\sqrt{3}(c+p)+6q+12s+12(cp+sq).
\]

Debe cumplirse \(X\cdot P=25\):

\[
24+6\sqrt{3}(c+p)+6q+12s+12(cp+sq)=25.
\]

Tenemos también \(\sqrt{3}c+s=1/12\), es decir \(s=\frac{1}{12}-\sqrt{3}c\).

Y \(P\) está en la circunferencia de radio \(2\sqrt{3}\) centrada en \(O_P\), y dentro del triángulo.

Además, no hemos usado que \(X\) está en el círculo con diámetro \(AP\), que es lo que da \(X\cdot P=25\). Bien.

También sabemos que \(P\) está dentro, y probablemente hay una única solución para \(\phi\) dado \(\theta\), y el valor de \(XP\) será el mismo para ambas posiciones de \(X\).

---

**13. Otra relación: \(P\) sobre el círculo de diámetro \(AP\)...**

En realidad \(P\) siempre está sobre el círculo de diámetro \(AP\) trivialmente. La condición es que \(X\) esté sobre ese círculo, que ya usamos.

Necesitamos una relación adicional para determinar \(\phi\) en función de \(\theta\). ¿Qué otra condición hay?

Quizá \(P\) no es arbitrario en ese arco: también debe cumplir que el círculo con diámetro \(AP\) pase por \(X\), pero esto ya nos dio una ecuación. Aun así, tenemos dos incógnitas \((\theta,\phi)\) y una sola ecuación escalar \(X\cdot P=25\), más la relación \(\sqrt{3}c+s=1/12\) (que fija \(\theta\) salvo signo). Entonces \(X\) está esencialmente fijado (dos opciones), y para cada \(X\) la ecuación \(X\cdot P=25\) fija a \(P\) como intersección de una recta con el arco.

La recta es \(X\cdot P=25\), que como \(P\) está sobre la circunferencia centrada en \(O_P\), se resuelve explícitamente.

Eso nos daría \(P\), y luego \(XP=|P-X|\).

Hagámoslo simbólicamente.

---

**14. Resolver para \(\theta\)**

De \(s=\frac{1}{12}-\sqrt{3}c\) y \(c^2+s^2=1\):

\[
c^2+\left(\frac{1}{12}-\sqrt{3}c\right)^2=1.
\]

\[
c^2+\frac{1}{144}-\frac{\sqrt{3}}{6}c+3c^2=1.
\]

\[
4c^2-\frac{\sqrt{3}}{6}c+\frac{1}{144}-1=0.
\]

\[
4c^2-\frac{\sqrt{3}}{6}c-\frac{143}{144}=0.
\]

Multiplicamos por 144:

\[
576c^2-24\sqrt{3}\,c-143=0.
\]

Resolvemos:

\[
c=\frac{24\sqrt{3}\pm\sqrt{(24\sqrt{3})^2+4\cdot 576\cdot 143}}{2\cdot 576}.
\]

\[
=\frac{24\sqrt{3}\pm\sqrt{1728+329472}}{1152}
=\frac{24\sqrt{3}\pm\sqrt{331200}}{1152}.
\]

\[
\sqrt{331200}=\sqrt{3312\cdot 100}=10\sqrt{3312}=10\sqrt{144\cdot 23}=120\sqrt{23}.
\]

Entonces:

\[
c=\frac{24\sqrt{3}\pm 120\sqrt{23}}{1152}
=\frac{24(\sqrt{3}\pm 5\sqrt{23})}{1152}
=\frac{\sqrt{3}\pm 5\sqrt{23}}{48}.
\]

Esto me parece sospechosamente complicado; quizá me equivoqué en el desarrollo del ángulo.

---

**Verifiquemos el desarrollo de \(AX^2\):**

\(X=(3+2\sqrt{3}c,\ \sqrt{3}+2\sqrt{3}s)\).

\[
AX^2 = (3+2\sqrt{3}c)^2 + (\sqrt{3}+2\sqrt{3}s)^2.
\]

\[
=9+12\sqrt{3}c+12c^2 + 3+12s+12s^2.
\]

\[
=12+12(c^2+s^2)+12\sqrt{3}c+12s.
\]

\[
=12+12+12\sqrt{3}c+12s=24+12\sqrt{3}c+12s.
\]

Igual a 25:

\[
12\sqrt{3}c+12s=1 \implies \sqrt{3}c+s=\frac{1}{12}.
\]

Correcto.

El resultado con \(\sqrt{23}\) es feo; quizá el problema busca algo más simple y hay un camino mejor.

---

**15. Camino alternativo: geometría más elegante**

Observemos que el círculo con diámetro \(AP\) corta a \(\Gamma\) en \(A\) y \(X\). La potencia de \(O\) (centro de \(\Gamma\)) respecto al círculo de diámetro \(AP\) puede ayudar, o el eje radical.

El eje radical de \(\Gamma\) y del círculo de diámetro \(AP\) es la recta \(AX\).

La potencia del punto \(O\) respecto al círculo de diámetro \(AP\): el centro de este círculo es \(M\), punto medio de \(AP\). La potencia de \(O\) respecto a ese círculo:

\[
\mathrm{Pot}(O)=OM^2-(AP/2)^2.
\]

Por otro lado, como la recta \(OA\) corta a ese círculo en \(A\) y otro punto \(A'\) (reflejado de \(A\) respecto a \(M\)), no sé si ayuda.

La recta \(AX\), que es el eje radical, cumple \(d(O,\text{recta }AX)\) relacionada con la cuerda \(AX\) de \(\Gamma\).

Quizá la condición \(AX=5\) se traduzca en la distancia del centro \(O\) a la recta \(AX\). En la circunferencia de radio \(R=2\sqrt{3}\), la distancia del centro a la cuerda \(AX=5\) es:

\[
d=\sqrt{R^2-(AX/2)^2}=\sqrt{12-\frac{25}{4}}=\sqrt{\frac{23}{4}}=\frac{\sqrt{23}}{2}.
\]

¡Ahí está el \(\sqrt{23}\) de nuevo! Así que es esperable.

---

**16. Potencia de \(O\) respecto al círculo de diámetro \(AP\)**

El eje radical de ambos círculos es la recta \(AX\). La potencia del punto \(O\) respecto al círculo de diámetro \(AP\) debe ser igual a la potencia de \(O\) respecto a \(\Gamma\), que es \(-R^2\)? No, \(O\) es el centro de \(\Gamma\), su potencia respecto a \(\Gamma\) es \(-R^2=-12\).

La potencia de \(O\) respecto al círculo de diámetro \(AP\) es:

\[
OM^2-r_{AP}^2,
\]

donde \(M\) es el centro del círculo de diámetro \(AP\), \(r_{AP}=AP/2\).

\[
\mathrm{Pot}_{(M)}(O)=OM^2-(AP/2)^2.
\]

Esta potencia debe ser igual a \(-12\)? No, no tiene por qué. El eje radical es el lugar de puntos con igual potencia respecto a ambos círculos. \(O\) no está en el eje radical necesariamente.

---

**17. Enfoque con \(X\cdot P=25\) y el arco de \(P\)**

Retomemos. Teníamos:

\[
X\cdot P=25,
\]

con \(X\) conocido salvo el signo, y \(P\) sobre la circunferencia centrada en \(O_P=(6,2\sqrt{3})\).

Escribamos esto geométricamente. Para un \(X\) fijo sobre \(\Gamma\), los \(P\) que cumplen \(X\cdot P=25\) están sobre una recta perpendicular al vector \(X\) (ya que \(X\cdot P=|X|\, (\text{proyección})=25\), y \(|X|=5\), entonces la proyección de \(P\) sobre la dirección de \(X\) es \(25/5=5=|X|\)). Es decir:

La proyección de \(P\) sobre \(OX\) (dirección radial \(OA\)... cuidado, \(X\) no es paralelo a \(OA\)).

Como \(|X|=5\), la condición \(X\cdot P=25=5\cdot 5\) significa que la proyección de \(P\) sobre la dirección de \(X\) es exactamente \(|X|=5\). Como \(P\) tiene módulo... no sabemos.

Esto no simplifica mucho.

---

**18. Triángulo rectángulo \(AXP\) con \(P\) en el arco**

Tal vez haya una relación pitagórica usando la distancia de \(P\) a \(B\) y \(C\), o usando la ley de cosenos en \(BPC\) con \(BC=6\).

Sabemos \(BP=CP\)? No, \(P\) no está necesariamente en la mediatriz de \(BC\).

Sin embargo, el arco donde está \(P\) es simétrico respecto a la mediatriz \(AM\). El punto \(P\) no tiene por qué estar en esa mediatriz.

Pero quizá por la condición del círculo de diámetro \(AP\), \(X\) con \(AX=5\), y por simetría, la solución sea única y quizá \(P\) esté en la mediatriz de \(BC\). Si \(P\) estuviera en la mediatriz, tendríamos \(BP=CP\), y el triángulo \(BPC\) es isósceles con ángulo en \(P\) de \(120^\circ\), luego ángulos en \(B\) y \(C\) de \(30^\circ\). Entonces \(BP=CP=\frac{BC}{2}/\sin 60^\circ = 3/(\sqrt{3}/2)=2\sqrt{3}\). Es decir \(BP=CP=2\sqrt{3}\), y \(P\) sería el centro \(O\) de \(\Gamma\)... pero \(O\) no está en el arco interior (está del lado de \(A\)). Espera, \(P\) interior con \(BP=CP=2\sqrt{3}\) y \(\angle BPC=120^\circ\): el punto \(O=(3,\sqrt{3})\) está dentro del triángulo, y verifica \(\angle BOC=120^\circ\). ¡Sí! \(O\) está dentro del triángulo y ve \(BC\) bajo \(120^\circ\). Pero antes descarté \(O\) porque "mismo lado que \(A\)" para el centro del arco; pero \(O\) es un punto interior válido con \(\angle BOC=120^\circ\). Revisemos:

\(O=(3,\sqrt{3})\), \(B=(6,0)\), \(C=(3,3\sqrt{3})\).

Vectores: \(\overrightarrow{OB}=(3,-\sqrt{3})\), \(\overrightarrow{OC}=(0,2\sqrt{3})\).

Producto punto: \(3\cdot0+(-\sqrt{3})(2\sqrt{3})=-6\).

Normas: \(|OB|=\sqrt{9+3}=2\sqrt{3}\), \(|OC|=2\sqrt{3}\).

\(\cos=\frac{-6}{12}=-\frac12\), ángulo \(120^\circ\). ¡Correcto!

Entonces \(O\) es un punto válido. Pero además, ¿hay otros puntos interior con \(\angle BPC=120^\circ\)? Sí, todo el arco de la circunferencia que pasa por \(B,C,O\). El centro de esa circunferencia es \(O_P=(6,2\sqrt{3})\)? Verifiquemos: esa circunferencia pasa por \(B\), \(C\) y \(O\). Su centro debe equidistar de ellos.

Distancia de \(O_P=(6,2\sqrt{3})\) a \(O=(3,\sqrt{3})\):

\[
\sqrt{3^2+3}=2\sqrt{3}.
\]

A \(B=(6,0)\):

\[
\sqrt{0+12}=2\sqrt{3}.
\]

A \(C=(3,3\sqrt{3})\):

\[
\sqrt{9+3}=2\sqrt{3}.
\]

¡Sí! Entonces \(O_P\) es el centro, y la circunferencia pasa por \(B,C,O\). El arco interior (dentro del triángulo) va de \(B\) a \(C\) y pasa por \(O\). Y \(O\) es el punto más alejado de \(BC\) en ese arco (el vértice del arco, sobre la mediatriz).

Así \(P\) recorre ese arco interior desde \(B\) hasta \(C\) pasando por \(O\).

---

**19. Simetría y unicidad de \(XP\)**

Si \(P\) no está en la mediatriz, el problema aún podría tener dos soluciones simétricas para \(P\), dando el mismo \(XP\)? No necesariamente, porque \(X\) también cambia.

Pero es plausible que la solución con \(AX=5\) sea única salvo simetría, y que el valor de \(XP\) sea el mismo por simetría.

Consideremos el caso simétrico: \(P=O\) sobre la mediatriz, y \(X\) uno de los dos puntos con \(AX=5\), simétricos respecto a \(OA\).

¿Está \(X\) sobre el círculo con diámetro \(AO\)?

Como \(O\) es centro de \(\Gamma\), \(AO=R=2\sqrt{3}\). El círculo con diámetro \(AO\) tiene centro \(M=(1.5,\sqrt{3}/2)\) y radio \(\sqrt{3}\).

¿Corta a \(\Gamma\) en un punto con \(AX=5\)? Veamos si existe tal \(X\).

La condición: \(\angle AXO=90^\circ\), es decir \(X\) debe ver el diámetro \(AO\) bajo ángulo recto. Como \(O\) es centro de \(\Gamma\), la recta \(OX\) es radial. El ángulo entre \(AX\) y \(OX\) (radio) debe ser \(90^\circ\), es decir \(AX\) tangente a \(\Gamma\) en \(X\). Pero \(AX\) es una cuerda por \(A\) y \(X\), no puede ser tangente salvo que \(X=A\). Contradicción.

Por tanto \(P=O\) no funciona (salvo \(X=A\)). Entonces \(P\neq O\), y \(X\) no es el punto de tangencia.

---

**20. Relación fundamental: \(AX\) tangente al círculo de diámetro \(AP\)**

En el círculo con diámetro \(AP\), el punto \(X\) cumple \(\angle AXP=90^\circ\). Además \(A\) y \(X\) están en \(\Gamma\).

Consideremos la tangente a \(\Gamma\) en \(A\). La recta \(AX\) forma un cierto ángulo con esa tangente.

Quizá lo más limpio sea usar trigonometría en el triángulo \(AXP\) y el triángulo \(ABC\).

Sabemos \(AX=5\), \(AP=d\), \(XP=t\), y \(d^2=25+t^2\).

Además, \(\angle AXP=90^\circ\), así que el ángulo en \(A\) del triángulo \(AXP\) es \(\alpha=\angle XAP\), con:

\[
\sin\alpha=\frac{t}{d}, \quad \cos\alpha=\frac{5}{d}.
\]

También en \(\Gamma\), la cuerda \(AX=5\) subtiende un ángulo \(\angle ABX\) o \(\angle ACX\) en la circunferencia.

El ángulo central \(\angle AOX=2\angle ABX\). De la cuerda \(AX=5\), el ángulo inscrito \(\angle ABX\) satisface:

\[
\sin(\angle ABX/2)... \text{ mejor: } \angle AOX = 2\arcsin\frac{AX}{2R}=2\arcsin\frac{5}{4\sqrt{3}}\approx 2\arcsin(0.7217).
\]

No muy simple.

---

**21. ¿Relación entre \(P\) y \(X\) vía ángulos?**

Como \(P\) ve \(BC\) bajo \(120^\circ\), y el triángulo es equilátero, tenemos una configuración rica.

La condición \(\angle BPC=120^\circ\) con \(P\) interior equivale (por el teorema del ángulo inscrito) a que \(P\) está sobre el arco \(BC\) de la circunferencia que pasa por \(B\), \(C\) y \(O\). En particular, \(\angle BOC=120^\circ\) también, y \(O\) está en ese arco.

Entonces \(B,C,O,P\) son concíclicos. La circunferencia que los contiene es \(\omega\) (centro \(O_P\), radio \(2\sqrt{3}\)).

Ahora, \(X\) está sobre \(\Gamma\) (circunscrita) con \(AX=5\), y sobre el círculo de diámetro \(AP\).

El círculo de diámetro \(AP\) y \(\omega\): \(P\) está en ambos trivialmente (en \(\omega\) y en el círculo de diámetro \(AP\)). ¿Se cortan en otro punto? El círculo de diámetro \(AP\) y \(\omega\) se cortan en \(P\) y quizá otro punto \(Y\). ¿Será \(Y\) relevante?

Consideremos la potencia de \(A\) respecto a \(\omega\):

\[
\mathrm{Pot}_\omega(A)=AO_P^2-(2\sqrt{3})^2.
\]

\[
AO_P=\sqrt{(6-0)^2+(2\sqrt{3}-0)^2}=\sqrt{36+12}=\sqrt{48}=4\sqrt{3}.
\]

Entonces:

\[
\mathrm{Pot}_\omega(A)=48-12=36.
\]

Como la recta \(AB\) corta a \(\omega\) en \(B\) y otro punto. \(B\in\omega\). La recta \(AB\) (eje \(x\)) corta a \(\omega\) en \(B=(6,0)\) y en otro punto. Calculemos: \(\omega\) es \((x-6)^2+(y-2\sqrt{3})^2=12\). En \(y=0\):

\[
(x-6)^2+12=12 \implies (x-6)^2=0 \implies x=6.
\]

¡Tangente! La recta \(AB\) es tangente a \(\omega\) en \(B\). Entonces \(A\) está fuera, y la potencia \(36\) implica tangente de longitud \(6\). Efectivamente \(AB=6\), y es tangente en \(B\). Coherente.

Similarmente \(AC=6\) es tangente a \(\omega\) en \(C\).

---

**22. Potencia y semejanza**

Como \(AB\) es tangente a \(\omega\) en \(B\), y \(P\in\omega\), tenemos:

\[
AB^2=36 = \text{potencia de } A.
\]

La recta \(AP\) corta a \(\omega\) en \(P\) y otro punto \(Q\):

\[
AP\cdot AQ = 36.
\]

Pero \(AP=d\), así:

\[
AQ=\frac{36}{d}.
\]

Como \(P\) interior, \(AP\) también corta al arco interior en \(P\) y sale por \(Q\) del otro lado.

Además, \(Q\) está sobre \(\omega\).

Similarmente, el círculo de diámetro \(AP\) interseca a \(\Gamma\) en \(A\) y \(X\). La potencia de \(P\) respecto a \(\Gamma\): \(P\) está dentro de \(\Gamma\) (pues está dentro del triángulo, y el triángulo está dentro de \(\Gamma\) salvo los vértices). La potencia de \(P\):

\[
\mathrm{Pot}_\Gamma(P)=PO^2-R^2=PO^2-12.
\]

La recta \(PA\) corta a \(\Gamma\) en \(A\) y \(A'\) (el otro punto de \(\Gamma\) alineado con \(P,A\)):

\[
PA\cdot PA' = |\mathrm{Pot}_\Gamma(P)|.
\]

Como \(P\) interior, la potencia es negativa, y \(PA\cdot PA'=12-PO^2\).

Pero quizá \(A'\) sea justamente \(X\)? No, \(X\) no está en la recta \(AP\) necesariamente; \(X\) está en el círculo de diámetro \(AP\), y \(\angle AXP=90^\circ\), así que \(XP\perp XA\), y \(X\) en general no está sobre \(AP\).

---

**23. Usar la tangente \(AB\) a \(\omega\)**

La tangencia de \(AB\) y \(AC\) a \(\omega\) sugiere que el triángulo \(ABC\) es tangencial a \(\omega\) en \(B\) y \(C\). De hecho, \(\omega\) es la circunferencia tangente a \(AB\) en \(B\), a \(AC\) en \(C\), que pasa por \(O\) y \(P\).

El círculo con diámetro \(AP\): queremos su segunda intersección \(X\) con \(\Gamma\).

Quizá podamos usar el siguiente hecho: las circunferencias \(\Gamma\) y \(\omega\) son tangentes en el punto medio de \(BC\), digamos \(M\). De hecho \(\Gamma\) y \(\omega\) son tangentes en \(M=(4.5,1.5\sqrt{3})\).

Esto forma una configuración de dos circunferencias tangentes (\(\Gamma\) y \(\omega\)) y un punto \(A\) exterior a ambas, con \(AB,AC\) tangentes a \(\omega\) y \(AB,AC\) cuerdas de \(\Gamma\).

---

**24. Inversión**

Una inversión con centro \(A\) y radio \(6\) (ya que \(AB=AC=6\)) intercambia la recta \(BC\)... Veamos.

Bajo inversión centrada en \(A\) de radio \(6\):

- \(B\to B\) (pues \(AB=6\)).
- \(C\to C\).
- La circunferencia \(\omega\), tangente a \(AB\) en \(B\) y a \(AC\) en \(C\), se transforma en una recta \(\ell\) que pasa por \(B\) y \(C\). ¡Porque una circunferencia que pasa por el centro de inversión? No, \(\omega\) no pasa por \(A\). Una circunferencia que no pasa por el centro de inversión se transforma en otra circunferencia. Pero como \(AB\) y \(AC\) son tangentes a \(\omega\), al invertir, las rectas \(AB\) y \(AC\) (que pasan por el centro \(A\)) se transforman en sí mismas, y \(\omega\) se transforma en una circunferencia tangente a \(AB\) en \(B\) y a \(AC\) en \(C\). ¿Cuál? Podría ser la circunferencia de diámetro... La circunferencia que es tangente a \(AB\) en \(B\), a \(AC\) en \(C\) y que además... hay infinitas; pero \(\omega\) se transforma en otra circunferencia con esas tangencias. La circunferencia que pasa por \(B,C\) y es tangente a \(AB\) en \(B\) y a \(AC\) en \(C\) sería la circunferencia de diámetro \(BC\)? No.

Hmm, esto se complica.

---

**25. Relación directa mediante la potencia de \(A\)**

Retomemos potencias. Sea \(d=AP\), \(t=XP\).

En el círculo de diámetro \(AP\), como \(X\) está sobre él, \(\angle AXP=90^\circ\), y \(t^2=d^2-25\).

La recta \(AP\) es un diámetro de este círculo. La recta \(AP\) corta a \(\Gamma\) en \(A\) y \(A'\).

La potencia del punto \(P\) respecto a \(\Gamma\):

\[
\mathrm{Pot}_\Gamma(P)=PO^2-R^2.
\]

Como \(P\) está sobre \(\omega\), y \(O\) es el centro de \(\Gamma\), podemos calcular \(PO\).

Los centros: \(O=(3,\sqrt{3})\), \(O_P=(6,2\sqrt{3})\), y \(OO_P=2\sqrt{3}\), \(O_OP\) distancia entre centros.

\(P\) está sobre \(\omega\): \(|P-O_P|=2\sqrt{3}\).

Queremos \(PO\). Usemos que \(\Gamma\) y \(\omega\) son tangentes exteriormente en \(M\), y \(P\in\omega\).

El ángulo \(O O_P P\) es el ángulo central en \(\omega\) para el punto \(P\). Sea \(\phi\) el parámetro: \(P=O_P + 2\sqrt{3}(\cos\phi,\sin\phi)\).

Entonces:

\[
PO^2 = |P-O|^2 = |(O_P-O)+2\sqrt{3}(\cos\phi,\sin\phi)|^2.
\]

\(O_P-O=(3,\sqrt{3})\), que tiene módulo \(2\sqrt{3}\).

\[
PO^2 = (2\sqrt{3})^2 + (2\sqrt{3})^2 + 2(2\sqrt{3})(2\sqrt{3})\cos(\text{ángulo entre } O_P-O \text{ y } P-O_P).
\]

El vector \(O_P-O=(3,\sqrt{3})\) apunta de \(O\) a \(O_P\), en dirección \((3,\sqrt{3})\), ángulo \(30^\circ\) respecto al eje \(x\).

El vector \(P-O_P=2\sqrt{3}(\cos\phi,\sin\phi)\) tiene ángulo \(\phi\).

Entonces:

\[
PO^2=12+12+24\cos(\phi-30^\circ)=24+24\cos(\phi-30^\circ).
\]

La potencia de \(P\) respecto a \(\Gamma\):

\[
\mathrm{Pot}_\Gamma(P)=24+24\cos(\phi-30^\circ)-12 =12+24\cos(\phi-30^\circ).
\]

Esta potencia es negativa si \(P\) está dentro de \(\Gamma\) (dentro del triángulo), lo que concuerda.

Ahora, la recta \(PA\) corta \(\Gamma\) en \(A\) y \(A'\). Como \(A\) está en \(\Gamma\), la potencia de \(P\) es:

\[
\mathrm{Pot}_\Gamma(P)=PA\cdot PA' = d\cdot PA',
\]

con signo. Como \(P\) interior, \(PA'\) es la distancia de \(P\) a \(A'\), y el producto \(d\cdot PA'\) con signo negativo; por tanto:

\[
d\cdot PA' = -|\mathrm{Pot}_\Gamma(P)|,
\]

si \(A'\) está del lado opuesto. Cuidado con signos. Usemos la fórmula de potencia: para un punto \(P\) y una circunferencia, para cualquier recta por \(P\) que corta la circunferencia en \(U\) y \(V\), se cumple \(PU\cdot PV=\mathrm{Pot}(P)\) (con signo, considerando distancias dirigidas). Si \(P\) está dentro, \(\mathrm{Pot}<0\), y \(U,V\) están en lados opuestos de \(P\), de modo que \(PU\cdot PV\) dirigidas dan negativo.

Aquí la recta \(PA\) corta en \(A\) y \(A'\). Tomando la recta orientada de \(P\) hacia \(A\), \(PU=PA\) positivo, y \(PV=-PA'\) si \(A'\) está al otro lado; entonces \(PA\cdot (-PA')=\mathrm{Pot}<0\), así \(PA\cdot PA'=-\mathrm{Pot}\).

Luego:

\[
d\cdot PA' = -12-24\cos(\phi-30^\circ).
\]

Puede ser útil para conocer \(A'\), pero no para \(X\) directamente.

---

**26. Relación entre \(X\) y \(\phi\) mediante el círculo de diámetro \(AP\)**

El círculo con diámetro \(AP\) tiene centro \(M=\frac{A+P}{2}\). Su ecuación es \(X\cdot (P-X)=0\) ⇔ \(X\cdot P=|X|^2=25\).

Además \(X\in\Gamma\), con \(|X-3-\sqrt{3}i|=2\sqrt{3}\). En vector: \(|X-O|^2=12\), es decir:

\[
|X|^2-2X\cdot O+|O|^2=12.
\]

\(|O|^2=9+3=12\), \(|X|^2=25\):

\[
25-2X\cdot O+12=12 \implies 25=2X\cdot O \implies X\cdot O=\frac{25}{2}.
\]

Interesante: \(X\cdot O=12.5\).

Esto nos da la proyección de \(X\) sobre \(O\), pero ya sabíamos.

---

**27. Encontrar \(X\) explícitamente (dos opciones)**

De \(\sqrt{3}c+s=1/12\), con \(c^2+s^2=1\), obtenemos \(c\) y \(s\) con el \(\sqrt{23}\). Sigamos; quizá se simplifique al final.

Sea \(c_\pm=\frac{\sqrt{3}\pm 5\sqrt{23}}{48}\).

Ambas soluciones son válidas? \(\sqrt{3}\approx1.732\), \(5\sqrt{23}\approx23.98\). Entonces \(c_+\approx(1.732+23.98)/48\approx0.5356\), \(c_-\approx(1.732-23.98)/48\approx-0.4635\). Ambas en \([-1,1]\), luego hay dos puntos \(X\) con \(AX=5\), simétricos respecto a \(OA\).

Para cada \(X\), la ecuación \(X\cdot P=25\) con \(P\in\omega\) nos da \(P\). Verifiquemos que la intersección de la recta \(X\cdot P=25\) con \(\omega\) existe y da \(P\) interior.

Escribamos \(P=O_P+2\sqrt{3}(\cos\phi,\sin\phi)\).

\[
X\cdot P=X\cdot O_P+2\sqrt{3}(X\cdot u),
\]

donde \(u=(\cos\phi,\sin\phi)\).

\[
X\cdot O_P=(3+2\sqrt{3}c)(6)+(\sqrt{3}+2\sqrt{3}s)(2\sqrt{3}).
\]

Desarrollemos:

\[
=18+12\sqrt{3}c+6+12s = 24+12(\sqrt{3}c+s)=24+12\cdot\frac{1}{12}=25.
\]

¡Qué bonito! \(X\cdot O_P=25\).

Entonces la ecuación \(X\cdot P=25\) se reduce a:

\[
25+2\sqrt{3}\,(X\cdot u)=25 \implies X\cdot u=0.
\]

Es decir, \(u\) es perpendicular a \(X\).

Por tanto, \((\cos\phi,\sin\phi)\) es perpendicular a \(X\). Luego hay dos soluciones para \(u\): \(u=\pm\,\frac{X^\perp}{|X|}\), donde \(X^\perp\) es \(X\) rotado \(90^\circ\).

---

**28. Elegir \(P\) interior**

Tenemos \(u=\pm\,X^\perp/5\). Para determinar cuál da \(P\) interior, notemos que \(P\) debe estar dentro del triángulo.

Recordemos que \(O_P=(6,2\sqrt{3})\). El arco interior va desde \(B=(6,0)\) y \(C=(3,3\sqrt{3})\). Para \(P\) interior, \(u\) debe apuntar hacia la izquierda y hacia dentro.

El punto \(M\) (punto medio de \(BC\)) corresponde a \(u=(-1/2,-\sqrt{3}/2)\)? Calculemos: \(M=(4.5,1.5\sqrt{3})\), \(M-O_P=(-1.5,-0.5\sqrt{3})\), módulo \(=\sqrt{2.25+0.75}=\sqrt{3}\). Espera, el módulo debería ser \(2\sqrt{3}\approx3.464\), pero \(M\) está a distancia \(\sqrt{3}\) de \(O_P\). Revisemos: \(O_P=(6,3.464)\), \(M=(4.5,2.598)\). Diferencia \(=(-1.5,-0.866)\), módulo \(=\sqrt{2.25+0.75}=\sqrt{3}\approx1.732\), no \(2\sqrt{3}\). Contradicción: ¿\(\omega\) no pasa por \(M\)?

Revisemos \(\omega\): centro \(O_P=(6,2\sqrt{3})\), radio \(2\sqrt{3}\). \(M=(4.5,1.5\sqrt{3})\). Distancia \(MO_P=\sqrt{(1.5)^2+(0.5\sqrt{3})^2}=\sqrt{2.25+0.75}=\sqrt{3}\). ¡No es \(2\sqrt{3}\)! Entonces \(\omega\) no pasa por \(M\), y \(\Gamma\) y \(\omega\) NO son tangentes en \(M\).

Recalculemos la distancia entre centros \(O\) y \(O_P\): \(O=(3,\sqrt{3})\), \(O_P=(6,2\sqrt{3})\), diferencia \((3,\sqrt{3})\), módulo \(\sqrt{9+3}=2\sqrt{3}\). Como ambos radios son \(2\sqrt{3}\), la distancia entre centros es igual a un radio, no a la suma de radios. Entonces las circunferencias se cortan en dos puntos, no son tangentes.

Los puntos de intersección de \(\Gamma\) y \(\omega\): resolver.

\[
(x-3)^2+(y-\sqrt{3})^2=12,
\]
\[
(x-6)^2+(y-2\sqrt{3})^2=12.
\]

Restamos la segunda de la primera:

Primera menos segunda:

\[
(x-3)^2-(x-6)^2+(y-\sqrt{3})^2-(y-2\sqrt{3})^2=0.
\]

\[
[(x-3)-(x-6)][(x-3)+(x-6)] + [(y-\sqrt{3})-(y-2\sqrt{3})][(y-\sqrt{3})+(y-2\sqrt{3})]=0.
\]

\[
(3)(2x-9)+(\sqrt{3})(2y-3\sqrt{3})=0.
\]

\[
6x-27+2\sqrt{3}y-9=0.
\]

\[
6x+2\sqrt{3}y-36=0 \implies 3x+\sqrt{3}y=18 \implies \sqrt{3}x+y=6\sqrt{3}.
\]

\[
y=6\sqrt{3}-\sqrt{3}x = \sqrt{3}(6-x).
\]

Esta es la recta que pasa por \(B=(6,0)\) y \(C=(3,3\sqrt{3})\). ¡Es justamente \(BC\)!

Entonces \(\Gamma\) y \(\omega\) se cortan en \(B\) y \(C\). Claro, porque ambas pasan por \(B\) y \(C\). No son tangentes; se cortan en \(B\) y \(C\). El eje radical es \(BC\).

Todo cuadra: \(\omega\) pasa por \(B\) y \(C\), al igual que \(\Gamma\).

---

**29. Continuemos con \(X\cdot P=25\)**

Conservamos el resultado central:

\[
X\cdot P=25 \quad\Longleftrightarrow\quad X\cdot u=0 \quad\Longleftrightarrow\quad u\perp X.
\]

Como \(|X|=5\), las dos soluciones son \(u=\pm\,X^\perp/5\).

Para \(P\) interior, elegimos el signo correcto.

---

**30. Calcular \(XP\)**

\(P=O_P+2\sqrt{3}\,u\) con \(u\perp X\) y \(|u|=1\).

Calculemos \(XP=|P-X|=|O_P-X+2\sqrt{3}u|\).

Como \(u\perp X\), pero \(O_P-X\) no es necesariamente perpendicular a \(X\). Calculemos.

\[
|P-X|^2=|(O_P-X)+2\sqrt{3}u|^2=|O_P-X|^2+12+4\sqrt{3}\,(O_P-X)\cdot u.
\]

Calculemos cada término.

Primero, \(|O_P-X|^2=|O_P|^2+|X|^2-2O_P\cdot X\).

\(|O_P|^2=36+12=48\), \(|X|^2=25\), \(O_P\cdot X=25\) (calculado antes). Entonces:

\[
|O_P-X|^2=48+25-50=23.
\]

Luego,

\[
|P-X|^2=23+12+4\sqrt{3}\,(O_P-X)\cdot u=35+4\sqrt{3}(O_P\cdot u - X\cdot u).
\]

\(X\cdot u=0\), y \(O_P\cdot u\): como \(u\perp X\), \(O_P\cdot u=O_P\cdot\left(\pm\frac{X^\perp}{5}\right)=\pm\frac{O_P\cdot X^\perp}{5}\).

Georgometricamente, \(O_P\cdot X^\perp\) depende de \(X\). Calculemos.

\[
X=O+2\sqrt{3}(\cos\theta,\sin\theta).
\]

Tenemos \(\sqrt{3}c+s=1/12\) y \(c,s\) conocidos con \(\sqrt{23}\).

Podemos simplificar \(O_P\cdot X^\perp\). En coordenadas, \(X=(x,y)\), \(X^\perp=(-y,x)\).

\[
O_P\cdot X^\perp=(6,2\sqrt{3})\cdot(-y,x)=-6y+2\sqrt{3}x.
\]

\(x=3+2\sqrt{3}c\), \(y=\sqrt{3}+2\sqrt{3}s\).

\[
O_P\cdot X^\perp=-6(\sqrt{3}+2\sqrt{3}s)+2\sqrt{3}(3+2\sqrt{3}c)
=-6\sqrt{3}-12\sqrt{3}s+6\sqrt{3}+12c
=12(c-\sqrt{3}s).
\]

Entonces:

\[
O_P\cdot u=\pm\frac{12(c-\sqrt{3}s)}{5}.
\]

Por tanto:

\[
|P-X|^2=35\pm 4\sqrt{3}\cdot \frac{12(c-\sqrt{3}s)}{5}
=35\pm \frac{48\sqrt{3}(c-\sqrt{3}s)}{5}.
\]

Calculemos \(c-\sqrt{3}s\). Recordemos \(\sqrt{3}c+s=1/12\), y \(c,s\) resuelven la cuadrática.

De \(\sqrt{3}c+s=\frac{1}{12}\), y \(c^2+s^2=1\).

Queremos \(c-\sqrt{3}s\). Multipliquemos ambas ecuaciones por combinaciones.

Sea \(\sqrt{3}c+s=\frac{1}{12}\) (1).

Observemos que \(c-\sqrt{3}s\) y \(\sqrt{3}c+s\) son combinaciones ortogonales; podemos elevar al cuadrado la suma de sus cuadrados y relacionarlo con \(c^2+s^2\). De hecho:

\[
(\sqrt{3}c+s)^2+(c-\sqrt{3}s)^2
=3c^2+2\sqrt{3}cs+s^2+c^2-2\sqrt{3}cs+3s^2
=4(c^2+s^2)=4.
\]

Por tanto:

\[
\left(\frac{1}{12}\right)^2+(c-\sqrt{3}s)^2=4.
\]

\[
(c-\sqrt{3}s)^2=4-\frac{1}{144}=\frac{576-1}{144}=\frac{575}{144}.
\]

Así:

\[
c-\sqrt{3}s=\pm\frac{\sqrt{575}}{12}=\pm\frac{5\sqrt{23}}{12},
\]

porque \(575=25\cdot 23\).

Entonces:

\[
|P-X|^2=35\pm \frac{48\sqrt{3}}{5}\cdot \left(\pm\frac{5\sqrt{23}}{12}\right).
\]

Los signos se pueden combinar. Cuidemos: el signo de \(u\) (elegido para \(P\) interior) y el signo de \(c-\sqrt{3}s\) (que depende de cuál de los dos \(X\) tomamos) están ligados.

Para simplificar, notemos que hay dos configuraciones simétricas. Si elegimos \(X\) con \(c-\sqrt{3}s>0\), el signo de \(u\) para \(P\) interior será tal que se obtenga el mismo \(XP\) que en la configuración simétrica.

El producto de los signos dará \(+\frac{5\sqrt{23}}{12}\) veces \(\frac{48\sqrt{3}}{5}\). Veamos ambas posibilidades.

Si los signos de \(c-\sqrt{3}s\) y de \(u\) coinciden (positivo con positivo), entonces el término es:

\[
+\frac{48\sqrt{3}}{5}\cdot\frac{5\sqrt{23}}{12}=4\sqrt{69}.
\]

Si son opuestos, el término es \(-4\sqrt{69}\).

Entonces:

\[
XP^2=35\pm 4\sqrt{69}.
\]

Uno de esos valores corresponde a \(P\) interior, el otro a \(P\) exterior (el otro punto de intersección de la recta con \(\omega\)).

¿Cuál es el correcto? Para \(P\) interior, el punto \(P\) debe estar en el arco interior de \(\omega\). Determinemos cuál signo le corresponde.

---

**31. Determinar el signo para \(P\) interior**

Tomemos una de las dos soluciones \(X\). Por simetría, basta analizar una y luego ver.

Recordemos que \(u=\pm X^\perp/5\). La recta \(X\cdot y=25\) (para un punto genérico \(y\)) es perpendicular a \(X\). Al intersecar \(\omega\) con esa recta, se obtienen dos puntos: uno interior y otro exterior.

Necesitamos identificar cuál corresponde a qué signo.

Tomemos un caso concreto para intuir. Elijamos \(X\) de modo que \(c-\sqrt{3}s>0\).

De \(c,s\), puedo elegir por ejemplo la solución con \(c_+\approx0.5356\). Calculemos \(s\): \(s=\frac{1}{12}-\sqrt{3}c=\frac{1}{12}-1.732\cdot0.5356\approx0.0833-0.9274=-0.8441\).

Entonces \(s<0\). Así \(X=(3+2\sqrt{3}c,\sqrt{3}+2\sqrt{3}s)\approx(3+1.855,\ 1.732-2.925)=(4.855,-1.193)\). Este \(X\) está por debajo del eje \(x\), es decir en el arco inferior de \(\Gamma\) (fuera del triángulo), no en el arco que contiene a \(B\) y \(C\)? \(B=(6,0)\) y \(C=(3,5.196)\). El arco menor \(BC\) (el que contiene a \(A\)? no). En \(\Gamma\), el arco \(BC\) que no contiene a \(A\) es el arco "inferior-derecho". El punto \(X\approx(4.855,-1.193)\) está en ese arco.

Para la otra solución \(c_-\approx-0.4635\), \(s=\frac{1}{12}-1.732(-0.4635)\approx0.0833+0.8028=0.8861\). Entonces \(X\approx(3-1.605,\ 1.732+3.070)=(1.395,4.802)\), que está en el arco superior-izquierdo (cerca de \(C\), hacia \(A\)?).

Por simetría respecto a la mediatriz \(AM\), ambos son equivalentes.

Ahora, para \(X=(4.855,-1.193)\), \(c-\sqrt{3}s=0.5356-1.732(-0.8441)=0.5356+1.462=1.998>0\). Bien, positivo.

La recta perpendicular a \(X\): los puntos \(y\) con \(X\cdot y=25\).

Para \(P\) interior, mira la figura: \(P\) está en el arco interior de \(\omega\), cerca de \(O=(3,1.732)\) o de \(B,C\). El punto \(P\) interior debe estar, por ejemplo, cerca de \(O\).

Calculemos \(u\) para las dos opciones:

\(X\approx(4.855,-1.193)\), \(X^\perp=(1.193,4.855)\), \(|X^\perp|=5\), así \(u_+=(0.2386,0.9710)\).

Entonces \(P_+=O_P+2\sqrt{3}u_+=(6,3.464)+(0.826,3.364)=(6.826,6.828)\). Este está fuera del triángulo (arriba). No interior.

\(u_-=(-0.2386,-0.9710)\), \(P_-=(6,3.464)+(-0.826,-3.364)=(5.174,0.100)\). Este está cerca de \(B\), dentro del triángulo. ¡Interior!

Así, para \(c-\sqrt{3}s>0\), el signo de \(u\) es negativo (opuesto al signo de \(c-\sqrt{3}s\)). Por tanto el término de signo es \(-4\sqrt{69}\).

Entonces:

\[
XP^2=35-4\sqrt{69}.
\]

Por tanto:

\[
XP=\sqrt{35-4\sqrt{69}}.
\]

---

**32. Verificación del valor**

¿Cuánto vale \(XP\)? \(4\sqrt{69}\approx4\cdot8.3066=33.226\). \(35-33.226=1.774\). \(\sqrt{1.774}\approx1.332\).

Verifiquemos con las coordenadas halladas.

Para \(X\approx(4.855,-1.193)\) y \(P\approx(5.174,0.100)\):

\[
XP=\sqrt{(5.174-4.855)^2+(0.100+1.193)^2}=\sqrt{0.319^2+1.293^2}
=\sqrt{0.1018+1.672}=\sqrt{1.774}=1.332.
\]

¡Coincide!

Además \(AP\): \(P\approx(5.174,0.100)\), \(A=(0,0)\), \(AP\approx\sqrt{26.77+0.01}\approx5.174\). Espera, \(AP\approx5.17\). Y \(AXP\) rectángulo en \(X\): \(AX=5\), \(XP\approx1.332\), \(AP=\sqrt{25+1.774}=\sqrt{26.774}\approx5.174\). ¡Consistente!

Y la condición \(\angle BPC=120^\circ\): \(P=(5.174,0.100)\), \(B=(6,0)\), \(C=(3,5.196)\).

\(\overrightarrow{PB}=(0.826,-0.100)\), \(\overrightarrow{PC}=(-2.174,5.096)\).

Producto punto: \(0.826(-2.174)+(-0.100)(5.096)=-1.796-0.510=-2.306\).

\(|PB|\approx0.832\), \(|PC|\approx5.540\). Producto de normas \(\approx4.609\). \(\cos\approx-2.306/4.609\approx-0.5003\). Ángulo \(\approx120^\circ\). ¡Correcto!

Todo cuadra.

---

**33. Respuesta final**

\[
\boxed{\sqrt{35-4\sqrt{69}}}
\]