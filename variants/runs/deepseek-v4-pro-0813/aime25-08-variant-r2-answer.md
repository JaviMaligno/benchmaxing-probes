Vamos a resolver el problema paso a paso.

## 1. Interpretar la primera ecuación

La ecuación
\[
|20+15i-z|=13
\]
significa que \(z\) está a distancia \(13\) del punto \(20+15i\). Es decir, \(z\) está sobre la circunferencia de centro
\[
C=(20,15)
\]
y radio \(13\).

## 2. Interpretar la segunda ecuación

La segunda ecuación es
\[
|z-(12+k)|=|z-(5i+k)|.
\]
Aquí \(12+k\) y \(5i+k\) son dos números complejos. La ecuación dice que \(z\) equidista de estos dos puntos.

En el plano complejo, el lugar geométrico de los puntos que equidistan de dos puntos dados es la **mediatriz** del segmento que une ambos puntos.

Los dos puntos son:
\[
A=(k+12,0),\qquad B=(k,5).
\]
La mediatriz es la recta perpendicular al segmento \(AB\) por su punto medio.

El punto medio \(M\) es:
\[
M=\left(k+6,\frac52\right).
\]

El vector \(\overrightarrow{AB}=B-A=(-12,5)\). La mediatriz es perpendicular a \(AB\), así que su vector director es perpendicular a \((-12,5)\). Un vector perpendicular es \((5,12)\) (o cualquier múltiplo).

Por tanto, la mediatriz pasa por \(M=(k+6,5/2)\) y tiene dirección \((5,12)\).

Podemos parametrizar \(z\) sobre la mediatriz:
\[
z=(k+6,\tfrac52)+t(5,12),
\]
o en forma compleja,
\[
z=k+6+\frac52 i+t(5+12i).
\]

## 3. Condición de una única solución

El sistema tiene exactamente una solución compleja \(z\) cuando la circunferencia y la mediatriz se intersecan en un único punto. Es decir, la mediatriz es **tangente** a la circunferencia.

Esto ocurre cuando la distancia del centro \((20,15)\) a la mediatriz es exactamente el radio \(13\).

## 4. Distancia del centro a la mediatriz

La mediatriz pasa por \(M=(k+6,5/2)\) y tiene dirección \(d=(5,12)\).

La distancia desde \(C=(20,15)\) a la recta se calcula como:
\[
\text{dist}=\frac{|(C-M)\times d|}{|d|},
\]
donde \(\times\) denota el producto cruz en 2D.

Calculamos:
\[
C-M=\left(20-(k+6),\,15-\frac52\right)=\left(14-k,\,\frac{25}{2}\right).
\]

El producto cruz con \(d=(5,12)\) es:
\[
(C-M)\times d=(14-k)\cdot 12-\frac{25}{2}\cdot 5.
\]
Es decir,
\[
12(14-k)-\frac{125}{2}
=168-12k-\frac{125}{2}
=\frac{336-24k-125}{2}
=\frac{211-24k}{2}.
\]

La magnitud de \(d\) es:
\[
|d|=\sqrt{5^2+12^2}=\sqrt{169}=13.
\]

Por tanto, la distancia es:
\[
\text{dist}=\frac{\left|\frac{211-24k}{2}\right|}{13}
=\frac{|211-24k|}{26}.
\]

## 5. Condición de tangencia

Para tangencia,
\[
\frac{|211-24k|}{26}=13.
\]
Multiplicando por \(26\):
\[
|211-24k|=338.
\]

Esto da dos casos:
\[
211-24k=338
\quad\text{ó}\quad
211-24k=-338.
\]

### Caso 1:
\[
211-24k=338 \implies -24k=127 \implies k=-\frac{127}{24}.
\]

### Caso 2:
\[
211-24k=-338 \implies -24k=-549 \implies k=\frac{549}{24}=\frac{183}{8}.
\]

## 6. Suma de los posibles valores de \(k\)

\[
k_1+k_2=-\frac{127}{24}+\frac{183}{8}.
\]

Convertimos al denominador común \(24\):
\[
-\frac{127}{24}+\frac{183\cdot 3}{24}
=-\frac{127}{24}+\frac{549}{24}
=\frac{422}{24}
=\frac{211}{12}.
\]

La fracción \(\frac{211}{12}\) ya es irreducible porque \(211\) es primo y no divide a \(12\).

Entonces,
\[
m=211,\qquad n=12.
\]

## 7. Resultado final

\[
m+n=211+12=223.
\]

\[
\boxed{223}
\]