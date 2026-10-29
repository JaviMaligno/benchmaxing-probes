Para hallar la probabilidad de que un punto elegido al azar en el interior del triángulo equilátero $PQR$ esté más cerca del centro $O$ que de cualquiera de los tres vértices $P$, $Q$ y $R$, podemos comparar el área de la región favorable con el área total del triángulo.

### Paso 1: Relación geométrica entre el centro y los vértices
Sea $s$ la longitud del lado del triángulo equilátero $PQR$. La distancia desde el centro (baricentro y circuncentro) $O$ hasta cada uno de los vértices $P$, $Q$ y $R$ es el circunradio $R$:
$$R = OP = OQ = OR = \frac{s}{\sqrt{3}}$$

Un punto $X$ está más cerca de $O$ que del vértice $P$ si y solo si se encuentra en el semiplano determinado por la mediatriz del segmento $OP$ que contiene a $O$. Lo mismo ocurre para los vértices $Q$ y $R$ respecto a las mediatrices de $OQ$ y $OR$.

### Paso 2: Región descartada en cada vértice
Consideremos el vértice $P$. El segmento $OP$ biseca el ángulo interior en $P$ (que mide $60^\circ$), formando un ángulo de $30^\circ$ con los lados $PQ$ y $PR$.

Sea $N$ el punto medio de $OP$, de modo que $PN = \frac{R}{2} = \frac{s}{2\sqrt{3}}$. La mediatriz de $OP$ pasa por $N$ y es perpendicular a $OP$, cortando a los lados $PQ$ y $PR$ en los puntos $K$ y $K'$, respectivamente.

En el triángulo rectángulo $\triangle PNK$:
- $\angle PNK = 90^\circ$
- $\angle NPK = 30^\circ$
- $PN = \frac{s}{2\sqrt{3}}$

La distancia desde $P$ hasta $K$ es:
$$PK = \frac{PN}{\cos(30^\circ)} = \frac{\frac{s}{2\sqrt{3}}}{\frac{\sqrt{3}}{2}} = \frac{s}{3}$$

Por simetría, $PK' = \frac{s}{3}$. Dado que $\angle KPK' = 60^\circ$, el triángulo $\triangle PKK'$ que queda más cerca de $P$ que de $O$ es un triángulo equilátero de lado $\frac{s}{3}$.

### Paso 3: Cálculo de áreas y probabilidad
Como la razón de semejanza entre el triángulo pequeño $\triangle PKK'$ y el triángulo original $\triangle PQR$ es $\frac{1}{3}$, la razón entre sus áreas es:
$$\frac{\text{Área}(\triangle PKK')}{\text{Área}(\triangle PQR)} = \left(\frac{1}{3}\right)^2 = \frac{1}{9}$$

Lo mismo sucede en los otros dos vértices $Q$ y $R$. Como $\frac{s}{3} + \frac{s}{3} = \frac{2s}{3} < s$, los tres triángulos equiláteros de las esquinas no se solapan.

Por lo tanto, la fracción del área de $\triangle PQR$ formada por los puntos que están más cerca de alguno de los vértices $P$, $Q$ o $R$ que de $O$ es:
$$3 \times \frac{1}{9} = \frac{1}{3}$$

La probabilidad de que el punto elegido esté más cerca de $O$ que de cualquiera de los tres vértices es el complemento:
$$1 - \frac{1}{3} = \frac{2}{3}$$

\boxed{\frac{2}{3}}