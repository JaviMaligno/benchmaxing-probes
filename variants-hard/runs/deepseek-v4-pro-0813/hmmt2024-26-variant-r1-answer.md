Bien, resolvamos con calma.

Tenemos:

- $PQ = 25$, $PR = 45$, $PT = 15$.
- La circunferencia $\Gamma$ con centro $O$ pasa por $Q$ y $R$, y corta de nuevo a los segmentos $PQ$ y $PR$ en $Q'$ y $R'$.
- Las circunferencias de diámetros $QQ'$ y $RR'$ son tangentes externamente en $T$.

Como $Q'$ está en $PQ$ y $R'$ en $PR$, pongamos:

\[
Q = (0,0),\quad P=(25,0)
\]

Esto coloca a $Q'$ en el segmento $PQ$. Pero quizá sea más natural usar coordenadas con el ángulo en $P$.

---

**Paso 1: Potencia de $P$ respecto de $\Gamma$**

Como $P,Q,Q'$ son colineales y $P,R,R'$ son colineales, por potencia de $P$:

\[
PQ \cdot PQ' = PR \cdot PR'
\]

Sean

\[
PQ' = x,\qquad PR' = y
\]

Entonces

\[
25x = 45y \quad\Longrightarrow\quad y=\frac{5}{9}x
\]

---

**Paso 2: Circunferencias de diámetros $QQ'$ y $RR'$**

Para una circunferencia de diámetro $AB$, un punto $X$ está en ella si

\[
\angle AXB = 90^\circ
\]

El círculo con diámetro $QQ'$ tiene centro en el punto medio de $QQ'$ y radio $\frac{QQ'}{2}$. Como $Q=(0,0)$, $Q'=(x,0)$ (si ponemos $P=(25,0)$ y $Q$ a la izquierda), su centro $A_Q$ queda en $\left(\frac{x}{2},0\right)$ y su radio es $\frac{x}{2}$.

El círculo con diámetro $RR'$, análogamente, tendría centro $A_R$ y radio $\frac{RR'}{2}$.

---

**Paso 3: Tangencia externa en $T$**

Si dos circunferencias son tangentes externamente en $T$, entonces la distancia entre sus centros es la suma de sus radios, y $T$ está en la recta que une los centros. Además, la recta tangente común en $T$ es perpendicular a la línea de centros.

Los dos círculos de diámetros tienen un punto $P$ en común peculiar: por el teorema de Tales, como $P,Q,Q'$ son colineales y $Q\ne Q'$, el punto $P$ está sobre la circunferencia de diámetro $QQ'$. En efecto,

\[
\angle QPQ' = 180^\circ
\]

no sirve para Tales salvo que consideremos la recta $PQ$ como diámetro. Pero $Q$ y $Q'$ están ambos en el segmento $PQ$, así que $P$ está en la prolongación; el ángulo $QPQ'$ es llano, no recto. Por lo tanto, **$P$ no está sobre el círculo de diámetro $QQ'$**, salvo en el caso degenerado.

---

**Paso 4: Relación entre $T$ y las potencias**

Como $T$ es punto de tangencia de los círculos de diámetros $QQ'$ y $RR'$, se cumple que las tangentes desde $P$ a ambos círculos tienen longitudes relacionadas con $PT$. Pero lo que nos interesa es $PO$.

Usaremos coordenadas completas. Pongamos

\[
P=(0,0),\quad Q=(25,0)
\]

y supongamos que $R$ está en una dirección que forma ángulo $\theta$ con $PQ$, con

\[
R = 45(\cos\theta,\sin\theta)
\]

Entonces $Q'$ está en $PQ$ a distancia $x$ de $P$:

\[
Q'=(x,0)
\]

y $R'$ está en $PR$ a distancia $y=\frac{5}{9}x$ de $P$:

\[
R'=\frac{5x}{9}(\cos\theta,\sin\theta)
\]

---

**Paso 5: Centros y radios**

Círculo $C_1$ de diámetro $QQ'$, con $Q=(25,0)$, $Q'=(x,0)$:

\[
\text{centro } M_1=\left(\frac{25+x}{2},0\right),\quad r_1=\frac{|25-x|}{2}
\]

Círculo $C_2$ de diámetro $RR'$, con $R=45u$, $R'=\frac{5x}{9}u$, donde $u=(\cos\theta,\sin\theta)$:

\[
\text{centro } M_2 = \frac{45+\frac{5x}{9}}{2}u
\]

\[
r_2=\frac{45-\frac{5x}{9}}{2}
\]

(suponemos $x<25$ para que $Q'$ esté en el segmento $PQ$, y $R'$ en $PR$; verificaremos).

---

**Paso 6: Tangencia externa**

La distancia entre centros es

\[
d = |M_1-M_2| = r_1+r_2
\]

y $T$ cumple $PT=15$, estando $T$ sobre el segmento $M_1M_2$.

Usemos que la tangencia da una posición precisa de $T$. De manera más eficiente: como los círculos de diámetros se cortan ortogonalmente a $\Gamma$ en $Q'$ y $R'$, el centro radical de los tres círculos (los dos de diámetro y $\Gamma$) es $P$. Por tanto, $P$ es el centro radical.

Entonces, las longitudes de las tangentes desde $P$ a los dos círculos de diámetro coinciden. La tangente desde $P$ al círculo de diámetro $QQ'$ tiene longitud:

\[
\sqrt{PQ\cdot PQ'}=\sqrt{25x}
\]

pues $PM_1^2-r_1^2 = \frac{(25+x)^2}{4}-\frac{(25-x)^2}{4}=25x$.

Análogamente, la tangente desde $P$ al círculo de diámetro $RR'$ mide

\[
\sqrt{PR\cdot PR'}=\sqrt{45\cdot \frac{5x}{9}}=\sqrt{25x}
\]

que coincide. Y como $T$ es la tangencia, la tangente común en $T$ es perpendicular a $M_1M_2$.

---

**Paso 7: Triángulo $PM_1T$**

El punto $T$ está sobre la circunferencia de diámetro $QQ'$, así que

\[
M_1T = r_1 = \frac{25-x}{2}
\]

y el ángulo $PM_1T$ es el ángulo entre $PM_1$ y $M_1T$. Pero $M_1T$ es perpendicular a la tangente común. La tangente desde $P$ al círculo $C_1$ toca en un punto $U_1$ y su longitud es $PU_1=\sqrt{25x}$. La recta tangente común es distinta de $PU_1$ en general.

Apliquemos el teorema de la potencia en $T$: como $T$ está en ambos círculos, y $P$ es el centro radical, la potencia de $T$ respecto a $\Gamma$ es igual a su potencia respecto a los otros dos, que es cero. Por lo tanto, $T$ también está en $\Gamma$. **Esto es clave**: la tangencia de los dos círculos de diámetro junto con que $P$ es centro radical implica que $T$ pertenece a $\Gamma$.

En efecto, potencia de $T$ respecto a $C_1$ es 0; respecto a $C_2$ es 0; como $P$ es centro radical, la potencia respecto a $\Gamma$ debe ser igual, es decir 0. Luego $T\in\Gamma$.

---

**Paso 8: Aplicar potencia desde $T$ y obtener $O$**

Como $T\in\Gamma$, y $\Gamma$ tiene centro $O$ y pasa por $Q,R$, se tiene $OT=OQ=OR$.

La potencia de $P$ respecto a $\Gamma$ es

\[
\operatorname{Pot}(P)=PQ\cdot PQ'=25x
\]

pero también

\[
\operatorname{Pot}(P)=PO^2-r^2
\]

donde $r=OQ$.

Como $T\in\Gamma$, $OT=r$, y conocemos $PT=15$. En el triángulo $POT$:

\[
PT^2 = PO^2 + OT^2 - 2\cdot PO\cdot OT\cos\angle POT
\]

No tenemos $\angle POT$ directamente. Pero $O$ es el centro y $OT=OQ=OR$.

---

**Paso 9: Calcular $x$ usando la condición adicional**

La condición $PT=15$ nos dará $x$. Para el círculo de diámetro $QQ'$, el punto $T$ cumple $M_1T=r_1$ y $PT=15$. También $T$ está en la recta $M_1M_2$ y $M_2T=r_2$.

Sabemos:

\[
M_1M_2 = r_1+r_2
\]

y $P$, $T$, y la tangente común forman un triángulo rectángulo. En el triángulo $PM_1T$:

\[
PT^2 = PM_1^2 + M_1T^2 - 2\,PM_1\cdot M_1T\cos\angle PM_1T
\]

El ángulo $\angle PM_1T$ es el ángulo entre $PM_1$ y $M_1M_2$ (pues $T$ está en $M_1M_2$).

Calculemos $PM_1$:

\[
PM_1 = \frac{25+x}{2}
\]

La tangente desde $P$ a $C_1$ mide $\sqrt{25x}$, por lo que si $\alpha$ es el ángulo entre $PM_1$ y la tangente desde $P$, se tiene $\sin\alpha = \frac{r_1}{PM_1}$. Pero es más simple usar el triángulo rectángulo $P U_1 M_1$, donde $U_1$ es el punto de tangencia:

\[
PU_1=\sqrt{25x},\quad U_1M_1=r_1,\quad \angle PU_1M_1=90^\circ
\]

Entonces la distancia de $P$ a la recta $M_1M_2$ está relacionada con la tangente común.

---

**Paso 10: Relación con $T$**

Como la tangente común en $T$ es perpendicular a $M_1M_2$, y esta tangente pasa por $T$, la distancia de $P$ a la tangente común es el cateto del triángulo rectángulo formado con $PT$ y el otro cateto sobre $M_1M_2$.

Esto se vuelve tedioso. Mejor usemos la condición de que $T$ es el centro radical de $C_1$, $C_2$ y $\Gamma$: la potencia de $P$ respecto a $\Gamma$ es igual a la de los otros, y como $T\in\Gamma$, entonces

\[
PO^2 - OT^2 = 25x
\]

Además, la cuerda $QR$ de $\Gamma$ está a una cierta distancia de $O$, y $P$ es el punto de intersección de las secantes $PQ$ y $PR$.

Existe una fórmula estándar: si dos círculos son tangentes en $T$ y $\Gamma$ pasa por sus puntos, entonces la longitud de la tangente común desde $P$ y $PT$ se relacionan. Concretamente, para el círculo de diámetro $QQ'$:

El punto $T$ está en $C_1$, y la tangente común en $T$ es a su vez tangente a $C_1$ y a $C_2$. La longitud de la tangente desde $P$ a $C_1$ por $U_1$ y la distancia $PT$ están vinculadas por el ángulo en $P$.

---

Demos un enfoque más directo: **coordenadas con $T$**.

Como $T$ es la tangencia de los círculos de diámetros y además pertenece a $\Gamma$, y $PT=15$, podemos tomar $T$ como origen o usar inversión centrada en $P$ con radio $\sqrt{25x}$, que deja invariantes ambos círculos de diámetro y también $\Gamma$ (por lo del centro radical). Bajo esta inversión, cada círculo de diámetro se transforma en la recta perpendicular correspondiente... Esto puede simplificar.

---

**Paso 11: Inversión**

Consideremos la inversión $\mathcal I$ con centro $P$ y radio $\rho=\sqrt{25x}$. Entonces:

- $Q$ y $Q'$ se intercambian: $\mathcal I(Q)=Q'$, $\mathcal I(Q')=Q$, pues $PQ\cdot PQ'=\rho^2=25x$.
- $R$ y $R'$ se intercambian de la misma manera.
- Los círculos de diámetro $QQ'$ y $RR'$, que pasan por pares conjugados por inversión, son **invariantes** como conjuntos (se transforman en sí mismos, intercambiando $Q$ con $Q'$ y $R$ con $R'$).
- $\Gamma$ también pasa por estos pares, y por tanto es invariante.

Como $T$ es el punto de tangencia de los círculos de diámetro, en $T$ los dos círculos comparten tangente y son invariantes, luego $T$ es un punto fijo de la inversión o bien su imagen es otro punto con la misma propiedad. Como $T$ yace en ambos círculos y en $\Gamma$, y estos son invariantes, la imagen de $T$ es un punto $T'$ que también pertenece a los tres. La única posibilidad no trivial es que $T'=T$, así que **$T$ debe cumplir**

\[
PT^2 = \rho^2 = 25x
\]

Dado que $PT=15$:

\[
225=25x \quad\Longrightarrow\quad x=9
\]

¡Excelente! Entonces

\[
PQ'=9,\qquad PR'=\frac{5}{9}\cdot 9=5
\]

---

**Paso 12: Ahora calcular $PO$**

Sabemos $T\in\Gamma$, $PT=15$, y $\rho^2=225$ es la potencia de $P$ respecto a $\Gamma$:

\[
\operatorname{Pot}(P)=PO^2-OT^2 = 225
\]

Además, como $T\in\Gamma$, $OT$ es el radio de $\Gamma$: $OT=OQ=OR$.

Necesitamos una relación más. Como $T$ es fijo por la inversión, la tangente a $\Gamma$ en $T$ es perpendicular a $PT$ (pues la inversión deja $\Gamma$ invariante y $T$ fijo; esto implica que la tangente en $T$ es invariante). Para que una recta tangente que pasa por $T$ sea invariante bajo inversión centrada en $P$, debe ser perpendicular a $PT$. Así, **$PT$ pasa por $O$**.

Por tanto, $O$, $T$ y $P$ son colineales. Entonces

\[
PO = PT + OT = 15+OT
\]

Usemos la potencia:

\[
PO^2-OT^2=(PO-OT)(PO+OT)=(PO-OT)\cdot PO
\]

pero $PO-OT = PT =15$, así que

\[
\operatorname{Pot}(P)=15\cdot PO = 225
\]

\[
15\,PO=225 \quad\Longrightarrow\quad PO=15
\]

Espera: si $PO=15$, entonces $O$ y $T$ están a la misma distancia de $P$ pero en direcciones opuestas; $OT = PO+PT = 30$. Veamos consistencia: $PO=15$, $OT=30$, $PT=15$ con $O,T,P$ colineales y $T$ entre $P$ y $O$ no, sino $O$ entre $P$ y $T$ o al revés. Si $PO=15=PT$ y $O\ne T$, entonces $O$ y $T$ están en lados opuestos de $P$ o son el mismo punto. Como $OT=30$, están en lados opuestos de $P$: $O$ está a distancia 15 de $P$ y $T$ a distancia 15 en la dirección opuesta, de modo que $OT=30$.

Entonces $PO=15$, $OT=30$, el radio de $\Gamma$ es 30. Veamos si esto es compatible con los datos:

- $OQ=30$, $PQ=25$, $PO=15$.
- En triángulo $POQ$: por ley de cosenos,

\[
OQ^2=PO^2+PQ^2-2\cdot PO\cdot PQ\cos\angle OPQ
\]

\[
900=225+625-2\cdot15\cdot25\cos\angle OPQ
\]

\[
900=850-750\cos\angle OPQ
\]

\[
750\cos\angle OPQ = -50 \implies \cos\angle OPQ = -\frac{1}{15}
\]

Esto es geométricamente factible (ángulo obtuso en $P$).

Veamos $R$: $OR=30$, $PR=45$, $PO=15$. Por ley de cosenos en $POR$:

\[
900=225+2025-2\cdot15\cdot45\cos\angle OPR
\]

\[
900=2250-1350\cos\angle OPR
\]

\[
1350\cos\angle OPR=1350 \implies \cos\angle OPR=1
\]

Esto implica $\angle OPR=0$, es decir, $O$, $P$ y $R$ colineales con $O$ y $R$ del mismo lado de $P$. Entonces $PR=45=PO+OR=15+30=45$; consistente. Y $\angle QPR$ sería $180^\circ-\angle OPQ$ con $\cos\angle OPQ=-\frac{1}{15}$, de modo que $\cos\angle QPR=\frac{1}{15}$.

Revisemos si $Q'$ y $R'$ están realmente en los segmentos $PQ$ y $PR$:

- $PQ'=9<25$ ✓
- $PR'=5<45$ ✓

Y la cuerda $QR$ de $\Gamma$ tiene extremos cuyas distancias a $P$ son 25 y 45, con radio 30 y $PO=15$; es coherente con un triángulo donde $O$ está sobre $PR$ y $R$ está a 45 de $P$, mientras $Q$ forma ángulo con $\cos=\frac{1}{15}$ respecto a $PR$.

Además, la tangencia externa de los círculos de diámetros: 

- Círculo con diámetro $QQ'$: centro $M_1$ a $(25+9)/2=17$ de $P$ sobre la recta $PQ$, radio 8.
- Círculo con diámetro $RR'$: centro $M_2$ a $(45+5)/2=25$ de $P$ sobre la recta $PR$, radio 20.

Distancia entre centros:

\[
M_1M_2^2 = 17^2+25^2-2\cdot17\cdot25\cos\angle QPR
\]

Con $\cos\angle QPR=1/15$:

\[
=289+625-\frac{850}{15}=914-\frac{170}{3}=\frac{2742-170}{3}=\frac{2572}{3}
\]

Esto no es igual a $(8+20)^2=784$. ¡Hay inconsistencia! La tangencia externa exigiría $M_1M_2=r_1+r_2=28$, pero obtuvimos $\sqrt{2572/3}\approx29.27$.

Por lo tanto, algo falla. El supuesto de que $T$ es fijo bajo la inversión y que la tangente en $T$ es perpendicular a $PT$ no se cumple necesariamente. Reconsideremos.

---

**Corrección: la inversión y el punto $T$**

La inversión $\mathcal I$ deja invariantes los dos círculos de diámetro, pero como $T$ está en ambos y la tangencia se preserva, la imagen $T'$ debe ser también punto de tangencia de las imágenes de los círculos, que son los mismos círculos. Un par de círculos tangentes externamente tiene exactamente un punto de tangencia. Por tanto, $T'=T$, **a menos que** la inversión intercambie los círculos, pero no es el caso: cada círculo de diámetro es invariante como conjunto porque contiene a un par conjugado $Q,Q'$ y además la inversión manda circunferencias que no pasan por $P$ en circunferencias que no pasan por $P$.

Como $C_1$ no pasa por $P$, su imagen es una circunferencia que tampoco pasa por $P$, y contiene a $Q'=\mathcal I(Q)$ y a $Q=\mathcal I(Q')$. Una circunferencia está determinada por tres puntos. La imagen de $C_1$ contiene a $Q$ y $Q'$, pero ¿es la misma $C_1$? Para que la imagen sea $C_1$, la imagen de cualquier punto de $C_1$ debe estar en $C_1$. La inversión mapea $C_1$ en sí misma si y solo si $C_1$ es ortogonal al círculo de inversión (o es una recta). ¿Es $C_1$ ortogonal al círculo centrado en $P$ con radio $\rho=\sqrt{25x}$?

Para $C_1$: centro $M_1$, radio $r_1$. Es ortogonal al círculo de inversión si

\[
PM_1^2 = r_1^2+\rho^2
\]

\[
\left(\frac{25+x}{2}\right)^2 = \left(\frac{25-x}{2}\right)^2 + 25x
\]

Desarrollemos:

\[
\frac{625+50x+x^2}{4} = \frac{625-50x+x^2}{4}+25x
\]

Multiplicamos por 4:

\[
625+50x+x^2 = 625-50x+x^2+100x
\]

\[
625+50x+x^2 = 625+50x+x^2
\]

¡Se cumple! Por lo tanto, $C_1$ es ortogonal al círculo de inversión. Análogamente $C_2$ también. Entonces $C_1$ y $C_2$ son invariantes como conjuntos, y su punto de tangencia $T$ cumple:

- Si $T$ es un punto de tangencia de dos circunferencias invariantes y ortogonales al círculo de inversión, el punto $T$ tiene potencia $PT^2-\rho^2$ respecto al círculo de inversión. Para que $T$ esté en el círculo de inversión, necesitaríamos $PT=\rho$. Pero $T$ no necesariamente está en el círculo de inversión.

De hecho, como $C_1$ es ortogonal al círculo de inversión, este círculo $I$ corta a $C_1$ en dos puntos que son fijos. El punto $T$ está en $C_1$ y en $C_2$; su imagen debe estar también en $C_1$ y $C_2$. Como $C_1\cap C_2$ tiene solo el punto $T$ (tangencia), necesariamente $T'=T$, y por lo tanto **$PT=\rho$**. Esto es válido, y da $\rho=15$.

Entonces $x=9$ es correcto. El problema está en mi afirmación de que $O$, $T$ y $P$ son colineales.

La tangente a $\Gamma$ en $T$: como $\Gamma$ es invariante por inversión, $\Gamma$ es ortogonal al círculo de inversión. Por tanto, el círculo de inversión $I$ y $\Gamma$ se cortan en dos puntos fijos. El punto $T$ pertenece a $\Gamma$ y a $I$ (pues $PT=\rho$). En un punto de intersección de dos círculos ortogonales, las tangentes son perpendiculares. Así, **la tangente a $\Gamma$ en $T$ es perpendicular a la tangente a $I$ en $T$, que a su vez es perpendicular a $PT$**. Por tanto, la tangente a $\Gamma$ en $T$ es **paralela** a $PT$, no perpendicular. Luego $OT\perp$ tangente en $T$, así que $OT\perp PT$. ¡Esto cambia todo!

Por lo tanto, en el triángulo $POT$:

\[
\angle PTO = 90^\circ
\]

Entonces, por Pitágoras:

\[
PO^2 = PT^2+OT^2 = 225+OT^2
\]

Además, la potencia de $P$ respecto a $\Gamma$ es

\[
PO^2-OT^2 = 225
\]

que coincide, pero no nos da $OT$. Necesitamos más información: el radio $OT=OQ=OR$.

---

**Paso 13: Calcular $OT$ con la geometría**

Sabemos que $\Gamma$ es ortogonal al círculo de inversión $I$ (centro $P$, radio 15). Como $O$ es el centro de $\Gamma$, la condición de ortogonalidad entre dos circunferencias es:

\[
PO^2 = OT^2 + 15^2
\]

lo cual ya tenemos. Falta otra relación: pasar por $Q$ y $R$.

Tenemos $PQ=25$, $PR=45$, y $Q'$, $R'$ con $PQ'=9$, $PR'=5$.

Como $\Gamma$ pasa por $Q$ y $R$, la potencia de $P$:

\[
25\cdot 9=225,\qquad 45\cdot5=225
\]

consistente.

Para hallar $PO$ y $OT$, usemos que la inversión $\mathcal I$ intercambia $Q$ con $Q'$ y $R$ con $R'$, y deja $\Gamma$ invariante. Los puntos $Q$ y $Q'$ están en la misma recta por $P$, a distancias 25 y 9 de $P$. En una inversión de radio 15, estos quedan intercambiados.

La circunferencia $\Gamma$ contiene a $Q$ y a $Q'$. Por lo tanto, la cuerda $QQ'$ es perpendicular al radio que pasa por su punto medio, pero $QQ'$ es la recta $PQ$, así que la proyección de $O$ sobre $PQ$ cae en el punto medio de $QQ'$, que dista $(25+9)/2=17$ de $P$.

Llamemos $d$ a la distancia de $O$ a la recta $PQ$. Entonces el triángulo rectángulo con hipotenusa $OT$ (radio), cateto $d$ y cateto correspondiente a la proyección: la proyección de $O$ sobre $PQ$ está a 17 de $P$, y $Q$ está a 25, por lo que el cateto horizontal desde la proyección hasta $Q$ mide $25-17=8$. Luego

\[
OT^2 = d^2 + 8^2
\]

Análogamente para $RR'$: la recta $PR$ contiene a $R$ y $R'$, con distancias 45 y 5 desde $P$. El punto medio dista 25 de $P$, y $R$ dista 45, así que el cateto a lo largo de $PR$ mide $45-25=20$. La distancia de $O$ a la recta $PR$ es $d'$, y

\[
OT^2 = d'^2 + 20^2
\]

Por tanto,

\[
d^2+64 = d'^2+400
\]

\[
d'^2 = d^2-336
\]

Esto sugiere que $d'$ podría no existir si $d^2<336$. Veamos con otro ángulo. La distancia $d$ de $O$ a $PQ$ y $d'$ a $PR$ se relacionan con $PO$ y el ángulo en $P$.

---

**Paso 14: Coordenadas finales**

Pongamos $P=(0,0)$, $Q=(25,0)$, y $R=45(\cos\alpha,\sin\alpha)$ con $\cos\alpha$ a determinar. La recta $PQ$ es el eje $x$; la recta $PR$ forma ángulo $\alpha$.

Sabemos que $O$ está a la misma distancia de las rectas $PQ$ y $PR$ en el sentido de las proyecciones anteriores. Además, como $\Gamma$ pasa por $Q=(25,0)$ y $Q'=(9,0)$, la mediatriz de $QQ'$ es la recta $x=17$; luego la coordenada $x$ de $O$ es 17. Es decir,

\[
O=(17,h)
\]

para algún $h$.

Además, $\Gamma$ pasa por $R$ y $R'$, así que $O$ está sobre la mediatriz de $RR'$. El punto medio de $RR'$ es

\[
M_{RR'} = \frac{R+R'}{2} = \frac{45u+5u}{2}=25u
\]

y el vector $RR' = (45-5)u = 40u$, con $u=(\cos\alpha,\sin\alpha)$. La mediatriz es la recta que pasa por $25u$ perpendicular a $u$, es decir, en dirección $u^\perp=(-\sin\alpha,\cos\alpha)$:

\[
O = 25u + t\,u^\perp
\]

Igualando con $O=(17,h)$:

\[
25(\cos\alpha,\sin\alpha)+t(-\sin\alpha,\cos\alpha) = (17,h)
\]

De la componente $x$:

\[
25\cos\alpha - t\sin\alpha = 17 \quad (1)
\]

De la componente $y$:

\[
25\sin\alpha + t\cos\alpha = h \quad (2)
\]

El radio al cuadrado usando $Q$ y $O=(17,h)$:

\[
OT^2 = OQ^2 = (25-17)^2 + h^2 = 64+h^2
\]

Y usando $R$:

\[
OT^2 = OR^2 = |45u-O|^2
\]

pero como $O$ está en la mediatriz de $RR'$, la distancia de $O$ a $R$ es igual a la distancia de $O$ a $R'$; calculemos con $R$:

La componente de $O$ a lo largo de $u$ es $25$ (pues $O=25u+t u^\perp$), y la componente perpendicular es $t$. El punto $R$ tiene componente $45$ a lo largo de $u$ y 0 perpendicular. Por tanto,

\[
OR^2 = (45-25)^2 + t^2 = 400+t^2
\]

Igualamos los dos radios:

\[
64+h^2 = 400+t^2
\]

\[
h^2-t^2 = 336 \quad (3)
\]

Además, la ortogonalidad con la inversión dice que el radio $OT=\rho_I=15$ en el punto $T$, pero en realidad la condición de que $\Gamma$ sea ortogonal al círculo de inversión de radio 15 es:

\[
PO^2 = OT^2+225
\]

Con $O=(17,h)$, $PO^2=289+h^2$, y $OT^2=64+h^2$, esto da:

\[
289+h^2 = 64+h^2+225
\]

¡Se cumple idénticamente! Por lo tanto, la ortogonalidad no impone condiciones adicionales sobre $h$; es automática una vez que $O$ está en las mediatrices adecuadas con la potencia correcta.

Así que necesitamos otra condición: el hecho de que los círculos de diámetro sean tangentes externamente. Hasta ahora solo usamos que $\Gamma$ pasa por los cuatro puntos y la potencia.

---

**Paso 15: Condición de tangencia de los círculos de diámetro**

Círculo $C_1$ de diámetro $QQ'$: centro $M_1=(17,0)$, radio 8 (sobre el eje $x$).

Círculo $C_2$ de diámetro $RR'$: centro $M_2=25u$, radio 20.

La tangencia externa exige:

\[
|M_1M_2| = 8+20 = 28
\]

Calculemos:

\[
M_1=(17,0),\qquad M_2=25(\cos\alpha,\sin\alpha)
\]

\[
|M_1-M_2|^2 = 17^2+25^2-2\cdot17\cdot25\cos\alpha
\]

\[
= 289+625-850\cos\alpha = 914-850\cos\alpha
\]

Para que sea $28^2=784$:

\[
914-850\cos\alpha = 784
\]

\[
850\cos\alpha = 130
\]

\[
\cos\alpha = \frac{130}{850} = \frac{13}{85}
\]

Entonces

\[
\sin\alpha = \sqrt{1-\frac{169}{7225}} = \sqrt{\frac{7056}{7225}} = \frac{84}{85}
\]

---

**Paso 16: Hallar $h$ y $t$**

De la ecuación (1):

\[
25\cos\alpha - t\sin\alpha = 17
\]

\[
25\cdot\frac{13}{85} - t\cdot\frac{84}{85} = 17
\]

\[
\frac{325}{85} - \frac{84t}{85} = 17
\]

Multiplicamos por 85:

\[
325 - 84t = 1445
\]

\[
-84t = 1120
\]

\[
t = -\frac{1120}{84} = -\frac{40}{3}
\]

De la ecuación (2):

\[
h = 25\sin\alpha + t\cos\alpha
\]

\[
= 25\cdot\frac{84}{85} + \left(-\frac{40}{3}\right)\cdot\frac{13}{85}
\]

\[
= \frac{2100}{85} - \frac{520}{255}
\]

\[
\frac{2100}{85} = \frac{6300}{255}
\]

\[
h = \frac{6300-520}{255} = \frac{5780}{255} = \frac{1156}{51}
\]

Verifiquemos con (3): $h^2-t^2=336$.

\[
t^2 = \frac{1600}{9}
\]

\[
h^2 = \frac{1156^2}{51^2} = \frac{1336336}{2601}
\]

Esto es engorroso; verifiquemos numéricamente. $h\approx 22.67$, $t\approx -13.33$. $h^2\approx 514$, $t^2\approx 178$, diferencia $\approx 336$ ✓.

---

**Paso 17: Calcular $PO$**

\[
PO^2 = 17^2 + h^2
\]

Primero obtengamos $h$ de manera más limpia. De (1) con $t=-\frac{40}{3}$ y las fracciones:

\[
\cos\alpha = \frac{13}{85},\quad \sin\alpha = \frac{84}{85}
\]

\[
h = 25\cdot\frac{84}{85} - \frac{40}{3}\cdot\frac{13}{85}
\]

\[
= \frac{2100}{85} - \frac{520}{255}
\]

Mínimo común denominador 255:

\[
\frac{2100}{85} = \frac{2100\cdot3}{255}=\frac{6300}{255}
\]

\[
h = \frac{6300-520}{255} = \frac{5780}{255} = \frac{1156}{51}
\]

Entonces

\[
PO^2 = 289 + \left(\frac{1156}{51}\right)^2
\]

\[
= 289 + \frac{1336336}{2601}
\]

Pongamos $289 = \frac{289\cdot2601}{2601}$. Notemos que $2601 = 51^2 = 3\cdot 867$; además $289\cdot 9 = 2601$, de hecho $2601 = 9\cdot 289$. Porque $51^2 = 2601$ y $17^2=289$, y $51=3\cdot17$, entonces $2601=9\cdot289$.

Así,

\[
289 = \frac{9\cdot 289\cdot 289}{2601} = \frac{9\cdot 289^2}{2601}
\]

Entonces

\[
PO^2 = \frac{9\cdot 289^2 + 1156^2}{2601}
\]

Observemos que $1156 = 4\cdot 289$. Pues $4\cdot 289 = 1156$. Entonces

\[
PO^2 = \frac{9\cdot 289^2 + 16\cdot 289^2}{2601}
\]

\[
= \frac{25\cdot 289^2}{2601}
\]

\[
= \frac{25\cdot 289^2}{9\cdot 289}
\]

\[
= \frac{25\cdot 289}{9}
\]

\[
= \frac{7225}{9}
\]

Por lo tanto,

\[
PO = \frac{85}{3}
\]

---

**Verificación final**

- $PO = \frac{85}{3} \approx 28.33$.
- $OT$ (radio de $\Gamma$): $OT^2 = 64+h^2$.

\[
h^2 = \frac{1156^2}{2601} = \frac{16\cdot 289^2}{9\cdot 289} = \frac{16\cdot 289}{9}
\]

\[
OT^2 = 64 + \frac{16\cdot289}{9} = \frac{576+4624}{9} = \frac{5200}{9}
\]

\[
OT = \frac{20\sqrt{13}}{3} \approx 24.04
\]

La potencia de $P$: $PO^2-OT^2 = \frac{7225}{9}-\frac{5200}{9}=\frac{2025}{9}=225$ ✓, coincide con $PQ\cdot PQ'=25\cdot9=225$ ✓.

Además, $OT\perp PT$ en $T$ (por ortogonalidad con la inversión), de modo que $PO^2 = PT^2+OT^2 = 225+\frac{5200}{9}=\frac{2025+5200}{9}=\frac{7225}{9}$ ✓.

Todo es consistente.

---

\[
\boxed{\frac{85}{3}}
\]