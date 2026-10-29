

Voy a razonar paso a paso.

Sea \(f(x)=ax^2+bx+c\). Sabemos que \(|f(x)|\le 1\) para todo \(x\in[0,1]\). Queremos maximizar \(|a|+|b|+|c|\).

**Paso 1: Expresar los coeficientes en términos de valores de la función**

Evaluemos en tres puntos convenientes: \(x=0,\frac12,1\).

\[
f(0)=c
\]
\[
f(1)=a+b+c
\]
\[
f\!\left(\tfrac12\right)=\frac{a}{4}+\frac{b}{2}+c
\]

Tenemos:
\[
a=2f(1)+2f(0)-4f\!\left(\tfrac12\right)
\]

Verifiquemos:
\[
2(a+b+c)+2c-4\left(\frac{a}{4}+\frac{b}{2}+c\right)
=2a+2b+2c+2c-a-2b-4c=a.
\]
Correcto.

Para \(b\):
\[
b=4f\!\left(\tfrac12\right)-f(1)-3f(0)
\]

Verifiquemos:
\[
4\left(\frac{a}{4}+\frac{b}{2}+c\right)-(a+b+c)-3c
=a+2b+4c-a-b-c-3c=b.
\]
Correcto.

**Paso 2: Acotar una combinación particular**

Como \(|f(x)|\le 1\) para todo \(x\in[0,1]\), en particular \(|f(0)|,|f(1)|,|f(1/2)|\le 1\).

Evaluemos el valor de \(a\) si queremos hacer todos los coeficientes grandes y con el mismo signo. Intuimos que el máximo se alcanza cuando alguno de los coeficientes es negativo y los otros dos positivos, porque \(a\) y \(b\) están ligados por valores en extremos y punto medio.

**Paso 3: Determinar la estructura óptima**

Vamos a plantear el caso en que \(a>0\), \(b>0\) y \(c<0\) (el polinomio es convexo y en \(x=0\) toma valor negativo). Entonces \(|a|+|b|+|c|=a+b-c\) (con \(c<0\)).

Usando \(c=f(0)\) y \(a+b+c=f(1)\), tenemos \(a+b=f(1)-f(0)\).

Para maximizar \(a+b-c\) con \(c\) negativo, queremos que \(f(0)=c\) esté cerca de \(-1\) y \(f(1)\) cerca de \(1\).

**Paso 4: Usar la restricción en el punto medio**

De la expresión de \(a\):
\[
a=2f(1)+2f(0)-4f(1/2).
\]

Para \(a>0\) grande, queremos \(f(1/2)\) negativo. Pongamos \(f(0)=-1\), \(f(1)=1\), \(f(1/2)=-1\).

Entonces:
\[
a=2(1)+2(-1)-4(-1)=4
\]
\[
b=4(-1)-1-3(-1)=0
\]
\[
c=-1
\]

Aquí \(|a|+|b|+|c|=4+0+1=5\).

**Paso 5: Mejorar haciendo \(b\) positivo**

El caso \(a=4,b=0,c=-1\) da suma 5, pero queremos \(b>0\) para sumar más. Sin embargo, aumentar \(b\) desde 0 requiere cambiar los valores, reduciendo \(a\).

Probemos con un polinomio que toca los extremos. Queremos \(f(0)=-1\), \(f(1)=1\) y \(\min f(x)=-1\) en algún punto interior con vértice en \(x=-\frac{b}{2a}\).

Sea el vértice en \(x=t\in(0,1)\). Como \(f\) es convexa con \(a>0\) y el mínimo es \(-1\), de modo que \(f(t)=-1\).

Entonces \(f(x)=a(x-t)^2-1\) con la condición \(f(0)=-1\) y \(f(1)=1\).

De \(f(0)=-1\):
\[
a t^2 -1 = -1 \implies a t^2=0
\]
Esto fuerza \(t=0\), contradiciendo \(t\in(0,1)\).

Por tanto no podemos tener simultáneamente \(f(0)=-1\) y \(f(1)=1\) con un mínimo interior igual a \(-1\). Debemos elegir un vértice interior y ajustar los extremos.

**Paso 6: Configuración con vértice interior**

Sea \(f(x)=a(x-t)^2-1\) con \(a>0\) y \(0<t<1\), de modo que el mínimo es \(-1\). Imponemos también \(f(1)=1\):

\[
a(1-t)^2-1=1 \implies a(1-t)^2=2 \implies a=\frac{2}{(1-t)^2}.
\]

Ahora \(c=f(0)=a t^2-1=\frac{2t^2}{(1-t)^2}-1\).

Además \(b=-2at=-\frac{4t}{(1-t)^2}\).

Como \(b<0\), tenemos \(|a|+|b|+|c|=a+|b|+|c|\), con \(c\) que podría ser positivo o negativo.

Calculemos \(c\): \(c=\frac{2t^2}{(1-t)^2}-1\). Queremos que \(|c|\) no sea tan grande... En realidad maximizamos \(a+|b|+|c|\).

**Paso 7: Analizar la función objetivo**

\[
S(t)=\frac{2}{(1-t)^2}+\frac{4t}{(1-t)^2}+\left|\frac{2t^2}{(1-t)^2}-1\right|.
\]

Primer término y segundo:
\[
\frac{2+4t}{(1-t)^2}.
\]

Para \(c\): ¿positivo o negativo? El mínimo de \(x^2\) en \(t\) es \(-1\), y \(c=f(0)\). Dado que el mínimo es \(-1\) y el polinomio es convexo, \(f(0)\) podría ser negativo. De hecho, si \(t<1/2\), el valor \(x=0\) queda a la izquierda del vértice y \(f(0)>-1\), pero podría ser negativo.

Resolvamos \(c=0\):
\[
\frac{2t^2}{(1-t)^2}=1 \implies \sqrt{2}\,t=1-t \implies t=\frac{1}{1+\sqrt{2}}=\sqrt{2}-1\approx 0.414.
\]

Para \(t<\sqrt2-1\), \(c<0\); para \(t>\sqrt2-1\), \(c>0\).

Probemos ambas ramas.

**Caso \(c<0\) (\(t<\sqrt2-1\))**: 
\[
S(t)=\frac{2+4t}{(1-t)^2}-\left(\frac{2t^2}{(1-t)^2}-1\right)
=\frac{2+4t-2t^2}{(1-t)^2}+1.
\]

Derivemos. Mejor probemos un valor numérico. En \(t=0.3\):
\[
S=\frac{2+1.2}{0.49}=6.5306,\quad |c|=\left|\frac{0.18}{0.49}-1\right|=0.6327,
\]
total \(6.5306+0.6327=7.163\).

Esto ya supera 5.

**Caso \(c>0\) (\(t>\sqrt2-1\))**:
\[
S(t)=\frac{2+4t}{(1-t)^2}+\frac{2t^2}{(1-t)^2}-1
=\frac{2+4t+2t^2}{(1-t)^2}-1.
\]

Derivemos:

\[
S'(t)=\frac{(4+4t)(1-t)^2-(2+4t+2t^2)\cdot 2(1-t)(-1)}{(1-t)^4}.
\]

Simplifiquemos el numerador:
\[
(4+4t)(1-t)^2+2(2+4t+2t^2)(1-t).
\]

En \(t=0.5\):
\[
S=\frac{2+2+0.5}{0.25}-1=\frac{4.5}{0.25}-1=18-1=17.
\]

¡17! Verifiquemos: \(t=0.5\), \(a=\frac{2}{0.25}=8\), \(b=-\frac{4\cdot 0.5}{0.25}=-8\), \(c=\frac{2\cdot0.25}{0.25}-1=1\).

Entonces \(|a|+|b|+|c|=8+8+1=17\).

¿Cumple \(|f(x)|\le1\) en \([0,1]\)?

\[
f(x)=8x^2-8x+1=8(x-0.5)^2-1.
\]

En \(x=0\): \(f(0)=1\). En \(x=0.5\): \(f=-1\). En \(x=1\): \(f=1\). Como la parábola es convexa, el mínimo está en \(x=0.5\) y vale \(-1\); los máximos en los extremos valen 1. Así pues, \(|f(x)|\le1\) para todo \(x\in[0,1]\).

Esto da \(8+8+1=17\).

**Paso 8: ¿Se puede superar 17?**

Por simetría, si consideramos \(f\) cóncava, obtendríamos \(a=-8\), \(b=8\), \(c=-1\) o configuraciones similares, con la misma suma 17.

Planteemos el problema con la transformación que maximiza. La condición \(|f(x)|\le1\) en \([0,1]\) implica que el polinomio cuadrático tiene ciertas propiedades en la frontera. Se puede demostrar con la condición de que el polinomio de grado 2 es la interpolación en tres puntos.

Consideremos la función lineal que interpola en \(0\) y \(1\): \(L(x)=c+(a+b+c-c)x=c+(a+b)x\). Como hay un término cuadrático \(a x^2+b x+c\), la curvatura está dada por \(a\).

**Paso 9: Cota formal**

Usemos las identidades:
\[
a=\frac{f(0)-2f(1/2)+f(1)}{2}\cdot 2 = ?
\]

En realidad, para el operador diferencias: 
\[
a=\frac{f(1)-2f(1/2)+f(0)}{2(1/2)^2}=2(f(1)-2f(1/2)+f(0)).
\]

Esto coincide con la expresión anterior.

Queremos acotar \(|a|+|b|+|c|\). Notemos que la curva \(8x^2-8x+1\) alcanza \(a=8,b=-8,c=1\) con suma 17. ¿La cota general podría ser 19?

Probemos la familia \(f(x)=a(x-t)^2+m\) con \(m=-1\) (mínimo). El máximo de \(a\) se da cuando \(t\) está más cerca de un extremo: \(a=\frac{2}{(1-t)^2}\) crece al acercar \(t\) a 1. Si \(t\to1\), \(a\to\infty\), pero \(b\to-\infty\) también, y \(c\to\infty\). Sin embargo, la restricción \(|f(0)|\le1\) limita \(t\).

Con \(f(x)=a(x-t)^2-1\):
\[
f(0)=a t^2-1 \in[-1,1] \implies 0\le at^2\le 2.
\]
\[
f(1)=a(1-t)^2-1 \in[-1,1] \implies 0\le a(1-t)^2\le 2.
\]

De \(f(1)\): \(a\le \frac{2}{(1-t)^2}\).

Queremos maximizar \(|a|+|b|+|c|\). Como el mínimo es en \(t\), hay una relación entre \(a,b,c\).

Ya vimos \(S(t)\) crece en la rama \(c>0\) al acercar \(t\) a 1, pero \(t\) no puede acercarse tanto a 1 porque \(f(0)\) se haría mayor que 1. En efecto, \(f(0)=at^2-1\le1\) da \(at^2\le2\), es decir \(\frac{2t^2}{(1-t)^2}\le2\), lo que implica \(t\le \frac{1}{1+\sqrt{?}}\).

Resolvamos:
\[
\frac{2t^2}{(1-t)^2}\le2 \implies t^2\le(1-t)^2 \implies t\le 1-t \implies t\le 0.5.
\]

¡Ajá! Para que \(f(0)\le1\) con mínimo \(-1\), necesitamos \(t\le0.5\). Entonces el máximo en la rama \(c>0\) está en \(t=0.5\), dando \(S=17\).

Para la rama \(c<0\), t varía en \((0,\sqrt2-1)\), y \(S(t)\) era creciente o tenía su máximo en \(t=0.5\) no permitido. Probemos en \(t=\sqrt2-1\approx0.414\):
\[
a=\frac{2}{(0.586)^2}=5.828,\quad |b|=\frac{4\cdot0.414}{0.343}=4.828,\quad c=0
\]
suma \(10.656<17\).

Así, el máximo con mínimo interior y \(a>0\) es 17, y se alcanza en \(t=0.5\).

**Paso 10: Simetría y caso con máximo interior**

De manera análoga, si la parábola es cóncava (\(a<0\)), el máximo interior alcanza 1 y los extremos \(-1\), se obtiene la misma suma.

Concluimos que el valor máximo es 17.

Por tanto:

\[
\boxed{17}
\]