Numeremos las letras como \(A=1,\dots,L=12\). En cada pareja, la palabra tiene como primera letra la menor de las dos. Como las 6 primeras letras son todas distintas, la última palabra en orden alfabético es la pareja cuyo elemento menor es el mayor de los seis elementos menores.

Total de agrupaciones en pares:
\[
11\cdot 9\cdot 7\cdot 5\cdot 3\cdot 1=10395.
\]

Queremos que la pareja de “menor máximo” contenga a \(G=7\).

**Caso 1:** el menor máximo es \(F=6\), y su compañera es \(G\).
Entonces los menores son obligatoriamente \(\{1,2,3,4,5,6\}\) y las mayores \(\{7,\dots,12\}\). Para que la pareja \((6,7)\) sea la última, hay \(5!\) formas de emparejar el resto:
\[
5!=120.
\]

**Caso 2:** el menor máximo es \(G=7\).
Los menores son \(\{1,\dots,6\}\) menos un elemento \(r\), más el \(7\). Las mayores son \(\{8,9,10,11,12,r\}\). Para cada \(r\), la compañera de \(7\) debe elegirse entre \(\{8,\dots,12\}\): hay \(5\) opciones. Luego \(r\) debe emparejarse con alguno de los números \(1,2,\dots,r-1\): hay \(r-1\) opciones. Los restantes se emparejan de \(4!\) formas.

Entonces, para cada \(r\):
\[
5(r-1)4! = 120(r-1).
\]
Sumando \(r=1,\dots,6\):
\[
120(0+1+2+3+4+5)=120\cdot 15=1800.
\]

Casos favorables:
\[
120+1800=1920.
\]

Probabilidad:
\[
\frac{1920}{10395}=\frac{128}{693}.
\]

Por tanto \(m+n=128+693=821\).

\[
\boxed{821}
\]