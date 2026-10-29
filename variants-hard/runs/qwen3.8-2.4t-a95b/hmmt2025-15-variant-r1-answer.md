Modelamos el museo como un grafo: las salas son vértices y las puertas son aristas.

Hay

\[
9\cdot 12+13\cdot 8=108+104=212
\]

puertas en total.

En un paseo cerrado sin repetir puertas, el conjunto de puertas usadas forma un subgrafo donde cada sala tiene grado par: cada vez que se entra a una sala, se sale de ella.

### Cota superior

Para cualquier conjunto de salas \(S\), el número de puertas usadas que cruzan de \(S\) a su complemento debe ser par, porque la suma de los grados pares en \(S\) cuenta dos veces las puertas internas y una vez las puertas que salen de \(S\).

Consideremos los cortes verticales entre la columna \(c\) y la columna \(c+1\), para \(c=1,\dots,12\). Cada uno de esos cortes tiene \(9\) puertas cruzándolo, una por fila. Como \(9\) es impar, no pueden usarse todas; al menos una puerta de cada corte vertical debe quedar sin usarse. Esto obliga a omitir al menos \(12\) puertas horizontales.

Análogamente, los cortes horizontales entre la fila \(r\) y la fila \(r+1\), para \(r=1,\dots,8\), tienen \(13\) puertas cruzándolos. Como \(13\) es impar, al menos una puerta de cada corte horizontal debe quedar sin usarse. Esto obliga a omitir al menos \(8\) puertas verticales.

Por tanto, deben omitirse al menos

\[
12+8=20
\]

puertas. Así, el número de puertas recorridas es a lo más

\[
212-20=192.
\]

### Construcción que alcanza 192

Numeremos las filas de \(1\) a \(9\) y las columnas de \(1\) a \(13\). Borramos exactamente estas \(20\) puertas:

- En la fila \(1\): entre columnas \(1\)-\(2\), \(3\)-\(4\), \(5\)-\(6\), \(7\)-\(8\), \(9\)-\(10\), \(11\)-\(12\).
- En la fila \(9\): entre columnas \(2\)-\(3\), \(4\)-\(5\), \(6\)-\(7\), \(8\)-\(9\), \(10\)-\(11\), \(12\)-\(13\).
- En la columna \(1\): entre filas \(1\)-\(2\), \(3\)-\(4\), \(5\)-\(6\), \(7\)-\(8\).
- En la columna \(13\): entre filas \(2\)-\(3\), \(4\)-\(5\), \(6\)-\(7\), \(8\)-\(9\).

Cada sala interior conserva todas sus puertas. Cada sala de la frontera que no es esquina pierde exactamente una puerta, y las esquinas pierden \(0\) o \(2\) puertas. Por tanto, todas las salas tienen grado par en el subgrafo restante. Además, salvo dos esquinas aisladas, el subgrafo es conexo, así que por el teorema de Euler existe un circuito cerrado que usa todas las puertas restantes.

Entonces se pueden recorrer

\[
212-20=192
\]

puertas.

\[
\boxed{192}
\]