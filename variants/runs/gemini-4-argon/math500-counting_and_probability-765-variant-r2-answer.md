Para resolver este problema paso a paso, definamos los conjuntos de estudiantes según las materias que cursan:

* Sea $A$ el conjunto de estudiantes que toman cálculo.
* Sea $P$ el conjunto de estudiantes que toman física.
* Sea $C$ el conjunto de estudiantes que toman química.

A partir del enunciado, tenemos los siguientes datos:
1. Total de estudiantes: $390$
2. Estudiantes que no toman ninguna de las tres materias: $20$
3. Estudiantes que toman las tres materias ($|A \cap P \cap C|$): $20$
4. Estudiantes que toman cálculo ($|A|$): $200$
5. Estudiantes que toman química ($|C|$): $2|P|$ (el doble de los que toman física)
6. Estudiantes que toman cálculo y química ($|A \cap C|$): $80$
7. Estudiantes que toman física y química ($|P \cap C|$): $80$
8. Estudiantes que toman física y cálculo ($|A \cap P|$): $35$

**Paso 1: Encontrar el número de estudiantes que toman al menos una materia.**
Restamos del total de estudiantes aquellos que no toman ninguna materia:
$$|A \cup P \cup C| = 390 - 20 = 370$$

**Paso 2: Aplicar el principio de inclusión-exclusión.**
La fórmula para la unión de tres conjuntos es:
$$|A \cup P \cup C| = |A| + |P| + |C| - |A \cap P| - |A \cap C| - |P \cap C| + |A \cap P \cap C|$$

Sea $x = |P|$ el número de estudiantes que toman física. Entonces, el número de estudiantes que toman química es $|C| = 2x$. Sustituimos todos los valores conocidos en la fórmula:
$$370 = 200 + x + 2x - 35 - 80 - 80 + 20$$

**Paso 3: Resolver la ecuación para $x$.**
Agrupamos los términos semejantes:
$$370 = 3x + (200 - 35 - 80 - 80 + 20)$$
$$370 = 3x + 25$$

Restamos $25$ de ambos lados:
$$345 = 3x$$

Dividimos entre $3$:
$$x = \frac{345}{3} = 115$$

Por lo tanto, $115$ estudiantes toman física.

\boxed{115}