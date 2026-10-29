Analicemos el problema paso a paso.

**Total de disposiciones:** Fijemos las 5 posiciones del brazalete (posiciones etiquetadas). Como hay dos C, dos M y una I, el número de secuencias distintas de letras alrededor del brazalete es

$$\frac{5!}{2!\,2!} = 30,$$

y todas son igualmente probables (cada una corresponde a $2!\cdot 2! = 4$ colocaciones de las cuentas físicas).

**Disposiciones favorables:** Necesitamos contar cuántas de esas 30 secuencias etiquetadas se leen como "CMIMC" tras alguna rotación o reflexión. El grupo diédrico $D_5$ tiene 10 elementos (5 rotaciones y 5 reflexiones), así que a lo sumo hay 10 secuencias favorables, pero hay que descontar simetrías de la propia palabra.

La palabra cíclica $(C, M, I, M, C)$ es un palíndromo: al invertirla se obtiene $(C, M, I, M, C)$ de nuevo. Es decir, tiene una simetría de reflexión (el eje pasa por la I). No tiene simetría rotacional no trivial (ninguna rotación propia la deja igual, pues las letras no se repiten con período menor que 5).

Por lo tanto, el estabilizador de la palabra en $D_5$ tiene tamaño 2, y el número de secuencias etiquetadas distintas equivalentes a "CMIMC" es

$$\frac{10}{2} = 5.$$

**Probabilidad:**

$$P = \frac{5}{30} = \frac{1}{6}.$$

$$\boxed{\dfrac{1}{6}}$$