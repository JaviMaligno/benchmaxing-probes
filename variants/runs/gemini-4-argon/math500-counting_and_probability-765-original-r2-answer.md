Para resolver este problema, podemos utilizar el principio de inclusión-exclusión para tres conjuntos.

Definamos los conjuntos de estudiantes según las asignaturas que cursan:
* $C$: Cálculo
* $P$: Física (*Physics*)
* $Q$: Química (*Chemistry*)

Según los datos del problema, sabemos que:
* Total de personas en la escuela = $360$
* Estudiantes que no toman ninguna de las tres asignaturas = $15$
* Por lo tanto, el número total de estudiantes que toman al menos una asignatura es:
  $$|C \cup P \cup Q| = 360 - 15 = 345$$

También tenemos los siguientes datos:
* $|C \cap P \cap Q| = 15$ (toman las tres asignaturas)
* $|C| = 180$ (toman cálculo)
* $|Q| = 2|P|$ (el doble de estudiantes toma química en comparación con física)
* $|C \cap Q| = 75$ (toman cálculo y química)
* $|P \cap Q| = 75$ (toman física y química)
* $|P \cap C| = 30$ (toman física y cálculo)

Aplicamos la fórmula del principio de inclusión-exclusión:
$$|C \cup P \cup Q| = |C| + |P| + |Q| - |C \cap P| - |C \cap Q| - |P \cap Q| + |C \cap P \cap Q|$$

Sustituimos los valores conocidos en la ecuación:
$$345 = 180 + |P| + 2|P| - 30 - 75 - 75 + 15$$

Simplificamos los términos numéricos del lado derecho:
$$345 = 3|P| + (180 - 30 - 75 - 75 + 15)$$
$$345 = 3|P| + (180 - 180 + 15)$$
$$345 = 3|P| + 15$$

Restamos $15$ en ambos lados de la ecuación:
$$330 = 3|P|$$

Dividimos entre $3$:
$$|P| = 110$$

\boxed{110}