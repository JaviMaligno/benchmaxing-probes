Para hallar la probabilidad pedida, podemos comparar el área de la región de puntos más cercanos a $O$ que a cualquiera de los vértices $P$, $Q$ y $R$ con el área total del triángulo equilátero $PQR$.

**Paso 1: Caracterización geométrica de la región**
Un punto $X$ en el interior del triángulo está más cerca de $O$ que del vértice $P$ si y solo si se encuentra en el mismo semiplano que $O$ respecto a la mediatriz del segmento $OP$. De manera análoga, debe estar del lado de $O$ respecto a las mediatrices de $OQ$ y $OR$.

**Paso 2: Relación de alturas y semejanza**
Sea $R$ el circunradio del triángulo equilátero $PQR$, es decir, $OP = OQ = OR = R$. 
- En un triángulo equilátero, el centro $O$ coincide con el baricentro, el circuncentro y el incentro. Como el baricentro divide a cada altura (y mediana) en razón $2:1$, la distancia de $O$ a cada lado del triángulo es $\frac{1}{2}R$, y la altura total del triángulo $PQR$ es:
  $$h = R + \frac{1}{2}R = \frac{3}{2}R.$$

- Consideremos ahora la mediatriz del segmento $OP$. Esta recta es perpendicular a $OP$ (que es la bisectriz del ángulo en $P$) y pasa por el punto medio de $OP$, a una distancia $\frac{1}{2}R$ del vértice $P$. 
- Como $OP$ es perpendicular al lado $QR$, la mediatriz de $OP$ es paralela al lado $QR$. Por tanto, dicha mediatriz corta a los lados $PQ$ y $PR$ formando un pequeño triángulo equilátero con vértice en $P$ y altura:
  $$h_P = \frac{1}{2}R.$$

**Paso 3: Cálculo de áreas y probabilidad**
La razón de semejanza entre el pequeño triángulo equilátero junto al vértice $P$ (formado por los puntos más cercanos a $P$ que a $O$) y el triángulo total $PQR$ es la razón entre sus alturas:
$$k = \frac{h_P}{h} = \frac{\frac{1}{2}R}{\frac{3}{2}R} = \frac{1}{3}.$$

Por lo tanto, el área de este triángulo pequeño es $k^2 = \left(\frac{1}{3}\right)^2 = \frac{1}{9}$ del área del triángulo $PQR$.

Por simetría, las mediatrices de $OQ$ y $OR$ determinan en las esquinas $Q$ y $R$ otros dos triángulos equiláteros congruentes, cada uno con $\frac{1}{9}$ del área total. Como la razón de semejanza es $\frac{1}{3} < \frac{1}{2}$, estos tres triángulos pequeños no se solapan entre sí.

El área conjunta de los puntos que están más cerca de alguno de los tres vértices que de $O$ representa:
$$3 \times \frac{1}{9} = \frac{1}{3}$$
del área total de $\triangle PQR$.

En consecuencia, la fracción del área correspondiente a los puntos que están más cerca de $O$ que de cualquiera de los tres vértices es:
$$1 - \frac{1}{3} = \frac{2}{3}.$$

\boxed{\frac{2}{3}}