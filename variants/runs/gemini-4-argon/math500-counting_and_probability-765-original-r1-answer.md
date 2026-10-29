Para resolver este problema, podemos utilizar el principio de inclusión-exclusión para tres conjuntos. 

Definamos los conjuntos de estudiantes según la materia que cursan:
* $C$: estudiantes que toman cálculo.
* $P$: estudiantes que toman física.
* $Q$: estudiantes que toman química.

De acuerdo con el enunciado, tenemos los siguientes datos:
* Total de estudiantes: $360$
* Estudiantes que no toman ninguna de las tres materias: $15$
* Estudiantes que toman las tres materias ($|C \cap P \cap Q|$): $15$
* Estudiantes que toman cálculo ($|C|$): $180$
* Estudiantes que toman química ($|Q|$): $2|P|$ (el doble de los que toman física)
* Estudiantes que toman cálculo y química ($|C \cap Q|$): $75$
* Estudiantes que toman física y química ($|P \cap Q|$): $75$
* Estudiantes que toman física y cálculo ($|P \cap C|$): $30$

**Paso 1: Calcular cuántos estudiantes toman al menos una de las tres materias.**
Restamos del total de estudiantes aquellos que no toman ninguna materia:
$$|C \cup P \cup Q| = 360 - 15 = 345$$

**Paso 2: Aplicar el principio de inclusión-exclusión.**
La fórmula para la unión de tres conjuntos es:
$$|C \cup P \cup Q| = |C| + |P| + |Q| - |C \cap P| - |C \cap Q| - |P \cap Q| + |C \cap P \cap Q|$$

Sustituimos los valores conocidos y reemplazamos $|Q|$ por $2|P|$:
$$345 = 180 + |P| + 2|P| - 30 - 75 - 75 + 15$$

**Paso 3: Despejar $|P|$.**
Agrupamos los términos semejantes en el lado derecho de la ecuación:
$$345 = 3|P| + (180 - 30 - 75 - 75 + 15)$$
$$345 = 3|P| + (180 - 180 + 15)$$
$$345 = 3|P| + 15$$

Restamos $15$ en ambos lados:
$$330 = 3|P|$$

Dividimos entre $3$:
$$|P| = \frac{330}{3} = 110$$

\boxed{110}