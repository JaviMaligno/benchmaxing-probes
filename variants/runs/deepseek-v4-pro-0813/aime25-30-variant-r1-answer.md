Voy a resolver el problema paso a paso.

Tenemos
\[
g(x)=\frac{(x-8)(x-50)(x-72)(x-k)}{x},\qquad x>0.
\]

Queremos hallar exactamente tres valores positivos de \(k\) para los cuales \(g\) alcanza su mínimo en exactamente dos puntos \(x>0\).

## 1. Expansión del polinomio

Primero desarrollamos el numerador, excepto por el factor en \(k\). Sea
\[
P(x)=(x-8)(x-50)(x-72).
\]

Calculemos los productos paso a paso.

\[
(x-8)(x-50)=x^2-58x+400.
\]

Luego,
\[
(x^2-58x+400)(x-72)
= x^3-72x^2-58x^2+58\cdot72\,x+400x-400\cdot72.
\]

Como \(58\cdot72=4176\) y \(400\cdot72=28800\),

\[
P(x)=x^3-(72+58)x^2+(4176+400)x-28800
\]
\[
=x^3-130x^2+4576x-28800.
\]

Multiplicamos ahora por \(x-k\):

\[
(x-k)P(x)=xP(x)-kP(x).
\]

Primero,
\[
xP(x)=x^4-130x^3+4576x^2-28800x.
\]

También,
\[
-kP(x)=-kx^3+130kx^2-4576kx+28800k.
\]

Sumando,
\[
(x-k)P(x)=x^4-(130+k)x^3+(4576+130k)x^2-(28800+4576k)x+28800k.
\]

Entonces
\[
g(x)=\frac{x^4-(130+k)x^3+(4576+130k)x^2-(28800+4576k)x+28800k}{x}
\]
\[
=x^3-(130+k)x^2+(4576+130k)x-(28800+4576k)+\frac{28800k}{x}.
\]

## 2. Derivada de \(g\)

Derivamos:
\[
g'(x)=3x^2-2(130+k)x+(4576+130k)-\frac{28800k}{x^2}.
\]

Igualamos a cero:
\[
3x^2-2(130+k)x+(4576+130k)-\frac{28800k}{x^2}=0.
\]

Multiplicamos por \(x^2\) para obtener
\[
3x^4-2(130+k)x^3+(4576+130k)x^2-28800k=0.
\]

Sea
\[
Q(x)=3x^4-2(130+k)x^3+(4576+130k)x^2-28800k.
\]

Tenemos \(g'(x)=\frac{Q(x)}{x^2}\), así que los puntos críticos \(x>0\) son exactamente las raíces positivas de \(Q\).

## 3. Raíces conocidas de \(Q\)

Observemos un hecho clave. Los ceros \(8,50,72,k\) del numerador juegan un papel especial. Derivemos una factorización útil.

Note que si \(x=a\) es una raíz del numerador \(h(x)=(x-8)(x-50)(x-72)(x-k)\), entonces
\[
g(x)=\frac{h(x)}{x}.
\]
La derivada es
\[
xg'(x)=h'(x)-g(x)?
\]

Mejor hagámoslo explícitamente:
\[
g'(x)=\frac{xh'(x)-h(x)}{x^2}.
\]

En \(x=8\), como \(h(8)=0\),
\[
g'(8)=\frac{8h'(8)}{64}=\frac{h'(8)}8.
\]

Para las raíces simples de \(h\),
\[
h'(8)=(8-50)(8-72)(8-k).
\]
Es decir,
\[
h'(8)=(-42)(-64)(8-k)=2688(8-k).
\]

Entonces
\[
g'(8)=336(8-k).
\]

De forma análoga,
\[
g'(50)=\frac{50(50-8)(50-72)(50-k)}{50^2}
=\frac{(42)(-22)(50-k)}{50}
=\frac{-924(50-k)}{50}.
\]

Y
\[
g'(72)=\frac{(64)(22)(72-k)}{72}
=\frac{1408(72-k)}{72}
=\frac{176}{9}(72-k).
\]

Estos cálculos serán útiles, aunque quizá lo más importante viene de la estructura de \(Q\).

## 4. Puntos críticos que son raíces de \(P\)

Consideremos \(x=8,50,72\) que son las raíces de \(P(x)=(x-8)(x-50)(x-72)\).

Para \(x=r\) con \(P(r)=0\),
\[
g(x)=\frac{P(x)(x-k)}x.
\]

Para \(x=8\):
\[
P(8)=0,
\]
y la expresión de \(g'(x)\) simplifica. Calculemos directamente \(Q(x)\) para \(x=8\):
\[
Q(8)=3\cdot8^4-2(130+k)\cdot8^3+(4576+130k)\cdot8^2-28800k.
\]

\[
8^2=64,\quad 8^3=512,\quad 8^4=4096.
\]

Entonces
\[
Q(8)=12288-1024(130+k)+64(4576+130k)-28800k.
\]

\[
=12288-133120-1024k+292864+8320k-28800k.
\]

Sumando las constantes:
\[
12288-133120+292864=172032.
\]

Sumando los términos con \(k\):
\[
-1024+8320-28880=-21504.
\]

Así,
\[
Q(8)=172032-21504k=21504(8-k).
\]

Esto coincide con el cálculo anterior:
\[
g'(8)=\frac{Q(8)}{64}=\frac{21504(8-k)}{64}=336(8-k).
\]

De manera similar se obtienen las otras.

## 5. Relación con \(g\)

El comportamiento de \(g\):

- Como \(x\to0^+\), el término \(\frac{28800k}{x}\to+\infty\) si \(k>0\). Así que \(g\to+\infty\).
- Como \(x\to+\infty\), \(g\sim x^3\), así que \(g\to+\infty\).

Por tanto, el mínimo global se alcanza en puntos críticos interiores.

Para que el mínimo se alcance exactamente en dos puntos, necesitamos que la derivada \(g'\) tenga varias raíces positivas y que dos de ellas sean mínimos globales con el mismo valor.

## 6. Caso en que \(g\) tiene dos puntos críticos iguales en valor

Una manera natural: el mínimo global se produce en dos raíces distintas de \(P\) (es decir, dos de \(8,50,72\)) cuando sus valores de \(g\) coinciden, y además son los menores.

Calculemos \(g\) en las raíces de \(P\).

Para \(x=8\):
\[
g(8)=\frac{P(8)(8-k)}8=0
\]
pues \(P(8)=0\). Espera, eso no puede ser correcto, porque \(g\) tiene mínimo positivo. Déjame revisar.

En realidad, si \(x=8\), el numerador es \(0\), así que \(g(8)=0\). El valor de \(g\) puede ser negativo si el numerador es negativo.

Revisemos el comportamiento de \(g\). El numerador \(h(x)=(x-8)(x-50)(x-72)(x-k)\).

Los signos de \(h(x)\) dependen de la posición de \(k\) entre las raíces.

Como \(x\to0^+\), \(g\sim\frac{h(0)}x\) con \(h(0)=(-8)(-50)(-72)(-k)=28800k>0\), así que \(g\to+\infty\).

Como \(x\to+\infty\), \(g\to+\infty\).

Sin embargo, no podemos concluir simplemente que el mínimo sea positivo. De hecho, \(g\) puede ser negativo, ya que \(g(8)=0\) pero entre raíces puede ser negativo.

Veamos: Para \(x=50\), \(g(50)=0\). Para \(x=72\), \(g(72)=0\). Para \(x=k\), \(g(k)=0\). Pero en los intervalos entre estas raíces, \(g\) puede ser negativa.

Por tanto, el mínimo global seguramente es negativo, y se alcanza en alguna región donde \(h(x)<0\).

Esto sugiere que los puntos donde \(g\) cambia de signo y las raíces de la derivada determinan la ubicación del mínimo.

## 7. Estrategia algebraica

Para hallar los valores de \(k\) en que el mínimo se alcanza exactamente dos veces, necesitamos igualar valores de \(g\) en dos puntos críticos distintos y además asegurar que son el mínimo global.

Puntos críticos posibles:

1. Dos raíces de \(P\) (como \(8\) y \(50\), etc.) que sean mínimos con el mismo valor (ambos darían \(0\), pero \(0\) no es mínimo si hay valores negativos).

Espera, \(g(8)=g(50)=g(72)=g(k)=0\). Entonces si el mínimo global es \(0\), se alcanza en las cuatro raíces. Si el mínimo es negativo, se alcanza en puntos intermedios.

Así que para tener exactamente dos puntos de mínimo, el valor mínimo debe ser negativo y alcanzarse exactamente dos veces.

Los puntos críticos interiores están en los intervalos donde \(g\) decrece y luego crece. Como \(g\) es diferenciable y tiende a \(+\infty\) en los extremos, cada valle local en un intervalo de decrecimiento da un punto de mínimo.

## 8. Estructura de \(g'\): discriminante

Podemos reescribir \(Q\) para buscar raíces dobles de \(g'\), es decir, valores de \(k\) para los cuales \(Q\) tiene una raíz doble. Si \(Q\) tiene una raíz doble en \(x_0>0\), entonces \(g'\) se anula dos veces en el mismo punto, y la función es estacionaria de orden superior. Eso puede hacer que el mínimo se alcance exactamente dos veces (dos puntos) para ciertos \(k\).

El discriminante de \(Q\) en \(x\) será un polinomio en \(k\). Las raíces reales de este discriminante darán los \(k\) candidatos.

Calculemos el discriminante de
\[
Q=3x^4-2(130+k)x^3+(4576+130k)x^2-28800k.
\]

El discriminante de un polinomio de grado 4:
\[
\Delta = 256a^3e^3-192a^2bde^2-128a^2c^2e^2+144a^2cd^2e-27a^2d^4
\]
donde
\[
Q=ax^4+bx^3+cx^2+dx+e
\]
con
\[
a=3,\quad b=-2(130+k),\quad c=4576+130k,\quad d=0,\quad e=-28800k.
\]

Aquí \(d=0\), lo que simplifica bastante.

Con \(d=0\):
\[
\Delta=256a^3e^3-192a^2b\cdot0+(-128a^2c^2e^2)+0+0
\]
\[
=256a^3e^3-128a^2c^2e^2.
\]

Además faltan términos con \(b\), pero con \(d=0\) todos los términos con \(b\) tienen factor \(d\), así que se anulan. Veamos: el primer término con \(b\) es \(-192a^2bde^2\), que es cero. El término \(b^2\) no aparece cuando \(d=0\) en la fórmula general de discriminante de cuártica. En efecto, para \(d=0\):

\[
\Delta=256a^3e^3-128a^2c^2e^2+144a^2c\cdot0-27a^2\cdot0
\]
más términos con \(b\) que tienen \(d\) o \(e\)? Déjame ver la fórmula completa.

La fórmula completa del discriminante de cuártica es:
\[
\Delta = 256a^3e^3 - 192a^2bde^2 - 128a^2c^2e^2 + 144a^2cd^2e - 27a^2d^4 
\]
\[
+ 144ab^2d e^2 - 6ab^2 d^2 e - 80abc d e^2 + 18abcd^2 e + 16ac^3 d^2 - 4ac^3 e^2?
\]

No, esa no es la forma estándar. Mejor usaré una calculadora simbólica mental o un enfoque distinto.

## 9. Raíces dobles de \(Q\) y condición de tangencia

Una forma más directa: el discriminante de \(Q\) con respecto a \(x\) es un polinomio en \(k\). Expresémoslo factorizando.

Sabemos que \(g'(x)=3x^2-2(130+k)x+4576+130k-\frac{28800k}{x^2}\).

La condición para un punto de inflexión horizontal o raíz doble se traduce en que \(Q\) y \(Q'\) comparten una raíz. Es decir, eliminamos \(x\) del sistema
\[
Q(x)=0,\quad Q'(x)=0.
\]

El resultante con respecto a \(x\) es un polinomio en \(k\), y sus raíces reales son los \(k\) para los que \(Q\) tiene una raíz doble (o una raíz de orden superior).

## 10. Calculemos el resultante numéricamente

Voy a usar álgebra con precisión. Escribamos \(Q\) en forma más manejable.

Observamos que
\[
g'(x)=\frac{Q(x)}{x^2}.
\]

Podemos factorizar \(Q\) parcialmente. Notemos que \(Q\) escrita en términos de \(x-8, x-50, x-72\) puede simplificar.

Sabemos que \(g(x)=\frac{(x-8)(x-50)(x-72)(x-k)}x\).

Sea \(h(x)=(x-8)(x-50)(x-72)(x-k)\).

Entonces
\[
g'(x)=\frac{h'(x)x-h(x)}{x^2}.
\]

Si \(x\) es raíz de \(P(x)=(x-8)(x-50)(x-72)\) pero no de \(x\) o \(x-k\), entonces \(h(x)=0\), y
\[
g'(x)=\frac{h'(x)}x.
\]

Para \(x=8,50,72\), ya calculamos esos valores.

Para \(x=k\):
\[
g'(k)=\frac{h'(k)k-h(k)}{k^2}=\frac{h'(k)k}{k^2}=\frac{h'(k)}k
\]
pues \(h(k)=0\).

\[
h'(k)=P(k)=(k-8)(k-50)(k-72).
\]

Así,
\[
g'(k)=\frac{(k-8)(k-50)(k-72)}k.
\]

De manera similar, en \(x=8\):
\[
g'(8)=\frac{h'(8)}8=\frac{P'(8)(8-k)}8.
\]

Como \(P'(8)=(8-50)(8-72)=2688\),
\[
g'(8)=336(8-k).
\]

En \(x=50\):
\[
P'(50)=(50-8)(50-72)=42\cdot(-22)=-924.
\]
\[
g'(50)=\frac{-924(50-k)}{50}=\frac{462}{25}(k-50).
\]

En \(x=72\):
\[
P'(72)=(72-8)(72-50)=64\cdot22=1408.
\]
\[
g'(72)=\frac{1408(72-k)}{72}=\frac{176}{9}(72-k).
\]

## 11. Raíces de \(Q\) en términos de puntos críticos

El polinomio \(Q\) es de grado 4. Conocemos su valor en \(x=8,50,72\):
\[
Q(8)=64\cdot336(8-k)=21504(8-k),
\]
\[
Q(50)=2500\cdot\frac{462}{25}(k-50)=46200(k-50),
\]
\[
Q(72)=5184\cdot\frac{176}{9}(72-k)=101376(72-k).
\]

Como \(Q\) es de grado 4 con coeficiente principal 3, y conocemos tres valores, podríamos intentar hallar una factorización parcial.

Quizá \(Q\) se puede escribir como producto de dos cuadráticas cuyos coeficientes dependen de \(k\). La presencia de \(d=0\) (sin término \(x\)) sugiere que \(Q\) podría factorizar.

## 12. Intentemos factorizar \(Q\) mediante simetría

Consideremos \(Q(x)=x^2g'(x)\):
\[
Q(x)=3x^4-2(130+k)x^3+(4576+130k)x^2-28800k.
\]

Intentemos una factorización de la forma
\[
Q(x)=(x^2+ax+b)(3x^2+cx+d)
\]
con coeficientes dependientes de \(k\). Igualando coeficientes:

Desarrollamos:
\[
(x^2+ax+b)(3x^2+cx+d)
=3x^4+(c+3a)x^3+(d+ac+3b)x^2+(ad+bc)x+bd.
\]

Comparando con \(Q\):
\[
3x^4-(2(130+k))x^3+(4576+130k)x^2+0\cdot x-28800k.
\]

El coeficiente de \(x\) es 0:
\[
ad+bc=0.
\]

El término constante:
\[
bd=-28800k.
\]

Coeficiente de \(x^3\):
\[
c+3a=-2(130+k).
\]

Coeficiente de \(x^2\):
\[
d+ac+3b=4576+130k.
\]

Tenemos cuatro incógnitas \(a,b,c,d\) y cuatro ecuaciones. Intentemos suponer que las raíces de \(Q\) son simétricas en algún sentido.

## 13. Enfoque distinto: condición de mínimo doble global

El problema pide exactamente tres valores de \(k\). Una pista: esos tres valores probablemente están relacionados con las raíces \(8,50,72\) y forman una media de algún tipo.

Pensemos en el caso en que el mínimo global se alcanza en dos puntos \(x_1,x_2\), ambos positivos, y es el mismo valor \(m\). Entonces, en \(x_1\) y \(x_2\), la curva \(y=g(x)\) y la recta horizontal \(y=m\) son tangentes. Es decir, \(g(x)-m\) tiene raíces dobles en \(x_1\) y \(x_2\).

Como \(g\) tiende a \(+\infty\) en los extremos, su gráfica tiene valles. Para que el mínimo se alcance exactamente en dos puntos, debe haber dos valles a la misma altura \(m\), que es la más baja.

## 14. Consideremos casos límite

Cuando \(k\) coincide con una de las raíces \(8,50,72\), el factor \((x-k)\) duplica una raíz del numerador. Veamos qué pasa.

Por ejemplo, si \(k=8\):
\[
g(x)=\frac{(x-8)^2(x-50)(x-72)}x.
\]
En \(x=8\), ahora \(h\) tiene una raíz doble, así que \(g(8)=0\) y \(g'(8)=0\). Entonces \(x=8\) es un punto crítico. Como \(g\) cruza o toca el eje en \(x=8\) con multiplicidad 2, hay un extremo local en \(x=8\). ¿Será mínimo? En \(x=8\), el valor es \(0\). Como \(g\) es negativa en algún intervalo, el mínimo global es negativo. Así que \(x=8\) no es mínimo global (es un máximo local si la función es negativa cerca). Por tanto, \(k=8\) no da un mínimo en dos puntos; el mínimo se alcanza una sola vez (o en dos puntos intermedios).

Así que los valores buscados de \(k\) no son \(8,50,72\).

## 15. Busquemos raíces dobles del discriminante

Para hallar precisamente los \(k\), calculo el discriminante de \(Q\) con respecto a \(x\). Usaré la fórmula del discriminante de cuártica, teniendo cuidado con el término \(d=0\).

La fórmula general para el discriminante de un polinomio cuártico \(ax^4+bx^3+cx^2+dx+e\) es:

\[
\Delta = 256a^3e^3 - 192a^2bde^2 - 128a^2c^2e^2 + 144a^2cd^2e - 27a^2d^4
\]
\[
+ 144ab^2d^2e - 6ab^2d^4 + 80abcde^2 - 18abcd^2e - 4ac^3d^2
\]
\[
+ 16ac^4e - 4b^3d^2e + b^2c^2d^2 - 4b^2c^3e - 27b^4e^2 + 18b^3cde + 4b^3d^3 + b^2c^2e^2?
\]

No, no recuerdo exactamente. Mejor usar el resultante de \(Q\) y \(Q'\).

## 16. Factorización usando las raíces 8, 50, 72

Consideremos la peculiar estructura. Hemos notado que para las raíces \(r\in\{8,50,72\}\), tenemos \(Q(r)=C_r(r-k)\) con \(C_r\) constante. Eso sugiere que \(Q\) es un polinomio en \(k\) de grado 1 para \(x\) fijo. De hecho, \(Q\) es lineal en \(k\):

\[
Q(x)=3x^4-260x^3-2kx^3+4576x^2+130kx^2-28800k.
\]

Agrupando los términos con \(k\):
\[
Q(x)=(3x^4-260x^3+4576x^2)+k(-2x^3+130x^2-28800).
\]

Sea
\[
A(x)=3x^4-260x^3+4576x^2,
\]
\[
B(x)=-2x^3+130x^2-28800.
\]

Entonces
\[
Q(x)=A(x)+kB(x).
\]

Para que \(x\) sea punto crítico de \(g\) para un \(k\) dado, tenemos \(Q(x)=0\). Para que, además, sea una raíz doble (punto crítico degenerado), necesitamos también \(Q'(x)=0\).

Entonces,
\[
Q'(x)=A'(x)+kB'(x)=0.
\]

De \(Q(x)=0\) obtenemos
\[
k=-\frac{A(x)}B(x).
\]

Sustituyendo en \(Q'(x)=0\):
\[
A'(x)-\frac{A(x)}B(x)B'(x)=0.
\]

Es decir,
\[
A'(x)B(x)-A(x)B'(x)=0.
\]

Esto define una ecuación solo en \(x\). Resolvámosla.

## 17. Cálculo de \(A'\), \(B'\)

\[
A(x)=3x^4-260x^3+4576x^2.
\]
\[
A'(x)=12x^3-780x^2+9152x.
\]

\[
B(x)=-2x^3+130x^2-28800.
\]
\[
B'(x)=-6x^2+260x.
\]

Ahora computemos
\[
F(x)=A'(x)B(x)-A(x)B'(x).
\]

## 18. Desarrollo de \(F\)

Para evitar signos engorrosos, factoricemos. Observemos que \(A(x)=x^2(3x^2-260x+4576)\). Intentemos factorizar \(3x^2-260x+4576\):

El discriminante:
\[
260^2-4\cdot3\cdot4576=67600-54912=12688.
\]
\[
\sqrt{12688}=? \quad 112^2=12544,\ 113^2=12769. 
\]
No es cuadrado perfecto. Así que no factoriza de forma simple.

\(B(x)=-2x^3+130x^2-28800\). Intentemos raíces: ¿\(x=16\)?
\[
-2\cdot4096+130\cdot256-28800=-8192+33280-28800=-3712.
\]

¿\(x=18\)?
\[
-2\cdot5832+130\cdot324-28800=-11664+42120-28800=1656.
\]

¿\(x=20\)?
\[
-2\cdot8000+130\cdot400-28800=-16000+52000-28800=7200.
\]

No hay raíces obvias.

Computemos \(F\) desarrollando.

\[
A'=12x^3-780x^2+9152x.
\]
\[
B=-2x^3+130x^2-28800.
\]

Producto \(A'B\):

Multiplicamos término a término:

- \(12x^3\cdot(-2x^3)=-24x^6\).
- \(12x^3\cdot130x^2=1560x^5\).
- \(12x^3\cdot(-28800)=-345600x^3\).
- \(-780x^2\cdot(-2x^3)=1560x^5\).
- \(-780x^2\cdot130x^2=-101400x^4\).
- \(-780x^2\cdot(-28800)=22464000x^2\).
- \(9152x\cdot(-2x^3)=-18304x^4\).
- \(9152x\cdot130x^2=1189760x^3\).
- \(9152x\cdot(-28800)=-263577600x\).

Sumamos \(A'B\):

Coeficiente de \(x^6\): \(-24\).

Coeficiente de \(x^5\): \(1560+1560=3120\).

Coeficiente de \(x^4\): \(-101400-18304=-119704\).

Coeficiente de \(x^3\): \(-345600+1189760=844160\).

Coeficiente de \(x^2\): \(22464000\).

Coeficiente de \(x\): \(-263577600\).

Término constante: \(0\).

Entonces,
\[
A'B = -24x^6+3120x^5-119704x^4+844160x^3+22464000x^2-263577600x.
\]

Ahora \(A B'\):

\[
A=3x^4-260x^3+4576x^2.
\]
\[
B'=-6x^2+260x.
\]

Multiplicamos:

- \(3x^4\cdot(-6x^2)=-18x^6\).
- \(3x^4\cdot260x=780x^5\).
- \(-260x^3\cdot(-6x^2)=1560x^5\).
- \(-260x^3\cdot260x=-67600x^4\).
- \(4576x^2\cdot(-6x^2)=-27456x^4\).
- \(4576x^2\cdot260x=1189760x^3\).

Sumamos \(A B'\):

Coeficiente de \(x^6\): \(-18\).

Coeficiente de \(x^5\): \(780+1560=2340\).

Coeficiente de \(x^4\): \(-67600-27456=-95056\).

Coeficiente de \(x^3\): \(1189760\).

Coeficiente de \(x^2\): \(0\).

Coeficiente de \(x\): \(0\).

Término constante: \(0\).

Entonces,
\[
AB' = -18x^6+2340x^5-95056x^4+1189760x^3.
\]

## 19. Cálculo de \(F=A'B-AB'\)

Restamos:
\[
F=(-24x^6+3120x^5-119704x^4+844160x^3+22464000x^2-263577600x)
\]
\[
-(-18x^6+2340x^5-95056x^4+1189760x^3).
\]

Coeficiente de \(x^6\): \(-24-(-18)=-6\).

Coeficiente de \(x^5\): \(3120-2340=780\).

Coeficiente de \(x^4\): \(-119704-(-95056)=-24648\).

Coeficiente de \(x^3\): \(844160-1189760=-345600\).

Coeficiente de \(x^2\): \(22464000-0=22464000\).

Coeficiente de \(x\): \(-263577600-0=-263577600\).

Término constante: \(0\).

Entonces,
\[
F(x)=-6x^6+780x^5-24648x^4-345600x^3+22464000x^2-263577600x.
\]

Factor común \(x\):
\[
F(x)=x(-6x^5+780x^4-24648x^3-345600x^2+22464000x-263577600).
\]

Además, podemos sacar \(-6\) y quizá otros factores. Dividamos por \(-6\):
\[
F(x)=-6x\left(x^5-130x^4+4108x^3+57600x^2-3744000x+43929600\right).
\]

Revisemos los coeficientes:

- \(780/(-6)=-130\) ✓.
- \(-24648/(-6)=4108\) ✓.
- \(-345600/(-6)=57600\) ✓.
- \(22464000/(-6)=-3744000\) ✓.
- \(-263577600/(-6)=43929600\) ✓.

Así,
\[
F(x)=-6x\,G(x)
\]
donde
\[
G(x)=x^5-130x^4+4108x^3+57600x^2-3744000x+43929600.
\]

Notemos que la solución \(x=0\) de \(F=0\) no es admisible como punto crítico (pues \(g\) no está definida en \(x=0\), aunque la derivada sí tiende). Nos interesan las raíces positivas de \(G\).

## 20. Resolución de \(G(x)=0\)

Intentemos factorizar \(G\). Busquemos raíces racionales. Como el polinomio tiene coeficientes enteros y el coeficiente principal es 1, cualquier raíz racional es entera y divide a \(43929600\).

Probemos con valores que parecen relacionados con 8, 50, 72.

Calculemos \(G(8)\):

\[
8^5=32768,\quad 8^4=4096,\quad 8^3=512,\quad 8^2=64.
\]

\[
G(8)=32768-130\cdot4096+4108\cdot512+57600\cdot64-3744000\cdot8+43929600.
\]

\[
130\cdot4096=532480.
\]
\[
4108\cdot512=4108\cdot500+4108\cdot12=2054000+49296=2103296.
\]
\[
57600\cdot64=3686400.
\]
\[
3744000\cdot8=29952000.
\]

Sumamos:
\[
32768-532480+2103296+3686400-29952000+43929600.
\]

Agrupamos positivos: \(32768+2103296+3686400+43929600=49752064\).

Agrupamos negativos: \(-532480-29952000=-30484480\).

Restamos: \(49752064-30484480=19267584\neq0\).

\(G(8)\neq0\).

Probemos \(G(50)\):

\[
50^5=312500000,\quad 50^4=6250000,\quad 50^3=125000,\quad 50^2=2500.
\]

\[
G(50)=312500000-130\cdot6250000+4108\cdot125000+57600\cdot2500-3744000\cdot50+43929600.
\]

\[
130\cdot6250000=812500000.
\]
\[
4108\cdot125000=513500000.
\]
\[
57600\cdot2500=144000000.
\]
\[
3744000\cdot50=187200000.
\]

Sumamos:
\[
312500000-812500000+513500000+144000000-187200000+43929600.
\]

Agrupamos positivos: \(312500000+513500000+144000000+43929600=1013929600\).

Agrupamos negativos: \(-812500000-187200000=-999700000\).

Restamos: \(1013929600-999700000=14229600\neq0\).

\(G(50)\neq0\).

Probemos \(G(72)\):

\[
72^5,\ 72^4,\ldots
\]

Esto se vuelve laborioso. Mejor factoricemos \(G\) con ayuda de las raíces de \(P\).

## 21. Cambio de enfoque: usar la condición en las raíces de \(P\)

En lugar de resolver \(F=0\), podemos imponer condiciones en las raíces de \(P\) para que sean puntos de mínimo y el mínimo se alcance dos veces.

Cuando \(x=8,50,72\), la derivada \(g'(x)\) es proporcional a \(x-k\) (o \(k-x\)). Por tanto:

- Si \(x=8\), \(g'(8)=336(8-k)\).
- Si \(x=50\), \(g'(50)=\frac{462}{25}(k-50)\).
- Si \(x=72\), \(g'(72)=\frac{176}{9}(72-k)\).

Para que \(x=8\) sea un punto crítico, necesitamos \(k=8\). Para \(x=50\), \(k=50\). Para \(x=72\), \(k=72\).

Para que dos de estos puntos sean críticos a la vez, \(k\) tendría que ser dos valores distintos a la vez, imposible. Entonces, para \(k\notin\{8,50,72\}\), ninguno de \(8,50,72\) es punto crítico.

Por tanto, los dos puntos de mínimo deben ser puntos críticos que no son \(8,50,72\). Es decir, son raíces de \(Q\) que no son \(8,50,72\).

## 22. Número de puntos críticos

\(Q\) es de grado 4. Para \(k\) genérico, \(Q\) tiene hasta 4 raíces reales. Necesitamos que haya al menos dos raíces positivas que sean mínimos globales con el mismo valor.

Para \(k\) específicos, \(Q\) podría tener una raíz doble, reduciendo el número de puntos críticos. En ese caso, el mínimo podría alcanzarse exactamente dos veces.

## 23. Análisis de casos según el signo de \(k\)

Recordemos que \(g\to+\infty\) cuando \(x\to0^+\) y cuando \(x\to\infty\). La función \(g\) puede tener varios mínimos y máximos locales. El número de puntos críticos se determina por las raíces de \(Q\).

Como \(Q\) es de grado 4 y su coeficiente principal es \(3>0\), \(Q\to+\infty\) cuando \(x\to\pm\infty\). Las raíces reales de \(Q\) alternan signos de \(g'\) (a través de \(g' = Q/x^2\)).

Puntos críticos de \(g\): raíces positivas de \(Q\).

Para que \(g\) alcance el mínimo en exactamente dos puntos, debe haber exactamente dos puntos donde \(g\) tiene su mínimo global.

## 24. Caso especialmente simple: \(Q\) tiene raíz doble positiva

Si \(Q\) tiene una raíz doble en \(x_0>0\), la gráfica de \(g\) tiene una inflexión horizontal en \(x_0\), pero con dos puntos de mínimo? No, una raíz doble de \(Q\) no implica dos puntos de mínimo; significa que hay un único punto crítico degenerado.

Sin embargo, quizá el mínimo global se alcance en dos puntos porque la función tiene dos valles con el mismo valor, sin que \(Q\) tenga raíces dobles. En ese caso, la condición es \(g(x_1)=g(x_2)\) para dos raíces distintas de \(Q\).

Esto es más complicado algebraicamente.

## 25. Regreso al discriminante

El discriminante de \(Q\) detecta raíces dobles. Pero el problema pide valores de \(k\) para los que el mínimo se alcanza en dos puntos. Estos valores de \(k\) pueden no corresponder a raíces dobles de \(Q\).

Pensemos de nuevo. Supongamos que el mínimo global se alcanza en dos puntos \(x_1<x_2\). Entonces, localmente la función tiene la forma de dos valles. La derivada \(g'\) cambia de signo de negativo a positivo en cada uno de los puntos de mínimo.

Como \(g\to+\infty\) en los extremos, la derivada \(g'\) debe ser negativa a la derecha de \(0^+\) (pues \(g\) decrece desde \(+\infty\)), luego positiva en un máximo, negativa, positiva en un máximo, etc. El número de cambios de signo de \(g'\) determina los extremos.

Para que \(g\) tenga exactamente dos mínimos globales con el mismo valor, podría haber tres puntos críticos: los dos mínimos y un máximo local entre ellos.

Si \(Q\) tiene exactamente tres raíces positivas, \(g\) tiene tres puntos críticos: dos mínimos locales (en los extremos) y un máximo local. En este caso, el mínimo global es el menor de los dos mínimos locales. Para que ambos sean mínimos globales, deben tener el mismo valor.

Así, buscamos \(k\) tal que \(Q\) tenga tres raíces positivas y los valores de \(g\) en las dos raíces extremas sean iguales.

## 26. Igualdad de valores de \(g\) en dos puntos críticos

Sean \(x_1,x_2\) dos raíces de \(Q\) (puntos críticos) con \(g(x_1)=g(x_2)\). Entonces,

\[
\frac{(x_1-8)(x_1-50)(x_1-72)(x_1-k)}{x_1}
=
\frac{(x_2-8)(x_2-50)(x_2-72)(x_2-k)}{x_2}.
\]

Esto es una ecuación con \(k\). Podemos resolverla en términos de \(x_1,x_2\), y luego usar que ambos son raíces de \(Q\).

Este es el llamado problema de "tangentes dobles" o "mínimo doble".

## 27. Reescribamos \(g\) de forma conveniente

\[
g(x)=\frac{P(x)(x-k)}x = \frac{P(x)}x(x-k).
\]

Sea
\[
u(x)=\frac{P(x)}x = \frac{(x-8)(x-50)(x-72)}x.
\]

Entonces
\[
g(x)=u(x)(x-k)=xu(x)-ku(x).
\]

Derivada:
\[
g'(x)=u(x)+xu'(x)-ku'(x).
\]

Los puntos críticos satisfacen
\[
u(x)+(x-k)u'(x)=0.
\]

Esto quizá simplifique. Calculemos \(u(x)\):

\[
u(x)=\frac{x^3-130x^2+4576x-28800}{x}
=x^2-130x+4576-\frac{28800}{x}.
\]

Entonces,
\[
u'(x)=2x-130+\frac{28800}{x^2}.
\]

En un punto crítico:
\[
u(x)+(x-k)u'(x)=0.
\]

## 28. Igualdad en dos puntos críticos

Si \(x_1,x_2\) son puntos críticos con \(g(x_1)=g(x_2)\), entonces:

Para cada punto crítico, \(g(x)=u(x)(x-k)\). Además, la condición de punto crítico da:
\[
(x-k)u'(x)=-u(x).
\]

Sustituyendo \(x-k\) en \(g\):
\[
g(x)=u(x)\cdot\left(-\frac{u(x)}{u'(x)}\right)=-\frac{u(x)^2}{u'(x)}
\]
en el punto crítico (si \(u'(x)\neq0\)).

Entonces la condición \(g(x_1)=g(x_2)\) se reduce a
\[
\frac{u(x_1)^2}{u'(x_1)}=\frac{u(x_2)^2}{u'(x_2)}.
\]

Esto no depende explícitamente de \(k\).

Además, para cada punto crítico,
\[
k=x+\frac{u(x)}{u'(x)}.
\]

Si \(x_1,x_2\) son dos puntos críticos con el mismo valor de \(g\), entonces
\[
x_1+\frac{u(x_1)}{u'(x_1)}=x_2+\frac{u(x_2)}{u'(x_2)}.
\]

Definamos
\[
\phi(x)=x+\frac{u(x)}{u'(x)}.
\]

Entonces \(x_1,x_2\) deben satisfacer
\[
\phi(x_1)=\phi(x_2)
\]
y además
\[
\frac{u(x_1)^2}{u'(x_1)}=\frac{u(x_2)^2}{u'(x_2)}.
\]

Pero quizá hay una simplificación adicional. Notemos que
\[
\phi(x)=x+\frac{u(x)}{u'(x)}.
\]

Para la igualdad de \(g\), necesitamos \(u(x_1)(x_1-k)=u(x_2)(x_2-k)\). Con \(k=\phi(x_1)=\phi(x_2)\).

## 29. Relación entre las raíces de \(u'\) y los puntos de tangencia

Calculemos \(u'(x)=0\):
\[
2x-130+\frac{28800}{x^2}=0.
\]

Multiplicamos por \(x^2\):
\[
2x^3-130x^2+28800=0.
\]

Dividiendo entre 2:
\[
x^3-65x^2+14400=0.
\]

Intentemos factorizar. Probemos \(x=40\):
\[
64000-65\cdot1600+14400=64000-104000+14400=-25600.
\]

Probemos \(x=45\):
\[
91125-65\cdot2025+14400=91125-131625+14400=-26100.
\]

Probemos \(x=48\):
\[
110592-65\cdot2304+14400=110592-149760+14400=-24768.
\]

Probemos \(x=36\):
\[
46656-65\cdot1296+14400=46656-84240+14400=-23184.
\]

Probemos \(x=30\):
\[
27000-65\cdot900+14400=27000-58500+14400=-17100.
\]

Probemos \(x=20\):
\[
8000-65\cdot400+14400=8000-26000+14400=-3600.
\]

Probemos \(x=18\):
\[
5832-65\cdot324+14400=5832-21060+14400=-828.
\]

Probemos \(x=17\):
\[
4913-65\cdot289+14400=4913-18785+14400=528.
\]

Así que hay una raíz entre 17 y 18. Probemos \(x=60\):
\[
216000-65\cdot3600+14400=216000-234000+14400=-3600.
\]

Probemos \(x=64\):
\[
262144-65\cdot4096+14400=262144-266240+14400=10304.
\]

Así que hay una raíz entre 60 y 64. Probemos \(x=61\):
\[
226981-65\cdot3721+14400=226981-241865+14400=-484.
\]

Probemos \(x=62\):
\[
238328-65\cdot3844+14400=238328-249860+14400=2868.
\]

Entonces hay una raíz entre 61 y 62.

Probemos \(x=8\):
\[
512-65\cdot64+14400=512-4160+14400=10752.
\]

Probemos \(x=10\):
\[
1000-65\cdot100+14400=1000-6500+14400=8900.
\]

Probemos \(x=12\):
\[
1728-65\cdot144+14400=1728-9360+14400=6768.
\]

Probemos \(x=14\):
\[
2744-65\cdot196+14400=2744-12740+14400=4404.
\]

Probemos \(x=16\):
\[
4096-65\cdot256+14400=4096-16640+14400=1856.
\]

Probemos \(x=15\):
\[
3375-65\cdot225+14400=3375-14625+14400=3150.
\]

Así que la raíz negativa o pequeña... En realidad, \(u'(x)\) puede tener tres raíces reales. Veamos \(x\) negativo: \(x^3-65x^2+14400=0\). Para \(x=0\), positivo. Para \(x\to-\infty\), tiende a \(-\infty\). Para \(x\) negativo grande, \(-65x^2\) domina, así que es negativo. En \(x=0\) es \(14400>0\). Entonces hay una raíz negativa.

Para \(x\) positivo, hay dos raíces: una entre 17 y 18, y otra entre 61 y 62. Estas son las raíces positivas de \(u'\).

## 30. Significado geométrico

Las raíces de \(u'\) corresponden a los puntos críticos de \(u(x)=\frac{P(x)}x\), que a su vez corresponden a los puntos críticos de \(g\) para \(k\) tales que... en realidad \(g'=u+(x-k)u'\). En un punto crítico de \(g\), \(k=\phi(x)=x+u/u'\).

Cuando \(u'(x)=0\), \(\phi\) diverge, lo que indica que \(g'=0\) solo si \(u(x)=0\), es decir, en \(x=8,50,72\) con \(k\) correspondiente. Esto es coherente.

## 31. Valores particulares de \(k\)

Para que el mínimo se alcance en dos puntos, es natural que esos dos puntos sean dos de las raíces de \(P\) (es decir, dos de \(8,50,72\)) cuando el valor de \(g\) en ambos es el mismo y es el mínimo global. Como \(g(8)=g(50)=g(72)=0\), el valor \(0\) sería el mínimo global, pero entonces también \(g(k)=0\). Para que el mínimo se alcance exactamente en dos puntos, necesitamos que exactamente dos de los cuatro valores \(8,50,72,k\) aporten mínimos, y que no haya más puntos con valor \(0\) ni valores negativos.

Si \(k\) no está entre las raíces \(8,50,72\) de tal forma que \(g\) tome valores negativos, entonces el mínimo es \(0\) y se alcanza en las cuatro raíces si \(k\) es distinto de ellas (cuatro puntos), o en tres si \(k\) coincide con una de ellas (pero entonces una raíz es doble). Esto sugiere que para ciertos valores de \(k\), la función no toma valores negativos, y el mínimo \(0\) se alcanza en exactamente dos puntos.

Por ejemplo, si \(k\) está fuera del intervalo \([8,72]\) y en un lado tal que \(h(x)\ge0\) para todo \(x>0\), entonces \(g(x)\ge0\) y el mínimo \(0\) se alcanza en las raíces de \(h\).

Veamos los signos de \(h(x)=(x-8)(x-50)(x-72)(x-k)\) para \(x>0\).

Los factores \(x-8,x-50,x-72\) se anulan en \(8,50,72\), respectivamente. Sus signos:

- \(x<8\): \(x-8<0\), \(x-50<0\), \(x-72<0\) → producto negativo.
- \(8<x<50\): \(x-8>0\), \(x-50<0\), \(x-72<0\) → producto positivo.
- \(50<x<72\): \(x-8>0\), \(x-50>0\), \(x-72<0\) → producto negativo.
- \(x>72\): los tres positivos → producto positivo.

Es decir, \(P(x)=(x-8)(x-50)(x-72)\) tiene signos: negativo, positivo, negativo, positivo en los intervalos \((0,8),(8,50),(50,72),(72,\infty)\).

Multiplicando por \(x-k\), el signo de \(h=P(x)(x-k)\) depende de la ubicación de \(k\).

Para que \(g=h/x\ge0\) en todo \(x>0\), necesitamos \(h\ge0\) en todo \(x>0\).

Caso \(k\le8\): el factor \(x-k\ge0\) en \((0,\infty)\) si \(k\le0\)? No, si \(k>0\), para \(x<k\), \(x-k<0\).

Veamos caso por caso.

### Caso \(k\ge72\):

Entonces \(x-k<0\) para \(x<k\).

- En \((0,8)\): \(P<0\), \(x-k<0\) → \(h>0\).
- En \((8,50)\): \(P>0\), \(x-k<0\) → \(h<0\).
- En \((50,72)\): \(P<0\), \(x-k<0\) → \(h>0\).
- En \((72,k)\): \(P>0\), \(x-k<0\) → \(h<0\).
- En \((k,\infty)\): \(P>0\), \(x-k>0\) → \(h>0\).

Así que \(h\) es negativo en \((8,50)\) y en \((72,k)\). Entonces \(g\) toma valores negativos en esos intervalos. El mínimo global es negativo y se alcanza en dos puntos? Potencialmente, hay dos valles: uno en \((8,50)\) y otro en \((72,k)\). Si sus mínimos locales son iguales, el mínimo global se alcanza en dos puntos.

### Caso \(50<k<72\):

- En \((0,8)\): \(P<0\), \(x-k<0\) (pues \(x<8<50<k\)) → \(h>0\).
- En \((8,50)\): \(P>0\), \(x-k<0\) → \(h<0\).
- En \((50,k)\): \(P<0\), \(x-k<0\) → \(h>0\).
- En \((k,72)\): \(P<0\), \(x-k>0\) → \(h<0\).
- En \((72,\infty)\): \(P>0\), \(x-k>0\) → \(h>0\).

Así que \(h<0\) en \((8,50)\) y en \((k,72)\). De nuevo hay dos valles donde \(g<0\). El mínimo global se alcanza en dos puntos si los mínimos locales en ambos intervalos son iguales.

### Caso \(8<k<50\):

- En \((0,8)\): \(P<0\), \(x-k<0\) (pues \(x<8<k\)) → \(h>0\).
- En \((8,k)\): \(P>0\), \(x-k<0\) → \(h<0\).
- En \((k,50)\): \(P>0\), \(x-k>0\) → \(h>0\).
- En \((50,72)\): \(P<0\), \(x-k>0\) → \(h<0\).
- En \((72,\infty)\): \(P>0\), \(x-k>0\) → \(h>0\).

Aquí \(h<0\) en \((8,k)\) y en \((50,72)\). Dos valles.

### Caso \(k<8\):

- En \((0,k)\): \(P<0\), \(x-k<0\) → \(h>0\).
- En \((k,8)\): \(P<0\), \(x-k>0\) → \(h<0\).
- En \((8,50)\): \(P>0\), \(x-k>0\) → \(h>0\).
- En \((50,72)\): \(P<0\), \(x-k>0\) → \(h<0\).
- En \((72,\infty)\): \(P>0\), \(x-k>0\) → \(h>0\).

Aquí \(h<0\) en \((k,8)\) y en \((50,72)\). Dos valles.

En todos los casos, \(h\) es negativo en exactamente dos intervalos, y \(g\) tiene dos valles donde es negativa. El mínimo global es el menor de los dos mínimos locales.

## 32. Condición de mínimo doble global

Para que el mínimo se alcance en exactamente dos puntos, los dos mínimos locales deben ser iguales, es decir, el valor mínimo de \(g\) en el primer valle debe ser igual al valor mínimo en el segundo valle.

Debido a la simetría de la estructura, los tres valores de \(k\) surgirán de las tres maneras en que \(k\) se puede colocar para generar dos valles con mínimos iguales.

Notemos la simetría: los intervalos donde \(h<0\) siempre son dos, y las raíces que los delimitan son entre \(8,50,72,k\). Por ejemplo, en el caso \(k\ge72\), los valles son \((8,50)\) y \((72,k)\). El primer valle es fijo, y el segundo depende de \(k\). Ajustando \(k\), igualamos los mínimos.

En el caso \(50<k<72\), los valles son \((8,50)\) y \((k,72)\). De nuevo, el primero fijo.

En el caso \(8<k<50\), los valles son \((8,k)\) y \((50,72)\). El segundo fijo.

En el caso \(k<8\), los valles son \((k,8)\) y \((50,72)\). El segundo fijo.

Parece que siempre hay un valle fijo: \((8,50)\) o \((50,72)\). En el caso \(k\ge72\), el valle fijo es \((8,50)\); en \(50<k<72\), fijo \((8,50)\); en \(8<k<50\), fijo \((50,72)\); en \(k<8\), fijo \((50,72)\).

## 33. Enfoque mediante la condición de tangentes dobles

En lugar de perseguir el resultado algebraico general, propongo una forma elegante.

El mínimo doble de \(g\) ocurre cuando hay un valor \(m\) tal que \(g(x)=m\) tiene exactamente dos raíces dobles. Es decir, \(g(x)-m\) tiene dos raíces dobles \(x_1,x_2\), y sus otras dos raíces (complejas o reales) son mayores (no producen valores menores).

La ecuación \(g(x)=m\) para \(x>0\) se puede escribir como
\[
\frac{P(x)(x-k)}x=m
\]
o
\[
P(x)(x-k)=mx.
\]

Esta es una ecuación de grado 4 en \(x\), lineal en \(k\) y lineal en \(m\). Los \(k\) para los cuales esta ecuación tiene dos raíces dobles son precisamente los que buscamos, con \(m\) igual al mínimo.

La condición de dos raíces dobles significa que el polinomio
\[
P(x)(x-k)-mx
\]
es el cuadrado de un polinomio cuadrático multiplicado por una constante.

Es decir,
\[
(x-8)(x-50)(x-72)(x-k)-mx = C(x-\alpha)^2(x-\beta)^2
\]
para algún \(C\ne0\) y raíces \(\alpha,\beta>0\).

Comparando grados, \(C=1\) (el coeficiente de \(x^4\) es 1). Entonces,
\[
(x-8)(x-50)(x-72)(x-k)-mx=(x-\alpha)^2(x-\beta)^2.
\]

Para que el lado derecho sea exactamente un cuadrado de un cuadrático, el lado izquierdo debe ser un cuadrado perfecto de grado 4.

Reescribamos el lado izquierdo:
\[
P(x)(x-k)-mx=(x-k)P(x)-mx.
\]

Queremos que esto sea un cuadrado. Esto impone que el discriminante del polinomio de grado 4 sea cero (dos raíces dobles), y además que el término \(mx\) ajuste las raíces para que sean dobles.

## 34. Condición de cuadrado perfecto

Para que \(P(x)(x-k)-mx\) sea un cuadrado perfecto \((x-\alpha)^2(x-\beta)^2\), el polinomio debe tener la forma
\[
x^4 - (130+k)x^3 + (4576+130k)x^2 - (28800+4576k+m)x + 28800k.
\]

Si esto es igual a \((x^2+px+q)^2=x^4+2px^3+(p^2+2q)x^2+2pqx+q^2\), entonces:

Coeficiente de \(x^3\):
\[
2p=-(130+k).
\]

Coeficiente de \(x^2\):
\[
p^2+2q=4576+130k.
\]

Coeficiente de \(x\):
\[
2pq=-(28800+4576k+m).
\]

Término constante:
\[
q^2=28800k.
\]

Tenemos también la condición de que las raíces \(\alpha,\beta\) sean reales positivas, lo que implica \(p<0\) y \(q>0\), y el discriminante \(p^2-4q\ge0\). Pero primero resolvamos las ecuaciones.

De \(q^2=28800k\), como \(k>0\), \(q>0\) o \(q<0\). Para que \(g\) tenga mínimo negativo, \(m<0\), y esto suele corresponder a \(q>0\) o \(q<0\) dependiendo. Sigamos.

Sea \(q=\sqrt{28800k}\) o \(q=-\sqrt{28800k}\). Probemos con \(q>0\).

De \(2p=-(130+k)\):
\[
p=-\frac{130+k}2.
\]

Sustituimos en la ecuación de \(x^2\):
\[
\left(\frac{130+k}2\right)^2+2q=4576+130k.
\]

Multiplicamos por 4:
\[
(130+k)^2+8q=18304+520k.
\]

\[
16900+260k+k^2+8q=18304+520k.
\]

\[
k^2-260k+8q-1404=0.
\]

Sustituimos \(q=\sqrt{28800k}\). Entonces,
\[
k^2-260k+8\sqrt{28800k}-1404=0.
\]

Esta ecuación es complicada, pero podemos usar la ecuación del coeficiente de \(x\) también.

Coeficiente de \(x\):
\[
2pq=-(28800+4576k+m).
\]

Con \(p=-\frac{130+k}2\) y \(q\):
\[
-q(130+k)=-(28800+4576k+m).
\]

\[
m=28800+4576k-q(130+k).
\]

Además, el valor \(m\) es el mínimo de \(g\), y en los puntos \(x=\alpha,\beta\), \(g=m\).

## 35. Posibilidad alternativa: \(q<0\)

Si \(q=-\sqrt{28800k}\), similar. Probemos ambos casos numéricamente más tarde.

## 36. Intentemos resolver la ecuación para \(k\)

Retomemos
\[
k^2-260k+8q-1404=0
\]
con \(q=\sqrt{28800k}\).

Elevar al cuadrado para eliminar la raíz puede introducir soluciones extrañas, pero avanzaremos.

Sea \(r=\sqrt{k}\), \(k=r^2\). Entonces \(q=\sqrt{28800}r\).

\[
r^4-260r^2+8\sqrt{28800}\,r-1404=0.
\]

\[
\sqrt{28800}=\sqrt{288\cdot100}=10\sqrt{288}=10\cdot12\sqrt2? 
\]
\[
288=144\cdot2,\quad \sqrt{288}=12\sqrt2.
\]
Así,
\[
\sqrt{28800}=120\sqrt2.
\]

Entonces \(8\sqrt{28800}=960\sqrt2\).

Ecuación:
\[
r^4-260r^2+960\sqrt2\,r-1404=0.
\]

Esta ecuación tiene coeficientes irracionales. Las soluciones para \(r\) serán de la forma \(\sqrt{k}\). Hmm.

Alternativamente, quizá hay una factorización más limpia.

## 37. Enfoque numérico iterativo

En lugar de resolver simbólicamente la ecuación con radicales, usemos el hecho de que los valores de \(k\) son probablemente enteros o racionales simples. El problema probablemente tiene una respuesta entera.

Los tres valores de \(k\) probablemente son las tres raíces de un polinomio cúbico con raíces enteras o racionales. La suma pedida podría ser un número entero.

Hagamos una prueba numérica. Podemos usar Python para encontrar los valores de \(k\) donde los dos mínimos locales de \(g\) coinciden. Esto es un método de bisección.

## 38. Uso de Python para hallar los valores de \(k\)

Voy a escribir un código que, para un \(k\) dado, localice los dos mínimos locales de \(g\) y compare sus valores. Luego busque los \(k\) donde la diferencia es cero.

Necesitamos ubicar los intervalos donde \(g<0\). Como discutimos, hay dos intervalos para cada \(k>0\). Localicemos numéricamente los mínimos.

Por ejemplo, para \(k=100\) (caso \(k>72\)): los valles en \((8,50)\) y \((72,100)\).

Para \(k=60\) (caso \(50<k<72\)): valles en \((8,50)\) y \((60,72)\).

Para \(k=30\) (caso \(8<k<50\)): valles en \((8,30)\) y \((50,72)\).

Para \(k=4\) (caso \(k<8\)): valles en \((4,8)\) y \((50,72)\).

Busquemos los \(k\) donde los mínimos locales coinciden.

## 39. Implementación numérica

Escribamos código para buscar los \(k\).

```python
import mpmath as mp

def g(x, k):
    return (x-8)*(x-50)*(x-72)*(x-k)/x

def gprime(x, k):
    # Derivada
    return 3*x**2 - 2*(130+k)*x + (4576+130*k) - 28800*k/x**2

def find_local_min_in_interval(a, b, k):
    # Encontrar raíz de gprime en [a,b] donde g es mínima
    # Buscar raíz de gprime
    f = lambda x: gprime(x, k)
    # bisección
    fa = f(a); fb = f(b)
    # Si no hay cambio de signo, buscar por muestreo
    x = mp.findroot(f, [(a+b)/2], method='bisection')
    return x

# Para cada caso
```

Mejor usar un método robusto. Usemos `mp.findroot` con la derivada numérica.

Voy a ejecutar una búsqueda.

## 40. Ejecutemos el código

Voy a usar el entorno para ejecutar Python y buscar los valores.

```python
import scipy.optimize as opt
import numpy as np

def g(x, k):
    return (x-8)*(x-50)*(x-72)*(x-k)/x

def gprime(x, k):
    return 3*x**2 - 2*(130+k)*x + (4576+130*k) - 28800*k/x**2

def local_min_in(a, b, k):
    # minimización de g en [a,b]
    xs = np.linspace(a, b, 1000)
    vals = g(xs, k)
    idx = np.argmin(vals)
    # refinar
    res = opt.minimize_scalar(lambda x: g(x,k), bounds=(a,b), method='bounded')
    return res.x, res.fun

def diff(k, interval1, interval2):
    x1, v1 = local_min_in(*interval1, k)
    x2, v2 = local_min_in(*interval2, k)
    return v1 - v2, (x1, v1, x2, v2)

# Buscar en cada caso
```

Ejecutemos para distintos intervalos.

## 41. Búsqueda de los tres \(k\)

### Caso \(k>72\): valles \((8,50)\) y \((72,k)\)

Aquí el segundo valle es \((72,k)\), que depende de \(k\). El primer valle \((8,50)\) es fijo.

Definamos \(D(k)=g(x_1^*)-g(x_2^*)\), con \(x_1^*\) mínimo en \((8,50)\) y \(x_2^*\) mínimo en \((72,k)\).

Busquemos \(k>72\) donde \(D(k)=0\).

### Caso \(50<k<72\): valles \((8,50)\) y \((k,72)\)

### Caso \(8<k<50\): valles \((8,k)\) y \((50,72)\)

### Caso \(k<8\): valles \((k,8)\) y \((50,72)\)

Ejecutemos.

## 42. Código Python

Voy a escribir y ejecutar el código para obtener los valores.

```python
import scipy.optimize as opt
import numpy as np

def g(x,k):
    return (x-8)*(x-50)*(x-72)*(x-k)/x

def local_min(a,b,k):
    # mínimo de g en (a,b)
    res = opt.minimize_scalar(g, args=(k,), bounds=(a,b), method='bounded')
    return res.x, res.fun

def D_caso1(k):
    # k>72: valles (8,50) y (72,k)
    _, v1 = local_min(8,50,k)
    _, v2 = local_min(72,k,k)
    return v1-v2

# etc.
```

Potencial problema: `minimize_scalar` con `args=(k,)` debe pasarse así. Revisar.

Ejecutaré el código en el entorno.

## 43. Ejecución real

Voy a usar la herramienta para ejecutar Python y obtener los resultados numéricos.

Voy a escribir un script completo.

```python
import numpy as np
from scipy.optimize import minimize_scalar, brentq

def g(x, k):
    return (x-8)*(x-50)*(x-72)*(x-k)/x

def local_min(a, b, k):
    res = minimize_scalar(g, args=(k,), bounds=(a, b), method='bounded')
    return res.x, res.fun

def diferencias(k):
    # k>72
    _, v1 = local_min(8, 50, k)
    _, v2 = local_min(72, k, k)
    return v1 - v2
```

Busquemos raíces de `diferencias(k)` para cada caso.

## 44. Resultado esperado

Probablemente los tres valores de \(k\) son las raíces de un polinomio cúbico. La suma podría ser \(130\) o algo relacionado. De hecho, \(8+50+72=130\). Quizá los tres valores de \(k\) sean \(8,50,72\)? Pero ya vimos que no son esos.

Quizá la suma es \(130\). O quizá los valores son \(8,50,72\) en algún sentido transformado. Veamos.

Si la respuesta es \(130\), tendría una explicación elegante. Pero necesito verificar numéricamente.

Ejecutemos.

## 45. Código y ejecución

Voy a solicitar al entorno que ejecute Python.

```python
import numpy as np
from scipy.optimize import minimize_scalar, brentq

def g(x, k):
    return (x-8)*(x-50)*(x-72)*(x-k)/x

def local_min(a, b, k):
    res = minimize_scalar(g, args=(k,), bounds=(a, b), method='bounded')
    return res.x, res.fun

# Caso 1: k>72, valles (8,50) y (72,k)
def D1(k):
    _, v1 = local_min(8, 50, k)
    _, v2 = local_min(72, k, k)
    return v1 - v2

# Encontrar raíz de D1 en (72, 200)
k1 = brentq(D1, 72.001, 200)
print("k1 =", k1)
_, v1 = local_min(8, 50, k1)
_, v2 = local_min(72, k1, k1)
print("v1 =", v1, "v2 =", v2)

# Caso 2: 50<k<72, valles (8,50) y (k,72)
def D2(k):
    _, v1 = local_min(8, 50, k)
    _, v2 = local_min(k, 72, k)
    return v1 - v2

k2 = brentq(D2, 50.001, 71.999)
print("k2 =", k2)
_, v1 = local_min(8, 50, k2)
_, v2 = local_min(k2, 72, k2)
print("v1 =", v1, "v2 =", v2)

# Caso 3: 8<k<50, valles (8,k) y (50,72)
def D3(k):
    _, v1 = local_min(8, k, k)
    _, v2 = local_min(50, 72, k)
    return v1 - v2

k3 = brentq(D3, 8.001, 49.999)
print("k3 =", k3)
_, v1 = local_min(8, k3, k3)
_, v2 = local_min(50, 72, k3)
print("v1 =", v1, "v2 =", v2)

# Caso 4: k<8, valles (k,8) y (50,72)
def D4(k):
    _, v1 = local_min(k, 8, k)
    _, v2 = local_min(50, 72, k)
    return v1 - v2

# Intentar encontrar raíz en (0,8)
try:
    k4 = brentq(D4, 0.001, 7.999)
    print("k4 =", k4)
    _, v1 = local_min(k4, 8, k4)
    _, v2 = local_min(50, 72, k4)
    print("v1 =", v1, "v2 =", v2)
except Exception as e:
    print("No hay raíz en (0,8):", e)

print("Suma:", k1+k2+k3)
```

Ejecutemos este código.

## 46. Resultados

Al ejecutar, esperamos obtener tres valores de \(k\). La suma se calcula al final.

Procedamos a ejecutar el código en el entorno.

## 47. Ejecución mediante herramienta

Voy a ejecutar el script Python usando mi entorno.

## 48. Nota sobre el entorno

El entorno tiene Python disponible con scipy quizá instalado. Si no, usaré solo numpy y métodos de bisección propios.

Voy a ejecutar.Voy a ejecutar un análisis numérico para encontrar los valores de \(k\).

```python
import numpy as np
from scipy.optimize import minimize_scalar, brentq

def g(x, k):
    return (x-8)*(x-50)*(x-72)*(x-k)/x

def local_min(a, b, k):
    res = minimize_scalar(g, args=(k,), bounds=(a, b), method='bounded')
    return res.x, res.fun

# Caso 1: k>72, valles (8,50) y (72,k)
def D1(k):
    _, v1 = local_min(8, 50, k)
    _, v2 = local_min(72, k, k)
    return v1 - v2

k1 = brentq(D1, 72.001, 200)
print("k1 =", k1)
x1, v1 = local_min(8, 50, k1)
x2, v2 = local_min(72, k1, k1)
print("x1 =", x1, "v1 =", v1, "x2 =", x2, "v2 =", v2)

# Caso 2: 50<k<72, valles (8,50) y (k,72)
def D2(k):
    _, v1 = local_min(8, 50, k)
    _, v2 = local_min(k, 72, k)
    return v1 - v2

k2 = brentq(D2, 50.001, 71.999)
print("k2 =", k2)
x1, v1 = local_min(8, 50, k2)
x2, v2 = local_min(k2, 72, k2)
print("x1 =", x1, "v1 =", v1, "x2 =", x2, "v2 =", v2)

# Caso 3: 8<k<50, valles (8,k) y (50,72)
def D3(k):
    _, v1 = local_min(8, k, k)
    _, v2 = local_min(50, 72, k)
    return v1 - v2

k3 = brentq(D3, 8.001, 49.999)
print("k3 =", k3)
x1, v1 = local_min(8, k3, k3)
x2, v2 = local_min(50, 72, k3)
print("x1 =", x1, "v1 =", v1, "x2 =", x2, "v2 =", v2)

# Caso 4: k<8, valles (k,8) y (50,72)
def D4(k):
    _, v1 = local_min(k, 8, k)
    _, v2 = local_min(50, 72, k)
    return v1 - v2

try:
    k4 = brentq(D4, 0.001, 7.999)
    print("k4 =", k4)
    x1, v1 = local_min(k4, 8, k4)
    x2, v2 = local_min(50, 72, k4)
    print("x1 =", x1, "v1 =", v1, "x2 =", x2, "v2 =", v2)
except Exception as e:
    print("No hay raíz en (0,8):", e)

print("Suma:", k1 + k2 + k3)
```