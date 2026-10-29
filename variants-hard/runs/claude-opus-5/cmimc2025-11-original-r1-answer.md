## Planteamiento

Las cinco cuentas se colocan al azar en las cinco posiciones del círculo. Como hay dos C iguales y dos M iguales, el número de disposiciones distinguibles en posiciones etiquetadas es

$$\frac{5!}{2!\,2!} = 30,$$

todas equiprobables.

## Cuántas sirven

Hay que contar las disposiciones que coinciden con CMIMC tras alguna rotación o reflexión, es decir, el tamaño de la órbita de CMIMC bajo el grupo diédrico $D_5$ (orden 10).

Por la fórmula órbita–estabilizador, basta hallar el estabilizador. Escribiendo las posiciones $1,\dots,5$ como C, M, I, M, C, la reflexión que fija la posición 3 (la I) intercambia $1\leftrightarrow 5$ (C con C) y $2\leftrightarrow 4$ (M con M), dejando la palabra invariante. La identidad y esa reflexión son las únicas simetrías que la fijan, así que el estabilizador tiene orden 2 y

$$|\text{órbita}| = \frac{10}{2} = 5.$$

Verificación por conteo directo: fijando la I y eligiendo las posiciones de las dos C entre las cuatro restantes, las órbitas tienen tamaños $10, 10, 5, 5$, que suman 30. CMIMC corresponde al caso con las dos C adyacentes entre sí (órbita de tamaño 5).

## Probabilidad

$$\frac{5}{30} = \frac{1}{6}$$

\boxed{\dfrac{1}{6}}