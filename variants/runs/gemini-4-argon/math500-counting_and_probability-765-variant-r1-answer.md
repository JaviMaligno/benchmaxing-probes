Para resolver este problema, podemos utilizar el **principio de inclusión-exclusión** para tres conjuntos.

Definamos los conjuntos de estudiantes según las asignaturas que cursan:
* $C$: estudiantes que toman cálculo.
* $F$: estudiantes que toman física.
* $Q$: estudiantes que toman química.

De acuerdo con el enunciado, tenemos los siguientes datos:
* Total de estudiantes = $390$
* Estudiantes que no toman ninguna de las tres asignaturas = $20$
* Estudiantes que toman al menos una asignatura: $|C \cup F \cup Q| = 390 - 20 = 370$
* $|C| = 200$
* $|Q| = 2|F|$ (el doble de estudiantes toma química que física)
* $|C \cap Q| = 80$
* $|F \cap Q| = 80$
* $|F \cap C| = 35$
* $|C \cap F \cap Q| = 20$

Según el principio de inclusión-exclusión para tres conjuntos:
$$|C \cup F \cup Q| = |C| + |F| + |Q| - |C \cap Q| - |F \cap Q| - |F \cap C| + |C \cap F \cap Q|$$

Sustituimos los valores conocidos llamando $x = |F|$ al número de estudiantes que toman física (por lo que $|Q| = 2x$):
$$370 = 200 + x + 2x - 80 - 80 - 35 + 20$$

Simplificamos la ecuación:
$$370 = 200 + 3x - 175$$
$$370 = 25 + 3x$$
$$345 = 3x$$
$$x = \frac{345}{3} = 115$$

Por lo tanto, $115$ estudiantes toman física.

\boxed{115}