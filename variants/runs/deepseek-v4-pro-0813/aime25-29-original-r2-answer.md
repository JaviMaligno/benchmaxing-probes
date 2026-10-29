
Razonemos paso a paso.

## 1. Situar el triángulo

El triángulo $ABC$ es rectángulo en $A$, hipotenusa $BC=38$. Coloquemos:

- $A=(0,0)$
- $B=(b,0)$ ($b>0$)
- $C=(0,c)$ ($c>0$)

Entonces $BC=\sqrt{b^2+c^2}=38$, así que $b^2+c^2=38^2=1444$.

## 2. Puntos $K$ y $L$

Nos dicen que hay puntos $K$ y $L$ dentro del triángulo con

$$AK=AL=BK=CL=KL=14.$$

Es decir:

- $K$ está a distancia $14$ de $A$ y de $B$.
- $L$ está a distancia $14$ de $A$ y de $C$.
- $KL=14$.

Además ambos están dentro del triángulo, lo cual nos ayudará a elegir signos.

Los puntos que distan $14$ de $A$ y de $B$ son las intersecciones de dos circunferencias: una centrada en $A$ con radio $14$ y otra centrada en $B$ con radio $14$. Como $AB=b$, tales intersecciones existen solo si $b\le 28$.

La distancia de $A$ a la recta vertical que pasa por el punto medio de $AB$ nos da la coordenada. La mediatriz de $AB$ es $x=b/2$. La distancia vertical al eje desde un punto de esa mediatriz que cumple $AK=14$ es

$$y_K = \pm \sqrt{14^2 - \left(\frac b2\right)^2} = \pm \sqrt{196 - \frac{b^2}{4}}.$$

Como $K$ está dentro del triángulo (que está en el primer cuadrante, con $x,y\ge 0$), tomamos la coordenada positiva:

$$K = \left(\frac b2,\ \sqrt{196-\frac{b^2}{4}}\right).$$

Análogamente para $L$, que dista $14$ de $A$ y de $C$. La mediatriz de $AC$ (eje $y=c/2$) nos da

$$L = \left(\sqrt{196-\frac{c^2}{4}},\ \frac c2\right),$$

tomando la coordenada $x$ positiva por estar dentro del triángulo.

## 3. Condición $KL=14$

Escribimos:

$$KL^2 = \left(\frac b2 - \sqrt{196-\frac{c^2}{4}}\right)^2
+ \left(\sqrt{196-\frac{b^2}{4}} - \frac c2\right)^2 = 196.$$

Esto parece complicado. Busquemos una relación más simple.

## 4. Interpretación geométrica con triángulos equiláteros

Como $AK=BK=14$, el triángulo $ABK$ es isósceles con dos lados de longitud $14$. Además $AK=AL=KL=14$ nos dice que $AKL$ es equilátero de lado $14$.

¿Y $BK$? $BK=14$. ¿Y $CL=14$.

Observemos que $AK=BK=14$ significa $K$ está en la mediatriz de $AB$, como vimos. Y $AL=CL=14$ significa $L$ está en la mediatriz de $AC$.

Fijémonos en las áreas. Como $A$ es el vértice recto:

$$\operatorname{área}(ABK) = \frac12 \cdot AB \cdot (\text{altura de }K\text{ sobre }AB).$$

La altura de $K$ sobre $AB$ es $y_K$. Entonces

$$[ABK] = \frac12\, b\, y_K = \frac12\, b\sqrt{196-\frac{b^2}{4}}.$$

Como $AK=BK=14$, también podemos usar la fórmula de Herón para $ABK$ con lados $14,14,b$.

Base $AB=b$, altura $h_K = \sqrt{14^2-(b/2)^2} = \sqrt{196-b^2/4}$.

Es decir $[ABK] = \frac12 b \sqrt{196-b^2/4}$.

Para $ACL$, lados $14,14,c$, altura $h_L=\sqrt{196-c^2/4}$, y

$$[ACL] = \frac12 c \sqrt{196-c^2/4}.$$

## 5. Área del cuadrilátero $BKLC$

El cuadrilátero $BKLC$ es la unión de los triángulos $BKL$ y $BLC$ (diagonal $BL$), o bien $BKC$ y $KLC$. Conviene elegir una descomposición útil.

Una idea: el cuadrilátero $BKLC$ tiene vértices $B$, $K$, $L$, $C$. El área buscada puede pensarse como

$$[BKLC] = [ABC] - [ABK] - [ACL] - [AKL]?$$

Comprobemos. El triángulo grande $ABC$ está formado por:

- el triángulo $ABK$,
- el triángulo $ACL$,
- el triángulo $AKL$,
- y el cuadrilátero $BKLC$.

¿Es así? Los puntos $K$ y $L$ están dentro del triángulo. Tracemos los segmentos $AK$, $AL$, $KL$. El segmento $AK$ divide el triángulo en dos partes, pero $AL$ y $KL$ añaden más cortes.

Consideremos la región delimitada por los segmentos desde $A$ a $K$, de $K$ a $L$ y de $L$ a $A$: es el triángulo $AKL$, que queda “pegado” al vértice $A$. Luego:

- El triángulo con vértices $A, B, K$ es $ABK$ (pegado al lado $AB$).
- El triángulo con vértices $A, C, L$ es $ACL$ (pegado al lado $AC$).
- El resto es el cuadrilátero $BKLC$ que toca la hipotenusa $BC$.

¿Cubren estas cuatro regiones todo el triángulo $ABC$ sin solaparse? El triángulo $ABC$ queda dividido por el segmento $KL$ y las líneas desde $A$ a $K$ y $A$ a $L$. La región cercana a $A$ delimitada por $AK$, $KL$ y $AL$ es $AKL$. La región entre $AB$, $BK$ y $AK$ es $ABK$. La región entre $AC$, $CL$ y $AL$ es $ACL$. La región restante, entre $BK$, $KL$, $LC$ y $BC$, es exactamente $BKLC$.

Por lo tanto:

$$[BKLC] = [ABC] - [ABK] - [ACL] - [AKL].$$

## 6. Cálculo del área de $AKL$

$AKL$ es equilátero de lado $14$ (pues $AK=AL=KL=14$):

$$[AKL] = \frac{\sqrt3}{4}\cdot 14^2 = \frac{\sqrt3}{4}\cdot 196 = 49\sqrt3.$$

## 7. Relación entre $b$ y $c$

Como $b^2+c^2=1444$ y además los segmentos encajan, quizá podamos determinar $b$ y $c$ usando los ángulos.

Sea $\theta = \angle BAK$. En el triángulo $ABK$, lados $AK=BK=14$. Entonces los ángulos en $A$ y en $B$ son iguales. Llamemos $\alpha$ al ángulo en $A$: $\angle BAK = \alpha$. Entonces $\angle ABK=\alpha$ y $\angle AKB = 180^\circ - 2\alpha$.

La ley de cosenos en $ABK$:

$$AB^2 = b^2 = 14^2 + 14^2 - 2\cdot 14\cdot 14\cos(180^\circ-2\alpha).$$

Pero $\cos(180^\circ-2\alpha)=-\cos 2\alpha$, luego

$$b^2 = 392 + 392\cos 2\alpha = 392(1+\cos 2\alpha) = 392\cdot 2\cos^2\alpha = 784\cos^2\alpha.$$

Por tanto $b = 28\cos\alpha$.

Como $AK=BK$, la base $b$ satisface $0\le \alpha\le 90^\circ$ y $b=28\cos\alpha$. Además la altura de $K$ sobre $AB$ es $14\sin\alpha$.

Luego

$$[ABK] = \frac12\, b\, (14\sin\alpha) = \frac12\cdot 28\cos\alpha \cdot 14\sin\alpha = 196\sin\alpha\cos\alpha = 98\sin 2\alpha.$$

## 8. Ángulo en $C$ para $L$

De manera análoga, sea $\beta = \angle CAL$ (medido desde $AC$). Como $AL=CL=14$, por el mismo razonamiento

$$c = 28\cos\beta$$

y

$$[ACL] = 98\sin 2\beta.$$

## 9. Relación entre $\alpha$ y $\beta$

Como $ABC$ es rectángulo en $A$, los lados $AB$ y $AC$ son perpendiculares. Los rayos $AK$ y $AL$ están dentro del ángulo recto. El ángulo $KAL$ es el ángulo en $A$ del triángulo equilátero $AKL$, así que

$$\angle KAL = 60^\circ.$$

Si $AK$ forma un ángulo $\alpha$ con $AB$ y $AL$ forma un ángulo $\beta$ con $AC$ (en el otro lado del ángulo recto), entonces

$$\alpha + \beta + 60^\circ = 90^\circ,$$

porque los rayos $AB$ y $AC$ forman $90^\circ$, y entre $AK$ y $AL$ hay $60^\circ$.

Por lo tanto

$$\alpha + \beta = 30^\circ.$$

## 10. Resolver $\alpha$ y $\beta$

Además, la hipotenusa nos impone:

$$b^2+c^2=1444.$$

Sustituyendo $b=28\cos\alpha$ y $c=28\cos\beta$:

$$784\cos^2\alpha + 784\cos^2\beta = 1444.$$

Dividiendo entre $784$:

$$\cos^2\alpha + \cos^2\beta = \frac{1444}{784} = \frac{361}{196}.$$

Con $\beta = 30^\circ - \alpha$.

Usemos la identidad $\cos^2\alpha+\cos^2(30^\circ-\alpha)$.

Calculemos:

$$\cos^2\alpha + \cos^2(30^\circ-\alpha)
= \cos^2\alpha + \left(\frac{\sqrt3}{2}\cos\alpha + \frac12\sin\alpha\right)^2.$$

Desarrollando:

$$= \cos^2\alpha + \frac34\cos^2\alpha + \frac{\sqrt3}{2}\sin\alpha\cos\alpha + \frac14\sin^2\alpha.$$

$$= \frac74\cos^2\alpha + \frac14\sin^2\alpha + \frac{\sqrt3}{2}\sin\alpha\cos\alpha.$$

Igualamos a $361/196$.

Podemos expresar en términos de $\cos 2\alpha$. Sabemos:

$$\cos^2\alpha = \frac{1+\cos 2\alpha}{2},\qquad
\sin^2\alpha = \frac{1-\cos 2\alpha}{2},\qquad
\sin\alpha\cos\alpha = \frac{\sin 2\alpha}{2}.$$

Entonces:

$$\frac74\cdot\frac{1+\cos2\alpha}{2}
+\frac14\cdot\frac{1-\cos2\alpha}{2}
+\frac{\sqrt3}{2}\cdot\frac{\sin2\alpha}{2}
= \frac{361}{196}.$$

Simplifiquemos el lado izquierdo.

Primer término: $\frac{7(1+\cos2\alpha)}{8}$.
Segundo término: $\frac{1-\cos2\alpha}{8}$.
Tercer término: $\frac{\sqrt3}{4}\sin2\alpha$.

Suma de los dos primeros:

$$\frac{7+7\cos2\alpha + 1 - \cos2\alpha}{8}
= \frac{8+6\cos2\alpha}{8}
= 1 + \frac34\cos2\alpha.$$

Luego:

$$1+\frac34\cos2\alpha+\frac{\sqrt3}{4}\sin2\alpha = \frac{361}{196}.$$

Restamos $1$:

$$\frac34\cos2\alpha+\frac{\sqrt3}{4}\sin2\alpha
= \frac{361}{196}-1 = \frac{165}{196}.$$

Multiplicamos por $\frac43$:

$$\cos2\alpha + \frac{\sqrt3}{3}\sin2\alpha
= \frac{165}{196}\cdot\frac43 = \frac{55}{49}.$$

## 11. Expresar como coseno de una suma

Notemos que

$$\cos2\alpha + \frac{\sqrt3}{3}\sin2\alpha
= \frac{2}{\sqrt3}\cdot\frac{2\sqrt3/2}{2/\sqrt3}?$$

Mejor: buscamos una combinación lineal $R\cos(2\alpha-\phi)$.

Para $A\cos t + B\sin t = R\cos(t-\phi)$ con $R=\sqrt{A^2+B^2}$ y $\tan\phi = B/A$.

Aquí $A=1$, $B=\sqrt3/3$. Entonces

$$R=\sqrt{1+\frac13} = \sqrt{\frac43} = \frac{2}{\sqrt3}.$$

Y $\tan\phi = \frac{\sqrt3/3}{1} = \frac{\sqrt3}{3} = \frac{1}{\sqrt3}$, por lo que $\phi=30^\circ$.

Entonces:

$$\frac{2}{\sqrt3}\cos(2\alpha-30^\circ) = \frac{55}{49}.$$

Multiplicamos:

$$\cos(2\alpha-30^\circ) = \frac{55}{49}\cdot\frac{\sqrt3}{2} = \frac{55\sqrt3}{98}.$$

Como $\frac{55\sqrt3}{98}\approx 0.972$, es un valor válido para coseno.

## 12. Calcular $\cos2\alpha$ y $\cos2\beta$

Sea $t = 2\alpha - 30^\circ$. Entonces

$$\cos t = \frac{55\sqrt3}{98},\qquad \sin t = \pm\sqrt{1-\cos^2 t}.$$

$$1-\cos^2 t = 1 - \frac{3025\cdot 3}{9604} = 1 - \frac{9075}{9604} = \frac{529}{9604}.$$

Luego $\sin t = \pm \frac{23}{98}$.

Ahora bien, $2\alpha = t+30^\circ$. Necesitamos saber si $K$ y $L$ están dentro. Como $\alpha,\beta>0$ y $\alpha+\beta=30^\circ$, entonces $\alpha,\beta\in(0,30^\circ)$. Por tanto $2\alpha\in(0,60^\circ)$ y $t = 2\alpha - 30^\circ \in (-30^\circ, 30^\circ)$.

Entonces $\sin t$ tiene el mismo signo que $t$. No sabemos aún el signo, pero lo resolveremos con la condición $\beta>0$.

Tenemos

$$\cos2\alpha = \cos(t+30^\circ) = \cos t\cos30^\circ - \sin t\sin30^\circ.$$

Caso $\sin t = +23/98$:

$$\cos2\alpha = \frac{55\sqrt3}{98}\cdot\frac{\sqrt3}{2} - \frac{23}{98}\cdot\frac12
= \frac{165}{196} - \frac{23}{196}
= \frac{142}{196} = \frac{71}{98}.$$

Caso $\sin t = -23/98$:

$$\cos2\alpha = \frac{165}{196} + \frac{23}{196}
= \frac{188}{196} = \frac{47}{49}.$$

Además $\beta = 30^\circ-\alpha$, de modo que

$$2\beta = 60^\circ - 2\alpha.$$

Como $\alpha+\beta=30^\circ$, tenemos $2\beta=60^\circ-2\alpha$.

Calculemos $\cos2\beta$ en cada caso.

Recordemos $\beta = 30^\circ - \alpha$. Entonces

$$2\beta = 60^\circ - 2\alpha.$$

Por tanto

$$\cos2\beta = \cos(60^\circ - 2\alpha)
= \cos60^\circ\cos2\alpha + \sin60^\circ\sin2\alpha.$$

Necesitamos $\sin2\alpha$ en cada caso.

Para $2\alpha = t+30^\circ$:

$$\sin2\alpha = \sin(t+30^\circ)
= \sin t\cos30^\circ + \cos t\sin30^\circ.$$

Caso 1: $\sin t = 23/98$.

$$\sin2\alpha = \frac{23}{98}\cdot\frac{\sqrt3}{2} + \frac{55\sqrt3}{98}\cdot\frac12
= \frac{23\sqrt3+55\sqrt3}{196}
= \frac{78\sqrt3}{196}
= \frac{39\sqrt3}{98}.$$

Entonces

$$\cos2\beta = \frac12\cdot\frac{71}{98} + \frac{\sqrt3}{2}\cdot\frac{39\sqrt3}{98}
= \frac{71}{196} + \frac{117}{196}
= \frac{188}{196}
= \frac{47}{49}.$$

Caso 2: $\sin t = -23/98$.

$$\sin2\alpha = \frac{-23\sqrt3+55\sqrt3}{196}
= \frac{32\sqrt3}{196}
= \frac{8\sqrt3}{49}.$$

Entonces

$$\cos2\beta = \frac12\cdot\frac{47}{49} + \frac{\sqrt3}{2}\cdot\frac{8\sqrt3}{49}
= \frac{47}{98} + \frac{24}{98}
= \frac{71}{98}.$$

Observamos que los dos casos son simétricos intercambiando $\alpha$ y $\beta$: un caso da $(\cos 2\alpha,\cos2\beta) = (71/98, 47/49)$ y el otro $(47/49, 71/98)$. Ambos corresponden simplemente a intercambiar los papeles de $b$ y $c$, lo cual no cambia el resultado final del área. Elegimos, por ejemplo,

$$\cos2\alpha = \frac{71}{98},\qquad \cos2\beta=\frac{47}{49}.$$

## 13. Cálculo de $\sin2\alpha$ y $\sin2\beta$

Para el caso elegido, $\sin t=23/98$ y hallamos

$$\sin2\alpha = \frac{39\sqrt3}{98}.$$

Para $\beta$, como $2\beta=60^\circ-2\alpha$:

$$\sin2\beta = \sin(60^\circ-2\alpha)
= \sin60^\circ\cos2\alpha - \cos60^\circ\sin2\alpha.$$

Usando $\cos2\alpha=71/98$ y $\sin2\alpha=39\sqrt3/98$:

$$\sin2\beta = \frac{\sqrt3}{2}\cdot\frac{71}{98}
- \frac12\cdot\frac{39\sqrt3}{98}
= \frac{71\sqrt3 - 39\sqrt3}{196}
= \frac{32\sqrt3}{196}
= \frac{8\sqrt3}{49}.$$

## 14. Áreas de $ABK$ y $ACL$

Recordemos

$$[ABK]=98\sin2\alpha = 98\cdot\frac{39\sqrt3}{98} = 39\sqrt3.$$

$$[ACL]=98\sin2\beta = 98\cdot\frac{8\sqrt3}{49}
= \frac{784\sqrt3}{49}
= 16\sqrt3.$$

## 15. Área de $ABC$

$$[ABC]=\frac12 bc.$$

Con $b=28\cos\alpha$ y $c=28\cos\beta$:

$$bc = 784\cos\alpha\cos\beta.$$

Usamos $\cos\alpha\cos\beta = \frac{\cos(\alpha+\beta)+\cos(\alpha-\beta)}{2}$.

Sabemos $\alpha+\beta=30^\circ$, luego $\cos(\alpha+\beta)=\sqrt3/2$.

Además $\alpha-\beta = 2\alpha - 30^\circ = t$. Entonces $\cos(\alpha-\beta)=\cos t = 55\sqrt3/98$.

Por tanto:

$$\cos\alpha\cos\beta
= \frac12\left(\frac{\sqrt3}{2}+\frac{55\sqrt3}{98}\right).$$

Calculemos:

$$\frac{\sqrt3}{2} = \frac{49\sqrt3}{98}.$$

Sumamos:

$$\frac{49\sqrt3+55\sqrt3}{98} = \frac{104\sqrt3}{98} = \frac{52\sqrt3}{49}.$$

Entonces

$$\cos\alpha\cos\beta = \frac12\cdot\frac{52\sqrt3}{49} = \frac{26\sqrt3}{49}.$$

Luego

$$bc = 784\cdot\frac{26\sqrt3}{49}
= \frac{784}{49}\cdot 26\sqrt3
= 16\cdot 26\sqrt3
= 416\sqrt3.$$

Por tanto:

$$[ABC] = \frac12\cdot 416\sqrt3 = 208\sqrt3.$$

## 16. Área del cuadrilátero $BKLC$

Ahora:

$$[BKLC] = [ABC] - [ABK] - [ACL] - [AKL].$$

Sustituimos:

- $[ABC]=208\sqrt3$
- $[ABK]=39\sqrt3$
- $[ACL]=16\sqrt3$
- $[AKL]=49\sqrt3$

Entonces:

$$[BKLC] = 208\sqrt3 - 39\sqrt3 - 16\sqrt3 - 49\sqrt3
= (208-39-16-49)\sqrt3
= 104\sqrt3.$$

Por lo tanto $n=104$.

\[
\boxed{104}
\]