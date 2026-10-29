## Planteamiento

Sea un octaedro regular con vértices

\[
(\pm a,0,0),\quad (0,\pm a,0),\quad (0,0,\pm a).
\]

Llamemos a los seis vértices

\[
V_1=(a,0,0),\quad V_2=(-a,0,0),\quad V_3=(0,a,0),\quad V_4=(0,-a,0),\quad V_5=(0,0,a),\quad V_6=(0,0,-a).
\]

Sea \(P=(x,y,z)\). Las distancias al cuadrado desde \(P\) a los seis vértices son:

\[
\begin{aligned}
d_1^2 &= (x-a)^2+y^2+z^2,\\
d_2^2 &= (x+a)^2+y^2+z^2,\\
d_3^2 &= x^2+(y-a)^2+z^2,\\
d_4^2 &= x^2+(y+a)^2+z^2,\\
d_5^2 &= x^2+y^2+(z-a)^2,\\
d_6^2 &= x^2+y^2+(z+a)^2.
\end{aligned}
\]

Observemos una identidad importante. Para cada par de vértices opuestos:

\[
d_1^2+d_2^2 = 2(x^2+y^2+z^2)+2a^2.
\]

De hecho, lo mismo vale para los tres pares opuestos:

\[
d_1^2+d_2^2=d_3^2+d_4^2=d_5^2+d_6^2.
\]

Es decir, **la suma de los cuadrados de las distancias a cada par de vértices opuestos es constante**.

---

## Uso de los datos

Las cinco distancias dadas son \(3,7,8,9,11\). La distancia desconocida la llamamos \(t\). Los seis números se agrupan en tres pares opuestos, y cada par debe tener la misma suma de cuadrados.

Primero notemos que no todas las distancias dadas pueden ir en pares que ya sumen lo mismo, porque la sexta debe acoplarse con una de ellas.

Probemos emparejar la distancia desconocida \(t\) con cada una de las dadas, exigiendo que las otras cuatro puedan agruparse en dos pares con la misma suma de cuadrados.

---

### Caso 1: \(t\) se empareja con \(3\)

Necesitamos que las cuatro distancias \(7,8,9,11\) se agrupen en dos pares con igual suma de cuadrados. Las posibles sumas son:

\[
7^2+8^2=113,\quad 9^2+11^2=202,
\]

\[
7^2+9^2=130,\quad 8^2+11^2=185,
\]

\[
7^2+11^2=170,\quad 8^2+9^2=145.
\]

Ninguna pareja de sumas coincide, así que este caso no funciona.

---

### Caso 2: \(t\) se empareja con \(7\)

Debemos agrupar \(3,8,9,11\) en dos pares con igual suma de cuadrados:

\[
3^2+8^2=73,\quad 9^2+11^2=202,
\]

\[
3^2+9^2=90,\quad 8^2+11^2=185,
\]

\[
3^2+11^2=130,\quad 8^2+9^2=145.
\]

Tampoco hay coincidencia.

---

### Caso 3: \(t\) se empareja con \(8\)

Debemos agrupar \(3,7,9,11\) en dos pares con igual suma de cuadrados:

\[
3^2+7^2=58,\quad 9^2+11^2=202,
\]

\[
3^2+9^2=90,\quad 7^2+11^2=170,
\]

\[
3^2+11^2=130,\quad 7^2+9^2=130.
\]

Aquí sí hay coincidencia:

\[
3^2+11^2=130=7^2+9^2.
\]

Por lo tanto, \(t\) debe cumplir

\[
t^2+8^2=130,
\]

de donde

\[
t^2=130-64=66,
\]

y así

\[
t=\sqrt{66}.
\]

---

### Caso 4: \(t\) se empareja con \(9\)

Debemos agrupar \(3,7,8,11\):

\[
3^2+7^2=58,\quad 8^2+11^2=185,
\]

\[
3^2+8^2=73,\quad 7^2+11^2=170,
\]

\[
3^2+11^2=130,\quad 7^2+8^2=113.
\]

No hay coincidencia.

---

### Caso 5: \(t\) se empareja con \(11\)

Debemos agrupar \(3,7,8,9\):

\[
3^2+7^2=58,\quad 8^2+9^2=145,
\]

\[
3^2+8^2=73,\quad 7^2+9^2=130,
\]

\[
3^2+9^2=90,\quad 7^2+8^2=113.
\]

No hay coincidencia.

---

## Conclusión

El único emparejamiento posible exige

\[
t^2=66.
\]

Por lo tanto, la distancia de \(P\) al sexto vértice es

\[
\boxed{\sqrt{66}}.
\]