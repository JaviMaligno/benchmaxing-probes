Voy a resolver el problema paso a paso.

Sea \(f(x)=px^2+qx+r\), con la condición \(|f(x)|\le 1\) para todo \(0\le x\le 2\).

Queremos maximizar \(|p|+|q|+|r|\).

## Paso 1: Condiciones en los puntos clave

Como \(|f(x)|\le 1\) en todo el intervalo, en particular en \(x=0,1,2\):

- \(f(0)=r\), luego \(|r|\le 1\).
- \(f(1)=p+q+r\), luego \(|p+q+r|\le 1\).
- \(f(2)=4p+2q+r\), luego \(|4p+2q+r|\le 1\).

## Paso 2: Buscar el máximo

La función \(g(x)=px^2+qx+r\) es convexa o cóncava según el signo de \(p\). En un intervalo, una cuadrática alcanza su máximo y mínimo en los extremos o en el vértice. Pero aquí los coeficientes pueden tener signos distintos, así que para maximizar \(|p|+|q|+|r|\) conviene probar configuraciones extremas.

Recordemos que canónicamente,

\[
f(x)=p\left(x+\frac{q}{2p}\right)^2 + \left(r-\frac{q^2}{4p}\right).
\]

Para que la cuadrática permanezca acotada en módulo por 1, sus valores en los extremos y en el vértice (si cae dentro de \([0,2]\)) deben estar en \([-1,1]\).

## Paso 3: Configuración que maximiza la suma de valores absolutos

Probemos con una parábola que pase por los extremos con valores elevados. La intuición sugiere que el máximo se alcanza cuando los valores en \(x=0,1,2\) son alternadamente \(+1\) y \(-1\), porque eso fuerza coeficientes grandes.

Caso: \(f(0)=1\), \(f(1)=-1\), \(f(2)=1\).

Entonces:
\[
r=1,
\]
\[
p+q+1=-1 \implies p+q=-2,
\]
\[
4p+2q+1=1 \implies 4p+2q=0 \implies 2p+q=0.
\]

Resolviendo:
De \(p+q=-2\) y \(2p+q=0\), restamos:
\[
(2p+q)-(p+q)=p=2,
\]
\[
q=-4.
\]

Así \(p=2,\ q=-4,\ r=1\). Suma:
\[
|p|+|q|+|r|=2+4+1=7.
\]

Verifiquemos que esta función cumple \(|f(x)|\le 1\) en \([0,2]\):

\[
f(x)=2x^2-4x+1=2(x-1)^2-1.
\]

Para \(x\in[0,2]\), \((x-1)^2\in[0,1]\), luego \(f(x)\in[-1,1]\). ¡Cumple!

## Paso 4: ¿Podemos exceder 7?

Probemos la otra configuración extrema: \(f(0)=-1\), \(f(1)=1\), \(f(2)=-1\).

\[
r=-1,
\]
\[
p+q-1=1 \implies p+q=2,
\]
\[
4p+2q-1=-1 \implies 4p+2q=0 \implies 2p+q=0.
\]

Restando: \(p=-2\), \(q=4\).

Suma: \(|p|+|q|+|r|=2+4+1=7\). Mismo resultado.

¿Configuraciones con \(f(0),f(1),f(2)\) en \(\pm 1\) con dos iguales y uno distinto? Por ejemplo \(f(0)=f(1)=1\), \(f(2)=-1\):

\[
r=1,
\]
\[
p+q=0,
\]
\[
4p+2q+1=-1 \implies 4p+2q=-2 \implies 2p+q=-1.
\]

Con \(q=-p\), \(2p-p=p=-1\), \(q=1\). Suma: \(1+1+1=3\).

Las otras configuraciones dan sumas menores.

## Paso 5: Justificación de optimalidad

Un enfoque sistemático: la cuadrática en \([0,2]\) está determinada por sus valores en tres puntos. Para maximizar \(|p|+|q|+|r|\), la bola unitaria del espacio de coeficientes debe ser lo más grande posible bajo la restricción de que el máximo en \([0,2]\) de \(|f|\) no exceda 1.

Mediante la fórmula de los coeficientes en términos de valores muestrales:

\[
r=f(0),
\]
\[
q=\frac{-3f(0)+4f(1)-f(2)}{2},
\]
\[
p=\frac{f(0)-2f(1)+f(2)}{2}.
\]

Queremos maximizar \(|r|+|q|+|p|\) sujeto a \(|f(0)|,|f(1)|,|f(2)|\le 1\) y a que el máximo en el intervalo no exceda 1.

El candidato \(p=2,q=-4,r=1\) alcanza 7. Por convexidad de la norma \(\ell^1\) y la linealidad de las restricciones, el máximo de una función lineal por tramos se alcanza en los vértices, que corresponden a extremos con valores \(\pm 1\). Probando todos los vértices factibles, ninguno supera 7. Por tanto,

\[
\boxed{7}
\]